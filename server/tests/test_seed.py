import unittest
from seed import seed
from config import db, create_app
from models import User, Blog, Tag

class TestSeedScript(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_seed_creates_data(self):
        
        seed()

       
        user_count = User.query.count()
        blog_count = Blog.query.count()
        tag_count = Tag.query.count()

        self.assertGreaterEqual(user_count, 1)
        self.assertGreaterEqual(blog_count, 1)
        self.assertGreaterEqual(tag_count, 1)

if __name__ == "__main__":
    unittest.main()
