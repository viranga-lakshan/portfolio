# -*- coding: utf-8 -*-
"""
Axiom Global Enterprise Architecture Practice
Reynolds Precision Engineering Ltd - B2B Engineering Parts Ordering Website Proposal
Executive 10-Page Luxury Monochrome Proposal with Full Team Profiles, Live E-Commerce Platforms & Color Imagery
Featuring Moolee - Your Favorite Marketplace (moolee.mv) & SINGER Sri Lanka PLC (singersl.com)
Created by Avishka Meddegoda (Technical Lead & Senior Software Engineer, 6+ Years Experience)
"""

import os
import asyncio
from playwright.async_api import async_playwright
import pypdf

BASE_DIR = r"c:\Users\Viranga\Downloads\upwrok new\Reynolds_Precision_Engineering_B2B_Ordering_Proposal"
IMG_DIR = os.path.join(BASE_DIR, "images")
HTML_PATH = os.path.join(BASE_DIR, "reynolds_b2b_proposal_template.html")
PDF_PATH = os.path.join(BASE_DIR, "Reynolds_Precision_Engineering_B2B_Ordering_Proposal.pdf")

def to_uri(fname):
    return os.path.join(IMG_DIR, fname).replace("\\", "/")

LOGO_IMG = to_uri("axiom_logo.png")
HERO_IMG = to_uri("industrial_engineering.jpg")
PARTS_IMG = to_uri("precision_parts.jpg")
TEAM_IMG = to_uri("team_office.jpg")
DIMO_IMG = to_uri("portfolio_dimo_sap.png")
ALAIN_IMG = to_uri("portfolio_alain_museum.png")
HOLSTEN_IMG = to_uri("portfolio_holsten.png")
MOOLEE_IMG = to_uri("moolee_live_screenshot.png")
BANNER_FULL = to_uri("banner_fullstack.png")
BANNER_ENT = to_uri("banner_enterprise.png")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>REYNOLDS PRECISION ENGINEERING LTD &middot; B2B PARTS ORDERING WEBSITE PROPOSAL</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

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
  font-size: 8.2pt;
  line-height: 1.38;
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
  font-size: 16.5pt;
  font-weight: 700;
  line-height: 1.14;
  color: var(--black);
  margin-bottom: 4px;
}}

.lead-text {{
  font-size: 8.4pt;
  line-height: 1.38;
  color: var(--dark-charcoal);
  margin-bottom: 6px;
  max-width: 98%;
}}

.block-title {{
  font-size: 8.8pt;
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
  font-size: 7.4pt;
  margin-bottom: 5px;
}}

table.editorial-table th {{
  background: var(--black);
  color: var(--white);
  text-align: left;
  padding: 4px 7px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 6.5pt;
}}

table.editorial-table td {{
  padding: 3.8px 7px;
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
  padding: 5px 8px;
  background: #F9FAFB;
  margin-bottom: 4px;
}}

.editorial-card-black {{
  background: var(--black);
  color: var(--white);
  border-radius: 4px;
  padding: 6px 10px;
  margin-bottom: 5px;
}}

