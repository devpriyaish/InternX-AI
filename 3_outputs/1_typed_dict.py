from typing import TypedDict, Annotated

class RiskManagement(TypedDict):
  IT: Annotated[str, "Risk level for IT department"]
  MachineSecurity: Annotated[float, "Risk level for Machine Security"]

risk: RiskManagement = {
  "IT": "High",
  "MachineSecurity": "Low"
}

new_risk: RiskManagement = {
  "IT": 27,
  "MachineSecurity": 5.0
}

print(risk)
print(new_risk)

print("--------- typed_dict is only for representation and not validation purpose -----------")
