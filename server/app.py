from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from flask_restful import Api

from config import db
from models import User, Blog, Tag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.secret_key = 'shhh-very-secret'

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 409
    new_user = User(
        username=data['username'],
        email=data['email']
    )
    new_user.password_hash = data['password']
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.authenticate(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401


@app.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user.to_dict())


@app.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = Blog.query.all()
    return jsonify([blog.to_dict() for blog in blogs])


@app.route('/blogs/<int:id>', methods=['GET'])
def get_blog(id):
    blog = Blog.query.get_or_404(id)
    return jsonify(blog.to_dict())


@app.route('/blogs', methods=['POST'])
@jwt_required()
def create_blog():
    user_id = get_jwt_identity()
    data = request.json
    new_blog = Blog(
        title=data['title'],
        image_url=data.get('image_url'),
        bio=data['bio'],
        user_id=user_id
    )
    db.session.add(new_blog)
    db.session.commit()
    return jsonify(new_blog.to_dict()), 201


@app.route('/blogs/<int:id>', methods=['PATCH'])
@jwt_required()
def update_blog(id):
    user_id = get_jwt_identity()
    blog = Blog.query.get_or_404(id)
    if blog.user_id != user_id:
        return jsonify({"message": "Unauthorized"}), 403
    data = request.json
    if 'title' in data:
        blog.title = data['title']
    if 'bio' in data:
        blog.bio = data['bio']
    if 'image_url' in data:
        blog.image_url = data['image_url']
    db.session.commit()
    return jsonify(blog.to_dict())


@app.route('/blogs/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_blog(id):
    user_id = get_jwt_identity()
    blog = Blog.query.get_or_404(id)
    if blog.user_id != user_id:
        return jsonify({"message": "Unauthorized"}), 403
    db.session.delete(blog)
    db.session.commit()
    return jsonify({"message": "Blog deleted"}), 204


@app.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.to_dict() for tag in tags])


@app.route('/tags', methods=['POST'])
@jwt_required()
def create_tag():
    data = request.json
    new_tag = Tag(name=data['name'])
    db.session.add(new_tag)
    db.session.commit()
    return jsonify(new_tag.to_dict()), 201


@app.route('/tags/<int:id>', methods=['GET'])
def get_tag(id):
    tag = Tag.query.get_or_404(id)
    return jsonify(tag.to_dict())


@app.route('/tags/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_tag(id):
    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    return jsonify({"message": "Tag deleted"}), 204


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@app.route('/users/<int:id>/blogs', methods=['GET'])
def get_user_blogs(id):
    blogs = Blog.query.filter_by(user_id=id).all()
    return jsonify([blog.to_dict() for blog in blogs])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
