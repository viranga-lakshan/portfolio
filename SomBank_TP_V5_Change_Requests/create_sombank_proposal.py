import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>SomBank TP V5 Change Requests Engineering Proposal - Sadak Samatar</title>
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
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 8.7pt;
    line-height: 1.4;
  }
  .page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    padding: 13mm 16mm 12mm 16mm;
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

  /* Header Bar */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 8px;
    margin-bottom: 11px;
  }
  .brand-title {
    font-size: 14pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-badge {
    background: #2563eb;
    color: #ffffff;
    font-size: 7.2pt;
    font-weight: 700;
    padding: 2.5px 7px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .brand-sub {
    font-size: 8.2pt;
    color: #475569;
    font-weight: 600;
    margin-top: 2px;
  }
  .meta-block {
    text-align: right;
    font-size: 8pt;
    color: #64748b;
    line-height: 1.35;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Hero Banner */
  .hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #2563eb 100%);
    color: #ffffff;
    border-radius: 6px;
    padding: 11px 14px;
    margin-bottom: 11px;
  }
  .hero-title {
    font-size: 12pt;
    font-weight: 800;
    letter-spacing: -0.3px;
    margin: 0 0 4px 0;
    color: #ffffff;
  }
  .hero-desc {
    font-size: 8.2pt;
    color: #e2e8f0;
    margin: 0 0 9px 0;
    line-height: 1.38;
  }
  .hero-pills {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }
  .hero-pill {
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.22);
    padding: 2.5px 7.5px;
    border-radius: 4px;
    font-size: 7.3pt;
    font-weight: 600;
    color: #f8fafc;
  }
  .hero-pill strong {
    color: #60a5fa;
  }

  /* Section Styling */
  .section {
    margin-bottom: 10px;
  }
  .section-title {
    font-size: 9.4pt;
    font-weight: 800;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-left: 3.5px solid #2563eb;
    padding-left: 7px;
    margin: 0 0 6px 0;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .section-title .tagline {
    font-size: 7.5pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
  }

  /* Cards & Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 8px 10px;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 3.5px;
  }
  .card-title {
    font-size: 8.6pt;
    font-weight: 700;
    color: #0f172a;
  }
  .card-badge {
    font-size: 6.8pt;
    font-weight: 700;
    padding: 2px 5px;
    border-radius: 3px;
    background: #eff6ff;
    color: #1d4ed8;
    text-transform: uppercase;
  }
  .card-p {
    font-size: 7.9pt;
    color: #334155;
    margin: 0 0 4.5px 0;
    line-height: 1.34;
  }
  .card-bullets {
    margin: 0;
    padding-left: 14px;
    font-size: 7.7pt;
    color: #475569;
    line-height: 1.34;
  }
  .card-bullets li {
    margin-bottom: 2.5px;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.6pt;
    margin-top: 3px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 4.5px 7px;
    font-weight: 700;
    font-size: 7.4pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  table.matrix-table td {
    padding: 5px 7px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
  }
  table.matrix-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  table.matrix-table td strong {
    color: #0f172a;
  }

  /* Team member card */
  .member-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #2563eb;
    border-radius: 5px;
    padding: 8px 9px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .member-name {
    font-size: 9.3pt;
    font-weight: 800;
    color: #0f172a;
  }
  .member-role {
    font-size: 7.6pt;
    font-weight: 700;
    color: #2563eb;
    text-transform: uppercase;
    margin-bottom: 3px;
  }
  .member-creds {
    font-size: 7.2pt;
    color: #64748b;
    margin-bottom: 5px;
    line-height: 1.28;
  }
  .skill-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 3px;
    margin-top: 4px;
  }
  .chip {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: #334155;
    font-size: 6.7pt;
    font-weight: 600;
    padding: 1.5px 4px;
    border-radius: 3px;
  }

  /* Diagram block */
  .diagram-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 7px 9px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.1pt;
    color: #0f172a;
    line-height: 1.34;
    margin-top: 4px;
  }

  /* Callout */
  .callout-box {
    background: #f0fdf4;
    border-left: 3.5px solid #16a34a;
    border-radius: 4px;
    padding: 6.5px 9px;
    margin-top: 5px;
  }
  .callout-title {
    font-size: 7.9pt;
    font-weight: 700;
    color: #15803d;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.5pt;
    color: #166534;
    line-height: 1.34;
    margin: 0;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 4.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #2563eb;
    text-decoration: none;
    margin-left: 10px;
    font-weight: 600;
  }
