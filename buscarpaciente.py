import requests
import json


def get_patient_id_by_dni(dni, system="http://www.renaper.gob.ar/dni"):
    """Buscar un paciente en el servidor HAPI FHIR por DNI y devolver su patient_id.

    Args:
        dni (str|int): número de documento del paciente.
        system (str): URI del sistema de identificación (por defecto RENAPER/DNI).

    Returns:
        str | None: el `id` lógico del recurso Patient si se encuentra, o `None` si no.
    """
    # Asegurar que el DNI se convierta a string para formar la URL
    dni_str = str(dni)
    search_url = f"https://hapi.fhir.org/baseR4/Patient?identifier={system}|{dni_str}"

    try:
        response = requests.get(search_url)
        response.raise_for_status()
    except requests.RequestException as e:
        # En caso de error de red o respuesta no 2xx devolvemos None
        print(f"Error al consultar el servidor FHIR: {e}")
        return None

    data = response.json()

    # Si hay al menos un resultado, devolvemos el id del último recurso en 'entry'
    if data.get("total", 0) > 0 and "entry" in data and len(data["entry"]) > 0:
        print(f"PACIENTE ENCONTRADO")
        paciente = data["entry"][-1]["resource"]
        nombre = f"{paciente['name'][0]['given'][0]} {paciente['name'][0]['family']}"
        print(f"Nombre Paciente: {nombre}")
        return paciente.get("id")

    return None


if __name__ == "__main__":
    # Ejemplo de uso desde línea de comandos
    dni = "42843082"
    print(f"Buscando paciente con DNI: {dni}")
    patient_id = get_patient_id_by_dni(dni)
    if patient_id:
        print(f"ID lógico      : {patient_id}")
        print(f"URL permanente : https://hapi.fhir.org/baseR4/Patient/{patient_id}\n")
    else:
        print("No se encontró ningún paciente con ese DNI.")
