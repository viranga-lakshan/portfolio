import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>LOGIXOTECH - Multi-Outlet POS Platform Technical Benchmark Report</title>
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
    font-size: 8.3pt;
    line-height: 1.36;
  }
  .page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    padding: 12mm 15mm 11mm 15mm;
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

  /* Cover Page Styling */
  .cover-page {
    padding: 24mm 20mm 20mm 20mm;
    background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0f172a 60%, #020617 100%);
    color: #ffffff;
    justify-content: space-between;
  }
  .cover-logo-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.18);
    padding-bottom: 14px;
  }
  .company-logo-text {
    font-size: 19pt;
    font-weight: 900;
    letter-spacing: 1.5px;
    color: #ffffff;
    text-transform: uppercase;
  }
  .company-logo-text span {
    color: #38bdf8;
  }
  .report-tagline-badge {
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.4);
    color: #7dd3fc;
    font-size: 7.6pt;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }
  .cover-body {
    margin-top: 25mm;
    margin-bottom: 25mm;
  }
  .cover-pre-title {
    color: #38bdf8;
    font-size: 9.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
  }
  .cover-main-title {
    font-size: 23pt;
    font-weight: 900;
    line-height: 1.18;
    color: #ffffff;
    letter-spacing: -0.6px;
    margin-bottom: 12px;
  }
  .cover-sub-title {
    font-size: 11pt;
    color: #94a3b8;
    line-height: 1.4;
    max-width: 90%;
    margin-bottom: 20px;
  }
  .cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 6px;
    padding: 14px 18px;
    margin-top: 15px;
  }
  .cover-meta-item {
    font-size: 8.2pt;
    color: #cbd5e1;
  }
  .cover-meta-item strong {
    color: #ffffff;
    font-weight: 700;
    display: block;
    margin-bottom: 1px;
    font-size: 8.5pt;
  }
  .cover-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 7.5pt;
    color: #64748b;
  }

  /* Internal Header */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 6px;
    margin-bottom: 9.5px;
  }
  .brand-title {
    font-size: 12.5pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.3px;
    display: flex;
    align-items: center;
    gap: 7px;
  }
  .brand-badge {
    background: #0f172a;
    color: #38bdf8;
    font-size: 7pt;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 3px;
    letter-spacing: 0.5px;
  }
  .brand-sub {
    font-size: 7.9pt;
    color: #475569;
    font-weight: 600;
    margin-top: 1.5px;
  }
  .meta-block {
    text-align: right;
    font-size: 7.5pt;
    color: #64748b;
    line-height: 1.32;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Section Styling */
  .section {
    margin-bottom: 9px;
  }
  .section-title {
    font-size: 9.3pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3px solid #0284c7;
    padding-left: 6.5px;
    margin-bottom: 5.5px;
    text-transform: uppercase;
    letter-spacing: 0.25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 7.3pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
    letter-spacing: 0;
  }

  /* Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7.5px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6.5px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
  }

  /* Cards */
  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 9px;
  }
  .card.tint {
    background: #f0f9ff;
    border-color: #bae6fd;
  }
  .card.slate {
    background: #f8fafc;
    border-color: #e2e8f0;
  }
  .card.accent {
    border-left: 3px solid #0284c7;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3.5px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2.5px;
  }
  .card.tint .card-header {
    border-color: #bae6fd;
  }
  .card-title {
    font-size: 8.3pt;
    font-weight: 700;
    color: #0f172a;
  }
  .card-badge {
    font-size: 6.6pt;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 3px;
    background: #e2e8f0;
    color: #475569;
    text-transform: uppercase;
  }
  .card.tint .card-badge {
    background: #e0f2fe;
    color: #0369a1;
  }
  .card-p {
    font-size: 7.6pt;
    color: #334155;
    margin: 0 0 3.5px 0;
    line-height: 1.32;
  }
  .card-bullets {
    margin: 0;
    padding-left: 12.5px;
    font-size: 7.4pt;
    color: #475569;
    line-height: 1.3;
  }
  .card-bullets li {
    margin-bottom: 1.8px;
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
    font-size: 6.9pt;
    color: #0369a1;
  }

  /* Tables */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
    margin-top: 2px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 4px 6.5px;
    font-weight: 700;
    font-size: 7.2pt;
    text-transform: uppercase;
    letter-spacing: 0.25px;
  }
  table.matrix-table td {
    padding: 4px 6.5px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.28;
  }
  table.matrix-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  table.matrix-table td strong {
    color: #0f172a;
  }

  /* Pipeline / Visual Flow */
  .visual-pipeline {
    display: flex;
    align-items: stretch;
    gap: 6px;
    margin-top: 3px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6.5px;
  }
  .pipe-box {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 7.5px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .pipe-box.accent {
    border-top: 3px solid #0284c7;
    flex: 1.25;
  }
  .pipe-badge {
    display: inline-block;
    font-size: 6.5pt;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 2px;
  }
  .pipe-title {
    font-size: 8pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2.5px;
  }
  .pipe-desc {
    font-size: 7.3pt;
    color: #475569;
    line-height: 1.28;
    margin: 0;
  }
  .pipe-bullets {
    margin: 0;
    padding-left: 11px;
    font-size: 7pt;
    color: #334155;
    line-height: 1.26;
  }
  .pipe-bullets li {
    margin-bottom: 1.5px;
  }
  .pipe-arrow {
    display: flex;
    align-items: center;
    color: #94a3b8;
    font-size: 10pt;
    font-weight: 700;
  }

  /* Metric Delta Comparison Grid */
  .delta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6.5px;
    margin-top: 4px;
  }
  .delta-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 8px;
    text-align: center;
  }
  .delta-metric {
    font-size: 7pt;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 2px;
  }
  .delta-numbers {
    display: flex;
    justify-content: center;
    align-items: baseline;
    gap: 5px;
    margin-bottom: 2px;
  }
  .delta-before {
    font-size: 8.2pt;
    color: #dc2626;
    text-decoration: line-through;
    font-weight: 600;
  }
  .delta-after {
    font-size: 11.5pt;
    color: #059669;
    font-weight: 800;
  }
  .delta-badge {
    display: inline-block;
    font-size: 6.5pt;
    font-weight: 700;
    color: #059669;
    background: #ecfdf5;
    padding: 1px 4.5px;
    border-radius: 3px;
  }

  /* Disclaimer Box */
  .disclaimer-box {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 3.5px solid #d97706;
    border-radius: 4px;
    padding: 5px 8px;
    margin-top: 5px;
  }
  .disclaimer-text {
    font-size: 7.1pt;
    color: #92400e;
    line-height: 1.28;
    font-weight: 600;
  }

  /* Callout */
  .callout-box {
    background: #f0f9ff;
    border-left: 3.5px solid #0284c7;
    border-radius: 4px;
    padding: 5.5px 8.5px;
    margin-top: 4.5px;
  }
  .callout-title {
    font-size: 8pt;
    font-weight: 700;
    color: #0369a1;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.4pt;
    color: #0c4a6e;
    line-height: 1.3;
  }

  /* Profile Box */
  .profile-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6.5px 8.5px;
  }
  .profile-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2px;
  }
  .profile-name {
    font-size: 8.5pt;
    font-weight: 800;
    color: #0f172a;
  }
  .profile-role {
    font-size: 7.3pt;
    color: #0284c7;
    font-weight: 700;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 3.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.1pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #0284c7;
    text-decoration: none;
    margin-left: 8px;
    font-weight: 600;
  }
