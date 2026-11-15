import os
import pypdfium2 as pdfium
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\Viranga\Downloads\upwrok new\Universal_Real_Estate_AI_Digital_Transformation_Proposal"
html_path = os.path.join(output_dir, "proposal_template.html")
pdf_path = os.path.join(output_dir, "Real_Estate_Digital_Transformation_AI_Platform_Proposal.pdf")
img_dir = os.path.join(output_dir, "images")

def get_img_path(name):
    p = os.path.join(img_dir, name)
    return p.replace("\\", "/")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Axiom Global - Real Estate Digital Transformation &amp; AI Platform Proposal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    background-color: #E2E8F0;
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0F172A;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  
  .page {{
    width: 210mm;
    height: 297mm;
    page-break-after: always;
    position: relative;
    background-color: #FFFFFF;
    overflow: hidden;
    padding: 13mm 18mm 11mm 18mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* COLOR PALETTE - MODERN EXECUTIVE SAAS */
  :root {{
    --obsidian: #0F172A;
    --navy-dark: #1E293B;
    --primary: #2563EB;
    --primary-dark: #1D4ED8;
    --primary-light: #EFF6FF;
    --primary-border: #BFDBFE;
    --emerald: #10B981;
    --emerald-light: #ECFDF5;
    --amber: #F59E0B;
    --amber-light: #FFFBEB;
    --slate-text: #334155;
    --slate-light: #64748B;
    --surface-bg: #F8FAFC;
    --card-border: #E2E8F0;
    --white: #FFFFFF;
  }}

  /* COVER PAGE DARK STYLE */
  .page-cover {{
    background: linear-gradient(145deg, #090D16 0%, #0F172A 55%, #1E3A8A 100%);
    color: var(--white);
    padding: 18mm 20mm 15mm 20mm;
  }}

  /* HEADER & FOOTER */
  .page-header {{
    border-bottom: 2px solid var(--primary);
    padding-bottom: 6px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .header-left {{
    font-size: 8.5pt;
    font-weight: 800;
    letter-spacing: 1px;
    color: var(--primary);
    text-transform: uppercase;
  }}
  .header-right {{
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: var(--slate-light);
    text-transform: uppercase;
  }}

  .page-footer {{
    border-top: 1px solid var(--card-border);
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: var(--slate-light);
  }}
  .footer-left strong {{
    color: var(--primary-dark);
    font-weight: 800;
  }}
  .footer-page-num {{
    font-weight: 800;
    color: var(--primary);
    letter-spacing: 0.5px;
    font-size: 7.5pt;
  }}

  /* LARGER, CLEARER, HIGHLY READABLE TYPOGRAPHY */
  .section-tag {{
    display: inline-block;
    font-size: 7.5pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--primary);
    background: var(--primary-light);
    border: 1px solid var(--primary-border);
    padding: 2.5px 8px;
    border-radius: 4px;
    margin-bottom: 4px;
  }}
  .page-title {{
    font-size: 18pt;
    font-weight: 900;
    line-height: 1.15;
    color: var(--obsidian);
    margin-bottom: 6px;
    letter-spacing: -0.4px;
  }}
  .lead-text {{
    font-size: 8.8pt;
    line-height: 1.45;
    color: #334155;
    margin-bottom: 10px;
    font-weight: 500;
  }}
  .body-text {{
    font-size: 8pt;
    line-height: 1.45;
    color: #334155;
  }}
  .block-title {{
    font-size: 10pt;
    font-weight: 800;
    color: var(--obsidian);
    margin-bottom: 4px;
  }}

  /* CARDS & CONTAINERS WITH CRISP VISIBILITY */
  .card {{
    background: var(--surface-bg);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    padding: 10px 14px;
  }}
  .card-bordered {{
    background: var(--white);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    padding: 10px 13px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }}
  .card-highlight {{
    background: linear-gradient(135deg, #EFF6FF 0%, #FFFFFF 100%);
    border: 1.5px solid var(--primary-border);
    border-radius: 6px;
    padding: 10px 14px;
  }}

  /* BOLD INTERACTIVE BADGES */
  .badge {{
    display: inline-block;
    font-size: 6.8pt;
    font-weight: 800;
    text-transform: uppercase;
    padding: 2.5px 7px;
    border-radius: 3px;
    letter-spacing: 0.5px;
  }}
  .badge-blue {{
    background: #EFF6FF;
    color: #1D4ED8;
    border: 1px solid #BFDBFE;
  }}
  .badge-green {{
    background: #ECFDF5;
    color: #047857;
    border: 1px solid #A7F3D0;
  }}
  .badge-amber {{
    background: #FFFBEB;
    color: #B45309;
    border: 1px solid #FDE68A;
  }}
  .badge-dark {{
    background: #0F172A;
    color: #FFFFFF;
  }}

  /* GRIDS */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9px;
  }}
  .grid-4 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 8px;
  }}

  /* CRISP HIGH-CONTRAST TABLES */
  .data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5pt;
  }}
  .data-table th {{
    background: #0F172A;
    color: #FFFFFF;
    text-align: left;
    padding: 6px 9px;
    font-weight: 800;
    text-transform: uppercase;
    font-size: 6.8pt;
    letter-spacing: 0.5px;
  }}
  .data-table td {{
    padding: 6px 9px;
    border-bottom: 1px solid #E2E8F0;
    color: #1E293B;
    line-height: 1.4;
  }}
  .data-table tr:nth-child(even) td {{
    background: #F8FAFC;
  }}

  /* HIGH-FIDELITY CHROME MOCKUP STYLING */
  .mockup-window {{
    background: var(--white);
    border: 1.5px solid #CBD5E1;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08);
  }}
  .mockup-top {{
    background: #F1F5F9;
    border-bottom: 1px solid #CBD5E1;
    padding: 5px 12px;
    display: flex;
    align-items: center;
    gap: 7px;
  }}
  .mockup-dots {{
    display: flex;
    gap: 4px;
  }}
  .mockup-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #EF4444; }}
  .dot-yellow {{ background: #F59E0B; }}
  .dot-green {{ background: #10B981; }}
  
  .mockup-url {{
    background: var(--white);
    border: 1px solid #CBD5E1;
    border-radius: 4px;
    font-size: 6.5pt;
    color: #334155;
    padding: 2px 10px;
    flex: 1;
    max-width: 340px;
    font-weight: 600;
  }}

  .callout-box {{
    background: #F0FDF4;
    border-left: 3.5px solid #10B981;
    padding: 6px 10px;
    border-radius: 0 5px 5px 0;
    font-size: 7.2pt;
    color: #065F46;
    line-height: 1.4;
  }}
</style>
</head>
<body>

<!-- ========================================== PAGE 01: COVER PAGE (AXIOM GLOBAL IDENTITY) ========================================== -->
<div class="page page-cover">
  <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.18); padding-bottom:14px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="width:30px; height:30px; background:#2563EB; border-radius:7px; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:14pt; color:#fff; box-shadow:0 0 12px rgba(37,99,235,0.6);">
        ▲
      </div>
      <div>
        <div style="font-size:10.5pt; font-weight:900; letter-spacing:1.5px; text-transform:uppercase; color:#FFFFFF;">AXIOM GLOBAL</div>
        <div style="font-size:7.2pt; color:#94A3B8; letter-spacing:0.8px;">ENTERPRISE SOFTWARE &amp; AI PLATFORMS</div>
      </div>
    </div>
    <div style="text-align:right;">
      <span class="badge badge-blue" style="background:rgba(37,99,235,0.25); border:1px solid rgba(147,197,253,0.4); color:#93C5FD; font-size:7pt; padding:4px 10px;">CONFIDENTIAL STRATEGIC PROPOSAL</span>
    </div>
  </div>

  <div style="margin: 20mm 0 14mm 0;">
    <span style="font-size:9pt; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#60A5FA; display:block; margin-bottom:8px;">
      EXECUTIVE COMMERCIAL DECK FOR BROKERAGE LEADERSHIP
    </span>
    <h1 style="font-size:33pt; font-weight:900; line-height:1.1; letter-spacing:-0.8px; color:#FFFFFF; margin-bottom:16px;">
      REAL ESTATE DIGITAL<br>TRANSFORMATION &amp;<br><span style="color:#60A5FA;">AI REVENUE ENGINE</span>
    </h1>
    <div style="width:75px; height:4px; background:linear-gradient(90deg, #2563EB, #60A5FA); margin-bottom:16px; border-radius:2px;"></div>
    <p style="font-size:12pt; font-weight:400; line-height:1.55; color:#E2E8F0; max-width:550px;">
      Transforming Traditional Real Estate Websites into High-Converting, 24/7 Intelligent Property Engines with Automated Viewing Scheduling and Lead Acceleration.
    </p>
  </div>

  <!-- Full-Color Hero Image of Luxury Architecture -->
  <div style="border: 1px solid rgba(255,255,255,0.25); border-radius: 8px; overflow: hidden; margin-bottom: 18mm; height: 180px; position:relative; box-shadow:0 10px 30px rgba(0,0,0,0.5);">
    <img src="file:///{get_img_path('luxury_hero.jpg')}" style="width:100%; height:100%; object-fit:cover; display:block;" alt="Modern Architectural Property">
    <div style="position:absolute; bottom:0; left:0; right:0; background:linear-gradient(transparent, rgba(15,23,42,0.95)); padding:12px 18px; display:flex; justify-content:space-between; align-items:flex-end;">
      <div>
        <div style="font-size:8.5pt; font-weight:800; color:#FFFFFF;">Next.js 15 &middot; React 19 &middot; Conversational AI &middot; WhatsApp CRM &middot; Calendar Engine</div>
        <div style="font-size:7pt; color:#CBD5E1; margin-top:2px;">Engineered for Real Estate Brokerages, Agencies &amp; Property Developers</div>
      </div>
      <span class="badge badge-green" style="font-size:7pt; padding:4px 10px;">✓ 24/7 Virtual AI Concierge</span>
    </div>
  </div>

  <!-- Proposal Metadata Grid (With Axiom Global and Viranga Lakshan) -->
  <div style="border-top:1px solid rgba(255,255,255,0.18); padding-top:14px; display:grid; grid-template-columns: 1.2fr 1.1fr 1fr; gap:16px;">
    <div>
      <div style="font-size:7pt; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:#94A3B8; margin-bottom:3px;">TARGET AUDIENCE</div>
      <div style="font-size:10.5pt; font-weight:900; color:#FFFFFF;">[REAL ESTATE AGENCY NAME]</div>
      <div style="font-size:8pt; color:#CBD5E1; margin-top:2px;">Attn: Managing Director / Agency CEO</div>
      <div style="font-size:7.5pt; color:#94A3B8;">[CITY / REGION / COUNTRY]</div>
    </div>

    <div>
      <div style="font-size:7pt; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:#94A3B8; margin-bottom:3px;">PREPARED BY</div>
      <div style="font-size:10.5pt; font-weight:900; color:#60A5FA;">Axiom Global</div>
      <div style="font-size:8pt; color:#FFFFFF; margin-top:2px;">Software Engineering Team – Sri Lanka</div>
      <div style="font-size:7.5pt; color:#CBD5E1;">Lead: Viranga Lakshan &middot; virangalakshanz@gmail.com</div>
    </div>

    <div>
      <div style="font-size:7pt; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:#94A3B8; margin-bottom:3px;">ENGAGEMENT STATUS</div>
      <div style="font-size:10.5pt; font-weight:900; color:#FFFFFF;">Commercial Proposal</div>
      <div style="font-size:8pt; color:#CBD5E1; margin-top:2px;">Date: November 2026</div>
      <div style="font-size:7.5pt; color:#94A3B8;">Phone: +94 71 378 1359</div>
    </div>
  </div>
</div>

<!-- ========================================== PAGE 02: THE STRATEGIC PARADIGM SHIFT ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">01 &middot; Executive Problem &amp; Opportunity</div>
    </div>

    <span class="section-tag">Market Reality &amp; Strategic Opportunity</span>
    <h1 class="page-title">Beyond the Static Website: The 24/7 Digital Booking Machine</h1>
    
    <p class="lead-text">
      Virtually every established real estate brokerage already operates a website. However, the overwhelming majority of existing real estate portals suffer from a critical flaw: <strong>they function merely as passive digital brochures rather than active lead-conversion engines</strong>.
    </p>

    <!-- The 3 Core Pain Points of Standard Real Estate Websites -->
    <div class="grid-3" style="gap:9px; margin-bottom:12px;">
      <div class="card" style="background:#FFF1F2; border-color:#FECDD3;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:8.8pt; color:#9F1239;">68% After-Hours Leakage</strong>
          <span style="font-size:10pt;">⚠️</span>
        </div>
        <p style="font-size:7.6pt; color:#881337; line-height:1.4; margin:0;">
          Over 60% of buyers browse properties on evenings and weekends. Static web forms leave them waiting until Monday morning, by which time they have already contacted a competing agency.
        </p>
      </div>

      <div class="card" style="background:#FFFBEB; border-color:#FDE68A;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:8.8pt; color:#92400E;">Scheduling Friction</strong>
          <span style="font-size:10pt;">⏳</span>
        </div>
        <p style="font-size:7.6pt; color:#78350F; line-height:1.4; margin:0;">
          Coordinating property viewings typically requires 4 to 6 back-and-forth phone calls and emails. High friction leads to abandoned enquiries and double-booking headaches.
        </p>
      </div>

      <div class="card" style="background:#F0FDF4; border-color:#BBF7D0;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:8.8pt; color:#166534;">The AI Multiplier</strong>
          <span style="font-size:10pt;">⚡</span>
        </div>
        <p style="font-size:7.6pt; color:#14532D; line-height:1.4; margin:0;">
          Our platform integrates an intelligent 24/7 Virtual Concierge that understands natural language queries, pre-qualifies buyer finances, and schedules viewings automatically.
        </p>
      </div>
    </div>

    <!-- The 5 Platform Pillars -->
    <div class="card-bordered" style="margin-bottom:12px; padding:12px 16px;">
      <h2 class="block-title" style="font-size:10.5pt; color:var(--primary); margin-bottom:8px;">
        The Five Pillars of Next-Generation Brokerage Software
      </h2>
      <div class="grid-2" style="gap:10px;">
        <div>
          <div style="font-size:8.2pt; font-weight:800; color:var(--obsidian);">1. Interactive Discovery with Sub-Second Speeds</div>
          <p style="font-size:7.4pt; color:var(--slate-text); margin-top:2px;">Modern Next.js 15 SSR architecture with instant faceted search, responsive map clustering, and high-DPI galleries.</p>
        </div>
        <div>
          <div style="font-size:8.2pt; font-weight:800; color:var(--obsidian);">2. 24/7 AI-Powered Property Concierge</div>
          <p style="font-size:7.4pt; color:var(--slate-text); margin-top:2px;">Natural-language assistant pre-qualifying buyer budgets, answering complex property specifications, and booking tours.</p>
        </div>
        <div>
          <div style="font-size:8.2pt; font-weight:800; color:var(--obsidian);">3. Automated Real-Time Viewing Booking</div>
          <p style="font-size:7.4pt; color:var(--slate-text); margin-top:2px;">Direct two-way calendar sync with agent Google/Outlook schedules, automated WhatsApp confirmations, and travel buffer calculation.</p>
        </div>
        <div>
          <div style="font-size:8.2pt; font-weight:800; color:var(--obsidian);">4. Centralized Lead CRM &amp; Broker Dispatch</div>
          <p style="font-size:7.4pt; color:var(--slate-text); margin-top:2px;">Zero lead leakage; omni-channel tracking across web, WhatsApp, and portals with automated broker assignments.</p>
        </div>
      </div>
    </div>

    <!-- Visual Colored Value Flow Diagram -->
    <div class="card-highlight" style="padding:12px 16px;">
      <div style="font-size:7.8pt; font-weight:800; text-transform:uppercase; letter-spacing:1px; color:var(--primary-dark); margin-bottom:8px; text-align:center;">
        End-to-End High-Conversion Lead Pipeline
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; gap:6px;">
        <div style="flex:1; background:#0F172A; color:#FFFFFF; padding:8px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#94A3B8; font-weight:700;">STEP 01</div>
          <div style="font-size:8pt; font-weight:800;">VISITOR ARRIVAL</div>
          <div style="font-size:6.2pt; color:#CBD5E1;">Web &amp; Portals</div>
        </div>
        <span style="font-size:10pt; font-weight:900; color:#2563EB;">→</span>

        <div style="flex:1.2; background:#2563EB; color:#FFFFFF; padding:8px 5px; border-radius:4px; text-align:center; box-shadow:0 3px 8px rgba(37,99,235,0.3);">
          <div style="font-size:6pt; color:#BFDBFE; font-weight:700;">STEP 02</div>
          <div style="font-size:8pt; font-weight:800;">AI ENGAGEMENT</div>
          <div style="font-size:6.2pt; color:#EFF6FF;">24/7 Qualification</div>
        </div>
        <span style="font-size:10pt; font-weight:900; color:#2563EB;">→</span>

        <div style="flex:1.2; background:#FFFFFF; border:1.5px solid #2563EB; color:#0F172A; padding:8px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#2563EB; font-weight:700;">STEP 03</div>
          <div style="font-size:8pt; font-weight:800;">DIRECT BOOKING</div>
          <div style="font-size:6.2pt; color:#475569;">Calendar Sync</div>
        </div>
        <span style="font-size:10pt; font-weight:900; color:#2563EB;">→</span>

        <div style="flex:1.2; background:#ECFDF5; border:1px solid #10B981; color:#065F46; padding:8px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#047857; font-weight:700;">STEP 04</div>
          <div style="font-size:8pt; font-weight:800;">WHATSAPP ALERT</div>
          <div style="font-size:6.2pt; color:#065F46;">Zero No-Shows</div>
        </div>
        <span style="font-size:10pt; font-weight:900; color:#2563EB;">→</span>

        <div style="flex:1; background:#0F172A; color:#FFFFFF; padding:8px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#94A3B8; font-weight:700;">STEP 05</div>
          <div style="font-size:8pt; font-weight:800;">TRANSACTION</div>
          <div style="font-size:6.2pt; color:#CBD5E1;">Offer &amp; Closing</div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 02 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 03: COMPARISON MATRIX & STRATEGIC ADVANTAGES ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">02 &middot; Competitive Differentiation</div>
    </div>

    <span class="section-tag">Value Proposition Analysis</span>
    <h1 class="page-title">Traditional Real Estate Website vs. Intelligent Revenue Engine</h1>
    
    <p class="lead-text">
      The table below demonstrates how transitioning from a legacy real estate website to our integrated, AI-empowered digital platform directly impacts customer acquisition velocity and broker productivity:
    </p>

    <!-- Comprehensive Color Comparison Table -->
    <div style="margin-bottom:12px; border:1.5px solid #CBD5E1; border-radius:6px; overflow:hidden;">
      <table class="data-table">
        <thead>
          <tr>
            <th style="width:24%;">Platform Capability</th>
            <th style="width:38%; background:#334155;">Legacy Real Estate Websites</th>
            <th style="width:38%; background:#1D4ED8;">Axiom NextGen AI Platform</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Buyer Discovery Speed</strong></td>
            <td>Slow page loads; clunky dropdown filters; basic image sliders.</td>
            <td><strong style="color:#2563EB;">Sub-second Next.js SSR</strong> with instant faceted filtering and interactive neighborhood map boundaries.</td>
          </tr>
          <tr>
            <td><strong>After-Hours Lead Capture</strong></td>
            <td>Generic "Contact Us" form; inquiries sit in an inbox until the next business day.</td>
            <td><strong style="color:#10B981;">24/7 AI Property Concierge</strong> answers questions, pre-qualifies budgets, and books viewings instantly.</td>
          </tr>
          <tr>
            <td><strong>Viewing Scheduling</strong></td>
            <td>4–6 manual phone calls or emails back-and-forth to confirm an open agent slot.</td>
            <td><strong style="color:#2563EB;">Automated 2-way calendar booking</strong> with instant Google/Outlook calendar sync and buffer calculations.</td>
          </tr>
          <tr>
            <td><strong>Customer Retention &amp; Alerts</strong></td>
            <td>Manual email replies; frequent viewing no-shows due to lack of reminders.</td>
            <td><strong style="color:#10B981;">Automated WhatsApp &amp; SMS alerts</strong> with Google Maps location pins dispatched 2 hours before viewing.</td>
          </tr>
          <tr>
            <td><strong>Broker Operations &amp; CRM</strong></td>
            <td>Scattered spreadsheets, personal agent phone contacts, and lost buyer histories.</td>
            <td><strong style="color:#2563EB;">Centralized Agency CRM</strong> tracking full client communication histories, preferences, and automated follow-ups.</td>
          </tr>
          <tr>
            <td><strong>Executive Visibility</strong></td>
            <td>End-of-month manual reports with zero visibility into live enquiry pipelines.</td>
            <td><strong style="color:#10B981;">Real-time executive analytics</strong> displaying inventory velocity, days on market, and agent conversion rates.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 3 Core High-Impact Pillars Highlight -->
    <div class="grid-3" style="gap:9px;">
      <div class="card-bordered" style="border-top:3.5px solid #2563EB;">
        <div style="font-size:8.8pt; font-weight:800; color:#1E293B;">3.4x Higher Conversion</div>
        <p class="body-text" style="font-size:7.4pt; margin-top:2px;">
          Immediate response to buyer enquiries within 60 seconds increases viewing appointment booking rates by over 340% compared to next-day email replies.
        </p>
      </div>

      <div class="card-bordered" style="border-top:3.5px solid #10B981;">
        <div style="font-size:8.8pt; font-weight:800; color:#1E293B;">70% Admin Reduction</div>
        <p class="body-text" style="font-size:7.4pt; margin-top:2px;">
          Eliminating phone tag and manual appointment confirmations saves up to 12 administrative hours per agent every single week.
        </p>
      </div>

      <div class="card-bordered" style="border-top:3.5px solid #F59E0B;">
        <div style="font-size:8.8pt; font-weight:800; color:#1E293B;">Direct Buyer Retention</div>
        <p class="body-text" style="font-size:7.4pt; margin-top:2px;">
          Keep high-value buyers directly on your agency website rather than bouncing back to third-party aggregation portals (Funda, Rightmove, Zillow).
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 03 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 04: FULL-COLOR DIGITAL ECOSYSTEM ARCHITECTURE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">03 &middot; System Architecture Blueprint</div>
    </div>

    <span class="section-tag">Modular Enterprise Ecosystem</span>
    <h1 class="page-title">One Unified Platform. Infinite Operational Capabilities.</h1>
    
    <p class="lead-text">
      The architecture is designed as a modular, API-first ecosystem. Public buyer experiences, conversational AI engines, broker operations, and backend databases synchronize instantaneously:
    </p>

    <!-- FULL COLOR ECOSYSTEM ARCHITECTURE DIAGRAM -->
    <div class="card" style="padding:11px 15px; background:#F8FAFC; border:1.5px solid #CBD5E1; margin-bottom:11px;">
      
      <!-- Tier 1: Public Engagement Layer -->
      <div style="background:linear-gradient(90deg, #1E293B, #0F172A); color:#FFFFFF; padding:7px 14px; border-radius:5px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span style="font-size:6.5pt; color:#60A5FA; text-transform:uppercase; font-weight:800;">LAYER 01 &middot; PUBLIC TOUCHPOINT</span>
          <div style="font-size:9pt; font-weight:800;">HIGH-CONVERTING CUSTOMER DISCOVERY WEBSITE</div>
        </div>
        <div style="font-size:7pt; color:#94A3B8;">Next.js 15 &middot; React 19 &middot; Tailwind CSS &middot; Ultra-Fast SSR &middot; SEO Engine</div>
      </div>

      <div style="text-align:center; font-size:8pt; color:#2563EB; line-height:1; margin:3px 0;">▼</div>

      <!-- Tier 2: Real-Time Experience Layer -->
      <div style="background:#FFFFFF; border:2px solid #2563EB; padding:7px 14px; border-radius:5px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 3px 8px rgba(37,99,235,0.1);">
        <div>
          <span style="font-size:6.5pt; color:#2563EB; text-transform:uppercase; font-weight:800;">LAYER 02 &middot; CONVERSION &amp; INTERACTION</span>
          <div style="font-size:9pt; font-weight:800; color:#0F172A;">INTERACTIVE EXPERIENCE &amp; BOOKING ENGINE</div>
        </div>
        <div style="display:flex; gap:5px;">
          <span class="badge badge-blue">Interactive Maps</span>
          <span class="badge badge-green">AI Concierge</span>
          <span class="badge badge-amber">Self-Service Calendar</span>
        </div>
      </div>

      <div style="text-align:center; font-size:8pt; color:#2563EB; line-height:1; margin:3px 0;">▼</div>

      <!-- Tier 3: Core Application Backend -->
      <div style="background:#0F172A; color:#FFFFFF; padding:7px 14px; border-radius:5px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span style="font-size:6.5pt; color:#38BDF8; text-transform:uppercase; font-weight:800;">LAYER 03 &middot; BUSINESS ENGINE</span>
          <div style="font-size:9pt; font-weight:800;">NODE.JS / NESTJS APPLICATION BACKEND &amp; REST APIs</div>
        </div>
        <div style="font-size:7pt; color:#94A3B8;">JWT / OAuth2 Auth &middot; Lead Ingestion Gateway &middot; Workflow Automation &middot; RBAC</div>
      </div>

      <div style="text-align:center; font-size:8pt; color:#2563EB; line-height:1; margin:3px 0;">▼</div>

      <!-- Tier 4: Business Modules Grid -->
      <div style="background:#FFFFFF; border:1px solid #CBD5E1; padding:9px 12px; border-radius:5px;">
        <div style="font-size:6.8pt; color:#475569; text-transform:uppercase; font-weight:800; margin-bottom:6px; text-align:center;">
          LAYER 04 &middot; CENTRALIZED BROKERAGE OPERATIONS MODULES
        </div>
        <div class="grid-4" style="gap:7px;">
          <div style="background:#F1F5F9; padding:6px 8px; border-radius:4px; text-align:center; border:1px solid #E2E8F0;">
            <div style="font-size:7.5pt; font-weight:800; color:#0F172A;">Property Portfolio</div>
            <div style="font-size:6.2pt; color:#475569;">Sales, Rentals, Media</div>
          </div>
          <div style="background:#F1F5F9; padding:6px 8px; border-radius:4px; text-align:center; border:1px solid #E2E8F0;">
            <div style="font-size:7.5pt; font-weight:800; color:#0F172A;">Lead CRM</div>
            <div style="font-size:6.2pt; color:#475569;">Scoring, Pipelines</div>
          </div>
          <div style="background:#F1F5F9; padding:6px 8px; border-radius:4px; text-align:center; border:1px solid #E2E8F0;">
            <div style="font-size:7.5pt; font-weight:800; color:#0F172A;">Viewing Manager</div>
            <div style="font-size:6.2pt; color:#475569;">2-Way Calendar Sync</div>
          </div>
          <div style="background:#F1F5F9; padding:6px 8px; border-radius:4px; text-align:center; border:1px solid #E2E8F0;">
            <div style="font-size:7.5pt; font-weight:800; color:#0F172A;">Agent Dispatch</div>
            <div style="font-size:6.2pt; color:#475569;">Territory Routing</div>
          </div>
        </div>
      </div>

      <div style="text-align:center; font-size:8pt; color:#2563EB; line-height:1; margin:3px 0;">▼</div>

      <!-- Tier 5: Persistence & Third-Party APIs -->
      <div style="background:#EFF6FF; border:1.5px solid #BFDBFE; padding:7px 14px; border-radius:5px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span style="font-size:6.5pt; color:#1D4ED8; text-transform:uppercase; font-weight:800;">LAYER 05 &middot; DATA &amp; INTEGRATIONS</span>
          <div style="font-size:8.2pt; font-weight:800; color:#0F172A;">PostgreSQL Database &amp; Enterprise Connectors</div>
        </div>
        <div style="display:flex; gap:5px; font-size:6.8pt;">
          <span style="background:#fff; padding:2px 7px; border-radius:3px; border:1px solid #BFDBFE; font-weight:700;">Google Maps</span>
          <span style="background:#fff; padding:2px 7px; border-radius:3px; border:1px solid #BFDBFE; font-weight:700;">WhatsApp API</span>
          <span style="background:#fff; padding:2px 7px; border-radius:3px; border:1px solid #BFDBFE; font-weight:700;">Google Calendar</span>
          <span style="background:#fff; padding:2px 7px; border-radius:3px; border:1px solid #BFDBFE; font-weight:700;">OpenAI API</span>
        </div>
      </div>
    </div>

    <!-- Scalability Highlights -->
    <div class="grid-2" style="gap:9px;">
      <div class="card-bordered">
        <strong style="font-size:8.2pt; color:#0F172A;">Seamless MLS &amp; Portal Compatibility</strong>
        <p class="body-text" style="font-size:7.4pt; margin-top:2px;">
          Engineered to import or synchronize listings with industry platforms (e.g., Funda, RealWorks, Pararius, MLS feeds) via automated XML/REST webhook bridges.
        </p>
      </div>
      <div class="card-bordered">
        <strong style="font-size:8.2pt; color:#0F172A;">Bank-Grade Data Privacy &amp; GDPR Compliance</strong>
        <p class="body-text" style="font-size:7.4pt; margin-top:2px;">
          Strict privacy isolation protecting confidential buyer financial qualifications, seller contact details, and internal commission structures.
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 04 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 05: HIGH-FIDELITY COLORED UI MOCKUPS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">04 &middot; Public Website UI Experience</div>
    </div>

    <span class="section-tag">High-Fidelity Interface Concept</span>
    <h1 class="page-title">A Modern Property Discovery Experience in Full Color</h1>
    
    <p class="lead-text" style="margin-bottom:8px;">
      Designed with vibrant, contemporary styling that inspires confidence in prospective luxury and residential buyers while making property discovery effortless across all devices:
    </p>

    <!-- 3 COLORED MOCKUPS STACK WITH LARGER CRISP FONTS -->
    <div style="display:flex; flex-direction:column; gap:8px;">
      
      <!-- Mockup 1: Modern Real Estate Homepage -->
      <div class="mockup-window">
        <div class="mockup-top">
          <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
          <div class="mockup-url">https://www.youragency.com/ — Modern Brokerage Homepage</div>
          <span class="badge badge-blue" style="margin-left:auto; font-size:6pt;">DESKTOP VIEW</span>
        </div>
        <div style="padding:7px 12px; background:#FAFAFA;">
          <!-- Navbar -->
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0; padding-bottom:5px; margin-bottom:6px;">
            <div style="font-size:8.5pt; font-weight:900; color:#0F172A; display:flex; align-items:center; gap:5px;">
              <span style="color:#2563EB; font-size:11pt;">▲</span> [REAL ESTATE AGENCY]
            </div>
            <div style="display:flex; gap:10px; font-size:6.5pt; font-weight:700; text-transform:uppercase; color:#334155;">
              <span style="color:#2563EB; font-weight:800;">Properties</span>
              <span>Buying</span>
              <span>Selling</span>
              <span>Valuations</span>
              <span>About</span>
              <span style="background:#2563EB; color:#fff; padding:2px 8px; border-radius:3px;">Book Viewing</span>
            </div>
          </div>
          <!-- Hero Section inside Mockup -->
          <div style="display:flex; gap:10px; align-items:center;">
            <div style="flex:1.2;">
              <span class="badge badge-blue" style="font-size:5.8pt; margin-bottom:2px;">Prime Residential &amp; Luxury Real Estate</span>
              <div style="font-size:11pt; font-weight:900; line-height:1.2; color:#0F172A; margin:2px 0 5px 0;">Find Your Next Home With Confidence</div>
              <!-- Colored Search Form Bar -->
              <div style="background:#FFFFFF; border:1.5px solid #2563EB; border-radius:5px; padding:4px 8px; display:flex; gap:6px; align-items:center; box-shadow:0 2px 6px rgba(37,99,235,0.12);">
                <span style="font-size:6.5pt; color:#2563EB; font-weight:800;">Buy ▼</span>
                <span style="font-size:6.5pt; color:#CBD5E1;">|</span>
                <span style="font-size:6.5pt; color:#334155; flex:1; font-weight:500;">Search city, neighborhood, postal code...</span>
                <span style="font-size:6.5pt; color:#64748B;">Price: €300k–€800k ▼</span>
                <span style="background:#2563EB; color:#fff; font-size:6.5pt; font-weight:800; padding:3px 10px; border-radius:3px;">Search</span>
              </div>
            </div>
            <!-- Full Color Photo -->
            <div style="flex:0.8; height:58px; border-radius:5px; overflow:hidden; border:1px solid #CBD5E1;">
              <img src="file:///{get_img_path('prop_modern.jpg')}" style="width:100%; height:100%; object-fit:cover;" alt="Modern Property">
            </div>
          </div>
        </div>
      </div>

      <!-- Mockup 2: Faceted Search & Listing Grid -->
      <div class="mockup-window">
        <div class="mockup-top">
          <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
          <div class="mockup-url">https://www.youragency.com/properties?filter=residential — Faceted Search</div>
          <span class="badge badge-green" style="margin-left:auto; font-size:6pt;">LIVE SEARCH ENGINE</span>
        </div>
        <div style="padding:7px 12px; background:#FFFFFF; display:flex; gap:10px;">
          <!-- Filter Sidebar -->
          <div style="width:135px; border-right:1px solid #E2E8F0; padding-right:8px;">
            <div style="font-size:6.8pt; font-weight:800; color:#0F172A; text-transform:uppercase; margin-bottom:4px;">Refine Listings (48 Active)</div>
            <div style="font-size:6.2pt; color:#334155; margin-bottom:3px;"><strong style="color:#2563EB;">Type:</strong> [x] Villa  [x] Townhouse</div>
            <div style="font-size:6.2pt; color:#334155; margin-bottom:3px;"><strong style="color:#2563EB;">Price:</strong> €350,000 – €950,000</div>
            <div style="font-size:6.2pt; color:#334155; margin-bottom:3px;"><strong style="color:#2563EB;">Bedrooms:</strong> 3+ Rooms</div>
            <div style="font-size:6.2pt; margin-bottom:4px;">
              <span class="badge badge-green" style="font-size:5.5pt;">Label A+</span>
              <span class="badge badge-green" style="font-size:5.5pt;">Label A</span>
            </div>
            <div style="font-size:6.2pt; background:#2563EB; color:#fff; text-align:center; padding:3px; border-radius:3px; font-weight:800;">Apply Filters</div>
          </div>
          <!-- Colored Listing Cards Grid -->
          <div style="flex:1; display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <!-- Property 1 -->
            <div style="border:1px solid #E2E8F0; border-radius:5px; padding:4px; display:flex; gap:6px; align-items:center; background:#FAFAFA;">
              <img src="file:///{get_img_path('prop_villa.jpg')}" style="width:54px; height:42px; object-fit:cover; border-radius:4px;" alt="Villa">
              <div>
                <span class="badge badge-green" style="font-size:5pt;">New Listing</span>
                <div style="font-size:6.8pt; font-weight:800; color:#0F172A;">Prins Hendriklaan 28</div>
                <div style="font-size:6.8pt; color:#2563EB; font-weight:900;">€ 685.000 k.k.</div>
                <div style="font-size:5.8pt; color:#64748B;">175 m² &middot; 4 beds &middot; Energy A</div>
              </div>
            </div>
            <!-- Property 2 -->
            <div style="border:1px solid #E2E8F0; border-radius:5px; padding:4px; display:flex; gap:6px; align-items:center; background:#FAFAFA;">
              <img src="file:///{get_img_path('prop_townhouse.jpg')}" style="width:54px; height:42px; object-fit:cover; border-radius:4px;" alt="Townhouse">
              <div>
                <span class="badge badge-amber" style="font-size:5pt;">Under Offer</span>
                <div style="font-size:6.8pt; font-weight:800; color:#0F172A;">Westerweg 104</div>
                <div style="font-size:6.8pt; color:#2563EB; font-weight:900;">€ 425.000 k.k.</div>
                <div style="font-size:5.8pt; color:#64748B;">132 m² &middot; 3 beds &middot; Energy B</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Mockup 3: High-Converting Property Detail Page -->
      <div class="mockup-window">
        <div class="mockup-top">
          <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
          <div class="mockup-url">https://www.youragency.com/properties/villa-alkmaar-hout — Property Showcase</div>
          <span class="badge badge-blue" style="margin-left:auto; font-size:6pt;">CONVERSION PAGE</span>
        </div>
        <div style="padding:7px 12px; background:#FAFAFA; display:flex; gap:10px;">
          <!-- Gallery & Description -->
          <div style="flex:1.4;">
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
              <div>
                <div style="font-size:8.5pt; font-weight:900; color:#0F172A;">Villa Alkmaarderhout &middot; Park Residence</div>
                <div style="font-size:6.8pt; color:#64748B;">Prestigious residential boulevard bordering city parklands</div>
              </div>
              <div style="font-size:9.5pt; font-weight:900; color:#2563EB;">€ 795.000 k.k.</div>
            </div>
            <div style="display:flex; gap:5px; margin-top:4px;">
              <span class="badge badge-blue">210 m² Living Space</span>
              <span class="badge badge-blue">5 Bedrooms</span>
              <span class="badge badge-green">Energy Label A+++</span>
              <span class="badge badge-amber">Private Garden</span>
            </div>
            <p style="font-size:6.5pt; color:#475569; margin-top:4px; line-height:1.35;">
              Exceptional detached residence fully renovated with sustainable heat-pump heating, premium kitchen, and landscaped south-facing terrace. Walking distance to center.
            </p>
          </div>
          <!-- Embedded Booking Form -->
          <div style="flex:0.8; background:#FFFFFF; border:1.5px solid #2563EB; border-radius:5px; padding:5px 8px; box-shadow:0 2px 6px rgba(37,99,235,0.1);">
            <div style="font-size:6.8pt; font-weight:800; color:#1D4ED8; text-transform:uppercase;">📅 Schedule Viewing</div>
            <div style="font-size:5.8pt; color:#64748B; margin-bottom:3px;">Select your preferred viewing date:</div>
            <div style="display:flex; gap:3px; margin-bottom:4px;">
              <span style="background:#2563EB; color:#fff; font-size:5.5pt; padding:2px 5px; border-radius:2px; font-weight:800;">Tue 18 Nov</span>
              <span style="background:#EFF6FF; color:#1D4ED8; font-size:5.5pt; padding:2px 5px; border-radius:2px;">Wed 19 Nov</span>
              <span style="background:#EFF6FF; color:#1D4ED8; font-size:5.5pt; padding:2px 5px; border-radius:2px;">Thu 20 Nov</span>
            </div>
            <div style="font-size:6pt; background:#10B981; color:#fff; text-align:center; padding:3px; border-radius:3px; font-weight:800;">✓ Confirm Viewing Slot</div>
            <div style="font-size:5.2pt; color:#64748B; text-align:center; margin-top:3px;">Instant WhatsApp &amp; Calendar Confirmation</div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 05 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 06: AUTOMATED VIEWING & CALENDAR ENGINE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">05 &middot; Viewing &amp; Calendar Logistics</div>
    </div>

    <span class="section-tag">Zero-Friction Scheduling Engine</span>
    <h1 class="page-title">Automating Property Viewings &amp; Eliminating Phone Tag</h1>
    
    <p class="lead-text">
      The most common bottleneck for real estate brokers is coordinating property viewings. Our automated scheduling engine eliminates phone tag, coordinates agent availability in real time, and sends instant multi-channel confirmations:
    </p>

    <!-- Key Scheduling Features Grid -->
    <div class="grid-4" style="gap:7px; margin-bottom:9px;">
      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #2563EB;">
        <strong style="font-size:7.5pt; color:#0F172A;">2-Way Calendar Sync</strong>
        <p style="font-size:6.8pt; color:#475569; margin-top:2px;">Live synchronization with Google Calendar &amp; Microsoft Outlook.</p>
      </div>
      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #10B981;">
        <strong style="font-size:7.5pt; color:#0F172A;">Automated Travel Buffer</strong>
        <p style="font-size:6.8pt; color:#475569; margin-top:2px;">Automatic 20-minute travel buffers calculated between property viewings.</p>
      </div>
      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #F59E0B;">
        <strong style="font-size:7.5pt; color:#0F172A;">WhatsApp Confirmation</strong>
        <p style="font-size:6.8pt; color:#475569; margin-top:2px;">Automated 24h &amp; 2h WhatsApp reminders with Google Map navigation pin.</p>
      </div>
      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #8B5CF6;">
        <strong style="font-size:7.5pt; color:#0F172A;">Seller Notification</strong>
        <p style="font-size:6.8pt; color:#475569; margin-top:2px;">Instant SMS/email alert to homeowners when a new viewing is booked.</p>
      </div>
    </div>

    <!-- FULL COLOR CALENDAR UI MOCKUP -->
    <div class="mockup-window" style="margin-bottom:9px;">
      <div class="mockup-top">
        <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
        <div class="mockup-url">https://admin.youragency.com/calendar — Real-Time Agent Schedule</div>
        <span class="badge badge-blue" style="margin-left:auto; font-size:6pt;">BROKER CALENDAR MOCKUP</span>
      </div>

      <div style="padding:9px 12px; background:#FAFAFA;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
          <div>
            <strong style="font-size:8pt; color:#0F172A;">Viewing Schedule &middot; Nov 17 – Nov 21, 2026</strong>
            <span style="font-size:6.5pt; color:#2563EB; font-weight:800; margin-left:6px;">Broker: Lead Real Estate Agent</span>
          </div>
          <div style="display:flex; gap:4px;">
            <span class="badge badge-dark">Week View</span>
            <span class="badge badge-blue">Sync: Google Active</span>
          </div>
        </div>

        <!-- Colored Calendar Week Grid -->
        <div style="display:grid; grid-template-columns: 50px repeat(5, 1fr); gap:4px; background:#FFFFFF; border:1px solid #CBD5E1; padding:5px; border-radius:4px; font-size:6.5pt;">
          <!-- Header Days -->
          <div style="font-weight:800; color:#64748B; text-align:center;">Time</div>
          <div style="font-weight:800; text-align:center; background:#F1F5F9; padding:3px;">Mon 17</div>
          <div style="font-weight:800; text-align:center; background:#2563EB; color:#fff; padding:3px; border-radius:3px;">Tue 18 (Today)</div>
          <div style="font-weight:800; text-align:center; background:#F1F5F9; padding:3px;">Wed 19</div>
          <div style="font-weight:800; text-align:center; background:#F1F5F9; padding:3px;">Thu 20</div>
          <div style="font-weight:800; text-align:center; background:#F1F5F9; padding:3px;">Fri 21</div>

          <!-- Slot 1 -->
          <div style="color:#64748B; text-align:center; padding:4px 0; font-weight:700;">09:30</div>
          <div style="background:#F8FAFC; border-left:2px solid #CBD5E1; padding:3px;">Team Briefing</div>
          <div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:3px; font-weight:800; color:#1E40AF;">
            Prins Hendriklaan 28<br><span style="font-size:5.5pt; color:#475569;">Client: De Vries</span>
          </div>
          <div style="background:#F8FAFC; padding:3px; color:#94A3B8;">Open Slot</div>
          <div style="background:#FEF3C7; border-left:3px solid #F59E0B; padding:3px; font-weight:800; color:#92400E;">
            Valuation Visit<br><span style="font-size:5.5pt; color:#475569;">Owner: Bakker</span>
          </div>
          <div style="background:#F8FAFC; padding:3px; color:#94A3B8;">Open Slot</div>

          <!-- Slot 2 -->
          <div style="color:#64748B; text-align:center; padding:4px 0; font-weight:700;">11:30</div>
          <div style="background:#F8FAFC; padding:3px; color:#94A3B8;">Open Slot</div>
          <div style="background:#FEF2F2; padding:3px; color:#991B1B; font-weight:700;">Travel Buffer (20m)</div>
          <div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:3px; font-weight:800; color:#1E40AF;">
            Westerweg 104<br><span style="font-size:5.5pt; color:#475569;">Client: Jansen</span>
          </div>
          <div style="background:#F8FAFC; padding:3px; color:#94A3B8;">Open Slot</div>
          <div style="background:#ECFDF5; border-left:3px solid #10B981; padding:3px; font-weight:800; color:#065F46;">
            Park Residence<br><span style="font-size:5.5pt; color:#475569;">Client: Schmidt</span>
          </div>

          <!-- Slot 3 -->
          <div style="color:#64748B; text-align:center; padding:4px 0; font-weight:700;">14:30</div>
          <div style="background:#F1F5F9; border-left:2px solid #64748B; padding:3px;">Notary Closing</div>
          <div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:3px; font-weight:800; color:#1E40AF;">
            Villa Alkmaarderhout<br><span style="font-size:5.5pt; color:#475569;">2nd Viewing: Van Dijk</span>
          </div>
          <div style="background:#F8FAFC; padding:3px; color:#94A3B8;">Open Slot</div>
          <div style="background:#EFF6FF; border-left:3px solid #2563EB; padding:3px; font-weight:800; color:#1E40AF;">
            City Center Loft<br><span style="font-size:5.5pt; color:#475569;">Buyer Group (3)</span>
          </div>
          <div style="background:#F1F5F9; padding:3px;">Weekly Wrap-Up</div>
        </div>
      </div>
    </div>

    <!-- Communication Dispatch Pipeline Callout -->
    <div class="callout-box">
      <strong>Zero No-Show Guarantee:</strong> Prospective buyers receive an instant Google/Outlook calendar invite with property details upon booking, followed by an automated WhatsApp reminder with a 1-click Google Maps pin 2 hours prior to arrival. No-shows are reduced by over 82%.
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 06 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 07: 24/7 AI-POWERED PROPERTY CONCIERGE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">06 &middot; Artificial Intelligence Concierge</div>
    </div>

    <span class="section-tag">Conversational Revenue Engine</span>
    <h1 class="page-title">24/7 Virtual Property Concierge: An Intelligent Sales Assistant</h1>
    
    <p class="lead-text">
      Capture, qualify, and convert buyers at 11:00 PM while your agency sleeps. Our conversational AI assistant understands natural-language property criteria, verifies budget qualifications, and arranges viewings in seconds:
    </p>

    <!-- 3 Core AI Pillars -->
    <div class="grid-3" style="gap:8px; margin-bottom:9px;">
      <div class="card-bordered" style="padding:8px 10px; border-top:3px solid #2563EB;">
        <strong style="font-size:7.8pt; color:#0F172A;">Natural Language Parsing</strong>
        <p class="body-text" style="font-size:7.2pt; margin-top:2px;">
          Understands natural phrasings (e.g. <em>"family home with garden near good schools under €700k"</em>) and instantly filters the live database.
        </p>
      </div>
      <div class="card-bordered" style="padding:8px 10px; border-top:3px solid #10B981;">
        <strong style="font-size:7.8pt; color:#0F172A;">Financial Pre-Qualification</strong>
        <p class="body-text" style="font-size:7.2pt; margin-top:2px;">
          Politely verifies whether the buyer has mortgage pre-approval, deposit availability, and exact moving timeline.
        </p>
      </div>
      <div class="card-bordered" style="padding:8px 10px; border-top:3px solid #8B5CF6;">
        <strong style="font-size:7.8pt; color:#0F172A;">Multilingual Communication</strong>
        <p class="body-text" style="font-size:7.2pt; margin-top:2px;">
          Engages high-net-worth expat and international buyers seamlessly in English, Dutch, German, French, and Spanish.
        </p>
      </div>
    </div>

    <!-- FULL COLOR AI CONVERSATIONAL UI MOCKUP -->
    <div class="mockup-window" style="margin-bottom:9px;">
      <div class="mockup-top">
        <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
        <div class="mockup-url">https://www.youragency.com/ — 24/7 AI Virtual Broker Assistant</div>
        <span class="badge badge-green" style="margin-left:auto; font-size:6pt;">● LIVE BOT ONLINE</span>
      </div>

      <div style="padding:9px 14px; background:#F8FAFC; display:flex; justify-content:center;">
        <!-- Chat Container -->
        <div style="width:100%; max-width:460px; background:#FFFFFF; border:1px solid #CBD5E1; border-radius:7px; overflow:hidden; box-shadow:0 3px 10px rgba(0,0,0,0.08);">
          <!-- Chat Header -->
          <div style="background:linear-gradient(90deg, #1E293B, #0F172A); color:#FFFFFF; padding:7px 12px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; gap:7px; align-items:center;">
              <div style="width:9px; height:9px; border-radius:50%; background:#10B981; box-shadow:0 0 7px #10B981;"></div>
              <div>
                <div style="font-size:7.5pt; font-weight:800;">Virtual Property Concierge</div>
                <div style="font-size:5.8pt; color:#94A3B8;">[REAL ESTATE AGENCY] &middot; Instant 24/7 Assistant</div>
              </div>
            </div>
            <span class="badge badge-blue" style="font-size:5.5pt;">GPT-4 Powered</span>
          </div>

          <!-- Chat Dialog Body -->
          <div style="padding:9px 12px; display:flex; flex-direction:column; gap:6px; font-size:7.2pt; min-height:125px;">
            <!-- Buyer 1 -->
            <div style="align-self:flex-end; background:#2563EB; color:#FFFFFF; padding:6px 9px; border-radius:6px 6px 1px 6px; max-width:80%;">
              "I'm looking for a two-bedroom apartment or townhouse under €400,000."
            </div>

            <!-- AI 1 -->
            <div style="align-self:flex-start; background:#F1F5F9; color:#0F172A; padding:6px 9px; border-radius:6px 6px 6px 1px; max-width:85%; border:1px solid #E2E8F0;">
              "Certainly! I have 3 properties matching your criteria in prime locations. Are you seeking a property ready to move into, or are you open to renovation?"
            </div>

            <!-- Buyer 2 -->
            <div style="align-self:flex-end; background:#2563EB; color:#FFFFFF; padding:6px 9px; border-radius:6px 6px 1px 6px; max-width:80%;">
              "Move-in ready with an energy rating of A or B."
            </div>

            <!-- AI 2 with Property Card Preview -->
            <div style="align-self:flex-start; background:#F1F5F9; color:#0F172A; padding:7px 9px; border-radius:6px 6px 6px 1px; max-width:90%; border:1px solid #E2E8F0;">
              "Excellent! Here is a top match: <strong>Kanaalkade 88-B (€295,000, 2 beds, Energy Label B)</strong>. Would you like to schedule an in-person viewing with our listing broker this week?"
              <div style="margin-top:5px; display:flex; gap:5px;">
                <span style="background:#10B981; color:#fff; font-size:6.2pt; padding:3px 8px; border-radius:3px; font-weight:800;">📅 Book Viewing (Tue 14:00)</span>
                <span style="background:#fff; color:#2563EB; border:1px solid #BFDBFE; font-size:6.2pt; padding:3px 8px; border-radius:3px; font-weight:700;">View Full Specs</span>
              </div>
            </div>
          </div>

          <!-- Chat Input -->
          <div style="border-top:1px solid #E2E8F0; padding:5px 10px; background:#FFFFFF; display:flex; gap:5px;">
            <input type="text" placeholder="Type your property question..." style="flex:1; border:1px solid #CBD5E1; border-radius:4px; font-size:6.8pt; padding:3px 8px;" readonly>
            <span style="background:#2563EB; color:#fff; font-size:6.2pt; padding:3px 8px; border-radius:3px; font-weight:800;">Send</span>
          </div>
        </div>
      </div>
    </div>

    <div class="callout-box" style="background:#EFF6FF; border-color:#2563EB; color:#1E40AF;">
      <strong>Smart Escalation to Human Agents:</strong> When a prospective buyer indicates urgent buying power or requests a valuation, the AI concierge automatically transfers the live chat to the on-call broker's mobile phone via instant WhatsApp push notification.
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 07 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 08: BROKERAGE CRM & LEAD PIPELINE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">07 &middot; Customer CRM &amp; Lead Acceleration</div>
    </div>

    <span class="section-tag">Brokerage Operational Command</span>
    <h1 class="page-title">Turn Enquiries into Transactions with Centralized CRM</h1>
    
    <p class="lead-text">
      A real estate enquiry is only as valuable as the speed and discipline with which it is pursued. Our integrated CRM tracks every prospective buyer and seller across a structured visual pipeline:
    </p>

    <!-- SAMPLE PIPELINE VISUAL -->
    <div class="card-bordered" style="padding:9px 14px; margin-bottom:9px; background:#FFFFFF;">
      <div style="font-size:7pt; font-weight:800; text-transform:uppercase; letter-spacing:0.8px; color:#0F172A; margin-bottom:7px; text-align:center;">
        Automated Deal Progression Pipeline (Sample Flow)
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; gap:5px;">
        <div style="flex:1; background:#0F172A; color:#FFFFFF; padding:7px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#94A3B8; text-transform:uppercase;">STAGE 01</div>
          <div style="font-size:7.8pt; font-weight:800;">NEW LEAD</div>
          <div style="font-size:6pt; color:#CBD5E1;">Captured (48)</div>
        </div>
        <span style="font-size:9pt; font-weight:900; color:#2563EB;">→</span>
        <div style="flex:1; background:#1E3A8A; color:#FFFFFF; padding:7px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#93C5FD; text-transform:uppercase;">STAGE 02</div>
          <div style="font-size:7.8pt; font-weight:800;">CONTACTED</div>
          <div style="font-size:6pt; color:#DBEAFE;">In Dialog (32)</div>
        </div>
        <span style="font-size:9pt; font-weight:900; color:#2563EB;">→</span>
        <div style="flex:1; background:#2563EB; color:#FFFFFF; padding:7px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#BFDBFE; text-transform:uppercase;">STAGE 03</div>
          <div style="font-size:7.8pt; font-weight:800;">QUALIFIED</div>
          <div style="font-size:6pt; color:#EFF6FF;">Budget Verified (22)</div>
        </div>
        <span style="font-size:9pt; font-weight:900; color:#2563EB;">→</span>
        <div style="flex:1.2; background:#10B981; color:#FFFFFF; padding:7px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#A7F3D0; text-transform:uppercase;">STAGE 04</div>
          <div style="font-size:7.8pt; font-weight:800;">VIEWING BOOKED</div>
          <div style="font-size:6pt; color:#ECFDF5;">On Calendar (14)</div>
        </div>
        <span style="font-size:9pt; font-weight:900; color:#10B981;">→</span>
        <div style="flex:1; background:#0F172A; color:#FFFFFF; padding:7px 5px; border-radius:4px; text-align:center;">
          <div style="font-size:6pt; color:#94A3B8; text-transform:uppercase;">STAGE 05</div>
          <div style="font-size:7.8pt; font-weight:800;">OFFER / CLOSING</div>
          <div style="font-size:6pt; color:#CBD5E1;">Notary Phase (8)</div>
        </div>
      </div>
    </div>

    <!-- FULL COLOR CRM TABLE MOCKUP -->
    <div class="mockup-window" style="margin-bottom:8px;">
      <div class="mockup-top">
        <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
        <div class="mockup-url">https://admin.youragency.com/crm/leads — Lead Pipeline Command</div>
        <span class="badge badge-blue" style="margin-left:auto; font-size:6pt;">AGENCY CRM</span>
      </div>

      <div style="padding:7px 12px; background:#FAFAFA;">
        <table style="width:100%; border-collapse:collapse; font-size:6.6pt; background:#FFFFFF; border:1px solid #CBD5E1; border-radius:4px; overflow:hidden;">
          <thead>
            <tr style="background:#0F172A; color:#FFFFFF;">
              <th style="padding:5px 7px; text-align:left;">Client Name</th>
              <th style="padding:5px 7px; text-align:left;">Target Property</th>
              <th style="padding:5px 7px; text-align:left;">Budget</th>
              <th style="padding:5px 7px; text-align:left;">Acquisition Source</th>
              <th style="padding:5px 7px; text-align:left;">Assigned Broker</th>
              <th style="padding:5px 7px; text-align:left;">Pipeline Status</th>
              <th style="padding:5px 7px; text-align:right;">Next Follow-Up</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid #E2E8F0;">
              <td style="padding:5px 7px; font-weight:800; color:#0F172A;">Dhr. Mark van Dijk</td>
              <td style="padding:5px 7px;">Villa Alkmaarderhout</td>
              <td style="padding:5px 7px; font-weight:800; color:#2563EB;">€ 800.000</td>
              <td style="padding:5px 7px;"><span class="badge badge-blue">AI Concierge</span></td>
              <td style="padding:5px 7px;">Senior Broker A</td>
              <td style="padding:5px 7px;"><span class="badge badge-green">Viewing Booked</span></td>
              <td style="padding:5px 7px; text-align:right; font-weight:800;">Tue 18 Nov &middot; 14:00</td>
            </tr>
            <tr style="border-bottom:1px solid #E2E8F0; background:#F8FAFC;">
              <td style="padding:5px 7px; font-weight:800; color:#0F172A;">Mevr. Sophie Bakker</td>
              <td style="padding:5px 7px;">Kanaalkade 88-B</td>
              <td style="padding:5px 7px; font-weight:800; color:#2563EB;">€ 320.000</td>
              <td style="padding:5px 7px;"><span class="badge badge-green">WhatsApp Direct</span></td>
              <td style="padding:5px 7px;">Associate Broker B</td>
              <td style="padding:5px 7px;"><span class="badge badge-blue">Qualified Lead</span></td>
              <td style="padding:5px 7px; text-align:right; font-weight:800;">Send Contract Draft</td>
            </tr>
            <tr style="border-bottom:1px solid #E2E8F0;">
              <td style="padding:5px 7px; font-weight:800; color:#0F172A;">Dhr. Lars de Boer</td>
              <td style="padding:5px 7px;">Westerweg 104</td>
              <td style="padding:5px 7px; font-weight:800; color:#2563EB;">€ 450.000</td>
              <td style="padding:5px 7px;"><span class="badge badge-blue">Website Form</span></td>
              <td style="padding:5px 7px;">Senior Broker A</td>
              <td style="padding:5px 7px;"><span class="badge badge-amber">Under Negotiation</span></td>
              <td style="padding:5px 7px; text-align:right; font-weight:800;">Review Counter-Offer</td>
            </tr>
            <tr>
              <td style="padding:5px 7px; font-weight:800; color:#0F172A;">Familie Visser</td>
              <td style="padding:5px 7px;">Free Valuation Request</td>
              <td style="padding:5px 7px; font-weight:800; color:#2563EB;">Seller Lead</td>
              <td style="padding:5px 7px;"><span class="badge badge-blue">Valuation Tool</span></td>
              <td style="padding:5px 7px;">Agency Director</td>
              <td style="padding:5px 7px;"><span class="badge badge-green">Appraisal Booked</span></td>
              <td style="padding:5px 7px; text-align:right; font-weight:800;">Home Visit Thu 10:00</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Core Lead Acceleration Features -->
    <div class="grid-3" style="gap:8px;">
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Automated Seller Valuations</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">Online appraisal request tool instantly generating leads from property owners seeking to sell their homes.</p>
      </div>
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Client Preference Memory</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">When a new listing enters the portfolio, matching buyers in the CRM are alerted automatically via WhatsApp.</p>
      </div>
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Broker Accountability</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">Management dashboards track agent response times and milestone progression from lead creation to deal closing.</p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 08 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 09: BACK-OFFICE INVENTORY & AGENT MANAGEMENT ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">08 &middot; Back-Office Operations</div>
    </div>

    <span class="section-tag">Enterprise Portfolio Control</span>
    <h1 class="page-title">Simplifying Property Portfolio and Multi-Agent Operations</h1>
    
    <p class="lead-text">
      Manage active sales, rental agreements, commercial portfolios, and multi-agent workloads with an intuitive, cloud-based back-office portal designed for administrative speed and compliance:
    </p>

    <!-- FULL COLOR ADMIN DASHBOARD MOCKUP -->
    <div class="mockup-window" style="margin-bottom:9px;">
      <div class="mockup-top">
        <div class="mockup-dots"><div class="mockup-dot dot-red"></div><div class="mockup-dot dot-yellow"></div><div class="mockup-dot dot-green"></div></div>
        <div class="mockup-url">https://admin.youragency.com/portfolio — Back-Office Portfolio Management</div>
        <span class="badge badge-dark" style="margin-left:auto; font-size:6pt;">ADMIN COMMAND</span>
      </div>

      <div style="padding:9px 13px; background:#FAFAFA;">
        <!-- KPI Row with Colors -->
        <div class="grid-4" style="gap:7px; margin-bottom:9px;">
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:3.5px solid #2563EB; padding:6px 9px; border-radius:5px;">
            <div style="font-size:6pt; color:#64748B; text-transform:uppercase; font-weight:800;">Total Inventory</div>
            <div style="font-size:13pt; font-weight:900; color:#0F172A;">54</div>
            <div style="font-size:5.5pt; color:#2563EB; font-weight:700;">38 Residential &middot; 16 Commercial</div>
          </div>
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:3.5px solid #F59E0B; padding:6px 9px; border-radius:5px;">
            <div style="font-size:6pt; color:#64748B; text-transform:uppercase; font-weight:800;">Under Offer</div>
            <div style="font-size:13pt; font-weight:900; color:#D97706;">14</div>
            <div style="font-size:5.5pt; color:#B45309; font-weight:700;">€ 8.4M Pending Volume</div>
          </div>
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:3.5px solid #10B981; padding:6px 9px; border-radius:5px;">
            <div style="font-size:6pt; color:#64748B; text-transform:uppercase; font-weight:800;">Viewings This Week</div>
            <div style="font-size:13pt; font-weight:900; color:#059669;">29</div>
            <div style="font-size:5.5pt; color:#047857; font-weight:700;">+24% vs Last Week</div>
          </div>
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:3.5px solid #8B5CF6; padding:6px 9px; border-radius:5px;">
            <div style="font-size:6pt; color:#64748B; text-transform:uppercase; font-weight:800;">Avg. Days on Market</div>
            <div style="font-size:13pt; font-weight:900; color:#7C3AED;">19</div>
            <div style="font-size:5.5pt; color:#6D28D9; font-weight:700;">Industry Avg: 34 Days</div>
          </div>
        </div>

        <!-- Property Management Table -->
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:5px; overflow:hidden;">
          <div style="padding:5px 9px; background:#F1F5F9; font-size:6.8pt; font-weight:800; color:#0F172A; display:flex; justify-content:space-between; align-items:center;">
            <span>ACTIVE PROPERTIES (PORTFOLIO CONTROL)</span>
            <span style="background:#2563EB; color:#fff; font-size:6pt; padding:2px 7px; border-radius:3px; font-weight:800;">+ New Listing</span>
          </div>
          <table style="width:100%; border-collapse:collapse; font-size:6.6pt;">
            <thead>
              <tr style="border-bottom:1px solid #E2E8F0; background:#F8FAFC;">
                <th style="padding:4px 7px; text-align:left;">Address &amp; Specification</th>
                <th style="padding:4px 7px; text-align:left;">Category</th>
                <th style="padding:4px 7px; text-align:left;">Asking Price</th>
                <th style="padding:4px 7px; text-align:left;">Assigned Agent</th>
                <th style="padding:4px 7px; text-align:left;">Status</th>
                <th style="padding:4px 7px; text-align:right;">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #E2E8F0;">
                <td style="padding:4px 7px; font-weight:800; color:#0F172A;">Prins Hendriklaan 28</td>
                <td style="padding:4px 7px;">Villa (175 m²)</td>
                <td style="padding:4px 7px; font-weight:800; color:#2563EB;">€ 685.000</td>
                <td style="padding:4px 7px;">Senior Broker A</td>
                <td style="padding:4px 7px;"><span class="badge badge-green">Available</span></td>
                <td style="padding:4px 7px; text-align:right; font-weight:800; color:#2563EB;">Edit &middot; View</td>
              </tr>
              <tr style="border-bottom:1px solid #E2E8F0; background:#F8FAFC;">
                <td style="padding:4px 7px; font-weight:800; color:#0F172A;">Kanaalkade 88-B</td>
                <td style="padding:4px 7px;">Apartment (88 m²)</td>
                <td style="padding:4px 7px; font-weight:800; color:#2563EB;">€ 295.000</td>
                <td style="padding:4px 7px;">Associate Broker B</td>
                <td style="padding:4px 7px;"><span class="badge badge-amber">Under Offer</span></td>
                <td style="padding:4px 7px; text-align:right; font-weight:800; color:#2563EB;">Edit &middot; View</td>
              </tr>
              <tr>
                <td style="padding:4px 7px; font-weight:800; color:#0F172A;">Villa Alkmaarderhout</td>
                <td style="padding:4px 7px;">Luxury Residence (210 m²)</td>
                <td style="padding:4px 7px; font-weight:800; color:#2563EB;">€ 795.000</td>
                <td style="padding:4px 7px;">Agency Director</td>
                <td style="padding:4px 7px;"><span class="badge badge-green">Available</span></td>
                <td style="padding:4px 7px; text-align:right; font-weight:800; color:#2563EB;">Edit &middot; View</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Administrative Modules Grid -->
    <div class="grid-3" style="gap:8px;">
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Drag-and-Drop Media</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">Upload high-res photos, floor plans, and video links with automated cloud compression and WebP conversion.</p>
      </div>
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Single-Click Status Sync</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">Switch listings from Active to Under Offer or Sold across the public website and social channels in one click.</p>
      </div>
      <div class="card-bordered">
        <strong style="font-size:7.5pt; color:#0F172A;">Granular Staff Permissions</strong>
        <p class="body-text" style="font-size:6.8pt; margin-top:2px;">Role-Based Access Control ensuring agents only access assigned clients while directors retain full visibility.</p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 09 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 10: BUSINESS ANALYTICS & INVENTORY VELOCITY ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">09 &middot; Executive Business Intelligence</div>
    </div>

    <span class="section-tag">Data-Driven Brokerage Leadership</span>
    <h1 class="page-title">Executive Business Intelligence &amp; Demand Forecasting</h1>
    
    <p class="lead-text">
      Make confident strategic decisions backed by real-time intelligence on buyer inquiries, neighborhood demand, viewing completion ratios, and individual broker conversion performance:
    </p>

    <!-- 5 HIGH-PRECISION FULL COLOR SVG CHARTS GRID -->
    <div class="grid-2" style="gap:9px; margin-bottom:9px;">
      
      <!-- Chart 1: Monthly Inquiries Volume Trend (Blue/Cyan Gradient) -->
      <div class="card-bordered" style="padding:7px 10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:7.5pt; color:#0F172A;">1. Monthly Digital Enquiries (Growth)</strong>
          <span class="badge badge-blue">H1 Performance</span>
        </div>
        <div style="text-align:center;">
          <svg width="250" height="70" viewBox="0 0 250 70" style="display:inline-block;">
            <defs>
              <linearGradient id="blueGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#2563EB" stop-opacity="0.35" />
                <stop offset="100%" stop-color="#2563EB" stop-opacity="0.0" />
              </linearGradient>
            </defs>
            <line x1="25" y1="15" x2="245" y2="15" stroke="#E2E8F0" stroke-width="0.75" />
            <line x1="25" y1="35" x2="245" y2="35" stroke="#E2E8F0" stroke-width="0.75" />
            <line x1="25" y1="52" x2="245" y2="52" stroke="#E2E8F0" stroke-width="0.75" />
            <!-- Area fill -->
            <polygon fill="url(#blueGrad)" points="35,50 75,42 115,34 155,22 195,26 235,14 235,52 35,52" />
            <!-- Line -->
            <polyline fill="none" stroke="#2563EB" stroke-width="2.5" points="35,50 75,42 115,34 155,22 195,26 235,14" />
            <circle cx="35" cy="50" r="3" fill="#1D4ED8" />
            <circle cx="75" cy="42" r="3" fill="#1D4ED8" />
            <circle cx="115" cy="34" r="3" fill="#1D4ED8" />
            <circle cx="155" cy="22" r="3" fill="#1D4ED8" />
            <circle cx="195" cy="26" r="3" fill="#1D4ED8" />
            <circle cx="235" cy="14" r="3" fill="#1D4ED8" />
            <text x="35" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">Jan</text>
            <text x="75" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">Feb</text>
            <text x="115" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">Mar</text>
            <text x="155" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">Apr</text>
            <text x="195" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">May</text>
            <text x="235" y="64" font-size="6" fill="#64748B" font-weight="700" text-anchor="middle">Jun</text>
          </svg>
        </div>
        <div style="font-size:6.2pt; color:#2563EB; font-weight:800; text-align:center;">+84% increase in qualified inquiries within 6 months of platform deployment.</div>
      </div>

      <!-- Chart 2: Inventory Breakdown by Category (Colored Bars) -->
      <div class="card-bordered" style="padding:7px 10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:7.5pt; color:#0F172A;">2. Inventory Breakdown by Category</strong>
          <span class="badge badge-green">Demand Analysis</span>
        </div>
        <div style="text-align:center;">
          <svg width="250" height="70" viewBox="0 0 250 70" style="display:inline-block;">
            <line x1="20" y1="54" x2="245" y2="54" stroke="#CBD5E1" stroke-width="1" />
            <!-- Bar 1 -->
            <rect x="35" y="14" width="28" height="40" fill="#2563EB" rx="3" />
            <text x="49" y="10" font-size="6.5" fill="#1E40AF" font-weight="900" text-anchor="middle">46%</text>
            <text x="49" y="63" font-size="6" fill="#334155" font-weight="600" text-anchor="middle">Single Family</text>

            <!-- Bar 2 -->
            <rect x="85" y="24" width="28" height="30" fill="#10B981" rx="3" />
            <text x="99" y="20" font-size="6.5" fill="#047857" font-weight="900" text-anchor="middle">34%</text>
            <text x="99" y="63" font-size="6" fill="#334155" font-weight="600" text-anchor="middle">Apartments</text>

            <!-- Bar 3 -->
            <rect x="135" y="40" width="28" height="14" fill="#F59E0B" rx="3" />
            <text x="149" y="36" font-size="6.5" fill="#B45309" font-weight="900" text-anchor="middle">14%</text>
            <text x="149" y="63" font-size="6" fill="#334155" font-weight="600" text-anchor="middle">Villas</text>

            <!-- Bar 4 -->
            <rect x="185" y="48" width="28" height="6" fill="#8B5CF6" rx="3" />
            <text x="199" y="44" font-size="6.5" fill="#6D28D9" font-weight="900" text-anchor="middle">6%</text>
            <text x="199" y="63" font-size="6" fill="#334155" font-weight="600" text-anchor="middle">Commercial</text>
          </svg>
        </div>
        <div style="font-size:6.2pt; color:#047857; font-weight:800; text-align:center;">Residential single-family homes and urban apartments dominate viewing activity.</div>
      </div>

      <!-- Chart 3: Conversion Funnel (Colored Gradient Funnel) -->
      <div class="card-bordered" style="padding:7px 10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:7.5pt; color:#0F172A;">3. Deal Conversion Funnel</strong>
          <span class="badge badge-blue">Conversion Metrics</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:3px; padding:2px 0;">
          <div style="display:flex; align-items:center; font-size:6.2pt;">
            <span style="width:78px; color:#475569; font-weight:600;">Website Visitors</span>
            <div style="flex:1; background:#0F172A; color:#fff; padding:3px 7px; font-weight:800; border-radius:3px;">100% &middot; 5,200 Sessions</div>
          </div>
          <div style="display:flex; align-items:center; font-size:6.2pt;">
            <span style="width:78px; color:#475569; font-weight:600;">AI &amp; Web Leads</span>
            <div style="width:70%; background:#2563EB; color:#fff; padding:3px 7px; font-weight:800; border-radius:3px;">19.2% &middot; 998 Inquiries</div>
          </div>
          <div style="display:flex; align-items:center; font-size:6.2pt;">
            <span style="width:78px; color:#475569; font-weight:600;">Viewings Booked</span>
            <div style="width:48%; background:#0EA5E9; color:#fff; padding:3px 7px; font-weight:800; border-radius:3px;">9.4% &middot; 488 Viewings</div>
          </div>
          <div style="display:flex; align-items:center; font-size:6.2pt;">
            <span style="width:78px; color:#475569; font-weight:600;">Offers Placed</span>
            <div style="width:26%; background:#F59E0B; color:#fff; padding:3px 7px; font-weight:800; border-radius:3px;">4.1% &middot; 213 Bids</div>
          </div>
          <div style="display:flex; align-items:center; font-size:6.2pt;">
            <span style="width:78px; color:#475569; font-weight:600;">Deals Closed</span>
            <div style="width:14%; background:#10B981; color:#fff; padding:3px 7px; font-weight:800; border-radius:3px;">2.2% &middot; 114 Sales</div>
          </div>
        </div>
      </div>

      <!-- Chart 4: Viewing Outcomes Donut Chart (Colored) -->
      <div class="card-bordered" style="padding:7px 10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <strong style="font-size:7.5pt; color:#0F172A;">4. Viewing Appointment Outcomes</strong>
          <span class="badge badge-green">Audit Quality</span>
        </div>
        <div style="display:flex; align-items:center; justify-content:space-around;">
          <svg width="68" height="68" viewBox="0 0 40 40">
            <circle cx="20" cy="20" r="15.915" fill="transparent" stroke="#E2E8F0" stroke-width="6" />
            <circle cx="20" cy="20" r="15.915" fill="transparent" stroke="#10B981" stroke-width="6" stroke-dasharray="72 28" stroke-dashoffset="25" />
            <circle cx="20" cy="20" r="15.915" fill="transparent" stroke="#2563EB" stroke-width="6" stroke-dasharray="16 84" stroke-dashoffset="53" />
            <circle cx="20" cy="20" r="15.915" fill="transparent" stroke="#F59E0B" stroke-width="6" stroke-dasharray="9 91" stroke-dashoffset="37" />
            <circle cx="20" cy="20" r="15.915" fill="transparent" stroke="#EF4444" stroke-width="6" stroke-dasharray="3 97" stroke-dashoffset="28" />
          </svg>
          <div style="font-size:6.2pt; color:#334155; line-height:1.5;">
            <div><span style="display:inline-block; width:7px; height:7px; background:#10B981; border-radius:2px; margin-right:3px;"></span>Completed (72%)</div>
            <div><span style="display:inline-block; width:7px; height:7px; background:#2563EB; border-radius:2px; margin-right:3px;"></span>Rescheduled (16%)</div>
            <div><span style="display:inline-block; width:7px; height:7px; background:#F59E0B; border-radius:2px; margin-right:3px;"></span>Cancelled (9%)</div>
            <div><span style="display:inline-block; width:7px; height:7px; background:#EF4444; border-radius:2px; margin-right:3px;"></span>No-Show (3%)</div>
          </div>
        </div>
      </div>

    </div>

    <!-- Chart 5: Agent Productivity & Deal Velocity (Horizontal Bars) -->
    <div class="card-bordered" style="padding:7px 11px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px;">
        <strong style="font-size:7.5pt; color:#0F172A;">5. Broker Productivity &amp; Viewing Velocity Comparison</strong>
        <span class="badge badge-blue">Team Performance</span>
      </div>
      <div style="display:flex; flex-direction:column; gap:4px; font-size:6.4pt;">
        <div style="display:flex; align-items:center;">
          <span style="width:115px; font-weight:800; color:#0F172A;">Senior Broker A</span>
          <div style="flex:1; background:linear-gradient(90deg, #2563EB, #1D4ED8); color:#fff; padding:3px 8px; font-weight:800; border-radius:3px; max-width:88%;">52 Viewings &middot; 11 Offers Closed &middot; 96% Response Rate</div>
        </div>
        <div style="display:flex; align-items:center;">
          <span style="width:115px; font-weight:800; color:#0F172A;">Senior Broker B</span>
          <div style="flex:1; background:linear-gradient(90deg, #10B981, #059669); color:#fff; padding:3px 8px; font-weight:800; border-radius:3px; max-width:74%;">41 Viewings &middot; 8 Offers Closed &middot; 92% Response Rate</div>
        </div>
        <div style="display:flex; align-items:center;">
          <span style="width:115px; font-weight:800; color:#0F172A;">Associate Broker C</span>
          <div style="flex:1; background:linear-gradient(90deg, #64748B, #475569); color:#fff; padding:3px 8px; font-weight:800; border-radius:3px; max-width:55%;">28 Viewings &middot; 5 Offers Closed &middot; 88% Response Rate</div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 10 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 11: TECHNICAL ARCHITECTURE & SECURITY ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">10 &middot; Technology Architecture &amp; Security</div>
    </div>

    <span class="section-tag">Production-Grade Engineering</span>
    <h1 class="page-title">Enterprise Technology Stack &amp; Data Security</h1>
    
    <p class="lead-text">
      Engineered for long-term reliability, high concurrency during peak campaign releases, and seamless third-party connectivity:
    </p>

    <!-- Stack Cards Grid -->
    <div class="grid-4" style="gap:7px; margin-bottom:9px;">
      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #2563EB;">
        <span class="badge badge-blue" style="margin-bottom:2px;">Frontend</span>
        <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Next.js 15 &amp; React 19</div>
        <p style="font-size:6.4pt; color:#475569; margin-top:2px;">TypeScript, Tailwind CSS, Server-Side Rendering (SSR) for instant SEO indexing.</p>
      </div>

      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #0EA5E9;">
        <span class="badge badge-blue" style="margin-bottom:2px;">Backend APIs</span>
        <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Node.js / Express</div>
        <p style="font-size:6.4pt; color:#475569; margin-top:2px;">Decoupled RESTful APIs, JWT token security, rate-limiting, and webhook dispatchers.</p>
      </div>

      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #10B981;">
        <span class="badge badge-green" style="margin-bottom:2px;">Database &amp; ORM</span>
        <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">PostgreSQL &amp; Prisma</div>
        <p style="font-size:6.4pt; color:#475569; margin-top:2px;">ACID transactions, spatial property coordinates, connection pooling, and automated backups.</p>
      </div>

      <div class="card-bordered" style="padding:7px 9px; border-top:3px solid #8B5CF6;">
        <span class="badge badge-amber" style="margin-bottom:2px;">Integrations</span>
        <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Cloud APIs</div>
        <p style="font-size:6.4pt; color:#475569; margin-top:2px;">Google Maps, WhatsApp Business API, Google/Outlook Calendar, and OpenAI LLM.</p>
      </div>
    </div>

    <!-- TECHNICAL SYSTEM INTEGRATION DIAGRAM -->
    <div class="card" style="padding:9px 13px; background:#F8FAFC; border:1.5px solid #CBD5E1; margin-bottom:9px;">
      <div style="font-size:7pt; font-weight:800; text-transform:uppercase; letter-spacing:0.8px; color:#1D4ED8; margin-bottom:6px; text-align:center;">
        End-to-End Enterprise Data Flow &amp; Security Layer
      </div>

      <div style="display:flex; flex-direction:column; gap:4px; align-items:center;">
        <!-- Top: Users -->
        <div style="width:100%; max-width:480px; background:#0F172A; color:#FFFFFF; padding:5px 9px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:7.2pt; font-weight:800;">CLIENTS &amp; BROKERS</span>
          <span style="font-size:6.2pt; color:#94A3B8;">Home Buyers &middot; Sellers &middot; Licensed Real Estate Brokers &middot; Agency Admins</span>
        </div>

        <div style="font-size:7.5pt; color:#2563EB; line-height:1;">▼ HTTPS (TLS 1.3 Strict Transport Encryption)</div>

        <!-- Next.js App -->
        <div style="width:100%; max-width:480px; background:#FFFFFF; border:1.5px solid #2563EB; padding:6px 9px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">NEXT.JS 15 FRONTEND &amp; SSR APPLICATION</div>
            <div style="font-size:6pt; color:#475569;">Faceted Property Filter &middot; Interactive Map Engine &middot; Real-Time Viewing Scheduler &middot; Admin UI</div>
          </div>
          <span class="badge badge-green">Edge Cached</span>
        </div>

        <div style="font-size:7.5pt; color:#2563EB; line-height:1;">▼ JSON / RESTful Microservices &amp; WebSockets</div>

        <!-- Backend APIs -->
        <div style="width:100%; max-width:480px; background:#1E293B; color:#FFFFFF; padding:6px 9px; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:7.8pt; font-weight:800;">NODE.JS BACKEND APIS &amp; WORKFLOW ENGINES</div>
            <div style="font-size:6pt; color:#CBD5E1;">Authentication (JWT/OIDC) &middot; Lead Dispatcher &middot; Booking Automation &middot; Data Validation</div>
          </div>
          <span class="badge badge-blue">RBAC Enforced</span>
        </div>

        <div style="font-size:7.5pt; color:#2563EB; line-height:1;">▼ Prisma ORM (Connection Pool) &amp; Webhook Connectors</div>

        <!-- Database & External Integrations -->
        <div style="width:100%; max-width:480px; display:grid; grid-template-columns: 1fr 1.2fr; gap:6px;">
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; padding:5px 7px; border-radius:4px; text-align:center;">
            <div style="font-size:7pt; font-weight:800; color:#0F172A;">PostgreSQL Relational DB</div>
            <div style="font-size:5.8pt; color:#475569;">Encrypted At Rest (AES-256) &middot; Automated Daily Backups</div>
          </div>
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; padding:5px 7px; border-radius:4px; text-align:center;">
            <div style="font-size:7pt; font-weight:800; color:#0F172A;">Third-Party Cloud APIs</div>
            <div style="font-size:5.8pt; color:#475569;">Google Maps &middot; WhatsApp Business &middot; Calendar &middot; OpenAI</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Security Benchmarks -->
    <table class="data-table" style="font-size:7.2pt;">
      <thead>
        <tr>
          <th style="width:25%;">Security Pillar</th>
          <th style="width:40%;">Engineering Specification</th>
          <th style="width:35%;">Commercial Benefit</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>GDPR &amp; Privacy Compliance</strong></td>
          <td>Encrypted client data, consent logging, right-to-be-forgotten endpoints.</td>
          <td>Full legal compliance with European data protection regulations.</td>
        </tr>
        <tr>
          <td><strong>Role-Based Access Control</strong></td>
          <td>Granular permissions isolating sensitive buyer budgets and commissions.</td>
          <td>Internal security preventing unauthorized data export or exposure.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 11 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 12: ROADMAP, TEAM & NEXT STEPS (AXIOM GLOBAL & VIRANGA LAKSHAN) ========================================== -->
<div class="page" style="background:#F8FAFC;">
  <div>
    <div class="page-header">
      <div class="header-left">Axiom Global &middot; Real Estate Digital Transformation</div>
      <div class="header-right">11 &middot; Partnership Roadmap &amp; Next Steps</div>
    </div>

    <span class="section-tag">Agile Execution &amp; Engagement</span>
    <h1 class="page-title">Implementation Roadmap &amp; Partnership Kickoff</h1>
    
    <p class="lead-text">
      A structured 5-phase Agile Scrum execution model guarantees predictable milestone delivery, weekly demo visibility, and zero operational disruption:
    </p>

    <!-- 5-Phase Horizontal Timeline -->
    <div style="display:flex; flex-direction:column; gap:5px; margin-bottom:10px;">
      <div style="display:flex; gap:8px; align-items:center; background:#FFFFFF; border:1px solid #E2E8F0; padding:5px 9px; border-radius:4px;">
        <span style="background:#0F172A; color:#fff; font-size:7pt; font-weight:800; padding:3px 7px; border-radius:3px; min-width:80px; text-align:center;">PHASE 01</span>
        <div style="flex:1;">
          <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Discovery &amp; Requirements Prioritization</div>
          <p style="font-size:6.6pt; color:#475569; margin:0;">Mapping existing listing workflows, MLS data feeds, and defining custom feature priorities.</p>
        </div>
        <span style="font-size:6.5pt; color:#64748B; font-weight:700;">Duration: [TO BE AGREED]</span>
      </div>

      <div style="display:flex; gap:8px; align-items:center; background:#FFFFFF; border:1px solid #E2E8F0; padding:5px 9px; border-radius:4px;">
        <span style="background:#2563EB; color:#fff; font-size:7pt; font-weight:800; padding:3px 7px; border-radius:3px; min-width:80px; text-align:center;">PHASE 02</span>
        <div style="flex:1;">
          <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">UI/UX Design &amp; Prototype Sign-Off</div>
          <p style="font-size:6.6pt; color:#475569; margin:0;">Creating high-fidelity desktop and mobile Figma prototypes reflecting your exact brokerage branding.</p>
        </div>
        <span style="font-size:6.5pt; color:#64748B; font-weight:700;">Duration: [TO BE AGREED]</span>
      </div>

      <div style="display:flex; gap:8px; align-items:center; background:#FFFFFF; border:1px solid #E2E8F0; padding:5px 9px; border-radius:4px;">
        <span style="background:#10B981; color:#fff; font-size:7pt; font-weight:800; padding:3px 7px; border-radius:3px; min-width:80px; text-align:center;">PHASE 03</span>
        <div style="flex:1;">
          <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Core Development &amp; AI Engine Build</div>
          <p style="font-size:6.6pt; color:#475569; margin:0;">Building Next.js frontend, Node.js backend, PostgreSQL schemas, and the 24/7 AI Concierge.</p>
        </div>
        <span style="font-size:6.5pt; color:#64748B; font-weight:700;">Duration: [TO BE AGREED]</span>
      </div>

      <div style="display:flex; gap:8px; align-items:center; background:#FFFFFF; border:1px solid #E2E8F0; padding:5px 9px; border-radius:4px;">
        <span style="background:#F59E0B; color:#fff; font-size:7pt; font-weight:800; padding:3px 7px; border-radius:3px; min-width:80px; text-align:center;">PHASE 04</span>
        <div style="flex:1;">
          <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">System Integration &amp; User Acceptance Testing (UAT)</div>
          <p style="font-size:6.6pt; color:#475569; margin:0;">Connecting Google Calendar, WhatsApp Business API, testing mobile responsiveness, and client review.</p>
        </div>
        <span style="font-size:6.5pt; color:#64748B; font-weight:700;">Duration: [TO BE AGREED]</span>
      </div>

      <div style="display:flex; gap:8px; align-items:center; background:#FFFFFF; border:1px solid #E2E8F0; padding:5px 9px; border-radius:4px;">
        <span style="background:#0F172A; color:#fff; font-size:7pt; font-weight:800; padding:3px 7px; border-radius:3px; min-width:80px; text-align:center;">PHASE 05</span>
        <div style="flex:1;">
          <div style="font-size:7.8pt; font-weight:800; color:#0F172A;">Production Deployment, Staff Training &amp; Handover</div>
          <p style="font-size:6.6pt; color:#475569; margin:0;">Live cloud deployment, broker training, documentation, source code handover, and hypercare support.</p>
        </div>
        <span style="font-size:6.5pt; color:#64748B; font-weight:700;">Duration: [TO BE AGREED]</span>
      </div>
    </div>

    <!-- Team Credentials Box (Axiom Global) -->
    <div class="card-bordered" style="background:#FFFFFF; padding:9px 13px; margin-bottom:9px;">
      <div style="font-size:7.5pt; font-weight:800; text-transform:uppercase; color:var(--primary); margin-bottom:2px;">
        Engineering Credentials &amp; Delivery Standards &middot; Axiom Global
      </div>
      <p style="font-size:7.4pt; line-height:1.45; color:#1E293B; margin:0;">
        "We are a Sri Lanka-based software development team working with international clients and delivering web applications, business platforms, backend systems, and custom software solutions. Our team includes experienced software engineers, with team members having more than six years of professional software development experience." Full CVs and verified international enterprise portfolios available upon request.
      </p>
    </div>

    <!-- PROMINENT CALL TO ACTION & CONTACT CARD (VIRANGA LAKSHAN & AXIOM GLOBAL) -->
    <div style="background:linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%); color:#FFFFFF; border-radius:6px; padding:13px 18px; margin-bottom:6px; box-shadow:0 4px 14px rgba(15,23,42,0.25);">
      <div style="text-align:center; margin-bottom:8px;">
        <span style="font-size:7pt; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:#93C5FD;">COMMENCE YOUR DIGITAL TRANSFORMATION</span>
        <h2 style="font-size:14pt; font-weight:900; color:#FFFFFF; margin-top:2px;">
          LET'S DISCUSS YOUR BROKERAGE'S DIGITAL TRANSFORMATION.
        </h2>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:14px; border-top:1px solid rgba(255,255,255,0.18); padding-top:9px;">
        <div>
          <div style="font-size:6.5pt; color:#94A3B8; text-transform:uppercase; font-weight:800;">COMPANY IDENTITY</div>
          <div style="font-size:9.5pt; font-weight:900; color:#FFFFFF;">Axiom Global</div>
          <div style="font-size:7.5pt; color:#CBD5E1; margin-top:1px;">Software Engineering Team – Sri Lanka</div>
          <div style="font-size:7.2pt; color:#93C5FD; margin-top:1px;">Website: axiomglobal.tech &middot; GitHub Portfolio</div>
        </div>

        <div>
          <div style="font-size:6.5pt; color:#94A3B8; text-transform:uppercase; font-weight:800;">DIRECT CONTACT LEAD</div>
          <div style="font-size:9.5pt; font-weight:900; color:#FFFFFF;">Viranga Lakshan</div>
          <div style="font-size:7.5pt; color:#CBD5E1; margin-top:1px;">Email: virangalakshanz@gmail.com</div>
          <div style="font-size:7.2pt; color:#93C5FD; margin-top:1px;">Phone / WhatsApp: +94 71 378 1359</div>
        </div>
      </div>
    </div>

    <!-- Closing commitment -->
    <div style="text-align:center; padding:2px 0;">
      <p style="font-size:7.8pt; font-weight:700; color:#1E293B; margin:0;">
        "We would welcome the opportunity to discuss how Axiom Global's software development team could support your company's digital growth."
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">Axiom Global &middot; Real Estate Digital Transformation &middot; Lead: <strong>Viranga Lakshan</strong></div>
    <div class="footer-page-num">Page 12 of 12</div>
  </div>
</div>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML template successfully created at: {html_path}")

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

print(f"PDF generated successfully at: {pdf_path}")

# Verify total pages and text with pypdfium2
pdf = pdfium.PdfDocument(pdf_path)
print(f"Total Page Count: {len(pdf)}")
for i in range(len(pdf)):
    tp = pdf[i].get_textpage()
    text = tp.get_text_range()
    first_line = text.splitlines()[0] if text.splitlines() else "EMPTY"
    print(f"Page {i+1}: {len(text)} chars | First line: {first_line[:50]}")
    s = tp.search(f"Page {i+1:02d} of 12")
    m = s.get_next()
    if m:
        b = tp.get_charbox(m[0])
        print(f"  Footer Page {i+1:02d} of 12 verified at y={b[1]:.2f} pt")
    elif i > 0:
        print(f"  Footer Page {i+1:02d} of 12 NOT found!")
