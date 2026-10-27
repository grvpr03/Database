from database import SessionLocal, engine, Base
import models
from security import hash_password

Base.metadata.create_all(engine)

books = [
    models.Book(title="1984", author="George Orwell", copies=3),
    models.Book(title="Animal Farm", author="George Orwell", copies=2),
    models.Book(title="The Lightning Thief", author="Rick Riordan", copies=4),
    models.Book(title="The Sea of Monsters", author="Rick Riordan", copies=2),
    models.Book(title="Harry Potter and the Philosopher's Stone", author="J.K. Rowling", copies=5),
    models.Book(title="Harry Potter and the Chamber of Secrets", author="J.K. Rowling", copies=3),
    models.Book(title="The Great Gatsby", author="F. Scott Fitzgerald", copies=3),
    models.Book(title="To Kill a Mockingbird", author="Harper Lee", copies=5),
    models.Book(title="The Hobbit", author="J.R.R. Tolkien", copies=4),
    models.Book(title="Pride and Prejudice", author="Jane Austen", copies=2),
]

users = [
    models.User(name="Admin", email="admin@example.com", hashed_password=hash_password("admin123"), role="admin"),
    models.User(name="Alice", email="alice@example.com", hashed_password=hash_password("alice123"), role="user"),
    models.User(name="Bob",   email="bob@example.com",   hashed_password=hash_password("bob123"),   role="user"),
]

db = SessionLocal()

if db.query(models.Book).count() > 0:
    print("Books already exist, skipping seed.")
else:
    db.add_all(books)
    db.commit()
    print(f"Added {len(books)} books.")

if db.query(models.User).count() > 0:
    print("Users already exist, skipping seed.")
else:
    db.add_all(users)
    db.commit()
    print(f"Added {len(users)} users.")

db.close()