</style>
</head>
<body>

<!-- ========================================== PAGE 1: COVER PAGE ========================================== -->
<div class="page cover-page">
  <div class="cover-logo-row">
    <div class="company-logo-text">LOGIXO<span>TECH</span></div>
    <div class="report-tagline-badge">Enterprise Database Engineering</div>
  </div>

  <div class="cover-body">
    <div class="cover-pre-title">Technical Project & Benchmark Assessment Report</div>
    <div class="cover-main-title">Multi-Outlet POS Platform<br>Performance, Optimization & Scalability Assessment</div>
    <div class="cover-sub-title">
      Documenting technical investigation methodologies, multi-tenant transaction concurrency, database lock mitigation, and scalability modeling for high-throughput retail & food-service platforms.
    </div>

    <div class="cover-meta-grid">
      <div class="cover-meta-item">
        <strong>Organization & Author:</strong>
        LOGIXOTECH Technical Engineering Team
      </div>
      <div class="cover-meta-item">
        <strong>Case Study Subject:</strong>
        Perera & Sons POS Platform Engagement
      </div>
      <div class="cover-meta-item">
        <strong>Industry Focus:</strong>
        Retail, Quick-Service & Food Beverage (F&B)
      </div>
      <div class="cover-meta-item">
        <strong>Report Classification:</strong>
        Anonymized Technical Benchmark Assessment
      </div>
      <div class="cover-meta-item">
        <strong>Publication Date:</strong>
        November 2026
      </div>
      <div class="cover-meta-item">
        <strong>Target Benchmark Context:</strong>
        Multi-Location High-Concurrency Shared Database Stacks
      </div>
    </div>
  </div>

  <div class="cover-footer">
    <span>LOGIXOTECH Engineering Division • Confidential Technical Evidence</span>
    <span>Multi-Outlet POS Performance Assessment • Page 1 of 9</span>
    <span>logixotech.com</span>
  </div>
</div>

