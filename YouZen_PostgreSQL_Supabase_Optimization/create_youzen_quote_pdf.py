import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YouZen - Phase 1 Quotation & Statement of Work</title>
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
    font-size: 8.2pt;
    line-height: 1.35;
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

  /* Minimalist Accent Line */
  .top-accent-line {
    width: 38px;
    height: 3px;
    background: #0f766e;
    border-radius: 2px;
    margin-bottom: 8px;
  }

  /* Header Top */
  .header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1.5px solid #0f766e;
    padding-bottom: 7px;
    margin-bottom: 10px;
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
    margin-top: 1.5px;
  }
  .meta-block {
    text-align: right;
    font-size: 7.6pt;
    color: #64748b;
    line-height: 1.32;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Executive Brief Banner */
  .quote-banner {
    background: #f0fdfa;
    border: 1px solid #ccfbf1;
    border-left: 3.5px solid #0f766e;
    border-radius: 4px;
    padding: 8px 11px;
    margin-bottom: 9px;
  }
  .quote-banner-title {
    font-size: 9.3pt;
    font-weight: 800;
    color: #115e59;
    margin-bottom: 2px;
  }
  .quote-banner-desc {
    font-size: 7.7pt;
    color: #134e4a;
    line-height: 1.32;
    margin: 0;
  }

  /* Section Styling */
  .section {
    margin-bottom: 8.5px;
  }
  .section-title {
    font-size: 9.2pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3px solid #0f766e;
    padding-left: 6.5px;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 0.25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 7.2pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
    letter-spacing: 0;
  }

  /* Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6.5px;
  }

  /* Cards */
  .card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 9px;
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
    margin-bottom: 3.5px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2.5px;
  }
  .card.tint .card-header {
    border-color: #99f6e4;
  }
  .card-title {
    font-size: 8.2pt;
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
    background: #ccfbf1;
    color: #0f766e;
  }
  .card-p {
    font-size: 7.5pt;
    color: #334155;
    margin: 0 0 3.5px 0;
    line-height: 1.3;
  }
  .card-bullets {
    margin: 0;
    padding-left: 12px;
    font-size: 7.3pt;
    color: #475569;
    line-height: 1.28;
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
    font-size: 6.8pt;
    color: #0f766e;
  }

  /* Tables */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.4pt;
    margin-top: 2px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 4px 6.5px;
    font-weight: 700;
    font-size: 7.1pt;
    text-transform: uppercase;
    letter-spacing: 0.25px;
  }
  table.matrix-table td {
    padding: 4px 6.5px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.26;
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
    padding: 5.5px 8.5px;
    margin-top: 4.5px;
  }
  .callout-title {
    font-size: 8pt;
    font-weight: 700;
    color: #115e59;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.4pt;
    color: #134e4a;
    line-height: 1.28;
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
    font-size: 7.2pt;
    color: #0f766e;
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
    color: #0f766e;
    text-decoration: none;
    margin-left: 8px;
    font-weight: 600;
  }
</style>
</head>
<body>

