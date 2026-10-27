import jwt
from config import settings
from security import hash_password, verify_password, create_access_token

print("--- Check A: hashing ---")
a = hash_password("alice123")
b = hash_password("alice123")
print(a)
print(a == b)
print(verify_password("alice123", a))
print(verify_password("wrong", a))

print("\n--- Check B: tokens ---")
token = create_access_token(1)
print(token)
print(token.count("."))
print(jwt.decode(token, settings.secret_key, algorithms=["HS256"]))