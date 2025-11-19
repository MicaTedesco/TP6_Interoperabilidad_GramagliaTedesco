import requests
from create_procedure import create_procedure_resource
from base import send_resource_to_hapi_fhir
from buscarpaciente import get_patient_id_by_dni

practitioner_id = "52960700"  

fecha_procedimiento = "2024-11-20"

dni_paciente = "42843082"
patient_id = get_patient_id_by_dni(dni_paciente)
print(f"URL → https://hapi.fhir.org/baseR4/Patient/{patient_id}\n")
print("="*80)
print("CREANDO PROCEDURE")
print("• Incluye: paciente, médico, procedimiento llevado a cabo, fecha del procedimiento, motivo, resultado y nota clínica detallada")
print("• SNOMED CT 225358003 → Procedimiento: Curación de herida")
print("• SNOMED CT 10960321000119104 → Motivo: Herida cortante en antebrazo izquierdo")

proc = create_procedure_resource(patient_id, dni_paciente, practitioner_id, fecha_procedimiento)
proc_id = send_resource_to_hapi_fhir(proc, "Procedure")

print("="*80)
print("\n")
print("PROCEDURE CREADO CON ÉXITO")
print(f"URL → https://hapi.fhir.org/baseR4/Procedure/{proc_id}")