import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Software Developer Proposal - Wosler Medical Technology - Viranga Lakshan</title>
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 7.9pt;
    line-height: 1.33;
  }
  .page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    padding: 11mm 14mm 10mm 14mm;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    background: #ffffff;
  }
  .page:last-child {
    page-break-after: avoid;
  }

  /* Minimalist Accent Line */
  .top-accent-line {
    width: 42px;
    height: 3px;
    background: #0f766e;
    border-radius: 2px;
    margin-bottom: 7px;
  }

  /* Header Top */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1.5px solid #0f766e;
    padding-bottom: 6px;
    margin-bottom: 8.5px;
  }
  .brand-title {
    font-size: 13pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.3px;
    display: flex;
    align-items: center;
    gap: 7px;
  }
  .brand-badge {
    background: #0f766e;
    color: #ffffff;
    font-size: 6.7pt;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .brand-sub {
    font-size: 8.2pt;
    color: #475569;
    font-weight: 600;
    margin-top: 1px;
  }
  .meta-block {
    text-align: right;
    font-size: 7.3pt;
    color: #64748b;
    line-height: 1.28;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Executive Banner */
  .quote-banner {
    background: #f0fdfa;
    border: 1px solid #ccfbf1;
    border-left: 3.5px solid #0f766e;
    border-radius: 4px;
    padding: 7px 11px;
    margin-bottom: 8px;
  }
  .quote-banner-title {
    font-size: 9pt;
    font-weight: 800;
    color: #115e59;
    margin-bottom: 2px;
  }
  .quote-banner-desc {
    font-size: 7.5pt;
    color: #134e4a;
    line-height: 1.3;
    margin: 0;
  }

  /* Section Styling */
  .section {
    margin-bottom: 7.5px;
  }
  .section-title {
    font-size: 8.9pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3px solid #0f766e;
    padding-left: 6.5px;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 6.9pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
    letter-spacing: 0;
  }

  /* Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6.5px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 5px;
  }

  /* Cards */
  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 8px;
  }
  .card.tint {
    background: #f0fdfa;
    border-color: #ccfbf1;
  }
  .card.slate {
    background: #f8fafc;
    border-color: #e2e8f0;
  }
  .card.accent {
    border-top: 2.5px solid #0f766e;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2.5px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
  }
  .card.tint .card-header {
    border-color: #99f6e4;
  }
  .card-title {
    font-size: 7.9pt;
    font-weight: 700;
    color: #0f172a;
  }
  .card-badge {
    font-size: 6.5pt;
    font-weight: 700;
    padding: 1px 4.5px;
    border-radius: 3px;
    background: #e2e8f0;
    color: #475569;
    text-transform: uppercase;
  }
  .card.tint .card-badge {
    background: #ccfbf1;
    color: #0f766e;
  }
  .card-p {
    font-size: 7.3pt;
    color: #334155;
    margin: 0 0 2.5px 0;
    line-height: 1.27;
  }
  .card-bullets {
    margin: 0;
    padding-left: 11px;
    font-size: 7.1pt;
    color: #475569;
    line-height: 1.25;
  }
  .card-bullets li {
    margin-bottom: 1.4px;
  }
  .card-bullets strong, .card-p strong {
    color: #0f172a;
  }

  code {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 0.5px 3px;
    border-radius: 3px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 6.7pt;
    color: #0f766e;
  }

  /* Tables */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.2pt;
    margin-top: 1.5px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 3.5px 6px;
    font-weight: 700;
    font-size: 6.8pt;
    text-transform: uppercase;
    letter-spacing: 0.25px;
  }
  table.matrix-table td {
    padding: 3.5px 6px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.23;
  }
  table.matrix-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  table.matrix-table td strong {
    color: #0f172a;
  }

  /* Callout */
  .callout-box {
    background: #f0fdfa;
    border-left: 3.5px solid #0f766e;
    border-radius: 4px;
    padding: 5px 8px;
    margin-top: 3.5px;
  }
  .callout-title {
    font-size: 7.7pt;
    font-weight: 700;
    color: #115e59;
    margin-bottom: 1px;
  }
  .callout-text {
    font-size: 7.1pt;
    color: #134e4a;
    line-height: 1.24;
  }

  /* Metric Stat Box */
  .stat-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4.5px 6.5px;
    text-align: center;
  }
  .stat-val {
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f766e;
    line-height: 1.1;
  }
  .stat-lbl {
    font-size: 6.5pt;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    margin-top: 1px;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 6.9pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #0f766e;
    text-decoration: none;
    margin-left: 8px;
    font-weight: 600;
  }
