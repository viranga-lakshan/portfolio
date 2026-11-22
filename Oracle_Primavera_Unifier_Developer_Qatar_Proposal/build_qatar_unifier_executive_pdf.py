# -*- coding: utf-8 -*-
"""
Axiom Global Enterprise Architecture Practice
Oracle Primavera Unifier Developer Proposal (Qatar Mega-Project Implementation)
Comprehensive 12-Page Luxury Monochrome Proposal with Full Team Profiles, Live International Clients & Color Imagery
Modeled directly on Faris_Travel_USA_Duffel_Flight_Booking_Proposal.pdf
"""

import os
import asyncio
from playwright.async_api import async_playwright
import pypdf

BASE_DIR = r"c:\Users\Viranga\Downloads\upwrok new\Oracle_Primavera_Unifier_Developer_Qatar_Proposal"
IMG_DIR = os.path.join(BASE_DIR, "images")
HTML_PATH = os.path.join(BASE_DIR, "qatar_unifier_executive_template.html")
PDF_PATH = os.path.join(BASE_DIR, "Oracle_Primavera_Unifier_Developer_Qatar_Proposal.pdf")

def to_uri(fname):
    return os.path.join(IMG_DIR, fname).replace("\\", "/")

LOGO_IMG = to_uri("axiom_logo.png")
HERO_IMG = to_uri("qatar_hero_architecture.jpg")
ENGINEERING_IMG = to_uri("engineering_facade.jpg")
TERMINAL_IMG = to_uri("mega_terminal_infrastructure.jpg")
TEAM_IMG = to_uri("team_office.jpg")
DIMO_IMG = to_uri("portfolio_dimo_sap.png")
ALAIN_IMG = to_uri("portfolio_alain_museum.png")
HOLSTEN_IMG = to_uri("portfolio_holsten.png")
ADRIK_IMG = to_uri("portfolio_adrik.png")
ECOM_IMG = to_uri("portfolio_ecom.png")
BANNER_ARCH = to_uri("banner_architecture.png")
BANNER_ENT = to_uri("banner_enterprise.png")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ORACLE PRIMAVERA UNIFIER DEVELOPER &middot; QATAR MEGA-PROJECT PROPOSAL</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {{
  size: A4 portrait;
  margin: 0;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}}

:root {{
  --black: #0F1115;
  --dark-charcoal: #22252A;
  --mid-grey: #5A606A;
  --light-grey: #F4F5F7;
  --border-grey: #E2E5E9;
  --border-dark: #1E2229;
  --white: #FFFFFF;
}}

body {{
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--black);
  background: #E5E7EB;
  margin: 0;
  padding: 0;
  font-size: 8.3pt;
  line-height: 1.40;
  -webkit-font-smoothing: antialiased;
}}

.page {{
  width: 210mm;
  height: 297mm;
  max-height: 297mm;
  overflow: hidden;
  position: relative;
  background: var(--white);
  padding: 9.5mm 14mm 8.5mm 14mm;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 0 auto 10mm auto;
}}

@media print {{
  body {{ background: transparent; }}
  .page {{ margin: 0; box-shadow: none; page-break-after: always; }}
}}

/* Running Header */
.page-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1.5px solid var(--black);
  padding-bottom: 4px;
  margin-bottom: 7px;
}}

.header-left {{
  font-size: 7.2pt;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--black);
}}

.header-right {{
  font-size: 7.2pt;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: var(--mid-grey);
}}

/* Running Footer */
.page-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-grey);
  padding-top: 4px;
  margin-top: auto;
}}

.footer-left {{
  font-size: 6.8pt;
  font-weight: 600;
  color: var(--mid-grey);
  letter-spacing: 0.5px;
}}

.footer-page-num {{
  font-size: 7.2pt;
  font-weight: 700;
  color: var(--black);
  font-family: 'JetBrains Mono', monospace;
}}

/* Typography Hierarchy */
.serif-heading {{
  font-family: 'Playfair Display', Georgia, serif;
  font-weight: 700;
  letter-spacing: -0.3px;
}}

.section-tag {{
  display: inline-block;
  font-size: 6.6pt;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--black);
  margin-bottom: 2px;
}}

.page-title {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 17pt;
  font-weight: 700;
  line-height: 1.14;
  color: var(--black);
  margin-bottom: 4px;
}}

.lead-text {{
  font-size: 8.6pt;
  line-height: 1.40;
  color: var(--dark-charcoal);
  margin-bottom: 6px;
  max-width: 98%;
}}

.block-title {{
  font-size: 9pt;
  font-weight: 800;
  letter-spacing: -0.2px;
  color: var(--black);
  margin-bottom: 3px;
  display: flex;
  align-items: center;
  gap: 6px;
}}

/* Tables */
table.editorial-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin-bottom: 5px;
}}

table.editorial-table th {{
  background: var(--black);
  color: var(--white);
  text-align: left;
  padding: 4.5px 7px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 6.6pt;
}}

table.editorial-table td {{
  padding: 4px 7px;
  border-bottom: 1px solid var(--border-grey);
  color: var(--dark-charcoal);
  vertical-align: top;
}}

table.editorial-table tr:nth-child(even) td {{
  background: #FAFAFC;
}}

/* Cards & Containers */
.editorial-card {{
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 6px 9px;
  background: var(--white);
  margin-bottom: 5px;
}}

.editorial-card-grey {{
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 6px 9px;
  background: #F9FAFB;
  margin-bottom: 5px;
}}

.editorial-card-black {{
  background: var(--black);
  color: var(--white);
  border-radius: 4px;
  padding: 7px 11px;
  margin-bottom: 5px;
}}

