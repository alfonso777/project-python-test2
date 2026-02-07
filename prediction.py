import json
import requests

inputs_dict = {
  "dataframe_split": {
    "columns": [
      "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
      "mean compactness", "mean concavity", "mean concave points", "mean symmetry", "mean fractal dimension",
      "radius error", "texture error", "perimeter error", "area error", "smoothness error",
      "compactness error", "concavity error", "concave points error", "symmetry error", "fractal dimension error",
      "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
      "worst compactness", "worst concavity", "worst concave points", "worst symmetry", "worst fractal dimension"
    ],
    "data": [[0.12, 0.89, 0.98, 0.06, 0.47, 0.35, 0.37, 0.7, 0.61, 0.16, 0.67, 0.58, 0.61, 0.47, 0.86, 0.21, 0.67, 0.69, 0.91, 0.19, 0.18, 0.23, 0.03, 0.63, 0.81, 0.82, 0.37, 0.38, 0.53, 0.19], [0.12, 0.89, 0.98, 0.06, 0.47, 0.35, 0.37, 0.7, 0.61, 0.13, 0.1, 0.58, 0.61, 0.40, 0.86, 0.21, 0.67, 0.69, 0.91, 0.19, 0.18, 0.23, 0.03, 0.63, 0.81, 0.82, 0.37, 0.38, 0.53, 0.19]]
  }
}
payload = json.dumps(inputs_dict)
response = requests.post(
    url=f"http://localhost:1234/invocations",
    data=payload,
    headers={"Content-Type": "application/json"},
)
print(response.json())
