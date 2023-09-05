from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Query

import entities
from models.report import ReportRequestCreate, ReportRequestUpdate


def get_report(db: Session, report_id: int) -> Optional[entities.Report]:
    return db.query(entities.Report).filter(entities.Report.id == report_id).first()


def list_report(db: Session, page: int, limit: int) -> List[entities.Report]:
    offset = (page - 1) * limit
    return db.query(entities.Report).offset(offset).limit(limit).all()


def get_report_by_report_id(db: Session, report_id: int) -> Optional[entities.Report]:
    return db.query(entities.Report).filter(entities.Report.id == report_id).first()


def get_report_by_report_reference(
    db: Session, report_reference: str
) -> Optional[entities.Report]:
    return (
        db.query(entities.Report)
        .filter(entities.Report.report_reference == report_reference)
        .first()
    )


def create_report(db: Session, report: ReportRequestCreate) -> entities.Report:
    db_report = entities.Report(**report.model_dump(exclude_unset=True))

    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    return db_report


def update_report(
    db: Session, report_id: int, report: ReportRequestUpdate
) -> Optional[entities.Report]:
    update_data = report.model_dump(exclude_unset=True)

    report_query = db.query(entities.Report).filter(entities.Report.id == report_id)
    db_report = report_query.first()

    if not update_data:
        return db_report
    report_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_report)

    return db_report


def delete_report(db: Session, report_id: int) -> Optional[entities.Report]:
    report_query = db.query(entities.Report).filter(entities.Report.id == report_id)
    db_report = report_query.first()

    print('db_report before', db_report, type(db_report))

    report_query.delete(synchronize_session=False)
    db.commit()

    print('db_report', db_report, type(db_report))

    return db_report
