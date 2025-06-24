from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt
from datetime import datetime

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-_password_hash', '-blogs.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, unique=True, nullable=True)
    _password_hash = db.Column(db.String, nullable=True) 

    blogs = relationship("Blog", backref="user", cascade='all, delete-orphan')  

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes are write-only.")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password.encode()).decode()

    def authenticate(self, password):
        return self._password_hash and bcrypt.check_password_hash(self._password_hash, password.encode())

    def __repr__(self):
        return f"<i am user number {self.id} and my name is {self.username} >"


class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'
    serialize_rules = ('-user.blogs', '-tags.blogs',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False, default=lambda: datetime.utcnow().isoformat())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    tags = relationship("Tag", secondary="article_tags", back_populates="blogs")


class Tag(db.Model, SerializerMixin):
    __tablename__ = 'tags'
    serialize_rules = ('-blogs.tags',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    blogs = relationship("Blog", secondary="article_tags", back_populates="tags")


article_tags = db.Table("article_tags",
    db.Column('blog_id', db.Integer, db.ForeignKey('blogs.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)
