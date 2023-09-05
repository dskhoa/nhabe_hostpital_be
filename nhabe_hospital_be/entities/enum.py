import enum


class ReportForm(str, enum.Enum):
    IS_REQUIRED = "is_required"
    IS_VOLUNTARY = "is_voluntary"


class IncidentSubject(str, enum.Enum):
    CLIENT = "client"
    VISITOR = "visitor"
    STAFF = "staff"
    INFRASTRUCTURE = "infrastructure"


class BooleanChoice(str, enum.Enum):
    YES = "yes"
    NO = "no"
    NOT_ACKNOWLEDGED = "not_acknowledged"


class IncidentClassification(str, enum.Enum):
    HAPPEN = "happen"
    NOT_HAPPEN = "not_happen"


class ImpactAssessment(str, enum.Enum):
    LIGHT = "light"
    MEDIUM = "medium"
    HARD = "hard"


class SituationClassification(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"


class DamageClassification(str, enum.Enum):
    NC0 = "NC0"
    NC1 = "NC1"
    NC2 = "NC2"
    NC3 = "NC3"