</style>
</head>
<body>

<!-- ========================================== PAGE 1 ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">
          FinTech & Banking Engineering Squad <span class="brand-badge">SomBank TP V5</span>
        </div>
        <div class="brand-sub">.NET Framework Architecture • Angular Single-Page Apps • Banking Change Requests & Zero Regression</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> Sadak Samatar, CTO — SomBank<br>
        <strong>Platform:</strong> Transaction Platform V5 (TP V5 — 2-Year Ongoing Engine)<br>
        <strong>Capacity:</strong> 2 Dedicated Full-Stack Engineers + Project Manager<br>
        <strong>Commitment:</strong> Contract-to-Hire Available • Strict NDA Ready
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">TP V5 Change Request Execution: Precision .NET & Angular Banking Engineering</div>
      <div class="hero-desc">
        A senior, battle-tested FinTech engineering squad ready to assume ownership of SomBank's confidential Change Request (CR) backlog for the flagship Transaction Platform (TP V5). Combining deep .NET Framework backend architecture, responsive Angular client applications, immutable audit logging, and zero-regression verification to safeguard live banking operations.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Backend: <strong>.NET Framework • C# • Web API • SQL Server</strong></div>
        <div class="hero-pill">Frontend: <strong>Angular (SPA) • TypeScript • HTML5/CSS3</strong></div>
        <div class="hero-pill">Domain: <strong>FinTech • Core Banking • Transaction Integrity</strong></div>
        <div class="hero-pill">Security: <strong>OAuth2 / JWT • OWASP • Strict Confidentiality</strong></div>
        <div class="hero-pill">Delivery: <strong>Fast Impact Analysis • Automated Regression Testing</strong></div>
      </div>
    </div>

    <!-- Executive Overview -->
    <div class="section">
      <div class="section-title">
        1. Executive Summary & Delivery Approach
        <span class="tagline">Engineered for a Mature 2-Year Production Banking Core</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Managing Change Requests on Mature Banking Systems</span>
            <span class="card-badge">Risk Awareness</span>
          </div>
          <p class="card-p">
            A banking platform running continuously for nearly two years under CTO leadership represents mature, mission-critical infrastructure where even minor modifications carry operational risk:
          </p>
          <ul class="card-bullets">
            <li><strong>Zero-Regression Mandate:</strong> New feature requests and workflow alterations must never disrupt existing customer balance calculations, payment clearing, or third-party API hooks.</li>
            <li><strong>Confidentiality & Compliance:</strong> SomBank's change specifications contain sensitive financial rules and institutional workflows requiring strict NDA protocol and isolated testing.</li>
            <li><strong>Handoff Continuity:</strong> Smoothly bridging the transition from the former CTO account to CTO Sadak Samatar with clean git history, documented code, and architectural consistency.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Dedicated Squad Advantage for SomBank</span>
            <span class="card-badge">Two-Engineer Capacity</span>
          </div>
          <p class="card-p">
            SomBank is seeking two engineers to accelerate TP V5 change delivery. Our squad delivers the exact dual-engineer throughput plus project governance:
          </p>
          <ul class="card-bullets">
            <li><strong>Senior .NET & Backend Architect (Viranga Lakshan):</strong> Manages C# .NET Web APIs, transaction orchestration, database integrity, and banking security protocols.</li>
            <li><strong>Angular & Frontend/Database Developer (Janith Kavishka):</strong> Specializes in Angular component architecture, responsive financial dashboards, and SQL Server transaction tracking.</li>
            <li><strong>FinTech Delivery Project Manager (Lithumitha Ravikumar):</strong> Oversees CR traceability, QA acceptance test validation, and zero-regression signoff.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Scope Alignment Table -->
    <div class="section">
      <div class="section-title">
        2. Technical Scope & Capabilities Alignment Matrix
        <span class="tagline">Direct Alignment with SomBank TP V5 Requirements</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">SomBank TP V5 Requirement</th>
            <th style="width: 42%;">Squad Implementation & Engineering Standard</th>
            <th style="width: 33%;">Verified Production Precedents</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>.NET Framework Backend Architecture</strong></td>
            <td>C# / .NET Web API development, Entity Framework / Dapper database layers, business logic encapsulation, and asynchronous task execution.</td>
            <td>Architected enterprise C# / .NET components, RESTful API gateways, and multi-service business domain logic.</td>
          </tr>
          <tr>
            <td><strong>Angular Single-Page Application (SPA)</strong></td>
            <td>Modern Angular architecture, RxJS reactive state management, modular components, TypeScript typing, and CSS/HTML responsive financial UI.</td>
            <td>Built complex financial tracking dashboards, approval matrices, and customer/admin portals with real-time UI states.</td>
          </tr>
          <tr>
            <td><strong>FinTech & Transaction Integrity</strong></td>
            <td>Double-entry accounting models, idempotency keys, ACID-compliant database transactions, ledger reconciliation, and tamper-evident audit trails.</td>
            <td>Engineered nationwide financial field collection & receipting for SINGER PLC and 3-way reconciliation engine (*InvoiceIQ*).</td>
          </tr>
          <tr>
            <td><strong>Confidential Change Request (CR) Protocol</strong></td>
            <td>Formal impact analysis before modifying code: dependency mapping, database schema regression checks, and isolated staging validation.</td>
            <td>Enterprise change management on multi-tenant SaaS commerce platforms and multi-squad delivery governance.</td>
          </tr>
          <tr>
            <td><strong>Banking Security & Access Control</strong></td>
            <td>Role-Based Access Control (RBAC), OAuth2 / JWT authentication, data-at-rest & in-transit encryption, and OWASP Top 10 hardening.</td>
            <td>Implemented Keycloak OAuth2/OIDC token verification middleware, secure S3 pipelines, and ClamAV antivirus scanning.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">Immediate Availability & Confidential NDA Execution</div>
      <div class="callout-text">
        We are prepared to sign SomBank's Non-Disclosure Agreement (NDA) immediately upon Upwork contract initiation. Our squad is fully available for long-term engagement and contract-to-hire consideration under CTO Sadak Samatar's direct supervision.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SomBank • TP V5 Change Requests Engineering Proposal</span>
    <span>Page 1 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 2 ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">Full-Stack .NET & Angular Banking Engine <span class="brand-badge">Architecture</span></div>
        <div class="brand-sub">Robust Engineering for High-Throughput Financial Systems</div>
      </div>
      <div class="meta-block">
        <strong>Stack:</strong> .NET Framework + Angular (SPA)<br>
        <strong>Database:</strong> SQL Server / ACID Compliant<br>
        <strong>Methodology:</strong> Zero-Regression Impact Analysis
      </div>
    </div>

    <!-- Technical Architecture -->
    <div class="section">
      <div class="section-title">
        3. Full-Stack Banking Architecture (.NET Framework + Angular)
        <span class="tagline">Enterprise Modularity Designed for Maintainability and Scale</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Backend: .NET Framework & Secure APIs</span>
            <span class="card-badge">C# / Web API</span>
          </div>
          <p class="card-p">
            We write clean, idiomatic C# .NET code following enterprise Domain-Driven Design (DDD) principles:
          </p>
          <ul class="card-bullets">
            <li><strong>Service & Repository Layering:</strong> Strict decoupling of business domain rules from data persistence and controller endpoints, ensuring changes in logic do not corrupt persistence.</li>
            <li><strong>Defensive Transaction Processing:</strong> Wrapping multi-step banking operations in strict database transactions with distributed locking and rollback safeguards.</li>
            <li><strong>High-Performance Data Access:</strong> Optimizing Entity Framework / ADO.NET / Dapper queries, avoiding N+1 bottlenecks, and enforcing database query execution time limits.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Frontend: Angular Component Architecture</span>
            <span class="card-badge">TypeScript / CSS</span>
          </div>
          <p class="card-p">
            Modern, maintainable Angular client engineering for seamless banking portal user experiences:
          </p>
          <ul class="card-bullets">
            <li><strong>Reactive State Management:</strong> Clean RxJS observables, behavior subjects, and centralized state stores preventing race conditions in financial forms.</li>
            <li><strong>Modular Feature Modules:</strong> Lazy-loaded modules for transactions, approvals, customer profiles, and reports ensuring fast initial load times.</li>
            <li><strong>Strict Validation & UI Guardrails:</strong> Real-time form validation, currency masking, decimal precision formatting, and double-click prevention on payment execution buttons.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Zero-Regression Engineering Protocol -->
    <div class="section">
      <div class="section-title">
        4. Confidential Change Request (CR) Execution Protocol
        <span class="tagline">4-Step Discipline to Ensure Zero Production Regression</span>
      </div>
      <div class="diagram-box">
        [STEP 1: IMPACT AUDIT] ──► [STEP 2: SANDBOX CODING] ──► [STEP 3: REGRESSION QA] ──► [STEP 4: CTO REVIEW]
        • Review Confidential CR   • Branch-isolated feature   • Automated Unit Tests       • Pull Request Walkthrough
        • Map dependent services   • Clean C# / Angular code   • Ledger & Balance Checks    • Zero-Downtime Deployment
        • Identify Schema Changes  • Zero hardcoded configs    • Cross-browser UI verify    • Post-launch verification
      </div>
      <div class="grid-2" style="margin-top: 6px;">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Impact Analysis & Schema Review</span>
            <span class="card-badge">Step 1 & 2</span>
          </div>
          <p class="card-p">
            Before touching existing production code, we review the confidential CR document and generate a technical impact matrix: identifying affected stored procedures, API contracts, and Angular components to prevent unintended side effects.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Automated Testing & Release Governance</span>
            <span class="card-badge">Step 3 & 4</span>
          </div>
          <p class="card-p">
            Every change is validated against regression test suites verifying that existing transaction workflows, balance updates, and export reports function identically. Code is delivered via atomic git commits with clear pull request summaries.
          </p>
        </div>
      </div>
    </div>

    <!-- Security & Audit Governance -->
    <div class="section">
      <div class="section-title">
        5. Banking Security, Audit Logging & Compliance
        <span class="tagline">Protecting Sensitive Somali Banking Data & Transactions</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Immutable Audit Trails</span>
            <span class="card-badge">Auditability</span>
          </div>
          <p class="card-p">
            Every state-changing operation records who, what, when, IP address, and previous state into tamper-evident database audit tables for regulatory compliance.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">OWASP Hardening</span>
            <span class="card-badge">App Security</span>
          </div>
          <p class="card-p">
            Protection against SQL Injection, Cross-Site Scripting (XSS), CSRF token validation, input sanitization, and secure HTTP-only cookie headers.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Least-Privilege RBAC</span>
            <span class="card-badge">Access Control</span>
          </div>
          <p class="card-p">
            Granular permissions mapping ensuring branch staff, compliance officers, and system administrators only access authorized financial workflows.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SomBank • TP V5 Change Requests Engineering Proposal</span>
    <span>Page 2 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 3 ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">Verified FinTech & Enterprise Experience <span class="brand-badge">Track Record</span></div>
        <div class="brand-sub">Production Banking, Payment Processing, and Enterprise .NET Systems</div>
      </div>
      <div class="meta-block">
        <strong>Domain Precedents:</strong> FinTech & Financial Operations<br>
        <strong>Backend Tech:</strong> .NET Framework, C#, Java/Spring, SQL<br>
        <strong>Frontend Tech:</strong> Angular, React, TypeScript
      </div>
    </div>

    <!-- Case Studies -->
    <div class="section">
      <div class="section-title">
        6. Enterprise Production Case Studies
        <span class="tagline">Real Financial and Enterprise Systems Delivered by Squad Members</span>
      </div>

      <!-- SINGER PLC -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">Enterprise Financial Field Collection & Receipting Platform</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: SINGER Sri Lanka PLC (DMS Electronics) • Janith Kavishka</span>
          </div>
          <span class="card-badge">Financial Workflows</span>
        </div>
        <p class="card-p">
          <strong>Mission-Critical Financial Platform:</strong> Designed and developed a field financial collection and receipt management platform handling batch-wise transaction tracking, mobile receipt generation, and real-time reconciliation for nationwide retail and consumer finance.
        </p>
        <ul class="card-bullets">
          <li><strong>Database Integrity & Migration:</strong> Executed complete zero-downtime database migration to Amazon RDS (MySQL) with zero loss across millions of financial records.</li>
          <li><strong>Message-Driven Event Streaming:</strong> Implemented RabbitMQ message queues to guarantee asynchronous, decoupled processing of high-volume financial transactions.</li>
          <li><strong>Continuous Production Operations:</strong> Provided ongoing system design and production operational support ensuring uninterrupted uptime for island-wide branch operations.</li>
        </ul>
      </div>

      <!-- DIMO Lanka -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">DIMO Enterprise Gate Pass & Logistics Management System</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: DIMO Lanka (Enterprise Logistics) • Viranga Lakshan</span>
          </div>
          <span class="card-badge">Security & SAP ERP</span>
        </div>
        <p class="card-p">
          <strong>High-Security Enterprise Platform:</strong> Architected API gateway and core domain services managing vehicle gate pass dispatch, SAP ERP financial integration, and multi-role approval hierarchies.
        </p>
        <ul class="card-bullets">
          <li><strong>Keycloak OAuth2 / JWT Security:</strong> Handled centralized authentication, token verification middleware, and granular role-based authorization for multi-level managers.</li>
          <li><strong>Event-Driven Audit Trails:</strong> Integrated Spring Kafka publishing immutable audit events for all approvals, rejections, and material movements.</li>
          <li><strong>Secure File Handling with ClamAV:</strong> Engineered AWS S3 upload pipeline with automated asynchronous virus scanning and quarantine buckets.</li>
        </ul>
      </div>

      <!-- C# .NET & Guardian Funds Grid -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Enterprise C# & .NET Integrations</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Al Ain Museum & Holsten Arabia</span>
            </div>
            <span class="card-badge">.NET & C#</span>
          </div>
          <p class="card-p">
            Developed and customized C# / .NET backend components, Sitecore Helix architecture, and RESTful service integrations supporting enterprise content and transaction delivery.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Guardian Funds Financial Dashboard</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Guardian Funds (Australia)</span>
            </div>
            <span class="card-badge">FinTech PM</span>
          </div>
          <p class="card-p">
            Managed delivery of investment portfolio analytics dashboard and corporate investment platform. Coordinated QA test validation against strict financial acceptance criteria.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SomBank • TP V5 Change Requests Engineering Proposal</span>
    <span>Page 3 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 4 ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">Execution Roadmap & Squad Profiles <span class="brand-badge">Delivery</span></div>
        <div class="brand-sub">Structured Phasing, Team Expertise, and Immediate Onboarding for SomBank</div>
      </div>
      <div class="meta-block">
        <strong>Budget Alignment:</strong> $5,796 Milestone Scope<br>
        <strong>Model:</strong> 2 Dedicated Engineers + PM<br>
        <strong>Availability:</strong> Immediate Start • Full-Time Overlap
      </div>
    </div>

    <!-- Phased Execution Plan -->
    <div class="section">
      <div class="section-title">
        7. Phased Change Request Implementation Plan
        <span class="tagline">Systematic Execution from Confidential Document Ingestion to Deployment</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Confidential Ingestion & Architecture Audit</span>
            <span class="card-badge">Days 1–3</span>
          </div>
          <ul class="card-bullets">
            <li>Execute Upwork contract and sign SomBank Non-Disclosure Agreement (NDA).</li>
            <li>Receive confidential TP V5 change request documentation from CTO Sadak Samatar.</li>
            <li>Review existing .NET Framework solution structure, Angular SPA repo, and SQL Server schema.</li>
            <li>Deliver technical Change Impact Matrix and milestone breakdown for CTO signoff.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: .NET Backend & API Implementation</span>
            <span class="card-badge">Sprint 1</span>
          </div>
          <ul class="card-bullets">
            <li>Implement backend C# / .NET changes: updated endpoints, business logic services, and models.</li>
            <li>Execute safe database schema migrations, stored procedure updates, and index tuning.</li>
            <li>Enforce transaction isolation, parameter validation, and comprehensive unit tests.</li>
            <li>Provide staging API endpoints with Swagger/Postman documentation for frontend consumption.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: Angular Frontend & UI/UX Enhancements</span>
            <span class="card-badge">Sprint 2</span>
          </div>
          <ul class="card-bullets">
            <li>Build and refactor Angular components, templates (HTML5), and styling (CSS3/SCSS).</li>
            <li>Integrate updated .NET REST APIs with robust error handling and loading indicators.</li>
            <li>Implement client-side field validation, currency masks, and role-based view controls.</li>
            <li>Verify full responsiveness across desktop, tablet, and mobile browsers.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: Regression QA, Handover & Support</span>
            <span class="card-badge">Sprint 3</span>
          </div>
          <ul class="card-bullets">
            <li>Execute end-to-end regression testing across all existing and newly modified workflows.</li>
            <li>Conduct live pull request code review with CTO Sadak Samatar and SomBank tech team.</li>
            <li>Deploy changes to UAT/Staging, support user acceptance testing, and assist production deployment.</li>
            <li>Provide 30 days of warranty support and prepare for ongoing contract-to-hire extension.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Squad Member Profiles -->
    <div class="section">
      <div class="section-title">
        8. Meet The SomBank Engineering Squad
        <span class="tagline">Senior FinTech Specialists Dedicated to TP V5 Success</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Full-Stack / .NET Architect</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Enterprise Systems</div>
            <p class="card-p">
              Leads backend systems architecture, C# / .NET Web API engineering, banking security protocols, OAuth2/JWT integration, and database transactional integrity.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">.NET Framework</span>
            <span class="chip">C# / Web API</span>
            <span class="chip">SQL Server</span>
            <span class="chip">OAuth2 / JWT</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Angular & Database Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Financial Workflows & Full-Stack</div>
            <p class="card-p">
              Specializes in Angular SPA development, TypeScript, responsive CSS/HTML UI, financial transaction tracking, and database query optimization.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Angular (SPA)</span>
            <span class="chip">TypeScript</span>
            <span class="chip">CSS3 / HTML5</span>
            <span class="chip">FinTech Tracking</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Project Manager</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise SaaS & Financial Platforms</div>
            <p class="card-p">
              Manages Change Request traceability, sprint coordination, QA acceptance testing against banking specifications, and technical delivery documentation.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Project Management</span>
            <span class="chip">CR Traceability</span>
            <span class="chip">QA Acceptance</span>
            <span class="chip">Release Governance</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Commercial Alignment & Call to Action -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #2563eb; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Commercial Alignment with SomBank's $5,796 Budget</div>
      <div class="callout-text" style="color: #334155;">
        Our squad is fully aligned with SomBank's fixed-price budget of <strong>$5,796.00</strong>. We are structured to provide the capacity of <strong>two dedicated developers</strong> collaborating seamlessly under one contract, with long-term availability for contract-to-hire extension under CTO Sadak Samatar.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SomBank • TP V5 Change Requests Engineering Proposal</span>
    <span>Page 4 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\SomBank_TP_V5_Change_Requests"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "SomBank_TP_V5_Engineering_Proposal.pdf")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    
    print(f"HTML written to {html_file}")
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Edge error:", res.stderr)
        return False
        
    print(f"PDF generated at {pdf_file}")
    
    # Inspect page count
    pdf = pdfium.PdfDocument(pdf_file)
    page_count = len(pdf)
    print(f"Total page count: {page_count}")
    
    # Render pages to PNG
    for i, page in enumerate(pdf):
        image = page.render(scale=2).to_pil()
        out_img = os.path.join(base_dir, f"page_{i+1}.png")
        image.save(out_img)
        print(f"Rendered page {i+1} to {out_img}")
        
    return page_count == 4

if __name__ == "__main__":
    success = generate_pdf()
    print("Success:", success)
