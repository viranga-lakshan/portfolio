# Wosler Medical Technology – Software Developer Interview & Technical Prep Guide

This guide prepares you for conversations with Wosler's technical leadership, Chief Scientific Officer (CSO), and engineering team.

---

## 1. About Wosler & Strategic Context

* **Company Mission:** Making diagnostic imaging (ultrasound, X-ray, specialized imaging) accessible everywhere, especially in rural and underserved Canadian communities.
* **Operating Footprint:** Growing network of diagnostic imaging clinics across Alberta, Saskatchewan, and Nova Scotia.
* **Dual Nature:** Wosler operates both the physical diagnostic imaging clinics and builds the proprietary software, automation pipelines, and emerging AI technologies that power them.
* **Regulatory Certification:** **ISO 13485** (Quality Management System for Medical Devices) and **MDSAP** (Medical Device Single Audit Program, accepted by Health Canada and FDA).
* **Funding Stage:** Recently closed Seed Round, experiencing rapid clinic expansion and software product evolution.

---

## 2. Diagnostic Imaging Software Architecture & Clinical Workflows

### The End-to-End Diagnostic Imaging Lifecycle:
1. **Referral & Scheduling (RIS / Web Portal):** Referring physician submits an imaging requisition. Clinic staff schedule the appointment in the Radiology Information System (RIS).
2. **Patient Intake & Check-in:** Front-desk / patient tablet confirms demographic data, health card numbers, and consent (PIPEDA / provincial privacy compliant).
3. **Modality Examination (Ultrasound / X-ray):** Sonographer / technologist executes the scan. The imaging modality produces **DICOM (Digital Imaging and Communications in Medicine)** files.
4. **PACS Ingestion & Archiving:** The modality sends DICOM studies over network (DICOM C-STORE) to the **PACS (Picture Archiving and Communication System)** or cloud archive (AWS S3 + metadata database).
5. **Radiologist Reading & Reporting:** Radiologist accesses the study via a zero-footprint web viewer or diagnostic workstation, dictates findings, and creates a report.
6. **Report Distribution:** Final signed report is dispatched via HL7/FHIR to the referring physician and provincial health records (e.g., Netcare in Alberta).

---

## 3. Core MedTech Interoperability & Formats

### Q1: What is DICOM, and how do web applications interact with medical images?
* **DICOM Definition:** International standard format for medical images (CT, MRI, Ultrasound, X-ray) and metadata. A DICOM file contains both binary pixel data and extensive metadata headers (Patient Name, Patient ID, Modality, Study Date, Series Description, Window Width/Level).
* **Web Integration (DICOMweb & Cornerstone.js):**
  * Modern web browsers cannot natively render `.dcm` files.
  * We use **DICOMweb RESTful protocols** (WADO-RS for retrieving studies/images, QIDO-RS for querying metadata, STOW-RS for storing) or convert DICOM frames into compressed web formats (JPEG-LS / PNG / WebP) for fast rendering.
  * In React/TypeScript, libraries like **Cornerstone.js** or **OHIF Viewer** provide client-side viewport manipulation (panning, zooming, windowing/leveling contrast adjustments, length measurements).

### Q2: What are HL7 and FHIR, and why are they important for Wosler?
* **HL7 v2:** Traditional pipe-delimited messaging standard (`PID|1||...`, `OBX|...`) used for clinic scheduling (SIU messages), patient admissions (ADT messages), and lab/imaging results (ORU messages).
* **HL7 FHIR (Fast Healthcare Interoperability Resources):** Modern, RESTful JSON-based healthcare API standard.
  * Key Resources for Wosler: `Patient`, `ImagingStudy`, `DiagnosticReport`, `Practitioner`, `Appointment`.
  * Integrates modern web frontend (React/TypeScript) with clinical backends via clean JSON REST endpoints.

---

## 4. Canadian Healthcare Privacy & Compliance (PIPEDA, HIA)

### Q3: What security standards govern patient data in Alberta, Saskatchewan, and Nova Scotia?
* **PIPEDA (Federal):** Personal Information Protection and Electronic Documents Act establishes fair information principles across Canada.
* **Provincial Health Privacy Acts:**
  * **Alberta:** Health Information Act (HIA) — requires strict audit logging for every user viewing patient records ("Who viewed what patient chart and when?").
  * **Saskatchewan:** Health Information Protection Act (HIPA).
  * **Nova Scotia:** Personal Health Information Act (PHIA).
* **Technical Safeguards:**
  * **Encryption:** AES-256 for data at rest (AWS S3 server-side encryption, RDS encrypted storage) and TLS 1.3 for data in transit.
  * **Role-Based Access Control (RBAC):** Strict separation of privileges (e.g., receptionist can see demographic data and scheduling, sonographer sees requisition, radiologist sees imaging and clinical history).
  * **Data Residency:** Storing Personal Health Information (PHI) within Canadian AWS regions (`ca-central-1` in Montreal or Calgary).
  * **Audit Logging:** Tamper-evident logging of all authentication events, record accesses, and export activities.

---

## 5. Software Engineering Best Practices for MedTech (ISO 13485)

### Q4: How does working in an ISO 13485 / MDSAP certified environment impact software development?
* **Traceability (IEC 62304):** Every feature or change must trace from clinical user requirements ➔ design specifications ➔ code implementation (Git commits/PRs) ➔ automated verification tests.
* **Risk Management (ISO 14971):** Proactively analyzing failure modes (e.g., "What happens if network drops during scan upload?", "Could an incorrect patient ID be attached to an ultrasound series?"). Implementing defensive checks and idempotent transactions.
* **Quality Assurance & Automated Testing:**
  * Unit tests (Jest / Vitest / pytest) for business rules and calculations.
  * Integration tests for API contracts and database integrity.
  * End-to-end tests (Playwright / Cypress) validating clinical user journeys.
* **Strict Code Reviews:** Enforcing peer code reviews with mandatory checklists (security, performance, edge-case handling, documentation).

---

## 6. AI & Automation in Diagnostic Imaging

### Q5: How can AI/ML and LLMs be integrated into Wosler's clinic workflows?
1. **Intake & Requisition Triage:** Natural Language Processing (NLP) / LLM pipelines parse handwritten or scanned PDF referral notes from referring doctors, extracting patient details, examination requested, and clinical history into structured database records.
2. **Preliminary Report Generation:** Transcribing radiologist audio dictation using specialized medical speech models (Whisper-fine-tuned), formatting findings into standardized structured templates (e.g., BI-RADS for breast imaging).
3. **Quality & Completeness Checks:** Computer vision models verifying that ultrasound acquisition protocols contain all required anatomical view angles before the patient leaves the clinic room.
4. **Clinic Queue Automation:** Predicting appointment durations based on modality and patient history to optimize booking slots and minimize patient wait times.
