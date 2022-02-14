
from flask import Flask,jsonify,abort,request
from flask_migrate import Migrate
from flask_sqlalchemy import Pagination, SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:locars.com@localhost:5432/<Nom_De_Ta_base>"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Category(db.Model):

    __tablename__ = 'categories'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50))
    books = db.relationship('Book', backref='categories', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_cat,
            'categorie': self.libelle_categorie
        }


class Book(db.Model):

    __tablename__ = 'books'

    id_book = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(12), nullable=False)
    titre = db.Column(db.String(200), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    auteur = db.Column(db.String(200), nullable=False)
    editeur = db.Column(db.String(150), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id_cat'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_book,
            'code_ISBN': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'date_publication': self.date_publication
        }

def paginate(request):
    items = [item.format() for item in request]
    return items
def create_app(test_config=None):
    app = Flask(__name__)
    migrate = Migrate(app, db)
 
@app.after_request
def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

@app.route('/livres')
def get_books():
        try:
            books = Book.query.all()
            books = paginate(books)
            return jsonify({
                'success': True,
                'status_code': 200,
                'books': books,
                'total_books': len(books)
            })
        except:
            abort(404)
        finally:
            db.session.close()
            
@app.route('/livres/<int:id>')
def get_book(id):
        book = Book.query.get(id)
        if book is None:
            abort(404)
        else:
            return book.format()


@app.route('/categories/<int:id>/livres')
def book_category(id):
        try:
            category = Category.query.get(id)
            books = Book.query.filter_by(categorie_id=id).all()
            books = paginate(books)
            return jsonify({
                'Success': True,
                'Status_code': 200,
                'total': len(books),
                'classe': category.format(),
                'books': books
            })
        except:
            abort(404)
        finally:
            db.session.close()

@app.route('/categories')
def get_categories():
        categories = Category.query.all()
        categories = paginate(categories)
        if categories is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'status_code': 200,
                'category': categories,
                'total': len(categories)
            })

    ########################################
    # Chercher une categorie par son id
    ########################################

@app.route('/categories/<int:id>')
def get_category(id):
        category = Category.query.get(id)
        if category is None:
            abort(404)
        else:
            return category.format()

    ############################
    # Supprimer un livre
    ############################

@app.route('/livres/<int:id>', methods=['DELETE'])
def del_book(id):
        try:
            book = Book.query.get(id)
            book.delete()
            return jsonify({
                'success': True,
                'id_book': id,
                'new_total': Book.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

    #############################
    # Supprimer une categorie
    #############################

@app.route('/categories/<int:id>', methods=['DELETE'])
def del_category(id):
        try:
            category = Category.query.get(id)
            category.delete()
            return jsonify({
                'success': True,
                'status': 200,
                'id_cat': id,
                'new_total': Category.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

    ###########################################
    # Modifier les informations d'un livre
    ###########################################

@app.route('/livres/<int:id>', methods=['PATCH'])
def change_book(id):
        body = request.get_json()
        book = Book.query.get(id)
        try:
            if 'titre' in body and 'auteur' in body and 'editeur' in body:
                book.titre = body['titre']
                book.auteur = body['auteur']
                book.editeur = body['editeur']
            book.update()
            return book.format()
        except:
            abort(404)

    ########################################
    # Modifier le libellé d'une categorie
    ########################################

@app.route('/categories/<int:id>', methods=['PATCH'])
def change_name(id):
        body = request.get_json()
        category = Category.query.get(id)
        try:
            if 'categorie' in body:
                category.libelle_categorie = body['categorie']
            category.update()
            return category.format()
        except:
            abort(404)

    ##############################################
    # Rechercher un livre par son titre ou son auteur
    ##############################################
@app.route('/livres/<string:word>')
def search_book(word):
        mot = '%'+word+'%'
        titre = Book.query.filter(Book.titre.like(mot)).all()
        titre = paginate(titre)
        return jsonify({
            'books': titre
        })
	

@app.route('/livres', methods=['POST'])
def add_book():
        body = request.get_json()
        isbn = body['code_ISBN']
        new_titre = body['titre']
        new_date = body['date_publication']
        new_auteur = body['auteur']
        new_editeur = body['editeur']
        categorie_id = body['categorie_id']
        book = Book(isbn=isbn, titre=new_titre, date_publication=new_date,
                    auteur=new_auteur, editeur=new_editeur, categorie_id=categorie_id)
        book.insert()
        count = Book.query.count()
        return jsonify({
            'success': True,
            'added': book.format(),
            'total_books': count,
        })

@app.errorhandler(404)
def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Ressource non disponible"
        }), 404

        return app


app = create_app()

