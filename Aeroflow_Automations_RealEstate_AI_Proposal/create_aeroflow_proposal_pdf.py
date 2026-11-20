import os
import asyncio
from playwright.async_api import async_playwright
import pypdf

BASE_DIR = r"c:\Users\Viranga\Downloads\upwrok new\Aeroflow_Automations_RealEstate_AI_Proposal"
IMG_DIR = os.path.join(BASE_DIR, "images")
HTML_PATH = os.path.join(BASE_DIR, "proposal_template.html")
PDF_PATH = os.path.join(BASE_DIR, "Aeroflow_Automations_RealEstate_AI_Proposal.pdf")

def to_uri(fname):
    return os.path.join(IMG_DIR, fname).replace("\\", "/")

COVER_IMG = to_uri("realestate_cover.jpg")
LUXURY_HERO = to_uri("luxury_hero.jpg")
PROP_MODERN = to_uri("prop_modern.jpg")
TEAM_IMG = to_uri("team_office.jpg")
LOGO_IMG = to_uri("axiom_logo.png")

CSS_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap');

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
  font-size: 8.5pt;
  line-height: 1.44;
  -webkit-font-smoothing: antialiased;
}

.page {
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
}

@media print {
  body { background: transparent; }
  .page { margin: 0; box-shadow: none; page-break-after: always; }
}

/* Running Header */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1.5px solid var(--black);
  padding-bottom: 4px;
  margin-bottom: 8px;
}

.header-left {
  font-size: 7.2pt;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--black);
}

.header-right {
  font-size: 7.2pt;
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
  padding-top: 4px;
  margin-top: auto;
}

.footer-left {
  font-size: 6.8pt;
  font-weight: 600;
  color: var(--mid-grey);
  letter-spacing: 0.5px;
}

.footer-page-num {
  font-size: 7.2pt;
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
  font-size: 6.6pt;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--black);
  margin-bottom: 2px;
}

.page-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 18.5pt;
  font-weight: 700;
  line-height: 1.12;
  color: var(--black);
  margin-bottom: 5px;
}

.lead-text {
  font-size: 9pt;
  line-height: 1.44;
  color: var(--dark-charcoal);
  margin-bottom: 7px;
  max-width: 98%;
}

.block-title {
  font-size: 9.5pt;
  font-weight: 800;
  letter-spacing: -0.2px;
  color: var(--black);
  margin-bottom: 3px;
  display: flex;
  align-items: center;
  gap: 6px;
}

/* Tables */
table.editorial-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.6pt;
  margin-bottom: 5px;
}

table.editorial-table th {
  background: var(--black);
  color: var(--white);
  text-align: left;
  padding: 5px 8px;
  font-weight: 700;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-size: 6.8pt;
}

table.editorial-table td {
  padding: 4.5px 8px;
  border-bottom: 1px solid var(--border-grey);
  color: var(--dark-charcoal);
  vertical-align: top;
}

table.editorial-table tr:nth-child(even) td {
  background: #FAFAFC;
}

/* Cards & Layout */
.editorial-card {
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 7px 10px;
  background: var(--white);
  margin-bottom: 5px;
}

.editorial-card-grey {
  border: 1px solid var(--border-grey);
  border-radius: 4px;
  padding: 7px 10px;
  background: #F9FAFB;
  margin-bottom: 5px;
}

.editorial-card-black {
  background: var(--black);
  color: var(--white);
  border-radius: 4px;
  padding: 8px 12px;
  margin-bottom: 5px;
}

