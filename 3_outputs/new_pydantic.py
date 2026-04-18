from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class RiskManagement(BaseModel):
    description: str = "Global Risk Management"
    email: EmailStr
    IT: str
    MachineSecurity: str
    Dream: Optional[str] = None
    Index: float = Field(default=0.5, gt=0.0, lt=1.0, description="A decimal number representing risk value out of 1")

risk = RiskManagement(
    email="global@risk.in",
    IT="High",
    MachineSecurity="Low",
)

delhi_risk = RiskManagement(
    description = "Delhi Risk Management",
    email="delhi@risk.gov.in",
    IT="Low",
    MachineSecurity="Low",
    Dream="Disantrous",
    Index=0.3
)

print(risk)
print(delhi_risk)
print(delhi_risk.model_dump_json())
