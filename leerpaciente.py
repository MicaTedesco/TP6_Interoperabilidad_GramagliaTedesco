from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Tedesco"
    given_name = "Micaela Rocio"
    birth_date = "2000-08-21"
    gender = "female"
    phone = 1161751010 
    documento = 42843082

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, documento)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')
