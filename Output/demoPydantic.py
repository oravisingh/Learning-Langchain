# With Pydantic there is data validation
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Employee(BaseModel):
    name: str = "Ravinandan" # Default value can be ovrewritten but keeps the variable filled till no value is given
    age: int
    email: EmailStr
    nominee: Optional[str] = None # Default value can be ovrewritten but keeps the variable filled till no value is given
    salary: float = Field(gt=56100, lt= 210000, default = 0)

emp1 = {
    "name": "Ravinandan Samrat",
    "age": 21
}
# new_emp = Employee(**emp1)
new_emp2 = Employee(name = "Ravi", age = 22, salary = 75000, email = "abc@gm.com", nominee = "Mira")
# print(new_emp)
print(new_emp2)