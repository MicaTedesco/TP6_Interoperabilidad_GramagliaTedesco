import requests
import json

dni = "42843082"
system = "http://www.renaper.gob.ar/dni" 
search_url = f"https://hapi.fhir.org/baseR4/Patient?identifier={system}|{dni}"

print(f"Buscando paciente con DNI: {dni}")
print(f"URL utilizada: {search_url}\n")

response = requests.get(search_url)
data = response.json()

if data.get("total", 0) > 0:
    paciente = data["entry"][0]["resource"]
    patient_id = paciente["id"]
    nombre = f"{paciente['name'][0]['given'][0]} {paciente['name'][0]['family']}"
    
    print("PACIENTE ENCONTRADO:")
    print(f"ID lógico      : {patient_id}")
    print(f"Nombre completo: {nombre}")
    print(f"URL permanente : https://hapi.fhir.org/baseR4/Patient/{patient_id}\n")
    print("=" * 15)
    print("JSON COMPLETO")
    print("=" * 15)
    print(json.dumps(paciente, indent=2, ensure_ascii=False))
else:
    print("No se encontró ningún paciente con ese DNI.")
