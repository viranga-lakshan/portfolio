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
<!-- Using Cinzel/Playfair as Grenda equivalent, Plus Jakarta Sans as Satoshi equivalent, and Noto Sans Arabic -->
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
    padding: 16mm 18mm 14mm 18mm;
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
    --border-light: rgba(123, 146, 155, 0.25);
    --white: #FFFFFF;
  }

  /* HEADER & FOOTER */
  .page-header {
    border-bottom: 1.5px solid var(--midnight);
    padding-bottom: 8px;
    margin-bottom: 12px;
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
    width: 34px;
    height: 34px;
  }
  .brand-text-col {
    display: flex;
    flex-direction: column;
  }
  .brand-name {
    font-family: 'Cinzel', serif;
    font-size: 13pt;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: var(--midnight);
    line-height: 1.1;
  }
  .brand-sub {
    font-size: 6.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--copper);
    font-weight: 700;
    margin-top: 2px;
  }
  .header-meta {
    text-align: right;
    font-size: 7pt;
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
    font-size: 19pt;
    color: var(--midnight);
    line-height: 1.18;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  h2 {
    font-family: 'Cinzel', serif;
    font-size: 11.5pt;
    color: var(--midnight);
    line-height: 1.25;
    font-weight: 700;
    letter-spacing: 0.4px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  h3 {
    font-size: 8.5pt;
    color: var(--midnight);
    font-weight: 700;
    margin-bottom: 3px;
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
    font-size: 8pt;
    line-height: 1.48;
    color: #243E4C;
    margin-bottom: 6px;
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
    padding: 10px 12px;
    margin-bottom: 8px;
  }
  .card-dark {
    background-color: var(--midnight);
    color: #E2ECEF;
    border: 1px solid #1E4456;
    border-radius: 4px;
    padding: 11px 14px;
    margin-bottom: 9px;
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
    gap: 9px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 7px;
  }

  /* BADGES & TAGS */
  .badge {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 2px;
    font-size: 6.5pt;
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
    font-size: 7.5pt;
    line-height: 1.4;
    color: #243E4C;
    margin-bottom: 4px;
    position: relative;
    padding-left: 12px;
  }
  ul.spec-list li::before {
    content: "■";
    position: absolute;
    left: 0;
    top: 1px;
    font-size: 5pt;
    color: var(--copper);
  }
  .card-dark ul.spec-list li {
    color: #D3DFE4;
  }

  /* TABLES */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.2pt;
    margin-top: 4px;
  }
  table.matrix-table th {
    background-color: var(--midnight);
    color: #FFFFFF;
    font-weight: 700;
    text-align: left;
    padding: 4px 6px;
    font-size: 6.8pt;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  table.matrix-table td {
    padding: 4px 6px;
    border-bottom: 1px solid var(--border-light);
    color: #243E4C;
    vertical-align: top;
  }
  table.matrix-table tr:nth-child(even) td {
    background-color: rgba(255, 255, 255, 0.5);
  }

  .link-pill {
    display: inline-block;
    font-size: 6.8pt;
    font-weight: 700;
    color: var(--copper);
    text-decoration: none;
    background: rgba(201, 131, 82, 0.08);
    padding: 1px 5px;
    border-radius: 2px;
    border: 0.5px solid rgba(201, 131, 82, 0.3);
  }
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="brand-lockup">
        <!-- SVG Umran geometric logo mark -->
        <svg class="emblem-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <!-- Base & Lower interlocking structure (Midnight) -->
          <rect x="15" y="45" width="18" height="40" fill="#102C3A" rx="2"/>
          <rect x="38" y="25" width="18" height="60" fill="#102C3A" rx="2"/>
          <rect x="15" y="70" width="65" height="15" fill="#102C3A" rx="2"/>
          <!-- Two upper-right forms (Copper #C98352) -->
          <rect x="61" y="15" width="18" height="30" fill="#C98352" rx="2"/>
          <rect x="61" y="50" width="18" height="15" fill="#C98352" rx="2"/>
        </svg>
        <div class="brand-text-col">
          <div class="brand-name">ECONOMIC ARCHITECTURE</div>
          <div class="brand-sub">Advisory &middot; Structure The Incentives</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SOVEREIGN WEB & INFRASTRUCTURE PROPOSAL</strong><br>
        Domain: <code>econarc.com.sa</code> &middot; Brand Identity Guidelines 2026 Compliant<br>
        Date: November 2026 &middot; Strictly Confidential
      </div>
    </div>

    <!-- HERO STATEMENT -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 10px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 4px;">
        <span class="badge badge-dark-copper">Executive Technical Brief</span>
        <span style="font-size:7pt; color:#9FBAC7; font-weight:600;">RIYADH, KINGDOM OF SAUDI ARABIA</span>
      </div>
      <h1 style="color:#FFFFFF; font-size: 15.5pt; margin-bottom: 5px;">Sovereign Digital Presence & Secure Cloud Infrastructure</h1>
      <p style="font-size: 8pt; margin-bottom: 0; color: #D5E4EB;">
        Prepared specifically for <strong>Haitham Al Rebh</strong> (Principal &amp; Founder) and <strong>Roman J. Zytek, PhD</strong> (Partner). Translating Economic Architecture Advisory’s sovereign-grade practice—operating across macroeconomic policy, institutional diagnostics, financial system dynamics, and strategic research—into a digital experience marked by <strong>quiet authority, analytical depth, and institutional credibility</strong>.
      </p>
    </div>

    <!-- MANDATE ALIGNMENT -->
    <div class="grid-2" style="margin-bottom: 8px;">
      <div class="card card-copper-accent">
        <h2><span class="copper-dot"></span> The Firm's Structural Lens</h2>
        <p style="font-size:7.6pt; margin-bottom: 5px;">
          Economic performance is not produced by isolated initiatives; it is governed by dynamic incentive geometry, institutional behavior, and financial architecture. The digital platform must project this analytical rigor to sovereign clients, ministries, central banks, and multilateral institutions.
        </p>
        <div style="background:#F5F0E8; border:1px solid var(--border-light); padding:5px 8px; border-radius:3px; font-size:7.2pt; color:var(--midnight); font-weight:600;">
          <em>"Structure the Incentives. Diagnose the System. Redesign the Structure. Improve the Outcome."</em>
        </div>
      </div>

      <div class="card">
        <h2><span class="copper-dot"></span> Digital Mandate Objectives</h2>
        <ul class="spec-list">
          <li><strong>Bilingual Arabic/English Parity:</strong> Full bidirectional fidelity (LTR/RTL), custom Noto Sans Arabic typography, and zero-shift language switching.</li>
          <li><strong>Exact Brand Guidelines 2026:</strong> Strict adherence to Midnight (<code>#102C3A</code>), Copper (<code>#C98352</code>), Warm Neutral (<code>#F5F0E8</code>), and Blue Grey (<code>#7B929B</code>).</li>
          <li><strong>Zero-Trust Mail Infrastructure:</strong> Google Workspace / M365 on <code>econarc.com.sa</code> with SPF, 2048-bit DKIM, DMARC, and DNSSEC.</li>
          <li><strong>Research Engine:</strong> Dynamic CMS repository for white papers, working papers, policy briefs, and downloadable publications.</li>
        </ul>
      </div>
    </div>

    <!-- 6 CORE ADVISORY DOMAINS MAPPING -->
    <div class="card" style="margin-bottom: 8px;">
      <h2><span class="copper-dot"></span> Alignment Across the Six Core Advisory Domains</h2>
      <p style="font-size:7.5pt; margin-bottom: 6px;">
        The digital architecture is structured to mirror the firm's interconnected analytical disciplines with distinct taxonomy, research cross-tagging, and executive clarity:
      </p>
      <div class="grid-3">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">01. Macroeconomic Policy</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Macro frameworks, fiscal &amp; external sustainability, stabilization policy, macroeconomic surveillance, and policy coordination.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">02. Institutional Diagnostics</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Institutional effectiveness, policy capacity, governance structures, implementation constraints, and reform architecture.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">03. Financial-System Dev.</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Credit markets, financial sector development, macroprudential policy, risk management, supervision, and inclusion.</p>
        </div>
      </div>
      <div class="grid-3" style="margin-top:6px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">04. Productivity &amp; Diversif.</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Total factor productivity, broad-based growth, competitiveness, innovation systems, human capital, and economic diversification.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">05. Sovereign &amp; Public Finance</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Public financial management, fiscal rules, sovereign wealth, debt &amp; asset management, performance budgeting, and resilience.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--copper); font-size:7.3pt;">06. Strategic Economic Research</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35; color:#324C59;">Applied research, economic intelligence, working papers, country briefs, scenario modeling, and evidence-based decision support.</p>
        </div>
      </div>
    </div>

    <!-- BRAND VOICE & IDENTITY PRINCIPLES -->
    <div class="grid-2">
      <div class="card" style="margin-bottom:0;">
        <h3 style="font-size:7.5pt; color:var(--midnight); margin-bottom:4px;">Brand Personality &amp; Tone</h3>
        <p style="font-size:7.2pt; margin:0; line-height:1.4;">
          <strong>Intellectually Serious &middot; Clearly Structured &middot; Evidence-Led.</strong><br>
          We eschew startup clich&eacute;s, aggressive marketing triggers, and visual noise. The platform prioritizes calm negative space, restrained typography, and architectural geometry.
        </p>
      </div>
      <div class="card" style="margin-bottom:0;">
        <h3 style="font-size:7.5pt; color:var(--midnight); margin-bottom:4px;">Bilingual Institutional Presentation</h3>
        <p style="font-size:7.2pt; margin:0; line-height:1.4;">
          Designed specifically for senior Saudi ministerial and GCC decision-makers. Arabic is treated as a primary sovereign language, not an afterthought translation layer.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Confidential &middot; For Client Internal Review</span>
    </div>
    <div class="page-num">Page 01 of 04</div>
  </div>
</div>

<!-- ================= PAGE 2 ================= -->
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
          <div class="brand-sub">Digital System Architecture &middot; AR / EN</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SECTION 02: BILINGUAL UX &amp; CMS ARCHITECTURE</strong><br>
        Webflow / Decoupled Engine &middot; RTL/LTR Calibration<br>
        Typography: Grenda, Satoshi, Noto Sans Arabic
      </div>
    </div>

    <!-- BILINGUAL ARCHITECTURE & TYPOGRAPHY -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 9px;">
      <h2 style="font-size: 11pt; margin-bottom: 4px; color:#FFFFFF;">Bilingual System Architecture: Arabic &amp; English Parity</h2>
      <p style="font-size: 7.7pt; margin-bottom: 6px; color:#D8E5EB;">
        Creating an authentic bilingual institutional experience requires deep bidirectional typographic engineering, rather than simple CSS mirroring. Every component is designed to maintain optical balance across Latin and Arabic scripts.
      </p>
      <div class="grid-3">
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">English Latin Scale</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;">Headlines in <strong>Grenda</strong> (36&ndash;44pt / 24&ndash;30pt). Body copy in <strong>Satoshi</strong> (9&ndash;11pt, 145&ndash;155% leading, 0 to +5% tracking).</div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">Arabic Noto Scale</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;" class="arabic-text">العناوين والنصوص بخط <strong>Noto Sans Arabic</strong> مع ضبط ارتفاع الأسطر وتوافق المحاذاة والرموز الهندسية.</div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">Zero-Shift Language Switch</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;">Instant client-side route switching (<code>/en/</code> and <code>/ar/</code>) preserving reading state, scroll coordinates, and document filters.</div>
        </div>
      </div>
    </div>

    <!-- CORE 5 PAGES ARCHITECTURE -->
    <div class="card" style="margin-bottom: 9px;">
      <h2><span class="copper-dot"></span> Core Institutional Site Structure</h2>
      <div class="grid-2" style="gap: 8px;">
        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">01. Home / Structural Foundation</h3>
            <span class="badge badge-midnight">Landing</span>
          </div>
          <p style="font-size:6.9pt; margin:0; line-height:1.35;">Introduction to the firm's sovereign purpose, dynamic incentive geometry, and the structural diagnostic method. Direct gateways to leadership, advisory domains, and published intelligence.</p>
        </div>
        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">02. Founders &amp; Leadership</h3>
            <span class="badge badge-midnight">Credentials</span>
          </div>
          <p style="font-size:6.9pt; margin:0; line-height:1.35;">Executive advisory profiles of Haitham Al Rebh (ex-MEP, G20 Working Group Co-Chair, Order of King Abdul Aziz) and Dr. Roman J. Zytek (ex-IMF Senior Economist, Saudi G20 Adviser, Central Bank Chief Economist).</p>
        </div>
        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">03. Domains of Advisory Work</h3>
            <span class="badge badge-midnight">Frameworks</span>
          </div>
          <p style="font-size:6.9pt; margin:0; line-height:1.35;">In-depth structural breakdown of the 6 interconnected practice areas, articulating the diagnostic approach from surface symptoms to governing incentive structures.</p>
        </div>
        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">04. Insights &amp; Research Repository</h3>
            <span class="badge badge-midnight">CMS Engine</span>
          </div>
          <p style="font-size:6.9pt; margin:0; line-height:1.35;">Structured publishing platform for white papers, working papers, country briefs, and policy commentary. Multi-faceted filtering by domain, publication date, and downloadable bilingual PDFs.</p>
        </div>
      </div>
      <div style="border:1px solid var(--border-light); padding:6px 9px; border-radius:3px; background:#FAF8F5; margin-top:6px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
          <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">05. Institutional Inquiries &amp; Advisory Engagement</h3>
          <span class="badge badge-copper">Engagement Gateway</span>
        </div>
        <p style="font-size:6.9pt; margin:0; line-height:1.35;">Discrete, institutional contact gateway with automated cryptographic email routing to firm leadership, encrypted form submissions, and direct contact details for Saudi Arabia and international mandates.</p>
      </div>
    </div>

    <!-- CMS PLATFORM EVALUATION -->
    <div class="card" style="margin-bottom: 0;">
      <h2><span class="copper-dot"></span> CMS Engine Analysis: Webflow vs. Headless Architecture</h2>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width:25%;">Architecture Metric</th>
            <th style="width:37.5%;">Webflow CMS (Primary Preference)</th>
            <th style="width:37.5%;">Enterprise Headless (Next.js + Strapi/Storyblok)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Editorial Autonomy</strong></td>
            <td><strong>Superior:</strong> Non-technical visual editing. Leadership can draft and publish research papers without developer intervention.</td>
            <td><strong>High:</strong> Structured content schemas via Storyblok or Strapi dashboard; preview requires webhook rebuild.</td>
          </tr>
          <tr>
            <td><strong>Performance &amp; CDN</strong></td>
            <td><strong>Sub-Second:</strong> Tier-1 AWS/Fastly edge CDN caching, clean semantic HTML5, automated WebP/AVIF image pipeline.</td>
            <td><strong>Sub-Second:</strong> Static site generation (SSG) with Edge Vercel/Cloudflare deployment.</td>
          </tr>
          <tr>
            <td><strong>Bilingual Management</strong></td>
            <td><strong>Built-in Localization:</strong> Native Webflow Localization handles RTL/LTR page trees, localized slugs, and typography per locale.</td>
            <td><strong>Custom Code:</strong> Next.js <code>next-intl</code> or i18next configuration with custom RTL CSS stylesheets.</td>
          </tr>
          <tr>
            <td><strong>Maintenance &amp; Security</strong></td>
            <td><strong>Zero Server Overhead:</strong> Fully managed SaaS, zero server patching, automated SSL, SOC 2 Type II certified.</td>
            <td><strong>Requires DevOps:</strong> Containerized Node/Postgres hosting, regular dependency updates, reverse proxy configuration.</td>
          </tr>
          <tr>
            <td><strong>Recommendation</strong></td>
            <td><strong style="color:var(--copper);">RECOMMENDED:</strong> Perfectly matches your speed-to-market, security, and independent publishing requirements.</td>
            <td><strong>ALTERNATIVE:</strong> Evaluated if sovereign data residency strictly dictates GCC-only dedicated cloud hosting.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 02: Bilingual UX &amp; CMS Architecture</span>
    </div>
    <div class="page-num">Page 02 of 04</div>
  </div>
</div>

<!-- ================= PAGE 3 ================= -->
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
          <div class="brand-sub">Infrastructure &middot; Security &middot; Deliverability</div>
        </div>
      </div>
      <div class="header-meta">
        <strong>SECTION 03: SOVEREIGN CLOUD &amp; MAIL SECURITY</strong><br>
        Domain: <code>econarc.com.sa</code> &middot; Google Workspace / M365<br>
        Protocols: SPF, DKIM (2048-bit), DMARC, DNSSEC, TLS 1.3
      </div>
    </div>

    <!-- INFRASTRUCTURE OVERVIEW -->
    <div class="card-dark card-copper-accent" style="margin-bottom: 9px;">
      <h2 style="font-size: 11pt; margin-bottom: 4px; color:#FFFFFF;">Enterprise Email Routing &amp; Cryptographic Deliverability</h2>
      <p style="font-size: 7.7pt; margin-bottom: 6px; color:#D8E5EB;">
        For a strategic advisory practice communicating with ministers, central banks, and sovereign funds, email infrastructure cannot tolerate spoofing, spam flagging, or deliverability failures. We implement a bank-grade cryptographic authentication suite on <code>econarc.com.sa</code>.
      </p>
      <div class="grid-3">
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">Custom Business Addresses</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;"><code>haitham@econarc.com.sa</code><br><code>zytek@econarc.com.sa</code><br><code>inquiries@econarc.com.sa</code></div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">Platform Selection</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;">Google Workspace Enterprise or Microsoft 365 Business Premium with multi-factor authentication (MFA) enforcement.</div>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:6px 8px; border-radius:3px; border:1px solid rgba(255,255,255,0.12);">
          <div style="color:var(--copper); font-weight:700; font-size:7pt; text-transform:uppercase;">Deliverability Guarantee</div>
          <div style="font-size:6.8pt; color:#E3EFF4; margin-top:2px;">100% inbox placement score across institutional mail gateways (Outlook, Gmail, government firewalls).</div>
        </div>
      </div>
    </div>

    <!-- PROTOCOL SECURITY BLUEPRINT -->
    <div class="card" style="margin-bottom: 9px;">
      <h2><span class="copper-dot"></span> Cryptographic Mail Authentication Architecture</h2>
      <div class="grid-2" style="gap: 8px;">
        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">1. Sender Policy Framework (SPF)</h3>
            <span class="badge badge-midnight">DNS TXT</span>
          </div>
          <p style="font-size:6.8pt; margin:0 0 3px 0; line-height:1.35;">Restricts email sending authority strictly to authorized Google/Microsoft servers, stopping unauthorized domain impersonation.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:3px 6px; border-radius:2px; font-family:monospace; font-size:6.2pt;">
            v=spf1 include:_spf.google.com ~all
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">2. DKIM 2048-Bit Signing</h3>
            <span class="badge badge-midnight">RSA Cryptography</span>
          </div>
          <p style="font-size:6.8pt; margin:0 0 3px 0; line-height:1.35;">Signs all outbound messages with a private cryptographic key, validating that executive messages have not been altered in transit.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:3px 6px; border-radius:2px; font-family:monospace; font-size:6.2pt;">
            k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCg...
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">3. DMARC Policy &amp; Telemetry</h3>
            <span class="badge badge-midnight">Policy Enforcement</span>
          </div>
          <p style="font-size:6.8pt; margin:0 0 3px 0; line-height:1.35;">Instructs receiving mail servers to reject or quarantine fraudulent emails, while routing daily forensic reports to security monitoring.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:3px 6px; border-radius:2px; font-family:monospace; font-size:6.2pt;">
            v=DMARC1; p=reject; rua=mailto:dmarc@econarc.com.sa
          </div>
        </div>

        <div style="border:1px solid var(--border-light); padding:7px 9px; border-radius:3px; background:#FAF8F5;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2px;">
            <h3 style="font-size:7.5pt; color:var(--midnight); margin:0;">4. DNSSEC &amp; Strict Transport</h3>
            <span class="badge badge-midnight">Root Integrity</span>
          </div>
          <p style="font-size:6.8pt; margin:0 0 3px 0; line-height:1.35;">DNS Security Extensions (DNSSEC) to protect the <code>.com.sa</code> domain against DNS spoofing, coupled with MTA-STS and TLS 1.3 enforcement.</p>
          <div style="background:#102C3A; color:#E6F0F5; padding:3px 6px; border-radius:2px; font-family:monospace; font-size:6.2pt;">
            RFC 8461 (MTA-STS) &amp; RFC 8460 (TLSRPT) Active
          </div>
        </div>
      </div>
    </div>

    <!-- WEB HOSTING & EDGE PERFORMANCE -->
    <div class="card" style="margin-bottom: 0;">
      <h2><span class="copper-dot"></span> Sovereign Web Hosting, Global Edge &amp; Compliance</h2>
      <div class="grid-3">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--midnight); font-size:7.2pt;">Global Edge Network</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35;">Distributed multi-region CDN points of presence in Riyadh, Dubai, Frankfurt, London, and Virginia ensuring sub-second response times worldwide.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--midnight); font-size:7.2pt;">SSL &amp; Transport Security</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35;">Automated zero-downtime SSL certificate rotation, TLS 1.3 protocol suite, and HTTP Strict Transport Security (HSTS) with preloading.</p>
        </div>
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <h3 style="color:var(--midnight); font-size:7.2pt;">Form Privacy &amp; GDPR / PDPL</h3>
          <p style="font-size:6.8pt; margin:0; line-height:1.35;">Compliance with Saudi Personal Data Protection Law (PDPL) and GDPR: sanitized inquiry forms, CAPTCHA-free bot defense, and encrypted transit.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="page-footer-left">
      <span>Economic Architecture Advisory &middot; Sovereign Web &amp; Infrastructure Proposal</span>
      <span>|</span>
      <span>Section 03: Sovereign Cloud &amp; Mail Security</span>
    </div>
    <div class="page-num">Page 03 of 04</div>
  </div>
</div>

<!-- ================= PAGE 4 ================= -->
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
    <div class="card" style="margin-bottom: 8px;">
      <h2><span class="copper-dot"></span> Senior Delivery Specialists Assigned to the Mandate</h2>
      <div class="grid-2" style="gap:7px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.4pt; margin:0; color:var(--midnight);">Avishka Meddegoda</h3>
            <span class="badge badge-copper">6+ Years Exp.</span>
          </div>
          <div style="font-size:6.7pt; color:var(--copper); font-weight:700; margin-bottom:2px;">Cloud Architecture &amp; Security Hardening Lead</div>
          <p style="font-size:6.7pt; margin:0; line-height:1.35; color:#324C59;">Specialist in scalable cloud architectures, DNS security, and enterprise API integrations. Delivered mission-critical systems for regional telecom operators (Ooredoo Algeria, Ooredoo Maldives). Author of published IEEE research.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.4pt; margin:0; color:var(--midnight);">Viranga Lakshan</h3>
            <span class="badge badge-copper">Senior 2+ Years Exp.</span>
          </div>
          <div style="font-size:6.7pt; color:var(--copper); font-weight:700; margin-bottom:2px;">Frontend Engineering &amp; CMS Architecture Lead</div>
          <p style="font-size:6.7pt; margin:0; line-height:1.35; color:#324C59;">Enterprise CMS developer with deep expertise across Webflow, Sitecore Helix, Umbraco Headless, Storyblok, and Strapi. Lead frontend/CMS engineer for UAE government cultural platforms and GCC multilingual portals.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.4pt; margin:0; color:var(--midnight);">Janith Kavishka</h3>
            <span class="badge badge-copper">2+ Years Exp.</span>
          </div>
          <div style="font-size:6.7pt; color:var(--copper); font-weight:700; margin-bottom:2px;">Frontend Components &amp; Localization Engineer</div>
          <p style="font-size:6.7pt; margin:0; line-height:1.35; color:#324C59;">Full-stack developer specializing in React, Next.js, TypeScript, and responsive layouts. Proven experience delivering enterprise web systems and cloud migrations for multinational clients (SINGER Sri Lanka PLC, AWS RDS).</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:6px 8px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:7.4pt; margin:0; color:var(--midnight);">Lithumitha Ravikumar</h3>
            <span class="badge badge-copper">2 Years Exp. (PM)</span>
          </div>
          <div style="font-size:6.7pt; color:var(--copper); font-weight:700; margin-bottom:2px;">Dedicated Project Manager &amp; Delivery Governance</div>
          <p style="font-size:6.7pt; margin:0; line-height:1.35; color:#324C59;">Dedicated Project Manager (First Class Honours, Business Information Systems). Extensive experience managing international deliverables, including Al Ain Museum UAE delivery coordination and Australian investment platforms.</p>
        </div>
      </div>
    </div>

    <!-- ENTERPRISE CMS TRACK RECORD -->
    <div class="card" style="margin-bottom: 8px;">
      <h2><span class="copper-dot"></span> Proven Enterprise CMS Track Record &amp; GCC Institutional Experience</h2>
      <div class="grid-3" style="gap:6px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:7pt; color:var(--midnight);">Al Ain Museum (UAE)</strong>
            <a href="https://alainmuseum.ae" class="link-pill" target="_blank">alainmuseum.ae</a>
          </div>
          <div style="font-size:6.4pt; color:var(--copper); font-weight:700; margin-top:1px;">Sitecore Headless V2 Rebuild</div>
          <p style="font-size:6.3pt; margin:0; line-height:1.3; color:#324C59;">Government cultural institution platform in Abu Dhabi/Dubai. Frontend &amp; CMS delivery coordination by Viranga &amp; Lithumitha.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:7pt; color:var(--midnight);">Nat. History Museum</strong>
            <a href="https://nhmad.ae" class="link-pill" target="_blank">nhmad.ae</a>
          </div>
          <div style="font-size:6.4pt; color:var(--copper); font-weight:700; margin-top:1px;">Sitecore Helix Architecture</div>
          <p style="font-size:6.3pt; margin:0; line-height:1.3; color:#324C59;">Abu Dhabi government digital experience platform. Multilingual content delivery, performance, and platform stability.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:7pt; color:var(--midnight);">Holsten Arabia</strong>
            <a href="https://holstenarabia.me" class="link-pill" target="_blank">holstenarabia.me</a>
          </div>
          <div style="font-size:6.4pt; color:var(--copper); font-weight:700; margin-top:1px;">Umbraco Headless + Next.js</div>
          <p style="font-size:6.3pt; margin:0; line-height:1.3; color:#324C59;">Multilingual Middle Eastern digital experience platform with C#/.NET structured content schemas and responsive layouts.</p>
        </div>
      </div>
      <div class="grid-2" style="gap:6px; margin-top:5px;">
        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:7pt; color:var(--midnight);">Gravitee.io</strong>
            <a href="https://gravitee.io" class="link-pill" target="_blank">gravitee.io</a>
          </div>
          <div style="font-size:6.4pt; color:var(--copper); font-weight:700; margin-top:1px;">Storyblok Headless + Astro</div>
          <p style="font-size:6.3pt; margin:0; line-height:1.3; color:#324C59;">High-performance, content-driven global site using reusable Storyblok components for scalable digital experience.</p>
        </div>

        <div style="background:#FAF8F5; border:1px solid var(--border-light); padding:5px 7px; border-radius:3px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="font-size:7pt; color:var(--midnight);">Moolee Multi-Tenant E-Commerce</strong>
            <a href="https://moolee.mv" class="link-pill" target="_blank">moolee.mv</a>
          </div>
          <div style="font-size:6.4pt; color:var(--copper); font-weight:700; margin-top:1px;">Strapi Headless CMS + Node.js</div>
          <p style="font-size:6.3pt; margin:0; line-height:1.3; color:#324C59;">Multi-tenant enterprise platform with custom Strapi content schemas, automated workflows, and microservice integrations.</p>
        </div>
      </div>
    </div>

    <!-- ROADMAP & NEXT STEPS -->
    <div class="grid-2" style="gap:7px;">
      <div class="card" style="margin-bottom:0;">
        <h2><span class="copper-dot"></span> 4-Week Delivery Roadmap</h2>
        <table class="matrix-table">
          <tbody>
            <tr>
              <td><strong>Phase 1 (Days 1&ndash;5)</strong></td>
              <td>Brand translation, design tokens, typography scale &amp; bilingual component layouts.</td>
            </tr>
            <tr>
              <td><strong>Phase 2 (Days 6&ndash;14)</strong></td>
              <td>Frontend build, Webflow/CMS setup, 6 Domains &amp; Insights research repository.</td>
            </tr>
            <tr>
              <td><strong>Phase 3 (Days 15&ndash;18)</strong></td>
              <td>Google Workspace / M365 setup, DNSSEC, SPF, DKIM 2048-bit, and DMARC hardening.</td>
            </tr>
            <tr>
              <td><strong>Phase 4 (Days 19&ndash;24)</strong></td>
              <td>Multilingual QA, cross-device testing, SEO metadata, and editorial handover.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card-dark card-copper-accent" style="margin-bottom:0;">
        <h3 style="font-size:7.5pt; color:var(--copper); margin-bottom:3px; text-transform:uppercase;">Discovery Call &amp; Next Steps</h3>
        <p style="font-size:7pt; line-height:1.38; color:#D4E3EA; margin-bottom:5px;">
          Consistent with sovereign strategic advisory engagements, commercial scope and milestone schedules will be agreed upon during our introductory alignment meeting based on your finalized platform choice (Webflow vs Decoupled) and publication roadmap.
        </p>
        <div style="background:rgba(255,255,255,0.08); padding:5px 7px; border-radius:3px; border:1px solid rgba(255,255,255,0.15);">
          <div style="font-size:6.8pt; color:#FFFFFF; font-weight:700;">Initiate Engagement:</div>
          <div style="font-size:6.5pt; color:#A2BCC9; margin-top:1px;">We are available for an introductory alignment session to review the visual prototypes and confirm the DNS schedule.</div>
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

print(f"Wrote HTML template to {html_path}")

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

print(f"Generated PDF at {pdf_path}")

# Verify total pages with pypdfium2
pdf = pdfium.PdfDocument(pdf_path)
print(f"PDF Page count: {len(pdf)}")
for i in range(len(pdf)):
    text = pdf[i].get_textpage().get_text_range()
    first_line = text.splitlines()[0] if text.splitlines() else "EMPTY"
    print(f"Page {i+1}: {len(text)} chars | First line: {first_line[:50]}")