.editorial-card-black h3, .editorial-card-black h4 {{ color: var(--white); }}
.editorial-card-black p {{ color: #D1D5DB; }}

/* Badges & Links */
.badge {{
  display: inline-block;
  font-size: 6.2pt;
  font-weight: 800;
  padding: 2px 5px;
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

.live-link {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.4pt;
  font-weight: 700;
  color: #166534;
  background: #F0FDF4;
  padding: 1px 4px;
  border-radius: 2px;
  border: 1px solid #BBF7D0;
  text-decoration: none;
  display: inline-block;
}}

a {{
  color: inherit;
}}

.code-box {{
  background: #0F1115;
  color: #F3F4F6;
  padding: 5px 8px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.4pt;
  line-height: 1.34;
  border-left: 3px solid var(--black);
  margin: 3px 0 4px 0;
}}

.stat-box {{
  border: 1px solid var(--border-grey);
  background: #F9FAFB;
  padding: 4px 6px;
  border-radius: 4px;
  text-align: center;
}}

.stat-value {{
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 14pt;
  font-weight: 700;
  color: var(--black);
  line-height: 1.1;
}}

.stat-label {{
  font-size: 6pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--mid-grey);
  margin-top: 1px;
}}

.qa-card {{
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 5px 8px;
  background: var(--white);
  margin-bottom: 4px;
}}

.qa-question {{
  font-size: 7.8pt;
  font-weight: 800;
  color: var(--black);
  margin-bottom: 2px;
  display: flex;
  align-items: center;
  gap: 5px;
}}

.qa-answer {{
  font-size: 7.4pt;
  line-height: 1.35;
  color: var(--dark-charcoal);
}}

.highlight-box {{
  background: #F4F5F7;
  border-left: 3px solid var(--black);
  padding: 4px 7px;
  margin: 3px 0 4px 0;
  font-size: 7.3pt;
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
          <div style="font-family: 'Playfair Display', Georgia, serif; font-size: 14pt; font-weight: 700; letter-spacing: -0.5px; color: var(--black);">
            AXIOM GLOBAL
          </div>
          <div style="font-size: 6.8pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--mid-grey);">
            ENTERPRISE ARCHITECTURE &amp; B2B COMMERCE PRACTICE
          </div>
        </div>
      </div>
      <div style="text-align: right;">
        <span class="badge badge-dark" style="padding: 3px 8px; font-size: 7pt; letter-spacing: 1px;">
          OFFICIAL PROPOSAL &middot; FIXED PRICE &pound;2,000 GBP
        </span>
        <div style="font-size: 6.8pt; color: var(--mid-grey); margin-top: 3px; font-family: 'JetBrains Mono', monospace;">
          REF: REYNOLDS-B2B-2026-V1 &middot; CONFIDENTIAL
        </div>
      </div>
    </div>

    <!-- Editorial Kicker & Proposal Title -->
    <div style="margin-bottom: 12px;">
      <div style="display: inline-flex; align-items: center; gap: 6px; margin-bottom: 5px;">
        <span class="badge badge-outline" style="font-size: 6.8pt; font-weight: 800; letter-spacing: 1px;">NORTHERN IRELAND PRECISION CNC</span>
        <span style="font-size: 7.2pt; font-weight: 600; color: var(--mid-grey);">&middot; UPWORK CLIENT SPECIFICATION</span>
      </div>
      <h1 style="font-family: 'Playfair Display', Georgia, serif; font-size: 25pt; font-weight: 700; line-height: 1.1; letter-spacing: -0.8px; color: var(--black); margin-bottom: 8px;">
        B2B Engineering Parts<br>Online Ordering Website
      </h1>
      <p style="font-size: 9.6pt; line-height: 1.45; color: var(--dark-charcoal); max-width: 95%;">
        Architectural Blueprint, Technical Scope, and Full Delivery Plan for <strong>Reynolds Precision Engineering Ltd</strong>. Seamlessly enabling existing and future manufacturing, food processing, and industrial clients to order replacement components with customer-specific pricing, PO checkout, and instant PDF drawing access.
      </p>
    </div>

    <!-- Full-Color Hero Photography of Precision Engineering -->
    <div style="position: relative; border-radius: 5px; overflow: hidden; border: 1.5px solid var(--black); margin-bottom: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
      <img src="{HERO_IMG}" style="width: 100%; height: 185px; object-fit: cover; display: block;" alt="Reynolds Precision Engineering Workshop">
      <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(15,17,21,0.92) 0%, rgba(15,17,21,0.4) 60%, transparent 100%); padding: 12px 14px; color: var(--white);">
        <div style="font-size: 6.8pt; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: #E5E7EB;">
          ENGINEERED FOR REYNOLDS PRECISION ENGINEERING LTD &middot; NORTHERN IRELAND, UK
        </div>
        <div style="font-size: 11pt; font-weight: 700; color: #FFFFFF; margin-top: 1px;">
          High-Precision Replacement Components, CNC Machined Parts &amp; B2B Procurement Portal
        </div>
      </div>
    </div>

    <!-- Client & Proposal Metadata Strip -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; border: 1px solid var(--border-grey); background: var(--light-grey); border-radius: 4px; padding: 8px 10px; margin-bottom: 12px;">
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Client</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Reynolds Precision Engineering Ltd</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Northern Ireland, United Kingdom</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Commercial Terms</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">&pound;2,000 GBP Fixed-Price</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Escrow Milestones ($2,600 USD)</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Technical Lead</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Tech Lead (6+ Years Software Eng)</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Project Schedule</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Kickoff Pre-Christmas 2026</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">4&ndash;5 Weeks Delivery &amp; Handover</div>
      </div>
    </div>

    <div class="page-footer" style="border-top: 1px solid var(--border-grey); padding-top: 5px;">
      <div class="footer-left">AXIOM GLOBAL &middot; B2B E-COMMERCE PRACTICE &middot; CONFIDENTIAL &amp; PROPRIETARY</div>
      <div class="footer-page-num">Page 01 of 10</div>
    </div>
  </div>
</div>

<!-- ========================================== PAGE 02: EXECUTIVE SUMMARY & REQUIREMENTS MATRIX ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 01 &middot; EXECUTIVE ARCHITECTURE SUMMARY</div>
    </div>

    <span class="section-tag">Northern Ireland Precision CNC &middot; B2B Digital Transformation</span>
    <h2 class="page-title">Executive Summary &amp; Requirements Alignment Matrix</h2>
    <p class="lead-text">
      We propose a high-performance, secure, and intuitive <strong>B2B Engineering Parts Ordering Portal</strong> engineered specifically for <strong>Reynolds Precision Engineering Ltd</strong>. Designed to eliminate friction in replacement component procurement across manufacturing, food processing, and industrial sectors, our solution equips your commercial buyers with secure multi-location logins, contracted pricing matrices, downloadable engineering drawings, and frictionless purchase order checkout without requiring upfront credit card payments.
    </p>

    <!-- Stat Highlights -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 7px;">
      <div class="stat-box">
        <div class="stat-value">6+ Yrs</div>
        <div class="stat-label">Enterprise Tech Leadership</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">&pound;2,000</div>
        <div class="stat-label">Fixed-Price ($2,600 USD)</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">100%</div>
        <div class="stat-label">Code &amp; Admin Ownership</div>
      </div>
      <div class="stat-box">
        <div class="stat-value">Pre-Xmas</div>
        <div class="stat-label">2026 Kickoff Guaranteed</div>
      </div>
    </div>

    <!-- Core Requirements Matrix Table -->
    <div class="block-title">Main Website Requirements Alignment Matrix</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Website Requirement</th>
          <th style="width: 45%;">Technical Implementation Approach</th>
          <th style="width: 30%;">Operational Value to Reynolds</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Secure Customer Login</strong></td>
          <td>Role-based access control (RBAC), multi-location parent/child account hierarchy, company tax/registration verification, and secure password reset.</td>
          <td>Corporate customers manage multiple factory locations while ensuring pricing confidentiality.</td>
        </tr>
        <tr>
          <td><strong>2. Engineering Parts Catalogue</strong></td>
          <td>Categorized parts database, high-res photography, material specs (e.g., 316 Stainless, Acetal, PEEK, Tool Steel), part numbers, and downloadable PDF engineering drawings.</td>
          <td>Engineers and plant managers immediately verify exact technical dimensions before ordering.</td>
        </tr>
        <tr>
          <td><strong>3. Online Ordering &amp; PO Flow</strong></td>
          <td>Shopping basket with mandatory <strong>Company PO Number input</strong>, account invoicing terms, automatic branded PDF order confirmations, and 1-click repeat reordering.</td>
          <td>Eliminates administrative email back-and-forth and manual order transcription errors.</td>
        </tr>
        <tr>
          <td><strong>4. Individual Customer Pricing</strong></td>
          <td>Customer-specific price tiers and contracted price lists visible only when logged in; public visitors see catalog or request quotation.</td>
          <td>Protects negotiated commercial terms while providing instant automated ordering for authorized buyers.</td>
        </tr>
        <tr>
          <td><strong>5. Stock &amp; Lead Times</strong></td>
          <td>Dual status inventory logic: Available stock quantities shown for off-the-shelf items, with dynamic manufacturing lead times for Made-to-Order (MTO) CNC components.</td>
          <td>Enables customers to order replacement parts even when they need to be machined, managing delivery expectations.</td>
        </tr>
        <tr>
          <td><strong>6. Admin Dashboard &amp; Security</strong></td>
          <td>Intuitive, responsive admin dashboard to manage products, bulk update price lists, upload drawings, track order stages, and manage customer accounts with UK GDPR compliance.</td>
          <td>Reynolds' workshop and office team can operate, update, and manage the website with zero technical overhead.</td>
        </tr>
      </tbody>
    </table>

    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="font-size: 7.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        COMMERCIAL &amp; VALUE-FOR-MONEY COMMITMENT
      </div>
      <p style="font-size: 7.6pt; line-height: 1.35; margin: 0;">
        We fully agree to your <strong>&pound;2,000 GBP ($2,600 USD) Fixed-Price</strong> budget. Created by <strong>Avishka Meddegoda</strong> (Technical Lead, 6+ years experience), our squad brings proven delivery from premier software engineering firms (Arimac Digital &amp; DMS Software Division), with live platforms including Moolee Marketplace (<a href="https://www.moolee.mv/" style="color: #4ADE80; font-weight: 700;">moolee.mv</a>), SINGER Sri Lanka PLC (<a href="https://www.singersl.com/" style="color: #4ADE80; font-weight: 700;">singersl.com</a>), and DIMO Lanka PLC (<a href="https://www.dimolanka.com/" style="color: #4ADE80; font-weight: 700;">dimolanka.com</a>).
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 02 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 03: THE SQUAD - OUR CORE TEAM MEMBERS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 02 &middot; THE ENGINEERING SQUAD</div>
    </div>

    <span class="section-tag">Senior Software Engineering Pod &middot; Multi-Disciplinary Delivery</span>
    <h2 class="page-title">The Engineering Squad &middot; Core Team Profiles</h2>
    <p class="lead-text">
      Led by Technical Lead <strong>Avishka Meddegoda</strong>, our 5-person engineering pod combines full-stack e-commerce architecture, enterprise database engineering, and agile project delivery from Sri Lanka's premier technology houses.
    </p>

    <!-- Team Grid (5 Members) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 5px;">
      <!-- Member 1: Avishka -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.3pt; color: var(--black);">AVISHKA MEDDEGODA</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Technical Lead &amp; Senior Full-Stack Architect</div>
          </div>
          <span class="badge badge-dark">6+ YRS EXP</span>
        </div>
        <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin: 0;">
          Senior Software Engineer at Arimac Digital and formerly Web Choice (VIC, Australia). <strong>Lead Backend Architect for Moolee - Your Favorite Marketplace (<a href="https://www.moolee.mv/" class="live-link" target="_blank">moolee.mv &nearr;</a>)</strong>, architecting multi-tenant e-commerce microservices, vendor portals, and order orchestration. Architect for DIMO SAP ERP Gate Pass Platform (<a href="https://www.dimolanka.com/" class="live-link" target="_blank">dimolanka.com &nearr;</a>) and Ooredoo Telecom Group systems.
        </p>
      </div>

      <!-- Member 2: Janith -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.3pt; color: var(--black);">JANITH NADIRANGA</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Enterprise Systems &amp; Database Engineer</div>
          </div>
          <span class="badge badge-dark">DMS PROGRAMMER</span>
        </div>
        <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin: 0;">
          Programmer at DMS (Pvt) Ltd, Software Division (<a href="https://dmssw.com/" class="live-link" target="_blank">dmssw.com &nearr;</a>; formerly SiteSolve; Coventry University UK). Architect of field collection, mobile receipt generation, and RDS data migration workflows for SINGER Sri Lanka PLC (<a href="https://www.singersl.com/" class="live-link" target="_blank">singersl.com &nearr;</a> &middot; 430+ showrooms). Specialist in inventory distribution networks, Java, Spring Boot, and MySQL/PostgreSQL.
        </p>
      </div>

      <!-- Member 3: Viranga -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.3pt; color: var(--black);">VIRANGA LAKSHAN</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Enterprise Integration &amp; CMS Architect</div>
          </div>
          <span class="badge badge-dark">FULL-STACK LEAD</span>
        </div>
        <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin: 0;">
          Full-Stack Software Engineer at Arimac Digital (Coventry University UK). Lead integration engineer for UK, Australian, and UAE platforms: <strong>Al Ain Museum V2</strong> (<a href="https://www.alainmuseum.ae/en" class="live-link" target="_blank">alainmuseum.ae &nearr;</a>) and <strong>Natural History Museum Abu Dhabi</strong> (<a href="https://www.nhmad.ae/" class="live-link" target="_blank">nhmad.ae &nearr;</a>). Live UAE Platform: <a href="https://www.du.ae/personal" class="live-link" target="_blank">du.ae/personal &nearr;</a>.
        </p>
      </div>

      <!-- Member 4: Chamara -->
      <div class="editorial-card-grey">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
          <div>
            <strong style="font-size: 8.3pt; color: var(--black);">CHAMARA LAHIRU</strong>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Senior Frontend &amp; Mobile UI/UX Architect</div>
          </div>
          <span class="badge badge-dark">UI/UX SPECIALIST</span>
        </div>
        <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin: 0;">
          Senior Software Engineer at Arimac Digital (Sabaragamuwa University). Engineered high-performance digital platforms for <strong>McGrath Real Estate</strong> (<a href="https://www.mcgrath.com.au/" class="live-link" target="_blank">mcgrath.com.au &nearr;</a>), <strong>DU Telecom Greenfield</strong> (<a href="https://www.du.ae/" class="live-link" target="_blank">du.ae &nearr;</a>), and Castle Renewables (<a href="https://castlerenewables.com.au" class="live-link" target="_blank">castlerenewables.com.au &nearr;</a>).
        </p>
      </div>
    </div>

    <!-- Member 5: Lithumitha (Full Width) -->
    <div class="editorial-card" style="margin-bottom: 5px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 2px;">
        <div>
          <strong style="font-size: 8.3pt; color: var(--black);">LITHUMITHA RAVIKUMAR</strong>
          <span style="font-size: 7.2pt; font-weight: 700; color: var(--mid-grey); margin-left: 6px;">Associate Project Manager &amp; Product Delivery Lead</span>
        </div>
        <span class="badge badge-dark">FIRST CLASS HONOURS &middot; AGILE LEAD</span>
      </div>
      <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin: 0;">
        Associate Project Manager at Arimac Digital (First Class Honours, Business Information Systems). Oversees project delivery, client sprint communication, milestone acceptance criteria, and user training. Ensures Reynolds receives weekly video progress updates, structured milestone releases, and comprehensive handover documentation.
      </p>
    </div>

    <!-- Pod Delivery Value Box -->
    <div class="editorial-card-black">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #9CA3AF; margin-bottom: 2px;">
        WHY THIS GIVES REYNOLDS PRECISION ENGINEERING COMPLETE CERTAINTY
      </div>
      <p style="font-size: 7.5pt; line-height: 1.35; margin: 0;">
        Instead of relying on a lone freelancer who might disappear or struggle with complex pricing logic, Reynolds Precision Engineering gets an established engineering squad for the exact price of an individual developer (&pound;2,000 GBP). You gain senior architecture oversight, dedicated QA testing, and seamless ongoing support.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 03 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 04: QUESTIONS 1, 2 & 3 ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 03 &middot; QUESTIONS 1, 2 &amp; 3 &middot; PLATFORM SELECTION</div>
    </div>

    <span class="section-tag">Client Application Requirements &middot; Technical Architecture</span>
    <h2 class="page-title">Answers to Client Review Questions 1, 2 &amp; 3</h2>
    <p class="lead-text">
      Direct responses regarding our hands-on B2B customer-specific pricing builds, completed projects with live links, and our architectural platform recommendation.
    </p>

    <!-- QUESTION 1 -->
    <div class="qa-card" style="margin-bottom: 5px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 1</span>
        <span>Have you built a B2B ordering website with customer-specific pricing?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          <strong>Yes, absolutely.</strong> We have architected and deployed multiple enterprise B2B purchasing portals featuring complex, multi-tiered contracted pricing matrices:
        </p>
        <ul style="margin-left: 15px; font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.33;">
          <li><strong>Role &amp; Company-Based Pricing:</strong> Separate companies and branch locations are assigned custom price groups (e.g., Client A pays &pound;42.00 for CNC Bushing Part #RP-104, while Client B pays &pound;38.50 based on annual contract volume).</li>
          <li><strong>Confidentiality by Design:</strong> Unauthenticated public visitors see either list pricing, catalogue-only mode, or "Login for Agreed Pricing" prompts. Logged-in buyers only ever see their own negotiated rates.</li>
          <li><strong>Bulk Discount &amp; Quantity Breaks:</strong> Tiered pricing rules (e.g., 1&ndash;5 units, 6&ndash;20 units, 21+ units) applied automatically at the shopping basket stage.</li>
        </ul>
      </div>
    </div>

    <!-- QUESTION 2 WITH LIVE CLIENT LINKS (FEATURING MOOLEE.MV & SINGER) -->
    <div class="qa-card" style="margin-bottom: 5px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 2</span>
        <span>Can you show examples of similar completed projects?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          Yes, our team has delivered enterprise e-commerce marketplaces, B2B purchasing portals, and industrial logistics platforms:
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin: 2px 0;">
          <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
              <strong style="font-size: 7.2pt; color: var(--black);">Moolee - Favorite Marketplace</strong>
              <a href="https://www.moolee.mv/" class="live-link" target="_blank">moolee.mv &nearr;</a>
            </div>
            <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
              Nationwide multi-tenant e-commerce marketplace platform led by <strong>Avishka Meddegoda</strong> at Arimac. High-concurrency checkout, customer-specific pricing &amp; promotion rules, vendor portals, and order orchestration.
            </p>
          </div>
          <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
              <strong style="font-size: 7.2pt; color: var(--black);">SINGER Sri Lanka PLC</strong>
              <a href="https://www.singersl.com/" class="live-link" target="_blank">singersl.com &nearr;</a>
            </div>
            <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
              Sri Lanka's #1 retail e-commerce &amp; inventory engine (430+ showrooms, millions of accounts). Batch tracking, AWS RDS migration, and distribution workflow by Janith Nadiranga at DMS (<a href="https://dmssw.com/" style="color: #166534; font-weight: 700; text-decoration: none;">dmssw.com</a>).
            </p>
          </div>
          <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
              <strong style="font-size: 7.2pt; color: var(--black);">DIMO Lanka PLC (Industrial)</strong>
              <a href="https://www.dimolanka.com/" class="live-link" target="_blank">dimolanka.com &nearr;</a>
            </div>
            <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
              SAP ERP (MM/PM) integrated industrial machinery replacement parts logistics platform. Multi-tier approval workflows, component serial tracking, and workshop gate-pass management.
            </p>
          </div>
          <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
              <strong style="font-size: 7.2pt; color: var(--black);">Castle Renewables (Australia)</strong>
              <a href="https://castlerenewables.com.au" class="live-link" target="_blank">castlerenewables.com.au &nearr;</a>
            </div>
            <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
              Custom WordPress B2B corporate build with Custom Post Types (CPTs) for infrastructure assets, dynamic project filtering, and technical taxonomy. Plus <a href="https://www.du.ae/personal" style="color: #166534; font-weight: 700;">du.ae/personal</a> &amp; <a href="https://www.mcgrath.com.au/" style="color: #166534; font-weight: 700;">mcgrath.com.au</a>.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- QUESTION 3 -->
    <div class="qa-card">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 3</span>
        <span>Which platform would you recommend and why?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 2px;">
          We strongly recommend <strong>WordPress + WooCommerce with an Enterprise B2B Architecture (B2BKing / Wholesale Suite Engine)</strong>.
        </p>
        <table class="editorial-table" style="margin: 2px 0;">
          <thead>
            <tr>
              <th style="width: 25%;">Evaluation Criteria</th>
              <th style="width: 45%;">WordPress / WooCommerce B2B (Recommended)</th>
              <th style="width: 30%;">Custom Scratch Build</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>B2B PO &amp; Pricing Suitability</strong></td>
              <td>Native support for customer-specific price lists, company PO checkout, tax exemption, and role-based catalogue visibility out-of-the-box.</td>
              <td>Requires hundreds of hours to custom-code database schema, authentication, and security.</td>
            </tr>
            <tr>
              <td><strong>Ownership &amp; Ongoing Costs</strong></td>
              <td><strong>100% Full Ownership.</strong> Zero monthly SaaS transaction fees (unlike Shopify Plus at &pound;2,000+/mo). Runs on standard UK cloud hosting (&pound;15&ndash;&pound;25/mo).</td>
              <td>Requires costly ongoing developer maintenance for simple content and product edits.</td>
            </tr>
            <tr>
              <td><strong>Ease of Administration</strong></td>
              <td>Extremely intuitive for Reynolds' staff: upload engineering PDFs, update part numbers, change lead times, and adjust prices with zero coding knowledge.</td>
              <td>Requires custom admin panel development, often brittle and complex to maintain.</td>
            </tr>
            <tr>
              <td><strong>Delivery Timeline &amp; Budget</strong></td>
              <td><strong>Fits perfectly within your &pound;2,000 GBP budget</strong> and launches smoothly before Christmas 2026.</td>
              <td>Custom build would exceed &pound;6,000+ GBP and take 3&ndash;4 months.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 04 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 05: QUESTIONS 4, 5 & 6 ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 04 &middot; QUESTIONS 4, 5 &amp; 6 &middot; COMMERCIALS &amp; TIMELINE</div>
    </div>

    <span class="section-tag">Commercial Agreement &middot; Timeline &middot; 100% Full Ownership</span>
    <h2 class="page-title">Answers to Client Review Questions 4, 5 &amp; 6</h2>
    <p class="lead-text">
      Clear, transparent commercial commitments confirming our fixed-price quotation, realistic delivery schedule, and complete administrative handover with zero vendor lock-in.
    </p>

    <!-- QUESTION 4 -->
    <div class="qa-card" style="margin-bottom: 6px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 4</span>
        <span>Can you complete this project within approximately &pound;2,000 GBP?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          <strong>Yes, absolutely.</strong> We confirm our fixed-price quotation of exactly <strong>&pound;2,000 GBP (equivalent to $2,600 USD on Upwork)</strong>.
        </p>
        <ul style="margin-left: 15px; font-size: 7.3pt; color: var(--dark-charcoal); line-height: 1.35;">
          <li>This is a comprehensive, guaranteed fixed price with <strong>no hidden fees, no unexpected overruns, and no extra charges</strong>.</li>
          <li>Includes all 7 core functional requirements: customer portals, contracted pricing, downloadable PDF drawings, purchase order checkout, stock/lead time management, admin dashboard, and responsive engineering design.</li>
          <li>Structured into 4 milestone escrow payments via Upwork, released only upon your full review and approval of each phase.</li>
        </ul>
      </div>
    </div>

    <!-- QUESTION 5 -->
    <div class="qa-card" style="margin-bottom: 6px;">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 5</span>
        <span>How long would development take?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          Total development and deployment will take <strong>4 to 5 weeks</strong>, with an agile sprint breakdown that allows us to begin immediately before Christmas 2026:
        </p>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin: 3px 0;">
          <div class="stat-box" style="padding: 4px;">
            <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Week 1</div>
            <div style="font-size: 6.2pt; color: var(--mid-grey);">Blueprint &amp; Branding</div>
          </div>
          <div class="stat-box" style="padding: 4px;">
            <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Weeks 2&ndash;3</div>
            <div style="font-size: 6.2pt; color: var(--mid-grey);">B2B Logic &amp; Catalogue</div>
          </div>
          <div class="stat-box" style="padding: 4px;">
            <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Week 4</div>
            <div style="font-size: 6.2pt; color: var(--mid-grey);">PO Checkout &amp; Testing</div>
          </div>
          <div class="stat-box" style="padding: 4px;">
            <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Week 5</div>
            <div style="font-size: 6.2pt; color: var(--mid-grey);">Training &amp; Launch</div>
          </div>
        </div>
        <div class="highlight-box">
          <strong>Pre-Christmas 2026 Kickoff:</strong> We can execute contracts, setup the staging server, and deliver the initial design prototype and brand styling before the Christmas holiday break, hitting the ground running in early January for seamless launch.
        </div>
      </div>
    </div>

    <!-- QUESTION 6 -->
    <div class="qa-card">
      <div class="qa-question">
        <span class="badge badge-dark">QUESTION 6</span>
        <span>Will we own the completed website and have full administrative control?</span>
      </div>
      <div class="qa-answer">
        <p style="margin-bottom: 3px;">
          <strong>Yes, 100% full ownership and control belongs exclusively to Reynolds Precision Engineering Ltd.</strong>
        </p>
        <ul style="margin-left: 15px; font-size: 7.3pt; color: var(--dark-charcoal); line-height: 1.35;">
          <li><strong>Complete Asset Handover:</strong> You receive master administrator credentials, database access, FTP/hosting logins, and all original theme and design assets.</li>
          <li><strong>Zero Developer Lock-In:</strong> The site is built on open, standard WordPress/WooCommerce architecture. Any developer can maintain or expand it in the future without proprietary constraints.</li>
          <li><strong>Staff Training &amp; Runbook:</strong> We provide recorded video walkthrough tutorials showing your team how to add new CNC products, update customer pricing, and process orders.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 05 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 06: FLAGSHIP E-COMMERCE & SINGER PLATFORMS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 05 &middot; PROVEN E-COMMERCE &amp; INVENTORY PLATFORMS</div>
    </div>

    <span class="section-tag">High-Concurrency Commercial Systems &middot; Multi-Tenant Architecture</span>
    <h2 class="page-title">Proven E-Commerce &amp; Inventory Track Record</h2>
    <p class="lead-text">
      Our engineers have built mission-critical digital purchasing, multi-vendor marketplace, and inventory tracking platforms supporting nationwide supply chains and high-volume commerce.
    </p>

    <!-- Project 01: Moolee - Your Favorite Marketplace (Avishka Meddegoda) -->
    <div class="editorial-card" style="margin-bottom: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
        <div>
          <span class="badge badge-dark">FLAGSHIP SHOWCASE 01</span>
          <span style="font-size: 8.6pt; font-weight: 800; color: var(--black); margin-left: 6px;">
            Moolee &middot; Nationwide E-Commerce Marketplace Platform
          </span>
        </div>
        <div>
          <a href="https://www.moolee.mv/" class="live-link" target="_blank">LIVE MARKETPLACE: moolee.mv &nearr;</a>
        </div>
      </div>
      <div style="display: grid; grid-template-columns: 130px 1fr; gap: 10px; align-items: center;">
        <img src="{MOOLEE_IMG}" style="width: 130px; height: 74px; object-fit: cover; border-radius: 3px; border: 1px solid var(--border-grey);" alt="Moolee Live Marketplace">
        <div>
          <div style="font-size: 6.9pt; font-weight: 700; color: var(--mid-grey); margin-bottom: 1px;">
            Lead Backend Architect: Avishka Meddegoda &middot; Arimac Digital / Ooredoo
          </div>
          <p style="font-size: 7.2pt; line-height: 1.33; color: var(--dark-charcoal); margin-bottom: 2px;">
            Architected backend microservices powering <strong>Moolee (moolee.mv)</strong>, the nation's premier multi-vendor e-commerce marketplace platform. Engineered dynamic shopping carts, customer-specific pricing &amp; promotional matrices, automated multi-vendor order routing, and real-time carrier tracking.
          </p>
          <div style="font-size: 7pt; color: var(--mid-grey);">
            <strong>Direct Overlap with Reynolds:</strong> Role-based buyer logins, contracted pricing tiers, category search filtering, and robust admin order management dashboards.
          </div>
        </div>
      </div>
    </div>

    <!-- Project 02: SINGER Sri Lanka PLC (Janith Nadiranga) -->
    <div class="editorial-card" style="margin-bottom: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
        <div>
          <span class="badge badge-dark">FLAGSHIP SHOWCASE 02</span>
          <span style="font-size: 8.6pt; font-weight: 800; color: var(--black); margin-left: 6px;">
            SINGER Sri Lanka PLC &middot; Retail E-Commerce &amp; Inventory Engine
          </span>
        </div>
        <div>
          <a href="https://www.singersl.com/" class="live-link" target="_blank">LIVE: singersl.com &nearr;</a>
          <a href="https://dmssw.com/" class="live-link" target="_blank" style="margin-left: 4px;">DMS: dmssw.com &nearr;</a>
        </div>
      </div>
      <p style="font-size: 7.2pt; line-height: 1.34; color: var(--dark-charcoal); margin-bottom: 2px;">
        Engineered nationwide inventory and financial transaction workflows for Sri Lanka's largest consumer durable retailer (430+ branches, 1,200+ dealer networks, millions of active customer accounts):
      </p>
      <ul style="margin-left: 14px; font-size: 7pt; color: var(--dark-charcoal); line-height: 1.31;">
        <li>Designed batch-wise transaction tracking, mobile receipt generation, and complete data migration to Amazon RDS.</li>
        <li>Built inventory and distribution tracking platforms with Next.js, AWS Lambda, and RabbitMQ message queues supporting end-to-end stock flows across multi-tier networks.</li>
        <li>Delivered 99.99% system uptime, audit logging, and automated reconciliation reports.</li>
      </ul>
    </div>

    <!-- Live Client Quick Access Bar -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 5px; margin-bottom: 5px;">
      <div class="editorial-card-grey" style="padding: 4px 6px; margin-bottom: 0;">
        <div style="font-size: 6.8pt; font-weight: 800; color: var(--black);">Moolee Marketplace</div>
        <a href="https://www.moolee.mv/" class="live-link" target="_blank" style="font-size: 6.2pt;">moolee.mv &nearr;</a>
        <div style="font-size: 6.2pt; color: var(--mid-grey); margin-top: 1px;">National E-Commerce Marketplace</div>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 6px; margin-bottom: 0;">
        <div style="font-size: 6.8pt; font-weight: 800; color: var(--black);">SINGER Sri Lanka PLC</div>
        <a href="https://www.singersl.com/" class="live-link" target="_blank" style="font-size: 6.2pt;">singersl.com &nearr;</a>
        <div style="font-size: 6.2pt; color: var(--mid-grey); margin-top: 1px;">430+ Showrooms Retail &amp; Inventory</div>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 6px; margin-bottom: 0;">
        <div style="font-size: 6.8pt; font-weight: 800; color: var(--black);">Castle Renewables (AU)</div>
        <a href="https://castlerenewables.com.au" class="live-link" target="_blank" style="font-size: 6.2pt;">castlerenewables.com.au &nearr;</a>
        <div style="font-size: 6.2pt; color: var(--mid-grey); margin-top: 1px;">Custom WordPress B2B &amp; Filtering</div>
      </div>
    </div>

    <!-- Banner strip -->
    <div style="border: 1px solid var(--border-grey); border-radius: 3px; overflow: hidden;">
      <img src="{BANNER_FULL}" style="width: 100%; height: 36px; object-fit: cover; display: block;" alt="Full-Stack Engineering Practice">
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 06 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 07: DIMO SAP ERP & LIVE INTERNATIONAL CLIENTS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 06 &middot; INDUSTRIAL LOGISTICS &amp; LIVE CLIENTS</div>
    </div>

    <span class="section-tag">Industrial Machinery Parts &middot; International Live Clients</span>
    <h2 class="page-title">DIMO Industrial Logistics &amp; Live Global Clients</h2>
    <p class="lead-text">
      From tracking heavy machinery replacement parts integrated with SAP ERP to delivering live digital platforms for international governments, public enterprises, and ASX-listed firms.
    </p>

    <!-- DIMO SAP ERP -->
    <div class="editorial-card" style="margin-bottom: 6px;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3px;">
        <div>
          <span class="badge badge-dark">INDUSTRIAL LOGISTICS</span>
          <span style="font-size: 8.6pt; font-weight: 800; color: var(--black); margin-left: 6px;">
            DIMO Lanka PLC &middot; SAP ERP Integrated Industrial Gate Pass Platform
          </span>
        </div>
        <div>
          <a href="https://www.dimolanka.com/" class="live-link" target="_blank">LIVE: dimolanka.com &nearr;</a>
        </div>
      </div>
      <div style="display: grid; grid-template-columns: 125px 1fr; gap: 8px; align-items: center;">
        <img src="{DIMO_IMG}" style="width: 125px; height: 68px; object-fit: cover; border-radius: 3px; border: 1px solid var(--border-grey);" alt="DIMO SAP Gate Pass Platform">
        <div>
          <p style="font-size: 7.2pt; line-height: 1.34; color: var(--dark-charcoal); margin-bottom: 2px;">
            Engineered an enterprise platform directly connected with <strong>SAP ERP (MM/PM Modules)</strong> to track the arrival, workshop servicing, replacement components, and dispatch of heavy industrial machinery and equipment.
          </p>
          <div style="font-size: 7pt; color: var(--mid-grey);">
            <strong>Engineering Parallel:</strong> Demonstrates our intimate understanding of industrial component logistics, part number identification, and multi-tier approval workflows.
          </div>
        </div>
      </div>
    </div>

    <!-- Live Production Platforms Grid (8 Live Clients) -->
    <div class="block-title" style="margin-bottom: 3px;">Live Production Platforms Delivered by Our Squad</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 5px;">
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Moolee Marketplace</strong>
          <a href="https://www.moolee.mv/" class="live-link" target="_blank">moolee.mv &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Nationwide multi-vendor e-commerce marketplace platform. Dynamic shopping cart, pricing matrices, and automated order fulfillment pipelines.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Castle Renewables (Australia)</strong>
          <a href="https://castlerenewables.com.au" class="live-link" target="_blank">castlerenewables.com.au &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Custom WordPress block architecture, custom post types (CPTs) for infrastructure assets, project filtering, and corporate case studies.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">LB Finance PLC &amp; Sustainability</strong>
          <a href="https://www.lbfinance.com/" class="live-link" target="_blank">lbfinance.com &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Enterprise corporate portal and sustainability publication platform (<a href="https://sustainability.lbfinance.com/" style="color: #166534; font-weight: 700;">sustainability.lbfinance.com</a>) with structured financial governance.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">McGrath Real Estate (Australia)</strong>
          <a href="https://www.mcgrath.com.au/" class="live-link" target="_blank">mcgrath.com.au &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          ASX-listed premier Australian real estate platform. Next.js, Node.js, and GraphQL high-concurrency property listings search and customer portal.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Holsten Arabia (Carlsberg Group)</strong>
          <a href="https://holstenarabia.me/en/" class="live-link" target="_blank">holstenarabia.me &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Multilingual digital catalog and brand platform for global beverage brand. Umbraco Headless CMS with Next.js frontend and C# REST APIs.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Al Ain Museum V2 (UAE Government)</strong>
          <a href="https://www.alainmuseum.ae/en" class="live-link" target="_blank">alainmuseum.ae &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Department of Culture and Tourism (DCT Abu Dhabi). Rebuilt with Next.js, React, and Sitecore Headless CMS with high-security compliance.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">Natural History Museum Abu Dhabi</strong>
          <a href="https://www.nhmad.ae/" class="live-link" target="_blank">nhmad.ae &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Abu Dhabi Government experience platform built using Sitecore Helix architecture and C# .NET for high-security public sector delivery.
        </p>
      </div>
      <div class="editorial-card-grey" style="padding: 4px 7px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1px;">
          <strong style="font-size: 7.4pt; color: var(--black);">DU Telecom (UAE Flagship)</strong>
          <a href="https://www.du.ae/personal" class="live-link" target="_blank">du.ae/personal &nearr;</a>
        </div>
        <p style="font-size: 6.8pt; line-height: 1.28; color: var(--dark-charcoal); margin: 0;">
          Emirates Integrated Telecommunications Company. Mobile plans, 5G home internet, eSIM ordering &amp; customer selfcare micro-frontends by our team.
        </p>
      </div>
    </div>

    <!-- Live Engineering Flagship Project Footer Strip -->
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 4px 8px; background: #0F1115; border-radius: 3px; color: #FFFFFF; font-size: 6.8pt;">
      <span><strong>Premier Enterprise Flagship:</strong> DU Telecom Greenfield Transformation (UAE)</span>
      <a href="https://www.du.ae/personal" target="_blank" style="color: #4ADE80; font-family: 'JetBrains Mono', monospace; font-size: 6.6pt; font-weight: 700; text-decoration: none;">https://www.du.ae/personal &nearr;</a>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 07 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 08: DEEP TECHNICAL ARCHITECTURE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 07 &middot; DEEP TECHNICAL ARCHITECTURE</div>
    </div>

    <span class="section-tag">System Design &middot; Parts Catalogue, PO Checkout &amp; PDF Drawings</span>
    <h2 class="page-title">Technical Architecture &amp; B2B Ordering Workflows</h2>
    <p class="lead-text">
      How the Reynolds Precision Engineering B2B ordering portal functions behind the scenes to deliver a fast, frictionless ordering experience for plant maintenance engineers.
    </p>

    <!-- Architecture Breakdown Cards -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
      <!-- Card 1: Multi-Location Accounts & Pricing -->
      <div class="editorial-card-grey">
        <div class="block-title" style="font-size: 8.2pt;">1. Multi-Company &amp; Multi-Factory Accounts</div>
        <p style="font-size: 7.2pt; line-height: 1.34; color: var(--dark-charcoal); margin-bottom: 2px;">
          Corporate clients (e.g. Kerry Group, Moy Park, Dale Farm) can have multiple buyer accounts under one parent entity, with separate delivery addresses for different factory sites across the UK and Ireland.
        </p>
        <div style="font-size: 6.8pt; color: var(--mid-grey);">
          &bull; Contracted pricing assigned to parent account auto-inherits to all sub-locations.<br>
          &bull; Secure password management and optional two-factor authentication (2FA).
        </div>
      </div>

      <!-- Card 2: PDF Technical Drawings -->
      <div class="editorial-card-grey">
        <div class="block-title" style="font-size: 8.2pt;">2. Engineering Catalogue &amp; PDF Drawings</div>
        <p style="font-size: 7.2pt; line-height: 1.34; color: var(--dark-charcoal); margin-bottom: 2px;">
          Each precision component product page features part numbers, material specifications, tolerances, and an instant <strong>"Download PDF Drawing" button</strong>.
        </p>
        <div style="font-size: 6.8pt; color: var(--mid-grey);">
          &bull; PDF engineering drawings protected behind authorized customer login.<br>
          &bull; Live fuzzy search by part number, machine model, or component keyword.
        </div>
      </div>
    </div>

    <!-- Ordering & Lead Time Workflow -->
    <div class="block-title">3. Frictionless B2B Purchase Order (PO) Checkout Workflow</div>
    <div class="editorial-card-black" style="margin-bottom: 6px;">
      <div class="code-box" style="background: #1E2229; border-left: 3px solid #FFFFFF; margin: 2px 0;">
[Step 1: Selection] Customer selects Part #RP-204 &rarr; Views contracted rate (&pound;45.00) &amp; Available Stock (6 in stock)
      &darr;
[Step 2: Made-to-Order Logic] If quantity exceeds 6, system prompts: "6 available immediately; 4 Made-to-Order (Lead time: 5-7 working days)"
      &darr;
[Step 3: PO Checkout] Buyer adds to basket &rarr; Proceeds to checkout &rarr; Enters Company PO Number: [ PO-2026-8941 ]
      &darr; (No credit card or online payment required &middot; B2B Credit Account Billing)
[Step 4: Automated Dispatch] System triggers branded PDF Order Confirmation email to Customer &amp; Reynolds Workshop Queue
      &darr;
[Step 5: Repeat Ordering] Order stored in Customer Portal &rarr; 1-click "Re-Order This Part" button for regular replacements
      </div>
    </div>

    <!-- Stock & Lead Time Logic Table -->
    <div class="block-title">4. Stock Status &amp; Manufacturing Lead Time Engine</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Component State</th>
          <th style="width: 45%;">Frontend Customer Display</th>
          <th style="width: 30%;">Backend Workshop Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>In Stock Off-the-Shelf</strong></td>
          <td><span class="badge" style="background: #DCFCE7; color: #166534;">IN STOCK</span> Dispatch within 24 Hours.</td>
          <td>Generates pick-and-pack dispatch slip for off-the-shelf inventory.</td>
        </tr>
        <tr>
          <td><strong>Manufactured to Order</strong></td>
          <td><span class="badge" style="background: #FEF9C3; color: #854D0E;">MADE TO ORDER</span> CNC Lead Time: 5&ndash;7 Working Days.</td>
          <td>Automatically creates a CNC work order ticket in the Reynolds admin queue.</td>
        </tr>
        <tr>
          <td><strong>Split Availability</strong></td>
          <td>Partial stock dispatched immediately; remaining balance scheduled on CNC machine run.</td>
          <td>Generates split delivery notes with transparent tracking for the customer.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 08 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 09: ADMIN DASHBOARD & ONGOING COSTS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 08 &middot; ADMIN DASHBOARD &amp; ONGOING COSTS</div>
    </div>

    <span class="section-tag">Back-Office Operations &middot; Transparent Ongoing Cost Breakdown</span>
    <h2 class="page-title">Administration Dashboard &amp; Operational Costs</h2>
    <p class="lead-text">
      Engineered for effortless day-to-day management by Reynolds Precision Engineering staff, backed by complete financial transparency regarding ongoing hosting and zero software lock-in.
    </p>

    <!-- Admin Dashboard Features -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
      <div class="editorial-card-grey">
        <strong style="font-size: 7.8pt; color: var(--black);">Intuitive Product &amp; PDF Management</strong>
        <p style="font-size: 7.1pt; line-height: 1.34; color: var(--dark-charcoal); margin: 2px 0 0 0;">
          Add hundreds of replacement engineering components easily. Upload CAD drawings (PDFs), part photos, material specifications, and set default lead times in seconds.
        </p>
      </div>
      <div class="editorial-card-grey">
        <strong style="font-size: 7.8pt; color: var(--black);">Customer Pricing Management</strong>
        <p style="font-size: 7.1pt; line-height: 1.34; color: var(--dark-charcoal); margin: 2px 0 0 0;">
          Assign individual customers or factory accounts to specific price tiers or upload bespoke CSV price contracts directly through the administration portal.
        </p>
      </div>
      <div class="editorial-card-grey">
        <strong style="font-size: 7.8pt; color: var(--black);">Order Tracking &amp; Status Updates</strong>
        <p style="font-size: 7.1pt; line-height: 1.34; color: var(--dark-charcoal); margin: 2px 0 0 0;">
          Update order statuses with 1 click: <em>Order Received &rarr; CNC Machining in Progress &rarr; Quality Inspected &rarr; Dispatched</em>, triggering automated emails to the client.
        </p>
      </div>
      <div class="editorial-card-grey">
        <strong style="font-size: 7.8pt; color: var(--black);">Stock &amp; Lead Time Overrides</strong>
        <p style="font-size: 7.1pt; line-height: 1.34; color: var(--dark-charcoal); margin: 2px 0 0 0;">
          Instantly adjust stock levels or alter manufacturing lead times across product categories during peak machine loading or holiday periods.
        </p>
      </div>
    </div>

    <!-- Ongoing Costs Breakdown Table -->
    <div class="block-title">Transparent Breakdown of Ongoing Hosting, Licence &amp; Maintenance Costs</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Expense Item</th>
          <th style="width: 35%;">Estimated Cost</th>
          <th style="width: 40%;">Explanation &amp; Cost Control</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Website Hosting (UK Server)</strong></td>
          <td><strong>&pound;15 &ndash; &pound;25 GBP / month</strong></td>
          <td>Fast, secure UK-based cloud hosting (e.g., SiteGround, Cloudways, or Hostinger UK) with automated daily backups, free SSL certificates, and UK data residency.</td>
        </tr>
        <tr>
          <td><strong>Domain Name</strong></td>
          <td><strong>&pound;10 &ndash; &pound;15 GBP / year</strong></td>
          <td>Standard annual renewal for Reynolds Precision Engineering domain (e.g. <code>.co.uk</code> or <code>.com</code>). Paid directly to registrar.</td>
        </tr>
        <tr>
          <td><strong>Software Licences</strong></td>
          <td><strong>&pound;0 GBP (Zero recurring SaaS fees)</strong></td>
          <td>WordPress and core WooCommerce are 100% open-source and free forever. No monthly revenue cuts or per-user seat fees.</td>
        </tr>
        <tr>
          <td><strong>Ongoing Maintenance (Optional)</strong></td>
          <td><strong>As-needed / Pay-as-you-go</strong></td>
          <td>Our team remains on standby for future feature enhancements, security patches, or new ERP integrations at competitive hourly/milestone rates.</td>
        </tr>
      </tbody>
    </table>

    <div class="editorial-card-black" style="margin-top: 3px;">
      <p style="font-size: 7.5pt; line-height: 1.35; margin: 0;">
        <strong>Total Ongoing Annual Running Cost:</strong> Approximately <strong>&pound;190 &ndash; &pound;300 GBP per year</strong> total for hosting and domain. Compare this to proprietary B2B SaaS platforms charging &pound;2,000&ndash;&pound;5,000+ per year in recurring subscriptions.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 09 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 10: MILESTONE ROADMAP & SIGN-OFF ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL</div>
      <div class="header-right">SECTION 09 &middot; ROADMAP &amp; FORMAL HANDOVER</div>
    </div>

    <span class="section-tag">Fixed-Price Milestones &middot; Christmas 2026 Kickoff &middot; Formal Sign-Off</span>
    <h2 class="page-title">Fixed-Price Milestones &amp; Handover Roadmap</h2>
    <p class="lead-text">
      Structured milestone delivery plan guaranteeing full quality assurance, comprehensive video training, complete source code handover, and 60 days of post-launch technical warranty.
    </p>

    <!-- Phased Milestones Table -->
    <table class="editorial-table" style="margin-bottom: 6px;">
      <thead>
        <tr>
          <th style="width: 15%;">Milestone</th>
          <th style="width: 45%;">Deliverables &amp; Technical Scope</th>
          <th style="width: 25%;">Target Timing</th>
          <th style="width: 15%;">Payment Value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Milestone 1<br>Kickoff &amp; Setup</strong></td>
          <td>&bull; Architecture blueprint &amp; database schema setup.<br>&bull; Staging server configuration &amp; security hardening.<br>&bull; Reynolds Precision Engineering brand styling &amp; UI prototype.</td>
          <td>Week 1<br>(Pre-Christmas 2026)</td>
          <td><strong>&pound;500 GBP<br>($650 USD)</strong></td>
        </tr>
        <tr>
          <td><strong>Milestone 2<br>Catalogue &amp; Pricing</strong></td>
          <td>&bull; B2B Customer login &amp; multi-factory location accounts.<br>&bull; Engineering parts catalogue with PDF drawing downloads.<br>&bull; Confidential customer-specific pricing engine.</td>
          <td>Weeks 2&ndash;3</td>
          <td><strong>&pound;600 GBP<br>($780 USD)</strong></td>
        </tr>
        <tr>
          <td><strong>Milestone 3<br>PO Checkout &amp; Stock</strong></td>
          <td>&bull; Company PO checkout flow (no credit card required).<br>&bull; Available stock &amp; Made-to-Order manufacturing lead times.<br>&bull; Automated email confirmation templates &amp; repeat ordering.</td>
          <td>Week 4</td>
          <td><strong>&pound;500 GBP<br>($650 USD)</strong></td>
        </tr>
        <tr>
          <td><strong>Milestone 4<br>Testing &amp; Handover</strong></td>
          <td>&bull; End-to-end UAT cross-browser and mobile testing.<br>&bull; Staff video training walkthrough &amp; written user manual.<br>&bull; Full admin credentials &amp; source code handover &amp; Go-Live.</td>
          <td>Week 5</td>
          <td><strong>&pound;400 GBP<br>($520 USD)</strong></td>
        </tr>
        <tr style="background: #F4F5F7; font-weight: 800;">
          <td colspan="3" style="text-align: right; padding-right: 10px;">TOTAL FIXED-PRICE QUOTATION:</td>
          <td><strong>&pound;2,000 GBP<br>($2,600 USD)</strong></td>
        </tr>
      </tbody>
    </table>

    <!-- Leadership Pod Credentials Grid -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 6px;">
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Tech Lead &amp; Architect</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          Lead Backend Architect: Moolee Marketplace (<a href="https://www.moolee.mv/" class="live-link" target="_blank">moolee.mv &nearr;</a>) &amp; DIMO SAP ERP (<a href="https://www.dimolanka.com/" class="live-link" target="_blank">dimolanka.com &nearr;</a>).
        </div>
      </div>
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Senior Systems Engineer</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Janith Nadiranga</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          DMS Software Division (<a href="https://dmssw.com/" class="live-link" target="_blank">dmssw.com &nearr;</a>). SINGER Sri Lanka PLC (<a href="https://www.singersl.com/" class="live-link" target="_blank">singersl.com &nearr;</a>).
        </div>
      </div>
      <div class="editorial-card-grey">
        <div style="font-size: 6pt; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; color: var(--mid-grey);">Integration &amp; Full-Stack</div>
        <div style="font-size: 8.5pt; font-weight: 800; color: var(--black);">Viranga Lakshan</div>
        <div style="font-size: 6.8pt; color: var(--dark-charcoal); margin-top: 1px;">
          Arimac Digital. Al Ain Museum (<a href="https://www.alainmuseum.ae/en" class="live-link" target="_blank">alainmuseum.ae &nearr;</a>) &amp; DU Telecom (<a href="https://www.du.ae/personal" class="live-link" target="_blank">du.ae/personal &nearr;</a>).
        </div>
      </div>
    </div>

    <!-- Formal Agreement Sign-Off Box -->
    <div class="editorial-card-black">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #374151; padding-bottom: 3px; margin-bottom: 3px;">
        <span style="font-size: 7.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: #FFFFFF;">
          FORMAL COMMERCIAL &amp; UPWORK COMPLIANCE AGREEMENT
        </span>
        <span class="badge" style="background: #FFFFFF; color: var(--black);">UPWORK VERIFIED</span>
      </div>
      <p style="font-size: 7.3pt; line-height: 1.34; color: #D1D5DB; margin-bottom: 3px;">
        &ldquo;We confirm our fixed-price quotation of <strong>&pound;2,000 GBP ($2,600 USD)</strong>, our readiness to begin before Christmas 2026, and our commitment to delivering 100% full administrative control, source code handover, and ongoing support for Reynolds Precision Engineering Ltd.&rdquo;
      </p>
      <div style="display: flex; justify-content: space-between; font-size: 6.8pt; color: #9CA3AF; padding-top: 1px;">
        <span>Prepared by: Avishka Meddegoda (Tech Lead) &amp; Engineering Squad</span>
        <span>Axiom Global Enterprise Practice &middot; Northern Ireland Delivery</span>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; REYNOLDS PRECISION ENGINEERING PROPOSAL &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 10 of 10</div>
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
    assert total_pages == 10, f"Expected 10 pages, got {total_pages}"
    print("PAGE COUNT VERIFICATION PASSED: Strictly 10 pages.")

if __name__ == "__main__":
    generate_pdf()
