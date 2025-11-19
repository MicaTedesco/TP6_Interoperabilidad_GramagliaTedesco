from fhir.resources.procedure import Procedure
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.annotation import Annotation
from datetime import datetime

def create_procedure_resource(patient_id, documento_paciente, practitioner_id, fecha_procedimiento):
    procedure = Procedure.construct()
    procedure.status = "completed"

    # IDENTIFIER PACIENTE
    subject = Reference.construct()
    subject.reference = f"Patient/{patient_id}"
    subject.identifier = Identifier.construct()
    subject.identifier.system = "http://www.renaper.gob.ar/dni"
    subject.identifier.value = documento_paciente
    procedure.subject = subject

    # CÓDIGO SNOMED CT - PROCEDIMIENTO: CURACIÓN DE HERIDA
    procedure.code = CodeableConcept.construct()
    procedure.code.coding = [Coding.construct(system="http://snomed.info/sct", code="225358003", display="Curación de herida")]
    procedure.code.text = "Curación de herida"

    # FECHA DEL PROCEDIMIENTO
    procedure.performedDateTime = fecha_procedimiento

    # CÓDIGO SNOMED CT - MOTIVO: HERIDA CORTANTE EN ANTEBRAZO IZQUIERDO
    procedure.reasonCode = [CodeableConcept.construct(coding=[Coding.construct(
        system="http://snomed.info/sct",
        code="10960321000119104",
        display="Herida cortante en antebrazo izquierdo"
    )])]

    # RESULTADO
    procedure.outcome = CodeableConcept.construct(text="Herida limpia, sin signos de infección, buena evolución")

    # NOTA CLÍNICA
    note = Annotation.construct()
    note.text = "Curación de herida cortante en antebrazo izquierdo por accidente doméstico. Se realizó limpieza con solución fisiológica, aplicación de antiséptico y vendaje oclusivo. El paciente toleró bien el procedimiento."
    note.time = datetime.now().isoformat()
    procedure.note = [note]

    # MÉDICO RESPONSABLE
    performer_ref = Reference.construct()
    performer_ref.reference = f"Practitioner/{practitioner_id}"
    performer_ref.display = "Dr. Eric van den Broek"

    procedure.performer = [{
        "actor": performer_ref
    }]

    return procedure
