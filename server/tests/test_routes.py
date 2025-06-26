import unittest
from app import app, db
from models import User

class RouteTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        
        self.user = User(username="testuser", email="test@example.com")
        self.user.password_hash = "testpassword"
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        response = self.app.post('/register', json={
            "username": "newuser",
            "email": "new@example.com",
            "password": "newpass"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("newuser", str(response.data))

if __name__ == '__main__':
    unittest.main()