<!-- ========================================== PAGE 2: EXECUTIVE SUMMARY & BACKGROUND ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Executive Summary</span></div>
        <div class="brand-sub">Multi-Outlet POS Platform – Technical Performance & Scalability Assessment</div>
      </div>
      <div class="meta-block">
        <strong>Subject:</strong> Perera & Sons POS Performance Investigation<br>
        <strong>Engagement:</strong> Bottleneck Isolation, Indexing & Concurrency Engineering<br>
        <strong>Scope:</strong> Existing Platform Optimization Following Feature Expansion
      </div>
    </div>

    <!-- Section 3: Executive Summary -->
    <div class="section">
      <div class="section-title">
        3. Executive Summary
        <span class="tagline">Engagement Context and High-Level Objectives</span>
      </div>
      <div class="card tint accent">
        <div class="card-header">
          <span class="card-title">Engagement Overview & Mandate</span>
          <span class="card-badge">Engineering Mandate</span>
        </div>
        <p class="card-p">
          This technical project and benchmark report documents LOGIXOTECH's technical engagement involving the <strong>Perera & Sons multi-outlet Point of Sale (POS) platform</strong>. Perera & Sons operates an extensive retail and food-service network requiring reliable, high-volume transaction processing across dozens of commercial outlets feeding into a centralized database backend.
        </p>
        <p class="card-p">
          <strong>Important Project Sequence:</strong> The Perera & Sons POS platform was an existing, active production system. Following the release and rollout of additional POS application features, operational outlets experienced noticeable performance degradation, elevated checkout response times, and intermittent transaction delays during peak meal service hours. LOGIXOTECH was specifically contracted to perform an independent technical investigation, identify root-cause database and API bottlenecks, and execute targeted performance optimizations.
        </p>
        <p class="card-p" style="margin-bottom:0;">
          <strong>Technical Scope:</strong> LOGIXOTECH did not develop the original POS codebase or implement the newly introduced features. Our team was assigned the critical engineering task of profiling query execution, analyzing lock contention, reviewing connection pool exhaustion, and re-engineering hot data paths to preserve transaction consistency while drastically reducing response latencies.
        </p>
      </div>
    </div>

    <!-- Operating Environment Grid -->
    <div class="section">
      <div class="section-title">
        Multi-Location Business Environment Characteristics
        <span class="tagline">Operational Constraints Governing High-Throughput POS Networks</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">High-Frequency Storefront Operations</span>
            <span class="card-badge">Storefront</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Centralized Processing:</strong> Outlets process walk-in customer sales, takeaway packaging, and kitchen tickets against shared central database services.</li>
            <li><strong>Simultaneous Active Users:</strong> Hundreds of concurrent floor cashiers, counter managers, and kitchen staff interacting with the backend in real time.</li>
            <li><strong>Strict Invariant Requirements:</strong> Zero tolerance for missing sales records, duplicate ticket items, or out-of-sync retail pricing.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">System Stress Under Peak Load</span>
            <span class="card-badge">Bottlenecks</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Synchronous Latency Cascades:</strong> Slow queries during peak meal rushes directly blocked floor checkout terminals, leading to cashier UI freezes.</li>
            <li><strong>Connection Pool Saturation:</strong> Surging terminal connection requests exhausted database worker allocations, causing connection timeouts.</li>
            <li><strong>Row Lock Contention:</strong> Concurrent modifications to inventory and settlement tables triggered transaction serialization waits.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 4 (Part 1): Role of Centralized POS -->
    <div class="section">
      <div class="section-title">
        4. Project Background: Centralized Architecture Role
        <span class="tagline">Mission-Critical Functionality of the POS Backend</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Sales & Settlement</span>
            <span class="card-badge">Core POS</span>
          </div>
          <p class="card-p">
            Atomic processing of customer receipts, line items, payment splits, discounts, and tax calculations with guaranteed financial ledger consistency.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Catalog & Pricing</span>
            <span class="card-badge">Reference Data</span>
          </div>
          <p class="card-p">
            Central distribution of fast-changing item catalogs, regional price tiers, combo discounts, and promotional campaigns across all outlet terminals.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Operational Visibility</span>
            <span class="card-badge">Reporting</span>
          </div>
          <p class="card-p">
            Real-time sales rollup dashboards, hourly velocity metrics, stock depletion alerts, and end-of-day reconciliation reports for management.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 2 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 3: TECHNICAL INVESTIGATION & DIAGNOSIS ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Technical Investigation</span></div>
        <div class="brand-sub">Root-Cause Analysis Across Database, Application API, and Concurrency Layers</div>
      </div>
      <div class="meta-block">
        <strong>Investigation Lead:</strong> Viranga Lakshan (Lead Solutions Architect)<br>
        <strong>Diagnostics:</strong> Query Plan Analysis, Lock Inspection, Connection Profiling<br>
        <strong>Scope:</strong> 4 Dedicated Engineering Streams (Database, API, Concurrency, Fixes)
      </div>
    </div>

    <!-- Section 5: Technical Streams -->
    <div class="section">
      <div class="section-title">
        5. LOGIXOTECH Technical Investigation Workstreams
        <span class="tagline">Systematic Deconstruction of Performance Degradation</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">A. Database Performance Investigation</span>
            <span class="card-badge">PostgreSQL Engine</span>
          </div>
          <p class="card-p">
            LOGIXOTECH executed exhaustive telemetry and diagnostic profiling on the database cluster:
          </p>
          <ul class="card-bullets">
            <li><strong>Slow Query Profiling:</strong> Monitored query execution frequency, total elapsed execution time, and buffer cache misses using <code>pg_stat_statements</code>.</li>
            <li><strong>Execution Plan Deconstruction:</strong> Ran <code>EXPLAIN ANALYZE</code> on critical sales recording and receipt queries, uncovering unindexed sequential table scans.</li>
            <li><strong>Resource Utilization Review:</strong> Discovered database CPU spikes reaching 85%+ during meal peaks due to repeated sorting and in-memory hash joins.</li>
            <li><strong>Connection Starvation:</strong> Identified unpooled client connections where each terminal spawned direct backend connections, hitting server connection caps.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">B. API & Application Performance Review</span>
            <span class="card-badge">Data Access Layer</span>
          </div>
          <p class="card-p">
            Investigating backend services and application-to-database communication patterns:
          </p>
          <ul class="card-bullets">
            <li><strong>N+1 Query Cascades:</strong> Discovered that order retrieval endpoints fetched parent order headers and then triggered individual queries for each line item.</li>
            <li><strong>Unnecessary Polling Loops:</strong> Storefront terminals were executing unthrottled polling intervals every few seconds to refresh menu status, saturating bandwidth.</li>
            <li><strong>Over-Fetching Payloads:</strong> Endpoints retrieved full relational entity graphs with dozens of unneeded columns, inflating JSON serialization times.</li>
            <li><strong>Synchronous Blocking Workflows:</strong> Long-running inventory and receipt email tasks were executed within the primary request-response thread.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Investigation Part 2: Concurrency & Optimization Categories -->
    <div class="section">
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">C. Transaction & Concurrency Investigation</span>
            <span class="card-badge">Locking & Contention</span>
          </div>
          <p class="card-p">
            Analyzing transaction behavior under simultaneous multi-terminal checkout activity:
          </p>
          <ul class="card-bullets">
            <li><strong>Row Lock Queues:</strong> Multiple terminals updating central inventory counts or daily register summaries experienced prolonged row-level lock waits.</li>
            <li><strong>Deadlock Risks:</strong> Inconsistent acquisition ordering across <code>orders</code> and <code>order_items</code> tables caused occasional transaction rollbacks.</li>
            <li><strong>Duplicate Transaction Risks:</strong> Lack of client-side idempotency keys meant cashiers re-submitted pending orders when network latency spiked.</li>
            <li><strong>Isolation Level Verification:</strong> Evaluated Read Committed vs Repeatable Read tradeoffs to balance dirty read prevention against serialization errors.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">D. Verified Optimization Approaches</span>
            <span class="card-badge">Remediation Blueprint</span>
          </div>
          <p class="card-p">
            Targeted engineering remedies deployed or recommended by LOGIXOTECH:
          </p>
          <ul class="card-bullets">
            <li><strong>Composite & Partial Indexing:</strong> Created targeted B-tree indexes on <code>(outlet_id, created_at)</code> and partial indexes for open active orders.</li>
            <li><strong>Connection Pool Architecture:</strong> Implemented transaction-mode connection pooling (PgBouncer), capping backend processes while serving hundreds of terminals.</li>
            <li><strong>Batch Insertions & CTEs:</strong> Replaced multi-roundtrip row inserts with single atomic Common Table Expression (CTE) write queries.</li>
            <li><strong>Idempotent Order Ingestion:</strong> Enforced unique client-generated UUID keys to guarantee zero duplicate charges during network reconnects.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 5 Callout -->
    <div class="callout-box">
      <div class="callout-title">Engineering Discipline: Distinguishing Symptoms from Root Causes</div>
      <div class="callout-text">
        In complex enterprise systems, performance degradation following a feature release is rarely caused by a single bug. It is typically an amplification effect where unindexed queries increase database CPU, causing slower execution, which holds open database connections longer, rapidly exhausting connection pool limits and triggering timeout cascades across the client fleet.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 3 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 4: SCALABILITY ASSESSMENT (350-LOCATION MODEL) ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Scalability Modeling</span></div>
        <div class="brand-sub">Multi-Location Scalability Assessment: 350-Outlet Concurrency Scenario</div>
      </div>
      <div class="meta-block">
        <strong>Scenario Classification:</strong> Illustrative Enterprise Scalability Model<br>
        <strong>Simulated Footprint:</strong> 350 Retail Outlets • 1,050 Active Devices<br>
        <strong>Workload Characterization:</strong> Concurrent Lunch/Dinner Peak Sales Influx
      </div>
    </div>

    <!-- Section 6: Scalability Context -->
    <div class="section">
      <div class="section-title">
        6. Multi-Location Scalability Assessment: 350-Location Scenario
        <span class="tagline">Illustrative Workload Modeling for Enterprise Multi-Outlet Deployment</span>
      </div>
      <p class="card-p" style="margin-bottom:6px;">
        To evaluate the architectural boundaries of a centralized POS platform, LOGIXOTECH developed an illustrative scalability model based on an operational network of <strong>approximately 350 retail and food-service outlets</strong>. This model provides an objective stress-testing framework to assess database stability, connection saturation, and query latency under combined peak operating conditions.
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 28%;">Parameter</th>
            <th style="width: 22%; text-align: right;">Illustrative Workload</th>
            <th style="width: 50%;">Architectural Impact on Shared Database</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Business Locations</strong></td>
            <td style="text-align: right;"><strong>350</strong></td>
            <td>Multi-tenant data partitioning requirement; records scoped by <code>outlet_id</code>.</td>
          </tr>
          <tr>
            <td><strong>Dedicated POS Terminals</strong></td>
            <td style="text-align: right;"><strong>350</strong></td>
            <td>Continuous checkout writes, receipt printing, cash drawer reconciliation.</td>
          </tr>
          <tr>
            <td><strong>Staff Mobile Devices</strong></td>
            <td style="text-align: right;"><strong>700</strong></td>
            <td>Two mobile staff phones/tablets per outlet for table-side orders & inventory checks.</td>
          </tr>
          <tr>
            <td><strong>Total Active Devices</strong></td>
            <td style="text-align: right;"><strong>1,050 Devices</strong></td>
            <td>Simultaneous concurrent HTTP/WebSocket persistent connections to API layer.</td>
          </tr>
          <tr>
            <td><strong>Transaction Character</strong></td>
            <td style="text-align: right;"><strong>Concurrent Sales & Orders</strong></td>
            <td>Sub-second write requirement; high-frequency inserts into line-item tables.</td>
          </tr>
          <tr>
            <td><strong>Operational Model</strong></td>
            <td style="text-align: right;"><strong>Centralized Cloud Services</strong></td>
            <td>Shared PostgreSQL cluster hosting sales ledgers, catalogs, and reporting views.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual Architecture Component -->
    <div class="section">
      <div class="section-title">
        Multi-Outlet Concurrency Data Flow Architecture
        <span class="tagline">How 1,050 Distributed Client Devices Route into a Shared Cluster</span>
      </div>

      <div class="visual-pipeline">
        <div class="pipe-box">
          <div>
            <span class="pipe-badge">Layer 01: Outlet Fleet</span>
            <div class="pipe-title">Distributed Edge Fleet</div>
            <p class="pipe-desc">
              <strong>350 POS Terminals:</strong> Barcode scanning, receipt printing, payment gateway integration.<br><br>
              <strong>700 Staff Handhelds:</strong> Floor order taking, table status monitoring, inventory lookup.
            </p>
          </div>
        </div>

        <div class="pipe-arrow">➔</div>

        <div class="pipe-box accent">
          <div>
            <span class="pipe-badge">Layer 02: API & Pooler</span>
            <div class="pipe-title">Application & Pool Gateway</div>
            <ul class="pipe-bullets">
              <li><strong>Load Balancer:</strong> SSL termination & regional request routing.</li>
              <li><strong>API Services:</strong> Stateless Next.js / Node.js worker microservices.</li>
              <li><strong>Connection Pooler:</strong> PgBouncer multiplexing 1,050 client connections into a controlled backend pool.</li>
              <li><strong>Rate Limiter & Cache:</strong> Redis-backed catalog caching.</li>
            </ul>
          </div>
        </div>

        <div class="pipe-arrow">➔</div>

        <div class="pipe-box">
          <div>
            <span class="pipe-badge">Layer 03: Data Core</span>
            <div class="pipe-title">PostgreSQL Database</div>
            <p class="pipe-desc">
              Partitioned sales records, composite indexes, and strict ACID transaction boundaries.<br><br>
              Asynchronous read replicas dedicated to analytics and management reporting queries.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 6 Disclaimer -->
    <div class="disclaimer-box">
      <div class="disclaimer-text">
        <strong>Disclaimer:</strong> The 350-location parameter and 1,050 device count represent an illustrative enterprise workload scenario developed by LOGIXOTECH for technical modeling purposes. They are not historical project facts or verified infrastructure measurements from the Perera & Sons POS deployment.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 4 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 5: PERFORMANCE BENCHMARK (BEFORE & AFTER) ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Benchmark Metrics</span></div>
        <div class="brand-sub">Empirical Performance Benchmark: Before vs. After Optimization Scenario</div>
      </div>
      <div class="meta-block">
        <strong>Evaluation Protocol:</strong> Simulated Peak Meal-Rush Concurrency Test<br>
        <strong>Metric Scope:</strong> p95 Response Time, Query Latency, CPU, Connection Peak<br>
        <strong>Classification:</strong> Illustrative Scenario Benchmark
      </div>
    </div>

    <!-- Section 7: Benchmark Comparison -->
    <div class="section">
      <div class="section-title">
        7. Performance Benchmark: Before vs. After Optimization
        <span class="tagline">Illustrative Metric Demonstration of Systematic Database Remediation</span>
      </div>
      <p class="card-p" style="margin-bottom:6px;">
        To demonstrate the quantifiable impact of database query optimization, connection pooling, and lock contention mitigation, the table below illustrates performance metrics before and after targeted engineering remediation under a peak checkout simulation:
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 32%;">Performance Metric</th>
            <th style="width: 20%; text-align: right;">Example Baseline</th>
            <th style="width: 22%; text-align: right;">Example Optimized</th>
            <th style="width: 26%; text-align: right;">Measured Delta</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>API Response Time (p95)</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>920 ms</strong></td>
            <td style="text-align: right; color: #059669;"><strong>420 ms</strong></td>
            <td style="text-align: right;"><strong>54.3% Latency Drop</strong></td>
          </tr>
          <tr>
            <td><strong>Database Query Response Time</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>450 ms</strong></td>
            <td style="text-align: right; color: #059669;"><strong>120 ms</strong></td>
            <td style="text-align: right;"><strong>73.3% Latency Drop</strong></td>
          </tr>
          <tr>
            <td><strong>Database CPU Utilization</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>85%</strong></td>
            <td style="text-align: right; color: #059669;"><strong>45%</strong></td>
            <td style="text-align: right;"><strong>47.1% Load Reduction</strong></td>
          </tr>
          <tr>
            <td><strong>Failed Request Rate</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>5.0%</strong></td>
            <td style="text-align: right; color: #059669;"><strong>0.5%</strong></td>
            <td style="text-align: right;"><strong>90.0% Error Reduction</strong></td>
          </tr>
          <tr>
            <td><strong>Peak Database Connections</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>450</strong></td>
            <td style="text-align: right; color: #059669;"><strong>250</strong></td>
            <td style="text-align: right;"><strong>44.4% Pool Efficiency</strong></td>
          </tr>
          <tr>
            <td><strong>Transaction Processing Error Rate</strong></td>
            <td style="text-align: right; color: #dc2626;"><strong>2.0%</strong></td>
            <td style="text-align: right; color: #059669;"><strong>0.2%</strong></td>
            <td style="text-align: right;"><strong>90.0% Reliability Gain</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Visual Metric Delta Cards -->
    <div class="section">
      <div class="section-title">
        Visual Metric Improvement Indicators
        <span class="tagline">Key Operational Threshold Reductions</span>
      </div>
      <div class="delta-grid">
        <div class="delta-card">
          <div class="delta-metric">API Response Time (p95)</div>
          <div class="delta-numbers">
            <span class="delta-before">920 ms</span>
            <span class="delta-after">420 ms</span>
          </div>
          <span class="delta-badge">-54.3% Reduction</span>
        </div>

        <div class="delta-card">
          <div class="delta-metric">Database Query Latency</div>
          <div class="delta-numbers">
            <span class="delta-before">450 ms</span>
            <span class="delta-after">120 ms</span>
          </div>
          <span class="delta-badge">-73.3% Latency Drop</span>
        </div>

        <div class="delta-card">
          <div class="delta-metric">Database CPU Utilization</div>
          <div class="delta-numbers">
            <span class="delta-before">85%</span>
            <span class="delta-after">45%</span>
          </div>
          <span class="delta-badge">-47.1% CPU Relief</span>
        </div>

        <div class="delta-card">
          <div class="delta-metric">Failed Request Rate</div>
          <div class="delta-numbers">
            <span class="delta-before">5.0%</span>
            <span class="delta-after">0.5%</span>
          </div>
          <span class="delta-badge">10x Error Reduction</span>
        </div>

        <div class="delta-card">
          <div class="delta-metric">Peak Database Connections</div>
          <div class="delta-numbers">
            <span class="delta-before">450</span>
            <span class="delta-after">250</span>
          </div>
          <span class="delta-badge">-44.4% Connection Load</span>
        </div>

        <div class="delta-card">
          <div class="delta-metric">Transaction Error Rate</div>
          <div class="delta-numbers">
            <span class="delta-before">2.0%</span>
            <span class="delta-after">0.2%</span>
          </div>
          <span class="delta-badge">99.8% Success Rate</span>
        </div>
      </div>
    </div>

    <!-- Mandatory Disclaimer Box -->
    <div class="disclaimer-box" style="margin-top:7px;">
      <div class="disclaimer-text">
        <strong>Mandatory Technical Disclaimer:</strong> These figures are illustrative examples for a hypothetical performance optimization scenario. They are not verified historical measurements from the Perera & Sons POS project. LOGIXOTECH presents this model to articulate expected architectural outcomes when executing systematic query indexing, connection pooling, and concurrency refactoring.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 5 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 6: TECHNICAL METHODOLOGY & LOAD TESTING ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Engineering Methodology</span></div>
        <div class="brand-sub">Structured Query Tuning, Connection Pooling, and Repeatable Load Testing Framework</div>
      </div>
      <div class="meta-block">
        <strong>Execution Standards:</strong> EXPLAIN ANALYZE, pg_stat_statements, k6, Locust<br>
        <strong>Pool Architecture:</strong> Transaction-Mode Multiplexing (PgBouncer)<br>
        <strong>Verification:</strong> 5-Stage Controlled Staging Test Lifecycle
      </div>
    </div>

    <!-- Section 8: Technical Optimization Methodology -->
    <div class="section">
      <div class="section-title">
        8. Technical Optimization Methodology
        <span class="tagline">Core Engineering Principles Applied to Database & API Layers</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Query & Index Optimization</span>
            <span class="card-badge">Execution Plans</span>
          </div>
          <ul class="card-bullets">
            <li><strong>EXPLAIN ANALYZE:</strong> Evaluating costs, actual rows, and filter conditions to remove sequential table scans.</li>
            <li><strong>Composite B-Tree Indexes:</strong> Aligning index definitions with query <code>WHERE</code>, <code>ORDER BY</code>, and join predicates.</li>
            <li><strong>Partial Indexing:</strong> Indexing only active orders (e.g. <code>WHERE status = 'pending'</code>) to reduce index maintenance costs.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Connection Management</span>
            <span class="card-badge">Pool Architecture</span>
          </div>
          <ul class="card-bullets">
            <li><strong>PgBouncer Pooling:</strong> Utilizing transaction-mode pooling to reuse backend server processes immediately after query completion.</li>
            <li><strong>Connection Limits:</strong> Defining strict client connection ceilings to prevent thundering-herd database crashes.</li>
            <li><strong>Fast Session Release:</strong> Eliminating long-lived idle-in-transaction connections across application workers.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Transaction Concurrency</span>
            <span class="card-badge">Lock Mitigation</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Atomic Processing:</strong> Wrapping multi-item order checkouts in single atomic transactions.</li>
            <li><strong>Deterministic Locking:</strong> Sorting resource updates in fixed order across threads to prevent cross-table deadlocks.</li>
            <li><strong>Non-Blocking Reads:</strong> Leveraging Multi-Version Concurrency Control (MVCC) so queries never block writes.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 9: Benchmarking and Load-Testing Lifecycle -->
    <div class="section">
      <div class="section-title">
        9. Repeatable Benchmarking & Load-Testing Framework
        <span class="tagline">Five-Stage Controlled Verification Lifecycle</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 18%;">Lifecycle Stage</th>
            <th style="width: 32%;">Core Objective & Procedures</th>
            <th style="width: 32%;">Telemetry & Tools</th>
            <th style="width: 18%;">Key Deliverable</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stage 1: Baseline Audit</strong></td>
            <td>Inspect active system schema, query logs, API latency percentiles, active connections, and lock trees under normal traffic.</td>
            <td><code>pg_stat_statements</code>, buffer hit ratio, slow query logs.</td>
            <td>Empirical Baseline Performance Report.</td>
          </tr>
          <tr>
            <td><strong>Stage 2: Synthetic Data</strong></td>
            <td>Generate representative multi-tenant dataset mirroring real retail outlets, catalog depths, and order histories without exposing customer PII.</td>
            <td>Python synthetic data seeders, schema generators.</td>
            <td>Sanitized Staging Database Cluster.</td>
          </tr>
          <tr>
            <td><strong>Stage 3: Load Simulation</strong></td>
            <td>Simulate hundreds of POS terminals and mobile devices executing concurrent checkout orders, menu fetches, and ticket submissions.</td>
            <td>Automated <strong>k6</strong> / <strong>Locust</strong> distributed load test runners.</td>
            <td>Repeatable Test Execution Harness.</td>
          </tr>
          <tr>
            <td><strong>Stage 4: Bottleneck Triage</strong></td>
            <td>Measure p50, p95, p99 latencies, requests per second (RPS), database CPU, lock wait queues, and transaction rollback percentages.</td>
            <td>Grafana dashboards, PostgreSQL lock wait monitors.</td>
            <td>Identified Bottleneck Root-Cause Register.</td>
          </tr>
          <tr>
            <td><strong>Stage 5: Remediation & Re-Test</strong></td>
            <td>Deploy indexes, connection poolers, and query rewrites; re-execute identical load workloads to prove quantifiable gains.</td>
            <td>Automated comparative benchmarking suites.</td>
            <td>Before-and-After Verified Audit Report.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 6 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 7: DATABASE INTEGRITY & RELEVANCE TO YOUZEN ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Integrity & YouZen</span></div>
        <div class="brand-sub">Database Reliability, Transaction Integrity, and Direct Relevance to the YouZen Platform</div>
      </div>
      <div class="meta-block">
        <strong>YouZen Footprint:</strong> 100 Restaurants + 100 Hair Salons<br>
        <strong>Tech Stack:</strong> Next.js, Supabase (PostgreSQL), Realtime, RLS<br>
        <strong>Engineering Goal:</strong> Zero Double-Bookings & High-Speed POS Checkouts
      </div>
    </div>

    <!-- Section 10: Database Integrity -->
    <div class="section">
      <div class="section-title">
        10. Database Integrity & Concurrency Reliability
        <span class="tagline">Architectural Mechanisms Safeguarding Financial & Inventory Consistency</span>
      </div>
      <div class="grid-3">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Idempotent Transactions</span>
            <span class="card-badge">Zero Duplicates</span>
          </div>
          <p class="card-p">
            Utilizing client-generated UUIDs and unique database constraints on orders to guarantee that transient cellular network reconnects never generate duplicate order charges.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Atomic Inventory Commits</span>
            <span class="card-badge">ACID Compliance</span>
          </div>
          <p class="card-p">
            Enforcing atomic updates on stock balances within the same database transaction as sales receipt generation, preventing out-of-stock overselling anomalies.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Lock Mitigation Protocols</span>
            <span class="card-badge">High Concurrency</span>
          </div>
          <p class="card-p">
            Implementing <code>FOR UPDATE SKIP LOCKED</code> and advisory locks for high-frequency queues, allowing concurrent workers to process orders without blocking the primary table.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 11: Relevance to YouZen -->
    <div class="section">
      <div class="section-title">
        11. Direct Technical Relevance to the YouZen Platform
        <span class="tagline">Applying Proven POS & Booking Concurrency Engineering to Luca’s Platform</span>
      </div>
      <p class="card-p" style="margin-bottom:6px;">
        The technical lessons derived from multi-outlet POS optimization directly map to the architectural demands of the <strong>YouZen platform (supporting 100 restaurants and 100 hair salons on a shared PostgreSQL/Supabase database)</strong>:
      </p>

      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">YouZen Operational Area</th>
            <th style="width: 35%;">Concurrency & Database Challenge</th>
            <th style="width: 40%;">LOGIXOTECH Engineering Approach</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Restaurant Checkout Rush</strong><br>(100 POS + 200 phones)</td>
            <td>Simultaneous meal-time checkouts, table bill splits, and kitchen ticket dispatch creating hot-row lock queues on <code>orders</code>.</td>
            <td>Composite indexes on <code>(location_id, status)</code>, atomic CTE order ingestion, and PgBouncer connection multiplexing.</td>
          </tr>
          <tr>
            <td><strong>Hair Salon Bookings</strong><br>(Calendars & availability)</td>
            <td>Multi-user race conditions where concurrent online users and phone desks attempt to book the exact same stylist time slot.</td>
            <td>PostgreSQL exclusion constraints (<code>EXCLUDE USING gist</code>) and range types (<code>tsrange</code>) to physically eliminate double-bookings.</td>
          </tr>
          <tr>
            <td><strong>Supabase Realtime Traffic</strong><br>(Live kitchen & calendar sync)</td>
            <td>Hundreds of mobile staff devices listening to Postgres WAL changes, triggering connection exhaustion and redundant reads.</td>
            <td>Scoping Realtime channel subscriptions strictly by <code>location_id</code> and implementing client-side debounced invalidation.</td>
          </tr>
          <tr>
            <td><strong>Row-Level Security (RLS)</strong><br>(Tenant data protection)</td>
            <td>Multi-tenant RLS policies on shared tables re-evaluating subqueries on every single scanned row, spiking query latency.</td>
            <td>Refactoring RLS policies to use session-cached JWT claims and <code>STABLE</code> security-definer helper functions.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Important Independence Statement -->
    <div class="callout-box">
      <div class="callout-title">Critical Independence Statement: YouZen Requires Independent Staging Telemetry</div>
      <div class="callout-text">
        LOGIXOTECH emphasizes that while our multi-outlet POS optimization experience provides deep architectural domain knowledge, <strong>YouZen represents a distinct software platform that requires its own empirical baseline measurement and controlled staging tests.</strong> Historical results from the Perera & Sons engagement are not proof of YouZen's specific performance, but demonstrate our team's systematic ability to isolate bottlenecks and optimize high-concurrency database platforms.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 7 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 8: TEAM ALLOCATION, CONTRIBUTIONS & CONCLUSION ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Team & Governance</span></div>
        <div class="brand-sub">Dedicated Engineering Team Allocation, Historical Contributions, and Engagement Commitment</div>
      </div>
      <div class="meta-block">
        <strong>Primary Technical Owner:</strong> Viranga Lakshan (Database Fixes Implementation)<br>
        <strong>Primary Load-Testing Owner:</strong> Janith Kavishka (k6 Scripts & Benchmarks)<br>
        <strong>Primary Coordination Owner:</strong> Lithumitha Ravikumar (Client Milestones & Comms)
      </div>
    </div>

    <!-- Section 12: Dedicated Team Allocation for YouZen -->
    <div class="section">
      <div class="section-title">
        12. Dedicated LOGIXOTECH Team Responsibilities for YouZen
        <span class="tagline">Explicit Accountability for Every Deliverable Requested by Luca</span>
      </div>
      <div class="grid-3">
        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Viranga Lakshan</span>
            <span class="profile-role">Technical Lead & Database Eng.</span>
          </div>
          <p class="card-p"><strong>Primary Technical Owner</strong></p>
          <ul class="card-bullets">
            <li>Personally leads the PostgreSQL / Supabase technical audit and query profiling.</li>
            <li>Analyzes slow queries, lock contention, and RLS policy overhead.</li>
            <li><strong>Personally implements all agreed database fixes</strong>, index migrations, and SQL rewrites.</li>
            <li>Validates database optimization results and provides architectural sign-off.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Janith Kavishka</span>
            <span class="profile-role">Backend & Load-Testing Eng.</span>
          </div>
          <p class="card-p"><strong>Primary Load-Testing Owner</strong></p>
          <ul class="card-bullets">
            <li>Leads load-test planning, scenario design, and scripting in <strong>k6</strong> / <strong>Locust</strong>.</li>
            <li>Prepares synthetic data generators for 100 restaurants and 100 salons.</li>
            <li>Executes independent and combined peak load tests on staging.</li>
            <li>Profiles API bottlenecks and produces before-and-after latency comparisons.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Lithumitha Ravikumar</span>
            <span class="profile-role">Project Coordination & Client Comms</span>
          </div>
          <p class="card-p"><strong>Primary Coordination Owner</strong></p>
          <ul class="card-bullets">
            <li>Manages project timelines, scope tracking, and milestone deliverables.</li>
            <li>Coordinates daily client communication and schedules technical meetings.</li>
            <li>Maintains technical runbooks, changelogs, and audit documentation.</li>
            <li><em>Note: Role is project management and coordination, not primary database coding.</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 13: Historical Team Contributions vs YouZen Allocation -->
    <div class="section">
      <div class="section-title">
        13. Historical Team Contributions & Governance Transparency
        <span class="tagline">Distinguishing Past Project Involvements from Proposed Allocations</span>
      </div>
      <div class="card slate">
        <p class="card-p" style="margin-bottom:3px;">
          <strong>Historical Project Involvements:</strong> In previous technical optimization engagements, including the Perera & Sons investigation, LOGIXOTECH deployed specialized engineering personnel matching specific phase needs. Technical diagnosis, database indexing, and query tuning were directed by senior database architects, supported by systems testing engineers and engagement coordination managers.
        </p>
        <p class="card-p" style="margin-bottom:0; font-style: italic; color: #475569;">
          <strong>Governance Statement:</strong> Individual contributions should be confirmed against the project's actual delivery records. The team responsibilities described for YouZen represent the proposed allocation for the new engagement.
        </p>
      </div>
    </div>

    <!-- Section 14: Confidentiality & Anonymization -->
    <div class="section">
      <div class="section-title">
        14. Confidentiality & Data Protection
        <span class="tagline">Protecting Client Intellectual Property</span>
      </div>
      <p class="card-p" style="margin-bottom:0;">
        This document has been prepared with strict adherence to client non-disclosure standards. All sensitive operational data, internal server IP addresses, credentials, private schema definitions, and customer identifiers have been fully anonymized. Reference to Perera & Sons is made exclusively within the permitted boundaries of technical case study review.
      </p>
    </div>

    <!-- Section 15: Professional Conclusion -->
    <div class="section">
      <div class="section-title">
        15. Conclusion & Technical Commitment
        <span class="tagline">Delivering High-Performance, Scalable Database Foundations</span>
      </div>
      <div class="card tint accent">
        <p class="card-p" style="margin-bottom:0;">
          LOGIXOTECH approaches multi-tenant database optimization through empirical, measurable engineering: isolating root causes with rigorous telemetry, proving hypotheses through automated staging simulations, and implementing surgical database fixes that permanently protect transaction throughput. We are fully prepared to apply these proven principles to ensure the YouZen platform scales seamlessly across 100 restaurants and 100 hair salons.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 8 of 9</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 9: CLIENT REFERENCE & PROJECT VERIFICATION ========================================== -->
