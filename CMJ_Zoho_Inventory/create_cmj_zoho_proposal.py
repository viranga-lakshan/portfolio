import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Zoho Inventory Architecture, SKU Restructuring & Product Bundles - CMJ Door & Hardware Corp.</title>
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
    font-size: 8.8pt;
    line-height: 1.42;
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
    margin-bottom: 12px;
  }
  .brand-title {
    font-size: 14.5pt;
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
    font-size: 7.5pt;
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
    padding: 12px 14px;
    margin-bottom: 12px;
  }
  .hero-title {
    font-size: 12.5pt;
    font-weight: 800;
    letter-spacing: -0.3px;
    margin: 0 0 4px 0;
    color: #ffffff;
  }
  .hero-desc {
    font-size: 8.3pt;
    color: #e2e8f0;
    margin: 0 0 10px 0;
    line-height: 1.4;
  }
  .hero-pills {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
  }
  .hero-pill {
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.22);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 7.4pt;
    font-weight: 600;
    color: #f8fafc;
  }
  .hero-pill strong {
    color: #38bdf8;
  }

  /* Section Styling */
  .section {
    margin-bottom: 11px;
  }
  .section-title {
    font-size: 9.6pt;
    font-weight: 800;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-left: 3.5px solid #0284c7;
    padding-left: 7px;
    margin: 0 0 7px 0;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .section-title .tagline {
    font-size: 7.6pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
  }

  /* Cards & Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9px;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 9px 11px;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 4px;
  }
  .card-title {
    font-size: 8.8pt;
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
    font-size: 8pt;
    color: #334155;
    margin: 0 0 5px 0;
    line-height: 1.35;
  }
  .card-bullets {
    margin: 0;
    padding-left: 14px;
    font-size: 7.8pt;
    color: #475569;
    line-height: 1.35;
  }
  .card-bullets li {
    margin-bottom: 3px;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.7pt;
    margin-top: 4px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 5px 8px;
    font-weight: 700;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  table.matrix-table td {
    padding: 5.5px 8px;
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
    padding: 9px 10px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .member-name {
    font-size: 9.5pt;
    font-weight: 800;
    color: #0f172a;
  }
  .member-role {
    font-size: 7.8pt;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .member-creds {
    font-size: 7.3pt;
    color: #64748b;
    margin-bottom: 6px;
    line-height: 1.3;
  }
  .skill-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 3.5px;
    margin-top: 5px;
  }
  .chip {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: #334155;
    font-size: 6.8pt;
    font-weight: 600;
    padding: 1.5px 4.5px;
    border-radius: 3px;
  }

  /* Callout */
  .callout-box {
    background: #f0fdf4;
    border-left: 3.5px solid #16a34a;
    border-radius: 4px;
    padding: 7px 10px;
    margin-top: 6px;
  }
  .callout-title {
    font-size: 8pt;
    font-weight: 700;
    color: #15803d;
    margin-bottom: 2px;
  }
  .callout-text {
    font-size: 7.6pt;
    color: #166534;
    line-height: 1.35;
    margin: 0;
  }

  /* Architecture diagram block */
  .diagram-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 5px;
    padding: 8px 10px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 7.2pt;
    color: #0f172a;
    line-height: 1.35;
    margin-top: 4px;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.3pt;
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
          Zoho Inventory & ERP Solutions Squad <span class="brand-badge">Enterprise Catalog</span>
        </div>
        <div class="brand-sub">Catalog Taxonomy • Composite Assemblies • Supplier Costs • Stock Tracking • Zoho Books Sync</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> CMJ Door & Hardware Corp.<br>
        <strong>Industry:</strong> Commercial Doors, Architectural Hardware & Building Materials<br>
        <strong>Model:</strong> 3-Specialist Solutions Squad<br>
        <strong>Commercials:</strong> Transparent Fixed-Scope Milestones (Post-Discovery)
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Comprehensive Zoho Inventory Implementation & SKU Architecture</div>
      <div class="hero-desc">
        A dedicated solutions squad providing end-to-end catalog restructuring, intelligent SKU taxonomy, automated supplier price & markup modeling, multi-component composite door/hardware packages (BOM), duplicate resolution, real-time stock tracking, and seamless financial synchronization with Zoho Books for CMJ Door & Hardware Corp.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Focus: <strong>Doors, Hardware & Building Materials</strong></div>
        <div class="hero-pill">Taxonomy: <strong>Structured SKUs & Variant Attributes</strong></div>
        <div class="hero-pill">Assemblies: <strong>Composite Items (BOM) & Package Kits</strong></div>
        <div class="hero-pill">Pricing: <strong>Supplier Cost Tracking & Dynamic Markups</strong></div>
        <div class="hero-pill">Accounting: <strong>Automated Zoho Books Sync & COGS</strong></div>
      </div>
    </div>

    <!-- Executive Summary & Approach -->
    <div class="section">
      <div class="section-title">
        1. Executive Summary & Delivery Approach
        <span class="tagline">Engineered Specifically for Building Materials & Hardware Distribution</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Door & Hardware Inventory Challenge</span>
            <span class="card-badge">Domain Specifics</span>
          </div>
          <p class="card-p">
            Commercial door and architectural hardware catalogs possess distinct complexities that generic inventory setups fail to handle:
          </p>
          <ul class="card-bullets">
            <li><strong>Complex Matrix Variations:</strong> Handing (LH/RH/LHR/RHR), fire ratings (20/45/60/90-min), core types (honeycomb, solid wood, mineral), dimensions, and finishes (US26D, US10B, Black).</li>
            <li><strong>Package Assemblies (Kits):</strong> Pre-hung door packages consisting of a slab, frame, hinges, lockset, closer, kickplate, and threshold sold as a unified unit but tracked as separate inventory items.</li>
            <li><strong>Fluctuating Supplier Pricing:</strong> Volatile steel/lumber costs and complex vendor price lists requiring dynamic markup formulas to preserve contractor and retail gross margins.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Our Solution Architecture for CMJ</span>
            <span class="card-badge">Execution Squad</span>
          </div>
          <p class="card-p">
            Rather than a lone consultant attempting data cleanup while building workflows, our <strong>3-specialist engineering squad</strong> handles data cleansing, catalog modeling, and accounting integration concurrently:
          </p>
          <ul class="card-bullets">
            <li><strong>Clean Canonical Catalog:</strong> Programmatic audit and deduplication of existing items into standardized, readable SKU conventions.</li>
            <li><strong>Composite Item & BOM Workflows:</strong> Automated bill-of-materials deduction so assembling or selling a door combo instantly updates component stock levels.</li>
            <li><strong>Bi-Directional Financial Integrity:</strong> Seamless Zoho Books sync ensuring item sales, landed freight costs, and COGS reflect accurately without double-entry.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Scope Alignment Table -->
    <div class="section">
      <div class="section-title">
        2. Scope of Work Alignment Matrix
        <span class="tagline">Direct Mapping to CMJ Door & Hardware Corp. Requirements</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">CMJ Requested Requirement</th>
            <th style="width: 42%;">Squad Implementation & Architecture Strategy</th>
            <th style="width: 33%;">Key Deliverables for CMJ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Product & Variation Organization</strong></td>
            <td>Group products into logical Item Groups (Wood Doors, Hollow Metal, Hinges, Locks, Closers) with structured attributes (Size, Finish, Handing, Rating).</td>
            <td>Clean matrix item structure eliminating standalone clutter; standardized naming conventions across all items.</td>
          </tr>
          <tr>
            <td><strong>Intelligent SKU Architecture</strong></td>
            <td>Design a hierarchical, human-readable SKU schema incorporating Category, Subtype, Material, Dimension, and Finish codes.</td>
            <td>Universal SKU Master Registry with clear rules for future staff to generate consistent SKUs easily.</td>
          </tr>
          <tr>
            <td><strong>Supplier Costs & Markup Modeling</strong></td>
            <td>Configure vendor price lists, landed cost allocations (freight/tariffs), and automated markup percentage rules per customer tier (Trade, Retail, Contractor).</td>
            <td>Real-time profit margin visibility, price lists assigned to customer types, and margin floor protection.</td>
          </tr>
          <tr>
            <td><strong>Composite Items & Product Combos</strong></td>
            <td>Build Composite Items (BOM) for complete door units and hardware sets. Configure auto-assembly and component inventory deductions.</td>
            <td>1-click quoting and sales of pre-assembled door packages while maintaining accurate component counts.</td>
          </tr>
          <tr>
            <td><strong>Duplicate Resolution & Cleanup</strong></td>
            <td>Run automated data matching scripts to identify, merge, or archive duplicate records while preserving historical transactions.</td>
            <td>Consolidated, deduplicated database with zero transaction orphan records or broken history.</td>
          </tr>
          <tr>
            <td><strong>Stock Tracking & Fulfillment</strong></td>
            <td>Set up multi-location stock tracking, reorder points, low-stock warnings, purchase orders, dropship routing, and pick/pack/ship workflows.</td>
            <td>Automated purchase alerts, purchase order creation, package slips, and shipping label integrations.</td>
          </tr>
          <tr>
            <td><strong>Zoho Books Sync & Automation</strong></td>
            <td>Map chart of accounts (Inventory Asset, COGS, Sales Income), automate tax codes, and deploy custom Deluge scripts for margin alerts and reorders.</td>
            <td>Automated real-time financial synchronization with Zoho Books; automated email/Slack alerts for low-margin quotes.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">Transparent Commercial Policy: Discovery-First, Zero Artificial Pricing</div>
      <div class="callout-text">
        Every building material business has a different catalog volume and state of duplicate records. Rather than guessing an arbitrary upfront price that risk under-delivering or over-charging, we review your catalog data during a short discovery session and provide a transparent, fixed-scope milestone quotation within 24 hours.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CMJ Door & Hardware Corp. • Zoho Inventory Architecture Proposal</span>
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
        <div class="brand-title">Meet The Inventory Squad <span class="brand-badge">Squad Roles</span></div>
        <div class="brand-sub">Complementary Engineering, Data Architecture & Project Governance Dedicated to CMJ</div>
      </div>
      <div class="meta-block">
        <strong>Engagement Model:</strong> Coordinated 3-Person Team<br>
        <strong>Lead Contact:</strong> Viranga Lakshan<br>
        <strong>Timezone:</strong> UTC+5:30 (Extensive Global Overlap)
      </div>
    </div>

    <!-- Squad Member Profiles -->
    <div class="section">
      <div class="section-title">
        3. Squad Engineering & Management Profiles
        <span class="tagline">Solutions Architect + Inventory Database Engineer + Project Manager</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Solutions Architect</div>
            <div class="member-creds">Associate Software Engineer, Arimac Lanka • 4+ Years Enterprise Experience</div>
            <p class="card-p">
              Leads systems integration, Zoho ecosystem architecture, business workflow automations, and Zoho Books financial reconciliation. Expert in ERP data pipelines, REST API workflows, and secure multi-tier catalog modeling.
            </p>
            <ul class="card-bullets">
              <li>Architected product, order, tax, shipping, and tenant inventory services for enterprise digital platforms.</li>
              <li>Integrated mission-critical microservices with enterprise ERP (SAP) and AWS cloud infrastructure.</li>
              <li>Engineered automated validation workflows and custom integration middleware with error-recovery mechanisms.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Zoho Inventory</span>
            <span class="chip">Zoho Books Sync</span>
            <span class="chip">Deluge Scripting</span>
            <span class="chip">ERP Integration</span>
            <span class="chip">Workflow Automation</span>
            <span class="chip">REST APIs</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Inventory Database Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Enterprise Stock Tracking & Catalog Systems</div>
            <p class="card-p">
              Specializes in inventory data modeling, bulk data transformations, programmatic deduplication scripts, and multi-tier distribution tracking. Experienced in managing complex product matrices and automated reconciliation.
            </p>
            <ul class="card-bullets">
              <li>Contributed to an enterprise inventory and distribution tracking platform integrated with AWS and Amazon RDS.</li>
              <li>Architected <em>InvoiceIQ</em> accounts payable matching engine with deterministic 3-way line item reconciliation.</li>
              <li>Engineered <em>Nexware</em> warehouse management system with supplier purchase orders and stock flow controls.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">SKU Architecture</span>
            <span class="chip">Composite Items / BOM</span>
            <span class="chip">Catalog Deduplication</span>
            <span class="chip">Batch Tracking</span>
            <span class="chip">Data Transformation</span>
            <span class="chip">SQL / ETL</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Project Manager</div>
            <div class="member-creds">Associate Project Manager, Arimac Lanka • Enterprise SaaS & Data Platforms</div>
            <p class="card-p">
              Manages catalog data governance, requirement specifications, sprint planning, client communication, and user training. Ensures strict milestone delivery, quality assurance, and comprehensive documentation for CMJ staff.
            </p>
            <ul class="card-bullets">
              <li>Managed delivery across 4 engineering squads for enterprise multi-tenant digital commerce SaaS platforms.</li>
              <li>Led delivery of Castle Visualizer enterprise data platform consolidating disparate operational systems.</li>
              <li>Authored comprehensive standard operating procedures (SOPs), user training guides, and acceptance criteria.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Project Management</span>
            <span class="chip">Catalog Governance</span>
            <span class="chip">Sprint Coordination</span>
            <span class="chip">User Training / SOPs</span>
            <span class="chip">QA Acceptance</span>
            <span class="chip">Milestone Tracking</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Domain Architecture: Doors & Hardware -->
    <div class="section">
      <div class="section-title">
        4. Domain Blueprint: Doors, Hardware & Composite Packages
        <span class="tagline">Tailored Specifically to Building Materials Distribution</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Hierarchical SKU Taxonomy Formula</span>
            <span class="card-badge">Standardization</span>
          </div>
          <p class="card-p">
            We replace ambiguous item descriptions with an intelligent, standardized SKU format that informs staff immediately of the product's exact specifications:
          </p>
          <div class="diagram-box">
            <strong>[CAT]-[TYPE]-[MAT]-[DIM]-[HAND]-[FINISH]</strong><br>
            • Door Slab: <code>DR-WD-SLD-3070-RH-RAW</code> (Wood, Solid Core, 3'0"x7'0", Right Hand)<br>
            • Steel Frame: <code>FR-HM-KD-3070-534-GRY</code> (Hollow Metal, Knock-Down, 5-3/4" Jamb)<br>
            • Lockset: <code>HW-LCK-MRT-ENT-US26D</code> (Hardware, Mortise Entry, Satin Chrome)<br>
            • Commercial Closer: <code>HW-CLS-HD-DA-ALM</code> (Hardware, Heavy Duty Closer, Aluminum)
          </div>
          <p class="card-p" style="margin-top: 5px;">
            Enables instant barcode scanning, rapid warehouse bin picking, and zero confusion between field installers and office sales staff.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Composite Items & Automated Bill of Materials (BOM)</span>
            <span class="card-badge">Assemblies</span>
          </div>
          <p class="card-p">
            In Zoho Inventory, we configure <strong>Composite Items</strong> for pre-hung door units, commercial openings, and packaged hardware sets:
          </p>
          <div class="diagram-box">
            <strong>COMMERCIAL OPENING PACKAGE (SKU: PKG-COMM-3070-01)</strong><br>
            ├── 1x Door Slab (DR-WD-SLD-3070-RH-RAW)<br>
            ├── 1x Hollow Metal Frame (FR-HM-KD-3070-534-GRY)<br>
            ├── 3x Ball Bearing Hinges 4.5"x4.5" (HW-HNG-BB-4545-US26D)<br>
            ├── 1x Heavy Duty Lever Lockset (HW-LCK-CYL-US26D)<br>
            └── 1x Heavy Duty Surface Closer (HW-CLS-HD-DA-ALM)
          </div>
          <p class="card-p" style="margin-top: 5px;">
            <strong>Auto-Assembly / Auto-Disassembly:</strong> Selling 1 package automatically decrements 1 slab, 1 frame, 3 hinges, 1 lock, and 1 closer in real-time, preventing stockout surprises.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CMJ Door & Hardware Corp. • Zoho Inventory Architecture Proposal</span>
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
        <div class="brand-title">Deduplication, Stocking & Accounting <span class="brand-badge">Integrity</span></div>
        <div class="brand-sub">Eliminating Inventory Clutter, Landed Costs, and Real-Time Zoho Books Synchronization</div>
      </div>
      <div class="meta-block">
        <strong>Data Cleansing:</strong> Automated & Manual Verification<br>
        <strong>Accounting Sync:</strong> Bi-Directional Chart of Accounts<br>
        <strong>Custom Logic:</strong> Deluge Automations & Webhooks
      </div>
    </div>

    <!-- Deduplication & Data Cleansing -->
    <div class="section">
      <div class="section-title">
        5. Catalog Cleansing, Pricing Rules & Zoho Books Integration
        <span class="tagline">Building a Rock-Solid Operational Foundation for CMJ</span>
      </div>

      <div class="grid-2">
        <!-- Deduplication -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">Programmatic Deduplication & Cleanup</span>
            <span class="card-badge">Zero Data Loss</span>
          </div>
          <p class="card-p">
            Duplicates happen when different employees enter items slightly differently (e.g., <em>"3/0 x 7/0 Solid Core"</em> vs <em>"3070 SC Wood Door"</em>). Our approach cleans this without corrupting past records:
          </p>
          <ul class="card-bullets">
            <li><strong>Automated Data Audit:</strong> Export existing inventory, run similarity-matching algorithms on descriptions, vendor parts, and attributes to identify all duplicate clusters.</li>
            <li><strong>Canonical SKU Mapping:</strong> Designate the true master SKU for each product group; consolidate stock counts and supplier historical costs.</li>
            <li><strong>Safe Inactivation / Merging:</strong> Merge active records where appropriate or inactivate legacy duplicates while retaining full audit history for accounting and past invoices.</li>
          </ul>
        </div>

        <!-- Pricing & Markup Modeling -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">Supplier Costs, Landed Costs & Markups</span>
            <span class="card-badge">Margin Protection</span>
          </div>
          <p class="card-p">
            Ensure every quote and sale protects CMJ's profit margins through dynamic pricing structures:
          </p>
          <ul class="card-bullets">
            <li><strong>Supplier Price Lists:</strong> Manage multi-vendor cost sheets. Easily update vendor price hikes via CSV imports without breaking sales prices.</li>
            <li><strong>Landed Cost Tracking:</strong> Distribute incoming freight, crating, and delivery charges across purchased items, calculating true cost per unit.</li>
            <li><strong>Tiered Price Rules:</strong> Configure automated markup rules in Zoho Inventory for General Contractors, Subcontractors, Architects, and Over-the-Counter Retail.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Zoho Books & Stock Tracking -->
    <div class="section">
      <div class="grid-2">
        <!-- Stock Tracking & Fulfillment -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">Warehouse Stock Tracking & Purchasing</span>
            <span class="card-badge">End-to-End Flow</span>
          </div>
          <p class="card-p">
            Streamline CMJ's daily physical and administrative operations:
          </p>
          <ul class="card-bullets">
            <li><strong>Reorder Points & Safety Stock:</strong> Establish automated minimum stock levels based on vendor lead times. Generate Purchase Orders with 1 click.</li>
            <li><strong>Multi-Location / Bin Tracking:</strong> Track items across main warehouse, staging areas, and job-site drop-ships.</li>
            <li><strong>Fulfillment Workflows:</strong> Seamless transition from Sales Order → Package Slip → Shipping Notice → Customer Delivery Receipt.</li>
          </ul>
        </div>

        <!-- Zoho Books Financial Sync -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">Bi-Directional Zoho Books Synchronization</span>
            <span class="card-badge">Financial Audit</span>
          </div>
          <p class="card-p">
            Ensure complete harmony between warehouse operations and company financials:
          </p>
          <ul class="card-bullets">
            <li><strong>Chart of Accounts Mapping:</strong> Map Inventory Asset accounts, Cost of Goods Sold (COGS), Purchase Discrepancies, and Sales Income correctly.</li>
            <li><strong>Real-Time COGS Posting:</strong> When an order is fulfilled in Zoho Inventory, Zoho Books immediately reflects the accurate COGS entry.</li>
            <li><strong>Vendor Bills & Payments:</strong> Receiving items in the warehouse automatically generates or updates Bills in Zoho Books for accounts payable approval.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Custom Automations & Reporting -->
    <div class="section">
      <div class="section-title">
        6. Custom Deluge Automations & Management Reports
        <span class="tagline">Eliminating Manual Repetitive Tasks</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #0284c7; margin-bottom: 4px;">Low-Margin Guardrail</div>
          <p class="card-p">
            Custom Deluge script that flags any estimate or sales order where gross profit drops below CMJ's target threshold (e.g., &lt; 25%), requiring manager approval before issuing.
          </p>
        </div>
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #0284c7; margin-bottom: 4px;">Supplier Price Hike Alert</div>
          <p class="card-p">
            Automated notification triggered when vendor purchasing costs increase, prompting instant review of affected sales prices and composite package rates.
          </p>
        </div>
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #0284c7; margin-bottom: 4px;">Hardware Dead-Stock Report</div>
          <p class="card-p">
            Configured analytics dashboard highlighting non-moving hinges, locksets, and specialized trim, empowering smart discounting and inventory liquidity.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CMJ Door & Hardware Corp. • Zoho Inventory Architecture Proposal</span>
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
        <div class="brand-title">Implementation Roadmap & Precedents <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Structured Phasing, Verified Enterprise Experience, and Next Steps for CMJ</div>
      </div>
      <div class="meta-block">
        <strong>Execution Model:</strong> 5-Phase Structured Rollout<br>
        <strong>Handover:</strong> Full Documentation & Team Training<br>
        <strong>Support:</strong> 30 Days Post-Deployment Warranty
      </div>
    </div>

    <!-- Implementation Roadmap -->
    <div class="section">
      <div class="section-title">
        7. Phased Implementation Roadmap
        <span class="tagline">Step-by-Step Delivery Ensuring Zero Business Interruption</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Catalog Audit & Clean Data Architecture</span>
            <span class="card-badge">Weeks 1–2</span>
          </div>
          <ul class="card-bullets">
            <li>Ingest CMJ's existing product spreadsheets, vendor price books, and current Zoho setup.</li>
            <li>Run programmatic duplicate detection; identify and map duplicate item clusters.</li>
            <li>Finalize the standardized SKU naming taxonomy and Item Group matrix for doors and hardware.</li>
            <li>Designate clean master import templates for products, variants, and custom fields.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: Composite Bundles & Supplier Costing</span>
            <span class="card-badge">Weeks 2–3</span>
          </div>
          <ul class="card-bullets">
            <li>Build Composite Item packages (Pre-hung doors, complete commercial lockset trims, frame kits).</li>
            <li>Upload vendor cost lists; configure landed cost allocations for freight and delivery.</li>
            <li>Establish customer tier pricing rules (General Contractors, Retail, Commercial Subcontractors).</li>
            <li>Test auto-assembly and auto-disassembly component deduction workflows in a sandbox.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: Stocking, Fulfillment & Zoho Books Sync</span>
            <span class="card-badge">Weeks 3–4</span>
          </div>
          <ul class="card-bullets">
            <li>Configure warehouse locations, bin labeling logic, reorder points, and automated PO generation.</li>
            <li>Integrate and test bi-directional Zoho Books synchronization: Chart of Accounts, Asset accounts, COGS, and Tax rules.</li>
            <li>Establish sales order fulfillment workflows: picking, packing, shipping, and drop-ship routing.</li>
            <li>Conduct end-to-end transaction test from Quote → Sales Order → Fulfillment → Invoice → Payment.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: Deluge Automations, Reports & Training</span>
            <span class="card-badge">Weeks 4–5</span>
          </div>
          <ul class="card-bullets">
            <li>Deploy custom Deluge scripts for margin floor protection and automated reorder alerts.</li>
            <li>Build customized management reports: inventory valuation, sales by door/hardware category, and vendor lead times.</li>
            <li>Deliver live, recorded training sessions for CMJ sales, warehouse, and accounting personnel.</li>
            <li>Provide step-by-step Standard Operating Procedure (SOP) manuals for creating future items and bundles.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Verified Enterprise Experience -->
    <div class="section">
      <div class="section-title">
        8. Verified Enterprise Precedents
        <span class="tagline">Proven Track Record in Complex Inventory, ERP & Catalog Systems</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">SINGER Sri Lanka PLC (DMS Electronics)</span>
            <span class="card-badge">Enterprise Stock</span>
          </div>
          <p class="card-p">
            <strong>Multi-Tier Inventory & Distribution Tracking:</strong> Built distribution tracking platform integrated with AWS Lambda and Amazon RDS supporting multi-tier stock flows across a nationwide distribution network, handling batch tracking and automated replenishment.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">DIMO Lanka Enterprise Gate Pass System</span>
            <span class="card-badge">ERP Integration</span>
          </div>
          <p class="card-p">
            <strong>SAP ERP & Warehouse Logistics Integration:</strong> Engineered vehicle and equipment dispatch platform integrated with enterprise SAP ERP, multi-role approval workflows, and audit logging for premier industrial conglomerate.
          </p>
        </div>
      </div>
    </div>

    <!-- Engagement Terms & Call to Action -->
    <div class="section">
      <div class="section-title">
        9. Engagement Terms & Next Steps
        <span class="tagline">Getting Started with CMJ Door & Hardware Corp.</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">1. Catalog Discovery</span>
          </div>
          <p class="card-p">
            A 20-minute call to review your current Zoho setup, approximate SKU volume, and sample door/hardware price sheets.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">2. Fixed Quote & Roadmap</span>
          </div>
          <p class="card-p">
            Within 24 hours of discovery, receive an exact milestone breakdown with defined deliverables and transparent pricing.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">3. Immediate Kickoff</span>
          </div>
          <p class="card-p">
            Squad begins data audit and SKU design immediately upon kickoff, delivering clean catalog structure in Days 1–10.
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom Action Box -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #0284c7; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Ready to Organize CMJ's Inventory</div>
      <div class="callout-text" style="color: #334155;">
        We are available to start immediately. Please let us know a convenient time for a discovery discussion, or share a sample catalog export so we can review your data structure upfront.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CMJ Door & Hardware Corp. • Zoho Inventory Architecture Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\CMJ_Zoho_Inventory"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "CMJ_Door_Hardware_Zoho_Inventory_Proposal.pdf")
    
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
