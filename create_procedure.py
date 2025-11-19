from fhir.resources.procedure import Procedure
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.annotation import Annotation
from datetime import datetime

def create_procedure_resource(patient_id, documento_paciente, practitioner_id, fecha_procedimiento,SNOMED_procedure_code=None, SNOMED_procedure_text=None  ,SNOMED_reason_code= None, SNOMED_reason_text=None,outcome_text=None, note_text=None):
    procedure = Procedure.construct()
    procedure.status = "completed"

    # IDENTIFIER DEL PACIENTE
    subject = Reference.construct()
    subject.reference = f"Patient/{patient_id}"
    subject.identifier = Identifier.construct()
    subject.identifier.system = "http://www.renaper.gob.ar/dni"
    subject.identifier.value = documento_paciente
    procedure.subject = subject

    # CÓDIGO SNOMED CT - PROCEDIMIENTO: CURACIÓN DE HERIDA
    procedure.code = CodeableConcept.construct()
    procedure.code.coding = [Coding.construct(system="http://snomed.info/sct", code=SNOMED_procedure_code, display=SNOMED_procedure_text)]
    procedure.code.text = SNOMED_procedure_text

    # FECHA DEL PROCEDIMIENTO
    procedure.performedDateTime = fecha_procedimiento

    # CÓDIGO SNOMED CT - MOTIVO: HERIDA CORTANTE EN ANTEBRAZO IZQUIERDO
    procedure.reasonCode = [CodeableConcept.construct(coding=[Coding.construct(
        system="http://snomed.info/sct",
        code=SNOMED_reason_code,
        display=SNOMED_reason_text
    )])]

    # RESULTADO
    procedure.outcome = CodeableConcept.construct(text=outcome_text)

    # NOTA CLÍNICA
    note = Annotation.construct()
    note.text = note_text
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