</style>
</head>
<body>

<!-- ========================================== PAGE 1: EXECUTIVE QUALIFICATIONS & FIT ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">VIRANGA <span style="color:#0f766e;">LAKSHAN</span> <span class="brand-badge">Software Developer</span></div>
        <div class="brand-sub">Medical Technology Engineering • Web Applications, APIs, Cloud & AI Systems</div>
      </div>
      <div class="meta-block">
        <strong>Target Company:</strong> Wosler Diagnostics Inc.<br>
        <strong>Role:</strong> Software Developer (Reporting to CSO)<br>
        <strong>Arrangement:</strong> Virtual / Full-Time<br>
        <strong>Availability:</strong> Immediate Start
      </div>
    </div>

    <!-- Executive Brief Banner -->
    <div class="quote-banner">
      <div class="quote-banner-title">Engineering Mission & Alignment with Wosler</div>
      <p class="quote-banner-desc">
        Full-Stack Software Engineer with <strong>5+ years of production experience</strong> building resilient web applications, REST APIs, relational database backends, and cloud-hosted healthcare systems. Deeply aligned with Wosler's mission to expand diagnostic imaging access across Alberta, Saskatchewan, and Nova Scotia. Experienced delivering clean, maintainable, and audit-ready software within production environments supporting real-world clinical and patient workflows.
      </p>
    </div>

    <!-- Highlight Stats -->
    <div class="grid-4" style="margin-bottom: 7px;">
      <div class="stat-box">
        <div class="stat-val">5+ Years</div>
        <div class="stat-lbl">Full-Stack Software Eng.</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">React & TS</div>
        <div class="stat-lbl">Modern Web Applications</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">REST & SQL</div>
        <div class="stat-lbl">APIs & Relational Data</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">AWS & AI</div>
        <div class="stat-lbl">Cloud, Automation & LLMs</div>
      </div>
    </div>

    <!-- Section 1: Direct Requirement Alignment Matrix -->
    <div class="section">
      <div class="section-title">
        1. Qualifications & Requirements Alignment Matrix
        <span class="tagline">Direct Mapping to Wosler's Technical & Operational Criteria</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 28%;">Wosler Role Requirement</th>
            <th style="width: 52%;">Viranga's Production Experience & Engineering Competency</th>
            <th style="width: 20%; text-align: right;">Status & Match</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>3+ Years Software Development</strong></td>
            <td>5+ years building and maintaining enterprise software in production, contributing across frontend UI, backend services, and automated CI/CD pipelines.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Exceeds (5+ Yrs)</strong></td>
          </tr>
          <tr>
            <td><strong>Modern Frontend (React, Vue)</strong></td>
            <td>Extensive production engineering in React and TypeScript; building modular component architectures, accessible patient portals, and clinician dashboards.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Core Competency</strong></td>
          </tr>
          <tr>
            <td><strong>Backend & REST APIs</strong></td>
            <td>Architecting scalable RESTful web APIs with Node.js/TypeScript, Python, and C#; integrating microservices, third-party medical devices, and external webhooks.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Production Tested</strong></td>
          </tr>
          <tr>
            <td><strong>Relational Databases & SQL</strong></td>
            <td>Designing normalized schemas, indexing hot paths, tuning execution plans, and enforcing strict ACID transaction boundaries in PostgreSQL and SQL Server.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Advanced SQL</strong></td>
          </tr>
          <tr>
            <td><strong>Clean Code, Testing & Git</strong></td>
            <td>Disciplined practitioner of clean architecture, SOLID principles, TDD, automated unit/integration testing (Jest, PyTest), Git pull requests, and peer reviews.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Standard Practice</strong></td>
          </tr>
          <tr>
            <td><strong>Security & Sensitive Data</strong></td>
            <td>Deep understanding of application security: OAuth2/JWT auth, Role-Based Access Control (RBAC), TLS 1.3 encryption, and compliance principles (PIPEDA / HIPAA).</td>
            <td style="text-align: right; color: #0f766e;"><strong>Compliance Ready</strong></td>
          </tr>
          <tr>
            <td><strong>Cloud, Docker & Linux (Nice-to-Have)</strong></td>
            <td>Hands-on AWS experience (S3 for imaging files, Lambda serverless tasks, EC2, RDS), Docker containerization, and automated GitHub Actions CI/CD workflows.</td>
            <td style="text-align: right; color: #0f766e;"><strong>AWS & Containers</strong></td>
          </tr>
          <tr>
            <td><strong>AI/ML & Automation (Nice-to-Have)</strong></td>
            <td>Integrating LLM APIs and machine learning models for clinical note extraction, report summarization, automated requisition triage, and workflow routing.</td>
            <td style="text-align: right; color: #0f766e;"><strong>Hands-On AI/LLM</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 2: Engagement Terms Summary -->
    <div class="section">
      <div class="section-title">
        2. Engagement Overview & Readiness
        <span class="tagline">Immediate Full-Time Availability Aligned with Wosler's Growth</span>
      </div>
      <div class="grid-3">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Full-Time Commitment</span>
            <span class="card-badge">Capacity</span>
          </div>
          <p class="card-p">
            Dedicated full-time capacity reporting to the CSO, integrating seamlessly with Wosler's internal engineering team and technical partners.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Compensation Model</span>
            <span class="card-badge">Base Salary</span>
          </div>
          <p class="card-p">
            Fully aligned with Wosler's policy: open and flexible to discuss standard competitive base salary ranges during the first introductory conversation.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Immediate Availability</span>
            <span class="card-badge">Day 1 Ready</span>
          </div>
          <p class="card-p">
            Ready to start immediately within 24–48 hours; prepared to set up development environments, review documentation, and pick up initial sprint tasks.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Software Developer Proposal • Wosler Medical Technology</span>
    <span>Page 1 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 2: FULL-STACK ARCHITECTURE & SECURITY ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">FULL-STACK <span style="color:#0f766e;">ARCHITECTURE</span> <span class="brand-badge">Frontend & Backend</span></div>
        <div class="brand-sub">React, TypeScript, RESTful Services, SQL Architecture & Healthcare Security</div>
      </div>
      <div class="meta-block">
        <strong>Frontend:</strong> React • TypeScript • State Management • Responsive UI<br>
        <strong>Backend:</strong> Node.js • Python • REST APIs • Microservices<br>
        <strong>Database:</strong> PostgreSQL • SQL Server • ACID Transactions • Indexing
      </div>
    </div>

    <!-- Section 3: Modern Frontend Engineering -->
    <div class="section">
      <div class="section-title">
        3. Modern Frontend Engineering (React, TypeScript & Clinical UX)
        <span class="tagline">Intuitive, High-Reliability Interfaces for Healthcare Teams and Patients</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">React & TypeScript Component Architecture</span>
            <span class="card-badge">Frontend Core</span>
          </div>
          <p class="card-p">
            Building maintainable, type-safe web applications for clinical environments:
          </p>
          <ul class="card-bullets">
            <li><strong>Strict Type Safety:</strong> Leveraging TypeScript interfaces to eliminate runtime errors across complex clinical data models (demographics, study metadata, doctor orders).</li>
            <li><strong>Modular Reusable Design System:</strong> Building accessible, responsive component libraries ensuring consistent UX across reception desks, sonographer tablets, and patient portals.</li>
            <li><strong>Optimized State Management:</strong> Implementing React Query / Zustand for efficient server-state caching, eliminating redundant network calls during busy clinic shifts.</li>
            <li><strong>Error Boundaries & Resilient UX:</strong> Designing graceful degradation so clinical staff never experience white-screen crashes during active patient consultations.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Clinic Operations & Patient-Facing Applications</span>
            <span class="card-badge">Clinical Workflows</span>
          </div>
          <p class="card-p">
            Engineering software tailored for fast-paced clinic operations:
          </p>
          <ul class="card-bullets">
            <li><strong>Patient Intake & Check-in:</strong> Self-service digital check-in flows capturing health cards, requisition uploads, and medical history with clear validation.</li>
            <li><strong>Clinic Scheduling & Queue Boards:</strong> Real-time room and modality status views (Ultrasound, X-ray) that minimize patient wait times and track technologist utilization.</li>
            <li><strong>Requisition & Document Viewers:</strong> Rapid document rendering with zooming, annotation, and metadata extraction to assist clinical coordinators.</li>
            <li><strong>Offline-Tolerant Patterns:</strong> Optimistic client updates with background queue retries for clinics operating in remote areas with intermittent connectivity.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 4: Backend Services & Database Design -->
    <div class="section">
      <div class="section-title">
        4. Backend Services, REST APIs & Relational Database Design
        <span class="tagline">High-Throughput, ACID-Guaranteed Data Management</span>
      </div>
      <div class="grid-3">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">RESTful API Design</span>
            <span class="card-badge">Services</span>
          </div>
          <p class="card-p">
            Designing clean, versioned REST endpoints with OpenAPI/Swagger contracts, predictable JSON schemas, semantic HTTP status codes, and rate limiting.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Relational SQL Schemas</span>
            <span class="card-badge">Integrity</span>
          </div>
          <p class="card-p">
            Architecting normalized schemas in PostgreSQL and SQL Server with foreign key constraints, composite B-tree indexes, and optimized query plans.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">ACID Data Guarantees</span>
            <span class="card-badge">Reliability</span>
          </div>
          <p class="card-p">
            Enforcing strict database transaction boundaries and idempotent write endpoints, guaranteeing zero duplicate orders and zero dropped patient records.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 5: Application Security & Health Information Privacy -->
    <div class="section">
      <div class="section-title">
        5. Application Security & Healthcare Data Privacy (PIPEDA / HIPAA Standards)
        <span class="tagline">Protecting Sensitive Patient Health Information (PHI) Across Canadian Jurisdictions</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Authentication & Access Control</span>
            <span class="card-badge">Identity</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Role-Based Access Control (RBAC):</strong> Enforcing granular permission tiers separating receptionists, sonographers, radiologist readers, and clinic managers.</li>
            <li><strong>OAuth2 & JWT Token Architecture:</strong> Secure token generation with short TTLs, rotating refresh tokens, and CSRF/XSS protection.</li>
            <li><strong>Multi-Factor Authentication (MFA):</strong> Mandating MFA protocols for administrative and clinical access points to meet healthcare audit standards.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Data Protection & Audit Traceability</span>
            <span class="card-badge">Privacy Compliance</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Encryption Standards:</strong> Enforcing TLS 1.3 for data in transit and AES-256 for data at rest across database tables and imaging file storage.</li>
            <li><strong>Immutable Audit Trails:</strong> Logging all clinical chart views, export actions, and modifications to satisfy provincial privacy regulations (e.g., Alberta HIA).</li>
            <li><strong>Data Sanitization & De-Identification:</strong> Masking patient health card numbers and personal identifiers in test fixtures and logging outputs.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Quality Callout -->
    <div class="callout-box">
      <div class="callout-title">Software Engineering Hygiene & Quality Assurance</div>
      <div class="callout-text">
        High code standards are non-negotiable in healthcare technology. I build automated unit test suites (Jest/PyTest) for business validation rules, integration tests for API contracts, and perform thorough manual smoke testing before submitting clean, well-documented pull requests.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Software Developer Proposal • Wosler Medical Technology</span>
    <span>Page 2 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 3: CLOUD, MEDTECH & AI INTEGRATION ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">CLOUD & <span style="color:#0f766e;">MEDTECH</span> <span class="brand-badge">AWS, AI & Standards</span></div>
        <div class="brand-sub">AWS Cloud Architecture, Docker, AI Integration & Diagnostic Imaging Protocols</div>
      </div>
      <div class="meta-block">
        <strong>Cloud:</strong> AWS (S3, Lambda, EC2, RDS) • Docker • Linux<br>
        <strong>MedTech Protocols:</strong> DICOM • PACS/RIS • HL7 / FHIR Awareness<br>
        <strong>AI Integration:</strong> LLM APIs • Structured Parsing • Audio Transcription
      </div>
    </div>

    <!-- Section 6: AWS Cloud & DevOps -->
    <div class="section">
      <div class="section-title">
        6. AWS Cloud Infrastructure, Containerization & CI/CD
        <span class="tagline">Scalable, Resilient Hosting for Distributed Clinical Networks</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">AWS Healthcare Cloud Services</span>
            <span class="card-badge">AWS Stack</span>
          </div>
          <p class="card-p">
            Hands-on experience deploying and managing cloud workloads on AWS:
          </p>
          <ul class="card-bullets">
            <li><strong>Amazon S3 for Medical Storage:</strong> High-throughput, HIPAA/PIPEDA-compliant storage for ultrasound/X-ray studies, using pre-signed URLs and lifecycle archiving.</li>
            <li><strong>AWS Lambda Serverless Workers:</strong> Triggering event-driven background tasks (DICOM metadata indexing, automated report notifications, batch data sync).</li>
            <li><strong>Amazon RDS (PostgreSQL):</strong> Multi-AZ high-availability database instances with automated encrypted daily backups and point-in-time recovery.</li>
            <li><strong>AWS IAM Security:</strong> Principle of least privilege with strictly scoped role-based access for services and developers.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Docker, Linux & CI/CD Deployment Pipelines</span>
            <span class="card-badge">DevOps Automation</span>
          </div>
          <p class="card-p">
            Building repeatable, containerized deployment pipelines:
          </p>
          <ul class="card-bullets">
            <li><strong>Docker Containerization:</strong> Packaging frontend apps and backend microservices into lightweight, reproducible Alpine/Debian Linux containers.</li>
            <li><strong>GitHub Actions CI/CD:</strong> Automated pipelines running linters, TypeScript type checks, unit tests, and security dependency scans on every commit.</li>
            <li><strong>Production Rollouts:</strong> Staged release environments (Dev ➔ Staging ➔ Production) enabling zero-downtime rolling updates across clinic endpoints.</li>
            <li><strong>Environment Configuration:</strong> Managing secrets and environment variables cleanly through secure key management (AWS Secrets Manager / SSM).</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 7: Medical Software Standards & Diagnostic Imaging -->
    <div class="section">
      <div class="section-title">
        7. ISO 13485 & Diagnostic Imaging Interoperability Awareness
        <span class="tagline">Engineering within Regulated Medical Device & Quality Management Frameworks</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">ISO 13485 & MDSAP</span>
            <span class="card-badge">Compliance</span>
          </div>
          <p class="card-p">
            Familiar with the rigorous documentation, traceability (IEC 62304), and verification standards required for certified medical device software operating in clinical clinics.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">DICOM & PACS/RIS</span>
            <span class="card-badge">Imaging Flow</span>
          </div>
          <p class="card-p">
            Strong architectural understanding of diagnostic imaging pipelines: DICOM study metadata, C-STORE transfers, PACS image archiving, and RIS scheduling integration.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">HL7 & FHIR Standards</span>
            <span class="card-badge">Interoperability</span>
          </div>
          <p class="card-p">
            Grounded in modern health data exchange: mapping clinical events to FHIR resources (<code>Patient</code>, <code>ImagingStudy</code>, <code>DiagnosticReport</code>) for hospital interoperability.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 8: AI & Automation in Clinic Operations -->
    <div class="section">
      <div class="section-title">
        8. AI-Powered Healthcare Tools, LLMs & Workflow Automation
        <span class="tagline">Practical AI Solutions That Streamline Clinical Operations and Reduce Provider Fatigue</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Intelligent Requisition & Triage Automation</span>
            <span class="card-badge">Document AI</span>
          </div>
          <p class="card-p">
            Integrating LLMs and optical character recognition (OCR) to parse incoming doctor referral PDFs, automatically extracting patient demographics, requested examination protocols, and urgency flags into structured database records to accelerate scheduling.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Medical Audio Transcription & Structured Reporting</span>
            <span class="card-badge">Voice & Reporting</span>
          </div>
          <p class="card-p">
            Connecting speech-to-text models (e.g., fine-tuned Whisper) to transcribe radiologist and sonographer audio findings in real time, automatically populating standardized diagnostic report templates with human-in-the-loop review safeguards.
          </p>
        </div>
      </div>
    </div>

    <!-- Engineering Mindset Callout -->
    <div class="callout-box">
      <div class="callout-title">The Seed-Stage Engineering Mindset</div>
      <div class="callout-text">
        As Wosler grows post-seed, software development requires both agility and discipline. I bring an entrepreneurial, curious problem-solving attitude: comfortable tackling undefined problems, working across the entire technology stack, and taking pride in getting working, dependable software into the hands of clinical teams.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Software Developer Proposal • Wosler Medical Technology</span>
    <span>Page 3 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 4: GOVERNANCE, CASE STUDIES & ONBOARDING ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">DELIVERY & <span style="color:#0f766e;">GOVERNANCE</span> <span class="brand-badge">Case Studies & Plan</span></div>
        <div class="brand-sub">Engineering Track Record, Project Management Support & 30-Day Value Roadmap</div>
      </div>
      <div class="meta-block">
        <strong>Software Engineering:</strong> Viranga Lakshan (Full-Stack Engineer)<br>
        <strong>Project Management:</strong> Lithumitha Ravikumar (Project Manager)<br>
        <strong>Readiness:</strong> Immediate Start • Full-Time Remote
      </div>
    </div>

    <!-- Section 9: Dedicated Team Governance -->
    <div class="section">
      <div class="section-title">
        9. Team Allocation & Professional Roles
        <span class="tagline">Clear Engineering Execution Backed by Dedicated Project Management</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Viranga Lakshan</span>
            <span class="card-badge">Full-Stack Software Developer</span>
          </div>
          <p class="card-p"><strong>Primary Software Engineering Lead</strong></p>
          <ul class="card-bullets">
            <li>Personally responsible for full-stack software development across React, TypeScript, APIs, and databases.</li>
            <li>Designs, tests, and deploys clinical tools, workflow automations, and backend services.</li>
            <li>Troubleshoots production issues, investigates performance bottlenecks, and maintains automated test suites.</li>
            <li>Collaborates directly with the CSO, internal engineering teams, and contracted development partners.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Lithumitha Ravikumar</span>
            <span class="card-badge">Project Manager</span>
          </div>
          <p class="card-p"><strong>Dedicated Project Management Support</strong></p>
          <ul class="card-bullets">
            <li>Coordinates sprint schedules, requirements traceability, and delivery milestones.</li>
            <li>Manages documentation quality assurance to support ISO 13485 and MDSAP compliance workflows.</li>
            <li>Maintains cross-functional communication, issue tracking, and sprint status reporting.</li>
            <li><em>Note: Role is dedicated project management and delivery coordination.</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 10: Relevant Production Case Studies -->
    <div class="section">
      <div class="section-title">
        10. Relevant Production Case Studies
        <span class="tagline">Demonstrated Technical Excellence in Mission-Critical, Distributed Systems</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">High-Throughput Mobile & Clinic Network (MFCS)</span>
            <span class="card-badge">400+ Sites • 1M+ Daily Writes</span>
          </div>
          <p class="card-p">
            <strong>Architecture & Scope:</strong> Distributed transaction and record collection platform across 400+ nationwide retail branch sites:
          </p>
          <ul class="card-bullets">
            <li><strong>0.00% Record Loss:</strong> Strict ACID transaction boundaries processing 1,000,000+ daily operational records with zero data loss.</li>
            <li><strong>Zero Database Freezes:</strong> Eliminated row-level lock contention, reducing lock wait times from 1,450 ms to 45 ms.</li>
            <li><strong>Cloud Modernization:</strong> Migrated database workloads to AWS RDS with continuous production uptime.</li>
          </ul>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Healthcare Portfolio & Analytics Platform</span>
            <span class="card-badge">Security & Analytics</span>
          </div>
          <p class="card-p">
            <strong>Architecture & Scope:</strong> Secure, multi-tenant analytics and reporting portal for institutional stakeholders:
          </p>
          <ul class="card-bullets">
            <li><strong>React & TypeScript UI:</strong> Interactive, high-density data visualizations and role-gated reporting dashboards.</li>
            <li><strong>Audit & Security Compliance:</strong> Role-based access control (RBAC), multi-tenant data isolation, and encrypted audit trails.</li>
            <li><strong>Automated Testing:</strong> Comprehensive Jest and Cypress test coverage ensuring zero-regression releases.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 11: 30-Day Onboarding Plan -->
    <div class="section">
      <div class="section-title">
        11. Rapid 30-Day Onboarding & Value Delivery Roadmap
        <span class="tagline">Structured Transition to Accelerate Wosler's Clinical Software Velocity</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 1 – 10: Ramp-Up</span>
            <span class="card-badge">Foundation</span>
          </div>
          <p class="card-p">
            Set up local dev environment, review architecture and ISO 13485 guidelines, shadow clinic workflows, and ship first bug fix / UI enhancement PR.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 11 – 20: Feature Velocity</span>
            <span class="card-badge">Execution</span>
          </div>
          <p class="card-p">
            Take ownership of full-stack sprint tickets (React, REST APIs, SQL), write automated tests, participate in code reviews, and optimize clinic tools.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 21 – 30: Autonomous Drive</span>
            <span class="card-badge">Ownership</span>
          </div>
          <p class="card-p">
            Lead end-to-end feature implementations independently, contribute to AI/automation initiatives, and actively support production deployments.
          </p>
        </div>
      </div>
    </div>

    <!-- Immediate Kickoff Callout -->
    <div class="callout-box" style="margin-top: 4px;">
      <div class="callout-title">Ready for Initial Technical Conversation & Interview</div>
      <div class="callout-text">
        I am available immediately for an introductory conversation with the CSO and engineering leadership to discuss Wosler’s software roadmap, review code samples, and explore how my full-stack skills can support your clinic network.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Software Developer Proposal • Wosler Medical Technology</span>
    <span>Page 4 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\Wosler_Medical_Software_Developer"
    html_path = os.path.join(base_dir, "proposal.html")
    pdf_path = os.path.join(base_dir, "Viranga_Lakshan_Wosler_Software_Developer_Proposal.pdf")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"HTML written to {html_path}")

    msedge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    msedge_bin = None
    for p in msedge_paths:
        if os.path.exists(p):
            msedge_bin = p
            break

    if not msedge_bin:
        raise FileNotFoundError("Microsoft Edge executable not found.")

    cmd = [
        msedge_bin,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]

    subprocess.run(cmd, check=True)
    print(f"PDF generated at {pdf_path}")

    pdf = pdfium.PdfDocument(pdf_path)
    total_pages = len(pdf)
    print(f"Total page count: {total_pages}")

    for i in range(total_pages):
        page = pdf[i]
        image = page.render(scale=2.0).to_pil()
        preview_path = os.path.join(base_dir, f"page_{i+1}.png")
        image.save(preview_path)
        print(f"Rendered page {i+1} to {preview_path}")

    success = (total_pages == 4)
    print(f"Success (exactly 4 pages): {success}")
    return success

if __name__ == "__main__":
    generate_pdf()
