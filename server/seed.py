from faker import Faker
from config import db, create_app
from models import User, Blog, Tag
import random
from app import app

fake = Faker()
app = create_app()

def seed():
    with app.app_context():
        db.create_all()
        print("🌱 Seeding typshii...")

        # Clear tables
        Blog.query.delete()
        User.query.delete()
        Tag.query.delete()

        # Create users
        users = []
        for _ in range(15):
            user = User(
                username=fake.user_name(),
                email=fake.email()
            )
            user.password_hash = "password123"
            users.append(user)
            db.session.add(user)

        # Create tags
        tags = []
        for _ in range(15):
            tag = Tag(name=fake.word().capitalize())
            tags.append(tag)
            db.session.add(tag)

        db.session.commit()

        # Create blogs
        for _ in range(15):
            blog = Blog(
                title=fake.sentence(nb_words=5),
                image_url=fake.image_url(),
                bio=fake.paragraph(nb_sentences=3),
                user=random.choice(users),
                tags=random.sample(tags, k=random.randint(1, 3))
            )
            db.session.add(blog)

        db.session.commit()

        print("✅ Done seeding typshii!")

if __name__ == "__main__":
    seed()
