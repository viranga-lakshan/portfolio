import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PostgreSQL & Supabase Optimization - Technical Proposal</title>
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
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 8.4pt;
    line-height: 1.38;
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

  /* Minimalist Top Accent Bar */
  .top-accent-bar {
    width: 38px;
    height: 3px;
    background: #0f766e;
    border-radius: 2px;
    margin-bottom: 10px;
  }

  /* Header Top */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 9px;
    margin-bottom: 11px;
  }
  .brand-title {
    font-size: 14pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    margin-bottom: 2px;
  }
  .brand-sub {
    font-size: 8.5pt;
    color: #0f766e;
    font-weight: 600;
    letter-spacing: 0.2px;
  }
  .meta-block {
    text-align: right;
    font-size: 7.8pt;
    color: #64748b;
    line-height: 1.35;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Executive Brief Banner */
  .brief-banner {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #0f766e;
    border-radius: 4px;
    padding: 9px 12px;
    margin-bottom: 10px;
  }
  .brief-title {
    font-size: 9.8pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 3px;
  }
  .brief-desc {
    font-size: 8pt;
    color: #475569;
    line-height: 1.36;
    margin: 0;
  }

  /* Section Styling */
  .section {
    margin-bottom: 9.5px;
  }
  .section-title {
    font-size: 9.6pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3px solid #0f766e;
    padding-left: 7px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 7.5pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
  }

  /* Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 7px;
  }

  /* Cards */
  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 8px 10px;
  }
  .card.tint {
    background: #f0fdfa;
    border-color: #ccfbf1;
  }
  .card.slate {
    background: #f8fafc;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 3px;
  }
  .card.tint .card-header {
    border-color: #99f6e4;
  }
  .card-title {
    font-size: 8.5pt;
    font-weight: 700;
    color: #0f172a;
  }
  .card-badge {
    font-size: 6.8pt;
    font-weight: 700;
    padding: 1.5px 5.5px;
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
    font-size: 7.7pt;
    color: #334155;
    margin: 0 0 4px 0;
    line-height: 1.33;
  }
  .card-bullets {
    margin: 0;
    padding-left: 13px;
    font-size: 7.5pt;
    color: #475569;
    line-height: 1.32;
  }
  .card-bullets li {
    margin-bottom: 2px;
  }
  .card-bullets strong, .card-p strong {
    color: #0f172a;
  }
  code {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 0.5px 3.5px;
    border-radius: 3px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 7pt;
    color: #0f766e;
  }

  /* Architectural Visual Pipeline */
  .arch-pipeline {
    display: flex;
    align-items: stretch;
    gap: 7px;
    margin-top: 3px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 8px;
  }
  .arch-box {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 9px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .arch-box.highlight {
    border-top: 3px solid #0f766e;
    flex: 1.25;
  }
  .arch-badge {
    display: inline-block;
    font-size: 6.7pt;
    font-weight: 700;
    color: #0f766e;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 2px;
  }
  .arch-title {
    font-size: 8.3pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 3px;
  }
  .arch-desc {
    font-size: 7.4pt;
    color: #475569;
    line-height: 1.3;
    margin: 0;
  }
  .arch-bullets {
    margin: 0;
    padding-left: 12px;
    font-size: 7.2pt;
    color: #334155;
    line-height: 1.28;
  }
  .arch-bullets li {
    margin-bottom: 1.5px;
  }
  .arch-arrow {
    display: flex;
    align-items: center;
    color: #94a3b8;
    font-size: 11pt;
    font-weight: 700;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.6pt;
    margin-top: 2px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 4.5px 7px;
    font-weight: 700;
    font-size: 7.3pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  table.matrix-table td {
    padding: 4.5px 7px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.3;
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
    padding: 6px 9px;
    margin-top: 5px;
  }
  .callout-title {
    font-size: 8.2pt;
    font-weight: 700;
    color: #115e59;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.6pt;
    color: #134e4a;
    line-height: 1.32;
  }

  /* Profile Box */
  .profile-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 9px;
  }
  .profile-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2.5px;
  }
  .profile-name {
    font-size: 8.7pt;
    font-weight: 800;
    color: #0f172a;
  }
  .profile-role {
    font-size: 7.5pt;
    color: #0f766e;
    font-weight: 600;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #0f766e;
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
    <div class="top-accent-bar"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">Database Performance & Concurrency Proposal</div>
        <div class="brand-sub">PostgreSQL / Supabase / Next.js Multi-Tenant Optimization for YouZen</div>
      </div>
      <div class="meta-block">
        <strong>Target Envelope:</strong> 100 Restaurants + 100 Hair Salons<br>
        <strong>Focus:</strong> Query, Index, Lock & Realtime Optimization<br>
        <strong>Lead Engineer:</strong> Viranga Lakshan (Solutions Architect)<br>
        <strong>Model:</strong> Two-Phase Staging Simulation & Remediation
      </div>
    </div>

    <!-- Executive Brief Banner -->
    <div class="brief-banner">
      <div class="brief-title">Engineering YouZen for Peak Concurrency Without Latency Spikes</div>
      <p class="brief-desc">
        A production-focused database engineering proposal designed to benchmark, stress-test, and optimize YouZen's shared PostgreSQL and Supabase platform. Engineered to support 100 concurrent restaurants (100 checkouts + 200 staff mobile phones during dinner rush) and 100 hair salons (calendars, slot searches, and online bookings) under isolated and combined peak loads.
      </p>
    </div>

    <!-- Section 1: The Concurrency Challenge -->
    <div class="section">
      <div class="section-title">
        1. Target Workload & Concurrency Profile
        <span class="tagline">Understanding the Peak Demands of Both Applications</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">100 Restaurants Workload</span>
            <span class="card-badge">Dinner Rush</span>
          </div>
          <p class="card-p">
            High-frequency transaction writes, frequent state transitions, and real-time kitchen status broadcasting:
          </p>
          <ul class="card-bullets">
            <li><strong>Device Footprint:</strong> 100 dedicated checkout terminals + 200 active floor staff mobile phones.</li>
            <li><strong>Hot Transaction Paths:</strong> Live order item additions, kitchen ticket printing/routing, takeaway order submissions, and table check settlements.</li>
            <li><strong>Concurrency Hazards:</strong> Lock contention on shared order rows, duplicate ticket generation, and high-frequency auto-refresh loops.</li>
          </ul>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">100 Hair Salons Workload</span>
            <span class="card-badge">Booking Peak</span>
          </div>
          <p class="card-p">
            Intensive range queries, appointment slot evaluations, and multi-user schedule coordination:
          </p>
          <ul class="card-bullets">
            <li><strong>User Activity:</strong> Staff managing multi-column stylist calendars; clients running real-time availability searches online.</li>
            <li><strong>Hot Transaction Paths:</strong> Overlapping slot lookups, calendar grid rendering, and atomic appointment bookings across multiple staff.</li>
            <li><strong>Concurrency Hazards:</strong> Double-booking race conditions during simultaneous booking attempts, and heavy unindexed range scans on stylist schedules.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 2: What We Investigate First -->
    <div class="section">
      <div class="section-title">
        2. Immediate Technical Investigation Priorities
        <span class="tagline">Isolating Systemic Bottlenecks Before Changing Code or Schemas</span>
      </div>
      <div class="grid-3">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Realtime & Polling Storms</span>
            <span class="card-badge">Priority 1</span>
          </div>
          <p class="card-p">
            Investigating Supabase Realtime channel subscriptions and Next.js client-side refresh intervals. 200 staff phones querying for order updates can quickly saturate database CPU and generate thousands of duplicate WAL read events.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Lock Waits & Race Conditions</span>
            <span class="card-badge">Priority 2</span>
          </div>
          <p class="card-p">
            Profiling <code>pg_locks</code> and transaction isolation levels. Verifying whether concurrent checks and appointment writes cause cascading lock waits or deadlocks, and implementing <code>FOR UPDATE SKIP LOCKED</code> where appropriate.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Row-Level Security (RLS) Cost</span>
            <span class="card-badge">Priority 3</span>
          </div>
          <p class="card-p">
            Auditing tenant isolation policies on location-scoped tables. RLS subqueries that join user permission tables re-evaluate on every row unless wrapped in <code>STABLE</code> functions or cached JWT claims.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 3: Similar Project Benchmark -->
    <div class="section">
      <div class="section-title">
        3. Relevant Production Experience & Measurable Results
        <span class="tagline">Proven Optimization on PostgreSQL & Supabase Stacks</span>
      </div>
      <div class="card">
        <div class="card-header">
          <span class="card-title">Case Study: Multi-Outlet POS Platform Architecture</span>
          <span class="card-badge">Technical Benchmark</span>
        </div>
        <p class="card-p">
          Demonstrated architecture modeling for <strong>350 Business Locations – Illustrative Scalability Scenario (1,050 Simulated Active Devices)</strong> running POS terminals and reservation services:
        </p>
        <ul class="card-bullets">
          <li><strong>API Latency (p95):</strong> Lowered p95 response time from <strong>920 ms to 420 ms</strong> (-54.3%) under simulated peak checkout rush.</li>
          <li><strong>Database Query Latency:</strong> Slashed query response time from <strong>450 ms to 120 ms</strong> (-73.3%) through composite indexing.</li>
          <li><strong>Database CPU Load:</strong> Dropped CPU utilization from <strong>85% to 45%</strong> by eliminating table scans and pooling connections.</li>
          <li><strong>Connection Multiplexing:</strong> Pooled peak connections from <strong>450 to 250</strong> via PgBouncer transaction-mode connection pooling.</li>
        </ul>
        <div style="margin-top: 3px; font-size: 6.5pt; color: #64748b; font-style: italic; line-height: 1.2;">
          These figures are illustrative examples for a hypothetical performance optimization scenario. They are not verified historical measurements from the Perera & Sons POS project or LOGIXOTECH production testing.
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>YouZen Database Optimization Proposal • PostgreSQL / Supabase / Next.js</span>
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
    <div class="top-accent-bar"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">System Architecture & Concurrency Model</div>
        <div class="brand-sub">Traffic Routing, Data Access Layers, and Shared PostgreSQL Tenant Isolation</div>
      </div>
      <div class="meta-block">
        <strong>Data Access:</strong> Next.js Server & Supabase Data API<br>
        <strong>Replication:</strong> Supabase Realtime Change Broadcasts<br>
        <strong>Security:</strong> Row-Level Policies (RLS) Scoped to Location
      </div>
    </div>

    <!-- Section 4: Architectural Data Flow Diagram -->
    <div class="section">
      <div class="section-title">
        4. Application Traffic & Data Flow Topology
        <span class="tagline">Mapping High-Volume Touchpoints Across the Platform</span>
      </div>

      <div class="arch-pipeline">
        <div class="arch-box">
          <div>
            <span class="arch-badge">Layer 01: Client Traffic</span>
            <div class="arch-title">Application Clients</div>
            <p class="arch-desc">
              <strong>Restaurants:</strong> 100 checkout screens, kitchen display units, staff mobile phones, online takeaway.<br><br>
              <strong>Hair Salons:</strong> Stylist calendar views, phone booking desks, client-facing booking widgets.
            </p>
          </div>
        </div>

        <div class="arch-arrow">➔</div>

        <div class="arch-box highlight">
          <div>
            <span class="arch-badge">Layer 02: Access Layer</span>
            <div class="arch-title">Next.js & Supabase API</div>
            <ul class="arch-bullets">
              <li><strong>Server Requests:</strong> Scoped database functions & Next.js server actions.</li>
              <li><strong>Direct API Calls:</strong> Staff phones listening for changes directly through API.</li>
              <li><strong>Realtime Layer:</strong> WAL broadcasts to subscribed active screens.</li>
              <li><strong>Scheduled Workers:</strong> Cron jobs for background reconciliations.</li>
            </ul>
          </div>
        </div>

        <div class="arch-arrow">➔</div>

        <div class="arch-box">
          <div>
            <span class="arch-badge">Layer 03: Data Store</span>
            <div class="arch-title">PostgreSQL on Supabase</div>
            <p class="arch-desc">
              Shared relational cluster. Tenant records scoped by <code>location_id</code>.<br><br>
              Strict Row-Level Security (RLS) protecting multi-tenant tables, backed by PgBouncer transaction pooling.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 5: Data Models Deep Dive -->
    <div class="section">
      <div class="section-title">
        5. Concurrency & Domain Data Models
        <span class="tagline">Analyzing Hot Paths Across Restaurant and Salon Domains</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Restaurant Domain Models</span>
            <span class="card-badge">High-Write Volume</span>
          </div>
          <p class="card-p">
            Entities subject to continuous status updates, additions, and payment bindings:
          </p>
          <ul class="card-bullets">
            <li><strong>Takeaway Orders:</strong> High volume of concurrent inserts into <code>orders</code> and linked <code>order_line_items</code>.</li>
            <li><strong>Dining Room Tables:</strong> Real-time reservation status and table occupancy tracking linked to physical tables.</li>
            <li><strong>Table Checks & Sales:</strong> Active checks containing <code>ticket_items</code>, requiring atomic sales transactions linked to payment records.</li>
            <li><strong>Optimization Focus:</strong> Indexing foreign keys, preventing row-level deadlocks during table transfers, and avoiding full table locks on payment commits.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Hair Salon Domain Models</span>
            <span class="card-badge">Intensive Range Scans</span>
          </div>
          <p class="card-p">
            Entities defined by temporal constraints, stylist availability, and calendar rules:
          </p>
          <ul class="card-bullets">
            <li><strong>Appointments:</strong> Booked services linked to stylists and clients. High sensitivity to double-booking anomalies.</li>
            <li><strong>Service Catalog:</strong> Configurable service durations, buffer times, and stylist skill associations.</li>
            <li><strong>Scheduling Rules:</strong> Working hours, breaks, holidays, and temporary closures defining available booking windows.</li>
            <li><strong>Optimization Focus:</strong> Range index optimization (GiST / B-tree) for overlap checks (<code>tsrange</code>) and atomic slot locking.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 6: Preventing Concurrency Failures -->
    <div class="section">
      <div class="section-title">
        6. Safeguarding Business Rules Under Peak Concurrency
        <span class="tagline">Ensuring Zero Data Inconsistencies or Workflow Violations</span>
      </div>
      <div class="grid-3">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">No Double Bookings</span>
            <span class="card-badge">Integrity</span>
          </div>
          <p class="card-p">
            Utilizing PostgreSQL exclusion constraints (<code>EXCLUDE USING gist</code>) or short-lived advisory locks during checkout to guarantee that two simultaneous bookings cannot reserve the same stylist slot.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">No Duplicate Tickets</span>
            <span class="card-badge">Idempotency</span>
          </div>
          <p class="card-p">
            Enforcing client-generated idempotency keys and atomic upserts on orders to prevent staff phones from generating duplicate kitchen tickets during transient connection retries.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Fast Floor Checkouts</span>
            <span class="card-badge">Throughput</span>
          </div>
          <p class="card-p">
            Isolating payment reconciliation writes from real-time ticket display reads, ensuring checkout screens never experience UI freezes during peak dinner ordering rushes.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>YouZen Database Optimization Proposal • PostgreSQL / Supabase / Next.js</span>
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
    <div class="top-accent-bar"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">Step-by-Step Optimization Methodology</div>
        <div class="brand-sub">Two-Phase Execution Plan: Telemetry, Synthetic Staging Testing, and Fix Verification</div>
      </div>
      <div class="meta-block">
        <strong>Phase 1:</strong> Audit, Telemetry & Staging Simulation<br>
        <strong>Phase 2:</strong> Remediation, Fixes & Verification<br>
        <strong>Tooling:</strong> k6, pg_stat_statements, PgBouncer, EXPLAIN ANALYZE
      </div>
    </div>

    <!-- Section 7: Detailed Phase 1 Plan -->
    <div class="section">
      <div class="section-title">
        7. Phase 1: Baseline Audit & Synthetic Staging Load Testing
        <span class="tagline">Weeks 1–2: Quantifying Current Limits and Replicating Peak Failure Modes</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Step 1.1: Telemetry & Baseline Metrics</span>
            <span class="card-badge">Telemetry</span>
          </div>
          <p class="card-p">
            We establish granular baseline metrics on current database and API performance:
          </p>
          <ul class="card-bullets">
            <li><strong>pg_stat_statements:</strong> Query frequency, total runtime, mean exec time, and buffer cache misses.</li>
            <li><strong>Lock Contention:</strong> Profiling transaction wait times, blocked queries, and deadlocks.</li>
            <li><strong>Connection Utilization:</strong> Monitoring active, idle, and waiting connection pools in PgBouncer.</li>
            <li><strong>Traffic Profiling:</strong> Tracing automatic page refreshes and Supabase Realtime broadcast payloads.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Step 1.2: Synthetic Data & Peak Simulation</span>
            <span class="card-badge">Staging Harness</span>
          </div>
          <p class="card-p">
            We build automated, repeatable load-testing scripts (using k6 / Locust):
          </p>
          <ul class="card-bullets">
            <li><strong>Synthetic Data Generation:</strong> Seeding staging with 100 realistic restaurants and 100 hair salons with full relational history.</li>
            <li><strong>Scenario A (Restaurants):</strong> Simulating 100 checkouts + 200 staff mobile phones during a dinner rush.</li>
            <li><strong>Scenario B (Salons):</strong> Simulating active calendar views, availability lookups, and concurrent bookings.</li>
            <li><strong>Scenario C (Combined Peak):</strong> Running both workloads simultaneously to surface cross-tenant resource contention.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 8: Detailed Phase 2 Plan -->
    <div class="section">
      <div class="section-title">
        8. Phase 2: Fix Implementation & Remediation
        <span class="tagline">Weeks 3–4: Deploying Targeted Fixes and Re-Verifying Under Peak Load</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Step 2.1: Query, Index & Lock Tuning</span>
            <span class="card-badge">Engine Tuning</span>
          </div>
          <p class="card-p">
            Applying targeted database optimizations based on empirical trace data:
          </p>
          <ul class="card-bullets">
            <li><strong>Strategic Indexing:</strong> Composite indexes for multi-column filters, partial indexes for active checks and upcoming bookings, and covering indexes for foreign keys.</li>
            <li><strong>RLS Refactoring:</strong> Converting slow dynamic table joins in Row-Level Security policies into cached JWT claims and <code>STABLE</code> security-definer functions.</li>
            <li><strong>Lock Optimization:</strong> Restructuring updates on <code>orders</code> and <code>appointments</code> to eliminate blocking locks and prevent deadlocks.</li>
            <li><strong>Connection Pooling:</strong> Fine-tuning PgBouncer transaction-mode settings and client connection budgets.</li>
          </ul>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Step 2.2: Application & Realtime Triage</span>
            <span class="card-badge">Next.js & API</span>
          </div>
          <p class="card-p">
            Refining the data access layer in Next.js and Supabase Realtime:
          </p>
          <ul class="card-bullets">
            <li><strong>Channel Scoping:</strong> Filtering Realtime subscriptions by <code>location_id</code> so clients only receive events for their venue.</li>
            <li><strong>Debouncing & Batching:</strong> Replacing aggressive client polling on staff phones with debounced invalidations and batched state syncs.</li>
            <li><strong>Selective Fetching:</strong> Replacing over-fetching queries with minimal column projections to reduce serialization overhead.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 9: Verification Step -->
    <div class="section">
      <div class="section-title">
        9. Step 2.3: Re-Verification & Comparative Benchmarking
        <span class="tagline">Proving Measurable Gains Under Identical Staging Conditions</span>
      </div>
      <div class="card slate">
        <div class="card-header">
          <span class="card-title">Objective Verification Protocol</span>
          <span class="card-badge">Definitive Proof</span>
        </div>
        <p class="card-p">
          We re-execute the identical k6 load scripts against the optimized database under the exact same simulated dinner rush and salon booking peak workloads. We verify that:
        </p>
        <ul class="card-bullets">
          <li>Response times for checkouts, kitchen ticket submissions, and slot bookings drop significantly across p50, p95, and p99 percentiles.</li>
          <li>Peak connection counts remain stable within PgBouncer limits with zero connection pool timeouts.</li>
          <li>Zero missing or duplicate orders, and all competing booking requests strictly adhere to salon availability rules.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>YouZen Database Optimization Proposal • PostgreSQL / Supabase / Next.js</span>
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
    <div class="top-accent-bar"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">Deliverables, Handover & Engineering Team</div>
        <div class="brand-sub">Comprehensive Test Harness Handover, Capacity Guidance, and Team Credentials</div>
      </div>
      <div class="meta-block">
        <strong>Engagement:</strong> Remote Technical Specialist<br>
        <strong>Availability:</strong> Immediate Kickoff (Within 24–48 Hours)<br>
        <strong>Timeline:</strong> 2 Weeks Phase 1 + 2 Weeks Phase 2
      </div>
    </div>

    <!-- Section 10: Deliverables Matrix -->
    <div class="section">
      <div class="section-title">
        10. Concrete Handover Deliverables
        <span class="tagline">What YouZen Receives at the Conclusion of the Engagement</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">Deliverable</th>
            <th style="width: 45%;">Description & Contents</th>
            <th style="width: 30%;">Format</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Automated Test Suite</strong></td>
            <td>Repeatable, parameterized k6 / Locust load scripts simulating 100 restaurants, 100 salons, and combined peak workloads with synthetic data seeding utilities.</td>
            <td>Git repository, CLI scripts, and README execution guide.</td>
          </tr>
          <tr>
            <td><strong>Before/After Benchmark Report</strong></td>
            <td>Comprehensive empirical comparison of query response times (p50, p95, p99), request throughput (RPS), peak connection count, lock wait times, and error rates.</td>
            <td>Structured Technical Report (PDF / Markdown) with graphs.</td>
          </tr>
          <tr>
            <td><strong>Database & RLS Fixes</strong></td>
            <td>All SQL migration scripts for indexes, constraints, rewritten views, optimized RLS policies, and Next.js / Realtime connection code enhancements.</td>
            <td>Versioned Supabase SQL migration files and Git PRs.</td>
          </tr>
          <tr>
            <td><strong>Capacity & Rollout Runbook</strong></td>
            <td>Long-term platform capacity assessment, recommended compute tier thresholds, production zero-downtime rollout plan, and alerting triggers.</td>
            <td>Operational Runbook & Monitoring Thresholds document.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 11: Dedicated Engineering Team -->
    <div class="section">
      <div class="section-title">
        11. Dedicated Senior Engineering Team
        <span class="tagline">Full Resumes Attached in Proposal Package</span>
      </div>
      <div class="grid-3">
        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Viranga Lakshan</span>
            <span class="profile-role">Technical Lead</span>
          </div>
          <p class="card-p">
            <strong>Role for YouZen:</strong> Primary technical lead. Personally leads the PostgreSQL and Supabase audit; investigates queries, indexes, locks, and connection pools; personally implements agreed database fixes and optimizations; leads architecture decisions.
          </p>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Janith Kavishka</span>
            <span class="profile-role">Backend/API & Load-Testing Eng.</span>
          </div>
          <p class="card-p">
            <strong>Role for YouZen:</strong> Primary load-testing owner. Leads load-test planning and execution; develops k6 and Locust test scripts; generates synthetic test data for 100 restaurants and 100 salons; executes tests against staging.
          </p>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Lithumitha Ravikumar</span>
            <span class="profile-role">Project Coordination</span>
          </div>
          <p class="card-p">
            <strong>Role for YouZen:</strong> Coordinates project requirements, timelines, and milestones; manages client communication and status reporting; tracks progress. <em>Primary role is project management and coordination, not primary database engineering.</em>
          </p>
        </div>
      </div>
    </div>

    <!-- Section 12: Next Steps & Immediate Kickoff -->
    <div class="callout-box">
      <div class="callout-title">Immediate Kickoff & Collaboration Plan</div>
      <div class="callout-text">
        We are prepared to begin immediately upon selection. Our first step is a 30-minute technical kickoff call with Luca and the engineering team to review repository access, staging database provisioning, and telemetry capture tools. Phase 1 findings and the initial staging test harness will be delivered within 10 business days (approximately two weeks).
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>YouZen Database Optimization Proposal • PostgreSQL / Supabase / Next.js</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\YouZen_PostgreSQL_Supabase_Optimization"
    html_path = os.path.join(base_dir, "proposal.html")
    pdf_path = os.path.join(base_dir, "YouZen_PostgreSQL_Supabase_Optimization_Proposal.pdf")

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

    success = (total_pages == 4)
    print(f"Success: {success}")
    return success

if __name__ == "__main__":
    generate_pdf()

