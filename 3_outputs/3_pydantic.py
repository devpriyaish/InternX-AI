from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class RiskManagement(BaseModel):
  IT: str = Field(description="Risk level for IT department")
  MachineSecurity: float = Field(default=0.5, gt=0.1, lt=0.9, description="Risk level for Machine Security")
  email: EmailStr = Field(description="Contact email for risk management")
  department: Optional[str] = None


risk = RiskManagement(
  IT="High",
  email="abc@example.com"
)

new_risk = RiskManagement(
    IT=27,
    MachineSecurity=0.6,
    email="abc@example.com"
)

print(risk)
print(new_risk)