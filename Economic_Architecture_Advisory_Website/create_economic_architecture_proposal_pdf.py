import os
import pypdfium2 as pdfium
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\Viranga\Downloads\upwrok new\Economic_Architecture_Advisory_Website"
html_path = os.path.join(output_dir, "proposal_template.html")
pdf_path = os.path.join(output_dir, "Economic_Architecture_Advisory_Web_Infrastructure_Proposal.pdf")

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Economic Architecture Advisory - Web & Infrastructure Proposal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Noto+Sans+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    background-color: #E6E1D8;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #102C3A;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  
  .page {
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    position: relative;
    background-color: #F5F0E8;
    overflow: hidden;
    padding: 14mm 18mm 12mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* COLOR TOKENS */
  :root {
    --midnight: #102C3A;
    --copper: #C98352;
    --warm-neutral: #F5F0E8;
    --blue-grey: #7B929B;
    --border-light: rgba(123, 146, 155, 0.28);
    --white: #FFFFFF;
  }

  /* HEADER & FOOTER */
  .page-header {
    border-bottom: 1.5px solid var(--midnight);
    padding-bottom: 7px;
    margin-bottom: 9px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .brand-lockup {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .emblem-svg {
    width: 32px;
    height: 32px;
  }
  .brand-text-col {
    display: flex;
    flex-direction: column;
  }
  .brand-name {
    font-family: 'Cinzel', serif;
    font-size: 12.5pt;
    font-weight: 700;
    letter-spacing: 1.4px;
    color: var(--midnight);
    line-height: 1.1;
  }
  .brand-sub {
    font-size: 6.5pt;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: var(--copper);
    font-weight: 700;
    margin-top: 2px;
  }
  .header-meta {
    text-align: right;
    font-size: 6.8pt;
    color: var(--blue-grey);
    line-height: 1.35;
    font-weight: 500;
  }
  .header-meta strong {
    color: var(--midnight);
  }

  .page-footer {
    border-top: 1px solid var(--border-light);
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 6.5pt;
    color: var(--blue-grey);
  }
  .page-footer-left {
    display: flex;
    gap: 12px;
  }
  .page-num {
    font-weight: 700;
    color: var(--midnight);
  }

  /* TYPOGRAPHY */
  h1 {
    font-family: 'Cinzel', serif;
    font-size: 17pt;
    color: var(--midnight);
    line-height: 1.18;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  h2 {
    font-family: 'Cinzel', serif;
    font-size: 10.5pt;
    color: var(--midnight);
    line-height: 1.25;
    font-weight: 700;
    letter-spacing: 0.4px;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  h3 {
    font-size: 7.8pt;
    color: var(--midnight);
    font-weight: 700;
    margin-bottom: 2px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .copper-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    background-color: var(--copper);
    border-radius: 1px;
  }
  p {
    font-size: 7.5pt;
    line-height: 1.42;
    color: #243E4C;
    margin-bottom: 4px;
  }
  .arabic-text {
    font-family: 'Noto Sans Arabic', sans-serif;
    direction: rtl;
    text-align: right;
  }

  /* CARDS & CONTAINERS */
  .card {
    background-color: var(--white);
    border: 1px solid var(--border-light);
    border-radius: 4px;
    padding: 8px 11px;
    margin-bottom: 7px;
  }
  .card-dark {
    background-color: var(--midnight);
    color: #E2ECEF;
    border: 1px solid #1E4456;
    border-radius: 4px;
    padding: 9px 12px;
    margin-bottom: 7px;
  }
  .card-dark h2, .card-dark h3 {
    color: #FFFFFF;
  }
  .card-dark p {
    color: #D3DFE4;
  }
  .card-copper-accent {
    border-left: 3px solid var(--copper);
  }

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
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 6px;
  }

  /* BADGES & TAGS */
  .badge {
    display: inline-block;
    padding: 1.5px 5px;
    border-radius: 2px;
    font-size: 6.2pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .badge-copper {
    background-color: rgba(201, 131, 82, 0.15);
    color: var(--copper);
    border: 0.5px solid rgba(201, 131, 82, 0.4);
  }
  .badge-midnight {
    background-color: rgba(16, 44, 58, 0.1);
    color: var(--midnight);
    border: 0.5px solid rgba(16, 44, 58, 0.25);
  }
  .badge-dark-copper {
    background-color: rgba(201, 131, 82, 0.2);
    color: #E6A275;
    border: 0.5px solid rgba(201, 131, 82, 0.5);
  }

  /* LISTS */
  ul.spec-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  ul.spec-list li {
    font-size: 7.1pt;
    line-height: 1.35;
    color: #243E4C;
    margin-bottom: 3px;
    position: relative;
    padding-left: 11px;
  }
  ul.spec-list li::before {
    content: "■";
    position: absolute;
    left: 0;
    top: 1px;
    font-size: 4.5pt;
    color: var(--copper);
  }
  .card-dark ul.spec-list li {
    color: #D3DFE4;
  }

  /* TABLES */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 6.8pt;
    margin-top: 3px;
  }
  table.matrix-table th {
    background-color: var(--midnight);
    color: #FFFFFF;
    font-weight: 700;
    text-align: left;
    padding: 3.5px 5px;
    font-size: 6.4pt;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  table.matrix-table td {
    padding: 3px 5px;
    border-bottom: 1px solid var(--border-light);
    color: #243E4C;
    vertical-align: middle;
    line-height: 1.32;
  }
  table.matrix-table tr:nth-child(even) td {
    background-color: rgba(255, 255, 255, 0.5);
  }

  .link-pill {
    display: inline-block;
    font-size: 6.3pt;
    font-weight: 700;
    color: var(--copper);
    text-decoration: none;
    background: rgba(201, 131, 82, 0.08);
    padding: 1px 4px;
    border-radius: 2px;
    border: 0.5px solid rgba(201, 131, 82, 0.3);
  }
</style>
</head>
<body>

<!-- ================= PAGE 1: MANDATE & STRATEGIC ALIGNMENT ================= -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="brand-lockup">
        <svg class="emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="15" y="45" width="18" height="40" fill="#102C3A" rx="2"/>
          <rect x="38" y="25" width="18" height="60" fill="#102C3A" rx="2"/>
          <rect x="15" y="70" width="65" height="15" fill="#102C3A" rx="2"/>
          <rect x="61" y="15" width="18" height="30" fill="#C98352" rx="2"/>
          <rect x="61" y="50" width="18" height="15" fill="#C98352" rx="2"/>
        </svg>
        <div class="brand-text-col">
          <div class="brand-name">ECONOMIC ARCHITECTURE</div>
          <div class="brand-sub">Advisory &middot; Structure The Incentives</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SOVEREIGN WEB &amp; INFRASTRUCTURE PROPOSAL</strong><br>
        Domain: <code>econarc.com.sa</code> &middot; Brand Identity Guidelines 2026 Compliant<br>
        Technical Specification &middot; Strictly Confidential
      </div>
    </div>

    <!-- HERO STATEMENT -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 7px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 3px;">
        <span class="badge badge-dark-copper">Executive Technical Brief</span>
        <span style="font-size:6.8pt; color:#9FBAC7; font-weight:600;">RIYADH, KINGDOM OF SAUDI ARABIA</span>
      </div>
      <h1 style="color:#FFFFFF; font-size: 14pt; margin-bottom: 3px;">Sovereign Digital Presence &amp; Infrastructure Architecture</h1>
      <p style="font-size: 7.5pt; margin-bottom: 0; color: #D5E4EB;">
        Prepared specifically for <strong>Haitham Al Rebh</strong> (Principal &amp; Founder) and <strong>Roman J. Zytek, PhD</strong> (Partner). Translating Economic Architecture Advisory’s sovereign practice—operating across macroeconomic policy, institutional diagnostics, financial system dynamics, and strategic research—into a digital experience projecting <strong>quiet authority, analytical depth, and institutional credibility</strong>.
      </p>
    </div>

    <!-- MANDATE ALIGNMENT -->
    <div class="grid-2" style="margin-bottom: 7px;">
      <div class="card card-copper-accent">
        <h2><span class="copper-dot"></span> The Firm's Structural Lens</h2>
        <p style="font-size:7.3pt; margin-bottom: 4px;">
          Economic outcomes emerge from dynamic structural feedback loops governed by incentive geometry. The digital platform must articulate this analytical rigor to sovereign clients, ministries, central banks, and multilateral institutions.
        </p>
        <div style="background:#F5F0E8; border:1px solid var(--border-light); padding:4px 7px; border-radius:3px; font-size:6.9pt; color:var(--midnight); font-weight:600;">
          <em>"Structure the Incentives. Diagnose the System. Redesign the Structure. Improve the Outcome."</em>
        </div>
      </div>

      <div class="card">
        <h2><span class="copper-dot"></span> Digital Mandate Objectives</h2>
        <ul class="spec-list">
          <li><strong>Bilingual Arabic/English Parity:</strong> Full bidirectional fidelity (LTR/RTL), custom Noto Sans Arabic typography, and zero-shift language switching.</li>
          <li><strong>Exact Brand Guidelines 2026:</strong> Strict adherence to Midnight (<code>#102C3A</code>), Copper (<code>#C98352</code>), Warm Neutral (<code>#F5F0E8</code>), and Blue Grey (<code>#7B929B</code>).</li>
          <li><strong>Client-Owned Sovereign Infrastructure:</strong> Zero-trust email on <code>econarc.com.sa</code> with SPF, 2048-bit DKIM, DMARC, and DNSSEC.</li>
          <li><strong>Research Engine:</strong> Dynamic CMS repository for white papers, working papers, policy briefs, and downloadable publications.</li>
        </ul>
      </div>
    </div>

    <!-- 6 CORE ADVISORY DOMAINS MAPPING -->
    <div class="card" style="margin-bottom: 7px;">
      <h2><span class="copper-dot"></span> Alignment Across the Six Core Advisory Domains</h2>
      <p style="font-size:7.2pt; margin-bottom: 5px;">
        The digital architecture is structured to mirror the firm's interconnected analytical disciplines with distinct taxonomy, research cross-tagging, and executive clarity:
      </p>
      <div class="grid-3">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">01. Macroeconomic Policy</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Macro frameworks, fiscal &amp; external sustainability, stabilization policy, macroeconomic surveillance, and policy coordination.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">02. Institutional Diagnostics</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Institutional effectiveness, policy capacity, governance structures, implementation constraints, and reform architecture.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">03. Financial-System Dev.</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Credit markets, financial sector development, macroprudential policy, risk management, supervision, and inclusion.</p>
        </div>
      </div>
      <div class="grid-3" style="margin-top:5px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">04. Productivity &amp; Diversif.</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Total factor productivity, broad-based growth, competitiveness, innovation systems, human capital, and economic diversification.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">05. Sovereign &amp; Public Finance</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Public financial management, fiscal rules, sovereign wealth, debt &amp; asset management, performance budgeting, and resilience.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:6.9pt;">06. Strategic Economic Research</h3>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Applied research, economic intelligence, working papers, country briefs, scenario modeling, and evidence-based decision support.</p>
        </div>
      </div>
    </div>

    <!-- BRAND VOICE & IDENTITY PRINCIPLES -->
    <div class="grid-2">
      <div class="card" style="margin-bottom:0;">
        <h3 style="font-size:7.2pt; color:var(--midnight); margin-bottom:2px;">Brand Personality &amp; Tone</h3>
        <p style="font-size:6.9pt; margin:0; line-height:1.35;">
          <strong>Intellectually Serious &middot; Clearly Structured &middot; Evidence-Led.</strong><br>
          We eschew startup clichés and visual noise. The platform prioritizes calm negative space, restrained typography, and architectural geometry.
        </p>
      </div>
      <div class="card" style="margin-bottom:0;">
        <h3 style="font-size:7.2pt; color:var(--midnight); margin-bottom:2px;">Bilingual Institutional Presentation</h3>
        <p style="font-size:6.9pt; margin:0; line-height:1.35;">
          Designed specifically for senior Saudi ministerial and GCC decision-makers. Arabic is treated as a primary sovereign language, not an afterthought translation layer.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 01: Mandate &amp; Strategic Alignment</span>
    </div>
    <div class="page-num">Page 01 of 04</div>
  </div>
</div>

<!-- ================= PAGE 2: WEBFLOW CMS ARCHITECTURE & BILINGUAL ENGINEERING ================= -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="brand-lockup">
        <svg class="emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="15" y="45" width="18" height="40" fill="#102C3A" rx="2"/>
          <rect x="38" y="25" width="18" height="60" fill="#102C3A" rx="2"/>
          <rect x="15" y="70" width="65" height="15" fill="#102C3A" rx="2"/>
          <rect x="61" y="15" width="18" height="30" fill="#C98352" rx="2"/>
          <rect x="61" y="50" width="18" height="15" fill="#C98352" rx="2"/>
        </svg>
        <div class="brand-text-col">
          <div class="brand-name">ECONOMIC ARCHITECTURE</div>
          <div class="brand-sub">Webflow CMS Architecture &middot; AR / EN Parity</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SECTION 02: WEBFLOW CMS &amp; BILINGUAL SYSTEM</strong><br>
        Webflow Premium + Localize Essential Engine<br>
        Typography: Grenda &middot; Satoshi &middot; Noto Sans Arabic
      </div>
    </div>

    <!-- WEBFLOW SPECIFICATION & PILLARS -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 7px;">
      <h2 style="font-size: 10.5pt; margin-bottom: 3px; color:#FFFFFF;">Webflow CMS: High-Performance Architecture for Advisory Publishing</h2>
      <p style="font-size: 7.3pt; margin-bottom: 4px; color:#D8E5EB;">
        Webflow is the ideal platform for Economic Architecture Advisory. It combines rapid 2–3 week delivery velocity, visual autonomy for economists and advisory leadership, and a fully managed Tier-1 cloud infrastructure with zero server maintenance.
      </p>
      <div class="grid-3">
        <div style="background:rgba(255,255,255,0.06); padding:4px 6px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:6.7pt; text-transform:uppercase;">Visual Advisory Editing</div>
          <div style="font-size:6.4pt; color:#E3EFF4; margin-top:1px;">Advisory leadership updates policy briefs and working papers directly on-page with zero coding knowledge required.</div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:4px 6px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:6.7pt; text-transform:uppercase;">Native Arabic RTL Engine</div>
          <div style="font-size:6.4pt; color:#E3EFF4; margin-top:1px;">Webflow Localization applies automatic <code>dir="rtl"</code>, per-locale font styling, localized URLs, and regional SEO hreflang tags.</div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:4px 6px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:6.7pt; text-transform:uppercase;">Zero Server DevOps</div>
          <div style="font-size:6.4pt; color:#E3EFF4; margin-top:1px;">Fastly &amp; AWS edge CDN caching, automatic SSL, DDoS protection, SOC 2 compliance, and zero database patching.</div>
        </div>
      </div>
    </div>

    <!-- TECHNICAL EVALUATION BREAKDOWN -->
    <div class="card" style="margin-bottom: 7px;">
      <h2><span class="copper-dot"></span> Technical Capabilities &amp; Implementation Parameters (Webflow Premium)</h2>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width:24%;">Feature Domain</th>
            <th style="width:48%;">Webflow Implementation Specification</th>
            <th style="width:28%;">Advisory Practice Benefit</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Delivery Velocity</strong></td>
            <td>Rapid 2&ndash;3 week build; visual markup without backend overhead, allowing complete focus on brand geometry and typography.</td>
            <td>Immediate readiness for high-level client engagements and ministerial proposals.</td>
          </tr>
          <tr>
            <td><strong>Bilingual Typography</strong></td>
            <td>Headlines in <strong>Grenda</strong>, Latin body in <strong>Satoshi</strong>, Arabic in <strong>Noto Sans Arabic</strong>; custom logical CSS spacing.</td>
            <td>Authentic institutional parity between English and Arabic without awkward alignment shifts.</td>
          </tr>
          <tr>
            <td><strong>Research Repository</strong></td>
            <td>Up to 20,000 items and 40 collections; multi-faceted filtering by domain, publication date, and format.</td>
            <td>Structured repository for white papers, working papers, country briefs, and policy commentary.</td>
          </tr>
          <tr>
            <td><strong>Large Document Handling</strong></td>
            <td>Native file uploads up to 10 MB per PDF. Larger white papers linked via high-speed Cloudflare R2 / AWS S3 cloud storage.</td>
            <td>Unrestricted file size capacity for heavy econometric reports and charts.</td>
          </tr>
          <tr>
            <td><strong>Inquiry Intake Forms</strong></td>
            <td>Native encrypted forms with reCAPTCHA spam mitigation and direct cryptographic email forwarding to leadership.</td>
            <td>Discrete, reliable engagement intake for sovereign, ministerial, and multilateral clients.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- UNIFIED CONTENT ARCHITECTURE -->
    <div class="card" style="margin-bottom: 0;">
      <h2><span class="copper-dot"></span> Structured Information Architecture &amp; Core Collections</h2>
      <div class="grid-4" style="gap:5px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <h3 style="font-size:6.7pt; color:var(--copper);">1. Service Domains</h3>
          <p style="font-size:6.2pt; margin:0; line-height:1.25; color:#324C59;">6 Core Domains: Title, summary, structural lens, related insights, localized Arabic fields.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <h3 style="font-size:6.7pt; color:var(--copper);">2. Leadership Bios</h3>
          <p style="font-size:6.2pt; margin:0; line-height:1.25; color:#324C59;">Executive credentials (ex-MEP, IMF, G20, SIMAH), photo, order, LinkedIn profile.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <h3 style="font-size:6.7pt; color:var(--copper);">3. Insights Repository</h3>
          <p style="font-size:6.2pt; margin:0; line-height:1.25; color:#324C59;">White papers, policy briefs, article type, date, authors, domain tag, PDF download URL.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <h3 style="font-size:6.7pt; color:var(--copper);">4. Inquiries Gateway</h3>
          <p style="font-size:6.2pt; margin:0; line-height:1.25; color:#324C59;">Encrypted form submission, domain routing, automated email dispatch to leadership.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 02: Webflow CMS &amp; Bilingual System</span>
    </div>
    <div class="page-num">Page 02 of 04</div>
  </div>
</div>

<!-- ================= PAGE 3: INFRASTRUCTURE & VERIFIED RUNNING COSTS ================= -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="brand-lockup">
        <svg class="emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="15" y="45" width="18" height="40" fill="#102C3A" rx="2"/>
          <rect x="38" y="25" width="18" height="60" fill="#102C3A" rx="2"/>
          <rect x="15" y="70" width="65" height="15" fill="#102C3A" rx="2"/>
          <rect x="61" y="15" width="18" height="30" fill="#C98352" rx="2"/>
          <rect x="61" y="50" width="18" height="15" fill="#C98352" rx="2"/>
        </svg>
        <div class="brand-text-col">
          <div class="brand-name">ECONOMIC ARCHITECTURE</div>
          <div class="brand-sub">Security &middot; Infrastructure &middot; Transparent Costs</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SECTION 03: CLOUD &amp; EMAIL INFRASTRUCTURE</strong><br>
        Domain: <code>econarc.com.sa</code> &middot; Google Workspace / M365<br>
        Direct Client Cost Model &middot; Zero Agency Hosting Markup
      </div>
    </div>

    <!-- CLIENT OWNERSHIP & RISK PRINCIPLE -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 6px;">
      <h2 style="font-size: 10pt; margin-bottom: 2px; color:#FFFFFF;">Client-Owned Infrastructure &amp; Zero Agency Hosting Markup</h2>
      <p style="font-size: 7.2pt; margin-bottom: 3px; color:#D8E5EB;">
        In strict adherence to sovereign governance, <strong>we do not host client websites on agency accounts or charge hosting markups</strong>. All accounts (domain registrar, Webflow workspace, Google Workspace / Microsoft 365) are registered directly in <strong>Economic Architecture Advisory’s name</strong>. All third-party fees are paid directly to vendors, eliminating agency dependency and risk.
      </p>
    </div>

    <!-- VERIFIED PROJECT RUNNING COSTS TABLE -->
    <div class="card" style="margin-bottom: 6px;">
      <h2><span class="copper-dot"></span> Verified Monthly Project Infrastructure Running Costs (Direct Vendor Invoices)</h2>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width:25%;">Infrastructure Component</th>
            <th style="width:41%;">Verified Plan &amp; Platform Inclusions</th>
            <th style="width:17%;">Annual Billing</th>
            <th style="width:17%;">Monthly Billing</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Webflow CMS Hosting</strong></td>
            <td><strong>Premium Site Plan:</strong> Custom domain, 20,000 CMS items, 50 GB Fastly/AWS CDN bandwidth, site search, form uploads.</td>
            <td><strong>$25.00 / mo</strong><br><span style="font-size:5.8pt; color:#6B8089;">($300/yr upfront)</span></td>
            <td><strong>$39.00 / mo</strong><br><span style="font-size:5.8pt; color:#6B8089;">(Month-to-month)</span></td>
          </tr>
          <tr>
            <td><strong>Arabic Localization</strong></td>
            <td><strong>Localize Essential:</strong> 1 secondary Arabic locale, native automatic RTL, localized SEO, styles &amp; hreflang.</td>
            <td><strong>$9.00 / mo</strong><br><span style="font-size:5.8pt; color:#6B8089;">($108/yr upfront)</span></td>
            <td><strong>~$12.00 / mo</strong><br><span style="font-size:5.8pt; color:#6B8089;">(Month-to-month)</span></td>
          </tr>
          <tr style="background-color:rgba(201, 131, 82, 0.08);">
            <td><strong>Webflow Platform Total</strong></td>
            <td><strong>Fully managed cloud hosting, automated SSL, DDoS defense, zero server maintenance.</strong></td>
            <td><strong style="color:var(--midnight); font-size:7pt;">~$34.00 / mo</strong><br><span style="font-size:5.8pt; color:var(--copper); font-weight:700;">($408/year total)</span></td>
            <td><strong style="color:var(--midnight); font-size:7pt;">~$51.00 / mo</strong><br><span style="font-size:5.8pt; color:#6B8089;">(Flexible billing)</span></td>
          </tr>
          <tr>
            <td><strong>Saudi Domain (.com.sa)<br><code>econarc.com.sa</code></strong></td>
            <td colspan="3">
              <strong>If already owned by firm:</strong> <strong>$0 upfront</strong> (annual renewal only ~60–80 SAR / ~$16–21/yr via local Saudi registrar).<br>
              <strong>If new registration via Saudi CST/SaudiNIC registrar (e.g., Sahara Net, NourNet with CR):</strong> <strong>~60–100 SAR / year</strong> (~$16–$27 USD/year, approx. $1.50–2.25/mo).<br>
              <strong>If registered via global registrar (e.g., 101domain, Marcaria):</strong> <strong>~$50–$90+ USD / year</strong> (~$4.20–$7.50/mo) due to international administrative routing.
            </td>
          </tr>
          <tr>
            <td><strong>Enterprise Email Suite</strong></td>
            <td colspan="3">
              <strong>Google Workspace Business Starter</strong> (~$6.00/user/mo annual, $7.20 flexible) or <strong>Microsoft 365 Business Basic</strong> (~$6.00/user/mo).<br>
              For an executive team of 3 mailboxes (e.g., <code>haitham@</code>, <code>zytek@</code>, <code>inquiries@</code>), total is <strong>~$18.00–$24.00 / month</strong> paid directly to Google/Microsoft.
            </td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top:3px; font-size:6.1pt; color:var(--blue-grey); line-height:1.25;">
        *Note: All subscription fees are paid directly by the client to third-party vendors with zero markup. Agency professional development fees are separate and aligned in the discovery meeting.
      </div>
    </div>

    <!-- CRYPTOGRAPHIC EMAIL PROTOCOLS -->
    <div class="card" style="margin-bottom: 0;">
      <h2><span class="copper-dot"></span> Cryptographic Mail Deliverability Suite (econarc.com.sa)</h2>
      <div class="grid-2" style="gap: 6px;">
        <div style="border:1px solid var(--border-light); padding:5px 7px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1px;">
            <h3 style="font-size:7.1pt; color:var(--midnight); margin:0;">1. Sender Policy Framework (SPF)</h3>
            <span class="badge badge-midnight">DNS TXT</span>
          </div>
          <p style="font-size:6.5pt; margin:0 0 2px 0; line-height:1.25;">Restricts email sending authority strictly to authorized Google/Microsoft servers, stopping spoofing.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:2px 5px; border-radius:2px; font-family:monospace; font-size:6pt;">
            v=spf1 include:_spf.google.com ~all
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:5px 7px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1px;">
            <h3 style="font-size:7.1pt; color:var(--midnight); margin:0;">2. DKIM 2048-Bit Signing</h3>
            <span class="badge badge-midnight">RSA Cryptography</span>
          </div>
          <p style="font-size:6.5pt; margin:0 0 2px 0; line-height:1.25;">Signs outbound executive emails with a cryptographic key, guaranteeing message integrity in transit.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:2px 5px; border-radius:2px; font-family:monospace; font-size:6pt;">
            k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCg...
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:5px 7px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1px;">
            <h3 style="font-size:7.1pt; color:var(--midnight); margin:0;">3. DMARC Policy &amp; Telemetry</h3>
            <span class="badge badge-midnight">Policy Enforcement</span>
          </div>
          <p style="font-size:6.5pt; margin:0 0 2px 0; line-height:1.25;">Instructs recipient gateways to reject fraudulent mail while routing daily forensic telemetry to security.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:2px 5px; border-radius:2px; font-family:monospace; font-size:6pt;">
            v=DMARC1; p=reject; rua=mailto:dmarc@econarc.com.sa
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:5px 7px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1px;">
            <h3 style="font-size:7.1pt; color:var(--midnight); margin:0;">4. DNSSEC &amp; Strict Transport</h3>
            <span class="badge badge-midnight">Root Integrity</span>
          </div>
          <p style="font-size:6.5pt; margin:0 0 2px 0; line-height:1.25;">DNSSEC signing at registrar level protects <code>.com.sa</code> domain against DNS cache poisoning, with TLS 1.3.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:2px 5px; border-radius:2px; font-family:monospace; font-size:6pt;">
            RFC 8461 (MTA-STS) &amp; RFC 8460 (TLSRPT) Active
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 03: Cloud &amp; Email Infrastructure</span>
    </div>
    <div class="page-num">Page 03 of 04</div>
  </div>
</div>

<!-- ================= PAGE 4: DELIVERY TEAM, INTERNATIONAL CMS CASE STUDIES & ROADMAP ================= -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="brand-lockup">
        <svg class="emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="15" y="45" width="18" height="40" fill="#102C3A" rx="2"/>
          <rect x="38" y="25" width="18" height="60" fill="#102C3A" rx="2"/>
          <rect x="15" y="70" width="65" height="15" fill="#102C3A" rx="2"/>
          <rect x="61" y="15" width="18" height="30" fill="#C98352" rx="2"/>
          <rect x="61" y="50" width="18" height="15" fill="#C98352" rx="2"/>
        </svg>
        <div class="brand-text-col">
          <div class="brand-name">ECONOMIC ARCHITECTURE</div>
          <div class="brand-sub">Team &middot; Enterprise Track Record &middot; Roadmap</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SECTION 04: DELIVERY TEAM &amp; ROADMAP</strong><br>
        Proven Enterprise CMS &middot; GCC Sovereign Experience<br>
        Milestones: 2 to 4 Weeks &middot; Next Steps
      </div>
    </div>

    <!-- TEAM SPECIALISTS -->
    <div class="card" style="margin-bottom: 6px;">
      <h2><span class="copper-dot"></span> Senior Delivery Specialists Assigned to the Mandate</h2>
      <div class="grid-2" style="gap:6px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.2pt; margin:0; color:var(--midnight);">Viranga Lakshan</h3>
            <span class="badge badge-copper">Senior 2+ Years Exp.</span>
          </div>
          <div style="font-size:6.5pt; color:var(--copper); font-weight:700; margin-bottom:1px;">Frontend Engineering &amp; CMS Architecture Lead</div>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Enterprise CMS developer with hands-on delivery across Webflow, Sitecore Helix, Umbraco Headless, Storyblok, and Strapi. Built UAE government cultural platforms and Middle East multilingual digital portals.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.2pt; margin:0; color:var(--midnight);">Avishka Meddegoda</h3>
            <span class="badge badge-copper">6+ Years Exp.</span>
          </div>
          <div style="font-size:6.5pt; color:var(--copper); font-weight:700; margin-bottom:1px;">Cloud Architecture &amp; Security Hardening Lead</div>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Specialist in scalable cloud architectures, DNS security, and enterprise API integrations. Delivered mission-critical systems for regional telecom operators (Ooredoo Algeria, Ooredoo Maldives). Author of published IEEE research.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.2pt; margin:0; color:var(--midnight);">Janith Kavishka</h3>
            <span class="badge badge-copper">2+ Years Exp.</span>
          </div>
          <div style="font-size:6.5pt; color:var(--copper); font-weight:700; margin-bottom:1px;">Frontend Components &amp; Localization Engineer</div>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Full-stack developer specializing in React, Next.js, TypeScript, and responsive layouts. Experience delivering enterprise web systems and cloud migrations for multinational clients (SINGER Sri Lanka PLC, AWS RDS).</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.2pt; margin:0; color:var(--midnight);">Lithumitha Ravikumar</h3>
            <span class="badge badge-copper">2 Years Exp. (PM)</span>
          </div>
          <div style="font-size:6.5pt; color:var(--copper); font-weight:700; margin-bottom:1px;">Dedicated Project Manager &amp; Delivery Governance</div>
          <p style="font-size:6.5pt; margin:0; line-height:1.28; color:#324C59;">Dedicated Project Manager (First Class Honours, Business Information Systems). Extensive experience managing international deliverables, including Al Ain Museum UAE delivery coordination and Australian investment platforms.</p>
        </div>
      </div>
    </div>

    <!-- ENTERPRISE CMS INTERNATIONAL TRACK RECORD -->
    <div class="card" style="margin-bottom: 6px;">
      <h2><span class="copper-dot"></span> Recent International &amp; GCC Enterprise CMS Projects (Delivered by Team)</h2>
      <div class="grid-2" style="gap:5px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:6.8pt; color:var(--midnight);">Al Ain Museum V2 (UAE)</strong>
            <a href="https://alainmuseum.ae" class="link-pill" target="_blank">alainmuseum.ae</a>
          </div>
          <div style="font-size:6.2pt; color:var(--copper); font-weight:700;">Sitecore Headless V2 Rebuild &middot; Government Cultural Platform</div>
          <p style="font-size:6.1pt; margin:0; line-height:1.25; color:#324C59;">Rebuilding multi-site ecosystem with Next.js/React frontend &amp; Sitecore Headless CMS. Implemented recursive logic to traverse and render nested Sitecore hierarchies. Built by Viranga &amp; Lithumitha.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:6.8pt; color:var(--midnight);">Natural History Museum Abu Dhabi</strong>
            <a href="https://nhmad.ae" class="link-pill" target="_blank">nhmad.ae</a>
          </div>
          <div style="font-size:6.2pt; color:var(--copper); font-weight:700;">Sitecore Helix Architecture &middot; Abu Dhabi Government</div>
          <p style="font-size:6.1pt; margin:0; line-height:1.25; color:#324C59;">Implemented Sitecore CMS solutions following Helix principles for high-traffic government digital experience platform. Built custom C#/.NET components for multilingual content delivery.</p>
        </div>
      </div>
      <div class="grid-2" style="gap:5px; margin-top:4px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:6.8pt; color:var(--midnight);">Holsten Arabia</strong>
            <a href="https://holstenarabia.me" class="link-pill" target="_blank">holstenarabia.me</a>
          </div>
          <div style="font-size:6.2pt; color:var(--copper); font-weight:700;">Headless CMS + Next.js &middot; Bilingual Middle East Experience</div>
          <p style="font-size:6.1pt; margin:0; line-height:1.25; color:#324C59;">Built responsive multilingual digital experience platform across Middle Eastern markets, managing custom content schemas, RESTful APIs, and cross-device performance.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:4px 6px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:6.8pt; color:var(--midnight);">Gravitee.io</strong>
            <a href="https://gravitee.io" class="link-pill" target="_blank">gravitee.io</a>
          </div>
          <div style="font-size:6.2pt; color:var(--copper); font-weight:700;">Storyblok Headless + Astro &middot; Global Digital Experience</div>
          <p style="font-size:6.1pt; margin:0; line-height:1.25; color:#324C59;">Engineered reusable content components consuming headless CMS APIs, structured for modular, ultra-fast content-driven page delivery for global tech client.</p>
        </div>
      </div>
    </div>

    <!-- ROADMAP & NEXT STEPS -->
    <div class="grid-2" style="gap:6px;">
      <div class="card" style="margin-bottom:0;">
        <h2><span class="copper-dot"></span> 4-Week Phased Delivery Roadmap</h2>
        <table class="matrix-table">
          <tbody>
            <tr>
              <td><strong>Week 1: Foundations</strong></td>
              <td>Scope alignment, design tokens (Midnight, Copper, Neutral), Home + global components in English.</td>
            </tr>
            <tr>
              <td><strong>Week 2: Templates &amp; CMS</strong></td>
              <td>All page templates, 6 Domains structure, Insights research repository with filters, and inquiry forms.</td>
            </tr>
            <tr>
              <td><strong>Week 3: Bilingual &amp; DNS</strong></td>
              <td>Arabic locale, Noto Sans Arabic typography, RTL fixes, Google/M365 routing, SPF/DKIM/DMARC hardening.</td>
            </tr>
            <tr>
              <td><strong>Week 4: QA &amp; Handover</strong></td>
              <td>Cross-device testing, SEO tags, recorded editor training (1–2 hrs), admin documentation, and launch.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card-dark card-copper-accent" style="margin-bottom:0;">
        <h3 style="font-size:7.2pt; color:var(--copper); margin-bottom:2px; text-transform:uppercase;">Discovery Call &amp; Next Steps</h3>
        <p style="font-size:6.7pt; line-height:1.32; color:#D4E3EA; margin-bottom:4px;">
          Consistent with sovereign advisory engagements, professional development fees and milestone allocations will be aligned during our introductory discovery meeting based on your confirmed scope and publication schedule.
        </p>
        <div style="background:rgba(255,255,255,0.08); padding:4px 6px; border-radius:3px; border:1px solid rgba(255,255,255,0.15);">
          <div style="font-size:6.5pt; color:#FFFFFF; font-weight:700;">Initiate Engagement:</div>
          <div style="font-size:6.2pt; color:#A2BCC9; margin-top:1px;">We are available for an introductory alignment session to review visual prototypes, demonstrate Webflow editing, and verify domain setup.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 04: Delivery Team &amp; Roadmap</span>
    </div>
    <div class="page-num">Page 04 of 04</div>
  </div>
</div>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated HTML template saved to {html_path}")

# Compile HTML to PDF using Playwright Chromium
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"}
    )
    browser.close()

print(f"Successfully generated PDF at {pdf_path}")

# Verify total pages with pypdfium2
pdf = pdfium.PdfDocument(pdf_path)
print(f"Verified PDF Page count: {len(pdf)}")
for i in range(len(pdf)):
    tp = pdf[i].get_textpage()
    text = tp.get_text_range()
    first_line = text.splitlines()[0] if text.splitlines() else "EMPTY"
    print(f"Page {i+1}: {len(text)} chars | First line: {first_line[:50]}")
    s = tp.search(f"Page 0{i+1} of 04")
    m = s.get_next()
    if m:
        b = tp.get_charbox(m[0])
        print(f"  Footer Page 0{i+1} of 04 at y={b[1]:.2f} pt")
    else:
        print(f"  Footer Page 0{i+1} of 04 NOT found!")
