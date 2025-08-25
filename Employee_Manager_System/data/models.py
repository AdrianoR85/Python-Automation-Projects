from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Employee:
  id: Optional[int] = None
  name: str = ""
  phone: str = ""
  role: str = ""
  gender: str = ""
  salary: float = 0.0
  created_at: Optional[datetime] = None

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "phone": self.phone,
      "role": self.role,
      "gender": self.gender,
      "salary": self.salary,
      "created_at": self.created_at
    }
  
  def to_tuple_insert(self):
    # usado no INSERT (sem id, pq o banco gera)
    return (self.name, self.phone, self.role, self.gender, self.salary)

  def to_tuple_update(self):
    # usado no UPDATE (dados + id no final)
    return (self.name, self.phone, self.role, self.gender, self.salary, self.id)