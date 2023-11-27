from pydantic import BaseModel
from typing import Optional
class Admin(BaseModel):
    name: str
    role: str
    bio: Optional[str]