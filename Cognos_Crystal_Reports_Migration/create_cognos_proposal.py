import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cognos BI Developer - Crystal Reports Migration & Java Spring Boot Integration</title>
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
    border-bottom: 2px solid #0f62fe;
    padding-bottom: 8px;
    margin-bottom: 11px;
  }
  .brand-title {
    font-size: 13.5pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-badge {
    background: #0f62fe;
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
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #0f62fe 100%);
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
    color: #78a9ff;
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
    border-left: 3.5px solid #0f62fe;
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
    background: #edf5ff;
    color: #0043ce;
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

  /* Team member card */
  .member-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #0f62fe;
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
    color: #0f62fe;
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
    color: #0f62fe;
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
          Enterprise BI & Data Solutions Squad <span class="brand-badge">Cognos & Spring Boot</span>
        </div>
        <div class="brand-sub">Crystal Reports Migration • IBM Cognos Analytics • Complex SQL Optimization • Java Spring Boot Embedding</div>
      </div>
      <div class="meta-block">
        <strong>Engagement:</strong> Crystal Reports to Cognos BI Modernization<br>
        <strong>Focus Location:</strong> Richardson, Texas Project Mandate<br>
        <strong>Architecture:</strong> Java Spring Boot Embedded Analytics & RDBMS<br>
        <strong>Model:</strong> 3-Specialist Solutions Squad (Architect + Database DBA + BI PM)
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Cognos Analytics Modernization & Java Spring Boot Embedded Reporting</div>
      <div class="hero-desc">
        A senior enterprise BI and backend engineering squad dedicated to modernizing legacy Crystal Reports into high-performance, interactive IBM Cognos Analytics dashboards. Combining deep relational SQL performance tuning, Framework Manager / Data Module metadata modeling, and seamless RESTful integration into Java Spring Boot enterprise applications.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">BI Core: <strong>IBM Cognos Analytics 11.x / 12.x • Framework Manager</strong></div>
        <div class="hero-pill">Legacy Conversion: <strong>Crystal Reports ➔ Cognos Interactive Reports</strong></div>
        <div class="hero-pill">Backend: <strong>Java 21 / Spring Boot 3.x • RESTful APIs • Security Filters</strong></div>
        <div class="hero-pill">Database: <strong>Complex SQL • Index Optimization • Query Plan Tuning</strong></div>
        <div class="hero-pill">Governance: <strong>Multi-Tenant Row-Level Security • Zero Discrepancy</strong></div>
      </div>
    </div>

    <!-- Executive Summary & Delivery Model -->
    <div class="section">
      <div class="section-title">
        1. Executive Summary & Delivery Approach
        <span class="tagline">Bridging Legacy Reporting with Modern Cloud-Native Application Architecture</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Challenge of Crystal Reports Migration</span>
            <span class="card-badge">Complexity</span>
          </div>
          <p class="card-p">
            Migrating legacy Crystal Reports to IBM Cognos Analytics in an enterprise environment involves far more than simply recreating visual report layouts:
          </p>
          <ul class="card-bullets">
            <li><strong>Embedded Business Logic:</strong> Formulas, conditional suppressions, and subreports trapped in Crystal files must be deconstructed and translated into centralized semantic models.</li>
            <li><strong>SQL Query Bottlenecks:</strong> Unoptimized legacy queries causing slow page loads, lock contention, and database strain under concurrent enterprise reporting loads.</li>
            <li><strong>Spring Boot Application Integration:</strong> Seamlessly embedding Cognos dashboards into existing Java Spring Boot portals with unified OAuth2/JWT security and responsive UI containers.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Triad Squad Advantage for Richardson</span>
            <span class="card-badge">Execution Squad</span>
          </div>
          <p class="card-p">
            Rather than relying on a standalone report writer who lacks backend Java Spring Boot experience, our squad delivers end-to-end integration:
          </p>
          <ul class="card-bullets">
            <li><strong>Lead Java Spring Boot & Integration Architect (Viranga Lakshan):</strong> Connects Cognos RESTful services, Mashup Services, and embedded iframe/token auth into Spring Boot microservices.</li>
            <li><strong>Senior Database & SQL Performance Engineer (Janith Kavishka):</strong> Deconstructs legacy queries, rewrites nested joins into optimized views, and optimizes execution plans.</li>
            <li><strong>BI Delivery Project Manager (Lithumitha Ravikumar):</strong> Led enterprise multi-dashboard platforms (*Castle Visualizer* and *Guardian Funds*), managing QA reconciliation and stakeholder signoffs.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Scope Alignment Matrix -->
    <div class="section">
      <div class="section-title">
        2. Technical Capability Alignment Matrix
        <span class="tagline">Direct Mapping to Richardson Texas Cognos BI Mandate</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">Project Mandate Requirement</th>
            <th style="width: 42%;">Squad Engineering Standard & Approach</th>
            <th style="width: 33%;">Verified Production Precedents</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Crystal Reports Modernization</strong></td>
            <td>Reverse-engineering formulas, parameters, and grouping in Crystal; recreating as interactive, prompt-driven IBM Cognos reports and drill-through dashboards.</td>
            <td>Enterprise analytics consolidation across legacy databases on *Castle Visualizer* (Australia) and ERP systems.</td>
          </tr>
          <tr>
            <td><strong>Cognos Metadata & Data Modeling</strong></td>
            <td>Designing governed semantic layers using Cognos Framework Manager and modern Data Modules; establishing star/snowflake schemas, determinants, and query subjects.</td>
            <td>Multi-tenant schema isolation, domain-driven data models, and enterprise database architecture.</td>
          </tr>
          <tr>
            <td><strong>Advanced SQL Tuning & RDBMS</strong></td>
            <td>Query execution plan analysis, index optimization, eliminating Cartesian joins, partitioning large tables, and implementing materialized reporting views.</td>
            <td>High-volume transaction tracking and zero-downtime database optimization for SINGER Sri Lanka PLC (Amazon RDS).</td>
          </tr>
          <tr>
            <td><strong>Java Spring Boot Integration</strong></td>
            <td>Integrating Cognos Mashup Service (CMS) and REST APIs with Java Spring Boot; securing embedded reports via JWT token delegation and Spring Security filters.</td>
            <td>Architected enterprise Java 21 / Spring Boot 3.4.5 microservices, Keycloak OAuth2/JWT security, and SAP ERP integration for DIMO Lanka.</td>
          </tr>
          <tr>
            <td><strong>Data Discrepancy & Performance QA</strong></td>
            <td>Automated pixel-and-data comparison scripts validating historical Crystal output against newly generated Cognos reports with 100% data reconciliation.</td>
            <td>3-way automated financial reconciliation engine (*InvoiceIQ*) and QA acceptance validation for *Guardian Funds*.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">Full US Central Time (CT) Collaboration & High-Velocity Delivery</div>
      <div class="callout-text">
        Our squad provides active schedule overlap with Richardson, Texas (US Central Time) for daily standups, architectural pairing with backend engineers, and sprint demonstrations. We bring deep international enterprise delivery experience across Australia, Kuwait, UAE, and the US.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cognos BI Developer • Crystal Reports Migration & Java Integration</span>
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
        <div class="brand-title">Migration Methodology & Architecture <span class="brand-badge">Integration</span></div>
        <div class="brand-sub">Structured Crystal-to-Cognos Modernization and Java Spring Boot Embedding</div>
      </div>
      <div class="meta-block">
        <strong>Tooling:</strong> IBM Cognos Analytics • Framework Manager<br>
        <strong>Backend:</strong> Java Spring Boot 3.x • REST APIs<br>
        <strong>Security:</strong> OAuth2 / JWT • Row-Level Data Filtering
      </div>
    </div>

    <!-- 4-Phase Migration Methodology -->
    <div class="section">
      <div class="section-title">
        3. Crystal Reports to Cognos Modernization Framework
        <span class="tagline">A Disciplined, Error-Free 4-Stage Conversion Protocol</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Stage 1: Catalog Audit & Logic Extraction</span>
            <span class="card-badge">Analysis</span>
          </div>
          <p class="card-p">
            We inventory all existing Crystal Reports (`.rpt` files), cataloging data sources, parameters, record selection formulas, sub-reports, conditional suppressions, and visual formatting rules. Redundant and obsolete reports are identified to streamline the reporting catalog.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Stage 2: Semantic Modeling & SQL Tuning</span>
            <span class="card-badge">Data Modeling</span>
          </div>
          <p class="card-p">
            Rather than copying raw SQL into Cognos, we build governed semantic models in <strong>Framework Manager</strong> or Cognos <strong>Data Modules</strong>. Multi-table joins are normalized, calculations are moved to the database layer, and query subjects are tuned for reusable enterprise reporting.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Stage 3: Interactive Cognos Report Authoring</span>
            <span class="card-badge">Modernization</span>
          </div>
          <p class="card-p">
            Reports are rebuilt as modern, responsive IBM Cognos reports: replacing static tabular printouts with interactive drill-throughs, dynamic prompts, conditional formatting, and executive summary KPI dashboards optimized for web and mobile consumption.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Stage 4: Data Validation & Discrepancy Audits</span>
            <span class="card-badge">100% Accuracy</span>
          </div>
          <p class="card-p">
            We run side-by-side automated comparison tests matching historical Crystal Reports outputs against Cognos reports across identical date ranges and parameters, guaranteeing zero arithmetic drift, rounding errors, or missing edge-case rows.
          </p>
        </div>
      </div>
    </div>

    <!-- Java Spring Boot Embedded Analytics Architecture -->
    <div class="section">
      <div class="section-title">
        4. Java Spring Boot Embedded Analytics Architecture
        <span class="tagline">Seamlessly Integrating Cognos Reporting into Your Enterprise Backend</span>
      </div>
      <div class="diagram-box">
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [CLIENT WEB APPLICATION / FRONTEND (Angular / React / Thymeleaf)]                                │
│  └── Requests Embedded Report via Secured Container (iframe / Web SDK / Direct API View)         │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [JAVA SPRING BOOT ENTERPRISE BACKEND SERVICE]                                                    │
│  ├── Spring Security Filter Chain: Validates User JWT, Role (RBAC) & Tenant ID                   │
│  ├── Cognos Integration Service: Calls Cognos REST API / Mashup Service (CMS)                     │
│  │   ├── Generates Single Sign-On (SSO) Trusted Ticket / Session Token                           │
│  │   ├── Injects Dynamic Parameters (e.g., Department, User Organization, Date Range)             │
│  │   └── Retrieves Secure Report URL or Streams Export Output (PDF, XLSX, CSV)                   │
│  └── Audit Logging Service: Logs Report Execution Timestamp, Execution Duration & Accessing User │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [IBM COGNOS ANALYTICS 11.x / 12.x PLATFORM]                                                      │
│  ├── Cognos Gateway & Dispatcher ➔ Executes Framework Manager / Data Module Query                │
│  └── Applies Row-Level Security (Data Filters) Based on Injected User Session Context            │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [ENTERPRISE RELATIONAL DATABASE (SQL Server / Oracle / PostgreSQL)]                              │
│  └── Optimized Queries, Materialized Views & High-Performance Indexes Run in Milliseconds        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
      </div>
    </div>

    <!-- SQL Performance Engineering -->
    <div class="section">
      <div class="section-title">
        5. Advanced SQL Performance & Query Optimization
        <span class="tagline">Slashing Execution Times on Enterprise Reporting Databases</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Execution Plan Analysis</span>
            <span class="card-badge">Query Tuning</span>
          </div>
          <p class="card-p">
            Diagnosing slow SQL by inspecting execution plans: eliminating full table scans, resolving hash match bottlenecks, and rewriting inefficient correlated subqueries.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Indexed & Materialized Views</span>
            <span class="card-badge">Optimization</span>
          </div>
          <p class="card-p">
            Designing targeted composite indexes and materialized reporting views that pre-aggregate massive transaction datasets, delivering instant report responses.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Row-Level Security (RLS)</span>
            <span class="card-badge">Data Isolation</span>
          </div>
          <p class="card-p">
            Enforcing tenant and departmental security directly at the data model level, guaranteeing users only view authorized enterprise data without duplicating report layouts.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cognos BI Developer • Crystal Reports Migration & Java Integration</span>
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
        <div class="brand-title">Enterprise Analytics & Global Precedents <span class="brand-badge">Track Record</span></div>
        <div class="brand-sub">Production BI Dashboards, Java Spring Boot Systems, and Database Performance</div>
      </div>
      <div class="meta-block">
        <strong>Domain Reach:</strong> Enterprise Analytics, ERP & FinTech<br>
        <strong>Backend Tech:</strong> Java 21, Spring Boot 3.x, REST APIs<br>
        <strong>Databases:</strong> SQL Server, Oracle, MySQL, Amazon RDS
      </div>
    </div>

    <!-- Production Case Studies -->
    <div class="section">
      <div class="section-title">
        6. Verified Enterprise Production Case Studies
        <span class="tagline">Real International Systems Delivered by Squad Members</span>
      </div>

      <!-- Castle Visualizer -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">Castle Visualizer — Enterprise Data & Multi-Dashboard Analytics Platform</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: Castle Group (Australia) • PM: Lithumitha Ravikumar</span>
          </div>
          <span class="card-badge">Enterprise BI</span>
        </div>
        <p class="card-p">
          <strong>Cross-System Enterprise Analytics Consolidation:</strong> Led the end-to-end delivery of an enterprise multi-dashboard analytics platform, consolidating disparate operational data from multiple legacy systems into a unified, high-performance reporting environment.
        </p>
        <ul class="card-bullets">
          <li><strong>Stakeholder Requirements & Data Modeling:</strong> Managed comprehensive requirements definition, translating complex corporate KPIs and operational metrics into standardized data structures.</li>
          <li><strong>Sprint Coordination & Quality Assurance:</strong> Coordinated cross-functional engineering teams across data integration, database design, and frontend dashboards to deliver real-time visual insights for C-suite decision-makers.</li>
        </ul>
      </div>

      <!-- DIMO Gate Pass -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">DIMO Enterprise Gate Pass & Logistics Management System</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: DIMO Lanka (Enterprise Logistics) • Lead: Viranga Lakshan</span>
          </div>
          <span class="card-badge">Java Spring Boot 3.x</span>
        </div>
        <p class="card-p">
          <strong>Mission-Critical Java Microservices Architecture:</strong> Architected API Gateway and core domain microservices built with Java 21 and Spring Boot 3.4.5, managing complex approval hierarchies, audit event streaming, and enterprise ERP integration.
        </p>
        <ul class="card-bullets">
          <li><strong>Spring Security & Keycloak OAuth2/JWT:</strong> Implemented centralized token verification, role-based access control (RBAC), and secure REST API services connecting web and mobile clients.</li>
          <li><strong>Enterprise Integrations & Event Logging:</strong> Integrated directly with SAP ERP, Microsoft Graph / Azure AD, and Spring Kafka publishing immutable audit logs for all transactions.</li>
          <li><strong>MySQL Database Migrations:</strong> Managed relational schema design and automated database migrations using Flyway, containerizing services via Docker and CI/CD pipelines.</li>
        </ul>
      </div>

      <!-- SINGER PLC & Guardian Funds Grid -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Financial Reporting & DB Optimization</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">SINGER Sri Lanka PLC • Janith Kavishka</span>
            </div>
            <span class="card-badge">SQL Optimization</span>
          </div>
          <p class="card-p">
            Engineered batch-wise financial transaction tracking and real-time reconciliation systems. Executed full data migration and continuous query tuning on Amazon RDS (MySQL) for nationwide enterprise retail operations.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Guardian Funds Analytics Dashboard</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Guardian Funds (Australia)</span>
            </div>
            <span class="card-badge">Portfolio BI</span>
          </div>
          <p class="card-p">
            Managed delivery of an investment analytics dashboard consolidating financial metrics for senior stakeholder decision-making. Enforced rigorous QA acceptance criteria validating reporting calculations.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cognos BI Developer • Crystal Reports Migration & Java Integration</span>
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
        <div class="brand-title">Phased Roadmap & Squad Profiles <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Structured Delivery Plan, Team Capabilities, and Seamless Richardson Collaboration</div>
      </div>
      <div class="meta-block">
        <strong>Timeline:</strong> 8-Week Phased Migration<br>
        <strong>Timezone:</strong> Overlap with US Central Time (CT)<br>
        <strong>Handover:</strong> Full Technical Documentation & Runbooks
      </div>
    </div>

    <!-- Phased Implementation Roadmap -->
    <div class="section">
      <div class="section-title">
        7. 8-Week Phased Modernization & Integration Roadmap
        <span class="tagline">Systematic Execution Guaranteeing Zero Interruption to Business Operations</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Catalog Audit & SQL Mapping</span>
            <span class="card-badge">Weeks 1–2</span>
          </div>
          <ul class="card-bullets">
            <li>Inventory all legacy Crystal Reports (`.rpt`), identifying parameters, grouping, and sub-reports.</li>
            <li>Extract and document underlying SQL queries, stored procedures, and database dependencies.</li>
            <li>Establish baseline report runtime benchmarks and identify primary query bottlenecks.</li>
            <li>Deliver Crystal-to-Cognos Migration Matrix and prioritize high-value operational reports.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: Data Modeling & Query Tuning</span>
            <span class="card-badge">Weeks 3–4</span>
          </div>
          <ul class="card-bullets">
            <li>Build governed metadata models using Cognos <strong>Framework Manager</strong> and Data Modules.</li>
            <li>Refactor complex SQL queries: optimize joins, create targeted indexes, and design views.</li>
            <li>Configure row-level security filters, user parameter prompts, and multi-tenant determinants.</li>
            <li>Conduct database query performance benchmarks demonstrating query speed improvements.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: Cognos Authoring & Java Integration</span>
            <span class="card-badge">Weeks 5–6</span>
          </div>
          <ul class="card-bullets">
            <li>Author modern interactive Cognos reports, KPI summaries, and drill-through dashboards.</li>
            <li>Collaborate with backend developers to integrate Cognos RESTful / Mashup APIs into Java Spring Boot.</li>
            <li>Implement secure report embedding with Spring Security, passing dynamic JWT user tokens.</li>
            <li>Enable automated report scheduling and export delivery pipelines (PDF, Excel, CSV).</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: UAT, Reconciliation & Handover</span>
            <span class="card-badge">Weeks 7–8</span>
          </div>
          <ul class="card-bullets">
            <li>Execute automated data reconciliation tests comparing Crystal historical output vs. Cognos output.</li>
            <li>Partner with business analysts and product managers to conduct User Acceptance Testing (UAT).</li>
            <li>Resolve remaining edge-case discrepancies, performance bottlenecks, and UI adjustments.</li>
            <li>Deliver comprehensive technical documentation, data dictionary, and developer runbooks.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Squad Member Profiles -->
    <div class="section">
      <div class="section-title">
        8. Meet The BI & Integration Engineering Squad
        <span class="tagline">Senior Systems & Data Engineering Specialists Dedicated to Your Success</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Enterprise Architect & Java Lead</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Enterprise Systems</div>
            <p class="card-p">
              Specializes in Java 21 / Spring Boot 3.x backend architecture, REST API design, OAuth2/JWT security, system integrations, and report embedding within enterprise portals.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Java Spring Boot</span>
            <span class="chip">REST APIs</span>
            <span class="chip">OAuth2 / JWT</span>
            <span class="chip">API Gateways</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Senior Database & SQL Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Enterprise Core Systems & Database Operations</div>
            <p class="card-p">
              Expert in relational database design, complex SQL tuning, query execution plan analysis, index optimization, data reconciliation, and high-volume reporting architecture.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Complex SQL Tuning</span>
            <span class="chip">RDBMS Design</span>
            <span class="chip">Execution Plans</span>
            <span class="chip">Data Modeling</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">BI Project Manager & Systems Analyst</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise SaaS & Analytics Delivery</div>
            <p class="card-p">
              Leads requirements gathering, sprint coordination, cross-team collaboration, and QA acceptance criteria validation across enterprise analytics and reporting platforms.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">BI Project Management</span>
            <span class="chip">Requirements Analysis</span>
            <span class="chip">QA Validation</span>
            <span class="chip">Sprint Delivery</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Call to action -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #0f62fe; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Next Steps & Technical Architecture Discussion</div>
      <div class="callout-text" style="color: #334155;">
        We welcome a technical discovery call with your engineering and reporting leadership to review sample Crystal Report definitions (`.rpt`), evaluate your database schema, and demonstrate our Java Spring Boot Cognos integration framework. We are ready to begin immediately upon engagement.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cognos BI Developer • Crystal Reports Migration & Java Integration</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\Cognos_Crystal_Reports_Migration"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "Cognos_Crystal_Reports_Migration_Proposal.pdf")
    
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

