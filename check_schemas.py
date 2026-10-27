from database import SessionLocal
import models
from schemas import UserOut

db = SessionLocal()
user = db.get(models.User, 2)

print("DB object has hash:", user.hashed_password[:20] + '...')
print("UserOut sends:  ", UserOut.model_validate(user).model_dump_json())
db.close()
