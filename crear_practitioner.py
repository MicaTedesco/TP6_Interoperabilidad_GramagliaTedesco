import requests
from fhir.resources.practitioner import Practitioner
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address

def create_fictitious_practitioner():
    practitioner = Practitioner.construct()

    # Matrícula ficticia
    identifier = Identifier.construct()
    identifier.use = "official"
    identifier.system = "http://www.argentina.gob.ar/matriculas"
    identifier.value = "MAT-12345"
    practitioner.identifier = [identifier]

    # Nombre
    name = HumanName.construct()
    name.use = "official"
    name.family = "van den Broek"
    name.given = ["Eric"]
    name.suffix = ["MD"]
    practitioner.name = [name]

    # Telecom
    phone = ContactPoint.construct()
    phone.system = "phone"
    phone.value = "0205568263"
    phone.use = "work"

    email = ContactPoint.construct()
    email.system = "email"
    email.value = "E.M.vandenbroek@bmc.nl"
    email.use = "work"

    practitioner.telecom = [phone, email]

    # Género y fecha de nacimiento
    practitioner.gender = "male"
    practitioner.birthDate = "1975-12-07"

    # Dirección
    addr = Address.construct()
    addr.use = "work"
    addr.line = ["Galapagosweg 91"]
    addr.city = "Den Burg"
    addr.postalCode = "9105 PZ"
    addr.country = "NLD"
    practitioner.address = [addr]

    # Enviar a HAPI
    url = "https://hapi.fhir.org/baseR4/Practitioner"
    headers = {"Content-Type": "application/fhir+json"}
    resp = requests.post(url, data=practitioner.json(), headers=headers)

    if resp.status_code == 201:
        practitioner_id = resp.json()["id"]
        print("\nPRACTITIONER CREADO CON ÉXITO")
        print("URL → https://hapi.fhir.org/baseR4/Practitioner/" + practitioner_id)
        return practitioner_id
    else:
        print("Error creando Practitioner:", resp.text)
        return None

if __name__ == "__main__":
    create_fictitious_practitioner()
