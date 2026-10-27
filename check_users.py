from database import SessionLocal
import models

db = session = SessionLocal()
for u in db.query(models.User).all():
    print(u.id, u.email,u.role, u.hashed_password[:30] + '...')
print("Books:", db.query(models.Book).count())
db.close()

