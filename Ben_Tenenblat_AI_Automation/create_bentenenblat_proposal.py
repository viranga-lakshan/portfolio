import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Automation & Business Transformation Proposal - Ben Tenenblat Ltd</title>
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
    border-bottom: 2px solid #b48324;
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
    background: #b48324;
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
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 55%, #b48324 100%);
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
    color: #fde047;
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
    border-left: 3.5px solid #b48324;
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
    background: #fef9c3;
    color: #854d0e;
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
    background: #fdfbf7;
    border-left: 3.5px solid #b48324;
    border-radius: 4px;
    padding: 6.5px 9px;
    margin-top: 5px;
  }
  .callout-title {
    font-size: 7.9pt;
    font-weight: 700;
    color: #854d0e;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.5pt;
    color: #713f12;
    line-height: 1.34;
    margin: 0;
  }

  /* Team member card */
  .member-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #b48324;
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
    color: #b48324;
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
    color: #b48324;
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
          AI Automation & Business Transformation <span class="brand-badge">Luxury Hospitality</span>
        </div>
        <div class="brand-sub">Practical AI Systems • M365 Ecosystem Integration • Operational Excellence for Luxury Events</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> Ben Tenenblat Ltd (London, UK)<br>
        <strong>Venues Served:</strong> Claridge's, The Savoy, The Dorchester, Private Estates<br>
        <strong>Engagement:</strong> Phase 1 Assessment, Roadmap & Working PoC (£2,000)<br>
        <strong>Delivery Model:</strong> Hands-On Advisory & Implementation Squad
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Intelligent Automation for Bespoke Luxury Catering: From Enquiry to Post-Event Analysis</div>
      <div class="hero-desc">
        A bespoke, hands-on AI consultancy partnership tailored specifically to Ben Tenenblat Ltd’s operational reality. Bridging administration, sales quotations, event logistics, and kitchen production through intelligent automation natively embedded within Microsoft 365—designed to eliminate administrative drag while protecting the artisanal quality, kosher integrity, and white-glove service expected at London's most prestigious venues.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Focus: <strong>Luxury Weddings • Barmitzvahs • Prestigious Galas</strong></div>
        <div class="hero-pill">Platform: <strong>Microsoft 365 • Power Automate • Copilot • Claude / OpenAI</strong></div>
        <div class="hero-pill">Discipline: <strong>Hands-On Implementation, Not Just Strategy Reports</strong></div>
        <div class="hero-pill">Compliance: <strong>UK GDPR • Kosher Protocol • Food Safety Guardrails</strong></div>
        <div class="hero-pill">Phase 1 Commitment: <strong>£2,000 Fixed Price • Includes Working PoC</strong></div>
      </div>
    </div>

    <!-- Executive Overview & Philosophy -->
    <div class="section">
      <div class="section-title">
        1. Executive Vision: Practical AI in High-End Hospitality
        <span class="tagline">Enhancing Human Artistry and Commercial Control Without Inflexible Complexity</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Operational Challenge in Luxury Catering</span>
            <span class="card-badge">Industry Realities</span>
          </div>
          <p class="card-p">
            Delivering bespoke events at locations like Claridge's, The Savoy, and The Dorchester requires orchestrating hundreds of moving variables under zero-margin-for-error conditions:
          </p>
          <ul class="card-bullets">
            <li><strong>Laborious Bespoke Quotations:</strong> Manually drafting intricate catering proposals, pricing formulas, and menu variations consumes hours of key staff time, slowing response velocity.</li>
            <li><strong>Cascading Communication Friction:</strong> A client changing their guest count from 180 to 210 requires manual notifications across kitchen production, hiring, crockery, linens, and transport.</li>
            <li><strong>Disconnected Departmental Data:</strong> Operational knowledge is often siloed in individual inboxes, Word documents, and chef prep notes, hindering proactive coordination.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Our Hands-On Transformation Philosophy</span>
            <span class="card-badge">Advisory + Build</span>
          </div>
          <p class="card-p">
            We share Ben Tenenblat Ltd's conviction: you do not need generic chatbots or theoretical strategy decks. You need a <strong>hands-on technical squad</strong> that builds working systems:
          </p>
          <ul class="card-bullets">
            <li><strong>Native M365 Ecosystem:</strong> Embedding AI directly into Outlook, Word, and Excel via Power Automate and Copilot so your team adopts it effortlessly without learning alien tools.</li>
            <li><strong>Strict Human-in-the-Loop Governance:</strong> AI drafts, calculates, and flags; your senior staff approves, signs off, and retains full commercial and culinary authority.</li>
            <li><strong>Measurable ROI & Working PoC:</strong> Delivering immediate utility in Phase 1 with an interactive proof of concept demonstrating automated brief extraction and quote generation.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Scope Alignment Table -->
    <div class="section">
      <div class="section-title">
        2. Phase 1 Scope of Work & Deliverables (£2,000 Fixed Price)
        <span class="tagline">A Comprehensive 3-Week Diagnostic, Strategic Blueprint and Working Prototype</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">Phase 1 Deliverable</th>
            <th style="width: 43%;">Consultancy & Engineering Methodology</th>
            <th style="width: 32%;">Direct Value for Ben Tenenblat Ltd</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Departmental Discovery & Process Audit</strong></td>
            <td>In-depth structured interviews with leadership, sales, event planning, and kitchen leads; mapping current end-to-end workflows from inquiry to post-event review.</td>
            <td>Clear identification of administrative bottlenecks, duplicated effort, and friction points across departments.</td>
          </tr>
          <tr>
            <td><strong>AI Technology & Architecture Blueprint</strong></td>
            <td>Evaluating Microsoft 365 Copilot, Power Automate, Claude 3.5 Sonnet / OpenAI APIs, and document automation platforms against your operational requirements.</td>
            <td>Objective, vendor-neutral technology stack recommendation balancing power, low running costs, and data security.</td>
          </tr>
          <tr>
            <td><strong>Prioritized Opportunity & ROI Matrix</strong></td>
            <td>Scoring potential automation initiatives across the 9 business areas on commercial return, implementation complexity, time savings, and risk mitigation.</td>
            <td>Clear roadmap highlighting quick wins (immediate payback) versus foundational multi-departmental investments.</td>
          </tr>
          <tr>
            <td><strong>Working Proof of Concept (PoC)</strong></td>
            <td>Building a functional, interactive prototype (e.g., automated email enquiry parser into draft Word quotation & cover email) tested on real historic event data.</td>
            <td>Tangible demonstration of working AI within your business before committing to larger Phase 2 budgets.</td>
          </tr>
          <tr>
            <td><strong>Phased Implementation Roadmap & Costing</strong></td>
            <td>Detailed breakdown of Phase 2 (Core Sales & Admin Automation) and Phase 3 (Kitchen & Operations) with transparent timelines, budgets, and milestones.</td>
            <td>Complete commercial predictability enabling informed board-level investment decisions.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">UK GDPR & Data Confidentiality Assurance</div>
      <div class="callout-text">
        High-profile weddings and prestigious corporate events require uncompromising data protection. All recommended AI architectures enforce strict UK GDPR compliance, enterprise data boundaries (ensuring your proprietary recipes, client data, and pricing never train public models), and encrypted data transmission.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Ben Tenenblat Ltd • AI Automation & Transformation Proposal</span>
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
        <div class="brand-title">The 9 Transformation Domains <span class="brand-badge">Operational Blueprint</span></div>
        <div class="brand-sub">Progressively Connecting Administration, Sales, Kitchen, Logistics & Executive Oversight</div>
      </div>
      <div class="meta-block">
        <strong>Ecosystem:</strong> Microsoft 365 + Power Automate + AI<br>
        <strong>Human Oversight:</strong> Mandatory Signoff on Quotes & Allergens<br>
        <strong>Kosher Compliance:</strong> Embedded Dietary Protocols
      </div>
    </div>

    <!-- Operational Architecture Breakdown -->
    <div class="section">
      <div class="section-title">
        3. Strategic Architecture Across the 9 Business Domains
        <span class="tagline">Eliminating Administrative Bottlenecks Across Every Department</span>
      </div>
      <div class="grid-3">
        <!-- 1. Admin & Email -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">1. Email & Task Triage</div>
          <p class="card-p">
            Intelligent Outlook monitoring that reads incoming correspondence, categorizes urgent client inquiries, extracts action items, drafts contextual replies for review, and flags overdue follow-ups.
          </p>
        </div>

        <!-- 2. Quotations & Sales -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">2. Quotation Automation</div>
          <p class="card-p">
            Extracting event specs from inquiries to auto-generate branded Word/PDF proposals referencing approved menus, venue guidelines, and pricing tiers—reducing quote creation from hours to minutes.
          </p>
        </div>

        <!-- 3. Menu Innovation -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">3. Creative Trend Intelligence</div>
          <p class="card-p">
            Monitoring global luxury dining trends, presentation concepts, and seasonal ingredients into an organized, searchable culinary knowledge base strictly filtered for kosher compliance.
          </p>
        </div>

        <!-- 4. Event Planning & Packing -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">4. Packing Lists & Functions</div>
          <p class="card-p">
            Dynamic generation of event function sheets, staffing schedules, and packing lists (crockery, glassware, linen, service gear) calculated automatically from guest counts and venue logistics.
          </p>
        </div>

        <!-- 5. Kitchen & Purchasing -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">5. Kitchen & Production Flow</div>
          <p class="card-p">
            Converting approved menus into prep schedules, scaled ingredient batching, consolidated supplier purchasing sheets, and prominent dietary/allergen safety alerts.
          </p>
        </div>

        <!-- 6. Cascading Communication -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">6. Cascading Change Triggers</div>
          <p class="card-p">
            When guest counts or menus change, the system automatically identifies downstream impacts, recalculates kitchen prep and packing lists, and triggers targeted departmental notifications.
          </p>
        </div>

        <!-- 7. Business Development -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">7. Commercial Growth & Upselling</div>
          <p class="card-p">
            AI analysis identifying upsell opportunities (specialist bars, midnight snacks, premium wine pairings), tracking lost-business reasons, and researching prospective corporate gala partnerships.
          </p>
        </div>

        <!-- 8. Executive BI -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">8. Management BI Dashboards</div>
          <p class="card-p">
            Executive daily briefings highlighting sales pipeline health, revenue projections, upcoming event readiness scores, departmental capacity constraints, and operational risk alerts.
          </p>
        </div>

        <!-- 9. Post-Event Analysis -->
        <div class="card">
          <div class="card-title" style="font-size: 8.2pt; color: #b48324; margin-bottom: 3px;">9. Post-Event Cost Auditing</div>
          <p class="card-p">
            Automated reconciliation comparing initial quote margins against actual staffing overtime, food waste, and ad-hoc transport expenses to refine future pricing models.
          </p>
        </div>
      </div>
    </div>

    <!-- Cascading Change Architecture Diagram -->
    <div class="section">
      <div class="section-title">
        4. Cascading Operational Intelligence Architecture
        <span class="tagline">How an Event Modification Automatically Synchronizes the Whole Firm</span>
      </div>
      <div class="diagram-box">
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [TRIGGER: CLIENT UPDATES EVENT]  Client modifies guest count from 180 to 220 + adds vegan course  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [INTELLIGENT ORCHESTRATION LAYER (Microsoft Power Automate + AI Document Model)]                 │
│  ├── Parses alteration email / updated function sheet & logs timestamped revision               │
│  ├── Recalculates commercial quotation delta (additional £X,XXX) for Director Approval           │
│  └── Dispatches automated cascading updates to operational departments:                         │
│       │                                                                                          │
│       ├──► [KITCHEN PRODUCTION]: Updates ingredient quantities, prep batches & vegan allergen flag│
│       ├──► [PURCHASING]: Generates top-up purchase orders for meat, produce & specialty goods     │
│       ├──► [PACKING & WAREHOUSE]: Recalculates plates, cutlery, champagne flutes (+40 covers)    │
│       ├──► [STAFFING & LOGISTICS]: Flags requirement for 2 additional front-of-house servers     │
│       └──► [EXECUTIVE BRIEF]: Updates forecasted event revenue and gross margin calculations     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [HUMAN CONFIRMATION]: Department leads receive proactive Teams/Email task card to confirm updates│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Ben Tenenblat Ltd • AI Automation & Transformation Proposal</span>
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
        <div class="brand-title">Working Proof of Concept & Precedents <span class="brand-badge">Validation</span></div>
        <div class="brand-sub">Tangible Working Prototypes and Real Enterprise Automation Systems</div>
      </div>
      <div class="meta-block">
        <strong>Phase 1 PoC:</strong> Working AI Quote & Brief Generator<br>
        <strong>Integration:</strong> Microsoft Word & Outlook Templates<br>
        <strong>Track Record:</strong> Enterprise Workflows, ERP & Reconciliation
      </div>
    </div>

    <!-- Phase 1 Working PoC -->
    <div class="section">
      <div class="section-title">
        5. Phase 1 Working Proof of Concept (PoC) Specification
        <span class="tagline">A Practical, Functional System Delivered in Phase 1 to Validate Value</span>
      </div>
      <div class="card" style="margin-bottom: 9px;">
        <div class="card-header">
          <div>
            <span class="card-title">AI-Assisted Event Brief & Quotation Generator</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Target Deliverable for Phase 1</span>
          </div>
          <span class="card-badge">Working Prototype</span>
        </div>
        <p class="card-p">
          To fulfill your requirement for a tangible proof of concept, we will build a working prototype during Phase 1 that addresses your most time-sensitive bottleneck: <strong>Client Enquiries & Quotation Drafting</strong>.
        </p>
        <div class="grid-2" style="margin-top: 5px;">
          <div>
            <strong style="font-size: 7.8pt; color: #0f172a;">How the PoC Operates:</strong>
            <ul class="card-bullets">
              <li><strong>Inquiry Ingestion:</strong> Staff paste an unformatted client inquiry email or upload an event questionnaire into a dedicated M365 intake form.</li>
              <li><strong>Intelligent Parsing:</strong> The AI model extracts event date, guest count, venue (e.g., The Savoy), style of service, budget signals, and dietary preferences.</li>
              <li><strong>Template Pre-Population:</strong> Auto-populates Ben Tenenblat Ltd's existing branded Word quotation template with appropriate menus, pricing schedules, and personalized cover letters.</li>
            </ul>
          </div>
          <div>
            <strong style="font-size: 7.8pt; color: #0f172a;">Commercial & Quality Controls:</strong>
            <ul class="card-bullets">
              <li><strong>Missing Info Detector:</strong> Highlights ambiguities (e.g., <em>"Client mentioned 180 guests but did not specify canapé duration"</em>).</li>
              <li><strong>100% Human Approval:</strong> The generated quotation opens directly in Microsoft Word for final staff review, customization, and commercial signoff before sending.</li>
              <li><strong>Zero Risk Testing:</strong> Evaluated using historical inquiries to measure time saved and accuracy without impacting live operations.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Verified Enterprise Experience -->
    <div class="section">
      <div class="section-title">
        6. Verified Enterprise Production Case Studies
        <span class="tagline">Complex Automated Workflows, Reconciliation & Multi-Departmental Systems</span>
      </div>

      <!-- Case 1: InvoiceIQ -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">Automated Reconciliation & Data Matching Engine (InvoiceIQ)</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Automated Document Processing • Janith Kavishka</span>
          </div>
          <span class="card-badge">Automated Matching</span>
        </div>
        <p class="card-p">
          Designed and engineered an automated line-item reconciliation engine performing deterministic 3-way matching between supplier purchase orders, delivery dockets, and invoices. Implemented SHA-256 idempotency controls, discrepancy flagging, and automated reconciliation audit logging.
        </p>
      </div>

      <!-- Case 2: DIMO Lanka -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">Enterprise Multi-Departmental Workflow & Logistics Platform</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: DIMO Lanka • Lead: Viranga Lakshan</span>
          </div>
          <span class="card-badge">Enterprise Orchestration</span>
        </div>
        <p class="card-p">
          Architected enterprise microservices coordinating multi-tier role-based approvals, automated document generation, and direct integrations across SAP ERP, Microsoft Graph / Azure AD, and Kafka event audit streaming for premier industrial conglomerate.
        </p>
      </div>

      <!-- Case 3: Castle Visualizer -->
      <div class="card">
        <div class="card-header">
          <div>
            <span class="card-title">Castle Visualizer — Enterprise Data & Multi-Dashboard Platform</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: Castle Group (Australia) • PM: Lithumitha Ravikumar</span>
          </div>
          <span class="card-badge">Process Governance</span>
        </div>
        <p class="card-p">
          Led delivery of enterprise data integration platform consolidating disparate operational systems into a real-time executive reporting environment. Managed requirements definition, stakeholder workflows, and user acceptance testing across multi-disciplinary teams.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Ben Tenenblat Ltd • AI Automation & Transformation Proposal</span>
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
        <div class="brand-title">Roadmap, Squad & Engagement Terms <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Structured Phasing, Team Expertise, and Predictable Commercial Collaboration</div>
      </div>
      <div class="meta-block">
        <strong>Phase 1 Fee:</strong> £2,000 Fixed Price (Milestone Based)<br>
        <strong>Timeline:</strong> 3-Week Assessment & PoC Delivery<br>
        <strong>Long-Term Vision:</strong> Staged Implementation & Ongoing Partnership
      </div>
    </div>

    <!-- Phased Roadmap -->
    <div class="section">
      <div class="section-title">
        7. Phased Implementation Roadmap
        <span class="tagline">From Immediate Diagnostic to Full Operational Cohesion</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Diagnostic, Roadmap & PoC</span>
            <span class="card-badge">£2,000 Fixed • Weeks 1–3</span>
          </div>
          <ul class="card-bullets">
            <li>Structured interviews with sales, planning, kitchen, and operational leadership.</li>
            <li>End-to-end mapping of current documentation and communication flows.</li>
            <li>Evaluate M365 Copilot, Power Automate, and specialized AI models.</li>
            <li>Build and demonstrate the working Quotation / Brief Generator PoC.</li>
            <li>Deliver prioritized Opportunity Matrix and phased implementation investment plan.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: Core Sales & Admin Deployment</span>
            <span class="card-badge">Phase 2 • Months 2–3</span>
          </div>
          <ul class="card-bullets">
            <li>Deploy production quotation generation system into live M365 Outlook & Word.</li>
            <li>Configure intelligent email triage, priority flagging, and automated follow-ups.</li>
            <li>Establish the culinary trend and kosher recipe inspiration knowledge base.</li>
            <li>Staff training, user guide documentation, and early efficiency benchmarking.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: Event Docs & Kitchen Integration</span>
            <span class="card-badge">Phase 3 • Months 4–6</span>
          </div>
          <ul class="card-bullets">
            <li>Automate packing lists, function sheets, and crockery/glassware calculations.</li>
            <li>Deploy kitchen production sheets, scaled prep schedules, and allergen alerts.</li>
            <li>Implement cascading change triggers synchronizing office and kitchen when events alter.</li>
            <li>Connect ingredient purchasing forecasts with supplier order schedules.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: BI Dashboards & Post-Event Audits</span>
            <span class="card-badge">Phase 4 • Months 7+</span>
          </div>
          <ul class="card-bullets">
            <li>Deploy executive BI briefings: sales forecasts, event readiness, and capacity alerts.</li>
            <li>Implement post-event financial auditing: quoted vs. actual costs and waste tracking.</li>
            <li>Establish continuous learning loops to refine future quotation pricing formulas.</li>
            <li>Ongoing monthly retainer for system maintenance, fine-tuning, and new AI capabilities.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Meet the Squad -->
    <div class="section">
      <div class="section-title">
        8. Meet The Transformation Squad
        <span class="tagline">Senior Systems Integration, Data Modeling & Business Process Specialists</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead AI & Systems Architect</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Systems Architecture</div>
            <p class="card-p">
              Leads M365 integration, Microsoft Graph APIs, Power Automate pipelines, LLM prompt engineering, AI agent architectures, and enterprise security safeguards.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Microsoft 365</span>
            <span class="chip">Power Automate</span>
            <span class="chip">AI Agents / APIs</span>
            <span class="chip">UK GDPR</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Senior Data & Workflow Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Enterprise Data & Systems Automation</div>
            <p class="card-p">
              Specializes in data normalization, calculation algorithms (scaling ingredients & equipment), automated document generation, and financial reconciliation.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Data Modeling</span>
            <span class="chip">Document Automation</span>
            <span class="chip">Reconciliation</span>
            <span class="chip">Logic Engines</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Transformation Project Manager</div>
            <div class="member-creds">Associate Project Manager, Arimac • Business Process Governance</div>
            <p class="card-p">
              Leads stakeholder interviews, business process mapping, change management, standard operating procedure (SOP) authoring, and team adoption training.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Process Mapping</span>
            <span class="chip">SOP Authoring</span>
            <span class="chip">Change Mgmt</span>
            <span class="chip">Sprint Delivery</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Call to action -->
    <div class="callout-box" style="background: #fdfbf7; border-left: 3.5px solid #b48324; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Next Steps & Discovery Session Scheduling</div>
      <div class="callout-text" style="color: #334155;">
        We are available to commence Phase 1 immediately under your <strong>£2,000 fixed-price budget</strong>. With our 5.5-hour timezone proximity to London, we provide seamless afternoon working sessions and workshops for your team. We welcome an introductory video discussion to align on your immediate priorities.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Ben Tenenblat Ltd • AI Automation & Transformation Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\Ben_Tenenblat_AI_Automation"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "Ben_Tenenblat_AI_Transformation_Proposal.pdf")
    
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
