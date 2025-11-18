from fhir.resources.procedure import Procedure
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier

def create_procedure_resource(status=None, code=None, subject=None,text=None, documento=None):

    # Preparar la Reference del sujeto si se proporcionó
    reference = None
    if subject:
        reference = Reference()
        reference.reference = f"Patient/{subject}"
        # Si se provee el DNI (documento), lo agregamos como Identifier
        if documento:
            identifier = Identifier()
            identifier.system = "http://www.renaper.gob.ar/dni"
            identifier.value = str(documento)
            reference.identifier = identifier

    # Inicializar Procedure con status (o 'unknown') y con la subject Reference
    if reference:
        procedure = Procedure(status=status or "unknown", subject=reference)
    else:
        procedure = Procedure(status=status or "unknown")

    # Agregar el código del procedimiento si está disponible
    if code:
        codeable_concept = CodeableConcept()
        coding = Coding()
        coding.system = "http://snomed.info/sct"
        coding.code = code
        codeable_concept.coding = [coding]
        codeable_concept.text = text
        procedure.code = codeable_concept

    # (La subject ya se añadió al constructor si existía)

    return procedure