from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
  id: Optional[int] = None
  username: str=""
  password_hash: str=""
  is_activate: bool=True
  created_at: Optional[str]=None

  def to_dict(self):
    return{
      'id': self.id,
      'username': self.username,
      'is_active': self.is_activate,
      'created_at': self.created_at
    }