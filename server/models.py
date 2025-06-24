from sqlalchemy.orm import validates, relationship, Foreignkey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt
from datetime import datetime

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-_password_hash',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, unique=True, nullable=True)
    password_hash = db.Column(db.String, nullable=True) 

    blogs = relationship("Blog", backref="users", cascade='all, delete-orphan')  

    
   
    @hybrid_property
    def password_hash(self):
        raise self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password.encode()).decode()

    def authenticate(self, password):
        return self._password_hash and bcrypt.check_password_hash(self._password_hash, password.encode())

    def __repr__(self):
        return f"<i am user number {self.id} and my name is {self.name} >"
    

class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String, nullable=False)
    created_at = db.column (db.String, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.Foreignkey("user.id)" ))

    tags = relationship("tags" )








  
  
  
  
  
  
   #user
   # #article
   # # tag
   # # articletags 




