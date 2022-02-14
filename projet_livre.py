import os
from model import livres, categorie, setup_db, db
from flask_cors import CORS
from flask import Flask 
from flask import jsonify, request, abort
from flask_migrate import Migrate
from flask import SQLAlchemy  


app = Flask(__name__)  

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app,db) 


class Categorie(db.Model):

    __tablename__ = 'categorie'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50))
    books = db.relationship('livres', backref='categorie', lazy=True)

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


class Livres(db.Model):

    __tablename__ = 'livres'

    id_livres = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(12), nullable=False)
    titre = db.Column(db.String(200), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    auteur = db.Column(db.String(200), nullable=False)
    editeur = db.Column(db.String(150), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categorie.id_cat'), nullable=False)

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
            'id': self.id_livres,
            'code_ISBN': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'date_publication': self.date_publication
        }

        
#####################################################################################
#          Fonction permettant d'afficher les elemnent d'une liste
#####################################################################################


def paginate(request):
    donne = [donne.format() for donne in request]
    return donne


#################################################
#           Liste de tout les livres
#################################################



def create_app(test_config = None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-allow-Heaaders', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTION')
        return response



@app.route('/livres')
def get_livres():
    try:
        livres = livres.query.all()
        livres = paginate(livres)
        return jsonify ({
            'success': True,
            'statut_code': 200,
            'livres': livres,
            'total_livres': len(livres)
        })
    except:
        abort(404)
    finally:
        db.session.close()    



#################################################
#     Chercher un livre particulier par son id
#################################################


@app.route('/livres/<int:id>')
def get_livres(id):
    livres = livres.query.get(id)
    if livres is None:
        abort(404)
    else:
        return livres.format()    


#################################################
#   Lister la liste des livres d'une categorie
####################################################


@app.route('/categorie/<int:id>/livres')
def livres_categorie(id):
    try:
        categorie = categorie.query.get(id)
        livres = livres.query.filter_by(categorie_id=id).all()
        livres = paginate(livres)
        return jsonify (
            {
            'success': True,
            'statut_code': 200,
            'total': len(livres),
            'classse': categorie.format(),
            'livres': livres
                      }
            )
    except:
        abort (404)
    finally:
        db.sesssion.close()


#################################################
#   Lister toutes les categories
####################################################

@app.route('/categorie')
def get_categorie():
    categorie = categorie.query.all()
    categorie = paginate(categorie)
    if categorie is None:
        abort(404)
    else:
        return jsonify ({
            'success' : True,
            'status_code': 200,
            'categorie': categorie,
            'total': len(categorie)
        })


#################################################
#   Chercher une categorie par son id 
####################################################


@app.route('/categorie/<int:id>')
def get_categorie(id):
    categorie = categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()


#################################################
#            Supprimer un livre
#################################################

@app.route('/livres/<int:id', methods=['DELETE'])
def supp_livres(id):
    try:
        livres = livres.query.get(id)
        livres.delete()
        return jsonify({
            'success': True,
            'id_livres': id,
            'new_total': livres.query.count()
        })
    except:
        abort(404)
    finally:
        db.session.close()


#################################################
#            Supprimer une categorie
#################################################

@app.route('/categorie/<int:id', methods=['DELETE'])
def supp_livres(id):
    try:
        categorie = categorie.query.get(id)
        categorie.delete()
        return jsonify({
            'success': True,
            'id_livres': id,
            'new_total': categorie.query.count()
        })
    except:
        abort(404)
    finally:
        db.session.close()


#################################################
#     Modifier les informations d'un livre
#################################################


@app.route('/livres/<int:id', methods= ['PATCH'])
def change_livre(id):
    info = request.get_json()
    livres = livres.query.get(id)
    try:
        if 'titre' in info and 'auteur' in info and 'editeur' in info:
            livres.titre = info['titre']
            livres.auteur = info['auteur']
            livres.editeur = info['editeur']
        livres.update()
        return livres.format()
    except:
        abort(404)
    
#################################################
#      Modifier le libellé d'une categorie
#################################################

@app.route('/categorie/<int:id', methods=['PATCH'])    
def chang_name(id):
    info = request.get_json()
    categorie = categorie.query.get(id)
    try:
         if 'categorie' in info:
             categorie.libelle_categorie = info['categorie']
         categorie.update()
         return categorie.format()
    except:
        abort(404)


