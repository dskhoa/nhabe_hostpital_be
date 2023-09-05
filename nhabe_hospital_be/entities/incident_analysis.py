from sqlalchemy import Column, Enum, Integer, JSON, String

from database.database import Base
from entities.enum import BooleanChoice, DamageClassification


class IncidentAnalysis(Base):
    __tablename__ = "incident_analyses"

    id = Column(Integer, primary_key=True, index=True)
    analysis_reference = Column(String, unique=True, index=True)
    detailed_description = Column(String, default=None)
    incident_type = Column(JSON, default=None)
    treatment_executed = Column(String, default=None)
    incident_reason = Column(JSON, default=None)
    solution_executed = Column(String, default=None)
    recommendation_incident_prevention = Column(String, default=None)
    is_aligned_with_reporter = Column(Enum(BooleanChoice))
    is_accorded = Column(Enum(BooleanChoice))
    client_level = Column(Enum(DamageClassification))
    organization_level = Column(String, default=None)
    reporter_fullname = Column(String, default=None)
    reporter_role = Column(String, default=None)
    created_at = Column(Integer, default=None)
    updated_at = Column(Integer, default=None)