.editorial-card-black h3, .editorial-card-black h4 { color: var(--white); }
.editorial-card-black p { color: #D1D5DB; }

/* Badges */
.badge {
  display: inline-block;
  font-size: 6.4pt;
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

.code-box {
  background: #0F1115;
  color: #F3F4F6;
  padding: 5px 8px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 6.6pt;
  line-height: 1.35;
  border-left: 3px solid var(--black);
  margin: 3px 0 5px 0;
}
"""

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Aeroflow Automations &middot; Real Estate AI Sales Assistant &amp; Appointment Setter Proposal</title>
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
        <img src="{LOGO_IMG}" style="width: 38px; height: 38px; border-radius: 8px;" alt="Axiom Global">
        <div>
          <div style="font-size: 14pt; font-weight: 800; letter-spacing: -0.4px;">AXIOM GLOBAL</div>
          <div style="font-size: 6.8pt; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--mid-grey);">Enterprise AI Architecture &amp; Automation Practice</div>
        </div>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1.2px; text-transform: uppercase; background: var(--black); color: var(--white); padding: 3px 8px; border-radius: 3px; display: inline-block;">
          WHITE-LABEL PARTNERSHIP PROPOSAL
        </div>
        <div style="font-size: 7pt; color: var(--mid-grey); margin-top: 3px;">Date: November 2026 &middot; Fixed-Price &amp; Retainer</div>
      </div>
    </div>

    <!-- Main Title Block -->
    <div style="margin-top: 6px; margin-bottom: 14px;">
      <div style="font-size: 7.6pt; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: var(--mid-grey); margin-bottom: 4px;">
        MAKE.COM &middot; VOICEFLOW &middot; OPENAI FUNCTION CALLING &middot; VAPI AI VOICE &middot; CALENDAR SYNC
      </div>
      <h1 class="serif-heading" style="font-size: 25pt; line-height: 1.08; color: var(--black); margin-bottom: 6px;">
        Aeroflow Automations
      </h1>
      <div style="font-size: 11.5pt; font-weight: 500; color: var(--dark-charcoal); letter-spacing: -0.2px; font-style: italic;">
        Omnichannel Real Estate AI Sales Assistant &amp; Autonomous Appointment Setter Engine
      </div>
    </div>

    <!-- Hero Photography (Full Color) -->
    <div style="position: relative; width: 100%; height: 132mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--black); margin-bottom: 14px;">
      <img src="{COVER_IMG}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Real Estate AI Automation Architecture">
      <div style="position: absolute; bottom: 12px; left: 14px; background: rgba(15, 17, 21, 0.88); color: #FFFFFF; padding: 6px 12px; border-radius: 3px; font-size: 7.2pt; letter-spacing: 0.5px;">
        <strong>AEROFLOW AUTOMATIONS ENGINE</strong> &middot; Multi-Channel Sub-30s Lead Qualification &amp; Automated Calendar Booking
      </div>
    </div>
  </div>

  <!-- Bottom Metadata Table -->
  <div>
    <div style="display: grid; grid-template-columns: 1.2fr 1.2fr 1fr 1fr; gap: 8px; border-top: 1px solid var(--black); padding-top: 10px; margin-bottom: 8px;">
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Target Agency</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Aeroflow Automations</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">US Real Estate Agency Pipeline</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Partnership Terms</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">100% White-Label &amp; IP</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Client Account Ownership Confirmed</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Technical Leadership</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">Avishka Meddegoda</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Tech Lead (6+ Years Exp)</div>
      </div>
      <div>
        <div style="font-size: 6.2pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">Commercial Model</div>
        <div style="font-size: 8.5pt; font-weight: 700; color: var(--black);">$1,000 / Build + $100/mo</div>
        <div style="font-size: 7pt; color: var(--mid-grey);">Recurring Retainer per Client</div>
      </div>
    </div>

    <div class="page-footer" style="border-top: 1px solid var(--border-grey); padding-top: 5px;">
      <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
      <div class="footer-page-num">Page 01 of 10</div>
    </div>
  </div>
</div>

<!-- ========================================== PAGE 02: EXECUTIVE SUMMARY & VISION ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 01 &middot; EXECUTIVE ARCHITECTURE SUMMARY</div>
    <div class="header-right">AEROFLOW AUTOMATIONS BLUEPRINT</div>
  </div>

  <div>
    <div class="section-tag">AGENCY EXPANSION BLUEPRINT</div>
    <h2 class="page-title">Turnkey Real Estate AI Setter Infrastructure</h2>
    <p class="lead-text">
      Aeroflow Automations provides cutting-edge AI solutions to top-producing real estate brokerages across the United States. To scale your client onboarding without bottlenecks, our engineering team at <strong>Axiom Global</strong> delivers a standardized, modular, and white-label AI Sales Assistant &amp; Appointment Setter framework designed to deploy seamlessly for each real estate client.
    </p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 7px;">
      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Omnichannel Sub-30s Lead Ingestion</div>
        <p style="font-size: 7.8pt; color: var(--dark-charcoal); line-height: 1.4;">
          The system monitors incoming inquiries across <strong>Instagram DM, Website Chatbot, SMS (Twilio), and Email</strong>. Within 30 seconds of an inbound lead, the AI initiates natural, multi-turn dialogues to eliminate lead drop-off and establish immediate rapport.
        </p>
      </div>
      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Autonomous Calendar Booking</div>
        <p style="font-size: 7.8pt; color: var(--dark-charcoal); line-height: 1.4;">
          Once the AI qualifies buyer budget, location, and purchase timeline, it dynamically queries the agent's <strong>Google Calendar or Calendly</strong>, presents available showing slots, confirms the appointment, and triggers SMS reminders to eliminate no-shows.
        </p>
      </div>
    </div>

    <div class="block-title">Client Deliverables Matrix (Per Onboarded Real Estate Client)</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th style="width: 25%;">System Domain</th>
          <th style="width: 45%;">Functional Capability &amp; Integration</th>
          <th style="width: 30%;">Turnaround &amp; Ownership</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Make.com Hub</strong></td>
          <td>Master webhook router, state manager, CRM payload transformer, and error recovery engine.</td>
          <td>Built in Aeroflow Accounts (100% IP)</td>
        </tr>
        <tr>
          <td><strong>Voiceflow Agent</strong></td>
          <td>Conversational dialogue tree, contextual entity extraction, and multi-turn objection handling.</td>
          <td>Fully Documented &amp; Exportable</td>
        </tr>
        <tr>
          <td><strong>OpenAI GPT-4o Engine</strong></td>
          <td>Dynamic knowledge base (RAG), function calling for calendar checking, and natural human responses.</td>
          <td>Zero Robotic 3-Message Scripts</td>
        </tr>
        <tr>
          <td><strong>Vapi / Retell Voice</strong></td>
          <td>Inbound/outbound telephony qualification bot with under 600ms latency and speech-to-speech AI.</td>
          <td>Optional Voice Module Ready</td>
        </tr>
        <tr>
          <td><strong>Calendar &amp; CRM Sync</strong></td>
          <td>Two-way Google Calendar / Calendly synchronization + Follow Up Boss / Lofty / GHL injection.</td>
          <td>Tested End-to-End per Client</td>
        </tr>
      </tbody>
    </table>

    <div class="editorial-card-black" style="margin-top: 4px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
        <span style="font-size: 7.6pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">White-Label Partnership Guarantee</span>
        <span class="badge badge-outline" style="border-color: #fff; color: #fff;">BEHIND THE SCENES</span>
      </div>
      <p style="font-size: 7.6pt; line-height: 1.38; margin: 0;">
        We act as your silent technical engine room. <strong>All work is executed inside accounts owned and controlled by Aeroflow Automations</strong>, with 100% intellectual property transfer upon milestone release, zero direct end-client contact, and strict NDA compliance.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 02 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 03: ANSWERS TO QUESTIONS 1, 2 & 3 ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 02 &middot; CLIENT REVIEW QUESTIONS &middot; PROOF &amp; TERMS</div>
    <div class="header-right">APPLICATION REQUIREMENTS</div>
  </div>

  <div>
    <div class="section-tag">MANDATORY APPLICATION RESPONSES</div>
    <h2 class="page-title">Answers to Client Review Questions 1, 2 &amp; 3</h2>

    <!-- Question 1: Live Demo Link -->
    <div class="editorial-card" style="border-left: 3px solid var(--black); margin-bottom: 6px;">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">
        QUESTION 1: LIVE DEMO LINK OF REAL ESTATE AI BOT TO TEST RIGHT NOW
      </div>
      <p style="font-size: 7.8pt; color: var(--dark-charcoal); line-height: 1.4; margin: 3px 0;">
        We have published a live, interactive Real Estate AI Sales Assistant &amp; Appointment Setter prototype for Aeroflow Automations to test immediately:
      </p>
      <div style="background: #FAFAFC; border: 1.5px solid var(--black); border-radius: 4px; padding: 6px 10px; margin: 4px 0;">
        <div style="font-size: 6.8pt; font-weight: 800; text-transform: uppercase; color: var(--mid-grey);">Interactive Prototype Testing Link:</div>
        <div style="font-size: 9pt; font-weight: 700; color: var(--black); font-family: 'JetBrains Mono', monospace; margin: 2px 0;">
          <a href="https://viranga-lakshan.github.io/portfolio/real-estate-ai-demo/" style="color:var(--black); text-decoration:underline;">https://viranga-lakshan.github.io/portfolio/real-estate-ai-demo/</a>
        </div>
        <p style="font-size: 6.8pt; color: var(--mid-grey); line-height: 1.34; margin: 0;">
          <strong>What You Can Test:</strong> Multi-turn buyer qualification (budget, beds/baths, timeline, pre-approval), natural objection handling, dynamic Google Calendar / Calendly appointment booking modal, and simulated Vapi voice call.
        </p>
      </div>
    </div>

    <!-- Question 2: Terms Confirmation -->
    <div class="editorial-card" style="border-left: 3px solid var(--black); margin-bottom: 6px;">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">
        QUESTION 2: CONFIRMATION OF WHITE-LABEL, CLIENT ACCOUNT OWNERSHIP &amp; IP TERMS
      </div>
      <div style="font-size: 9.5pt; font-weight: 800; color: var(--black); margin: 2px 0;">
        CONFIRMED &mdash; We 100% accept all security, white-label, and IP ownership terms without exception.
      </div>
      <ul style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.38; margin-left: 14px;">
        <li><strong>100% IP Transfer:</strong> All Make.com scenarios, Voiceflow blueprints, system prompts, function calls, and code become the sole, exclusive property of Aeroflow Automations upon milestone payment.</li>
        <li><strong>Client Account Ownership:</strong> Every automation is built directly inside accounts owned and controlled by Aeroflow Automations. We never build on personal accounts or hold client access hostage.</li>
        <li><strong>Strict NDA &amp; White-Label:</strong> We remain completely invisible behind the scenes. Zero direct communication or solicitation with your end real estate clients.</li>
      </ul>
    </div>

    <!-- Question 3: Turnaround Time -->
    <div class="editorial-card" style="border-left: 3px solid var(--black);">
      <div style="font-size: 7pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--mid-grey);">
        QUESTION 3: ESTIMATED TURNAROUND TIME PER CLIENT SETUP
      </div>
      <p style="font-size: 7.8pt; color: var(--dark-charcoal); line-height: 1.4; margin: 3px 0;">
        Our turnaround time to deliver a complete, fully tested client setup is <strong>3 to 5 business days</strong>:
      </p>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin-top: 3px;">
        <div class="editorial-card-grey" style="margin: 0;">
          <strong style="font-size: 7.2pt; color: var(--black); display: block;">Days 1–2: Ingestion &amp; Prompt Configuration</strong>
          <span style="font-size: 6.8pt; color: var(--mid-grey); line-height: 1.32;">
            Import client brokerage branding, property inventory, MLS rules, neighborhood FAQs, and connect social/SMS webhooks in Make.com.
          </span>
        </div>
        <div class="editorial-card-grey" style="margin: 0;">
          <strong style="font-size: 7.2pt; color: var(--black); display: block;">Days 3–5: Calendar, CRM Sync &amp; Testing</strong>
          <span style="font-size: 6.8pt; color: var(--mid-grey); line-height: 1.32;">
            Wire Google Calendar/Calendly, test CRM ingestion (Follow Up Boss/Lofty), run live multi-channel stress tests, and deliver verified setup.
          </span>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 03 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 04: OMNICHANNEL CONVERSATION ENGINE ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 03 &middot; OMNICHANNEL CONVERSATION ENGINE</div>
    <div class="header-right">MAKE.COM + VOICEFLOW + OPENAI</div>
  </div>

  <div>
    <div class="section-tag">CONVERSATIONAL ARCHITECTURE</div>
    <h2 class="page-title">Natural, Human-Like Multi-Turn Dialogue</h2>
    <p class="lead-text">
      Basic 3-message chatbots repel serious real estate buyers. Our architecture couples <strong>Make.com</strong> for multi-channel webhook routing with <strong>Voiceflow</strong> and <strong>OpenAI GPT-4o Function Calling</strong> to sustain human-like, contextual conversations that adapt to unpredictable buyer behavior.
    </p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card">
        <div class="block-title">1. Make.com Unified Webhook Router</div>
        <p style="font-size: 7.6pt; color: var(--dark-charcoal); line-height: 1.38; margin-bottom: 3px;">
          Ingests incoming leads from Instagram Direct Messages (via Meta Graph API), Website Chat widgets, SMS (Twilio / ManyChat), and Email (IMAP/Gmail). Normalizes incoming payloads into a single standard message event and dispatches to the Voiceflow conversation runtime.
        </p>
        <div class="code-box">
POST /webhooks/incoming_lead
Headers: X-Channel: "instagram" | "sms" | "webchat"
Payload: {{ lead_id, channel_id, message_text, timestamp, sender_profile }}</div>
      </div>

      <div class="editorial-card">
        <div class="block-title">2. OpenAI Function Calling &amp; RAG</div>
        <p style="font-size: 7.6pt; color: var(--dark-charcoal); line-height: 1.38; margin-bottom: 3px;">
          Empowers the agent to dynamically execute internal tools rather than hallucinating. When a buyer asks about active listings or open dates, the model calls structured tools: <code>check_calendar_availability()</code> or <code>search_brokerage_properties()</code>.
        </p>
        <div class="code-box">
tools: [
  {{ name: "check_calendar_slots", params: {{ date, timezone }} }},
  {{ name: "book_property_showing", params: {{ lead_name, time, property_id }} }}
]</div>
      </div>
    </div>

    <div class="block-title">Omnichannel Real Estate AI Processing Pipeline</div>
    <div class="code-box" style="font-size: 6.6pt; line-height: 1.38;">
[Incoming Inquiries: Instagram DM &middot; Webchat &middot; SMS &middot; Email]
       │  (Triggered in &lt; 30 seconds)
       ▼
[Make.com Master Orchestrator] ───► [Contact Deduplication &amp; History Lookup]
       │
       ▼
[Voiceflow Conversational State Machine]
       │  (Extracts Entities: Budget, Beds/Baths, Preferred Zip Code, Timeline)
       ▼
[OpenAI GPT-4o / GPT-4o-mini + Vector RAG]
  ├─► Answers Brokerage FAQs (HOA fees, school districts, financing options)
  └─► Overcomes Buyer Objections ("Just looking", "Interest rates are high")
       │
       ▼
[Function Call: Check Google Calendar / Calendly Slots]
       │
       ▼
[Slot Accepted ──► Instant Confirmation SMS + Calendar Invite + CRM Lead Sync]</div>

    <div class="editorial-card-grey" style="border-left: 3px solid var(--black); margin-top: 4px;">
      <div class="block-title">Preventing 'Bot Fatigue' &amp; Robotic Loops</div>
      <p style="font-size: 7.6pt; color: var(--dark-charcoal); line-height: 1.38; margin: 0;">
        Our prompt architecture incorporates contextual memory across 15+ conversational turns. If a user interrupts the qualification flow to ask, <em>"What school district is that 4-bedroom house in?"</em>, the AI answers knowledgeably first before gracefully circling back to schedule a viewing.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 04 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 05: LEAD QUALIFICATION STATE MACHINE ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 04 &middot; REAL ESTATE LEAD QUALIFICATION ENGINE</div>
    <div class="header-right">BUYER DISCOVERY MATRIX</div>
  </div>

  <div>
    <div class="section-tag">QUALIFICATION FRAMEWORK</div>
    <h2 class="page-title">4-Pillar Real Estate Lead Qualification</h2>
    <p class="lead-text">
      The AI Assistant does not merely chat; it methodically extracts the four critical data points required by US real estate agents to distinguish tire-kickers from serious, transaction-ready buyers.
    </p>

    <div class="block-title">The 4-Pillar Lead Qualification Matrix</div>
    <table class="editorial-table" style="margin-bottom: 7px;">
      <thead>
        <tr>
          <th>Pillar</th>
          <th>Data Extracted</th>
          <th>AI Conversational Strategy</th>
          <th>Lead Classification</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Buyer Budget</strong></td>
          <td>Target purchase price range &amp; cash vs. loan</td>
          <td>"What general price window are you keeping in mind for the new home?"</td>
          <td>Under $400k &middot; $400k–$800k &middot; $800k–$1.5M &middot; Luxury $1.5M+</td>
        </tr>
        <tr>
          <td><strong>2. Property Criteria</strong></td>
          <td>Beds, baths, square footage, neighborhood, yard</td>
          <td>"Are you prioritizing specific neighborhoods, school zones, or yard sizes?"</td>
          <td>Single Family &middot; Condo &middot; Townhouse &middot; Multi-Family</td>
        </tr>
        <tr>
          <td><strong>3. Purchase Timeline</strong></td>
          <td>Move-in urgency &amp; lease expiration</td>
          <td>"How quickly would you like to have keys in hand if we found the ideal spot?"</td>
          <td><strong>Immediate (Hot)</strong> &middot; 30–60 Days &middot; 90+ Days (Nurture)</td>
        </tr>
        <tr>
          <td><strong>4. Pre-Approval</strong></td>
          <td>Lender status &amp; proof of funds</td>
          <td>"Have you already spoken with a local lender, or would an intro be helpful?"</td>
          <td>Pre-Approved Verified &middot; Cash Buyer &middot; Needs Lender Intro</td>
        </tr>
      </tbody>
    </table>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Handling Common Buyer Objections</div>
        <p style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36; margin-bottom: 2px;">
          <strong>Objection: "I'm just browsing online."</strong><br>
          <em>AI Response:</em> "No problem at all! Exploring the market is the smartest way to start. We actually have access to 3 off-market listings in that area before they hit Zillow. Would you like me to send those over?"
        </p>
      </div>

      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Instant Hot Lead Escalation Alerts</div>
        <p style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36; margin-bottom: 2px;">
          When a buyer indicates a budget &gt;$750k and a timeline &lt;30 days, Make.com immediately sends a priority push notification / SMS directly to the real estate agent's mobile phone: <em>"🚨 HOT BUYER: Pre-approved for $950k booking Saturday showing."</em>
        </p>
      </div>
    </div>

    <!-- Image insert -->
    <div style="position: relative; width: 100%; height: 50mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-grey); margin-top: 2px;">
      <img src="{LUXURY_HERO}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Luxury Real Estate Lead Qualification">
      <div style="position: absolute; bottom: 8px; left: 10px; background: rgba(15, 17, 21, 0.85); color: #fff; padding: 4px 8px; border-radius: 2px; font-size: 6.6pt;">
        <strong>PRECISION QUALIFICATION</strong> &middot; Automated Buyer Scoring &amp; Real-Time Agent Handoff Protocols
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 05 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 06: CALENDAR BOOKING & NO-SHOW REDUCTION ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 05 &middot; CALENDAR SYNC &amp; NO-SHOW REDUCTION</div>
    <div class="header-right">GOOGLE CALENDAR &amp; CALENDLY</div>
  </div>

  <div>
    <div class="section-tag">SCHEDULING AUTOMATION</div>
    <h2 class="page-title">Bi-Directional Calendar Booking Engine</h2>
    <p class="lead-text">
      The ultimate objective of the AI Sales Assistant is getting qualified buyers on the agent's calendar. The system integrates directly with <strong>Google Calendar API</strong> and <strong>Calendly API</strong> to propose conflict-free showing slots in real time.
    </p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 7px;">
      <div class="editorial-card">
        <div class="block-title">Smart Slot Matching &amp; Conflict Prevention</div>
        <ul style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.38; margin-left: 12px;">
          <li><strong>Real-Time Free/Busy Check:</strong> Queries agent's live Google Calendar, respecting personal blocks and existing showings.</li>
          <li><strong>Buffer Rules &amp; Drive Time:</strong> Automatically enforces 30-minute travel buffers between consecutive in-person property tours.</li>
          <li><strong>Timezone Normalization:</strong> Accurately handles out-of-state buyers relocating to the agent's local market.</li>
          <li><strong>Conversational Slot Proposal:</strong> Proposes 2 distinct options: <em>"Our specialist has Thursday at 2:00 PM or Saturday at 10:30 AM available. Which fits your schedule?"</em></li>
        </ul>
      </div>

      <div class="editorial-card">
        <div class="block-title">Automated No-Show Reduction Cadence</div>
        <ul style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.38; margin-left: 12px;">
          <li><strong>Instant Confirmation:</strong> Dispatches calendar invite with Google Meet / property address + instant SMS confirmation.</li>
          <li><strong>24-Hour Reminder:</strong> SMS reminder asking for a simple reply: <em>"Looking forward to meeting you tomorrow! Reply 'YES' to confirm."</em></li>
          <li><strong>2-Hour Reminder:</strong> Sends direct directions link and agent contact card.</li>
          <li><strong>Rescheduling Workflow:</strong> If buyer replies 'RESCHEDULE', the AI immediately offers alternative slots without agent effort.</li>
        </ul>
      </div>
    </div>

    <div class="block-title">Appointment Lifecycle &amp; Reminder Architecture</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th>Cadence Trigger</th>
          <th>Channel</th>
          <th>Automated Message Content</th>
          <th>System Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Instant (T-0)</strong></td>
          <td>Email &amp; SMS</td>
          <td>Calendar invitation with property address, agent profile &amp; Google Meet link.</td>
          <td>Logs appointment in CRM; tags lead as "Showing Scheduled".</td>
        </tr>
        <tr>
          <td><strong>T - 24 Hours</strong></td>
          <td>SMS Text</td>
          <td>"Hi [Name], Sarah from Austin Realty. Just confirming our tour tomorrow at 2PM. Reply YES to confirm!"</td>
          <td>Monitors reply; updates status in CRM.</td>
        </tr>
        <tr>
          <td><strong>T - 2 Hours</strong></td>
          <td>SMS Text</td>
          <td>"See you soon! Address: 3804 Westlake Ridge Dr. Agent Mike's cell: (512) 555-0192."</td>
          <td>Sends GPS pin &amp; parking instructions.</td>
        </tr>
      </tbody>
    </table>

    <div class="editorial-card-black" style="margin-top: 3px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
        <span style="font-size: 7.6pt; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">Measurable Business Impact for Real Estate Clients</span>
        <span class="badge badge-outline" style="border-color: #fff; color: #fff;">PROVEN ROI</span>
      </div>
      <p style="font-size: 7.6pt; line-height: 1.36; margin: 0; color: #D1D5DB;">
        By responding in under 30 seconds and running a structured 3-stage SMS confirmation sequence, this automation increases lead-to-appointment conversion by <strong>3x</strong> and reduces buyer no-show rates by over <strong>40%</strong>.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 06 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 07: INBOUND & OUTBOUND AI VOICE ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 06 &middot; INBOUND &amp; OUTBOUND AI VOICE CALLER</div>
    <div class="header-right">VAPI / RETELL INTEGRATION</div>
  </div>

  <div>
    <div class="section-tag">VOICE TELEPHONY ARCHITECTURE</div>
    <h2 class="page-title">Ultra-Low Latency Conversational Voice (Vapi / Retell)</h2>
    <p class="lead-text">
      For clients requesting phone automation, we deploy conversational voice agents using <strong>Vapi.ai</strong> or <strong>Retell AI</strong> connected via Twilio SIP trunking. The voice agent answers inbound calls within 2 rings and conducts natural phone conversations with sub-600ms latency.
    </p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card">
        <div class="block-title">Inbound Yard Sign &amp; Zillow Call Handling</div>
        <p style="font-size: 7.5pt; color: var(--dark-charcoal); line-height: 1.36; margin-bottom: 3px;">
          When an interested buyer calls the brokerage phone number listed on a yard sign or Zillow ad, the AI agent answers instantly: <em>"Thanks for calling Austin Premier Realty! Are you inquiring about the listing on Westlake Ridge Dr?"</em> It qualifies the caller and offers to book a private tour live on the call.
        </p>
      </div>

      <div class="editorial-card">
        <div class="block-title">Outbound Speed-to-Lead Follow Up</div>
        <p style="font-size: 7.5pt; color: var(--dark-charcoal); line-height: 1.36; margin-bottom: 3px;">
          When a new lead submits a Facebook or Google Ad lead form, Make.com triggers an automated outbound call within 60 seconds. If the lead answers, the voice AI greets them by name, qualifies their timeline, and connects them directly with the on-duty agent or books a showing.
        </p>
      </div>
    </div>

    <div class="block-title">Vapi / Retell Voice Telephony Technical Stack</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th>Component</th>
          <th>Technology Provider</th>
          <th>Technical Performance Benchmark</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Voice Orchestration</strong></td>
          <td>Vapi.ai / Retell AI</td>
          <td>Sub-600ms conversational turn-taking latency with interruption handling.</td>
        </tr>
        <tr>
          <td><strong>Telephony &amp; Numbers</strong></td>
          <td>Twilio SIP Trunking</td>
          <td>Local US area code phone numbers matching the client brokerage's city.</td>
        </tr>
        <tr>
          <td><strong>Speech-to-Text (STT)</strong></td>
          <td>Deepgram Nova-2</td>
          <td>Real-time streaming transcription with medical and real estate vocabulary.</td>
        </tr>
        <tr>
          <td><strong>Text-to-Speech (TTS)</strong></td>
          <td>ElevenLabs / Cartesia</td>
          <td>Hyper-realistic, human-sounding American voices with natural breathing cadence.</td>
        </tr>
        <tr>
          <td><strong>Function Execution</strong></td>
          <td>Serverless Webhook (Make.com)</td>
          <td>Live calendar query while the caller is on the line to confirm availability.</td>
        </tr>
      </tbody>
    </table>

    <div style="position: relative; width: 100%; height: 50mm; border-radius: 4px; overflow: hidden; border: 1px solid var(--border-grey); margin-top: 2px;">
      <img src="{PROP_MODERN}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Modern Real Estate Showing">
      <div style="position: absolute; bottom: 8px; left: 10px; background: rgba(15, 17, 21, 0.85); color: #fff; padding: 4px 8px; border-radius: 2px; font-size: 6.6pt;">
        <strong>CONVERSATIONAL VOICE</strong> &middot; Automated Inbound Call Handling &amp; Real-Time Phone Calendar Booking
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 07 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 08: CRM SYNCHRONIZATION & LEAD HANDOFF ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 07 &middot; REAL ESTATE CRM SYNCHRONIZATION</div>
    <div class="header-right">FUB &middot; LOFTY &middot; KVCORE &middot; GHL</div>
  </div>

  <div>
    <div class="section-tag">DATA INTEGRATION</div>
    <h2 class="page-title">Client CRM Synchronization &amp; Lead Handoff</h2>
    <p class="lead-text">
      To ensure zero disruption to your real estate clients' daily operations, every conversation, extracted lead detail, and scheduled appointment is automatically synchronized with their existing CRM in real time.
    </p>

    <div class="block-title">Supported Real Estate CRM Integrations</div>
    <table class="editorial-table" style="margin-bottom: 7px;">
      <thead>
        <tr>
          <th>CRM Platform</th>
          <th>Integration Method</th>
          <th>Synchronized Data Fields</th>
          <th>Automated Agent Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Follow Up Boss (FUB)</strong></td>
          <td>Direct REST API &middot; Events API</td>
          <td>Full name, phone, email, budget, timeline, notes &amp; stage.</td>
          <td>Creates Contact; adds "AI-Qualified" tag; sets appointment task.</td>
        </tr>
        <tr>
          <td><strong>Lofty (Chime)</strong></td>
          <td>Webhook &middot; REST API</td>
          <td>Buyer preferences (beds/baths), location, pre-approval status.</td>
          <td>Assigns lead to designated buyer agent with high-priority flag.</td>
        </tr>
        <tr>
          <td><strong>kvCORE</strong></td>
          <td>Lead Drop API &middot; Zapier/Make</td>
          <td>Contact info, inquiry source, showing date/time, full chat transcript.</td>
          <td>Applies automated smart campaign; triggers agent notification.</td>
        </tr>
        <tr>
          <td><strong>GoHighLevel (GHL)</strong></td>
          <td>Native Make.com app &middot; Webhooks</td>
          <td>Custom fields, opportunity pipeline stage, appointment calendar.</td>
          <td>Moves lead card across pipeline into "Showing Booked" column.</td>
        </tr>
        <tr>
          <td><strong>Google Sheets / Airtable</strong></td>
          <td>Direct Table Append</td>
          <td>Universal audit log of all leads, timestamps, and conversation metrics.</td>
          <td>Maintains live client reporting sheet for Aeroflow Automations.</td>
        </tr>
      </tbody>
    </table>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Full Conversation Transcripts in CRM Notes</div>
        <p style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36;">
          Agents never walk into a property showing blind. The automation appends an executive summary to the lead profile: <em>"Qualified by Sarah AI: Budget $1.1M, Pre-Approved with Chase, Moving by Dec 30, Wants Eanes School District. Chat transcript attached below."</em>
        </p>
      </div>

      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Lead De-duplication &amp; Historical Memory</div>
        <p style="font-size: 7.4pt; color: var(--dark-charcoal); line-height: 1.36;">
          If an existing contact messages on Instagram after submitting an SMS form 2 days earlier, Make.com checks phone/email records, attaches the new interaction to the existing CRM profile, and prevents duplicate lead generation.
        </p>
      </div>
    </div>

    <div class="editorial-card-grey" style="border-left: 3px solid var(--black); margin-top: 3px;">
      <div class="block-title">Reliability &amp; Error Recovery Protocol</div>
      <p style="font-size: 7.6pt; color: var(--dark-charcoal); line-height: 1.38; margin: 0;">
        All Make.com scenarios include automated error handlers with rollback routes. If a client's CRM API experiences temporary downtime, the lead payload is safely preserved in an Airtable queue and retried with exponential backoff, ensuring zero lost leads.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 08 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 09: ENGINEERING SQUAD & CREDENTIALS ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 08 &middot; DEDICATED ENGINEERING SQUAD &amp; CREDENTIALS</div>
    <div class="header-right">TECHNICAL ARCHITECTURE LEADERSHIP</div>
  </div>

  <div>
    <div class="section-tag">ENGINEERING SQUAD</div>
    <h2 class="page-title">Technical Team Composition &amp; Enterprise References</h2>
    <p class="lead-text">
      Axiom Global operates as a high-velocity software engineering squad based in Sri Lanka, developing and maintaining enterprise digital solutions for international clients across the US, UK, Australia, and the UAE.
    </p>

    <!-- Lead Engineer Box -->
    <div class="editorial-card-black" style="margin-bottom: 6px; padding: 8px 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
        <h3 class="serif-heading" style="font-size: 10pt; color: var(--white); margin: 0;">Avishka Meddegoda &middot; Technical Lead &amp; Systems Architect</h3>
        <span class="badge badge-outline" style="border-color: #fff; color: #fff;">PRIMARY ASSIGNED LEAD</span>
      </div>
      <p style="font-size: 7.5pt; line-height: 1.38; color: #E5E7EB; margin: 0;">
        <strong>6+ Years Experience:</strong> Senior Full-Stack &amp; Enterprise Systems Architect. Specialist in Make.com enterprise workflows, Voiceflow conversational state design, OpenAI API function calling, Twilio telephony, and backend microservices. Avishka will personally architect the modular client build templates and oversee technical QA.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 5px;">
      <div class="editorial-card">
        <div class="block-title">Viranga Lakshan &middot; Solutions Architect &amp; Delivery Lead</div>
        <div style="font-size: 6.4pt; color: var(--mid-grey); font-weight: 700; margin-bottom: 2px;">2+ Years Experience &middot; Lead Solutions Architect</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.34; margin: 0;">
          Coordinates client onboarding velocity, Make.com scenario documentation, and white-label QA checklists. Manages all partner communication and sprint milestones.
        </p>
      </div>

      <div class="editorial-card">
        <div class="block-title">Chamara Lahiru &middot; Senior Frontend Engineer</div>
        <div style="font-size: 6.4pt; color: var(--mid-grey); font-weight: 700; margin-bottom: 2px;">6+ Years Experience &middot; UI/UX &amp; Chatbot Interfaces</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.34; margin: 0;">
          Specialist in custom embeddable website chat widgets, branded client UI assets, responsive mobile views, and CSS animation styling.
        </p>
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card">
        <div class="block-title">Janith Kavishka &middot; Full-Stack &amp; API Integration Engineer</div>
        <div style="font-size: 6.4pt; color: var(--mid-grey); font-weight: 700; margin-bottom: 2px;">2+ Years Experience &middot; Webhook Specialist</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.34; margin: 0;">
          Focuses on CRM API endpoints (Follow Up Boss, Lofty, kvCORE), Twilio SMS provisioning, and calendar bi-directional synchronization.
        </p>
      </div>

      <div class="editorial-card">
        <div class="block-title">Lithumitha Ravikumar &middot; Project Manager &amp; QA Lead</div>
        <div style="font-size: 6.4pt; color: var(--mid-grey); font-weight: 700; margin-bottom: 2px;">2 Years Experience &middot; Agile Delivery &amp; QA</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.34; margin: 0;">
          Maintains client deployment schedules, verifies multi-channel response triggers, and ensures 100% white-label protocol compliance.
        </p>
      </div>
    </div>

    <div class="block-title">Proven International Enterprise References</div>
    <table class="editorial-table">
      <thead>
        <tr>
          <th>Platform / Project</th>
          <th>Domain &amp; Client</th>
          <th>Architecture &amp; Features</th>
          <th>Live Verification</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Al Ain Museum V2</strong></td>
          <td>Government Digital Experience &middot; UAE</td>
          <td>Next.js, TypeScript, Headless CMS, Enterprise APIs</td>
          <td><a href="https://alainmuseum.ae" style="color:var(--black); text-decoration:underline;">alainmuseum.ae</a></td>
        </tr>
        <tr>
          <td><strong>Moolee Multi-Tenant Platform</strong></td>
          <td>Enterprise E-Commerce &amp; Logistics</td>
          <td>Node.js, Microservices, Order Routing, Payments</td>
          <td><a href="https://moolee.mv" style="color:var(--black); text-decoration:underline;">moolee.mv</a></td>
        </tr>
        <tr>
          <td><strong>Holsten Arabia</strong></td>
          <td>Enterprise Web Experience &middot; Middle East</td>
          <td>Next.js, Umbraco Headless, .NET Core APIs</td>
          <td><a href="https://holstenarabia.me" style="color:var(--black); text-decoration:underline;">holstenarabia.me</a></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
    <div class="footer-page-num">Page 09 of 10</div>
  </div>
</div>

<!-- ========================================== PAGE 10: COMMERCIAL AGREEMENT & TERMS ========================================== -->
<div class="page">
  <div class="page-header">
    <div class="header-left">SECTION 09 &middot; COMMERCIAL AGREEMENT &amp; PARTNERSHIP ROADMAP</div>
    <div class="header-right">$1,000 BUILD + $100/MO RETAINER</div>
  </div>

  <div>
    <div class="section-tag">COMMERCIAL STRUCTURE</div>
    <h2 class="page-title">Compensation, Milestones &amp; Partnership Roadmap</h2>
    <p class="lead-text">
      Our proposed structure perfectly matches Aeroflow Automations' stated compensation model: <strong>$1,000 USD Fixed Price per complete client build</strong> via Upwork milestones, plus <strong>$100 USD/month recurring</strong> per active client for ongoing monitoring and updates.
    </p>

    <div class="block-title">Milestone Structure per Client Build ($1,000 USD Fixed Price)</div>
    <table class="editorial-table" style="margin-bottom: 6px;">
      <thead>
        <tr>
          <th>Milestone Stage</th>
          <th>Deliverable &amp; Scope Summary</th>
          <th>Verification Criteria</th>
          <th>Timeline</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Milestone 1</strong><br>Channel &amp; Voiceflow Setup</td>
          <td>
            Connect Instagram DM, Website Chat widget, SMS &amp; Email webhooks in client Make.com account. Build Voiceflow conversation tree with brokerage FAQs.
          </td>
          <td>Omnichannel ingestion active; AI replies in &lt;30s across all connected channels.</td>
          <td>Days 1–2</td>
          <td><strong>$400.00</strong><br><span style="font-size:6pt; color:var(--mid-grey);">(40%)</span></td>
        </tr>
        <tr>
          <td><strong>Milestone 2</strong><br>Qualification &amp; Calendar</td>
          <td>
            Deploy 4-pillar qualification logic (budget, timeline, location, pre-approval). Connect Google Calendar / Calendly with automatic slot detection.
          </td>
          <td>End-to-end qualification and live appointment booking test verified.</td>
          <td>Days 3–4</td>
          <td><strong>$400.00</strong><br><span style="font-size:6pt; color:var(--mid-grey);">(40%)</span></td>
        </tr>
        <tr>
          <td><strong>Milestone 3</strong><br>CRM Sync &amp; Handover</td>
          <td>
            Wire client CRM (Follow Up Boss / Lofty / GHL). Test 3-stage reminder cadence. Transfer 100% IP and deliver handover documentation.
          </td>
          <td>Verified CRM lead injection; full setup running inside client account.</td>
          <td>Day 5</td>
          <td><strong>$200.00</strong><br><span style="font-size:6pt; color:var(--mid-grey);">(20%)</span></td>
        </tr>
        <tr style="background: #F1F5F9; font-weight: 700;">
          <td colspan="4" style="text-align: right; text-transform: uppercase;">Total Build Fee per Client:</td>
          <td style="color: var(--black); font-size: 9pt;">$1,000.00 USD</td>
        </tr>
      </tbody>
    </table>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px;">
      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">$100/Month Recurring Retainer per Active Client</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.36; margin: 0;">
          Covers weekly Make.com error log audits, OpenAI prompt optimizations based on new brokerage listings, Voiceflow model tuning, and proactive uptime monitoring to ensure zero missed buyer inquiries.
        </p>
      </div>

      <div class="editorial-card" style="border-left: 3px solid var(--black);">
        <div class="block-title">Agency Scale &amp; Throughput Capacity</div>
        <p style="font-size: 7.2pt; color: var(--dark-charcoal); line-height: 1.36; margin: 0;">
          With our dedicated 5-member squad and standardized Make.com blueprints, our team can comfortably onboard <strong>5 to 10 new real estate brokerages per month</strong> for Aeroflow Automations without compromising delivery speed.
        </p>
      </div>
    </div>

    <div class="editorial-card-black" style="padding: 8px 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
        <div>
          <span style="font-size: 6.4pt; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; color: #D1D5DB;">Immediate Partnership Readiness</span>
          <h3 class="serif-heading" style="font-size: 10pt; color: #fff; margin: 0;">Ready to Deliver Client #1 Within 3–5 Days</h3>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 6.4pt; color: #9CA3AF;">Lead Solutions Architect</span>
          <div style="font-size: 8.2pt; font-weight: 700; color: #fff;">Viranga Lakshan</div>
        </div>
      </div>
      <p style="font-size: 7.4pt; line-height: 1.36; color: #D1D5DB; margin: 0;">
        We are prepared to sign your mutual NDA, establish access to your Aeroflow agency accounts, and immediately build your next real estate client setup. Let's connect on Upwork to finalize kickoff!
      </p>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-left">AXIOM GLOBAL &middot; AEROFLOW AUTOMATIONS PARTNERSHIP &middot; AXIOMGLOBAL.TECH</div>
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
    assert total_pages == 10, f"Expected 10 pages, got {total_pages}"
    print("PAGE COUNT VERIFICATION PASSED: Exactly 10 pages.")

if __name__ == "__main__":
    generate_pdf()