<!-- ========================================== PAGE 1 ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0f766e;">TECH</span> <span class="brand-badge">Commercial Quotation & SOW</span></div>
        <div class="brand-sub">YouZen PostgreSQL & Supabase Concurrency Optimization • Phase 1 Statement of Work</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> Luca & YouZen Technical Team<br>
        <strong>Engagement:</strong> Phase 1 Performance Audit & Load Simulation<br>
        <strong>Technical Lead:</strong> Viranga Lakshan (Lead Solutions Architect)<br>
        <strong>Date:</strong> November 2026
      </div>
    </div>

    <!-- Executive Brief Banner -->
    <div class="quote-banner">
      <div class="quote-banner-title">Phase 1 Fixed-Price Scope of Work & Commercial Quotation</div>
      <p class="quote-banner-desc">
        This document provides the formal fixed-price quotation, delivery timeline, itemized scope confirmation, and team responsibility breakdown for Phase 1 of the YouZen database optimization engagement, supporting 100 concurrent restaurants and 100 hair salons.
      </p>
    </div>

    <!-- Section 1: Commercial Summary -->
    <div class="section">
      <div class="section-title">
        1. Phase 1 Commercial Quotation & Terms
        <span class="tagline">Transparent Fixed-Price Deliverable with Zero Hidden Costs</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 32%;">Engagement Deliverable</th>
            <th style="width: 48%;">Scope Summary & Tooling</th>
            <th style="width: 20%; text-align: right;">Amount (USD)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Phase 1: Full Audit & Staging Simulation</strong></td>
            <td>Baseline telemetry, synthetic data generator (100 venues each), independent & combined peak k6 load tests, lock/booking checks, and comprehensive findings report.</td>
            <td style="text-align: right; color: #0f766e; font-size: 8.5pt;"><strong>$1,000.00</strong></td>
          </tr>
          <tr>
            <td><strong>Additional Infrastructure Costs</strong></td>
            <td>USD 0 under agreed existing staging-environment assumptions. Any required paid Supabase plan upgrades, additional cloud infrastructure or third-party services will be identified and approved by the client before being incurred.</td>
            <td style="text-align: right; color: #059669;"><strong>USD 0.00</strong></td>
          </tr>
          <tr>
            <td><strong>Delivery Timeline</strong></td>
            <td><strong>10 to 14 business days (2 to 3 weeks)</strong>, matching the Phase 1 sprint schedule (Weeks 1–3) in our Technical Proposal.</td>
            <td style="text-align: right;"><strong>Fixed Timeline</strong></td>
          </tr>
          <tr>
            <td><strong>Payment Milestone Structure</strong></td>
            <td>Single milestone funded in Upwork escrow ($1,000) upon kickoff, released upon delivery of verified test scripts and report.</td>
            <td style="text-align: right;"><strong>100% Escrow Protected</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 2: Detailed Phase 1 Inclusions -->
    <div class="section">
      <div class="section-title">
        2. Confirmation of Phase 1 Scope & Technical Inclusions
        <span class="tagline">All Requested Deliverables Fully Included in the $1,000 Fixed Price</span>
      </div>
      <div class="grid-2">
        <div class="card tint">
          <div class="card-header">
            <span class="card-title">1. Baseline Telemetry & Audit</span>
            <span class="card-badge">Telemetry</span>
          </div>
          <p class="card-p">
            Measuring existing query performance, API latencies (p50, p95, p99), connection pooler saturation in PgBouncer, lock wait duration trees, and buffer cache hit rates via <code>pg_stat_statements</code>. Tracing automatic client polling and Supabase Realtime replication overhead.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">2. Synthetic Data Setup</span>
            <span class="card-badge">Staging Harness</span>
          </div>
          <p class="card-p">
            Building an automated, realistic data seeding generator for 100 restaurants (tables, active menus, checks, line items) and 100 hair salons (stylists, working hours, services, booking windows) with multi-tenant relational integrity.
          </p>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">3. Independent App Load Tests</span>
            <span class="card-badge">Isolated Runs</span>
          </div>
          <ul class="card-bullets">
            <li><strong>Restaurant Rush:</strong> 100 checkouts + 200 staff mobile phones concurrently submitting items, printing kitchen tickets, and settling checks.</li>
            <li><strong>Salon Booking Peak:</strong> Multi-column stylist calendar rendering, availability slot lookups, and booking commits.</li>
          </ul>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">4. Combined Peak Concurrency Test</span>
            <span class="card-badge">Peak Stress</span>
          </div>
          <p class="card-p">
            Simultaneously executing the restaurant dinner rush and salon booking peak to measure cross-tenant database CPU spikes, lock queuing, and connection pool exhaustion under joint peak loads.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 2 (Part B): Concurrency Integrity Checks -->
    <div class="section">
      <div class="section-title">
        Concurrency & Business Rule Integrity Verification
        <span class="tagline">Stress-Testing High-Risk Scheduling and POS Workflows</span>
      </div>
      <div class="grid-3">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Conflicting Bookings Test</span>
            <span class="card-badge">Zero Overlaps</span>
          </div>
          <p class="card-p">
            Simulating parallel booking requests attempting to claim the exact same stylist time slot simultaneously to physically verify that race conditions cannot cause double-bookings.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Valid Parallel Bookings</span>
            <span class="card-badge">Throughput</span>
          </div>
          <p class="card-p">
            Verifying that concurrent bookings across different stylists or non-overlapping time windows proceed simultaneously with zero lock blocking or artificial queuing.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Order Idempotency Test</span>
            <span class="card-badge">Zero Duplicates</span>
          </div>
          <p class="card-p">
            Simulating staff mobile phone network retries during dinner rush to verify that duplicate kitchen tickets and redundant check settlements are completely prevented.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • YouZen Quotation & SOW</span>
    <span>Page 1 of 2</span>
    <span class="footer-links">
      <a href="https://viranga-lakshan.github.io/portfolio/">Portfolio</a>
      <a href="https://github.com/viranga-lakshan">GitHub</a>
    </span>
  </div>