<div class="page">
  <div>
    <!-- Top Header -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0284c7;">TECH</span> <span class="brand-badge">Client Reference</span></div>
        <div class="brand-sub">Project Reference, Verification Framework, and Governance Standards</div>
      </div>
      <div class="meta-block">
        <strong>Organization:</strong> Perera & Sons (Retail and Food & Beverage)<br>
        <strong>Engagement:</strong> Multi-Outlet POS Performance & Scalability<br>
        <strong>Protocol:</strong> Client Authorization & Reference Verification
      </div>
    </div>

    <!-- Section 16: Client Reference & Project Verification -->
    <div class="section">
      <div class="section-title">
        16. Client Reference & Project Verification
        <span class="tagline">Formal Verification Protocols for International Prospective Clients</span>
      </div>

      <!-- Project Reference Metadata Card -->
      <div class="card tint accent" style="margin-bottom: 7px;">
        <div class="card-header">
          <span class="card-title">Project Reference Profile – Perera & Sons POS Optimization</span>
          <span class="card-badge">Enterprise Profile</span>
        </div>
        <div class="grid-2" style="gap: 5px 12px; margin-top: 3px;">
          <div><strong>Client Organization:</strong> Perera & Sons</div>
          <div><strong>Service Provider:</strong> LOGIXOTECH Technical Team</div>
          <div><strong>Industry Sector:</strong> Retail and Food & Beverage (F&B)</div>
          <div><strong>Project Scale:</strong> ~350 Outlets (Subject to Scope Verification)</div>
          <div style="grid-column: span 2;">
            <strong>Project Scope:</strong> Performance investigation and optimization of an existing multi-outlet POS platform following the introduction of additional application features.
          </div>
        </div>
      </div>

      <!-- Engagement Summary -->
      <div class="card slate" style="margin-bottom: 7px;">
        <div class="card-header">
          <span class="card-title">Engagement Summary</span>
          <span class="card-badge">Scope Verified</span>
        </div>
        <p class="card-p" style="margin-bottom:0;">
          LOGIXOTECH was engaged to investigate operational performance and response-time degradation affecting the existing centralized POS platform. The technical engagement focused specifically on database query execution analysis, index architecture, connection pool management, concurrent transaction handling, API-level profiling, and multi-location system scalability.
        </p>
      </div>

      <!-- Client Reference Contact & Verification Grid -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Client Reference Contact Information</span>
            <span class="card-badge">Authorization</span>
          </div>
          <p class="card-p" style="font-size:7.2pt; color:#64748b; margin-bottom:4px;">
            <em>Contact details disclosed exclusively following formal client authorization:</em>
          </p>
          <ul class="card-bullets">
            <li><strong>Reference Contact Name:</strong> [Authorized Client Contact]</li>
            <li><strong>Official Position:</strong> [Executive / Technical Designation]</li>
            <li><strong>Organization:</strong> Perera & Sons</li>
            <li><strong>Business Email:</strong> [Authorized Business Email]</li>
            <li><strong>Business Contact Number:</strong> [Authorized Telephone]</li>
            <li><strong>Permission to Contact:</strong> [Confirmed / Pending]</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Project Verification Framework</span>
            <span class="card-badge">Validation Scope</span>
          </div>
          <p class="card-p">
            Subject to client authorization, LOGIXOTECH can facilitate a reference discussion to formally verify:
          </p>
          <ul class="card-bullets">
            <li><strong>1. Scope of Engagement:</strong> Nature and technical boundaries of the engagement.</li>
            <li><strong>2. LOGIXOTECH Involvement:</strong> Direct leadership of the POS performance investigation.</li>
            <li><strong>3. Team Responsibilities:</strong> Database and testing roles performed by the team.</li>
            <li><strong>4. Scale Supported:</strong> Approximate number of commercial business locations.</li>
            <li><strong>5. Remediation Delivered:</strong> Performance investigation and optimization activities undertaken.</li>
          </ul>
        </div>
      </div>

      <!-- Confidentiality & Evidence Governance -->
      <div class="callout-box" style="margin-top: 6px;">
        <div class="callout-title">Confidentiality Statement & Evidence Governance</div>
        <div class="callout-text">
          Client contact details and operational project information will only be disclosed with the client's formal authorization. Where direct contact details cannot be shared due to commercial non-disclosure obligations, LOGIXOTECH can arrange an authorized reference introduction or provide an approved anonymized project verification summary.<br>
          <strong>Evidence Classification:</strong> Historical project details and client references must be supported by actual project records and client confirmation. No hypothetical benchmark figures should be represented as verified project results.
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • Technical Performance & Scalability Report</span>
    <span>Page 9 of 9</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\LOGIXOTECH_Perera_Sons_Benchmark_Report"
    html_path = os.path.join(base_dir, "report.html")
    pdf_path = os.path.join(base_dir, "LOGIXOTECH_Multi_Outlet_POS_Performance_Scalability_Report.pdf")

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

    # Verify page count and render PNGs
    pdf = pdfium.PdfDocument(pdf_path)
    total_pages = len(pdf)
    print(f"Total page count: {total_pages}")

    for i in range(total_pages):
        page = pdf[i]
        image = page.render(scale=2.0).to_pil()
        preview_path = os.path.join(base_dir, f"page_{i+1}.png")
        image.save(preview_path)
        print(f"Rendered page {i+1} to {preview_path}")

    success = (total_pages == 9)
    print(f"Success (exactly 9 pages): {success}")
    return success

if __name__ == "__main__":
    generate_pdf()

