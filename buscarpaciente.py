import requests
import json

dni = "42843082"
search_url = f"https://hapi.fhir.org/baseR4/Patient?identifier={dni}"

response = requests.get(search_url)

print(f"Búsqueda de paciente con DNI {dni}:")
print(json.dumps(response.json(), indent=2))
