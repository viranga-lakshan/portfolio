import os
import asyncio
from playwright.async_api import async_playwright
import pypdf

BASE_DIR = r"c:\Users\Viranga\Downloads\upwrok new\GroundWell_Sound_Wellness_Wix_Acuity_Proposal"
IMG_DIR = os.path.join(BASE_DIR, "images")
HTML_PATH = os.path.join(BASE_DIR, "proposal_template.html")
PDF_PATH = os.path.join(BASE_DIR, "GroundWell_Sound_Wellness_Wix_Acuity_Proposal.pdf")

def to_uri(fname):
    return os.path.join(IMG_DIR, fname).replace("\\", "/")

HERO_IMG = to_uri("sound_bowls_hero.jpg")
SANCTUARY_IMG = to_uri("wellness_sanctuary.jpg")
REIKI_IMG = to_uri("reiki_meditation.jpg")
TUNING_IMG = to_uri("tuning_forks_sound.jpg")
ACUITY_IMG = to_uri("acuity_booking_flow.jpg")
COMMUNITY_IMG = to_uri("community_sound_bath.jpg")
LOGO_IMG = to_uri("axiom_logo.png")
TEAM_IMG = to_uri("team_office.jpg")

CSS_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {
  size: A4 portrait;
  margin: 0;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}

:root {
  --black: #0F1115;
  --dark-charcoal: #22252A;
  --mid-grey: #5A606A;
  --light-grey: #F4F5F7;
  --border-grey: #E2E5E9;
  --border-dark: #1E2229;
  --white: #FFFFFF;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--black);
  background: #E5E7EB;
  margin: 0;
  padding: 0;
  font-size: 7.6pt;
  line-height: 1.42;
  -webkit-font-smoothing: antialiased;
}

.page {
  width: 210mm;
  height: 297mm;
  max-height: 297mm;
  overflow: hidden;
  position: relative;
  background: var(--white);
  padding: 11mm 15mm 10mm 15mm;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 0 auto 10mm auto;
}

@media print {
  body {
    background: transparent;
  }
  .page {
    margin: 0;
    box-shadow: none;
    page-break-after: always;
  }
}

/* Running Header */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--black);
  padding-bottom: 5px;
  margin-bottom: 9px;
}

.header-left {
  font-size: 6.8pt;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--black);
}

.header-right {
  font-size: 6.8pt;
  font-weight: 600;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: var(--mid-grey);
}

/* Running Footer */
.page-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-grey);
  padding-top: 5px;
  margin-top: auto;
}

.footer-left {
  font-size: 6.2pt;
  font-weight: 600;
  color: var(--mid-grey);
  letter-spacing: 0.5px;
}

.footer-page-num {
  font-size: 6.5pt;
  font-weight: 700;
  color: var(--black);
  font-family: 'JetBrains Mono', monospace;
}

/* Typography Hierarchy */
.serif-heading {
  font-family: 'Playfair Display', Georgia, serif;
  font-weight: 700;
  letter-spacing: -0.3px;
}

.section-tag {
  display: inline-block;
  font-size: 6.2pt;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--black);
  margin-bottom: 2px;
}

.page-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 18pt;
  font-weight: 700;
  line-height: 1.12;
  color: var(--black);
  margin-bottom: 5px;
}

.lead-text {
  font-size: 8.2pt;
  line-height: 1.45;
  color: var(--dark-charcoal);
  margin-bottom: 8px;
  max-width: 98%;
}

.block-title {
  font-size: 8.8pt;
  font-weight: 800;
  letter-spacing: -0.2px;
  color: var(--black);
  margin-bottom: 3px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.body-text {
  font-size: 7.2pt;
  line-height: 1.4;
  color: var(--mid-grey);
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 7px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
}

/* Cards & Containers */
.card-bordered {
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 8px 10px;
  background: var(--white);
}

.card-dark {
  background: var(--black);
  color: var(--white);
  border-radius: 4px;
  padding: 10px 12px;
}

.card-dark .block-title {
  color: var(--white);
}

.card-dark .body-text {
  color: #D1D5DB;
}

/* Tables */
table.editorial-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 6.9pt;
  margin-bottom: 6px;
}

table.editorial-table th {
  background: var(--black);
  color: var(--white);
  text-align: left;
  padding: 5px 7px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 6.2pt;
}

table.editorial-table td {
  padding: 4.5px 7px;
  border-bottom: 1px solid var(--border-grey);
  color: var(--dark-charcoal);
  vertical-align: top;
}

table.editorial-table tr:nth-child(even) td {
  background: #FAFAFC;
}

