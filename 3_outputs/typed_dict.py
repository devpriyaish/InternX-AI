from typing import TypedDict

class RiskManagement(TypedDict):
  IT: str
  MachineSecurity: str

risk: RiskManagement = {
  "IT": "High",
  "MachineSecurity": "Low"
}

new_risk: RiskManagement = {
  "IT": 27,
  "MachineSecurity": 5
}

print(risk)
print(new_risk)

print("--------- typed_dict is only for representation and not validation purpose -----------")
