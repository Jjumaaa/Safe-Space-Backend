import unittest
from config import db, create_app
from models import User, Blog, Tag

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username="primrose", email="primrose@example.com")
        user.password_hash = "password123"
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username="primrose").first()
        self.assertIsNotNone(retrieved_user)
        self.assertTrue(retrieved_user.authenticate("password123"))

    def test_tag_creation(self):
        tag = Tag(name="Flask")
        db.session.add(tag)
        db.session.commit()

        retrieved_tag = Tag.query.filter_by(name="Flask").first()
        self.assertIsNotNone(retrieved_tag)

    def test_blog_creation(self):
        user = User(username="writer", email="writer@example.com")
        user.password_hash = "pass123"
        db.session.add(user)
        db.session.commit()

        blog = Blog(
            title="Learning Flask",
            bio="Flask is great.",
            user=user
        )
        db.session.add(blog)
        db.session.commit()

        retrieved_blog = Blog.query.filter_by(title="Learning Flask").first()
        self.assertIsNotNone(retrieved_blog)
        self.assertEqual(retrieved_blog.user.username, "writer")

if __name__ == '__main__':
    unittest.main()