</div>

<!-- ========================================== PAGE 2 ========================================== -->
<div class="page">
  <div>
    <div class="top-accent-line"></div>

    <!-- Header Top -->
    <div class="header-top">
      <div>
        <div class="brand-title">LOGIXO<span style="color:#0f766e;">TECH</span> <span class="brand-badge">Phase 2, Team & Reference</span></div>
        <div class="brand-sub">Deliverables Handover, Phase 2 Framework, Personal Accountability & Case Study</div>
      </div>
      <div class="meta-block">
        <strong>Phase 2 Range:</strong> $1,500 – $2,500 USD (Indicative)<br>
        <strong>Technical Owner:</strong> Viranga Lakshan (Fixes Implementation)<br>
        <strong>Evidence Base:</strong> 400+ Sites (MFCS) • 350 POS Outlets (P&S)
      </div>
    </div>

    <!-- Section 2 Continued: Handover Artifacts -->
    <div class="section">
      <div class="section-title">
        Phase 1 Final Handover Deliverables
        <span class="tagline">What YouZen Receives at the Conclusion of Phase 1</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Reusable Test Scripts in Git</span>
            <span class="card-badge">Code Asset</span>
          </div>
          <p class="card-p">
            Complete, parameterized <strong>k6</strong> (JavaScript/TypeScript) load scripts handed over in your repository with synthetic seeders and a clean README, allowing your team to re-run automated benchmarks on demand.
          </p>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Empirical Audit Report & Roadmap</span>
            <span class="card-badge">Technical Report</span>
          </div>
          <p class="card-p">
            A comprehensive findings report documenting baseline vs. peak latency percentiles (p50, p95, p99), requests per second (RPS), connection curves, and a prioritized, actionable backlog of fixes for Phase 2.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 3: Phase 2 Indicative Rates -->
    <div class="section">
      <div class="section-title">
        3. Phase 2 Indicative Commercial Framework
        <span class="tagline">Remediation Implementation & Benchmark Re-Verification</span>
      </div>
      <div class="card tint">
        <div class="card-header">
          <span class="card-title">Phase 2 Budget & Scope Governance</span>
          <span class="card-badge">Capped Fixed Price</span>
        </div>
        <div class="grid-2" style="margin-top:2px;">
          <div>
            <p class="card-p">
              <strong>Indicative Fixed-Price Range:</strong> <strong>$1,500 – $2,500 USD</strong><br>
              <strong>Pricing Basis:</strong> Estimated from 30–50 hours at our standard senior engineering rate ($45–$50/hr), delivered strictly as a capped fixed-price milestone for complete cost certainty.<br>
              <strong>Estimated Timeline:</strong> <strong>2 to 3 weeks (Weeks 4–6)</strong>, matching Phase 2 in our Technical Proposal.
            </p>
          </div>
          <div>
            <p class="card-p">
              <strong>Scope & Governance:</strong> Implementing prioritized composite indexes, query rewrites, RLS policy refactoring, concurrency guards, and Realtime channel scoping, followed by a complete re-run of the k6 benchmark suite. The final milestone budget will be agreed after reviewing the Phase 1 audit.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 4: Personal Accountability & Team Roles -->
    <div class="section">
      <div class="section-title">
        4. Dedicated Personal Responsibilities
        <span class="tagline">Explicit Accountability for Every Task</span>
      </div>
      <div class="grid-3">
        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Viranga Lakshan</span>
            <span class="profile-role">Technical Lead</span>
          </div>
          <p class="card-p"><strong>Primary Technical Owner</strong></p>
          <ul class="card-bullets">
            <li>Personally leads the PostgreSQL and Supabase audit.</li>
            <li>Investigates queries, indexes, locks, and connection pools.</li>
            <li><strong>Personally implements agreed database fixes and optimizations.</strong></li>
            <li>Leads database architecture decisions and technical sign-off.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Janith Kavishka</span>
            <span class="profile-role">Backend/API & Load-Testing Eng.</span>
          </div>
          <p class="card-p"><strong>Primary Load-Testing Owner</strong></p>
          <ul class="card-bullets">
            <li>Leads load-test planning and execution.</li>
            <li>Develops k6 and Locust test scripts.</li>
            <li>Generates synthetic test data for 100 restaurants and 100 salons.</li>
            <li>Executes tests against staging and supports API investigation.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Lithumitha Ravikumar</span>
            <span class="profile-role">Project Coordination</span>
          </div>
          <p class="card-p"><strong>Primary Coordination Owner</strong></p>
          <ul class="card-bullets">
            <li>Coordinates project requirements, timelines, and milestones.</li>
            <li>Manages client communication and status reporting.</li>
            <li>Prepares documentation and test deliverables; tracks progress.</li>
            <li><em>Primary role is project management and coordination, not primary database engineering.</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 5: Enterprise Track Record & Case Study Evidence -->
    <div class="section">
      <div class="section-title">
        5. Enterprise Case Studies & Evidence (Full Details in Proposal)
        <span class="tagline">Proven High-Concurrency Architectures Supporting Millions of Daily Transactions</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Case Study 01: Mobile Field Platform (MFCS)</span>
            <span class="card-badge">1M+ Daily Receipts</span>
          </div>
          <p class="card-p">
            High-concurrency mobile settlement network across <strong>400+ nationwide sites</strong> (Singer retail platform) processing <strong>10+ Lakhs (1,000,000+) receipts daily</strong>:
          </p>
          <ul class="card-bullets">
            <li><strong>0.00% Record Loss:</strong> Strict ACID boundaries with zero lost payments.</li>
            <li><strong>0 Database Locks / Deadlocks:</strong> Wait times dropped from 1,450ms to 45ms.</li>
            <li><strong>p95 End-of-Day Sync Latency:</strong> Dropped from <strong>3,200 ms to 480 ms</strong> (-85.0%).</li>
            <li><strong>Database CPU Load:</strong> Slashed from <strong>92% to 38%</strong> during peak upload rush.</li>
          </ul>
        </div>

        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Case Study 02: Multi-Outlet Retail POS</span>
            <span class="card-badge">350 Outlets • 1,050 Devices</span>
          </div>
          <p class="card-p">
            Enterprise multi-outlet POS platform (Perera & Sons) supporting <strong>350 commercial outlets and 1,050 active devices</strong> on shared database:
          </p>
          <ul class="card-bullets">
            <li><strong>p95 API Latency:</strong> Reduced from <strong>920 ms to 420 ms</strong> (-54.3%).</li>
            <li><strong>Query Response Time:</strong> Slashed from <strong>450 ms to 120 ms</strong> (-73.3%).</li>
            <li><strong>Database CPU Load:</strong> Dropped from <strong>85% to 45%</strong> during peak meal rush.</li>
            <li><strong>Connection Pool Efficiency:</strong> Capped connections from <strong>450 to 250</strong>.</li>
          </ul>
        </div>
      </div>
      <div class="callout-box" style="margin-top: 3.5px; padding: 4px 7.5px;">
        <div class="callout-title" style="font-size: 7.4pt; margin-bottom: 1px;">Immediate Kickoff & Reference Verification Protocol</div>
        <div class="callout-text" style="font-size: 7pt; line-height: 1.2;">
          <strong>Ready to Start:</strong> Phase 1 starts immediately upon Upwork milestone funding ($1,000) and staging database access. <em>Client reference introductions may be arranged subject to client authorization and availability. See our comprehensive 11-page master proposal (YouZen_Database_Optimization_Proposal2.pdf) for complete architectural schematics and k6 benchmarking blueprints.</em>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>LOGIXOTECH Engineering • YouZen Quotation & SOW</span>
    <span>Page 2 of 2</span>
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
    html_path = os.path.join(base_dir, "quote.html")
    pdf_path = os.path.join(base_dir, "YouZen_Phase1_Quotation_and_Statement_of_Work.pdf")

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
        preview_path = os.path.join(base_dir, f"quote_page_{i+1}.png")
        image.save(preview_path)
        print(f"Rendered page {i+1} to {preview_path}")

    success = (total_pages == 2)
    print(f"Success (exactly 2 pages): {success}")
    return success

if __name__ == "__main__":
    generate_pdf()

