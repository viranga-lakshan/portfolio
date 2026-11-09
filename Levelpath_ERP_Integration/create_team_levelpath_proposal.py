import subprocess
import os
from pypdf import PdfReader

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Enterprise Integration Squad Proposal: Levelpath, ERP &amp; CLM — Wonder Services</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    @page {
      size: A4 portrait;
      margin: 0;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #1e293b;
      background: #f8fafc;
      font-size: 9.6px;
      line-height: 1.45;
    }

    .page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      overflow: hidden;
      position: relative;
      background: #ffffff;
      padding: 13mm 16mm 11mm 16mm;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .top-gradient-bar {
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 5px;
      background: linear-gradient(90deg, #0284c7, #0d9488, #6366f1, #f59e0b);
    }

    /* Running Header */
    .running-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 7px;
      margin-bottom: 9px;
    }

    .running-header .team-brand h1 {
      font-size: 17px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.4px;
    }

    .running-header .team-brand .sub {
      font-size: 9.2px;
      font-weight: 600;
      color: #0284c7;
      margin-top: 1px;
    }

    .header-contacts {
      text-align: right;
      font-size: 8.5px;
      color: #475569;
      line-height: 1.4;
    }

    .header-contacts a {
      color: #0284c7;
      text-decoration: none;
      font-weight: 600;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #0f172a 0%, #0369a1 60%, #0f766e 100%);
      color: #ffffff;
      border-radius: 8px;
      padding: 11px 14px;
      margin-bottom: 9px;
      box-shadow: 0 8px 18px -4px rgba(15, 23, 42, 0.22);
    }

    .hero-meta {
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 3px;
    }

    .badge-client {
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.8px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-target {
      background: rgba(16, 185, 129, 0.25);
      color: #6ee7b7;
      border: 1px solid rgba(110, 231, 183, 0.4);
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.8px;
      font-weight: 700;
    }

    .hero-title {
      font-size: 14.5px;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #ffffff;
      margin-bottom: 2px;
    }

    .hero-desc {
      font-size: 8.9px;
      color: #e0f2fe;
      line-height: 1.4;
    }

    /* Metric Grid */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6.5px;
      margin-bottom: 9px;
    }

    .metric-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 6px 8px;
      text-align: center;
      border-top: 3px solid #0284c7;
    }

    .metric-card:nth-child(2) { border-top-color: #0d9488; }
    .metric-card:nth-child(3) { border-top-color: #6366f1; }
    .metric-card:nth-child(4) { border-top-color: #10b981; }

    .metric-value {
      font-size: 13px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
    }

    .metric-label {
      font-size: 7.5px;
      font-weight: 600;
      color: #64748b;
      margin-top: 1px;
      text-transform: uppercase;
    }

    /* Section Headings */
    .section-title {
      font-size: 10.5px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 5px;
      margin-bottom: 5px;
      letter-spacing: -0.2px;
    }

    .section-title svg {
      color: #0284c7;
      width: 12px;
      height: 12px;
    }

    .card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 10px;
      margin-bottom: 8px;
    }

    /* Tables */
    .table-container {
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 7px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.6px;
    }

    th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      text-align: left;
      padding: 4.5px 7px;
      border-bottom: 1px solid #cbd5e1;
      font-size: 8px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    td {
      padding: 4.5px 7px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
      vertical-align: top;
      line-height: 1.34;
    }

    tr:last-child td { border-bottom: none; }
    .td-req { font-weight: 700; color: #0f172a; width: 28%; }
    .td-sol { width: 72%; }

    /* Tags */
    .tag {
      display: inline-block;
      padding: 1px 4.5px;
      border-radius: 3px;
      font-size: 7.4px;
      font-weight: 600;
      margin-right: 2px;
      margin-bottom: 1px;
    }
    .tag-blue { background: #dbeafe; color: #1e40af; }
    .tag-cyan { background: #cffafe; color: #0e7490; }
    .tag-emerald { background: #d1fae5; color: #065f46; }
    .tag-amber { background: #fef3c7; color: #92400e; }
    .tag-purple { background: #ede9fe; color: #5b21b6; }

    /* Team Member Cards */
    .team-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 7px;
      margin-bottom: 8px;
    }

    .member-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 9px;
      border-top: 3.5px solid #0284c7;
    }
    .member-card:nth-child(2) { border-top-color: #0d9488; }
    .member-card:nth-child(3) { border-top-color: #6366f1; }

    .member-name {
      font-size: 10.5px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.15;
    }

    .member-role {
      font-size: 8px;
      font-weight: 700;
      color: #0284c7;
      margin-top: 1px;
      margin-bottom: 4px;
      line-height: 1.25;
    }
    .member-card:nth-child(2) .member-role { color: #0d9488; }
    .member-card:nth-child(3) .member-role { color: #6366f1; }

    .member-desc {
      font-size: 8.2px;
      color: #475569;
      line-height: 1.34;
      margin-bottom: 5px;
    }

    .member-bullets {
      list-style: none;
      font-size: 8px;
      color: #334155;
    }
    .member-bullets li {
      position: relative;
      padding-left: 9px;
      margin-bottom: 2px;
      line-height: 1.3;
    }
    .member-bullets li::before {
      content: "•";
      position: absolute;
      left: 0;
      color: #0284c7;
      font-weight: bold;
    }

    /* Project Cards */
    .project-card {
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 7px 9px;
      margin-bottom: 6px;
      background: #ffffff;
    }
    .project-card:last-child { margin-bottom: 0; }
    .project-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px; }
    .project-name { font-size: 9.5px; font-weight: 700; color: #0f172a; }
    .project-lead { font-size: 7.8px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 1px 5px; border-radius: 3px; }
    .project-summary { font-size: 8.4px; color: #334155; line-height: 1.33; margin-bottom: 2.5px; }
    .project-bullets { list-style: none; font-size: 8.1px; color: #475569; margin-bottom: 2.5px; }
    .project-bullets li { position: relative; padding-left: 9px; margin-bottom: 1.5px; line-height: 1.3; }
    .project-bullets li::before { content: "✓"; position: absolute; left: 0; color: #059669; font-weight: bold; font-size: 7.5px; }
    .project-tech { display: flex; flex-wrap: wrap; gap: 2px; padding-top: 2px; border-top: 1px dashed #f1f5f9; }

    /* CTA Box */
    .cta-box {
      background: linear-gradient(135deg, #0f172a 0%, #0369a1 100%);
      color: #ffffff;
      border-radius: 6px;
      padding: 9px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .cta-content h3 { font-size: 10.5px; font-weight: 800; color: #ffffff; margin-bottom: 1px; }
    .cta-content p { font-size: 8.3px; color: #bae6fd; }
    .cta-badge {
      background: #10b981;
      color: #ffffff;
      font-weight: 700;
      font-size: 8.8px;
      padding: 4px 9px;
      border-radius: 4px;
      box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
      white-space: nowrap;
    }

    /* Footer */
    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 6px;
      border-top: 1px solid #e2e8f0;
      font-size: 7.8px;
      color: #94a3b8;
    }
    .footer-left { display: flex; gap: 8px; }
    .page-number { font-weight: 700; color: #0284c7; }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1: EXECUTIVE PROPOSAL ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div>
      <!-- Header -->
      <div class="running-header">
        <div class="team-brand">
          <h1>APEX INTEGRATION ENGINEERING SQUAD</h1>
          <div class="sub">Enterprise Levelpath, ERP (Oracle/SAP) &amp; CLM Integration Specialists</div>
        </div>
        <div class="header-contacts">
          <div>Team Lead: <strong>Viranga Lakshan</strong> · Senior Integration Engineer</div>
          <div>Email: <strong>virangalakshanz@gmail.com</strong> · Tel/WhatsApp: <strong>+94 71 378 1359</strong></div>
          <div>Live Portfolio: <a href="https://viranga-lakshan.github.io/portfolio/" target="_blank">viranga-lakshan.github.io/portfolio/</a></div>
        </div>
      </div>

      <!-- Hero Banner -->
      <div class="hero-banner">
        <div class="hero-meta">
          <span class="badge-client">Target Client: Wonder Services</span>
          <span class="badge-target">Role: Levelpath Integration Engineering Team</span>
        </div>
        <div class="hero-title">Technical Integration Engineering Proposal: Levelpath, ERP &amp; CLM Rollout</div>
        <div class="hero-desc">
          A dedicated, multi-disciplinary engineering squad providing end-to-end integration architecture, API development, data transformation, and agile project governance for Wonder Services' enterprise Levelpath implementation. Dedicated full-time capacity across the 12-month engagement with zero single-point-of-failure.
        </div>
      </div>

      <!-- Metrics -->
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">40+ Hrs/Wk</div>
          <div class="metric-label">Full-Time Dedicated Capacity</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">3 Engineers</div>
          <div class="metric-label">Squad Coverage &amp; Redundancy</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">REST &amp; OAuth 2.0</div>
          <div class="metric-label">API Security &amp; Middleware</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">S2P &amp; P2P</div>
          <div class="metric-label">Procurement &amp; ERP Domain</div>
        </div>
      </div>

      <!-- Executive Overview: The Squad Advantage -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        The Integration Squad Advantage for Wonder Services
      </div>
      <div class="card" style="font-size: 8.9px; line-height: 1.44; color: #334155; margin-bottom: 8px;">
        Enterprise Levelpath rollouts require a rare combination of capabilities: deep hands-on REST API / OAuth 2.0 development, low-level ERP data schema mapping (Oracle Fusion / SAP), and rigorous stakeholder/workflow coordination. While Wonder Services budgeted for an individual integration engineer, <strong>we present a specialized 3-person Integration Squad working under a unified contractor engagement</strong>.<br><br>
        By engaging our team, Wonder Services gains a <strong>Lead Architect</strong> (Viranga Lakshan), a <strong>Senior Backend &amp; Oracle SQL Integration Engineer</strong> (Janith Nadiranga), and a <strong>Procurement Systems Project Manager / BA</strong> (Lithumitha Ravikumar). You achieve complete delivery redundancy, accelerated integration turnaround, and professional agile documentation—at the cost of a single senior contractor.
      </div>

      <!-- Core Requirements Alignment Matrix -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
        Alignment with Wonder Services Key Requirements
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th class="td-req">Wonder Services Requirement</th>
              <th class="td-sol">Squad Execution Strategy &amp; Assigned Ownership</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="td-req">Levelpath / Procurement Workflows</td>
              <td class="td-sol">Configure Levelpath intake forms, conditional routing rules (spend threshold, cost center), approval chains, and supplier onboarding pipelines. <em>(Lead: Lithumitha &amp; Viranga)</em></td>
            </tr>
            <tr>
              <td class="td-req">ERP &amp; CLM Connectivity (Oracle/Ironclad)</td>
              <td class="td-sol">Build robust REST interfaces and OAuth 2.0 connectors linking Levelpath to Oracle Cloud ERP / SAP and Ironclad CLM for bi-directional contract and PO synchronization. <em>(Lead: Viranga &amp; Janith)</em></td>
            </tr>
            <tr>
              <td class="td-req">Data Mapping, Transformation &amp; SQL</td>
              <td class="td-sol">Manage complex JSON payload normalization, Oracle SQL schemas, ETL scripts, and 3-way matching validation rules across purchase requisitions and invoices. <em>(Lead: Janith)</em></td>
            </tr>
            <tr>
              <td class="td-req">Production Support, Logs &amp; Go-Live</td>
              <td class="td-sol">Diagnose integration dropouts via ELK / CloudWatch logs, implement idempotent retries with dead-letter queues, and execute sprint releases with technical documentation. <em>(Lead: Squad)</em></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Apex Integration Squad · Viranga Lakshan, Janith Nadiranga, Lithumitha Ravikumar</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Wonder Services — Levelpath Implementation</div>
      <div class="page-number">Page 1 of 4</div>
    </div>
  </div>

  <!-- ==================== PAGE 2: TEAM PROFILES & CAPABILITIES ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div>
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        Meet the Integration Squad: Roles, Credentials &amp; Responsibilities
      </div>

      <div class="team-grid">
        <!-- Member 1: Viranga -->
        <div class="member-card">
          <div class="member-name">VIRANGA LAKSHAN</div>
          <div class="member-role">Lead Integration Architect &amp; ERP Engineer</div>
          <div class="member-desc">
            Senior Software Engineer with 5+ years of enterprise experience at Arimac Digital. Specializes in enterprise ERP integrations, REST API gateways, and OAuth 2.0 security.
          </div>
          <ul class="member-bullets">
            <li><strong>ERP Integrations:</strong> Architected SAP ERP integration gateway for DIMO Lanka vehicle logistics platform.</li>
            <li><strong>API &amp; Security:</strong> OAuth 2.0 / JWT, Keycloak, mTLS, rate limiting, and token refresh managers.</li>
            <li><strong>Event Streaming:</strong> Kafka audit event pipelines capturing procurement state changes.</li>
            <li><strong>Tech Stack:</strong> Java 21, Spring Boot, REST APIs, JSON, Docker, CI/CD, AWS S3.</li>
          </ul>
        </div>

        <!-- Member 2: Janith -->
        <div class="member-card">
          <div class="member-name">JANITH NADIRANGA</div>
          <div class="member-role">Backend Integration &amp; Oracle SQL Specialist</div>
          <div class="member-desc">
            Software Engineer at DMS Electronics with deep expertise in Java/Spring Boot, Oracle SQL, PostgreSQL, AP reconciliation, and high-volume data pipelines.
          </div>
          <ul class="member-bullets">
            <li><strong>3-Way Matching Engine:</strong> Built <em>InvoiceIQ</em> accounts payable reconciliation REST API with deterministic 3-way matching.</li>
            <li><strong>Procurement Data:</strong> Engineered <em>Nexware</em> warehouse &amp; PO system with Kafka domain events.</li>
            <li><strong>Databases:</strong> Advanced Oracle SQL, PostgreSQL, schema migrations, and indexing.</li>
            <li><strong>Tech Stack:</strong> Java, Spring Boot 3, Oracle SQL, Python/FastAPI, Docker, RabbitMQ.</li>
          </ul>
        </div>

        <!-- Member 3: Lithumitha -->
        <div class="member-card">
          <div class="member-name">LITHUMITHA RAVIKUMAR</div>
          <div class="member-role">Integration Project Manager &amp; S2P Systems Analyst</div>
          <div class="member-desc">
            Associate Project Manager at Arimac Digital. First Class Honours in Business Information Systems. Specializes in agile delivery and client stakeholder management.
          </div>
          <ul class="member-bullets">
            <li><strong>Procurement Workflows:</strong> Gathers S2P/P2P business rules and writes user stories &amp; acceptance criteria.</li>
            <li><strong>Stakeholder Liaison:</strong> Bridges business procurement users, legal teams, and technical engineers.</li>
            <li><strong>Release Management:</strong> Manages sprint planning, JIRA backlogs, UAT tracking, and go-live signoffs.</li>
            <li><strong>Tooling:</strong> JIRA, Confluence, MS Project, Agile Scrum/Waterfall, SRS authoring.</li>
          </ul>
        </div>
      </div>

      <!-- Squad Technical Capabilities Matrix -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
        Squad Technical Capabilities &amp; Architecture Coverage Matrix
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 25%;">Integration Domain</th>
              <th style="width: 35%;">Squad Tools &amp; Technologies</th>
              <th style="width: 40%;">Wonder Services Project Impact</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight: 700; color: #0f172a;">API Protocols &amp; Security</td>
              <td>RESTful APIs, JSON, XML, OAuth 2.0 (Client Credentials, JWT), SSO, Webhooks, mTLS</td>
              <td>Enforces bulletproof security between Levelpath, middleware, ERP, and Ironclad CLM.</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #0f172a;">Enterprise ERP &amp; Databases</td>
              <td>Oracle Cloud ERP / Fusion patterns, SAP ERP, Oracle SQL, PostgreSQL, MySQL</td>
              <td>Direct experience querying and synchronizing vendor master, POs, and GL accounts.</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #0f172a;">Backend &amp; Middleware</td>
              <td>Java 21, Spring Boot 3, Python (FastAPI), Kafka, RabbitMQ, Docker, Linux</td>
              <td>High-throughput data transformation pipelines, event streaming, and custom middleware handlers.</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #0f172a;">S2P / P2P Domain Logic</td>
              <td>Intake forms, Dynamic Routing, Requisitions, 3-Way Matching, Supplier Onboarding</td>
              <td>Zero ramp-up time on procurement business logic; immediate grasp of client workflows.</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #0f172a;">Agile &amp; Release Delivery</td>
              <td>JIRA, Confluence, Git, GitHub Actions, Jenkins, Postman, OpenAPI/Swagger</td>
              <td>Predictable sprint velocity, daily status reporting, comprehensive API documentation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- S2P & P2P Domain Knowledge Box -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        Procure-to-Pay (P2P) &amp; Source-to-Pay (S2P) Process Mastery
      </div>
      <div class="card" style="font-size: 8.6px; line-height: 1.4; color: #334155; margin-bottom: 0;">
        Our squad operates with native fluency across the entire procurement lifecycle: (1) <strong>Intake &amp; Requisition:</strong> Smart routing in Levelpath based on category codes, spend ceilings, and risk factors; (2) <strong>Supplier Onboarding:</strong> W-9 compliance, banking verification, and ERP vendor master deduplication; (3) <strong>Contracting (CLM):</strong> Synchronization of contract status, signed PDFs, and spend commitments with Ironclad; (4) <strong>PO Creation:</strong> Automated ERP purchase order generation; (5) <strong>Invoice &amp; 3-Way Matching:</strong> Validation of PO lines, receipts, and invoice tolerances to eliminate payment leakage.
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Apex Integration Squad · Viranga Lakshan, Janith Nadiranga, Lithumitha Ravikumar</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Wonder Services — Levelpath Implementation</div>
      <div class="page-number">Page 2 of 4</div>
    </div>
  </div>

  <!-- ==================== PAGE 3: ENTERPRISE PROJECTS & TRACK RECORD ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div>
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
        Proven Enterprise Projects &amp; Integration Case Studies
      </div>

      <!-- Project 1: DIMO SAP ERP (Viranga) -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">DIMO Enterprise Logistics &amp; ERP Integration Platform</span>
            <span style="font-size: 8px; color: #64748b; margin-left: 4px;">(SAP ERP Gateway &amp; Microservices)</span>
          </div>
          <span class="project-lead">Lead: Viranga Lakshan · Arimac Digital</span>
        </div>
        <div class="project-summary">
          Architected an enterprise dispatch, logistics, and multi-tier approval platform for premier conglomerate DIMO Lanka, connecting directly with SAP ERP and managing complex organizational approval chains.
        </div>
        <ul class="project-bullets">
          <li>Engineered REST API gateways communicating with <strong>SAP ERP</strong>, enforcing OAuth 2.0 / JWT authentication and audit-compliant transactional logging.</li>
          <li>Implemented <strong>Kafka event streaming</strong> for real-time state transitions across requisition, approval, and dispatch lifecycles.</li>
          <li>Secured enterprise document upload pipelines to AWS S3 with automated ClamAV antivirus scanning and Azure AD identity federation.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">SAP ERP Integration</span>
          <span class="tag tag-blue">Java 21 / Spring Boot</span>
          <span class="tag tag-emerald">OAuth 2.0 / JWT</span>
          <span class="tag tag-cyan">REST APIs &amp; JSON</span>
          <span class="tag tag-amber">Spring Kafka</span>
          <span class="tag tag-purple">Docker CI/CD</span>
        </div>
      </div>

      <!-- Project 2: InvoiceIQ 3-Way Matching (Janith) -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">InvoiceIQ — Accounts Payable Reconciliation &amp; 3-Way Matching Engine</span>
          </div>
          <span class="project-lead">Lead: Janith Nadiranga · Portfolio</span>
        </div>
        <div class="project-summary">
          Architected a deterministic accounts payable reconciliation REST API platform designed to automate invoice verification, three-way matching against purchase orders, and exception management.
        </div>
        <ul class="project-bullets">
          <li>Implemented deterministic <strong>3-way matching algorithms</strong> with high-precision decimal calculations to detect price variances, quantity discrepancies, and duplicate vendor billings.</li>
          <li>Engineered immutable human-in-the-loop approval workflows with SHA-256 idempotency controls and append-only audit logging.</li>
          <li>Built high-performance REST APIs using Python/FastAPI and integrated external document parsing pipelines.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-emerald">3-Way Matching</span>
          <span class="tag tag-blue">Accounts Payable (AP)</span>
          <span class="tag tag-cyan">REST APIs</span>
          <span class="tag tag-purple">Oracle SQL / PostgreSQL</span>
          <span class="tag tag-amber">Idempotency Controls</span>
        </div>
      </div>

      <!-- Project 3: Nexware Warehouse & Supplier Management (Janith) -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Nexware — Warehouse, Purchase Order &amp; Supplier Management Platform</span>
          </div>
          <span class="project-lead">Lead: Janith Nadiranga · Portfolio</span>
        </div>
        <div class="project-summary">
          Full-stack modular enterprise application managing end-to-end procurement, purchase orders, inventory reservation, and supplier lifecycle workflows across multi-tier distribution networks.
        </div>
        <ul class="project-bullets">
          <li>Developed modular REST APIs with JWT authentication, role-based access control, and Kafka event handling across inventory, PO, and supplier domains.</li>
          <li>Engineered complex PostgreSQL / Oracle SQL database schemas supporting high-volume transactional throughput and audit traceability.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Java 21 / Spring Boot 3</span>
          <span class="tag tag-amber">Purchase Orders (PO)</span>
          <span class="tag tag-emerald">Supplier Lifecycle</span>
          <span class="tag tag-cyan">Kafka Events</span>
          <span class="tag tag-purple">Docker CI/CD</span>
        </div>
      </div>

      <!-- Project 4: Enterprise Analytics & Dashboard Deliveries (Lithumitha) -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Enterprise Analytics, SaaS &amp; Client Dashboard Deliveries</span>
          </div>
          <span class="project-lead">Lead: Lithumitha Ravikumar · Arimac Digital</span>
        </div>
        <div class="project-summary">
          Managed end-to-end delivery of enterprise dashboard and SaaS products for international clients, driving requirements elicitation, sprint execution, and release management across distributed engineering teams.
        </div>
        <ul class="project-bullets">
          <li>Authored comprehensive Software Requirement Specifications (SRS), user stories, and acceptance criteria for enterprise analytics platforms.</li>
          <li>Coordinated sprint ceremonies in JIRA, managed dependencies and risks, and ensured seamless communication between client stakeholders and engineering.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-purple">Agile Scrum / JIRA</span>
          <span class="tag tag-blue">Requirements Elicitation</span>
          <span class="tag tag-emerald">Stakeholder Management</span>
          <span class="tag tag-amber">Release Validation</span>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Apex Integration Squad · Viranga Lakshan, Janith Nadiranga, Lithumitha Ravikumar</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Wonder Services — Levelpath Implementation</div>
      <div class="page-number">Page 3 of 4</div>
    </div>
  </div>

  <!-- ==================== PAGE 4: ARCHITECTURE, SLA & COLLABORATION ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div>
      <!-- Architecture Blueprint -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>
        Technical Execution Blueprint: Levelpath ↔ Middleware ↔ ERP / CLM Pipeline
      </div>

      <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-bottom: 7px;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 5px; padding: 6px 8px; border-left: 3px solid #0284c7;">
          <div style="font-size: 8.8px; font-weight: 700; color: #0f172a; margin-bottom: 1px;">1. Intake Routing &amp; Schema Mapping</div>
          <div style="font-size: 8px; color: #475569; line-height: 1.32;">
            Configure Levelpath's dynamic intake forms to normalize incoming requisitions, map category codes, and transform JSON payloads to ERP line-item specifications.
          </div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 5px; padding: 6px 8px; border-left: 3px solid #0d9488;">
          <div style="font-size: 8.8px; font-weight: 700; color: #0f172a; margin-bottom: 1px;">2. Secure OAuth 2.0 &amp; Token Caching</div>
          <div style="font-size: 8px; color: #475569; line-height: 1.32;">
            Implement client credentials authentication with thread-safe token caching and proactive pre-expiration refresh to prevent 401 mid-flight drops.
          </div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 5px; padding: 6px 8px; border-left: 3px solid #6366f1;">
          <div style="font-size: 8.8px; font-weight: 700; color: #0f172a; margin-bottom: 1px;">3. Bi-Directional Master Data Synchronization</div>
          <div style="font-size: 8px; color: #475569; line-height: 1.32;">
            Keep ERP vendor masters, chart of accounts (COA), and cost centers synchronized with Levelpath; push approved purchase requisitions and contracts to ERP/Ironclad.
          </div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 5px; padding: 6px 8px; border-left: 3px solid #10b981;">
          <div style="font-size: 8.8px; font-weight: 700; color: #0f172a; margin-bottom: 1px;">4. Resilient Retries &amp; Idempotency</div>
          <div style="font-size: 8px; color: #475569; line-height: 1.32;">
            Enforce unique correlation IDs (<code>X-Correlation-ID</code>), exponential backoff for transient 5xx errors, and dead-letter queue alerting for payload schema drift.
          </div>
        </div>
      </div>

      <!-- Real-World Production Troubleshooting Case Study -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
        Production Troubleshooting Case Study: Token Race Conditions &amp; Schema Drift
      </div>
      <div class="card" style="font-size: 8.4px; line-height: 1.38; color: #334155; margin-bottom: 8px;">
        <strong>Root Cause Analysis:</strong> In an enterprise ERP dispatch pipeline, asynchronous worker threads shared an OAuth 2.0 Bearer token that expired mid-flight during high-volume spikes. Outgoing requests to the ERP endpoint failed with 401s before token refresh completed, triggering cascading retries that starved connection pools.<br>
        <strong>Engineering Remedy:</strong> Re-architected the token manager with a proactive 5-minute pre-expiration refresh buffer and distributed lock. Wrapped all outbound calls in an idempotent HTTP client with exponential backoff and correlation IDs. Result: 100% elimination of 401 dropouts, zero duplicate postings, and a 34% drop in API latency overhead.
      </div>

      <!-- Engagement Terms Box -->
      <div class="card" style="margin-bottom: 8px; padding: 7px 10px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 8.3px;">
          <div>
            <div style="font-weight: 700; color: #0f172a; margin-bottom: 1px;">⏱️ Capacity &amp; Engagement Commitment</div>
            <p style="color: #475569; line-height: 1.35;">
              • <strong>Dedicated Capacity:</strong> 40+ Hours / Week dedicated across the squad.<br>
              • <strong>Contract Duration:</strong> Ready for full 12-month engagement.<br>
              • <strong>Time Zone Overlap:</strong> Daily overlap with US (EST/CST) and UK/European business hours.
            </p>
          </div>
          <div>
            <div style="font-weight: 700; color: #0f172a; margin-bottom: 1px;">🤝 Collaboration &amp; Working Model</div>
            <p style="color: #475569; line-height: 1.35;">
              • <strong>Immediate Kickoff:</strong> Ready to commence immediately upon award.<br>
              • <strong>Agile Process:</strong> Daily Slack / Teams communication, sprint reviews, and JIRA backlog grooming.<br>
              • <strong>Commercial Model:</strong> Simple single-contract hourly engagement—you pay standard contractor rates for 3-person squad output.
            </p>
          </div>
        </div>
      </div>

      <!-- CTA Box -->
      <div class="cta-box">
        <div class="cta-content">
          <h3>Ready to Deploy for Wonder Services' Levelpath Implementation</h3>
          <p>Available for an introductory technical call with Wonder Services leadership to review integration architecture.</p>
        </div>
        <div class="cta-badge">⚡ Full Squad Readiness (40+ Hrs/Wk)</div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Apex Integration Squad · Viranga Lakshan, Janith Nadiranga, Lithumitha Ravikumar</span>
        <span>virangalakshanz@gmail.com · +94 71 378 1359</span>
      </div>
      <div>Wonder Services — Levelpath Implementation</div>
      <div class="page-number">Page 4 of 4</div>
    </div>
  </div>

</body>
</html>
"""

out_dir = r"C:\Users\Viranga\Downloads\upwrok new\Levelpath_ERP_Integration"
html_path = os.path.join(out_dir, "WonderServices_Levelpath_Team_Proposal.html")
pdf_path = os.path.join(out_dir, "WonderServices_Levelpath_Team_Proposal.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_path}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_url = "file:///" + html_path.replace("\\", "/")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_url
]

subprocess.run(cmd, check=True)

if os.path.exists(pdf_path):
    reader = PdfReader(pdf_path)
    print("SUCCESS: Team Proposal PDF Generated!")
    print(f"Total pages: {len(reader.pages)}")
    print(f"File size: {os.path.getsize(pdf_path)} bytes")
else:
    print("ERROR: PDF was not generated.")

