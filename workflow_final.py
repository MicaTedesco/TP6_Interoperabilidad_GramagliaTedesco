import requests
from create_procedure import create_procedure_resource
from base import send_resource_to_hapi_fhir
from buscarpaciente import get_patient_id_by_dni

practitioner_id = "52962291"  

fecha_procedimiento = "2024-11-20"

dni_paciente = "42843082"
patient_id = get_patient_id_by_dni(dni_paciente)
print(f"URL → https://hapi.fhir.org/baseR4/Patient/{patient_id}\n")
print("="*80)

SNOMED_procedure_code = "225358003"
SNOMED_procedure_text = "Curación de herida"
SNOMED_reason_code = "10960321000119104"
SNOMED_reason_text = "Herida cortante en antebrazo izquierdo"
outcome_text = "Herida limpia, sin signos de infección, buena evolución"
note_text = "Curación de herida cortante en antebrazo izquierdo por accidente doméstico. Se realizó limpieza con solución fisiológica, aplicación de antiséptico y vendaje oclusivo. El paciente toleró bien el procedimiento."


print("CREANDO PROCEDURE")
print("• Incluye: paciente, médico, procedimiento llevado a cabo, fecha del procedimiento, motivo, resultado y nota clínica detallada")
print(f"• SNOMED CT {SNOMED_procedure_code} → Procedimiento: {SNOMED_procedure_text}")
print(f"• SNOMED CT {SNOMED_reason_code} → Motivo: {SNOMED_reason_text}")
print("="*80)
print("\n")
proc = create_procedure_resource(patient_id, dni_paciente, practitioner_id, fecha_procedimiento, SNOMED_procedure_code, SNOMED_procedure_text, SNOMED_reason_code, SNOMED_reason_text, outcome_text, note_text)
proc_id = send_resource_to_hapi_fhir(proc, "Procedure")

print(f"URL → https://hapi.fhir.org/baseR4/Procedure/{proc_id}")
