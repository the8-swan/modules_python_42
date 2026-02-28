from pydantic import BaseModel


class User(BaseModel):
    idr: int
    name: str


try:
    user = User(idr="123", name="456")
    print(user.idr)
except Exception as e:
    print(f"error: {e}")
