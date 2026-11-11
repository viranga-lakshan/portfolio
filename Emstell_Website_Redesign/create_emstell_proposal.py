import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Complete Redesign & Rebuild of Corporate Website - Emstell Technologies</title>
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
    border-bottom: 2px solid #0066ff;
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
    background: #0066ff;
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
    background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #0066ff 100%);
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
    border-left: 3.5px solid #0066ff;
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

  /* Team member card */
  .member-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #0066ff;
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
    color: #0066ff;
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
    color: #0066ff;
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
          Emstell Technologies <span class="brand-badge">Corporate Web Rebuild</span>
        </div>
        <div class="brand-sub">Streamlined 3-Pillar Architecture • Web Engineering • Mobile Apps • AI Solutions</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> Emstell Technology Consulting (Kuwait & Saudi Arabia)<br>
        <strong>Current Domain:</strong> www.emstell.com<br>
        <strong>Design Vision:</strong> De-Cluttered, Eye-Catching Tech Luxury<br>
        <strong>Engagement:</strong> Fixed-Price Milestone Redesign
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">From Clutter to Conversion: A High-Impact Facelift for Emstell.com</div>
      <div class="hero-desc">
        A complete architectural facelift and rebuild for Emstell.com. Stripping away legacy clutter and fragmented pages to focus exclusively on your three true revenue drivers: Web Engineering, Mobile App Development, and AI Solutions. Engineered with eye-catching modern tech visuals, frictionless multi-step inquiry capture, and an intuitive CMS backend for effortless team management.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Focus 1: <strong>Custom Web & Cloud Platforms</strong></div>
        <div class="hero-pill">Focus 2: <strong>iOS & Android Mobile Apps</strong></div>
        <div class="hero-pill">Focus 3: <strong>Enterprise AI & Automation</strong></div>
        <div class="hero-pill">Lead Engine: <strong>Interactive Inquiries & WhatsApp</strong></div>
        <div class="hero-pill">Backend: <strong>Smooth, Code-Free Content CMS</strong></div>
      </div>
    </div>

    <!-- Executive Summary & De-Cluttering Strategy -->
    <div class="section">
      <div class="section-title">
        1. Executive Vision & De-Cluttering Strategy
        <span class="tagline">"Less is More" — Elevating Emstell's Enterprise Credibility</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Current Challenge on Emstell.com</span>
            <span class="card-badge">Analysis</span>
          </div>
          <p class="card-p">
            Like many established technology firms, Emstell’s website has accumulated services, legacy blog posts, and sub-pages over years of operations. For prospective enterprise clients in Kuwait, Saudi Arabia, and the UK:
          </p>
          <ul class="card-bullets">
            <li><strong>Decision Fatigue:</strong> Too many generic menu items dilute Emstell's core mastery in Mobile, Web, and AI.</li>
            <li><strong>Outdated Visual Aesthetic:</strong> Dense text blocks and stock imagery fail to convey the cutting-edge technical sophistication of your engineering team.</li>
            <li><strong>High-Friction Inquiries:</strong> Static, uninspired contact forms result in high bounce rates and lost inbound enterprise leads.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Our Modernized Rebuild Blueprint</span>
            <span class="card-badge">Transformation</span>
          </div>
          <p class="card-p">
            We transform Emstell.com into a sleek, focused corporate flagship that commands instant authority:
          </p>
          <ul class="card-bullets">
            <li><strong>Radical Focus (The 3 Pillars):</strong> 100% of the site’s narrative orbits around Web Engineering, Mobile Apps, and AI Solutions.</li>
            <li><strong>Sleek Modern Visuals:</strong> Dark obsidian tones, electric blue accents, glassmorphic cards, and subtle interactive tech animations.</li>
            <li><strong>Interactive Lead Capture:</strong> A 2-step dynamic project estimator that qualifies leads by budget, platform, and timeline while offering direct WhatsApp chat.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Before vs. After Matrix -->
    <div class="section">
      <div class="section-title">
        2. Website Architecture: Before vs. After
        <span class="tagline">Consolidating 30+ Scattered URLs into 5 High-Impact Core Pages</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 25%;">Area</th>
            <th style="width: 37%;">Current Emstell.com State</th>
            <th style="width: 38%;">Proposed Modernized Rebuild</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Core Page Structure</strong></td>
            <td>Scattered sub-pages, nested service menus, redundant informational pages.</td>
            <td><strong>5 Core Pages:</strong> Home, Web Engineering, Mobile Apps, AI Solutions, Case Studies & Inquiries.</td>
          </tr>
          <tr>
            <td><strong>Visual Design & UI</strong></td>
            <td>Traditional template layout, standard stock photos, heavy text paragraphs.</td>
            <td><strong>Cyber-Minimalist Tech Luxury:</strong> Glassmorphic cards, micro-interactions, dark mode elegance, high-contrast typography.</td>
          </tr>
          <tr>
            <td><strong>Service Positioning</strong></td>
            <td>Broad, generic IT consulting claims lacking punchy modern differentiation.</td>
            <td><strong>Laser-Focused 3 Pillars:</strong> Dedicated deep-dive hubs for Web, iOS/Android Mobile, and Enterprise AI.</td>
          </tr>
          <tr>
            <td><strong>Lead Generation</strong></td>
            <td>Generic name/email/message contact box with slow response feedback.</td>
            <td><strong>Interactive Scope Estimator:</strong> Multi-step budget & tech selector + 1-click WhatsApp instant chat.</td>
          </tr>
          <tr>
            <td><strong>Content Management</strong></td>
            <td>Complex, fragmented dashboard making quick updates cumbersome.</td>
            <td><strong>Smooth Modular CMS:</strong> Clean, visual block editor allowing non-technical staff to edit case studies in minutes.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">Proven GCC & Kuwait Enterprise Track Record</div>
      <div class="callout-text">
        Our team has delivered major digital platforms for Kuwait and UAE clients, including <strong>Adrik News & Media (Kuwait)</strong>, <strong>Al Ain Museum (UAE)</strong>, and <strong>Holsten Arabia</strong>. We understand the aesthetic standards, regional trust signals, and mobile-first preferences of Gulf enterprise decision-makers.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Emstell Technologies • Corporate Website Redesign Proposal</span>
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
        <div class="brand-title">Clear Design Idea & Visual Direction <span class="brand-badge">Design Concept</span></div>
        <div class="brand-sub">Eye-Catching Aesthetics, Color Palette, and Information Architecture</div>
      </div>
      <div class="meta-block">
        <strong>Aesthetic:</strong> Cyber-Minimalist Dark Mode<br>
        <strong>Primary Accent:</strong> Electric Cobalt (#0066FF)<br>
        <strong>Core Pages:</strong> 5 Streamlined Landing Experiences
      </div>
    </div>

    <!-- Clear Design Idea Requirement -->
    <div class="section">
      <div class="section-title">
        3. Clear Design Concept: Eye-Catching Tech Luxury
        <span class="tagline">Delivering on Emstell's Requirement for a Clear Pre-Hire Design Idea</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Color Palette & Visual Dynamics</span>
            <span class="card-badge">Aesthetics</span>
          </div>
          <p class="card-p">
            To catch the eye of enterprise CTOs, founders, and government stakeholders across Kuwait and Saudi Arabia, we implement a commanding visual language:
          </p>
          <ul class="card-bullets">
            <li><strong>Deep Obsidian Canvas (#090D16):</strong> Creates infinite depth, high contrast, and luxury positioning that distinguishes Emstell from generic agency sites.</li>
            <li><strong>Electric Cobalt Blue (#0066FF) & Cyan (#00F5D4):</strong> Vibrant glowing gradients that draw instant focus to CTAs, interactive metrics, and active service cards.</li>
            <li><strong>Glassmorphic Bento Grids:</strong> Modern rounded containers with frosted glass borders (rgba 255, 255, 255, 0.08) showcasing client logos and capabilities.</li>
            <li><strong>Subtle Micro-Interactions:</strong> Smooth hover states, glowing cursor trails, and fluid scroll animations that communicate elite engineering quality.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">The 5 Core Streamlined Pages</span>
            <span class="card-badge">Architecture</span>
          </div>
          <p class="card-p">
            Every page is engineered with a strict commercial purpose:
          </p>
          <ul class="card-bullets">
            <li><strong>01. Homepage (The Flagship):</strong> Hero statement: <em>"Architecting Next-Generation Mobile Apps, Web Platforms & Enterprise AI for the GCC"</em>, live client ticker, 3-pillar interactive cards, and featured case studies.</li>
            <li><strong>02. Web Engineering:</strong> Custom web apps, enterprise SaaS, high-load e-commerce, cloud architecture, and modern tech stacks.</li>
            <li><strong>03. Mobile App Development:</strong> Native iOS/Android, Flutter/React Native, mobile FinTech, and GCC payment gateways (KNET, Apple Pay, Mada).</li>
            <li><strong>04. AI Solutions:</strong> Custom ChatGPT/LLM integrations, computer vision, predictive analytics, and automated enterprise workflows.</li>
            <li><strong>05. Case Studies & Interactive Inquiry:</strong> High-impact portfolio metrics + multi-step project cost estimator.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Homepage Wireframe Wireflow -->
    <div class="section">
      <div class="section-title">
        4. Homepage Blueprint & User Journey Wireflow
        <span class="tagline">Guiding the Visitor from First Impression to Signed Inquiry</span>
      </div>
      <div class="diagram-box">
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [NAVBAR]  EMSTELL LOGO        Web Engineering    Mobile Apps    AI Solutions    Case Studies   [START PROJECT CTA] │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [HERO SECTION]                                                                                   │
│  "Empowering Global Enterprises with Next-Gen Digital Products."                                 │
│  Subhead: Web Platforms • iOS/Android Apps • Generative AI & Automation                          │
│  [Explore Capabilities]    [Schedule a Discovery Call ➔]                                         │
│  Interactive 3D Technology Orb / Subtle Code Visualization Element                               │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [TRUST TICKER]  Trusted by Leading Brands across Kuwait, Saudi Arabia, UAE & the UK             │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [THE 3 CORE PILLARS - BENTO GRID]                                                                │
│  ┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐           │
│  │ 01. WEB ENGINEERING     │  │ 02. MOBILE APPS         │  │ 03. AI SOLUTIONS        │           │
│  │ Next.js, Microservices, │  │ Native iOS/Android,     │  │ Enterprise LLMs, Vision,│           │
│  │ Enterprise Portals &    │  │ Cross-Platform Flutter, │  │ Workflow Automation,    │           │
│  │ Cloud Infrastructure    │  │ Payment Gateways (KNET) │  │ Predictive Analytics    │           │
│  │ [Learn More ➔]          │  │ [Learn More ➔]          │  │ [Learn More ➔]          │           │
│  └─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [FEATURED CLIENT IMPACT] Interactive Case Studies with Real Metrics (e.g., 2.4M Users, 99.9% Up) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [INTERACTIVE INQUIRY SECTION] Multi-Step Scope Selector: [App] [Web] [AI] + [Direct WhatsApp]   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Emstell Technologies • Corporate Website Redesign Proposal</span>
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
        <div class="brand-title">Lead Capture Engine & CMS Backend <span class="brand-badge">Functionality</span></div>
        <div class="brand-sub">Frictionless Inquiries, Instant WhatsApp Routing, and Smooth Content Management</div>
      </div>
      <div class="meta-block">
        <strong>Lead Flow:</strong> Multi-Step Form + WhatsApp Direct<br>
        <strong>Speed:</strong> 98+ PageSpeed • Sub-1s Load Time<br>
        <strong>Backend:</strong> Smooth Visual Block Editor
      </div>
    </div>

    <!-- Interactive Lead Engine -->
    <div class="section">
      <div class="section-title">
        5. High-Converting Inquiry Engine
        <span class="tagline">Turning Passive Visitors into Qualified Business Leads</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">2-Step Interactive Project Estimator</span>
            <span class="card-badge">Conversion</span>
          </div>
          <p class="card-p">
            Traditional contact forms generate low response rates. We replace them with an engaging, interactive project selector:
          </p>
          <ul class="card-bullets">
            <li><strong>Step 1 (Scope Selection):</strong> Visitor clicks visual pills: <em>[ ] Mobile App (iOS/Android)</em>, <em>[ ] Enterprise Web Portal</em>, <em>[ ] AI Solution / Chatbot</em>, with an estimated launch timeline.</li>
            <li><strong>Step 2 (Contact Information):</strong> Clean input for Name, Corporate Email, Phone/WhatsApp, and Project Brief.</li>
            <li><strong>Automated Routing:</strong> Submissions instantly trigger email notifications to Emstell sales leads, log directly into your CRM/Google Sheets, and provide immediate confirmation to the client.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">GCC-Optimized WhatsApp Integration</span>
            <span class="card-badge">Instant Chat</span>
          </div>
          <p class="card-p">
            In the Gulf region (Kuwait and Saudi Arabia), business decisions move fastest over WhatsApp:
          </p>
          <ul class="card-bullets">
            <li><strong>Floating Smart WhatsApp Pill:</strong> Persistent, non-intrusive floating button that opens a pre-populated inquiry on WhatsApp (e.g., <em>"Hello Emstell, I'm interested in discussing a Mobile/AI project..."</em>).</li>
            <li><strong>Click-to-Call Regional Office Badges:</strong> Direct phone dialers for Emstell's Kuwait (Al Tijaria Tower) and Saudi Arabia office desks.</li>
            <li><strong>Zero Spam / CAPTCHA Free:</strong> Honeypot spam filtering that protects your inbox without frustrating prospective clients with image puzzles.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Smooth Backend CMS -->
    <div class="section">
      <div class="section-title">
        6. Smooth Backend Content Management Experience
        <span class="tagline">Empowering Emstell's Marketing Team with Zero Developer Dependency</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Modular Component-Based CMS</span>
            <span class="card-badge">Ease of Use</span>
          </div>
          <p class="card-p">
            Whether built on a headless architecture (Next.js + Strapi) or optimized modern WordPress, the content editing experience is designed for speed:
          </p>
          <ul class="card-bullets">
            <li><strong>Guardrailed Design Blocks:</strong> Marketing team members can edit case study text, upload mockups, and publish blogs without ever breaking typography, colors, or grid alignment.</li>
            <li><strong>Case Study Showcase Builder:</strong> Simple fields for Client Name, Industry, Challenge, Solution, Tech Stack Used, and Results Metrics.</li>
            <li><strong>Live Visual Preview:</strong> Preview updates before publishing to production with one click.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Technical Performance & SEO Benchmarks</span>
            <span class="card-badge">Speed & SEO</span>
          </div>
          <p class="card-p">
            Engineered to outperform competing software consultancies:
          </p>
          <ul class="card-bullets">
            <li><strong>Core Web Vitals Optimization:</strong> Target 95–99 Google PageSpeed score, sub-1-second Largest Contentful Paint (LCP), and zero Cumulative Layout Shift (CLS).</li>
            <li><strong>Next-Gen Image Formats:</strong> Automated WebP/AVIF compression with responsive srcset generation for flawless retina screen display.</li>
            <li><strong>GCC Search Optimization:</strong> Semantic Schema.org structured data for IT Services, Organization metadata, and OpenGraph social preview cards for LinkedIn and Twitter.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Emstell Technologies • Corporate Website Redesign Proposal</span>
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
        <div class="brand-title">Roadmap, Squad & Next Steps <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Structured 4-Week Delivery, GCC Track Record, and Commercial Terms</div>
      </div>
      <div class="meta-block">
        <strong>Timeline:</strong> 3 to 4 Weeks to Launch<br>
        <strong>Pre-Hire Deliverable:</strong> Complimentary Figma Hero Concept<br>
        <strong>Support:</strong> 30 Days Post-Deployment Warranty
      </div>
    </div>

    <!-- Phased Roadmap -->
    <div class="section">
      <div class="section-title">
        7. 4-Week Phased Implementation Roadmap
        <span class="tagline">Rapid, Predictable Execution from Concept to Production Cutover</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Wireframing & Figma Prototypes</span>
            <span class="card-badge">Week 1</span>
          </div>
          <ul class="card-bullets">
            <li>Conduct discovery review of existing emstell.com assets and key case studies.</li>
            <li>Deliver interactive Figma design prototypes for the 5 core pages for client review and signoff.</li>
            <li>Finalize the dark tech aesthetic, typography pairing, and responsive mobile layouts.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: Frontend Engineering & Visuals</span>
            <span class="card-badge">Week 2</span>
          </div>
          <ul class="card-bullets">
            <li>Build responsive, high-performance frontend interfaces adhering 1:1 to approved Figma designs.</li>
            <li>Implement fluid animations, glassmorphic bento cards, and interactive hover states.</li>
            <li>Build the 3-pillar deep-dive hubs for Web, Mobile Apps, and AI Solutions.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: CMS Backend & Inquiry Automations</span>
            <span class="card-badge">Week 3</span>
          </div>
          <ul class="card-bullets">
            <li>Configure smooth CMS backend allowing code-free case study, blog, and copy editing.</li>
            <li>Deploy the multi-step interactive project scope estimator with email and CRM notifications.</li>
            <li>Configure floating WhatsApp direct chat trigger and phone click-to-call routing.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: QA, Speed Optimization & Launch</span>
            <span class="card-badge">Week 4</span>
          </div>
          <ul class="card-bullets">
            <li>Execute cross-browser and mobile device testing (iOS Safari, Android Chrome, Desktop).</li>
            <li>Optimize Core Web Vitals to achieve 95+ PageSpeed benchmark.</li>
            <li>Perform zero-downtime DNS cutover to live domain (www.emstell.com) + 30 days warranty.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Meet the Squad -->
    <div class="section">
      <div class="section-title">
        8. Meet The Digital Rebuild Squad
        <span class="tagline">Proven Full-Stack & UI/UX Engineers with Gulf Enterprise Experience</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Full-Stack & CMS Architect</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Systems Experience</div>
            <p class="card-p">
              Specializes in modern web applications, Next.js/React, headless CMS architectures, and enterprise integrations across Kuwait, UAE, and global markets.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Next.js / React</span>
            <span class="chip">Headless CMS</span>
            <span class="chip">Tailwind CSS</span>
            <span class="chip">GCC Experience</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">UI/UX & Frontend Developer</div>
            <div class="member-creds">Programmer, DMS Electronics • Interactive Web & App Systems</div>
            <p class="card-p">
              Builds responsive frontend interfaces, interactive animation states, lead capture calculators, and fast-loading cross-device web experiences.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">UI/UX Design</span>
            <span class="chip">Responsive Web</span>
            <span class="chip">Form Automations</span>
            <span class="chip">Performance</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Project Manager</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise Digital Platforms</div>
            <p class="card-p">
              Oversees sprint milestones, client communication, design feedback cycles, and quality assurance to ensure launch deadlines are met without compromise.
            </p>
          </div>
          <div class="skill-chips">
            <span class="chip">Sprint Delivery</span>
            <span class="chip">QA Acceptance</span>
            <span class="chip">Milestone Tracking</span>
            <span class="chip">Documentation</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Call to action -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #0066ff; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Pre-Hire Deliverable: Clear Design Concept Ready for Review</div>
      <div class="callout-text" style="color: #334155;">
        As requested in your brief (<em>"You will have to give Clear design idea before we hire you"</em>), we are ready to share a visual Figma concept mockup of the new Emstell homepage hero and 3-pillar bento grid immediately upon our introductory discussion. Let us connect to discuss your exact vision.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Emstell Technologies • Corporate Website Redesign Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\Emstell_Website_Redesign"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "Emstell_Corporate_Website_Redesign_Proposal.pdf")
    
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

