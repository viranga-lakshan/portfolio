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
            <td>Utilizes existing Supabase staging project. Load tests executed via open-source k6 / Locust runners with zero software licensing costs.</td>
            <td style="text-align: right; color: #059669;"><strong>$0.00</strong></td>
          </tr>
          <tr>
            <td><strong>Delivery Timeline</strong></td>
            <td><strong>7 to 10 business days</strong> from receipt of repository access and staging database credentials.</td>
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
        <strong>Case Study:</strong> Perera & Sons POS (~350 Outlets Verified)
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
          <span class="card-badge">Flexible Scope</span>
        </div>
        <div class="grid-2" style="margin-top:2px;">
          <div>
            <p class="card-p">
              <strong>Indicative Fixed-Price Range:</strong> <strong>$1,500 – $2,500 USD</strong><br>
              <strong>Standard Senior Engineering Rate:</strong> <strong>$45 – $50 / hour</strong><br>
              <strong>Scope of Work:</strong> Implementing prioritized composite indexes, query rewrites, RLS policy refactoring, concurrency guards, and Realtime channel scoping, followed by a complete re-run of the k6 benchmark suite.
            </p>
          </div>
          <div>
            <p class="card-p">
              <strong>Collaborative Agreement:</strong> The exact milestone budget and delivery timeline for Phase 2 will be established collaboratively after reviewing the Phase 1 audit report together, ensuring you only pay for verified, high-impact fixes.
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
            <span class="profile-role">Technical Lead & Database Eng.</span>
          </div>
          <p class="card-p"><strong>Primary Technical Owner</strong></p>
          <ul class="card-bullets">
            <li>Personally leads the PostgreSQL / Supabase audit and slow query profiling.</li>
            <li>Audits table lock trees, connection pooling limits, and RLS policy overhead.</li>
            <li><strong>Personally implements all agreed database fixes</strong>, index migrations, and SQL rewrites in Phase 2.</li>
            <li>Signs off on final database architecture and benchmark verification.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Janith Kavishka</span>
            <span class="profile-role">Backend/API & Load-Testing Eng.</span>
          </div>
          <p class="card-p"><strong>Primary Load-Testing Owner</strong></p>
          <ul class="card-bullets">
            <li>Personally develops reusable k6 / Locust load scripts and synthetic data generators.</li>
            <li>Executes independent and combined peak load tests on staging.</li>
            <li>Profiles API bottlenecks, serialization overhead, and Realtime subscription traffic.</li>
            <li>Generates latency percentiles (p50, p95, p99) and connection saturation graphs.</li>
          </ul>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Lithumitha Ravikumar</span>
            <span class="profile-role">Project Coordination & Client Comms</span>
          </div>
          <p class="card-p"><strong>Primary Coordination Owner</strong></p>
          <ul class="card-bullets">
            <li>Manages delivery timelines, milestone tracking, and daily Slack/Teams communication.</li>
            <li>Coordinates technical syncs, meeting agendas, and changelog/documentation QA.</li>
            <li><em>Note: Role is dedicated project management and coordination, not primary database coding.</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 5: Case Study Reference & Immediate Kickoff -->
    <div class="section">
      <div class="section-title">
        5. Verified Case Study Evidence & Immediate Kickoff
        <span class="tagline">Proven Multi-Outlet POS Optimization (~350 Locations)</span>
      </div>
      <div class="grid-2">
        <div class="card slate">
          <div class="card-header">
            <span class="card-title">Supporting 9-Page Case Study Attached</span>
            <span class="card-badge">Perera & Sons</span>
          </div>
          <p class="card-p">
            Attached is our report <code>LOGIXOTECH_Multi_Outlet_POS_Performance_Scalability_Report.pdf</code> documenting our verified engagement on the Perera & Sons platform across <strong>~350 outlets and 1,050 active devices</strong>:
          </p>
          <ul class="card-bullets">
            <li>API p95 latency reduced from <strong>920 ms to 420 ms</strong> (-54.3%).</li>
            <li>Query response time dropped from <strong>450 ms to 120 ms</strong> (-73.3%).</li>
            <li>Database CPU dropped from <strong>85% to 45%</strong> during peak dinner rush.</li>
            <li>Reference introduction call with IT leadership available on request.</li>
          </ul>
        </div>

        <div class="card tint">
          <div class="card-header">
            <span class="card-title">Immediate Kickoff Action</span>
            <span class="card-badge">Ready to Start</span>
          </div>
          <p class="card-p">
            We are ready to begin Phase 1 immediately upon approval.
          </p>
          <ul class="card-bullets">
            <li><strong>Step 1:</strong> Fund the <strong>$1,000 Phase 1 Milestone</strong> on Upwork.</li>
            <li><strong>Step 2:</strong> Provide read/write access to your Supabase staging environment and repository.</li>
            <li><strong>Step 3:</strong> 30-minute kickoff call with Luca and the engineering team to confirm seed data schemas and baseline capture.</li>
          </ul>
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