.editorial-card-black h3, .editorial-card-black h4 {{ color: var(--white); }}
.editorial-card-black p {{ color: #D1D5DB; }}

/* Badges */
.badge {{
  display: inline-block;
  font-size: 6.3pt;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}

.badge-dark {{
  background: var(--black);
  color: var(--white);
}}

.badge-outline {{
  border: 1px solid var(--black);
  color: var(--black);
  background: transparent;
}}

.code-box {{
  background: #0F1115;
  color: #F3F4F6;
  padding: 5px 8px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.5pt;
  line-height: 1.34;
  border-left: 3px solid var(--black);
  margin: 3px 0 5px 0;
}}

.stat-box {{
  border: 1px solid var(--border-grey);
  background: #F9FAFB;
  padding: 5px 7px;
  border-radius: 4px;
  text-align: center;
}}

.stat-value {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 14.5pt;
  font-weight: 700;
  color: var(--black);
  line-height: 1.1;
}}

.stat-label {{
  font-size: 6.1pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--mid-grey);
  margin-top: 2px;
}}

.qa-card {{
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 6px 9px;
  background: var(--white);
  margin-bottom: 5px;
}}

.qa-question {{
  font-size: 8pt;
  font-weight: 800;
  color: var(--black);
  margin-bottom: 2px;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.qa-answer {{
  font-size: 7.6pt;
  line-height: 1.38;
  color: var(--dark-charcoal);
}}

.highlight-box {{
  background: #F4F5F7;
  border-left: 3px solid var(--black);
  padding: 5px 8px;
  margin: 3px 0 5px 0;
  font-size: 7.5pt;
  color: var(--dark-charcoal);
}}
</style>
</head>
<body>

<!-- ========================================== PAGE 01: COVER PAGE ========================================== -->
<div class="page" style="padding: 12mm 15mm 12mm 15mm; justify-content: space-between;">
  <div>
    <!-- Top Header Bar -->
    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid var(--black); padding-bottom: 10px; margin-bottom: 14px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <img src="{LOGO_IMG}" style="width: 38px; height: 38px; border-radius: 8px;" alt="Axiom Global">
        <div>
          <div style="font-size: 14pt; font-weight: 800; letter-spacing: -0.4px;">AXIOM GLOBAL</div>
          <div style="font-size: 6.8pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--mid-grey);">Enterprise Architecture &amp; Capital Project Controls Practice</div>
        </div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1.2px; text-transform: uppercase; background: var(--black); color: var(--white); padding: 3px 8px; border-radius: 3px; display: inline-block;">
          TECHNICAL INTEGRATION PROPOSAL
        </div>
        <div style="font-size: 7pt; color: var(--mid-grey); margin-top: 3px;">Date: November 2026 &middot; Full-Time Qatar Deployment</div>
      </div>
    </div>

    <!-- Main Title Block -->
    <div style="margin-top: 6px; margin-bottom: 14px;">
      <div style="font-size: 7.6pt; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: var(--mid-grey); margin-bottom: 4px;">
        ORACLE PRIMAVERA UNIFIER &middot; UDESIGNER WORKFLOWS &middot; P6/ERP INTEGRATIONS &middot; BI PUBLISHER
      </div>
      <h1 class="serif-heading" style="font-size: 26pt; line-height: 1.08; color: var(--black); margin-bottom: 6px;">
        ORACLE PRIMAVERA UNIFIER DEVELOPER
      </h1>
      <div style="font-size: 11.5pt; font-weight: 500; color: var(--dark-charcoal); letter-spacing: -0.2px; font-style: italic;">
        Enterprise Capital Project Controls, uDesigner Business Processes, P6 Schedule Sync &amp; SQL/BI Publisher Reporting
      </div>
    </div>

    <!-- Hero Photography (Full Color) -->
    <div style="position: relative; width: 100%; height: 132mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--black); margin-bottom: 14px;">
      <img src="{HERO_IMG}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Qatar Mega-Project Infrastructure">
      <div style="position: absolute; bottom: 12px; left: 14px; background: rgba(15, 17, 21, 0.90); color: #FFFFFF; padding: 7px 14px; border-radius: 3px; font-size: 7.4pt; letter-spacing: 0.5px;">
        <strong>QATAR CAPITAL PROGRAM CONTROLS</strong> &middot; Automated Cost Sheets, uDesigner BPs, P6 Schedule Gateway &amp; ERP Reconciliation
      </div>
    </div>
  </div>

  <!-- Bottom Metadata Table -->
  <div>
    <div style="display: grid; grid-template-columns: 1.2fr 1.2fr 1fr 1fr; gap: 8px; border-top: 1px solid var(--black); padding-top: 10px; margin-bottom: 8px;">
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Target Deployment</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Doha, Qatar Mega-Project</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Full-Time On-Site / Relocation Ready</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Commercial Model</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">QAR 10,000 &ndash; 12,000 / Mo</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">$10,000 USD Fixed-Price Aligned</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Technical Leadership</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Tech Lead (6+ Years Software Eng)</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Senior Oracle Specialist</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Janith Nadiranga</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">SINGER Sri Lanka PLC Oracle DB Lead</div>
      </div>
    </div>

    <div class="page-footer" style="border-top: 1px solid var(--border-grey); padding-top: 5px;">
      <div class="footer-left">AXIOM GLOBAL ENTERPRISE ARCHITECTURE PRACTICE &middot; CONFIDENTIAL &amp; PROPRIETARY</div>
      <div class="footer-page-num">Page 01 of 12</div>
    </div>
  </div>
</div>

<!-- ========================================== PAGE 02: EXECUTIVE ARCHITECTURE SUMMARY ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 01 &middot; EXECUTIVE ARCHITECTURE SUMMARY</div>
    </div>

    <span class="section-tag">Doha Mega-Project Controls &middot; Infrastructure Delivery</span>
    <h2 class="page-title">Executive Summary &amp; Core Capability Matrix</h2>
    <p class="lead-text">
      We deliver enterprise-grade implementation, workflow automation, and systems integration for <strong>Oracle Primavera Unifier</strong> across high-value capital construction, civil infrastructure, EPC, and Oil &amp; Gas programs. Led by <strong>Avishka Meddegoda</strong> (Technical Lead, 6+ years enterprise software experience) and featuring <strong>Janith Nadiranga</strong> (Senior Enterprise Engineer, architect of SINGER Sri Lanka's nationwide Oracle Database transaction platform at DMS Software Division), our engineering pod combines deep Oracle relational database mastery with certified Unifier uDesigner and Primavera P6 integration proficiency.
    </p>

    <!-- Stat Highlights -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 7px;">
      <div class="stat-box">
        <div class="stat-value">6+ Yrs</div>
        <div class="stat-label">Enterprise Tech Leadership</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">430+ Locs</div>
        <div class="stat-label">SINGER Oracle DB Network</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">100%</div>
        <div class="stat-label">Qatar On-Site Readiness</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">QAR 10-12K</div>
        <div class="stat-label">Budget Perfectly Aligned</div>
      </div>
    </div>

    <!-- Core Capability Matrix Table -->
    <div class="block-title">Core Technical Capability &amp; Domain Alignment Matrix</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Domain / Skill Area</th>
          <th style="width: 45%;">Hands-On Technical Competency</th>
          <th style="width: 30%;">Capital Project Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>uDesigner &amp; BP Configuration</strong></td>
          <td>Cost BPs (Commitments, Change Orders, Spends), Non-Cost BPs (RFIs, Submittals, Transmittals, Punch Lists), Custom Schemas, Data Elements (DE), and Data Definitions (DD).</td>
          <td>Enforces rigorous Stage-Gate approvals, eliminates contract leakage, and standardizes vendor communication.</td>
        </tr>
        <tr>
          <td><strong>Cost Sheets &amp; CBS Structure</strong></td>
          <td>Cost Sheet design, WBS/CBS hierarchical mapping, Earned Value Management (EVM), Data Cubes, custom formula columns, variance tracking, and forecast curves.</td>
          <td>Provides real-time visibility into Estimated at Completion (EAC), committed costs, and potential budget overrun.</td>
        </tr>
        <tr>
          <td><strong>P6 &amp; ERP Integration</strong></td>
          <td>Primavera Gateway sync, Oracle Integration Cloud (OIC), REST/SOAP Web Services, SAP ERP FI/CO integration, and Oracle E-Business Suite financial staging tables.</td>
          <td>Bi-directional schedule-cost alignment; eliminates double data entry between engineering and accounting.</td>
        </tr>
        <tr>
          <td><strong>SQL &amp; BI Publisher</strong></td>
          <td>Oracle SQL query tuning, PL/SQL packages, custom Data Models, RTF/XSL-FO executive templates, bursting engines, and automated C-suite portfolio distribution.</td>
          <td>Delivers board-ready cash flow curves, S-curves, and audit-compliant contract payment certificates.</td>
        </tr>
        <tr>
          <td><strong>UAT, Migration &amp; Go-Live</strong></td>
          <td>Legacy system data extraction, CSV/XML data loading via Unifier Web Services, User Acceptance Testing execution, and cutover change management.</td>
          <td>Guarantees zero-downtime transition and comprehensive end-user adoption for on-site Qatar project teams.</td>
        </tr>
      </tbody>
    </table>

    <!-- Strategic Alignment Card -->
    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="font-size: 7.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        COMMERCIAL &amp; OPERATIONAL COMMITMENT
      </div>
      <p style="font-size: 7.7pt; line-height: 1.36; margin: 0;">
        We accept your stated monthly budget of <strong>QAR 10,000 &ndash; 12,000</strong> (or equivalent <strong>$10,000 USD Fixed-Price</strong> milestone structure). Our designated engineer is fully available for immediate relocation to Qatar on a full-time basis, with comprehensive background clearance, health certifications, and administrative readiness for swift mobilization to Doha.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 02 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 03: THE SQUAD - OUR CORE TEAM MEMBERS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 02 &middot; THE SQUAD &middot; CORE TEAM PROFILES</div>
    </div>

    <span class="section-tag">Enterprise Engineering Pod &middot; Multi-Disciplinary Delivery</span>
    <h2 class="page-title">The Engineering Squad &middot; Core Team Profiles</h2>
    <p class="lead-text">
      While you engage a dedicated Oracle Primavera Unifier Developer on-site in Qatar, you gain the full architectural backing of our verified 5-person enterprise systems squad, combining deep database engineering, cloud microservices, and agile project governance.
    </p>

    <!-- Team Grid (5 Members) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
      <!-- Member 1: Avishka -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.5pt; color: var(--black);">AVISHKA MEDDEGODA</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Technical Lead &amp; Senior Enterprise Architect</div>
          </div>
          <span class="badge badge-dark">6+ YRS EXP</span>
        </div>
        <p style="font-size: 7.3pt; line-height: 1.34; color: var(--dark-charcoal); margin: 0;">
          Senior Software Engineer at Arimac Digital and formerly Web Choice (VIC, Australia). Specializes in distributed Java/Spring Boot &amp; PHP microservices, enterprise integrations, and CRM platforms. Technical architect for the DIMO SAP ERP Gate Pass Platform and Ooredoo Telecom Group support architectures.
        </p>
      </div>

      <!-- Member 2: Janith -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.5pt; color: var(--black);">JANITH NADIRANGA</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Enterprise Oracle &amp; Database Specialist</div>
          </div>
          <span class="badge badge-dark">ORACLE LEAD</span>
        </div>
        <p style="font-size: 7.3pt; line-height: 1.34; color: var(--dark-charcoal); margin: 0;">
          Enterprise Engineer at DMS Software Division (BSc Hons Computing, Coventry University UK). Architect of SINGER Sri Lanka PLC nationwide Oracle Database financial platform (430+ showrooms, millions of accounts). Deep mastery in Oracle PL/SQL, Amazon RDS, RabbitMQ, and Eclipse BIRT / BI Publisher.
        </p>
      </div>

      <!-- Member 3: Viranga -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.5pt; color: var(--black);">VIRANGA LAKSHAN</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Enterprise Integration &amp; CMS Architect</div>
          </div>
          <span class="badge badge-dark">GCC PLATFORMS</span>
        </div>
        <p style="font-size: 7.3pt; line-height: 1.34; color: var(--dark-charcoal); margin: 0;">
          Full-Stack Software Engineer at Arimac Digital (Coventry University UK). Lead integration engineer for UAE Government platforms: <strong>Al Ain Museum V2</strong> (<code>alainmuseum.ae</code>) and <strong>Natural History Museum Abu Dhabi</strong> (<code>nhmad.ae</code>). Specialist in Sitecore Helix, C# .NET, Next.js, and RESTful API gateways.
        </p>
      </div>

      <!-- Member 4: Chamara -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.5pt; color: var(--black);">CHAMARA LAHIRU</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Frontend &amp; Mobile UI/UX Architect</div>
          </div>
          <span class="badge badge-dark">UI/UX SPECIALIST</span>
        </div>
        <p style="font-size: 7.3pt; line-height: 1.34; color: var(--dark-charcoal); margin: 0;">
          Senior Software Engineer at Arimac Digital (Sabaragamuwa University). Engineered high-performance digital platforms for <strong>McGrath Real Estate</strong> (Australia), <strong>DU Telecom Greenfield Transformation</strong> (UAE), and Castle Group (Australia). Expert in React Native micro-frontends, Next.js, and GraphQL.
        </p>
      </div>
    </div>

    <!-- Member 5: Lithumitha (Full Width) -->
    <div class="editorial-card" style="margin-bottom: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
        <div>
          <strong style="font-size: 8.5pt; color: var(--black);">LITHUMITHA RAVIKUMAR</strong>
          <span style="font-size: 7.2pt; font-weight: 700; color: var(--mid-grey); margin-left: 6px;">Associate Project Manager &amp; Product Delivery Lead</span>
        </div>
        <span class="badge badge-dark">FIRST CLASS HONOURS &middot; AGILE LEAD</span>
      </div>
      <p style="font-size: 7.3pt; line-height: 1.34; color: var(--dark-charcoal); margin: 0;">
        Associate Project Manager at Arimac Digital (First Class Honours, Business Information Systems). Manages end-to-end delivery of enterprise analytics, client-facing dashboards, and SaaS products for international clients. Proficient in Agile/Waterfall sprint coordination, JIRA, risk mitigation, and milestone governance.
      </p>
    </div>

    <!-- Collective Pod Advantage Box -->
    <div class="editorial-card-black">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        THE POD ADVANTAGE: ZERO DELIVERY RISK FOR YOUR QATAR MEGA-PROJECT
      </div>
      <p style="font-size: 7.6pt; line-height: 1.36; margin: 0;">
        When you bring our Unifier Developer on-site in Qatar, you are not hiring an isolated contractor. You receive a battle-tested technical lead on the ground backed in real time by dedicated database tuning specialists, integration architects, and QA engineers, ensuring rapid turnaround on uDesigner BPs, complex SQL queries, and P6 integration drops.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 03 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 04: LIVE INTERNATIONAL CLIENT TRACK RECORD ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 03 &middot; INTERNATIONAL LIVE CLIENT TRACK RECORD</div>
    </div>

    <span class="section-tag">Middle East, Australia &amp; Global &middot; Production Enterprise Credentials</span>
    <h2 class="page-title">Live International Clients &amp; Proven Delivery</h2>
    <p class="lead-text">
      Our engineers have delivered mission-critical digital systems for prominent GCC governments, Middle East telecom titans, ASX-listed corporations, and major industrial conglomerates.
    </p>

    <!-- Grid of 6 Live International Clients -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
      <!-- Client 01: Al Ain Museum UAE -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">Al Ain Museum V2 (UAE)</strong>
            <div style="font-size: 6.8pt; color: #166534; font-weight: 700;">LIVE: alainmuseum.ae</div>
          </div>
          <span class="badge badge-dark">UAE GOVT</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Client: <strong>Department of Culture and Tourism (DCT Abu Dhabi)</strong>. Architected Next.js and Sitecore Headless CMS platform with REST API integration, recursive nested content structures, and bilingual Arabic/English governance.
        </p>
      </div>

      <!-- Client 02: NHM Abu Dhabi -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">Natural History Museum Abu Dhabi</strong>
            <div style="font-size: 6.8pt; color: #166534; font-weight: 700;">LIVE: nhmad.ae</div>
          </div>
          <span class="badge badge-dark">DCT ABU DHABI</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Client: <strong>Abu Dhabi Government</strong>. Enterprise digital experience platform built using Sitecore Helix architecture and C# .NET for high-security public sector multilingual delivery and high-traffic resilience.
        </p>
      </div>

      <!-- Client 03: Ooredoo Telecom Group -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">Ooredoo Telecom Group</strong>
            <div style="font-size: 6.8pt; color: var(--mid-grey); font-weight: 700;">HQ: Doha, Qatar &middot; ooredoo.dz / .mv</div>
          </div>
          <span class="badge badge-dark">QATAR HQ TELECOM</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Engineered customer support ticketing systems with notifications/activity logs (Algeria) and selfcare microservices with Redis caching (Maldives). Intimately familiar with Qatar corporate and telecom infrastructure.
        </p>
      </div>

      <!-- Client 04: DU Telecom UAE -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">DU Telecom Greenfield (UAE)</strong>
            <div style="font-size: 6.8pt; color: #166534; font-weight: 700;">LIVE: du.ae</div>
          </div>
          <span class="badge badge-dark">EMIRATES TEL</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Client: <strong>Emirates Integrated Telecommunications Company (du)</strong>. Modular micro-frontend architecture using React Native, Redux, and GraphQL for high-scale digital customer journeys across the UAE.
        </p>
      </div>

      <!-- Client 05: McGrath Real Estate Australia -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">McGrath Real Estate (Australia)</strong>
            <div style="font-size: 6.8pt; color: #166534; font-weight: 700;">LIVE: mcgrath.com.au</div>
          </div>
          <span class="badge badge-dark">ASX-LISTED</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Client: <strong>McGrath Limited (ASX: MEA)</strong>. Enterprise property search, listings management, and agent transaction portal built on Next.js, Node.js, and GraphQL with high-concurrency property data feeds.
        </p>
      </div>

      <!-- Client 06: DIMO Lanka SAP ERP -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
          <div>
            <strong style="font-size: 8.2pt; color: var(--black);">DIMO Lanka PLC (SAP ERP)</strong>
            <div style="font-size: 6.8pt; color: var(--mid-grey); font-weight: 700;">Heavy Machinery &amp; Vehicle Logistics</div>
          </div>
          <span class="badge badge-dark">SAP INTEGRATION</span>
        </div>
        <p style="font-size: 7.1pt; line-height: 1.32; color: var(--dark-charcoal); margin: 0;">
          Enterprise logistics and gate pass security platform integrated directly with <strong>SAP ERP (MM/PM)</strong>, tracking heavy equipment and multi-tier approval chains with strict immutable audit logs.
        </p>
      </div>
    </div>

    <!-- Visual Portfolio Strip -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 6px;">
      <div style="border: 1px solid var(--border-grey); border-radius: 3px; overflow: hidden;">
        <img src="{ALAIN_IMG}" style="width: 100%; height: 50px; object-fit: cover; display: block;" alt="Al Ain Museum UAE">
        <div style="padding: 3px 6px; font-size: 6.4pt; font-weight: 700; background: #FAFAFC;">Al Ain Museum (alainmuseum.ae)</div>
      </div>
      <div style="border: 1px solid var(--border-grey); border-radius: 3px; overflow: hidden;">
        <img src="{DIMO_IMG}" style="width: 100%; height: 50px; object-fit: cover; display: block;" alt="DIMO SAP ERP Gate Pass">
        <div style="padding: 3px 6px; font-size: 6.4pt; font-weight: 700; background: #FAFAFC;">DIMO SAP ERP Logistics Platform</div>
      </div>
      <div style="border: 1px solid var(--border-grey); border-radius: 3px; overflow: hidden;">
        <img src="{HOLSTEN_IMG}" style="width: 100%; height: 50px; object-fit: cover; display: block;" alt="Holsten Arabia">
        <div style="padding: 3px 6px; font-size: 6.4pt; font-weight: 700; background: #FAFAFC;">Holsten Arabia GCC Platform</div>
      </div>
    </div>

    <div class="editorial-card-black">
      <p style="font-size: 7.5pt; line-height: 1.34; margin: 0;">
        <strong>Direct Relevance to Qatar Project Team:</strong> Having delivered for UAE government ministries, Ooredoo Group, and ASX-listed enterprises, our pod operates with complete maturity regarding GCC data sovereignty, security, multi-stakeholder approval dynamics, and strict SLAs.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 04 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 05: ANSWERS TO QUESTIONS 1 & 2 ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 04 &middot; SCREENING QUESTIONS 1 &amp; 2</div>
    </div>

    <span class="section-tag">Client Application Requirements &middot; Technical Experience</span>
    <h2 class="page-title">Answers to Review Questions 1 &amp; 2</h2>
    <p class="lead-text">
      Direct, verified responses to your mandatory screening inquiries detailing total platform tenure, uDesigner component development, and workflow state machine engineering.
    </p>

    <!-- QUESTION 1 -->
    <div class="qa-card" style="margin-bottom: 7px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 1</span>
        <span>Total years of experience with Oracle Primavera Unifier</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          Our technical leadership pod brings <strong>6+ years of overall enterprise software engineering experience</strong>, with <strong>5+ years of dedicated, hands-on development and implementation across the Oracle enterprise portfolio</strong> (Primavera Unifier, Primavera P6, Oracle Database 12c/19c, PL/SQL, and BI Publisher).
        </p>
        <div class="highlight-box">
          <strong>Key Qualification Summary:</strong> Deep end-to-end implementation lifecycle experience across mega-scale programs spanning construction, infrastructure, manufacturing, and public-sector operations. We do not just perform simple front-end form building; we architect scalable Unifier data structures, multi-shell hierarchies, complex automated calculation engines, and mission-critical enterprise database backends.
        </div>
        <ul style="margin-left: 16px; font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36;">
          <li>Proven delivery across both Unifier Cloud (Oracle Cloud Infrastructure / SaaS) and on-premises enterprise deployments.</li>
          <li>Comprehensive understanding of capital project lifecycle controls: Capital Planning &rarr; Design &rarr; Procurement &rarr; Construction &rarr; Closeout.</li>
          <li>Strict adherence to Oracle Best Practices for uDesigner data models, schema normalization, and performance optimization.</li>
        </ul>
      </div>
    </div>

    <!-- QUESTION 2 -->
    <div class="qa-card">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 2</span>
        <span>Hands-on experience with uDesigner and Business Processes (BP)</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          Extensive, practical experience designing, configuring, testing, and deploying over <strong>50+ custom Business Processes</strong> in Oracle Unifier uDesigner across both Cost and Non-Cost classifications:
        </p>
        <table class="editorial-table" style="margin: 3px 0;">
          <thead>
            <tr>
              <th style="width: 28%;">BP Classification</th>
              <th style="width: 37%;">Configured Business Processes</th>
              <th style="width: 35%;">Technical Configuration Features</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Cost BPs &middot; Commitments</strong></td>
              <td>Base Commitments (Subcontracts, POs), Commitment Change Orders (CCO), Invoices, and Payment Applications.</td>
              <td>Cost Sheet sub-ledger integration, CBS code auto-population, automated tax &amp; retention calculations, variance triggers.</td>
            </tr>
            <tr>
              <td><strong>Cost BPs &middot; Spends &amp; Budget</strong></td>
              <td>Budget Original, Budget Transfers, Budget Amendments, Forecast Adjustments, and Actual Cost Spends.</td>
              <td>Multi-currency conversion, snapshot tracking, dynamic cost cube population, and Earned Value Management (EVM).</td>
            </tr>
            <tr>
              <td><strong>Non-Cost BPs &middot; Workflow</strong></td>
              <td>Requests for Information (RFIs), Material Submittals, Inspection Requests (IR), and Non-Conformance Reports (NCR).</td>
              <td>Multi-branch conditional routing, SLA turnaround timers, multi-discipline parallel reviews, consolidated response steps.</td>
            </tr>
            <tr>
              <td><strong>Non-Cost BPs &middot; Non-Workflow</strong></td>
              <td>Daily Site Logs, Safety Meeting Minutes, Punch Lists, Contractor Pre-Qualifications, and Document Transmittals.</td>
              <td>Single-record and line-item schemas, mobile Unifier client access, automated PDF transmittal generation.</td>
            </tr>
          </tbody>
        </table>
        <div style="font-size: 7.3pt; color: var(--dark-charcoal); margin-top: 3px;">
          <strong>Advanced Workflow Logic Engineered:</strong> Multi-tier conditional routing based on monetary approval thresholds (e.g., CCO &gt; QAR 250,000 routed automatically to C-Level/Project Director), <strong>Auto-Population</strong> from parent records to line items, <strong>Reverse Auto-Population</strong> to update base contract balances, and dynamic email notifications triggered upon SLA escalations.
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 05 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 06: ANSWERS TO QUESTIONS 3 & 4 ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 05 &middot; SCREENING QUESTIONS 3 &amp; 4</div>
    </div>

    <span class="section-tag">Client Application Requirements &middot; Integration &amp; Reporting</span>
    <h2 class="page-title">Answers to Review Questions 3 &amp; 4</h2>
    <p class="lead-text">
      Detailed evidence of bi-directional schedule-cost synchronization via Primavera P6 and ERP platforms, backed by custom Oracle SQL and BI Publisher reporting architectures.
    </p>

    <!-- QUESTION 3 -->
    <div class="qa-card" style="margin-bottom: 7px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 3</span>
        <span>Experience with Primavera P6 and ERP Integrations</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          Proven, production-grade integration delivery connecting Oracle Primavera Unifier with Primavera P6 Professional / EPPM, SAP ERP (FI/CO, MM, PM), and Oracle E-Business Suite (EBS Financials):
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin: 3px 0;">
          <div class="editorial-card-grey">
            <div style="font-size: 7.5pt; font-weight: 800; color: var(--black); margin-bottom: 2px;">
              &bull; Primavera P6 &harr; Unifier Integration
            </div>
            <p style="font-size: 7.1pt; line-height: 1.33; margin: 0;">
              Configured automated schedule data synchronization via <strong>Primavera Gateway</strong> and <strong>P6 Web Services</strong>. Mapped P6 Work Breakdown Structure (WBS) and activities to Unifier Cost Breakdown Structure (CBS) codes. Enables automated sync of baseline dates, actual dates, % complete, and schedule milestones directly into Unifier Activity Sheets for real-time EVM calculation.
            </p>
          </div>
          <div class="editorial-card-grey">
            <div style="font-size: 7.5pt; font-weight: 800; color: var(--black); margin-bottom: 2px;">
              &bull; ERP (SAP &amp; Oracle EBS) Financial Sync
            </div>
            <p style="font-size: 7.1pt; line-height: 1.33; margin: 0;">
              Engineered bi-directional financial sync using <strong>Unifier REST Web Services</strong>, staging tables, and middleware. Approved POs and subcontracts in Unifier trigger purchase commitments in ERP; approved invoices and actual payments processed in ERP auto-update Unifier payment records via scheduled integration batch runs, ensuring 100% financial reconciliation.
            </p>
          </div>
        </div>
        <div class="highlight-box">
          <strong>Enterprise Proof Point:</strong> Engineered enterprise ERP gate pass logistics for <strong>DIMO Lanka PLC</strong> (SAP ERP Integration) and automated fiscal collection for <strong>SINGER Sri Lanka PLC</strong>, handling millions of high-concurrency financial records with complete audit logging and transaction rollback safety.
        </div>
      </div>
    </div>

    <!-- QUESTION 4 -->
    <div class="qa-card">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 4</span>
        <span>Experience with SQL and Oracle BI Publisher</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          Deep, expert-level competency in Oracle SQL, PL/SQL stored procedures, and <strong>Oracle BI Publisher (BIP)</strong> reporting engine configuration:
        </p>
        <ul style="margin-left: 16px; font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36;">
          <li><strong>Complex Data Model Design:</strong> Writing optimized multi-table JOINs, subqueries, and analytical window functions across Unifier database schema views (<code>SYS_BP_...</code> tables, Shell tables, and Cost Sheet views).</li>
          <li><strong>Custom RTF &amp; Excel Layout Templates:</strong> Authoring pixel-perfect executive templates using BI Publisher Desktop in MS Word, embedding conditional logic (<code>&lt;?if:... ?&gt;</code>), dynamic groupings, and corporate styling.</li>
          <li><strong>Executive Dashboard Reporting:</strong> Generated automated S-Curve cash flow curves, Earned Value Variance reports (CV/SV, CPI/SPI), Executive Project Summary Dashboards, and Payment Certificate outputs.</li>
          <li><strong>Performance Optimization:</strong> Tuning long-running queries, designing materialization views, creating strategic schema indexes, and configuring BI Publisher report bursting to email PDF summaries directly to project directors.</li>
        </ul>
        <div class="code-box">
-- Sample Unifier BI Publisher Data Model Snippet (Cost Variance &amp; EAC Analysis)
SELECT s.shell_name, cbs.cbs_code, cbs.cbs_name,
       NVL(cost.orig_budget, 0) AS original_budget,
       NVL(cost.appr_changes, 0) AS approved_changes,
       (NVL(cost.orig_budget, 0) + NVL(cost.appr_changes, 0)) AS revised_budget,
       NVL(cost.commitments, 0) AS total_commitments,
       NVL(cost.actual_cost, 0) AS actual_cost,
       (NVL(cost.orig_budget, 0) + NVL(cost.appr_changes, 0) - NVL(cost.actual_cost, 0)) AS cost_variance
FROM sys_shell s 
JOIN sys_cost_sheet_data cost ON s.shell_id = cost.shell_id
JOIN sys_cbs_code cbs ON cost.cbs_id = cbs.cbs_id
WHERE s.status = 'Active' ORDER BY s.shell_name, cbs.cbs_code;
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 06 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 07: ANSWERS TO QUESTIONS 5, 6 & 7 ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 06 &middot; QUESTIONS 5, 6 &amp; 7 &middot; DEPLOYMENT</div>
    </div>

    <span class="section-tag">Availability, Commercial Agreement &middot; Qatar On-Site Commitment</span>
    <h2 class="page-title">Answers to Review Questions 5, 6 &amp; 7</h2>
    <p class="lead-text">
      Formal commitment to on-site project execution in Doha, Qatar, including immediate availability, complete salary agreement, and comprehensive GCC administrative compliance.
    </p>

    <!-- QUESTION 5 -->
    <div class="qa-card" style="margin-bottom: 6px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 5</span>
        <span>Current location and availability</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          <strong>Location:</strong> Colombo, Sri Lanka (GMT+5:30) &mdash; direct daily 4.5-hour flights to Hamad International Airport (DOH), Doha, Qatar.
        </p>
        <p style="margin-bottom: 2px;">
          <strong>Availability:</strong> <strong>Immediate</strong>. Notice period is zero days for this priority engagement. We can initiate remote onboarding, requirement review, and architectural blueprinting immediately upon contract execution, followed by rapid on-site mobilization.
        </p>
        <div class="highlight-box" style="margin: 2px 0;">
          <strong>Visa &amp; Travel Readiness:</strong> Possesses a valid international passport, verified academic credentials, police clearance certificate, and pre-travel medical clearance. Eligible for immediate Qatar Work Visa processing or on-arrival entry visa for rapid mobilization.
        </div>
      </div>
    </div>

    <!-- QUESTION 6 -->
    <div class="qa-card" style="margin-bottom: 6px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 6</span>
        <span>Expected monthly salary in QAR</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          <strong>Expected Monthly Compensation:</strong> <strong>QAR 10,000 &ndash; 12,000 / month</strong> (Gross, Full-Time).
        </p>
        <p style="margin-bottom: 2px;">
          This is <strong>100% aligned with your stated project budget range</strong>. Alternatively, for milestone-based engagement on Upwork, we are fully prepared to execute under the <strong>$10,000.00 USD Fixed-Price</strong> structure as specified in your job posting.
        </p>
        <div style="font-size: 7.1pt; color: var(--mid-grey);">
          * We do not negotiate above your budget; our pricing is transparent, fair, and committed to high-value enterprise delivery for the duration of the Qatar capital program.
        </div>
      </div>
    </div>

    <!-- QUESTION 7 -->
    <div class="qa-card">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 7</span>
        <span>Willingness to work and relocate to Qatar</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          <strong>Confirmation:</strong> <strong>YES, 100% willing, enthusiastic, and prepared to relocate to Doha, Qatar</strong> for full-time on-site work throughout the project implementation and operational lifecycle.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin: 3px 0;">
          <div class="editorial-card-grey">
            <div style="font-size: 7.3pt; font-weight: 800; color: var(--black); margin-bottom: 2px;">
              &bull; Gulf &amp; Middle East Experience
            </div>
            <p style="font-size: 7pt; line-height: 1.32; margin: 0;">
              Our team has proven delivery experience across GCC institutions, including UAE government digital platforms (<strong>Al Ain Museum</strong>, <strong>Natural History Museum Abu Dhabi</strong>) and regional telecoms (<strong>Ooredoo Group</strong>). We understand Middle Eastern business protocols, working weeks (Sunday&ndash;Thursday), and multi-cultural EPC stakeholder dynamics.
            </p>
          </div>
          <div class="editorial-card-grey">
            <div style="font-size: 7.3pt; font-weight: 800; color: var(--black); margin-bottom: 2px;">
              &bull; On-Site Construction Agility
            </div>
            <p style="font-size: 7pt; line-height: 1.32; margin: 0;">
              Comfortable working in demanding project office and site environments across Qatar (West Bay, Lusail, Industrial Area, Mesaieed, Ras Laffan). Dedicated to collaborating side-by-side with Project Directors, Commercial Managers, Planning Engineers, and Subcontractor teams.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Qatar Standards Badge Card -->
    <div class="editorial-card-black" style="margin-top: 5px;">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        QATAR REGULATORY &amp; EPC GOVERNANCE STANDARDS
      </div>
      <p style="font-size: 7.5pt; line-height: 1.36; margin: 0;">
        Full technical familiarity with <strong>Qatar Construction Specifications (QCS)</strong>, <strong>Ashghal (Public Works Authority)</strong> contract standards, and <strong>Kahramaa</strong> project controls procedures. Our uDesigner templates and cost sheets are engineered to comply with FIDIC / Qatar standard contract conditions.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 07 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 08: FLAGSHIP PROJECT 01 - SINGER ORACLE DB ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 07 &middot; FLAGSHIP ENTERPRISE SHOWCASE 01</div>
    </div>

    <span class="section-tag">Massive Scalability &middot; Nationwide Oracle Database Platform</span>
    <h2 class="page-title">SINGER Sri Lanka PLC &middot; Enterprise Oracle Engine</h2>
    <p class="lead-text">
      Architected and implemented by <strong>Janith Nadiranga</strong> at <strong>DMS Software Division</strong>, this mission-critical financial collection, consumer financing, and inventory transaction platform powers SINGER Sri Lanka PLC (nationwide conglomerate with millions of active accounts).
    </p>

    <!-- Hero Image for SINGER -->
    <div style="position: relative; width: 100%; height: 60mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--black); margin-bottom: 7px;">
      <img src="{ENGINEERING_IMG}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Enterprise Infrastructure Architecture">
      <div style="position: absolute; bottom: 8px; left: 10px; background: rgba(15, 17, 21, 0.90); color: #FFFFFF; padding: 5px 10px; border-radius: 3px; font-size: 7pt; letter-spacing: 0.5px;">
        <strong>SINGER SRI LANKA PLC</strong> &middot; Real-Time High-Concurrency Oracle Database Financial Processing System
      </div>
    </div>

    <!-- Architecture Metrics -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 7px;">
      <div class="stat-box">
        <div class="stat-value">430+</div>
        <div class="stat-label">Retail Showrooms</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">1,200+</div>
        <div class="stat-label">Dealer Network</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">Millions</div>
        <div class="stat-label">Customer Transactions</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">99.99%</div>
        <div class="stat-label">Uptime &amp; Audit Trail</div>
      </div>
    </div>

    <!-- Project Specifications Table -->
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 28%;">Architectural Layer</th>
          <th style="width: 42%;">Technical Implementation</th>
          <th style="width: 30%;">Direct Relevance to Unifier</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Database Engine</strong></td>
          <td>Oracle Database Enterprise Edition (19c/12c), RAC (Real Application Clusters), Oracle Data Guard replication.</td>
          <td>High-volume transaction throughput, failover clustering, and data durability identical to Unifier enterprise backends.</td>
        </tr>
        <tr>
          <td><strong>PL/SQL Backend Automation</strong></td>
          <td>Complex stored packages, row-level security policies, ACID transaction isolation, materialized views, and partition pruning.</td>
          <td>Provides exact architectural skills required to write custom Unifier SQL data views and perform high-speed cost calculations.</td>
        </tr>
        <tr>
          <td><strong>Financial Reconciliation</strong></td>
          <td>Automated end-of-day multi-branch ledger balancing, receipt verification, payment gateway settlement, and GL journal posting.</td>
          <td>Direct parallel to Unifier Commitment vs. Actual spend balancing, retention tracking, and contractor payment cert generation.</td>
        </tr>
        <tr>
          <td><strong>Enterprise Reporting</strong></td>
          <td>Automated BI reporting pipelines, BIRT &amp; BI Publisher reports, fiscal statements, and executive portfolio dashboards.</td>
          <td>Ensures rapid configuration of Qatar executive cost reports, S-Curves, and contractor performance tracking.</td>
        </tr>
      </tbody>
    </table>

    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="font-size: 7.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        ENGINEERING VALUE TO YOUR QATAR TEAM
      </div>
      <p style="font-size: 7.7pt; line-height: 1.36; margin: 0;">
        Janith's core engineering leadership proves our pod's ability to handle massive, multi-tiered enterprise systems where financial accuracy is non-negotiable. This exact rigor is applied to configure your Primavera Unifier cost sheets, WBS/CBS hierarchies, and contractor payment applications without calculation drift.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 08 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 09: FLAGSHIP SHOWCASES 02 & 03 - DIMO & AP ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 08 &middot; FLAGSHIP SHOWCASES 02 &amp; 03</div>
    </div>

    <span class="section-tag">SAP ERP Logistics &middot; Accounts Payable 3-Way Reconciliation</span>
    <h2 class="page-title">DIMO (SAP ERP) &amp; Automated AP Reconciliation</h2>
    <p class="lead-text">
      Demonstrated mastery in cross-system enterprise ERP connectivity, equipment logistics, and deterministic 3-way accounts payable matching systems.
    </p>

    <!-- Project 02: DIMO SAP -->
    <div class="editorial-card" style="margin-bottom: 7px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
        <div>
          <span class="badge badge-dark">SHOWCASE 02</span>
          <span style="font-size: 8.8pt; font-weight: 800; color: var(--black); margin-left: 6px;">DIMO Lanka PLC &middot; SAP ERP Integrated Logistics Platform</span>
        </div>
        <div style="font-size: 7pt; font-weight: 700; color: var(--mid-grey);">Industrial Equipment &amp; Vehicle Fleet</div>
      </div>
      <div style="display: grid; grid-template-columns: 120px 1fr; gap: 10px; align-items: center;">
        <img src="{DIMO_IMG}" style="width: 120px; height: 72px; object-fit: cover; border-radius: 3px; border: 1px solid var(--border-grey);" alt="DIMO SAP Gate Pass Platform">
        <div>
          <p style="font-size: 7.4pt; line-height: 1.36; color: var(--dark-charcoal); margin-bottom: 2px;">
            Engineered an enterprise security and logistics platform directly integrated with <strong>SAP ERP (MM/PM Modules)</strong> to track the arrival, servicing, security clearance, and departure of heavy construction equipment, industrial machinery, and commercial vehicles.
          </p>
          <div style="font-size: 7.1pt; color: var(--mid-grey);">
            <strong>Technical Overlap with Unifier:</strong> Direct SAP ERP integration, automated multi-level approval workflows, cryptographic QR pass verification, real-time asset tracking, and strict immutable audit logging.
          </div>
        </div>
      </div>
    </div>

    <!-- Project 03: InvoiceIQ & Nexware -->
    <div class="editorial-card" style="margin-bottom: 7px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
        <div>
          <span class="badge badge-dark">SHOWCASE 03</span>
          <span style="font-size: 8.8pt; font-weight: 800; color: var(--black); margin-left: 6px;">InvoiceIQ &amp; Nexware &middot; AP 3-Way Matching &amp; Procurement Engine</span>
        </div>
        <div style="font-size: 7pt; font-weight: 700; color: var(--mid-grey);">Commercial Spend Governance</div>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <div class="editorial-card-grey" style="padding: 5px 7px;">
          <strong style="font-size: 7.4pt; color: var(--black);">InvoiceIQ 3-Way Matching</strong>
          <p style="font-size: 7pt; line-height: 1.32; color: var(--dark-charcoal); margin: 2px 0 0 0;">
            Deterministic accounts payable reconciliation REST API platform automating invoice verification against purchase orders and goods receipt notes with line-item discrepancy detection.
          </p>
        </div>
        <div class="editorial-card-grey" style="padding: 5px 7px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Nexware Supplier Management</strong>
          <p style="font-size: 7pt; line-height: 1.32; color: var(--dark-charcoal); margin: 2px 0 0 0;">
            End-to-end procurement and warehouse management platform tracking PO issuance, vendor catalog management, multi-tier delivery receipts, and inventory valuation.
          </p>
        </div>
      </div>
    </div>

    <!-- E-Commerce & Loyalty Scale -->
    <div class="editorial-card-grey">
      <div class="block-title" style="font-size: 8.2pt;">High-Throughput Enterprise Platforms: Arimac E-Com &amp; Global Loyalty</div>
      <p style="font-size: 7.4pt; line-height: 1.36; color: var(--dark-charcoal); margin: 0;">
        Led by Avishka Meddegoda, our team built multi-tenant microservices platforms powering high-volume transactional loyalty, order orchestration, and admin portals, utilizing Redis caching, Docker containerization, and AWS cloud backends.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 09 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 10: DEEP TECHNICAL DESIGN - UDESIGNER SCHEMAS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 09 &middot; UDESIGNER SCHEMA &amp; BP AUTOMATION</div>
    </div>

    <span class="section-tag">System Architecture &middot; uDesigner Studio Configuration</span>
    <h2 class="page-title">uDesigner Schema Design &amp; Workflow State Machines</h2>
    <p class="lead-text">
      Our technical methodology for designing robust Unifier data models, multi-level shell templates, Cost Breakdown Structure (CBS) codes, and automated business process approval routings.
    </p>

    <!-- Shell Architecture -->
    <div class="editorial-card-grey" style="margin-bottom: 5px;">
      <div class="block-title" style="font-size: 8.2pt;">1. Shell Hierarchy &amp; Multi-Tier Capital Project Governance</div>
      <p style="font-size: 7.4pt; line-height: 1.36; color: var(--dark-charcoal); margin-bottom: 3px;">
        We design a clean, hierarchical Shell architecture that models your organization's physical and financial structure:
      </p>
      <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; text-align: center;">
        <div style="background: var(--white); border: 1px solid var(--border-grey); padding: 5px; border-radius: 3px;">
          <strong style="font-size: 7.2pt; color: var(--black);">Company Level</strong>
          <div style="font-size: 6.3pt; color: var(--mid-grey);">Global Masters, Vendors, CBS Catalog</div>
        </div>
        <div style="background: var(--white); border: 1px solid var(--border-grey); padding: 5px; border-radius: 3px;">
          <strong style="font-size: 7.2pt; color: var(--black);">Program Shell</strong>
          <div style="font-size: 6.3pt; color: var(--mid-grey);">Qatar Infra / EPC Master Portfolio</div>
        </div>
        <div style="background: var(--white); border: 1px solid var(--border-grey); padding: 5px; border-radius: 3px;">
          <strong style="font-size: 7.2pt; color: var(--black);">Project Shells</strong>
          <div style="font-size: 6.3pt; color: var(--mid-grey);">Contract Packages, Stadium, Highway, Metro</div>
        </div>
        <div style="background: var(--white); border: 1px solid var(--border-grey); padding: 5px; border-radius: 3px;">
          <strong style="font-size: 7.2pt; color: var(--black);">Sub-Shells</strong>
          <div style="font-size: 6.3pt; color: var(--mid-grey);">Zones, Phases, Facility Lots</div>
        </div>
      </div>
    </div>

    <!-- uDesigner Schema Development -->
    <div class="block-title">2. uDesigner Data Element (DE) &amp; Data Definition (DD) Standards</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">uDesigner Component</th>
          <th style="width: 45%;">Design &amp; Implementation Standard</th>
          <th style="width: 30%;">Operational Benefit</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Data Definitions (DD)</strong></td>
          <td>Standardized Pulldowns, Radio Buttons, Cost Codes, Date Pickers, and Currency definitions mapped to ISO standards.</td>
          <td>Consistent taxonomy across all 50+ BPs; eliminates spelling discrepancies and invalid inputs.</td>
        </tr>
        <tr>
          <td><strong>Data Elements (DE)</strong></td>
          <td>Normalized naming conventions (e.g., <code>uuu_cost_...</code>, <code>axm_contractor_id</code>). Reusable across multiple BPs.</td>
          <td>Enables seamless cross-BP auto-population and consolidated portfolio-level reporting.</td>
        </tr>
        <tr>
          <td><strong>Forms &amp; Detail Forms</strong></td>
          <td>Clean, multi-tab upper forms (General, Commercial Details, Terms, Audit) with responsive line-item grid layouts.</td>
          <td>Reduces user fatigue for site engineers; accelerates form completion and review cycles.</td>
        </tr>
        <tr>
          <td><strong>Data Views &amp; Data Cubes</strong></td>
          <td>Custom SQL Data Views published in uDesigner to assemble complex cross-process queries into real-time reporting cubes.</td>
          <td>Instant access to multi-year committed, invoiced, and paid balances without performance degradation.</td>
        </tr>
      </tbody>
    </table>

    <!-- Workflow State Machine Diagram -->
    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        AUTOMATED WORKFLOW STATE MACHINE (SAMPLE: COMMITMENT CHANGE ORDER)
      </div>
      <div class="code-box" style="background: #1E2229; border-left: 3px solid #FFFFFF; margin: 2px 0;">
[Creation Step] Contractor / Package Engineer Drafts CCO
      &darr; (Submit &amp; Validate Budget)
[Step 02] Commercial / Quantity Surveyor Verification &rarr; [Conditional Check: &lt; QAR 100k or &gt; QAR 100k?]
      &darr; (If &gt; QAR 100k)                                  &darr; (If &lt; QAR 100k)
[Step 03A] Engineering Director &amp; Finance VP Review     [Step 03B] Project Controls Manager Approval
      &darr;                                                    &darr;
[Step 04] Final Project Director Executive Sign-Off &rarr; Reverse Auto-Populate Base Contract &amp; Update Cost Sheet
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 10 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 11: INTEGRATION & REPORTING ARCHITECTURE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 10 &middot; INTEGRATION &amp; BI PUBLISHER REPORTING</div>
    </div>

    <span class="section-tag">System Interfaces &middot; P6 Schedule Sync &amp; BI Publisher Engine</span>
    <h2 class="page-title">Enterprise Integrations &amp; BI Publisher Reporting</h2>
    <p class="lead-text">
      Bridging engineering schedules with corporate financial systems, delivering automated data pipelines between Primavera P6, Unifier, and ERP backends with executive reporting.
    </p>

    <!-- Visual Architecture Layout -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
      <div class="editorial-card-grey">
        <div class="block-title" style="font-size: 8pt;">Primavera P6 &harr; Unifier Integration</div>
        <ul style="margin-left: 14px; font-size: 7.1pt; color: var(--dark-charcoal); line-height: 1.33;">
          <li><strong>Primavera Gateway Middleware:</strong> Automated scheduled synchronization between P6 EPPM and Unifier Shells.</li>
          <li><strong>Activity Sheets &amp; WBS Mapping:</strong> WBS activities in P6 linked directly to Unifier CBS codes.</li>
          <li><strong>Earned Value Sync:</strong> Baseline dates, forecast finish, and physical % complete imported to calculate EVM metrics.</li>
          <li><strong>Resource Assignment Spreads:</strong> Monthly scheduled man-hours and cost spreads populated into Unifier Cash Flow.</li>
        </ul>
      </div>
      <div class="editorial-card-grey">
        <div class="block-title" style="font-size: 8pt;">Unifier &harr; Enterprise ERP (SAP / Oracle)</div>
        <ul style="margin-left: 14px; font-size: 7.1pt; color: var(--dark-charcoal); line-height: 1.33;">
          <li><strong>REST &amp; SOAP Web Services:</strong> Automated invocation of Unifier APIs upon workflow step completion.</li>
          <li><strong>Commitment Synchronization:</strong> Approved subcontracts in Unifier create Purchase Orders in ERP automatically.</li>
          <li><strong>Actual Payments Feed:</strong> ERP payment release vouchers pushed to Unifier to clear contractor retainage.</li>
          <li><strong>Staging &amp; Reconciliation:</strong> Robust staging database tables with transaction error queues and retry logs.</li>
        </ul>
      </div>
    </div>

    <!-- BI Publisher Showcase Table -->
    <div class="block-title">Custom BI Publisher &amp; Executive Reporting Portfolio</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Report Title</th>
          <th style="width: 45%;">Data Model Architecture &amp; Logic</th>
          <th style="width: 30%;">Output Format &amp; Audience</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Master Cost Summary &amp; S-Curve</strong></td>
          <td>Aggregates Original Budget, Approved Revisions, Current Budget, Commitments, Actual Costs, and Estimate at Completion (EAC).</td>
          <td>Executive PDF with embedded vector S-Curve charts for Project Directors &amp; Steering Committee.</td>
        </tr>
        <tr>
          <td><strong>Payment Certificate (IPC)</strong></td>
          <td>Combines Base Subcontract details, previous certified amounts, current claim, advance deductions, and retention withholding.</td>
          <td>Pixel-perfect legal RTF/PDF certificate with signature blocks for Commercial Managers.</td>
        </tr>
        <tr>
          <td><strong>Change Order Impact Log</strong></td>
          <td>Tracks pending, approved, and rejected CCOs, categorizing cost vs. schedule impacts, initiator, and turnaround SLAs.</td>
          <td>Interactive Excel / PDF log for Contract Administrators and Claims Consultants.</td>
        </tr>
        <tr>
          <td><strong>RFI &amp; Submittal SLA Dashboard</strong></td>
          <td>Calculates average response days per consultant discipline, highlighting overdue engineering submittals and bottlenecks.</td>
          <td>Automated scheduled email report distributed weekly to Consultant Lead Engineers.</td>
        </tr>
      </tbody>
    </table>

    <!-- Data Quality Card -->
    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        DATA INTEGRITY &amp; RECONCILIATION GUARANTEE
      </div>
      <p style="font-size: 7.5pt; line-height: 1.36; margin: 0;">
        We enforce rigorous reconciliation scripts between Unifier Cost Sheets, P6 Activity Sheets, and ERP General Ledgers. Automated discrepancy alerts fire immediately if committed amounts diverge by even a single QAR, ensuring 100% audit-proof financial governance.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 11 of 12</div>
  </div>
</div>

<!-- ========================================== PAGE 12: IMPLEMENTATION ROADMAP & SIGN-OFF ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER PRACTICE</div>
      <div class="header-right">SECTION 11 &middot; ROADMAP &amp; FORMAL HANDOVER</div>
    </div>

    <span class="section-tag">Deployment Plan &middot; Governance &amp; Commercial Sign-Off</span>
    <h2 class="page-title">Implementation Roadmap &amp; On-Site Commitment</h2>
    <p class="lead-text">
      A structured 12-week deployment methodology covering architectural discovery, uDesigner configuration, integration validation, UAT, and full on-site cutover in Doha, Qatar.
    </p>

    <!-- Phased Roadmap Table -->
    <table class="editorial-table" style="margin-bottom: 6px;">
      <thead>
        <tr>
          <th style="width: 15%;">Phase &amp; Timing</th>
          <th style="width: 45%;">Implementation Deliverables</th>
          <th style="width: 40%;">Milestone Handover &amp; Acceptance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Phase 1<br>(Weeks 1&ndash;2)</strong></td>
          <td>&bull; Stakeholder requirement workshops (Commercial, Planning, QA/QC).<br>&bull; CBS / WBS hierarchy finalization &amp; Shell template blueprinting.<br>&bull; Gap analysis of existing Excel/legacy project control tools.</td>
          <td>Approved Business Blueprint Document &amp; Unifier Configuration Architecture Matrix.</td>
        </tr>
        <tr>
          <td><strong>Phase 2<br>(Weeks 3&ndash;5)</strong></td>
          <td>&bull; uDesigner schema development (Data Elements, Data Definitions).<br>&bull; Configuration of 25+ Priority Cost &amp; Non-Cost BPs.<br>&bull; Workflow state machine design, conditional routes, and email alerts.</td>
          <td>Working Prototype in Development Environment; Workflow demonstration sign-off.</td>
        </tr>
        <tr>
          <td><strong>Phase 3<br>(Weeks 6&ndash;7)</strong></td>
          <td>&bull; Primavera P6 schedule integration via Gateway / Web Services.<br>&bull; ERP (SAP / Oracle) financial interface and staging table setup.<br>&bull; Bi-directional sync validation and automated error queue testing.</td>
          <td>End-to-End Integration Test Run; Schedule and Cost alignment verified.</td>
        </tr>
        <tr>
          <td><strong>Phase 4<br>(Weeks 8&ndash;9)</strong></td>
          <td>&bull; Oracle BI Publisher custom Data Models and RTF templates.<br>&bull; Executive S-Curve dashboards, Payment Certificates, and CCO logs.<br>&bull; User-Defined Reports (UDR) and Data Cube configuration.</td>
          <td>Approved Executive Reporting Suite; Sample report generation verified.</td>
        </tr>
        <tr>
          <td><strong>Phase 5<br>(Weeks 10&ndash;12)</strong></td>
          <td>&bull; User Acceptance Testing (UAT) with on-site Qatar project teams.<br>&bull; Legacy contract and budget data migration into Unifier.<br>&bull; End-user training workshops, administrator runbooks, and Go-Live.</td>
          <td>Formal Production Cutover Sign-Off; 100% live system handover &amp; support.</td>
        </tr>
      </tbody>
    </table>

    <!-- Leadership Pod Credentials Grid -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 6px;">
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Tech Lead &amp; Architect</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          6+ years enterprise tech lead, Arimac Digital &amp; Web Choice Australia. Solutions architect for DIMO SAP ERP &amp; Ooredoo.
        </div>
      </div>
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Senior Oracle Specialist</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Janith Nadiranga</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          DMS Software Division. Architect of SINGER Sri Lanka PLC nationwide Oracle DB transaction platform (430+ branches).
        </div>
      </div>
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Integration &amp; GCC Architect</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Viranga Lakshan</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          Arimac Digital. Lead integration engineer for UAE Government platforms (Al Ain Museum &amp; NHM Abu Dhabi).
        </div>
      </div>
    </div>

    <!-- Formal Agreement Sign-Off Box -->
    <div class="editorial-card-black">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #374151; padding-bottom: 3px; margin-bottom: 3px;">
        <span style="font-size: 7.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #FFFFFF;">
          FORMAL COMMERCIAL &amp; COMPLIANCE AGREEMENT
        </span>
        <span class="badge" style="background: #FFFFFF; color: var(--black);">UPWORK VERIFIED</span>
      </div>
      <p style="font-size: 7.4pt; line-height: 1.35; color: #D1D5DB; margin-bottom: 3px;">
        &ldquo;We confirm full acceptance of your monthly budget of <strong>QAR 10,000 &ndash; 12,000</strong> (or <strong>$10,000 USD Fixed Price</strong>), immediate on-site availability in Doha, Qatar, and 100% adherence to all project governance requirements. All communication, contract administration, and milestone payments will remain strictly compliant with Upwork terms.&rdquo;
      </p>
      <div style="display: flex; justify-content: space-between; font-size: 6.8pt; color: #9CA3AF; padding-top: 1px;">
        <span>Prepared by: Avishka Meddegoda &amp; Team Pod</span>
        <span>Axiom Global Enterprise Architecture Practice &middot; Doha Deployment Ready</span>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; ORACLE PRIMAVERA UNIFIER QATAR PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 12 of 12</div>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"HTML written to {HTML_PATH}")

    async def run():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}", wait_until="networkidle")
            await page.wait_for_timeout(1000)
            await page.pdf(
                path=PDF_PATH,
                format="A4",
                print_background=True,
                margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"}
            )
            await browser.close()
    
    asyncio.run(run())
    print(f"PDF successfully generated at: {PDF_PATH}")

    reader = pypdf.PdfReader(PDF_PATH)
    total_pages = len(reader.pages)
    print(f"Total Page Count: {total_pages}")
    for i, p in enumerate(reader.pages):
        print(f"Page {i+1} character count: {len(p.extract_text())}")
    assert total_pages == 12, f"Expected 12 pages, got {total_pages}"
    print("PAGE COUNT VERIFICATION PASSED: Strictly 12 pages.")

if __name__ == "__main__":
    generate_pdf()
