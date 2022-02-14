import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import postgres


db_path = "postgresql://vojabfzacqpmcl:postgresql://postgres:locars.com@localhost:5432/Livre"

db = SQLAlchemy()


def setup_db(app, path=db_path):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
    db.create_all()


class Categorie(db.Model):

    __tablename__ = 'categorie'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50))
    livres = db.relationship('livres', backref='categorie', lazy=True)

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
            'id': self.id_livres,
            'code_ISBN': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'date_publication': self.date_publication
        }