/* Badges */
.badge {
  display: inline-block;
  font-size: 5.8pt;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-dark {
  background: var(--black);
  color: var(--white);
}

.badge-outline {
  border: 1px solid var(--black);
  color: var(--black);
  background: transparent;
}

.badge-stage {
  background: var(--light-grey);
  border: 1px solid var(--border-grey);
  color: var(--black);
}

/* Stat Box */
.stat-box {
  background: #FAFAFA;
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 7px 9px;
  text-align: center;
}

.stat-number {
  font-size: 16pt;
  font-weight: 800;
  color: var(--black);
  font-family: 'Playfair Display', Georgia, serif;
  line-height: 1;
}

.stat-label {
  font-size: 5.8pt;
  font-weight: 700;
  color: var(--mid-grey);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 2px;
}
"""

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>GroundWell Sound &amp; Wellness Center — Wix CMS &amp; Acuity Implementation</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>

<!-- ========================================== PAGE 01: COVER PAGE ========================================== -->
<div class="page" style="padding: 12mm 15mm 12mm 15mm; justify-content: space-between;">
  <div>
    <!-- Top Header Bar -->
    <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid var(--black); padding-bottom: 10px; margin-bottom: 14px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <img src="{LOGO_IMG}" style="width: 36px; height: 36px; border-radius: 8px;" alt="Axiom Global">
        <div>
          <div style="font-size: 13pt; font-weight: 800; letter-spacing: -0.4px;">AXIOM GLOBAL</div>
          <div style="font-size: 6.2pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--mid-grey);">Web Engineering &amp; Platform Architecture Practice</div>
        </div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 6.5pt; font-weight: 800; letter-spacing: 1.2px; text-transform: uppercase; background: var(--black); color: var(--white); padding: 3px 8px; border-radius: 3px; display: inline-block;">
          TECHNICAL IMPLEMENTATION PROPOSAL
        </div>
        <div style="font-size: 6.5pt; color: var(--mid-grey); margin-top: 3px;">Date: November 2026 &middot; Fixed-Price Delivery</div>
      </div>
    </div>

    <!-- Main Title Block -->
    <div style="margin-top: 6px; margin-bottom: 14px;">
      <div style="font-size: 7.2pt; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: var(--mid-grey); margin-bottom: 4px;">
        WIX CMS &middot; ACUITY SCHEDULING INTEGRATION &middot; FOUNDATIONAL SEO
      </div>
      <h1 class="serif-heading" style="font-size: 26pt; line-height: 1.08; color: var(--black); margin-bottom: 6px;">
        GroundWell Sound &amp; Wellness Center
      </h1>
      <div style="font-size: 11pt; font-weight: 500; color: var(--dark-charcoal); letter-spacing: -0.2px; font-style: italic;">
        End-to-End Build from Established Mockup with Dynamic CMS &amp; Conflict-Free Acuity Scheduling
      </div>
    </div>

    <!-- Hero Photography -->
    <div style="position: relative; width: 100%; height: 135mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--black); margin-bottom: 14px;">
      <img src="{HERO_IMG}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="GroundWell Sound Sanctuary">
      <div style="position: absolute; bottom: 12px; left: 14px; background: rgba(15, 17, 21, 0.88); color: #FFFFFF; padding: 6px 12px; border-radius: 3px; font-size: 6.8pt; letter-spacing: 0.5px;">
        <strong>GROUNDWELL SANCTUARY PLATFORM</strong> &middot; Seamless Visitor Discovery, Intuitive CMS Governance &amp; Multi-Staff Scheduling
      </div>
    </div>
  </div>

  <!-- Bottom Metadata Table -->
  <div>
    <div style="display: grid; grid-template-columns: 1.2fr 1.2fr 1fr 1fr; gap: 8px; border-top: 1px solid var(--black); padding-top: 10px; margin-bottom: 8px;">
      <div>
        <div style="font-size: 5.8pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Target Client</div>
        <div style="font-size: 8pt; font-weight: 700; color: var(--black);">GroundWell Center</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey);">Sound &amp; Wellness Sanctuary</div>
      </div>
      <div>
        <div style="font-size: 5.8pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Interactive Mockup</div>
        <div style="font-size: 8pt; font-weight: 700; color: var(--black);">Established Design</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey);">tinyurl.com/groundwellcentersite</div>
      </div>
      <div>
        <div style="font-size: 5.8pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Technical Leadership</div>
        <div style="font-size: 8pt; font-weight: 700; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey);">Tech Lead (6+ Years Exp)</div>
      </div>
      <div>
        <div style="font-size: 5.8pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Commercial Model</div>
        <div style="font-size: 8pt; font-weight: 700; color: var(--black);">$2,000 USD Fixed-Price</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey);">100% Budget Aligned</div>
      </div>
    </div>
    <div style="font-size: 6pt; color: #9CA3AF; text-align: center; border-top: 1px solid var(--border-grey); padding-top: 4px;">
      STRICTLY CONFIDENTIAL &middot; PREPARED EXCLUSIVELY FOR THE LEADERSHIP OF GROUNDWELL SOUND &amp; WELLNESS CENTER
    </div>
  </div>
</div>

<!-- ========================================== PAGE 02: EXECUTIVE SUMMARY ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">01 &middot; Executive Summary</div>
    </div>

    <span class="section-tag">Executive Summary &amp; Approach</span>
    <h1 class="page-title">Executive Summary</h1>
    
    <p class="lead-text">
      GroundWell Sound &amp; Wellness Center has successfully created an established interactive mockup (<code>tinyurl.com/groundwellcentersite</code>). The objective is to translate this design into a fully functional, production-ready Wix website integrated with Acuity Scheduling, structured Wix CMS collections, and local SEO foundations.
    </p>

    <!-- 4 High-Level Metrics -->
    <div class="grid-4" style="margin-bottom: 10px;">
      <div class="stat-box">
        <div class="stat-number">14+1</div>
        <div class="stat-label">Main Pages + Booking</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">02</div>
        <div class="stat-label">Shared CMS Templates</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">17</div>
        <div class="stat-label">Initial Offerings Populated</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">$2,000</div>
        <div class="stat-label">Fixed-Price Aligned</div>
      </div>
    </div>

    <!-- Core Strategic Pillars -->
    <div class="grid-2" style="margin-bottom: 10px;">
      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h2 class="block-title">The "Enter-Once" Wix CMS Vision</h2>
        <p class="body-text">
          Adding an offering must never require designing, copying, or manually duplicating a page. We architect <strong>two shared Wix dynamic templates</strong> (Classes/Workshops/Events and Certifications/Training). When you enter an offering into Wix CMS, it instantly populates its dedicated detail page, the primary Classes &amp; Events index, relevant modality pages (Sound, Reiki, Somatics), and the Homepage when marked as "Featured".
        </p>
      </div>

      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h2 class="block-title">Robust Acuity Scheduling Engine</h2>
        <p class="body-text">
          GroundWell coordinates multiple practitioners, distinct session durations, multi-day certification courses, and shared physical treatment rooms. We configure Acuity's native <strong>Rooms &amp; Resources</strong> to prevent room double-booking, embed seamless individual appointment widgets, configure reusable group pop-up modals, and connect digital intake waivers and gift certificate sales.
        </p>
      </div>
    </div>

    <!-- Our Engineering Pedigree -->
    <div class="card-bordered" style="background:#FAFAFC; border-left:3px solid var(--black); margin-bottom:8px;">
      <div style="font-size:7.8pt; font-weight:800; color:var(--black); margin-bottom:3px;">
        Senior Engineering Practice &middot; International Track Record
      </div>
      <p style="font-size:7pt; color:var(--dark-charcoal); line-height:1.4;">
        Led by <strong>Avishka Meddegoda</strong> (Technical Lead, 6+ Years Experience), our engineering squad brings enterprise technical discipline from Sri Lanka’s premier software technology firms (Arimac Digital core, enterprise cloud practices). Our senior developers have built international platforms across the US, UK, Australia (McGrath Real Estate Platform, Guardian Funds), and UAE (National History Museum, Al Ain Museum). We deliver bug-free, perfectly tested implementations built directly in accounts you own.
      </p>
    </div>

    <!-- Client Empowerment Commitment -->
    <div class="card-dark">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:3px;">
        <span style="font-size:8pt; font-weight:800;">Complete Client Independence Guarantee</span>
        <span class="badge" style="background:#FFFFFF; color:var(--black);">No Vendor Lock-In</span>
      </div>
      <p style="font-size:6.9pt; color:#E5E7EB; line-height:1.35;">
        You will never be dependent on an agency for routine operations. We build entirely within your owned Wix and Acuity accounts and provide a detailed, recorded video walkthrough showing exactly how to add CMS events, adjust calendar hours, and inspect bookings.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 02 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 03: WEBSITE SCOPE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">02 &middot; Website Scope</div>
    </div>

    <span class="section-tag">Page Hierarchy &amp; Sitemap Architecture</span>
    <h1 class="page-title">Website Scope: 14 Main Pages + Booking</h1>
    
    <p class="lead-text">
      We implement the full page structure established in your interactive mockup, ensuring consistent navigation, responsive hierarchy, and clear calls-to-action across all 14 main pages and the shared booking hub:
    </p>

    <!-- 14 Main Pages + Booking Hub Table -->
    <table class="editorial-table" style="margin-bottom:8px;">
      <thead>
        <tr>
          <th style="width: 5%;">#</th>
          <th style="width: 25%;">Page Name</th>
          <th style="width: 50%;">Core Content, Layout &amp; Interactive Features</th>
          <th style="width: 20%;">Functionality</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>01</strong></td>
          <td><strong>Home</strong></td>
          <td>Hero banner, welcome message, featured CMS offerings feed, modality highlights, testimonials.</td>
          <td>Dynamic CMS Feed</td>
        </tr>
        <tr>
          <td><strong>02</strong></td>
          <td><strong>Sound</strong></td>
          <td>Sound baths, crystal bowl therapy, frequency healing intro, connected CMS offerings feed.</td>
          <td>Modality Landing</td>
        </tr>
        <tr>
          <td><strong>03</strong></td>
          <td><strong>Reiki</strong></td>
          <td>Usui Reiki philosophy, individual energy sessions, practitioner intro, booking button.</td>
          <td>Modality Landing</td>
        </tr>
        <tr>
          <td><strong>04</strong></td>
          <td><strong>Tuning Forks</strong></td>
          <td>Biofield tuning, sonic acupuncture explanation, benefits overview, session booking CTA.</td>
          <td>Modality Landing</td>
        </tr>
        <tr>
          <td><strong>05</strong></td>
          <td><strong>Somatics</strong></td>
          <td>Somatic movement, nervous system regulation, embodied breathwork, connected events.</td>
          <td>Modality Landing</td>
        </tr>
        <tr>
          <td><strong>06</strong></td>
          <td><strong>Drumming</strong></td>
          <td>Rhythm journeys, shamanic drumming circles, community workshops, upcoming dates.</td>
          <td>Modality Landing</td>
        </tr>
        <tr>
          <td><strong>07</strong></td>
          <td><strong>Mentorship</strong></td>
          <td>1-on-1 practitioner mentorship programs, curriculum overview, application/booking CTA.</td>
          <td>Program Showcase</td>
        </tr>
        <tr>
          <td><strong>08</strong></td>
          <td><strong>Classes &amp; Events</strong></td>
          <td>Central chronological directory of upcoming workshops; filtered dynamically from Wix CMS.</td>
          <td>Wix CMS Directory</td>
        </tr>
        <tr>
          <td><strong>09</strong></td>
          <td><strong>Individual Sessions</strong></td>
          <td>Comprehensive directory of private 1-on-1 modalities, session lengths, practitioner profiles.</td>
          <td>Service Catalog</td>
        </tr>
        <tr>
          <td><strong>10</strong></td>
          <td><strong>Certifications &amp; Training</strong></td>
          <td>Multi-day professional sound &amp; energy training directory; filtered from Certifications CMS.</td>
          <td>Wix CMS Directory</td>
        </tr>
        <tr>
          <td><strong>11</strong></td>
          <td><strong>About</strong></td>
          <td>Sanctuary mission, facility philosophy, team biographies with More/Less expandable toggles.</td>
          <td>Interactive Bios</td>
        </tr>
        <tr>
          <td><strong>12</strong></td>
          <td><strong>Contact &amp; Visit</strong></td>
          <td>Interactive Google Map, parking &amp; arrival directions, custom contact form, newsletter signup.</td>
          <td>Visitor Hub &amp; Form</td>
        </tr>
        <tr>
          <td><strong>13</strong></td>
          <td><strong>Sound Instruments</strong></td>
          <td>Informational showcase (singing bowls, gongs, forks); "Email to Book Appointment" (No retail cart).</td>
          <td>Inquiry Only</td>
        </tr>
        <tr>
          <td><strong>14</strong></td>
          <td><strong>Gift Certificates</strong></td>
          <td>Dedicated gift certificate landing page linked from footer; direct Acuity purchase integration.</td>
          <td>Acuity Voucher Flow</td>
        </tr>
        <tr style="background:#F0FDF4;">
          <td><strong>+1</strong></td>
          <td><strong>Shared Booking Page</strong></td>
          <td>Unified individual appointment-booking hub with embedded Acuity multi-practitioner schedule.</td>
          <td>Acuity Embedded Engine</td>
        </tr>
      </tbody>
    </table>

    <!-- Visual Architecture Callout -->
    <div class="grid-2">
      <div class="card-bordered">
        <div style="font-weight:700; font-size:7.2pt; color:var(--black);">Sound Instruments Page Rule</div>
        <p class="body-text" style="font-size:6.6pt;">Per project brief, this page remains purely informational. An email inquiry trigger allows clients to book private instrument viewings. Zero online retail store or cart inventory overhead.</p>
      </div>
      <div class="card-bordered">
        <div style="font-weight:700; font-size:7.2pt; color:var(--black);">Gift Certificates Page Rule</div>
        <p class="body-text" style="font-size:6.6pt;">Directly connected to Acuity Gift Certificates. Allows digital purchasing and code redemption for sessions and events while cleanly excluding retail items.</p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 03 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 04: WIX CMS ARCHITECTURE ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">03 &middot; CMS Architecture</div>
    </div>

    <span class="section-tag">Dynamic Data Collections &amp; Templates</span>
    <h1 class="page-title">Wix CMS: 2 Templates &amp; 17 Offerings</h1>
    
    <p class="lead-text">
      The core requirement of this build is eliminating manual page duplication. We construct <strong>two shared Wix CMS dynamic templates</strong> populated with 17 initial content entries, creating an automated data pipeline across the entire site:
    </p>

    <!-- Two Template Breakdown Cards -->
    <div class="grid-2" style="margin-bottom: 9px;">
      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-weight:800; font-size:8pt;">TEMPLATE 01: Classes, Workshops &amp; Events</span>
          <span class="badge badge-dark">~13 Initial Entries</span>
        </div>
        <p class="body-text">
          A single shared dynamic page template that handles all sound baths, breathwork circles, and evening gatherings. Connects to the primary Classes &amp; Events calendar, filtered modality pages, and home page.
        </p>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-weight:800; font-size:8pt;">TEMPLATE 02: Certifications &amp; Training</span>
          <span class="badge badge-outline">~4 Initial Entries</span>
        </div>
        <p class="body-text">
          A shared dynamic template tailored for multi-day, accredited practitioner trainings. Features curriculum outlines, prerequisite schedules, certification credentials, and multi-day booking links.
        </p>
      </div>
    </div>

    <!-- Data Schema Table -->
    <div style="font-weight:800; font-size:7.5pt; color:var(--black); margin-bottom:3px;">
      GroundWell Wix CMS Collection Schema (Single Entry &rarr; Site-Wide Population)
    </div>
    <table class="editorial-table" style="margin-bottom:8px;">
      <thead>
        <tr>
          <th style="width: 25%;">Field Identifier</th>
          <th style="width: 15%;">Field Type</th>
          <th style="width: 45%;">Connected UI Placement &amp; Purpose</th>
          <th style="width: 15%;">Auto-Behavior</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>title</code> &amp; <code>slug</code></td>
          <td>Text / URL</td>
          <td>H1 title on detail page, card title, SEO-friendly descriptive URL string.</td>
          <td>Auto-generates URL</td>
        </tr>
        <tr>
          <td><code>modality_tag</code></td>
          <td>Tag Reference</td>
          <td>Connects offering to Sound, Reiki, Somatics, Drumming, or Tuning Forks pages.</td>
          <td>Auto-filters feeds</td>
        </tr>
        <tr>
          <td><code>event_date_time</code></td>
          <td>Date/Time</td>
          <td>Displays dates, times, and dictates chronological listing sequence.</td>
          <td>Chronological sort</td>
        </tr>
        <tr>
          <td><code>price_display</code></td>
          <td>Text / Currency</td>
          <td>Displays session price (e.g. $45 Sound Bath / $1,250 Certification).</td>
          <td>Formatted display</td>
        </tr>
        <tr>
          <td><code>main_image</code> &amp; <code>gallery</code></td>
          <td>Image Array</td>
          <td>Hero banner on detail page and responsive thumbnail on event cards.</td>
          <td>Responsive crops</td>
        </tr>
        <tr>
          <td><code>short_teaser</code></td>
          <td>Rich Text</td>
          <td>2-sentence summary appearing on index directory cards and homepage.</td>
          <td>Directory cards</td>
        </tr>
        <tr>
          <td><code>full_description</code></td>
          <td>Rich Text</td>
          <td>Comprehensive offering syllabus, preparation notes, and what to bring.</td>
          <td>Detail page body</td>
        </tr>
        <tr>
          <td><code>acuity_booking_url</code></td>
          <td>URL String</td>
          <td>Direct link to Acuity class/event ID; triggers reusable booking modal.</td>
          <td>Instant booking</td>
        </tr>
        <tr>
          <td><code>is_featured</code></td>
          <td>Boolean (Yes/No)</td>
          <td>When marked "Yes", automatically surfaces offering on Homepage hero feed.</td>
          <td>Homepage spotlight</td>
        </tr>
        <tr>
          <td><code>is_published</code></td>
          <td>Boolean (Yes/No)</td>
          <td>Allows client to draft offerings and toggle visibility without deleting data.</td>
          <td>Draft governance</td>
        </tr>
      </tbody>
    </table>

    <!-- Auto-Archive Callout -->
    <div class="card-bordered" style="background:#FAFAFC; border-left:3px solid var(--black);">
      <div style="font-size:7pt; font-weight:700; color:var(--black);">Automated Chronological Logic</div>
      <p style="font-size:6.7pt; color:var(--mid-grey); margin-top:2px; line-height:1.35;">
        Using Wix Dataset filters, all upcoming classes, workshops, and certifications automatically sort chronologically by <code>event_date_time</code>. Once an event date has passed, it automatically drops off the active listings without requiring manual client deletion.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 04 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 05: ACUITY SCHEDULING INTEGRATION ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">04 &middot; Acuity Scheduling</div>
    </div>

    <span class="section-tag">Multi-Staff &amp; Conflict-Free Operations</span>
    <h1 class="page-title">Acuity Scheduling Deep Dive</h1>
    
    <p class="lead-text">
      GroundWell’s operations require seamless coordination between multiple sound healers, reiki practitioners, and shared physical treatment rooms. We configure Acuity to operate as a bulletproof scheduling engine:
    </p>

    <!-- Visual Architecture Feature Image -->
    <div style="border: 1px solid var(--black); border-radius: 4px; overflow: hidden; height: 42mm; position: relative; margin-bottom: 9px;">
      <img src="{ACUITY_IMG}" style="width: 100%; height: 100%; object-fit: cover;" alt="Acuity Scheduling Architecture">
      <div style="position: absolute; bottom: 6px; left: 8px; background: rgba(0,0,0,0.85); color: #fff; padding: 4px 10px; font-size: 6.2pt; border-radius: 2px;">
        ACUITY SCHEDULING ENGINE: Multi-Practitioner Calendars, Shared Room Conflict Prevention &amp; Digital Intake Waivers
      </div>
    </div>

    <!-- 4 Key Acuity Configuration Modules -->
    <div class="grid-2" style="margin-bottom: 8px;">
      <!-- Module 1: Room Conflicts -->
      <div class="card-bordered" style="border-left:3px solid var(--black);">
        <div class="block-title" style="font-size:8pt;">01. Shared Room Conflict Prevention</div>
        <p class="body-text">
          Using Acuity’s <strong>Rooms &amp; Resources</strong> engine, we link each physical treatment room (e.g., "Sanctuary Room 1", "Sound Chamber") to appointment types. If Practitioner A books Room 1 at 2:00 PM, Acuity automatically blocks Practitioner B from booking Room 1 at that same hour, completely eliminating double-bookings.
        </p>
      </div>

      <!-- Module 2: Multi-Staff Individual Appointments -->
      <div class="card-bordered" style="border-left:3px solid var(--black);">
        <div class="block-title" style="font-size:8pt;">02. Individual Appointments &amp; Session Lengths</div>
        <p class="body-text">
          Configured with flexible durations (60-min, 75-min, 90-min) across multiple practitioners. Clients can either choose a specific practitioner or select "Any Available". Includes 15-minute automatic buffer times between sessions for sound bowl cleansing and room reset.
        </p>
      </div>

      <!-- Module 3: Group Classes & Certifications -->
      <div class="card-bordered" style="border-left:3px solid var(--black);">
        <div class="block-title" style="font-size:8pt;">03. Group Classes &amp; Multi-Day Training</div>
        <p class="body-text">
          Capacity-capped group bookings (e.g. 15 attendees max for Sound Baths). Supports recurring dates, drop-in tickets, and multi-day certification schedules where booking Day 1 automatically registers the student for all subsequent training modules.
        </p>
      </div>

      <!-- Module 4: Digital Waivers & Gift Certificates -->
      <div class="card-bordered" style="border-left:3px solid var(--black);">
        <div class="block-title" style="font-size:8pt;">04. Payments, Waivers &amp; Gift Certificates</div>
        <p class="body-text">
          Integrated Stripe/Square payment processing, coupon codes, and mandatory digital health intake waivers with digital signature checkboxes. Dedicated Gift Certificate setup enabling digital voucher generation, custom email delivery, and 1-click code redemption at checkout.
        </p>
      </div>
    </div>

    <!-- Embedded vs Popup Logic -->
    <div class="card-bordered" style="background:#FAFAFA;">
      <div style="font-weight:800; font-size:7.2pt; color:var(--black); margin-bottom:2px;">
        Embedded vs. Modal Booking Implementation
      </div>
      <p style="font-size:6.7pt; color:var(--dark-charcoal); line-height:1.35;">
        <strong>Individual Sessions:</strong> Uses an embedded iframe on the shared booking page with automatic resizing to prevent scroll clipping.<br>
        <strong>Group Events &amp; Workshops:</strong> Uses a clean, reusable modal pop-up triggered by the "Book Now" CTA on detail pages, ensuring the visitor stays immersed in the GroundWell website experience without jarring external redirects.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 05 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 06: PLATFORM BOUNDARIES: WIX VS ACUITY ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">05 &middot; Platform Governance</div>
    </div>

    <span class="section-tag">System Boundaries &amp; Mobile Considerations</span>
    <h1 class="page-title">Platform Governance: Wix vs. Acuity</h1>
    
    <p class="lead-text">
      As requested in your proposal requirements, we clearly delineate the architectural boundary between Wix and Acuity, and outline how mobile scheduling behaves:
    </p>

    <!-- Responsibility Matrix Table -->
    <div style="font-weight:800; font-size:7.5pt; color:var(--black); margin-bottom:3px;">
      Operational Matrix: Where Information is Managed &amp; Updated
    </div>
    <table class="editorial-table" style="margin-bottom:8px;">
      <thead>
        <tr>
          <th style="width: 30%;">Operational Area</th>
          <th style="width: 35%;">Managed in Wix CMS</th>
          <th style="width: 35%;">Managed in Acuity Scheduling</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Offering Content &amp; Storytelling</strong></td>
          <td>Offering titles, full descriptions, modality categories, hero photos, gallery images, and instructor bios.</td>
          <td>Basic appointment title &amp; confirmation email instructions only.</td>
        </tr>
        <tr>
          <td><strong>Dates, Times &amp; Display</strong></td>
          <td>Public marketing dates/times displayed on cards and chronological directory sorting.</td>
          <td>Actual real-time slot availability, booking deadlines, and capacity limits.</td>
        </tr>
        <tr>
          <td><strong>Pricing &amp; Transactions</strong></td>
          <td>Marketing price labels displayed on cards (e.g., "$55 per attendee").</td>
          <td>Actual credit card processing, deposit requirements, and tax calculation.</td>
        </tr>
        <tr>
          <td><strong>Practitioner Management</strong></td>
          <td>Team member photos, written biographies, and "Read More" profile cards.</td>
          <td>Practitioner calendar sync (Google/Apple), individual shift hours, and buffer times.</td>
        </tr>
        <tr>
          <td><strong>Room &amp; Resource Constraints</strong></td>
          <td>Descriptions of sanctuary spaces and room amenities.</td>
          <td>Physical room assignment, room conflict locks, and multi-staff resource pooling.</td>
        </tr>
        <tr>
          <td><strong>Intake &amp; Legal Compliance</strong></td>
          <td>General contact inquiries and newsletter email signups.</td>
          <td>Mandatory health intake forms, digital liability waivers, and emergency contacts.</td>
        </tr>
        <tr>
          <td><strong>Gift Certificates</strong></td>
          <td>Informational Gift Certificate landing page and footer link.</td>
          <td>Voucher creation, redemption codes, balance tracking, and expiry rules.</td>
        </tr>
      </tbody>
    </table>

    <!-- Mobile Considerations & Iframe Behavior -->
    <div class="grid-2" style="margin-bottom:7px;">
      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Mobile Scheduling UX &amp; Iframe Behavior</div>
        <p class="body-text">
          On mobile screens, standard iframes can cause iOS Safari double-scroll issues. We implement Acuity’s responsive viewport script with dynamic height auto-adjustment. On mobile, group offering booking buttons trigger an optimized overlay sheet, ensuring visitors can select dates and complete payments without pinch-zooming.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Automated Wix &harr; Acuity Sync (Optional Scope)</div>
        <p class="body-text">
          In the base scope, creating an offering involves entering content in Wix CMS and creating the class in Acuity (attaching the Acuity URL into the Wix row). If you desire 100% automated 2-way synchronization (where creating a class in Acuity automatically creates the Wix CMS item via webhooks/Zapier), we can deliver this as a separate add-on ($350 USD).
        </p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 06 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 07: DESIGN SYSTEM & MODALS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">06 &middot; Interactive Features</div>
    </div>

    <span class="section-tag">Interactive Mockup Fidelity &amp; Components</span>
    <h1 class="page-title">Design System, Modals &amp; Components</h1>
    
    <p class="lead-text">
      We execute with 100% fidelity to your established interactive mockup (<code>tinyurl.com/groundwellcentersite</code>), ensuring responsive precision, tranquil visual balance, and intuitive micro-interactions:
    </p>

    <!-- Visual Feature Banner -->
    <div style="border: 1px solid var(--black); border-radius: 4px; overflow: hidden; height: 42mm; position: relative; margin-bottom: 9px;">
      <img src="{SANCTUARY_IMG}" style="width: 100%; height: 100%; object-fit: cover;" alt="GroundWell Sanctuary Interior">
      <div style="position: absolute; bottom: 6px; left: 8px; background: rgba(0,0,0,0.85); color: #fff; padding: 4px 10px; font-size: 6.2pt; border-radius: 2px;">
        SERENE INTERACTION DESIGN: Thoughtful Whitespace, Expandable Bios &amp; Three Reusable Pop-Up Modals
      </div>
    </div>

    <!-- 3 Reusable Pop-Up Modals Breakdown -->
    <div style="font-weight:800; font-size:7.5pt; color:var(--black); margin-bottom:3px;">
      Three Reusable Modal Pop-Up Layouts (Site-Wide Lightboxes)
    </div>
    <div class="grid-3" style="margin-bottom: 9px;">
      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="font-weight:800; font-size:7.5pt; margin-bottom:2px;">MODAL 01: Booking Pop-Up</div>
        <p class="body-text">
          A clean, focused lightbox modal housing Acuity’s group offering scheduler. Opens smoothly from any detail page CTA, keeping the visitor anchored to the site without page reloads.
        </p>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="font-weight:800; font-size:7.5pt; margin-bottom:2px;">MODAL 02: FAQs &amp; Policies</div>
        <p class="body-text">
          Accessible from footers and offering sidebars. Clearly displays arrival guidelines, what to wear for sound baths, cancellation windows (e.g. 24h notice), and refund policies.
        </p>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="font-weight:800; font-size:7.5pt; margin-bottom:2px;">MODAL 03: Privacy &amp; Terms</div>
        <p class="body-text">
          Standard legal compliance modal covering website privacy practices, health disclaimer waivers, and studio code of conduct without requiring heavy independent landing pages.
        </p>
      </div>
    </div>

    <!-- Interactive Features Grid -->
    <div class="grid-3" style="gap:6px;">
      <div class="card-bordered">
        <div class="block-title" style="font-size:7.2pt;">Expandable Team Bios</div>
        <p class="body-text" style="font-size:6.5pt;">Clean compact practitioner cards featuring a smooth "Read More / Read Less" toggle to maintain tidy vertical rhythm on the About page.</p>
      </div>
      <div class="card-bordered">
        <div class="block-title" style="font-size:7.2pt;">Guest Collaborator Cards</div>
        <p class="body-text" style="font-size:6.5pt;">Modular profile callouts displayed on relevant workshop and event pages highlighting visiting sound masters and guest teachers.</p>
      </div>
      <div class="card-bordered">
        <div class="block-title" style="font-size:7.2pt;">Downloadable PDF Calendar</div>
        <p class="body-text" style="font-size:6.5pt;">A prominent button/link allowing visitors to download a printable monthly PDF schedule of upcoming sanctuary sound journeys.</p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 07 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 08: FOUNDATIONAL & LOCAL SEO ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">07 &middot; Foundational SEO</div>
    </div>

    <span class="section-tag">Search Visibility &amp; Structured Data</span>
    <h1 class="page-title">Foundational &amp; Local SEO Architecture</h1>
    
    <p class="lead-text">
      GroundWell is a physical wellness sanctuary that relies heavily on local search intent (e.g. "sound bath near me", "reiki healing sanctuary"). We engineer comprehensive foundational and local SEO into the website architecture:
    </p>

    <!-- 6 Core SEO Pillars -->
    <div class="grid-3" style="margin-bottom: 9px;">
      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Descriptive Location URLs</div>
        <p class="body-text">
          Logical URL hierarchy reflecting modality and location keyword relevance (e.g., <code>/sound-healing</code>, <code>/reiki-sessions</code>, <code>/classes-events/sound-bath</code>), avoiding generic IDs.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Dynamic CMS Meta Data</div>
        <p class="body-text">
          Automated SEO title tags and meta descriptions mapped directly to Wix CMS collection fields. When a new workshop is published, its SEO metadata generates automatically.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Schema Structured Data</div>
        <p class="body-text">
          Implementation of Schema.org JSON-LD structured data for <code>LocalBusiness</code>, <code>HealthAndBeautyBusiness</code>, and <code>Event</code> schema to qualify for Google rich search snippets.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Image &amp; Speed Optimization</div>
        <p class="body-text">
          Every uploaded photograph is compressed into modern WebP format, paired with descriptive alt-tags, and lazy-loaded to ensure rapid mobile page load times.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Internal Semantic Linking</div>
        <p class="body-text">
          Contextual links connecting individual modality pages (Sound, Somatics) directly to upcoming CMS classes, establishing topical authority for Google search algorithms.
        </p>
      </div>

      <div class="card-bordered">
        <div class="block-title" style="font-size:7.8pt;">Google Console &amp; Sitemap</div>
        <p class="body-text">
          XML sitemap verification, robots.txt configuration, and connection to Google Search Console to guarantee immediate indexing of all 14 pages and CMS dynamic detail routes.
        </p>
      </div>
    </div>

    <!-- SEO Scope Clarity Box -->
    <div class="card-dark" style="margin-bottom:6px;">
      <div style="font-size:7.8pt; font-weight:800; margin-bottom:3px;">Strict Scope Boundary: Technical Foundations vs. Ongoing Marketing</div>
      <p style="font-size:6.8pt; color:#E5E7EB; line-height:1.35;">
        Our scope includes complete technical, on-page, and local Schema SEO implementation at launch. Ongoing monthly backlink campaigns, commercial keyword blog writing, and Google Ads management are external marketing services outside this website development scope.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 08 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 09: 2026 SUBSCRIPTIONS & RECURRING COSTS ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">08 &middot; Subscription Costs</div>
    </div>

    <span class="section-tag">100% Verified 2026 Platform Pricing</span>
    <h1 class="page-title">Required Subscriptions &amp; Recurring Costs</h1>
    
    <p class="lead-text">
      To protect your operational budget and eliminate any financial surprises, below is the exact, verified 2026 subscription pricing for Wix and Acuity Scheduling, based on GroundWell's specific technical requirements:
    </p>

    <!-- Verified 2026 Subscription Comparison Cards -->
    <div class="grid-2" style="margin-bottom: 9px;">
      <!-- Wix Subscription Card -->
      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-weight:800; font-size:8.5pt;">WIX PLATFORM SUBSCRIPTION</span>
          <span class="badge badge-dark">2026 Verified Rates</span>
        </div>
        <div style="font-size: 14pt; font-weight: 800; color: var(--black); font-family: 'Playfair Display', serif;">
          $29 / mo <span style="font-size:7pt; font-family:'Plus Jakarta Sans',sans-serif; color:var(--mid-grey); font-weight:500;">(Billed Annually at $348/yr)</span>
        </div>
        <div style="font-size: 6.8pt; color: var(--mid-grey); margin-bottom: 6px;">
          Plan Choice: <strong>Wix Core Plan</strong> (or $36/mo on month-to-month billing)
        </div>
        <ul style="padding-left:14px; font-size:6.6pt; color:var(--dark-charcoal); line-height:1.45;">
          <li>✓ Connects custom domain and removes all Wix advertising.</li>
          <li>✓ <strong>Free Custom Domain Voucher</strong> included for the 1st year.</li>
          <li>✓ 50 GB cloud media storage (ample for high-res sound therapy galleries).</li>
          <li>✓ Up to 5 collaborator seats for staff &amp; practitioners.</li>
          <li>✓ Advanced custom form handling for visitor contact &amp; newsletter intake.</li>
          <li><em>Alternative Option:</em> Wix Light is available at $17/mo annual ($24/mo monthly), but offers only 2 GB storage and 2 collaborators. We recommend <strong>Wix Core</strong> for GroundWell's media catalog.</li>
        </ul>
      </div>

      <!-- Acuity Subscription Card -->
      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="font-weight:800; font-size:8.5pt;">ACUITY SCHEDULING SUBSCRIPTION</span>
          <span class="badge badge-dark">2026 Verified Rates</span>
        </div>
        <div style="font-size: 14pt; font-weight: 800; color: var(--black); font-family: 'Playfair Display', serif;">
          $27 / mo <span style="font-size:7pt; font-family:'Plus Jakarta Sans',sans-serif; color:var(--mid-grey); font-weight:500;">(Billed Annually at $324/yr)</span>
        </div>
        <div style="font-size: 6.8pt; color: var(--mid-grey); margin-bottom: 6px;">
          Plan Choice: <strong>Acuity Standard Plan</strong> (formerly "Growing", or $34/mo monthly)
        </div>
        <ul style="padding-left:14px; font-size:6.6pt; color:var(--dark-charcoal); line-height:1.45;">
          <li>✓ <strong>Up to 6 Staff/Room Calendars:</strong> Mandatory to support multiple practitioners + shared treatment room conflict prevention.</li>
          <li>✓ <strong>Gift Certificates &amp; Packages:</strong> Required for digital gift certificate sales and redemption (excluded on basic plan).</li>
          <li>✓ <strong>Automated SMS/Text Reminders:</strong> Drastically reduces client appointment no-shows.</li>
          <li>✓ Mandatory digital intake forms and liability waivers prior to booking.</li>
          <li>✓ 2-way Google/Apple personal calendar synchronization for practitioners.</li>
          <li><em>Note:</em> The basic "Starter" plan ($16/mo) supports only 1 calendar and excludes gift certificates and SMS, making <strong>Standard</strong> the required tier.</li>
        </ul>
      </div>
    </div>

    <!-- Ancillary Operational Costs Table -->
    <div style="font-weight:800; font-size:7.5pt; color:var(--black); margin-bottom:3px;">
      Ancillary Operational &amp; Transaction Costs (100% Transparent)
    </div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">Service Item</th>
          <th style="width: 45%;">Description &amp; Operational Function</th>
          <th style="width: 15%;">Billing Cycle</th>
          <th style="width: 15%;">2026 Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Custom Domain Name</strong></td>
          <td>e.g. <code>groundwellcenter.com</code> (Free 1st year with annual Wix plan).</td>
          <td>Annual Renewal</td>
          <td>~$15–$25 / year</td>
        </tr>
        <tr>
          <td><strong>Payment Processing</strong></td>
          <td>Stripe / Square transaction fees for online appointment &amp; event checkout.</td>
          <td>Per Transaction</td>
          <td>2.9% + $0.30</td>
        </tr>
        <tr>
          <td><strong>Professional Email (Optional)</strong></td>
          <td>Google Workspace for custom domain email (e.g. <code>hello@groundwellcenter.com</code>).</td>
          <td>Monthly / User</td>
          <td>~$6–$7 / month</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 09 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 10: OUR TECHNICAL LEADERSHIP & SQUAD ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">09 &middot; Engineering Squad</div>
    </div>

    <span class="section-tag">Talent &amp; Proven International Track Record</span>
    <h1 class="page-title">Technical Leadership &amp; Engineering Squad</h1>
    
    <p class="lead-text">
      GroundWell will be supported by a seasoned five-member software engineering squad led by Technical Lead <strong>Avishka Meddegoda</strong>. Our engineers work at Sri Lanka’s premier software technology firms, delivering mission-critical platforms for international clients worldwide:
    </p>

    <!-- Key Leadership Profiles -->
    <div class="grid-2" style="margin-bottom: 8px;">
      <!-- Avishka Meddegoda -->
      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div>
            <div style="font-size: 9pt; font-weight: 800; color: var(--black);">Avishka Meddegoda</div>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Technical Lead &middot; 6+ Years Experience</div>
          </div>
          <span class="badge badge-dark">Technical Lead</span>
        </div>
        <p class="body-text" style="margin-top: 4px; margin-bottom: 4px;">
          <strong>Responsibilities:</strong> Oversees end-to-end technical architecture, Acuity API integrations, room conflict logic, data security, and QA verification.
        </p>
        <div style="font-size: 6.3pt; color: var(--dark-charcoal); line-height: 1.35; background: #F8FAFC; padding: 5px; border-radius: 3px;">
          <strong>Track Record:</strong> Senior Full-Stack Engineer at Sri Lanka's leading digital firm; published IEEE author. Architected high-concurrency systems across the UAE, Middle East, and US. Expertise in Java Spring Boot, Node.js, API security, and platform integrations.
        </div>
      </div>

      <!-- Viranga Lakshan -->
      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
          <div>
            <div style="font-size: 9pt; font-weight: 800; color: var(--black);">Viranga Lakshan</div>
            <div style="font-size: 6.8pt; font-weight: 700; color: var(--mid-grey);">Client Solutions Architect &middot; 2+ Years Experience</div>
          </div>
          <span class="badge badge-dark">Client Liaison</span>
        </div>
        <p class="body-text" style="margin-top: 4px; margin-bottom: 4px;">
          <strong>Responsibilities:</strong> Direct client communications, Wix CMS collection schema design, dynamic template layout implementation, and handover training.
        </p>
        <div style="font-size: 6.3pt; color: var(--dark-charcoal); line-height: 1.35; background: #F8FAFC; padding: 5px; border-radius: 3px;">
          <strong>Track Record:</strong> Specialized in Headless CMS, React/Next.js, and platform builds for international cultural and enterprise institutions (including National History Museum Abu Dhabi and Al Ain Museum).
        </div>
      </div>
    </div>

    <!-- Supporting Engineering Specialists -->
    <div class="grid-3" style="margin-bottom: 8px;">
      <!-- Chamara Lahiru -->
      <div class="card-bordered">
        <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Chamara Lahiru</div>
        <div style="font-size: 6.2pt; font-weight: 700; color: var(--mid-grey); margin-bottom: 2px;">Senior Frontend Lead &middot; 6+ Yrs</div>
        <p class="body-text" style="font-size: 6.4pt;">
          <strong>Role:</strong> Responsive layout execution, touch-first mobile styling, and modal micro-interactions.
        </p>
        <div style="font-size: 5.9pt; color: var(--dark-charcoal); margin-top: 2px;">
          Delivered <strong>McGrath Real Estate (Australia)</strong> frontend.
        </div>
      </div>

      <!-- Janith Kavishka -->
      <div class="card-bordered">
        <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Janith Kavishka</div>
        <div style="font-size: 6.2pt; font-weight: 700; color: var(--mid-grey); margin-bottom: 2px;">Full-Stack Integrator &middot; 2+ Yrs</div>
        <p class="body-text" style="font-size: 6.4pt;">
          <strong>Role:</strong> Acuity intake form mapping, payment webhook testing, and room conflict rule verification.
        </p>
        <div style="font-size: 5.9pt; color: var(--dark-charcoal); margin-top: 2px;">
          Enterprise database and integration specialist.
        </div>
      </div>

      <!-- Lithumitha Ravikumar -->
      <div class="card-bordered">
        <div style="font-size: 8pt; font-weight: 800; color: var(--black);">Lithumitha Ravikumar</div>
        <div style="font-size: 6.2pt; font-weight: 700; color: var(--mid-grey); margin-bottom: 2px;">Project Manager &middot; 2 Yrs</div>
        <p class="body-text" style="font-size: 6.4pt;">
          <strong>Role:</strong> Milestone schedule tracking, daily asynchronous client reports, and multi-browser QA.
        </p>
        <div style="font-size: 5.9pt; color: var(--dark-charcoal); margin-top: 2px;">
          Managed delivery for <strong>Guardian Funds (Australia)</strong>.
        </div>
      </div>
    </div>

    <!-- Office Image -->
    <div style="border: 1px solid var(--black); border-radius: 4px; overflow: hidden; height: 32mm; position: relative;">
      <img src="{TEAM_IMG}" style="width: 100%; height: 100%; object-fit: cover;" alt="Axiom Global Engineering Squad">
      <div style="position: absolute; bottom: 6px; left: 8px; background: rgba(0,0,0,0.85); color: #fff; padding: 4px 10px; font-size: 6.2pt; border-radius: 2px;">
        AXIOM GLOBAL ENGINEERING PRACTICE: Professional Engineers Delivering Global Digital Platforms
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 10 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 11: PROJECT TIMELINE & MILESTONES ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">10 &middot; Delivery Roadmap</div>
    </div>

    <span class="section-tag">Predictable Velocity &amp; Phased Execution</span>
    <h1 class="page-title">Project Timeline &amp; Milestones</h1>
    
    <p class="lead-text">
      We execute through a structured 4-week delivery roadmap, ensuring full alignment with your interactive mockup, thorough testing of scheduling conflicts, and complete handover before launch:
    </p>

    <!-- Weekly Milestones Table -->
    <table class="editorial-table" style="margin-bottom:8px;">
      <thead>
        <tr>
          <th style="width: 15%;">Phase / Week</th>
          <th style="width: 45%;">Technical Implementation &amp; Key Milestones</th>
          <th style="width: 25%;">Client Review &amp; Inputs</th>
          <th style="width: 15%;">Verification</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Week 01</strong><br><span style="font-size:5.8pt; color:var(--mid-grey);">Days 1–5</span></td>
          <td>
            <strong>Foundation &amp; Page Architecture</strong><br>
            Wix workspace setup in client account; global typography, navigation header &amp; footer; build 14 static main page structures from mockup.
          </td>
          <td>Provide Wix/Acuity collaborator invites; provide brand assets &amp; photography.</td>
          <td><span class="badge badge-dark">Milestone 1</span></td>
        </tr>
        <tr>
          <td><strong>Week 02</strong><br><span style="font-size:5.8pt; color:var(--mid-grey);">Days 6–10</span></td>
          <td>
            <strong>Wix CMS &amp; Dynamic Templates</strong><br>
            Build 2 shared CMS detail templates (Events &amp; Certifications); establish schema fields; populate initial ~17 offerings; configure chronological sorting.
          </td>
          <td>Review CMS collection entries &amp; detail page staging preview.</td>
          <td><span class="badge badge-dark">Milestone 1</span></td>
        </tr>
        <tr>
          <td><strong>Week 03</strong><br><span style="font-size:5.8pt; color:var(--mid-grey);">Days 11–15</span></td>
          <td>
            <strong>Acuity Scheduling Integration</strong><br>
            Configure multi-practitioner sessions, session lengths, group classes, room conflict locks, digital waivers, coupon codes, and gift certificates; embed widgets.
          </td>
          <td>Connect Stripe/Square account; verify practitioner working hours.</td>
          <td><span class="badge badge-dark">Milestone 2</span></td>
        </tr>
        <tr>
          <td><strong>Week 04</strong><br><span style="font-size:5.8pt; color:var(--mid-grey);">Days 16–20</span></td>
          <td>
            <strong>Modals, SEO, QA &amp; Handover</strong><br>
            Build 3 pop-ups (Booking, FAQs, Privacy); implement local SEO schema; execute room conflict test orders; recorded training video; <strong>Go-Live!</strong>
          </td>
          <td>Execute final content replacement round; sign off on launch.</td>
          <td><span class="badge" style="background:#22C55E; color:#fff;">Go-Live!</span></td>
        </tr>
      </tbody>
    </table>

    <!-- Project Governance Guarantee -->
    <div class="grid-3" style="gap:6px;">
      <div class="card-bordered">
        <div style="font-weight:700; font-size:6.8pt; color:var(--black);">Daily Async Standups</div>
        <p class="body-text" style="font-size:6.2pt;">Transparent daily progress updates via Upwork/Slack detailing completed tasks and upcoming milestones.</p>
      </div>
      <div class="card-bordered">
        <div style="font-weight:700; font-size:6.8pt; color:var(--black);">Recorded Loom Demos</div>
        <p class="body-text" style="font-size:6.2pt;">Weekly video walkthroughs demonstrating live features in staging for easy, non-technical review.</p>
      </div>
      <div class="card-bordered">
        <div style="font-weight:700; font-size:6.8pt; color:var(--black);">Built in Owned Accounts</div>
        <p class="body-text" style="font-size:6.2pt;">Development occurs strictly inside your own Wix and Acuity accounts for 100% security and zero transfer friction.</p>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 11 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 12: DELIVERABLES CHECKLIST ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">11 &middot; Deliverables Checklist</div>
    </div>

    <span class="section-tag">Quality Assurance &amp; Handover Protocol</span>
    <h1 class="page-title">Deliverables Checklist</h1>
    
    <p class="lead-text">
      Every deliverable is verified against strict functional acceptance criteria before project completion and sign-off:
    </p>

    <!-- Complete Deliverables Checklist -->
    <div class="grid-2" style="margin-bottom: 9px;">
      <div class="card-bordered" style="border-top: 3px solid var(--black);">
        <div style="font-weight:800; font-size:7.8pt; margin-bottom:4px; color:var(--black);">Website &amp; CMS Deliverables</div>
        <ul style="padding-left:14px; font-size:6.6pt; color:var(--dark-charcoal); line-height:1.45;">
          <li>✓ 14 main responsive pages faithfully translated from interactive mockup.</li>
          <li>✓ 1 shared individual appointment-booking hub page with embedded Acuity.</li>
          <li>✓ 2 shared Wix CMS dynamic detail templates (Events &amp; Certifications).</li>
          <li>✓ Initial ~17 offerings populated with descriptions, images, prices &amp; links.</li>
          <li>✓ Automated chronological sorting of upcoming classes &amp; auto-archive.</li>
          <li>✓ Dynamic cross-population to modality pages and Homepage featured feed.</li>
          <li>✓ Compact practitioner biographies with "Read More/Less" expansion toggles.</li>
          <li>✓ Informational Sound Instruments showcase with email appointment button.</li>
          <li>✓ 3 reusable site-wide modal pop-ups (Booking, FAQs/Policies, Privacy/Terms).</li>
          <li>✓ Downloadable monthly PDF calendar link/button implementation.</li>
        </ul>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black); background:#FAFAFC;">
        <div style="font-weight:800; font-size:7.8pt; margin-bottom:4px; color:var(--black);">Acuity, SEO &amp; Handover Deliverables</div>
        <ul style="padding-left:14px; font-size:6.6pt; color:var(--dark-charcoal); line-height:1.45;">
          <li>✓ Acuity initial setup for multi-practitioners and distinct session lengths.</li>
          <li>✓ Shared treatment-room configuration with automated conflict prevention.</li>
          <li>✓ Digital health intake forms and mandatory liability waivers.</li>
          <li>✓ Stripe/Square payment gateway connection and test transaction validation.</li>
          <li>✓ Gift Certificate purchasing page and 1-click checkout redemption flow.</li>
          <li>✓ Practitioner 2-way Google/Apple personal calendar synchronization.</li>
          <li>✓ Complete foundational SEO: URLs, meta titles, descriptions, Schema JSON-LD.</li>
          <li>✓ 1 consolidated final round of client content and photography replacement.</li>
          <li>✓ Custom domain connection, SSL certificate verification, and DNS routing.</li>
          <li>✓ <strong>Recorded Video Walkthrough (Loom):</strong> Step-by-step training on adding CMS offerings, updating calendar availability, and inspecting client bookings.</li>
        </ul>
      </div>
    </div>

    <!-- Client Handover Training Box -->
    <div class="card-dark" style="margin-bottom:6px;">
      <div style="font-size:7.8pt; font-weight:800; margin-bottom:3px;">Recorded Video Handover Training (No Ongoing Agency Retainer Needed)</div>
      <p style="font-size:6.8pt; color:#E5E7EB; line-height:1.35;">
        You receive a tailored, high-resolution recorded video walkthrough. We demonstrate how easy it is to add a new sound bath in Wix CMS, how to adjust holiday hours in Acuity, and how to issue gift vouchers. Your team will have complete, permanent autonomy over your platform.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 12 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 13: COMMERCIAL PROPOSAL ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">12 &middot; Commercial Terms</div>
    </div>

    <span class="section-tag">Fixed-Price Alignment &amp; Escrow Milestones</span>
    <h1 class="page-title">Commercial Terms &amp; Budget Alignment</h1>
    
    <p class="lead-text">
      We operate strictly within agreed, fixed-price commercial terms. We fully accept and align with your project’s posted fixed-price budget ($2,000 USD), structured across transparent Upwork escrow milestones:
    </p>

    <!-- Pricing Summary Cards -->
    <div class="grid-3" style="margin-bottom: 9px;">
      <div class="card-bordered" style="border-top: 3px solid var(--black); text-align: center;">
        <div class="badge badge-stage" style="margin-bottom: 3px;">TOTAL FIXED PRICE</div>
        <div style="font-size: 16pt; font-weight: 800; color: var(--black); font-family: 'Playfair Display', serif;">$2,000 USD</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey); margin-top: 2px;">100% Budget Aligned</div>
        <div style="font-size: 6pt; color: var(--dark-charcoal); margin-top: 4px; border-top: 1px solid var(--border-grey); padding-top: 4px;">
          Includes complete 14+1 pages, 2 CMS templates, Acuity &amp; SEO.
        </div>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black); text-align: center;">
        <div class="badge badge-outline" style="margin-bottom: 3px;">REVISION ALLOWANCE</div>
        <div style="font-size: 16pt; font-weight: 800; color: var(--black); font-family: 'Playfair Display', serif;">2 Full Rounds</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey); margin-top: 2px;">Iterative Staging Reviews</div>
        <div style="font-size: 6pt; color: var(--dark-charcoal); margin-top: 4px; border-top: 1px solid var(--border-grey); padding-top: 4px;">
          Covers layout feedback &amp; 1 consolidated content-replacement round.
        </div>
      </div>

      <div class="card-bordered" style="border-top: 3px solid var(--black); background: #FAFAFC; text-align: center;">
        <div class="badge badge-dark" style="margin-bottom: 3px;">POST-LAUNCH SUPPORT</div>
        <div style="font-size: 16pt; font-weight: 800; color: var(--black); font-family: 'Playfair Display', serif;">30-Day Warranty</div>
        <div style="font-size: 6.5pt; color: var(--mid-grey); margin-top: 2px;">Complimentary Bug-Fix SLA</div>
        <div style="font-size: 6pt; color: var(--dark-charcoal); margin-top: 4px; border-top: 1px solid var(--border-grey); padding-top: 4px;">
          Immediate assistance for any technical or scheduling conflicts.
        </div>
      </div>
    </div>

    <!-- Escrow Milestone Schedule Table -->
    <table class="editorial-table" style="margin-bottom:8px;">
      <thead>
        <tr>
          <th style="width: 25%;">Milestone Release</th>
          <th style="width: 45%;">Deliverables &amp; Verification Criteria</th>
          <th style="width: 15%;">Share</th>
          <th style="width: 15%;">Amount (USD)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Milestone 1: Setup &amp; CMS Foundation</strong></td>
          <td>14 static main pages built from mockup; 2 shared CMS templates built; initial 17 offerings populated with chronological sorting.</td>
          <td>40%</td>
          <td>$800 USD</td>
        </tr>
        <tr>
          <td><strong>Milestone 2: Acuity Engine &amp; Modals</strong></td>
          <td>Acuity multi-practitioner schedules, room conflict rules, intake waivers, gift certificates, and 3 pop-up modals configured &amp; tested.</td>
          <td>40%</td>
          <td>$800 USD</td>
        </tr>
        <tr>
          <td><strong>Milestone 3: Final QA, Training &amp; Launch</strong></td>
          <td>Consolidated content replacement, payment &amp; booking tests, foundational SEO setup, domain cutover, and recorded video walkthrough.</td>
          <td>20%</td>
          <td>$400 USD</td>
        </tr>
      </tbody>
    </table>

    <!-- Exclusions Clarity Box -->
    <div class="card-bordered" style="background:#FAFAFA;">
      <div style="font-weight:800; font-size:7.2pt; color:var(--black); margin-bottom:2px;">
        Exclusions Identified in Base Scope (Zero Hidden Ambiguity)
      </div>
      <p style="font-size:6.6pt; color:var(--dark-charcoal); line-height:1.35;">
        Per project brief: Ongoing monthly website maintenance, monthly printable PDF calendar graphic design, online retail store shopping cart functionality, and custom automated 2-way Wix-Acuity webhook synchronization are outside the base scope.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 13 of 14</div>
  </div>
</div>

<!-- ========================================== PAGE 14: WHY CHOOSE OUR TEAM & CLOSING ========================================== -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="header-left">GroundWell Sound &middot; Wix CMS &amp; Acuity Implementation</div>
      <div class="header-right">13 &middot; Partnership Commitment</div>
    </div>

    <span class="section-tag">Why Axiom Global &middot; Partnership Commitment</span>
    <h1 class="page-title">Why Partner With Axiom Global?</h1>
    
    <p class="lead-text">
      GroundWell is an extraordinary sound and wellness sanctuary that deserves an equally disciplined, tranquil, and reliable technical implementation:
    </p>

    <!-- 4 Core Practice Value Pillars -->
    <div class="grid-2" style="margin-bottom: 9px;">
      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h3 class="block-title" style="font-size:8.2pt;">01. Deep Wix CMS &amp; Dynamic Data Fluency</h3>
        <p class="body-text">
          We understand Wix Datasets, Dynamic Pages, and content collections deeply. We engineer clean data structures that guarantee adding future sound baths or certification dates will be as simple as filling out a 30-second form.
        </p>
      </div>

      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h3 class="block-title" style="font-size:8.2pt;">02. Bulletproof Acuity Conflict Prevention</h3>
        <p class="body-text">
          Shared treatment rooms are the #1 source of scheduling chaos for wellness centers. We configure Acuity’s resource pools with rigorous precision, ensuring your practitioners and sound healers never experience room overlap.
        </p>
      </div>

      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h3 class="block-title" style="font-size:8.2pt;">03. Mockup Fidelity &amp; Design Respect</h3>
        <p class="body-text">
          You already did the hard work establishing an elegant interactive mockup. We treat your mockup as an exact specification, maintaining pixel-perfect typographic hierarchy, serene whitespace, and responsive poise across every device.
        </p>
      </div>

      <div class="card-bordered" style="border-left: 3px solid var(--black);">
        <h3 class="block-title" style="font-size:8.2pt;">04. Senior Engineering Squad Redundancy</h3>
        <p class="body-text">
          Unlike solo freelancers who get overwhelmed or disappear, our five-member senior engineering squad provides complete delivery security, continuous progress, and peer-reviewed code quality under Technical Lead Avishka Meddegoda.
        </p>
      </div>
    </div>

    <!-- Closing Callout Box -->
    <div class="card-dark" style="padding: 14px 18px; margin-bottom: 9px;">
      <div style="font-size: 11pt; font-weight: 800; font-family: 'Playfair Display', serif; margin-bottom: 4px;">
        Let’s Bring the GroundWell Sanctuary to Life.
      </div>
      <p style="font-size: 7.2pt; color: #D1D5DB; line-height: 1.45; margin-bottom: 8px;">
        We appreciate the opportunity to submit this proposal. We are ready to commence development immediately within your owned Wix and Acuity accounts upon milestone agreement.
      </p>
      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:8px;">
        <div>
          <div style="font-size:8pt; font-weight:800; color:#FFFFFF;">Avishka Meddegoda &middot; Technical Lead</div>
          <div style="font-size:6.5pt; color:#9CA3AF;">Viranga Lakshan &middot; Client Solutions Architect &middot; Axiom Global</div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:7pt; color:#FBBF24; font-weight:700;">virangalakshanz@gmail.com &middot; +94 71 378 1359</div>
          <div style="font-size:6.2pt; color:#9CA3AF;">axiomglobal.tech &middot; Global Enterprise Delivery</div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; WIX CMS &amp; ACUITY SCHEDULING PROPOSAL</div>
    <div class="footer-page-num">Page 14 of 14</div>
  </div>
</div>

</body>
</html>
"""

def generate_pdf():
    # 1. Write HTML
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"HTML written to {HTML_PATH}")

    # 2. Compile via Playwright
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

    # 3. Verify Page Count with PyPDF
    reader = pypdf.PdfReader(PDF_PATH)
    total_pages = len(reader.pages)
    print(f"Total Page Count: {total_pages}")
    assert total_pages == 14, f"Expected 14 pages, got {total_pages}"
    print("PAGE COUNT VERIFICATION PASSED: Exactly 14 pages.")

if __name__ == "__main__":
    generate_pdf()
