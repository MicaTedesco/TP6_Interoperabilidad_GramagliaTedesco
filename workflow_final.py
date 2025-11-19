import requests
from create_procedure import create_procedure_resource
from base import send_resource_to_hapi_fhir

dni = "42843082"
url = f"https://hapi.fhir.org/baseR4/Patient?identifier=http://www.renaper.gob.ar/dni|{dni}"

print("BUSCANDO PACIENTE CON DNI: ", dni)
print("\n")
resp = requests.get(url).json()

if resp["total"] == 0:
    print("No se encontró el paciente.")
    exit()

patient_id = resp["entry"][0]["resource"]["id"]
print(f"PACIENTE ENCONTRADO")
print(f"URL → https://hapi.fhir.org/baseR4/Patient/{patient_id}\n")
print("="*80)
print("CREANDO PROCEDURE")
print("• SNOMED CT 225358003 → Curación de herida")
print("• SNOMED CT 10960321000119104 → Herida cortante en antebrazo izquierdo")
print("• Incluye performer, encounter, reasonCode, outcome, note")
print("• DNI argentino como identifier\n")

proc = create_procedure_resource(patient_id, dni)
proc_id = send_resource_to_hapi_fhir(proc, "Procedure")

print("="*80)
print("PROCEDURE CREADO CON ÉXITO")

print(f"URL → https://hapi.fhir.org/baseR4/Procedure/{proc_id}")
