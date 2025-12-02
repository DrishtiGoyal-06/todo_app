# seed.py
from flaskr import create_app
from flaskr.models.tag_model import TagModel
from flaskr.models.user_model import UserModel
from flaskr.db import db
from werkzeug.security import generate_password_hash # type: ignore

app = create_app()


def seed_tags():
    tag_names = [
        "Work", "Study", "Free Time", "Exercise", "Health", "Travel",
        "Hobbies", "Shopping", "Finances", "Family", "Chores", "Friends",
        "Meetings", "Goals", "Projects", "Learning", "Entertainment",
        "Relaxation", "Urgent", "Miscellaneous",
    ]

    with app.app_context():
        for tag_name in tag_names:
            try:
                # Only insert if not already in the DB
                if not TagModel.query.filter_by(name=tag_name).first():
                    db.session.add(TagModel(name=tag_name))
                    db.session.commit()
                    print(f"Inserted tag: {tag_name}")
            except Exception as err:
                db.session.rollback()
                print(f"Skipping duplicate or error for tag '{tag_name}': {err}")


def seed_users():
    users = [
        {"username": "alice", "email": "alice@example.com", "password": "password123"},
        {"username": "bob", "email": "bob@example.com", "password": "password123"},
        {"username": "charlie", "email": "charlie@example.com", "password": "password123"},
        {"username": "dave", "email": "dave@example.com", "password": "password123"},
        {"username": "eve", "email": "eve@example.com", "password": "password123"},
    ]

    with app.app_context():
        for user in users:
            try:
                if not UserModel.query.filter_by(email=user["email"]).first():
                    hashed_password = generate_password_hash(user["password"])
                    db.session.add(
                        UserModel(
                            username=user["username"],
                            email=user["email"],
                            password=hashed_password,
                        )
                    )
                    db.session.commit()
                    print(f"Inserted user: {user['username']}")
            except Exception as err:
                db.session.rollback()
                print(f"Skipping duplicate or error for user '{user['username']}': {err}")


if __name__ == "__main__":
    print("Seeding tags...")
    seed_tags()
    print("Seeding users...")
    seed_users()
    print("Seeding complete!")


