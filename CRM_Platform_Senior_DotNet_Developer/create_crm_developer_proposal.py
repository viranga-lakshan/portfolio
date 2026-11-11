import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Senior Software Developer, CRM Platform (C# and ASP.NET) - Viranga Lakshan</title>
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
    font-size: 8pt;
    line-height: 1.34;
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
    background: #2563eb;
    border-radius: 2px;
    margin-bottom: 7px;
  }

  /* Header Top */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1.5px solid #2563eb;
    padding-bottom: 6px;
    margin-bottom: 9px;
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
    background: #2563eb;
    color: #ffffff;
    font-size: 6.8pt;
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
    font-size: 7.4pt;
    color: #64748b;
    line-height: 1.3;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Executive Banner */
  .quote-banner {
    background: #eff6ff;
    border: 1px solid #dbeafe;
    border-left: 3.5px solid #2563eb;
    border-radius: 4px;
    padding: 7px 11px;
    margin-bottom: 8.5px;
  }
  .quote-banner-title {
    font-size: 9.2pt;
    font-weight: 800;
    color: #1e40af;
    margin-bottom: 2px;
  }
  .quote-banner-desc {
    font-size: 7.6pt;
    color: #1e3a8a;
    line-height: 1.32;
    margin: 0;
  }

  /* Section Styling */
  .section {
    margin-bottom: 8px;
  }
  .section-title {
    font-size: 9pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3px solid #2563eb;
    padding-left: 6.5px;
    margin-bottom: 4.5px;
    text-transform: uppercase;
    letter-spacing: 0.25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 7pt;
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
    padding: 6.5px 8.5px;
  }
  .card.tint {
    background: #f0f7ff;
    border-color: #dbeafe;
  }
  .card.slate {
    background: #f8fafc;
    border-color: #e2e8f0;
  }
  .card.accent {
    border-top: 2.5px solid #2563eb;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
  }
  .card.tint .card-header {
    border-color: #bfdbfe;
  }
  .card-title {
    font-size: 8pt;
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
    background: #dbeafe;
    color: #1d4ed8;
  }
  .card-p {
    font-size: 7.4pt;
    color: #334155;
    margin: 0 0 3px 0;
    line-height: 1.28;
  }
  .card-bullets {
    margin: 0;
    padding-left: 11px;
    font-size: 7.2pt;
    color: #475569;
    line-height: 1.26;
  }
  .card-bullets li {
    margin-bottom: 1.5px;
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
    color: #2563eb;
  }

  /* Tables */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.3pt;
    margin-top: 1.5px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 3.5px 6px;
    font-weight: 700;
    font-size: 6.9pt;
    text-transform: uppercase;
    letter-spacing: 0.25px;
  }
  table.matrix-table td {
    padding: 3.5px 6px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.24;
  }
  table.matrix-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  table.matrix-table td strong {
    color: #0f172a;
  }

  /* Callout */
  .callout-box {
    background: #eff6ff;
    border-left: 3.5px solid #2563eb;
    border-radius: 4px;
    padding: 5px 8px;
    margin-top: 4px;
  }
  .callout-title {
    font-size: 7.8pt;
    font-weight: 700;
    color: #1e40af;
    margin-bottom: 1px;
  }
  .callout-text {
    font-size: 7.2pt;
    color: #1e3a8a;
    line-height: 1.25;
  }

  /* Metric Stat Box */
  .stat-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 7px;
    text-align: center;
  }
  .stat-val {
    font-size: 11pt;
    font-weight: 800;
    color: #2563eb;
    line-height: 1.1;
  }
  .stat-lbl {
    font-size: 6.6pt;
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
    font-size: 7pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #2563eb;
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
        <div class="brand-title">VIRANGA <span style="color:#2563eb;">LAKSHAN</span> <span class="brand-badge">Senior Software Engineer</span></div>
        <div class="brand-sub">Senior Software Developer, CRM Platform • C#, ASP.NET MVC & AWS Cloud Architecture</div>
      </div>
      <div class="meta-block">
        <strong>Engagement:</strong> Full-Time (>30–40 hrs/wk) • Hourly<br>
        <strong>Working Hours:</strong> 100% Pacific Time (PT) Business Hours<br>
        <strong>Proposed Rate:</strong> $18.00 – $20.00 / hr (Contract-to-Hire)<br>
        <strong>Availability:</strong> Immediate Start (Within 24–48 Hours)
      </div>
    </div>

    <!-- Executive Brief Banner -->
    <div class="quote-banner">
      <div class="quote-banner-title">Executive Profile & Technical Value Proposition</div>
      <p class="quote-banner-desc">
        Senior Full-Stack & .NET Software Engineer with <strong>5+ years of hands-on production engineering experience</strong> specializing in high-scale C#, ASP.NET MVC, .NET Framework 4.8, and modern .NET. Veteran of mature, large-scale codebases written by others, 24/7 on-call incident response, and AWS cloud integrations. Fully committed to working full Pacific Time business hours on an immediate contract-to-hire basis.
      </p>
    </div>

    <!-- Highlight Stats -->
    <div class="grid-4" style="margin-bottom: 7.5px;">
      <div class="stat-box">
        <div class="stat-val">5+ Years</div>
        <div class="stat-lbl">Production C# / .NET</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">100% PT</div>
        <div class="stat-lbl">Pacific Time Overlap</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">AWS Certified</div>
        <div class="stat-lbl">Lambda, S3, EC2, Dynamo</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">24/7 On-Call</div>
        <div class="stat-lbl">PagerDuty & Datadog Tier-3</div>
      </div>
    </div>

    <!-- Section 1: Direct Requirement Alignment Matrix -->
    <div class="section">
      <div class="section-title">
        1. Direct Technical Requirements Alignment Matrix
        <span class="tagline">100% Compliance with Posted Engagement Criteria</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 28%;">Client Job Requirement</th>
            <th style="width: 52%;">Viranga's Production Experience & Demonstrated Track Record</th>
            <th style="width: 20%; text-align: right;">Status & Match</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>4+ Years C# & ASP.NET MVC</strong></td>
            <td>5+ years developing, maintaining, and scaling enterprise C# web applications, ASP.NET MVC custom filters, model binders, and Razor views.</td>
            <td style="text-align: right; color: #16a34a;"><strong>Exceeds (5+ Yrs)</strong></td>
          </tr>
          <tr>
            <td><strong>.NET Framework 4.8 Knowledge</strong></td>
            <td>Deep expertise in .NET Framework 4.8 runtime, IIS application pools, `System.Web` pipeline, Autofac/Unity DI, and legacy assembly binding.</td>
            <td style="text-align: right; color: #2563eb;"><strong>100% Expert</strong></td>
          </tr>
          <tr>
            <td><strong>Large Existing Codebases</strong></td>
            <td>Inherited, refactored, and stabilized multi-year enterprise codebases (Singer PLC, SomBank TP V5 core) without introducing functional regressions.</td>
            <td style="text-align: right; color: #2563eb;"><strong>Proven Track Record</strong></td>
          </tr>
          <tr>
            <td><strong>Hands-on AWS Experience</strong></td>
            <td>Production delivery across <strong>EC2</strong> (ALB auto-scaling), <strong>S3</strong> (pre-signed document URLs), <strong>Lambda</strong> (C# serverless workers), and <strong>DynamoDB</strong> (audit logs).</td>
            <td style="text-align: right; color: #2563eb;"><strong>All 4 Services</strong></td>
          </tr>
          <tr>
            <td><strong>JavaScript UI Frameworks</strong></td>
            <td>Building dynamic frontend modules, responsive data tables, client-side validation, and real-time CRM updates using modern JS, TypeScript, React, and Vue.</td>
            <td style="text-align: right; color: #2563eb;"><strong>Full-Stack Fluidity</strong></td>
          </tr>
          <tr>
            <td><strong>CI/CD & DevOps Practices</strong></td>
            <td>Continuous integration with <strong>TeamCity</strong>, automated blue/green multi-tenant releases in <strong>Octopus Deploy</strong>, and infrastructure monitoring.</td>
            <td style="text-align: right; color: #2563eb;"><strong>TeamCity & Octopus</strong></td>
          </tr>
          <tr>
            <td><strong>24/7 Production On-Call</strong></td>
            <td>Veteran of Tier-3 24/7 production on-call rotations using <strong>PagerDuty</strong> and <strong>Datadog APM</strong>; strict 5-min response SLA and blameless post-mortems.</td>
            <td style="text-align: right; color: #2563eb;"><strong>Production Tested</strong></td>
          </tr>
          <tr>
            <td><strong>Mentorship & Code Reviews</strong></td>
            <td>Conducted hundreds of structured code reviews; led engineering design sessions, standardized SOLID principles, and mentored junior developers.</td>
            <td style="text-align: right; color: #2563eb;"><strong>Active Mentor</strong></td>
          </tr>
          <tr>
            <td><strong>Pacific Time Business Hours</strong></td>
            <td>Fully dedicated to working 8:00 AM – 5:00 PM Pacific Time (PT), enabling real-time collaboration on Slack, Zoom, and standups.</td>
            <td style="text-align: right; color: #16a34a;"><strong>Full PT Overlap</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 2: Engagement Terms Summary -->
    <div class="section">
      <div class="section-title">
        2. Commercial Proposal & Commitment Terms
        <span class="tagline">Aligned Directly with Client Budget and Contract-to-Hire Model</span>
      </div>
      <div class="grid-3">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Hourly Rate & Budget</span>
            <span class="card-badge">Target Rate</span>
          </div>
          <p class="card-p">
            <strong>Proposed Rate:</strong> <strong>$18.00 – $20.00 / hr</strong><br>
            Comfortably aligned with client's $15.00 – $20.00 posted range. Delivers senior-level architecture and execution at exceptional value.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Duration & Capacity</span>
            <span class="card-badge">Full-Time</span>
          </div>
          <p class="card-p">
            <strong>Allocation:</strong> 40 Hours / Week (>30 hrs/wk mandate).<br>
            <strong>Duration:</strong> 6-Month contract with immediate readiness and long-term intent for <strong>contract-to-hire</strong> conversion.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Time Zone & Start Date</span>
            <span class="card-badge">Immediate</span>
          </div>
          <p class="card-p">
            <strong>Time Zone:</strong> 100% Pacific Time (PT) overlap.<br>
            <strong>Start Date:</strong> Immediate kickoff within 24–48 hours of offer acceptance and repository provisioning.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Senior Software Developer Proposal • CRM Platform</span>
    <span>Page 1 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 2: TECHNICAL ARCHITECTURE & AWS ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">TECHNICAL <span style="color:#2563eb;">COMPETENCIES</span> <span class="brand-badge">.NET & AWS</span></div>
        <div class="brand-sub">ASP.NET MVC 4.8, C# Clean Architecture, AWS Cloud Stack & Code Modernization</div>
      </div>
      <div class="meta-block">
        <strong>Runtime:</strong> .NET Framework 4.8 ➔ Modern .NET 8<br>
        <strong>AWS Stack:</strong> Lambda • S3 • EC2 • DynamoDB<br>
        <strong>Frontend:</strong> React • Vue • TypeScript • ASP.NET Razor
      </div>
    </div>

    <!-- Section 3: C# and ASP.NET MVC Deep Dive -->
    <div class="section">
      <div class="section-title">
        3. C# & ASP.NET MVC Mastery (.NET Framework 4.8 Core)
        <span class="tagline">Enterprise Patterns, Legacy Stabilization, and Clean Architecture</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">ASP.NET MVC Pipeline & .NET 4.8 Architecture</span>
            <span class="card-badge">Core Engine</span>
          </div>
          <p class="card-p">
            Deep experience engineering within the ASP.NET MVC 5 / .NET 4.8 pipeline:
          </p>
          <ul class="card-bullets">
            <li><strong>Custom Action Filters & Attributes:</strong> Building centralized authorization filters, audit logging interceptors, and exception handling pipelines.</li>
            <li><strong>Dependency Injection & Inversion of Control:</strong> Standardizing constructor injection via Autofac, Unity, and SimpleInjector across legacy WebForms and MVC controllers.</li>
            <li><strong>High-Throughput Data Access:</strong> Profiling and optimizing Entity Framework 6 (EF6) and Dapper queries; eliminating N+1 lazy-loading cascades and tuning SQL transactions.</li>
            <li><strong>Memory & LOH Optimization:</strong> Preventing Large Object Heap fragmentation through stream-based JSON parsing and memory buffer reuse.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Mastering Large Existing Codebases Written by Others</span>
            <span class="card-badge">Zero Regressions</span>
          </div>
          <p class="card-p">
            Specialized methodology for diving into undocumented, multi-year legacy code:
          </p>
          <ul class="card-bullets">
            <li><strong>Characterization & Golden Master Testing:</strong> Writing automated integration tests to lock down current input/output behavior before touching legacy code.</li>
            <li><strong>Dependency Decoupling (Seam Identification):</strong> Abstracting monolithic God classes behind clean domain interfaces using Michael Feathers' refactoring techniques.</li>
            <li><strong>Zero-Regression Discipline:</strong> Deploying changes in small, self-contained PRs with verified automated unit tests and smoke tests.</li>
            <li><strong>Fast Ramp-up:</strong> Quickly deciphering database schemas, stored procedures, and implicit business rules without slowing down sprint cadence.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 4: Modernization Roadmap -->
    <div class="section">
      <div class="section-title">
        4. .NET Framework 4.8 to Modern .NET (.NET 8) Migration Strategy
        <span class="tagline">Pragmatic, Zero-Downtime Strangler-Fig Modernization Pattern</span>
      </div>
      <div class="grid-3">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Step 1: Domain Decoupling</span>
            <span class="card-badge">Step 01</span>
          </div>
          <p class="card-p">
            Extracting business logic, entity models, and calculation engines from <code>System.Web</code> into <strong>.NET Standard 2.0</strong> class libraries compatible with both .NET 4.8 and .NET 8.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Step 2: YARP Reverse Proxy</span>
            <span class="card-badge">Step 02</span>
          </div>
          <p class="card-p">
            Deploying Microsoft YARP (Yet Another Reverse Proxy) in front of IIS. High-value API endpoints are re-architected in .NET 8 while legacy views route seamlessly to .NET 4.8.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Step 3: EF Core Transition</span>
            <span class="card-badge">Step 03</span>
          </div>
          <p class="card-p">
            Transitioning legacy EF6 EDMX models to Code-First mappings, adopting EF Core batching, compiled queries, and connection resilience with zero database schema disruption.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 5: Hands-on AWS Cloud Architecture -->
    <div class="section">
      <div class="section-title">
        5. Hands-on AWS Cloud Architecture (Lambda, S3, EC2, DynamoDB)
        <span class="tagline">Production Integration with AWS SDK for .NET</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">AWS EC2 & S3 Document Storage</span>
            <span class="card-badge">Compute & Assets</span>
          </div>
          <ul class="card-bullets">
            <li><strong>EC2 Workload Hosting:</strong> Provisioning Windows Server IIS instances behind Application Load Balancers (ALB) with auto-scaling groups and SSL offloading.</li>
            <li><strong>S3 Pre-Signed URL Architecture:</strong> Offloading file uploads/downloads (CRM contracts, customer attachments, email exports) directly to Amazon S3 using pre-signed URLs, reducing EC2 memory load by 70%.</li>
            <li><strong>Lifecycle Policies:</strong> Implementing S3 Intelligent-Tiering and Glacier archiving for historical customer audit records to slash storage overhead.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">AWS Lambda & DynamoDB Services</span>
            <span class="card-badge">Serverless & NoSQL</span>
          </div>
          <ul class="card-bullets">
            <li><strong>C# Serverless Lambda Functions:</strong> Building asynchronous microservices for background CRM tasks: webhook payload ingestion, daily sales summaries, and batch CSV imports.</li>
            <li><strong>Amazon DynamoDB Single-Table Design:</strong> Designing high-velocity audit logging and customer activity streams using composite partition keys (<code>TenantId#EntityId</code>) and sort keys.</li>
            <li><strong>Event-Driven Pipelines:</strong> Connecting Amazon S3 bucket events and SQS queues to C# Lambda consumers for resilient, self-healing background processing.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 6: Frontend JavaScript Fluidity -->
    <div class="callout-box">
      <div class="callout-title">Frontend JavaScript & UI Framework Fluidity</div>
      <div class="callout-text">
        Experienced in bridging ASP.NET MVC server-rendered views with modern client-side JavaScript frameworks (React, Vue, TypeScript). Skilled in building rich CRM pipeline Kanban boards, real-time client activity timelines, asynchronous form submission with optimistic UI updates, and responsive multi-column data grids.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Senior Software Developer Proposal • CRM Platform</span>
    <span>Page 2 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 3: DEVOPS, ON-CALL & LEADERSHIP ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">DEVOPS & <span style="color:#2563eb;">RELIABILITY</span> <span class="brand-badge">24/7 Production</span></div>
        <div class="brand-sub">TeamCity, Octopus Deploy, Datadog APM, PagerDuty On-Call & Team Mentorship</div>
      </div>
      <div class="meta-block">
        <strong>CI/CD Tooling:</strong> TeamCity • Octopus Deploy<br>
        <strong>Observability:</strong> Datadog APM • CloudWatch • SQL Profiler<br>
        <strong>On-Call Discipline:</strong> 24/7 Tier-3 Rotation • PagerDuty Sev-1/Sev-2
      </div>
    </div>

    <!-- Section 7: CI/CD Pipelines -->
    <div class="section">
      <div class="section-title">
        6. Automated CI/CD Pipelines (TeamCity & Octopus Deploy)
        <span class="tagline">Repeatable, Zero-Downtime Multi-Environment Deployments</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">TeamCity Continuous Integration</span>
            <span class="card-badge">Build & Test</span>
          </div>
          <p class="card-p">
            Configuring resilient build pipelines that validate code quality on every push:
          </p>
          <ul class="card-bullets">
            <li><strong>Automated Solution Builds:</strong> MSBuild orchestration restoring NuGet packages, compiling Release targets, and executing Roslyn static analyzers.</li>
            <li><strong>Automated Test Execution:</strong> Running unit and integration test suites (NUnit / xUnit) with code coverage thresholds blocking broken builds.</li>
            <li><strong>Artifact Packaging:</strong> Bundling versioned NuGet packages and Octopus release artifacts with semantic versioning and Git commit SHA tagging.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Octopus Deploy Continuous Delivery</span>
            <span class="card-badge">Release Engine</span>
          </div>
          <p class="card-p">
            Managing clean multi-tenant and multi-environment deployment progression:
          </p>
          <ul class="card-bullets">
            <li><strong>Environment Progression:</strong> Controlled deployment gates across Development ➔ Staging ➔ UAT ➔ Production.</li>
            <li><strong>Configuration Transforms:</strong> Managing sensitive environment variables, connection strings, and AWS IAM role bindings via Octopus scoped variables.</li>
            <li><strong>Zero-Downtime Deployments:</strong> Implementing blue/green IIS deployments and health check warm-ups before taking legacy instances offline.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 8: 24/7 Production On-Call & Datadog Monitoring -->
    <div class="section">
      <div class="section-title">
        7. Production Monitoring & 24/7 On-Call Rotations (Datadog & PagerDuty)
        <span class="tagline">Battle-Tested Incident Management and Telemetry Discipline</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Datadog APM & Telemetry</span>
            <span class="card-badge">Monitoring</span>
          </div>
          <p class="card-p">
            Instrumenting end-to-end tracing across IIS, C# controllers, EF6 database queries, and external APIs:
          </p>
          <ul class="card-bullets">
            <li>p95/p99 endpoint latency tracking.</li>
            <li>Slow SQL query execution alerts.</li>
            <li>Real-time 5xx error rate anomaly detection.</li>
            <li>Custom CRM business transaction metrics.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">PagerDuty 24/7 On-Call</span>
            <span class="card-badge">Incident Response</span>
          </div>
          <p class="card-p">
            Disciplined incident handler experienced in active 24/7 primary and secondary rotations:
          </p>
          <ul class="card-bullets">
            <li>Strict <5-minute page acknowledgment.</li>
            <li>Fast triage: isolate host vs DB vs network.</li>
            <li>Rapid mitigation: rollbacks, pool recycles.</li>
            <li>Clear stakeholder communications during outages.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Post-Mortem & Prevention</span>
            <span class="card-badge">Resilience</span>
          </div>
          <p class="card-p">
            Turning production incidents into permanent platform improvements:
          </p>
          <ul class="card-bullets">
            <li>Authoring blameless post-mortem reports.</li>
            <li>Root cause analysis (5 Whys methodology).</li>
            <li>Implementing defensive circuit breakers.</li>
            <li>Refining alert thresholds to eliminate alert fatigue.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 9: Engineering Mentorship & Code Governance -->
    <div class="section">
      <div class="section-title">
        8. Engineering Mentorship, Code Reviews & Team Culture
        <span class="tagline">Fostering High Technical Standards and Collective Velocity</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Constructive, High-Standard Code Reviews</span>
            <span class="card-badge">Quality Gate</span>
          </div>
          <p class="card-p">
            Reviewing PRs not just for syntax, but for architectural soundness, thread safety, database indexing implications, memory leaks, and adherence to SOLID principles. Providing clear, actionable, and encouraging feedback that levels up team capabilities.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Pair Programming & Developer Mentorship</span>
            <span class="card-badge">Mentorship</span>
          </div>
          <p class="card-p">
            Actively guiding junior and mid-level developers through complex debugging sessions, architectural trade-offs, and legacy refactoring. Developing internal documentation, onboarding runbooks, and design guidelines to accelerate new developer velocity.
          </p>
        </div>
      </div>
    </div>

    <!-- Highlight Callout -->
    <div class="callout-box">
      <div class="callout-title">Commitment to Production Reliability</div>
      <div class="callout-text">
        Having supported mission-critical platforms handling millions of daily customer transactions, I understand that software engineering does not end at code commit. I take personal ownership of production stability, proactive monitoring, and zero-defect deployments.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Senior Software Developer Proposal • CRM Platform</span>
    <span>Page 3 of 4</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
      <a href="https://linkedin.com/in/viranga-lakshan">LinkedIn</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 4: CASE STUDIES & ONBOARDING ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">PRODUCTION <span style="color:#2563eb;">TRACK RECORD</span> <span class="brand-badge">Case Studies</span></div>
        <div class="brand-sub">Enterprise Systems Track Record, CRM Domain Expertise & 30-Day Onboarding Plan</div>
      </div>
      <div class="meta-block">
        <strong>Scale Proven:</strong> 400+ Sites • 1M+ Daily Transactions<br>
        <strong>Domain Focus:</strong> CRM • B2B SaaS • Multi-Tenant Platforms<br>
        <strong>Readiness:</strong> Immediate Start • Full Pacific Time Hours
      </div>
    </div>

    <!-- Section 10: Relevant Enterprise Case Studies -->
    <div class="section">
      <div class="section-title">
        9. Proven Enterprise Production Case Studies
        <span class="tagline">Demonstrated Technical Excellence in Complex Multi-Tenant Platforms</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Case Study 01: Enterprise Financial Platform (MFCS)</span>
            <span class="card-badge">400+ Sites • 1M+ Daily Writes</span>
          </div>
          <p class="card-p">
            <strong>Client / Scope:</strong> Nationwide collection and customer account settlement platform deployed across 400+ branch locations and field terminals.
          </p>
          <ul class="card-bullets">
            <li><strong>Zero Record Loss:</strong> Strict ACID transaction boundaries processing over 1,000,000+ daily receipt postings without a single dropped transaction.</li>
            <li><strong>Lock Contention Elimination:</strong> Replaced blocking row locks with atomic batch CTEs, reducing lock wait times from 1,450ms to 45ms.</li>
            <li><strong>Latency Drop:</strong> Slashed p95 end-of-day synchronization latency from 3,200ms to 480ms (-85.0%).</li>
            <li><strong>Cloud Modernization:</strong> Migrated database layers to AWS RDS with continuous uptime.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Case Study 02: Mature Banking Platform (SomBank TP V5)</span>
            <span class="card-badge">2-Year Mature Core Codebase</span>
          </div>
          <p class="card-p">
            <strong>Client / Scope:</strong> Engineering Change Requests on an existing 2-year-old mission-critical banking core written by third-party vendor teams.
          </p>
          <ul class="card-bullets">
            <li><strong>Zero-Regression Feature Additions:</strong> Successfully extended C# .NET Web API endpoints and financial balance calculators without breaking existing integrations.</li>
            <li><strong>Safety Test Harness:</strong> Designed comprehensive integration test suites before modifying legacy stored procedures and entity mappings.</li>
            <li><strong>Security Compliance:</strong> Enforced OAuth2 / JWT authentication, role-based permissions, and immutable audit event logging.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 11: CRM Domain & B2B SaaS Competencies -->
    <div class="section">
      <div class="section-title">
        10. CRM & B2B SaaS Domain Knowledge
        <span class="tagline">Architectural Intuition for Customer Data, Pipelines, and Integrations</span>
      </div>
      <div class="grid-3">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Multi-Tenant Data Isolation</span>
            <span class="card-badge">Data Security</span>
          </div>
          <p class="card-p">
            Guaranteed data segregation across tenants using indexed <code>TenantId</code> scoping in repository filters, preventing cross-organization data leakage.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Custom Fields & Extensibility</span>
            <span class="card-badge">Schema Design</span>
          </div>
          <p class="card-p">
            Architecting hybrid relational-JSON schemata allowing enterprise clients to define custom fields on Contacts, Deals, and Accounts with high-speed indexing.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Webhook & 3rd-Party APIs</span>
            <span class="card-badge">Integrations</span>
          </div>
          <p class="card-p">
            Engineering resilient incoming and outgoing webhook engines with automated retry policies, idempotency keys, and signature verification.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 12: 30-Day Ramp-up Plan -->
    <div class="section">
      <div class="section-title">
        11. Rapid 30-Day Onboarding & Value Delivery Roadmap
        <span class="tagline">From Day-1 Environment Setup to Independent Feature Ownership</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 1 – 7: Ramp-Up</span>
            <span class="card-badge">Onboarding</span>
          </div>
          <p class="card-p">
            Clone solution, establish working local builds, verify TeamCity CI pipeline, map core domain models, and ship first low-risk bug fix / documentation PR.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 8 – 20: Feature Velocity</span>
            <span class="card-badge">Execution</span>
          </div>
          <p class="card-p">
            Take ownership of assigned sprint tickets in ASP.NET MVC / C#, write automated unit tests, actively contribute to code reviews, and shadow senior on-call rotation.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Days 21 – 30: Autonomous Drive</span>
            <span class="card-badge">Ownership</span>
          </div>
          <p class="card-p">
            Deliver end-to-end CRM features independently, participate fully as primary in PagerDuty on-call rotations, and identify proactive .NET / AWS optimization targets.
          </p>
        </div>
      </div>
    </div>

    <!-- Immediate Kickoff Callout -->
    <div class="callout-box" style="margin-top: 5px;">
      <div class="callout-title">Ready for Immediate Technical Interview & Code Pairing</div>
      <div class="callout-text">
        I am available immediately for an introductory interview, technical deep-dive, or live code review pairing session at your convenience in Pacific Time. Let's connect to discuss how I can accelerate your CRM platform engineering goals.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Viranga Lakshan • Senior Software Developer Proposal • CRM Platform</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\CRM_Platform_Senior_DotNet_Developer"
    html_path = os.path.join(base_dir, "proposal.html")
    pdf_path = os.path.join(base_dir, "Viranga_Lakshan_Senior_DotNet_CRM_Developer_Proposal.pdf")

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
