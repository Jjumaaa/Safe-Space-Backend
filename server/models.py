from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-_password_hash',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=True)   
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    recipes = relationship('Recipe', back_populates='user')

    @hybrid_property
    def password_hash(self):
        raise self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password.encode()).decode()

    def authenticate(self, password):
        return self._password_hash and bcrypt.check_password_hash(self._password_hash, password.encode())

    def __repr__(self):
        return f"<i am user number {self.id} and my name is {self.username} and my passwrd typshi is {self._password_hash} i love this photo {self.image_url} and yeah this is all about it {self.bio}>"
