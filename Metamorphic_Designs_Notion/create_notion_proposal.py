import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Notion Firm Operating System Proposal - Metamorphic Designs</title>
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
    border-bottom: 2px solid #0284c7;
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
    background: #0284c7;
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
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0369a1 100%);
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
    color: #38bdf8;
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
    border-left: 3.5px solid #0284c7;
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
    background: #e0f2fe;
    color: #0369a1;
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
    border-top: 3px solid #0284c7;
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
    color: #0284c7;
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

  /* Architecture diagram block */
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
    color: #0284c7;
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
          Metamorphic Designs <span class="brand-badge">Firm Operating System</span>
        </div>
        <div class="brand-sub">End-to-End Connected Notion Architecture for Interior Design & Architecture Practice</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> Devendra Parvalkar, Partner & Principal Designer<br>
        <strong>Practice:</strong> Metamorphic Designs, Pune (18 Years of Excellence)<br>
        <strong>Timezone:</strong> 100% Synchronous IST (UTC+5:30 Sri Lanka & India)<br>
        <strong>Engagement:</strong> Fixed-Price Milestones with 30-Day Support
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Metamorphic: Unified Practice Management & Operational Workspace</div>
      <div class="hero-desc">
        A custom-engineered, relational Notion workspace uniting Project Management, Sales CRM & Lead Intake, Site Execution, Material & Vendor Procurement, Content Marketing, HR Governance, and Executive Dashboards into one single source of truth—built ground-up for how an elite interior and architecture firm truly executes.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Focus: <strong>Residential, Hospitality, Commercial & Bungalows</strong></div>
        <div class="hero-pill">Architecture: <strong>Connected Relational Schema & Rollups</strong></div>
        <div class="hero-pill">Operations: <strong>11-Stage Design-to-Handover Workflow</strong></div>
        <div class="hero-pill">Security: <strong>Granular Teamspaces & Export Lockdown</strong></div>
        <div class="hero-pill">Delivery: <strong>5-Stage Phased Rollout + SOP Playbook</strong></div>
      </div>
    </div>

    <!-- Executive Summary & Approach -->
    <div class="section">
      <div class="section-title">
        1. Executive Summary & Delivery Approach
        <span class="tagline">Engineered Specifically to Eliminate Scattered Spreadsheets & WhatsApp Chaos</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Operational Challenge in Design Practices</span>
            <span class="card-badge">Current Reality</span>
          </div>
          <p class="card-p">
            Over 18 years of growth, handling residential bungalows, luxury penthouses, hospitality venues, and commercial spaces creates intense cross-functional coordination:
          </p>
          <ul class="card-bullets">
            <li><strong>Fragmented Data Silos:</strong> Drawings in Drive, leads in WhatsApp, contractor rates in Excel, and daily site updates trapped in phone chats.</li>
            <li><strong>Lack of Stage Visibility:</strong> Partners cannot see at a glance where approvals, payments, or procurement bottlenecks are stalling projects.</li>
            <li><strong>High Team Turnover Risks:</strong> Designers and site supervisors join and leave; without automated onboarding, offboarding, and access controls, valuable IP, vendor rates, and client data are exposed.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Our Solution Architecture for Metamorphic</span>
            <span class="card-badge">Engineering Squad</span>
          </div>
          <p class="card-p">
            This is not a generic template install. Our <strong>3-specialist squad</strong> builds an interconnected, relational system tailored to your exact 18-year operational reality:
          </p>
          <ul class="card-bullets">
            <li><strong>Central Relational Data Core:</strong> Clients ↔ Projects ↔ Tasks ↔ Vendors ↔ Invoices ↔ Marketing Assets are linked through two-way relations and automated rollups.</li>
            <li><strong>Stage-Triggered Automation:</strong> Moving a project from <em>3D Visualisation</em> to <em>Drawings & BOQ</em> automatically generates the required stage checklists and assignee tasks.</li>
            <li><strong>Pragmatic Security:</strong> Strict Teamspace permissions, restricted views, and disabled workspace export/duplication protect Metamorphic's proprietary workflows and client data.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Architecture & Module Matrix -->
    <div class="section">
      <div class="section-title">
        2. Workspace Architecture & Module Alignment
        <span class="tagline">Comprehensive Scope Covering Every Department</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 24%;">Module & Priority</th>
            <th style="width: 44%;">Notion Technical Architecture & Capabilities</th>
            <th style="width: 32%;">Impact for Metamorphic Team</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Workspace Core & Relational Map</strong></td>
            <td>Master database schema, standardized property taxonomy, unified status vocabulary, and visual navigation hub.</td>
            <td>Clean, uncluttered workspace where every department navigates instinctively in 2 clicks.</td>
          </tr>
          <tr>
            <td><strong>2. Project Management (Core Priority)</strong></td>
            <td>11-stage design-to-handover workflow, auto-task generation, 3D/Drawing approvals tracker, and mobile site execution logs.</td>
            <td>Real-time project health, stage deadlines, drawing revision logs, and zero dropped execution tasks.</td>
          </tr>
          <tr>
            <td><strong>3. Sales CRM & Tele-calling</strong></td>
            <td>Multi-channel lead capture (WhatsApp, phone, social), kanban pipeline, tele-calling caller metrics, and 1-click won lead conversion.</td>
            <td>Complete sales visibility, automated reminders, and instant project kickoff when contracts are signed.</td>
          </tr>
          <tr>
            <td><strong>4. Marketing & Pune SEO</strong></td>
            <td>Content calendar (Reels, YouTube, FB), on-site shoot repository linked to projects, and Pune local SEO/keyword tracker.</td>
            <td>Streamlined content production turning completed architectural projects into high-converting social proof.</td>
          </tr>
          <tr>
            <td><strong>5. Operations, BOQs & Vendors</strong></td>
            <td>Categorized vendor/contractor directory, material library, PO tracking, BOQ estimated vs actual margin variance, and payment milestones.</td>
            <td>Eliminates cost overruns, tracks vendor payment releases, and protects project profit margins.</td>
          </tr>
          <tr>
            <td><strong>6. HR, Attendance & Security</strong></td>
            <td>Team directory, 9:30 AM–6:30 PM attendance/leave tracker (Mon off), 30-60-90 onboarding, and strict offboarding access revocation.</td>
            <td>Partners and HR maintain complete control over employee access and sensitive company IP.</td>
          </tr>
          <tr>
            <td><strong>7. Partner Live Dashboard</strong></td>
            <td>Executive command center: active projects by stage, overdue tasks, revenue pipeline, collections due, and team workload.</td>
            <td>Devendra and partners can assess firm health in 60 seconds without messaging multiple managers.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">100% Synchronous IST Availability (Sri Lanka & Pune, India)</div>
      <div class="callout-text">
        Based in Sri Lanka (UTC+5:30), our entire team works in the <strong>exact same timezone</strong> as Pune, India. We are available for live video discovery sessions, daily sprint updates, and interactive team training during your regular 9:30 AM – 6:30 PM business hours.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Metamorphic Designs • Notion Firm Operating System Proposal</span>
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
        <div class="brand-title">Project Management & Sales CRM <span class="brand-badge">Core Engine</span></div>
        <div class="brand-sub">The Operational Engine: From First Enquiry to Site Handover</div>
      </div>
      <div class="meta-block">
        <strong>11 Project Stages:</strong> Pre-Design to Handover<br>
        <strong>Lead Ingestion:</strong> Multi-Channel & Automated<br>
        <strong>Approvals:</strong> Version-Controlled 3D & Drawings
      </div>
    </div>

    <!-- Project Management Deep Dive -->
    <div class="section">
      <div class="section-title">
        3. Project Management Module (Core Priority)
        <span class="tagline">Tailored to Interior Design & Architecture Lifecycles</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The 11-Stage Master Project Pipeline</span>
            <span class="card-badge">Lifecycle</span>
          </div>
          <p class="card-p">
            Every project flows through a standardized, stage-governed pipeline with automated stage gates:
          </p>
          <div class="diagram-box">
            01. Enquiry ➔ 02. Site Visit ➔ 03. Concept Design ➔<br>
            04. Design Development ➔ 05. 3D Visualisation ➔<br>
            06. Working Drawings & BOQ ➔ 07. Client Approval ➔<br>
            08. Procurement & POs ➔ 09. Site Execution ➔<br>
            10. Snagging & Finishing ➔ 11. Final Handover
          </div>
          <ul class="card-bullets" style="margin-top: 5px;">
            <li><strong>Auto-Task Stage Generation:</strong> Advancing to a stage automatically creates its designated deliverables (e.g., entering Stage 06 creates Electrical, Plumbing, Flooring, and Ceiling drawing tasks).</li>
            <li><strong>Tailored Views by Role:</strong> Timeline (Gantt) for leads, Kanban boards for designers, execution checklists for site engineers, and milestone cards for partners.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Approvals, Site Logs & Client Portals</span>
            <span class="card-badge">Execution</span>
          </div>
          <p class="card-p">
            <strong>Design Approvals Tracker:</strong> Version-controlled logging for 2D AutoCAD drawings, 3D SketchUp/3ds Max renders, and physical material sample sign-offs with client timestamps.
          </p>
          <p class="card-p">
            <strong>Mobile Site Execution Tracker:</strong> Site supervisors can upload daily progress photos, log contractor headcounts, flag on-site obstacles, and maintain a live Snag List with contractor assignments and completion statuses.
          </p>
          <p class="card-p">
            <strong>Secure Client-Facing Portal (Optional):</strong> A clean, read-only dashboard allowing clients to see project milestones, approved renders, and meeting minutes without accessing sensitive BOQs or vendor costs.
          </p>
        </div>
      </div>
    </div>

    <!-- Sales & CRM Module -->
    <div class="section">
      <div class="section-title">
        4. Sales & CRM Module
        <span class="tagline">Capturing, Qualifying and Converting Leads Across All Channels</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Multi-Channel Lead Capture & Ingestion</span>
            <span class="card-badge">Intake</span>
          </div>
          <p class="card-p">
            Centralize leads coming from WhatsApp, phone calls, Instagram DMs, YouTube comments, Facebook ads, website forms, and tele-callers:
          </p>
          <ul class="card-bullets">
            <li><strong>Direct Webhook / Automation Ingestion:</strong> Connect website forms and WhatsApp inquiries directly into Notion via <strong>Make / n8n</strong> or Notion native forms.</li>
            <li><strong>Lead Taxonomy:</strong> Captures Source, Location (Baner, Koregaon Park, Wakad, etc.), Property Type (Bungalow, Villa, 3BHK/4BHK), Budget Range, and Lead Temperature (🔥 Hot, ☀️ Warm, ❄️ Cold).</li>
            <li><strong>Automated Follow-Up Reminders:</strong> Notion database automations alert sales representatives before follow-ups become overdue.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Sales Pipeline & 1-Click Conversion</span>
            <span class="card-badge">Kanban Pipeline</span>
          </div>
          <p class="card-p">
            <strong>Active Pipeline Stages:</strong> <em>New Lead ➔ Contacted ➔ Qualified ➔ Site Meeting ➔ Proposal Sent ➔ Negotiation ➔ Won / Lost</em> (with lost-reason analytics: budget, timeline, competitor).
          </p>
          <p class="card-p">
            <strong>Tele-Calling Team Dashboard:</strong> Dedicated view tracking daily calls dialed, connects, qualified leads, and site meetings booked per tele-caller.
          </p>
          <p class="card-p">
            <strong>1-Click Won Conversion:</strong> Clicking "Won" triggers a Notion button that automatically creates the new Client record, initializes the Master Project with pre-filled scope and budget, and archives the lead seamlessly.
          </p>
        </div>
      </div>
    </div>

    <!-- Relational Data Map Diagram -->
    <div class="section">
      <div class="section-title">
        5. Master Relational Database Map
        <span class="tagline">How Data Flows Across Metamorphic's Workspace</span>
      </div>
      <div class="diagram-box">
        [LEADS / CRM]  ─────────(Won Lead Button)─────────►  [CLIENTS DATABASE]
              │                                                     │
              ▼                                                     ▼
     [SALES QUOTATIONS] ──► [COMMERCIALS] ◄── [MASTER PROJECTS (11 Stages)]
                                                      │           │
           ┌──────────────────────────────────────────┴─────┐     │
           ▼                                                ▼     ▼
    [STAGE TASKS & CHECKLISTS]                     [SITE EXECUTION LOGS & SNAGS]
           │                                                │
           ▼                                                ▼
    [DESIGN & 3D APPROVALS]                        [PROCUREMENT & PO TRACKER]
           │                                                │
           ▼                                                ▼
    [MARKETING CONTENT BANK]                       [VENDOR & MATERIAL DIRECTORY]
      (Reels, YouTube, Pune SEO)                    (Carpenters, Marble, Electrical)
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Metamorphic Designs • Notion Firm Operating System Proposal</span>
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
        <div class="brand-title">Operations, Marketing, HR & Security <span class="brand-badge">Governance</span></div>
        <div class="brand-sub">Securing Company Intellectual Property, Vendor Costing, and Team Operations</div>
      </div>
      <div class="meta-block">
        <strong>Working Hours:</strong> 9:30 AM – 6:30 PM (Mon Off)<br>
        <strong>Security:</strong> Restricted HR & Finance Teamspaces<br>
        <strong>Content Hub:</strong> Project-to-Content Pipeline
      </div>
    </div>

    <!-- Operations & Procurement -->
    <div class="section">
      <div class="section-title">
        6. Operations, BOQs, Vendors & Procurement
        <span class="tagline">Eliminating Material Delays and Protecting Project Margins</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Vendor & Contractor Directory</span>
            <span class="card-badge">Directory</span>
          </div>
          <p class="card-p">
            Centralized database of trusted trade partners: Carpenters, Civil Contractors, Painters, Electricians, False Ceiling, Marble/Granite suppliers, and Modular Kitchen fabricators.
          </p>
          <ul class="card-bullets">
            <li>Track specialty category, quality rating (1–5 stars), standard labor/material rates, contact details, past Metamorphic projects, and payment terms.</li>
            <li>Link contractors directly to active project site execution tasks and snag lists.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">BOQs, PO Tracking & Milestone Invoicing</span>
            <span class="card-badge">Financial Health</span>
          </div>
          <p class="card-p">
            <strong>Procurement & PO Tracker:</strong> Track items across project stages: <em>Ordered ➔ In Transit ➔ Delivered to Site ➔ Installed ➔ Approved</em>.
          </p>
          <p class="card-p">
            <strong>BOQ Variance Analysis:</strong> Compare Estimated BOQ Costs vs. Actual Site Incurred Costs with automated margin rollups to prevent budget leakage.
          </p>
          <p class="card-p">
            <strong>Milestone Payment Tracker:</strong> Track client billing milestones (Booking, Concept Signoff, Execution Milestones, Handover) and upcoming vendor payments.
          </p>
        </div>
      </div>
    </div>

    <!-- Marketing & HR Grid -->
    <div class="section">
      <div class="grid-2">
        <!-- Marketing Module -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">Marketing & Pune Local SEO Module</span>
            <span class="card-badge">Social & Growth</span>
          </div>
          <p class="card-p">
            Turn completed interior and architecture projects into steady inbound client acquisition:
          </p>
          <ul class="card-bullets">
            <li><strong>Content Calendar:</strong> Track multi-platform pipeline for Instagram Reels, YouTube home walkthroughs, and Facebook posts (<em>Idea ➔ Script ➔ Shoot ➔ Edit ➔ Scheduled ➔ Published</em>).</li>
            <li><strong>On-Site Shoot Linkage:</strong> Link content pieces directly to completed projects for effortless sourcing of before/after photos and site walk videos.</li>
            <li><strong>Pune AEO & Keyword Registry:</strong> Database of target search terms (e.g., <em>"Bungalow Architects Pune"</em>, <em>"Luxury Interior Designers Koregaon Park"</em>) tied to Google Business Profile updates.</li>
          </ul>
        </div>

        <!-- HR & Team Module -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">HR, Attendance & Role-Based Governance</span>
            <span class="card-badge">Strict Security</span>
          </div>
          <p class="card-p">
            Manage your team cleanly while locking down sensitive company assets:
          </p>
          <ul class="card-bullets">
            <li><strong>Attendance & Leave Tracker:</strong> Tailored to Metamorphic's 9:30 AM – 6:30 PM schedule, six days a week with Monday weekly off.</li>
            <li><strong>Standardized Onboarding (30-60-90):</strong> Automated checklist, tool access provisioning, design standards review, and SOP reading tasks.</li>
            <li><strong>Rapid Offboarding Protocol:</strong> Checklists to immediately revoke workspace access, reassign active tasks, and ensure drawings/files remain secure.</li>
            <li><strong>Recruitment Pipeline:</strong> Job openings, candidate resumes, interview feedback, and hiring decisions.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Security & Permissions Advisory -->
    <div class="section">
      <div class="section-title">
        7. Permissions, Security & Honest Notion Protection Advice
        <span class="tagline">Protecting Client Confidentiality, Vendor Pricing and Firm IP</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Teamspace Isolation</span>
            <span class="card-badge">Access Control</span>
          </div>
          <p class="card-p">
            Create strictly separated Teamspaces: <em>Partners Only</em> (Financials, HR, Margins), <em>Design Studio</em>, <em>Site Operations</em>, and <em>Sales & Marketing</em>.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Export & Duplication Lockdown</span>
            <span class="card-badge">IP Security</span>
          </div>
          <p class="card-p">
            Disable workspace-level exporting and template duplication across non-admin roles to prevent unauthorized bulk downloading of database lists.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Honest Notion Boundaries</span>
            <span class="card-badge">Best Practices</span>
          </div>
          <p class="card-p">
            Notion does not support column-level masking within a database. We architect separate relational summary databases for partners so staff cannot see profit margins.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Metamorphic Designs • Notion Firm Operating System Proposal</span>
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
        <div class="brand-title">Implementation Roadmap & Squad <span class="brand-badge">Execution Plan</span></div>
        <div class="brand-sub">Phased Milestone Delivery, Team Resumes, Tooling Costs & Discovery Kickoff</div>
      </div>
      <div class="meta-block">
        <strong>Execution Model:</strong> 5-Stage Phased Rollout<br>
        <strong>Timeline:</strong> 5–6 Weeks to Full Adoption<br>
        <strong>Warranty:</strong> 30 Days Dedicated Support
      </div>
    </div>

    <!-- Phased Roadmap -->
    <div class="section">
      <div class="section-title">
        8. Phased Implementation Roadmap & Milestones
        <span class="tagline">Structured Rollout Ensuring Team Adoption Without Overwhelm</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Milestone 1: Discovery & Architecture Blueprint</span>
            <span class="card-badge">Week 1</span>
          </div>
          <ul class="card-bullets">
            <li>Run a 45-minute video discovery session with Devendra and key department heads.</li>
            <li>Deliver interactive Workspace Map & Database Relational Diagram for partner approval before building.</li>
            <li>Establish master taxonomy, property standards, and Teamspace security boundaries.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Milestone 2: Project Management & Sales CRM</span>
            <span class="card-badge">Weeks 2–3 (Core Priority)</span>
          </div>
          <ul class="card-bullets">
            <li>Build the 11-stage Projects database with auto-generating stage task checklists and templates.</li>
            <li>Deploy Design Approvals tracker, Mobile Site Execution photo log, and Snagging system.</li>
            <li>Build Sales CRM, Tele-calling tracker, lead capture forms, and 1-click won lead conversion.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Milestone 3: Operations, BOQ, Marketing & HR</span>
            <span class="card-badge">Weeks 3–4</span>
          </div>
          <ul class="card-bullets">
            <li>Deploy Vendor & Contractor Directory with ratings, Material Library, and PO tracking.</li>
            <li>Build BOQ cost vs. actual variance tracker and milestone payment schedule.</li>
            <li>Configure Marketing Content Calendar, Pune SEO keyword bank, and Brand Asset wiki.</li>
            <li>Implement HR Directory, Attendance/Leave tracker (Mon off), and Onboarding/Offboarding workflows.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Milestone 4: Data Migration, Dashboards & Training</span>
            <span class="card-badge">Weeks 5–6</span>
          </div>
          <ul class="card-bullets">
            <li>Clean and migrate existing spreadsheets (leads, active projects, vendors, contacts) into Notion.</li>
            <li>Build live Partner Command Dashboard and Departmental dashboards.</li>
            <li>Deliver live recorded training sessions for partners, designers, sales, site team, and HR.</li>
            <li>Hand over written Metamorphic Notion Playbook + 30 days of post-launch adjustment support.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Meet the Squad -->
    <div class="section">
      <div class="section-title">
        9. Meet The Notion Solutions Squad
        <span class="tagline">Dedicated Engineering & Project Governance Team</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Solutions Architect</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Systems Experience</div>
            <p class="card-p">
              Leads workspace architecture, complex relational database schemas, advanced formulas, Notion automations, and third-party webhook integrations (Make/n8n).
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Notion Architecture</span>
            <span class="chip">Relational Schemas</span>
            <span class="chip">Automations</span>
            <span class="chip">Make / n8n / APIs</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Database & Migration Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Enterprise Data Systems</div>
            <p class="card-p">
              Specializes in data normalization, Excel/Sheets ETL data cleaning, historical data migration, and formula rollups ensuring zero data loss during import.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Data Migration</span>
            <span class="chip">Spreadsheet ETL</span>
            <span class="chip">Data Normalization</span>
            <span class="chip">Rollups & Formulas</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Project Manager & SOP Lead</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise SaaS Delivery</div>
            <p class="card-p">
              Manages requirement documentation, SOP authoring, milestone delivery governance, user acceptance testing, and live training walkthroughs for team adoption.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Project Management</span>
            <span class="chip">SOP Playbooks</span>
            <span class="chip">Team Training</span>
            <span class="chip">Milestone Tracking</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Tooling Costs & Call to Action -->
    <div class="section">
      <div class="section-title">
        10. Third-Party Tooling & Commercial Next Steps
        <span class="tagline">Transparent Running Costs & Zero Surprises</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Estimated Third-Party Software Costs</span>
            <span class="card-badge">Low Overhead</span>
          </div>
          <p class="card-p">
            • <strong>Notion Plus Plan:</strong> ~$8–$10/user/month (required for team collaboration and file uploads).<br>
            • <strong>Make.com / n8n:</strong> Free tier or ~$9/month (only if automating WhatsApp/web forms into Notion).<br>
            • <em>Zero other mandatory paid subscriptions required. Native Notion features handle 95% of the build.</em>
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Transparent Milestone Contracting</span>
            <span class="card-badge">Upwork Escrow</span>
          </div>
          <p class="card-p">
            We work via structured fixed-price milestone escrow on Upwork. Following a 20-minute discovery call to review your current spreadsheets, we confirm the exact fixed price per milestone within 24 hours.
          </p>
        </div>
      </div>
    </div>

    <!-- Callout -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #0284c7; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Ready to Build Metamorphic's Firm Operating System</div>
      <div class="callout-text" style="color: #334155;">
        We are available to start immediately. Please let us know a convenient time for an introductory video call this week so we can review your current spreadsheets and begin drafting your Workspace Architecture Blueprint.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Metamorphic Designs • Notion Firm Operating System Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\Metamorphic_Designs_Notion"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "Metamorphic_Designs_Notion_OS_Proposal.pdf")
    
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
