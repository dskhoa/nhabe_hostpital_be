BEGIN;
CREATE TABLE "reports" ("id" bigserial NOT NULL PRIMARY KEY, "report_reference" varchar(255) NOT NULL UNIQUE, "is_required" varchar(255) NULL, "unit" varchar(255) NULL, "client_fullname" varchar(255) NULL, "client_birthdate" TIMESTAMP NULL, "client_medical_record_id" varchar(255) NULL, "client_gender_male" boolean NULL, "department" varchar(255) NULL, "incident_subject" varchar(255) NULL, "incident_location" varchar(255) NULL, "exact_location" varchar(255) NULL, "issued_date" TIMESTAMP NULL, "short_description" varchar(2048) NULL, "proposal_solution" varchar(2048) NULL, "performed_treatment" varchar(2048) NULL, "is_informed" varchar(255) NULL, "is_recorded" varchar(255) NULL, "is_family_noticed" varchar(255) NULL, "is_client_noticed" varchar(255) NULL, "incident_classification" varchar(255) NULL, "impact_assessment" varchar(255) NULL, "reporter_fullname" varchar(255) NULL, "reporter_phone" varchar(255) NULL, "reporter_email" varchar(255) NULL, "reporter_type" varchar(255) NULL, "observer_1" varchar(255) NULL, "observer_2" varchar(255) NULL, "title" varchar(255) NULL, "status" varchar(255) NULL, "situation_classification" varchar(255) NULL, "damage_classification" varchar(255) NULL, "created_at" TIMESTAMP NULL, "updated_at" TIMESTAMP NULL);
CREATE INDEX "report_report_reference_cf81f601_like" ON "reports" ("report_reference" varchar_pattern_ops);
COMMIT;



BEGIN;
CREATE TABLE "incident_analyses" ("id" bigserial NOT NULL PRIMARY KEY, "analysis_reference" varchar(255) NOT NULL UNIQUE, "detailed_description" varchar(2048) NULL, "incident_type" jsonb NULL, "treatment_executed" varchar(2048) NULL, "incident_reason" jsonb NULL, "solution_executed" varchar(2048) NULL, "recommendation_incident_prevention" varchar(2048) NULL, "is_aligned_with_reporter" varchar(2048) NULL, "is_accorded" varchar(255) NULL, "client_level" varchar(255) NULL, "organization_level" varchar(255) NULL, "reporter_fullname" varchar(255) NULL, "reporter_role" varchar(255) NULL, "created_at" TIMESTAMP NULL, "updated_at" TIMESTAMP NULL);
CREATE INDEX "incident_analyses_analysis_reference_23fb03e6_like" ON "incident_analyses" ("analysis_reference" varchar_pattern_ops);
COMMIT;



BEGIN;
CREATE TABLE "users" ( "id" bigserial NOT NULL PRIMARY KEY, "username" varchar(255) DEFAULT NULL, "password" varchar(255) DEFAULT NULL, "firstname" varchar(255) DEFAULT NULL, "lastname" varchar(255) DEFAULT NULL, "avatar" varchar(255) DEFAULT NULL, "role" varchar(255) DEFAULT NULL, "email" varchar(255) DEFAULT NULL, "phone" varchar(255) DEFAULT NULL, "identification" varchar(255) DEFAULT NULL, "created_at" TIMESTAMP DEFAULT NULL, "updated_at" TIMESTAMP DEFAULT NULL );
CREATE INDEX "users_username_like" ON "users" ("username" varchar_pattern_ops);
COMMIT;


INSERT INTO users (username, password, firstname, lastname, avatar, role, email, phone, identification, created_at, updated_at)
VALUES ('nhabe_admin', 'nhabehospital@secret', 'Admin', 'User', '', 'admin', 'admin@nhabe.com', '', '', NOW(), NOW());