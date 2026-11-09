import os
import subprocess
from pypdf import PdfReader

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upwork Proposal - Application & Desktop Code Generator - Viranga Lakshan</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

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

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      background-color: #f1f5f9;
      line-height: 1.42;
      font-size: 11px;
    }

    .page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      overflow: hidden;
      position: relative;
      background: #ffffff;
      padding: 15mm 18mm 13mm 18mm;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* Top Gradient Accent */
    .top-gradient-bar {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, #6366f1, #3b82f6, #06b6d4, #10b981);
    }

    /* Header */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 11px;
      border-bottom: 1.5px solid #e2e8f0;
      margin-bottom: 12px;
    }

    .author-info h1 {
      font-size: 21px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    .author-info .title {
      font-size: 11.5px;
      font-weight: 600;
      color: #4f46e5;
      margin-top: 2px;
    }

    .contact-chips {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 3px;
      font-size: 9.5px;
      color: #475569;
    }

    .contact-item a {
      color: #0284c7;
      text-decoration: none;
      font-weight: 600;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #31104b 100%);
      color: #ffffff;
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 12px;
      box-shadow: 0 8px 20px -4px rgba(15, 23, 42, 0.25);
    }

    .hero-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
    }

    .badge-client {
      background: rgba(99, 102, 241, 0.25);
      color: #a5b4fc;
      border: 1px solid rgba(165, 180, 252, 0.4);
      padding: 2.5px 8px;
      border-radius: 5px;
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-exp {
      background: rgba(16, 185, 129, 0.25);
      color: #34d399;
      border: 1px solid rgba(52, 211, 153, 0.4);
      padding: 2.5px 8px;
      border-radius: 5px;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.4px;
    }

    .badge-price {
      background: rgba(245, 158, 11, 0.25);
      color: #fbbf24;
      border: 1px solid rgba(251, 191, 36, 0.4);
      padding: 2.5px 8px;
      border-radius: 5px;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.4px;
    }

    .hero-title {
      font-size: 17px;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #ffffff;
      margin-bottom: 5px;
    }

    .hero-desc {
      font-size: 10.3px;
      color: #cbd5e1;
      line-height: 1.45;
    }

    /* Metric Cards */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 9px;
      margin-bottom: 12px;
    }

    .metric-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 9px;
      padding: 9px 10px;
      text-align: center;
      border-top: 3px solid #6366f1;
    }

    .metric-card:nth-child(2) { border-top-color: #06b6d4; }
    .metric-card:nth-child(3) { border-top-color: #10b981; }
    .metric-card:nth-child(4) { border-top-color: #f59e0b; }

    .metric-value {
      font-size: 15px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    .metric-label {
      font-size: 8.8px;
      font-weight: 600;
      color: #64748b;
      margin-top: 1px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    /* Section Header */
    .section-title {
      font-size: 12.2px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 8px;
      letter-spacing: -0.2px;
    }

    .section-title svg {
      color: #4f46e5;
      width: 15px;
      height: 15px;
    }

    .card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 9px;
      padding: 11px 13px;
      margin-bottom: 11px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    /* Upwork Introduction Callout */
    .intro-callout {
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 1.5px solid #a7f3d0;
      border-radius: 9px;
      padding: 10px 13px;
      margin-bottom: 11px;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }

    .intro-icon {
      background: #10b981;
      color: #ffffff;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 13px;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .intro-text h4 {
      font-size: 11px;
      font-weight: 700;
      color: #065f46;
      margin-bottom: 2px;
    }

    .intro-text p {
      font-size: 10px;
      color: #047857;
      line-height: 1.4;
    }

    /* Technical Approach Grid */
    .approach-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 9px;
      margin-bottom: 11px;
    }

    .approach-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 9px 11px;
    }

    .approach-header {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 10.5px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 3px;
    }

    .approach-bullet {
      width: 17px;
      height: 17px;
      border-radius: 50%;
      background: #ede9fe;
      color: #6d28d9;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 9px;
      font-weight: 800;
      flex-shrink: 0;
    }

    .approach-desc {
      font-size: 9.6px;
      color: #475569;
      line-height: 1.38;
    }

    /* Multi-Language Architecture Box */
    .arch-box {
      background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
      border: 1px solid #bfdbfe;
      border-radius: 9px;
      padding: 10px 12px;
      margin-bottom: 5px;
    }

    .arch-title {
      font-size: 10.8px;
      font-weight: 700;
      color: #1e40af;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
    }

    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 7px;
    }

    .pillar-item {
      background: #ffffff;
      border: 1px solid #dbeafe;
      border-radius: 6px;
      padding: 7px 9px;
    }

    .pillar-name {
      font-size: 9.5px;
      font-weight: 700;
      color: #2563eb;
      margin-bottom: 2px;
    }

    .pillar-text {
      font-size: 8.8px;
      color: #475569;
      line-height: 1.32;
    }

    /* Projects Showcase */
    .project-card {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 9px;
      background: #ffffff;
    }

    .project-card:last-child {
      margin-bottom: 0;
    }

    .project-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 4px;
    }

    .project-name {
      font-size: 11px;
      font-weight: 700;
      color: #0f172a;
    }

    .project-client {
      font-size: 8.8px;
      font-weight: 600;
      color: #4f46e5;
      background: #ede9fe;
      padding: 1.5px 6px;
      border-radius: 4px;
    }

    .project-summary {
      font-size: 9.5px;
      color: #334155;
      line-height: 1.38;
      margin-bottom: 4px;
    }

    .project-bullets {
      list-style: none;
      font-size: 9.2px;
      color: #475569;
      margin-bottom: 5px;
    }

    .project-bullets li {
      position: relative;
      padding-left: 12px;
      margin-bottom: 2.5px;
      line-height: 1.33;
    }

    .project-bullets li::before {
      content: "✓";
      position: absolute;
      left: 0;
      color: #059669;
      font-weight: bold;
      font-size: 8.5px;
    }

    .project-tech {
      display: flex;
      flex-wrap: wrap;
      gap: 3.5px;
      padding-top: 3px;
      border-top: 1px dashed #f1f5f9;
    }

    /* Tags */
    .tag {
      display: inline-block;
      padding: 1.5px 5.5px;
      border-radius: 4px;
      font-size: 8.3px;
      font-weight: 600;
      margin-right: 3px;
      margin-bottom: 2px;
    }

    .tag-blue { background: #dbeafe; color: #1e40af; }
    .tag-cyan { background: #cffafe; color: #0e7490; }
    .tag-emerald { background: #d1fae5; color: #065f46; }
    .tag-purple { background: #ede9fe; color: #5b21b6; }
    .tag-amber { background: #fef3c7; color: #92400e; }
    .tag-indigo { background: #e0e7ff; color: #3730a3; }

    /* Skills Grid */
    .skills-matrix {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 7px;
      margin-bottom: 10px;
    }

    .skill-category {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 7px;
      padding: 7px 9px;
    }

    .skill-cat-title {
      font-size: 8.8px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 3px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 1.5px;
    }

    .skill-cat-items {
      font-size: 8.8px;
      color: #475569;
      line-height: 1.35;
    }

    /* Fixed Price Plan */
    .plan-box {
      border: 1.5px solid #e0e7ff;
      background: #fcfdff;
      border-radius: 8px;
      padding: 9px 12px;
      margin-bottom: 9px;
    }

    .plan-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }

    .plan-step {
      font-size: 9px;
      color: #334155;
      line-height: 1.35;
    }

    .plan-step strong {
      display: block;
      color: #1e1b4b;
      font-size: 9.5px;
      margin-bottom: 2px;
    }

    /* CTA Box */
    .cta-box {
      background: linear-gradient(135deg, #0f172a 0%, #31104b 100%);
      color: #ffffff;
      border-radius: 9px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .cta-content h3 {
      font-size: 11.8px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 1px;
    }

    .cta-content p {
      font-size: 9.3px;
      color: #c7d2fe;
    }

    .cta-badge {
      background: #10b981;
      color: #ffffff;
      font-weight: 700;
      font-size: 9.8px;
      padding: 5px 11px;
      border-radius: 5px;
      box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
      white-space: nowrap;
    }

    /* Footer */
    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 8px;
      border-top: 1px solid #e2e8f0;
      font-size: 8.5px;
      color: #94a3b8;
    }

    .footer-left {
      display: flex;
      gap: 10px;
    }

    .page-number {
      font-weight: 700;
      color: #4f46e5;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1: EXECUTIVE PROPOSAL & ARCHITECTURE ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Header -->
      <div class="header">
        <div class="author-info">
          <h1>VIRANGA LAKSHAN</h1>
          <div class="title">Software Engineer · Full Stack, Desktop & Code Scaffolding Specialist</div>
        </div>
        <div class="contact-chips">
          <div class="contact-item">
            <span>📄 <a href="https://drive.google.com/file/d/1dNXU_Ig0WMNT2lwEaoSZ6P8O1Xx1EKxu/view?usp=sharing" target="_blank">View Full CV (Google Drive)</a></span>
          </div>
          <div class="contact-item">
            <span>📧 virangalakshanz@gmail.com</span>
          </div>
          <div class="contact-item">
            <span>📱 +94 71 378 1359</span>
          </div>
          <div class="contact-item">
            <span>🔗 <a href="https://linkedin.com/in/viranga-lakshan-869515279" target="_blank">linkedin.com/in/viranga-lakshan</a></span>
          </div>
        </div>
      </div>

      <!-- Hero Banner -->
      <div class="hero-banner">
        <div class="hero-meta">
          <span class="badge-client">Upwork Fixed-Price Proposal</span>
          <span class="badge-exp">✓ 4 Years Industry Enterprise Exp</span>
          <span class="badge-price">★ $200 Fixed Price · 100% Non-AI</span>
        </div>
        <div class="hero-title">Technical Proposal: Deterministic Application & Desktop Code Generator (Without AI)</div>
        <div class="hero-desc">
          A robust, rule-based code generation engine for desktop and applications. 100% deterministic, offline-capable, and template-driven (no AI hallucinations or API costs). Built to generate clean, maintainable code across your required languages (C#, Java, PHP, JavaScript, Python, HTML/CSS).
        </div>
      </div>

      <!-- Upwork Introduction Callout -->
      <div class="intro-callout">
        <div class="intro-icon">★</div>
        <div class="intro-text">
          <h4>New to Upwork — Backed by 4 Years of Proven Enterprise Experience</h4>
          <p>
            While I am new to the Upwork platform, I bring <strong>4 years of dedicated industry software engineering experience</strong> working at premier technology companies (including <strong>Arimac Lanka</strong> and <strong>SLT Digital Lab</strong>), building mission-critical enterprise systems for top international corporations across Kuwait, UAE, and Sri Lanka.
          </p>
        </div>
      </div>

      <!-- Metric Highlights -->
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">4 Years</div>
          <div class="metric-label">Software Industry Exp</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Non-AI</div>
          <div class="metric-label">100% Deterministic Engine</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Multi-Stack</div>
          <div class="metric-label">C#, Java, PHP, JS, Python</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">$200 Fixed</div>
          <div class="metric-label">Guaranteed On-Time Delivery</div>
        </div>
      </div>

      <!-- Section: Why Non-AI Code Generation -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
        Non-AI Code Generation: Technical Architecture & Core Advantages
      </div>
      <div class="approach-grid">
        <div class="approach-card">
          <div class="approach-header">
            <span class="approach-bullet">1</span>
            <span>Template & AST-Based Scaffolding</span>
          </div>
          <div class="approach-desc">
            Uses proven template engines (Mustache / Handlebars / Jinja2 / T4) combined with token parsers to map schema inputs directly to production-ready boilerplate without errors.
          </div>
        </div>
        <div class="approach-card">
          <div class="approach-header">
            <span class="approach-bullet">2</span>
            <span>100% Predictable & Bug-Free Output</span>
          </div>
          <div class="approach-desc">
            Unlike AI models that suffer from hallucinations, non-deterministic outputs, and random syntax drift, rule-based generation guarantees syntactically flawless code every time.
          </div>
        </div>
        <div class="approach-card">
          <div class="approach-header">
            <span class="approach-bullet">3</span>
            <span>Zero API Costs & Fully Offline</span>
          </div>
          <div class="approach-desc">
            Runs entirely on the local machine with no external LLM dependencies, zero recurring token fees, instantaneous millisecond generation speed, and total IP confidentiality.
          </div>
        </div>
        <div class="approach-card">
          <div class="approach-header">
            <span class="approach-bullet">4</span>
            <span>Desktop GUI or Lightweight CLI</span>
          </div>
          <div class="approach-desc">
            Delivered as an intuitive desktop tool (built with Electron/HTML/CSS or C# .NET WPF / Python GUI) or a CLI utility with clean configuration files (JSON/YAML/Forms).
          </div>
        </div>
      </div>

      <!-- Generator Workflow Box -->
      <div class="arch-box">
        <div class="arch-title">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          How the Code Generator Works
        </div>
        <div class="pillars-grid">
          <div class="pillar-item">
            <div class="pillar-name">1. Input / Schema Ingestion</div>
            <div class="pillar-text">
              Accepts entity models, database schemas, field definitions, or form inputs defining your classes, endpoints, or UI layouts.
            </div>
          </div>
          <div class="pillar-item">
            <div class="pillar-name">2. Rule & Template Engine</div>
            <div class="pillar-text">
              Applies structured language rules, naming conventions, import statements, and design patterns (Repository, MVC, Clean Architecture).
            </div>
          </div>
          <div class="pillar-item">
            <div class="pillar-name">3. One-Click Project Output</div>
            <div class="pillar-text">
              Outputs full directories of source files with formatted indentation, ready to compile and run immediately in your target language.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Viranga Lakshan · Software Engineer</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Application Code Generator (Without AI) Proposal</div>
      <div class="page-number">Page 1 of 3</div>
    </div>
  </div>

  <!-- ==================== PAGE 2: PROFESSIONAL PROJECTS (COMPANY EXPERIENCES 1, 2, 3) ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Section: Professional Projects Experience -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
        Professional Projects Experience (Enterprise Company Roles)
      </div>

      <!-- Project 01: Multi-Tenant E-Commerce Platform -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Project 01: Multi-Tenant E-Commerce Platform</span>
          </div>
          <span class="project-client">Arimac Digital · Full-Stack & Microservices</span>
        </div>
        <div class="project-summary">
          Backend and full-stack developer on a microservices-based, multi-tenant e-commerce platform supporting customer-facing and administrative applications. The platform consists of Node.js BFF services, Laravel Lumen domain services, and a Strapi headless CMS.
        </div>
        <ul class="project-bullets">
          <li>Developed and maintained <strong>Node.js/Express BFF services</strong> for customer and admin applications, aggregating and orchestrating APIs across multiple backend microservices.</li>
          <li>Developed and integrated <strong>Laravel Lumen microservices</strong> covering business domains including customers, orders, payments, products, promotions, tax, shipping, reporting, activities, and tenant management.</li>
          <li>Implemented authentication and authorization using <strong>Keycloak with OAuth2/OIDC and JWT</strong>, supporting secure access across distributed services.</li>
          <li>Integrated <strong>Strapi CMS and external REST APIs</strong>, while containerizing services with <strong>Docker</strong> and working with <strong>GitLab CI/CD</strong> for build and deployment workflows.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Node.js</span>
          <span class="tag tag-blue">Express.js</span>
          <span class="tag tag-purple">PHP 8</span>
          <span class="tag tag-purple">Laravel Lumen</span>
          <span class="tag tag-indigo">Strapi CMS</span>
          <span class="tag tag-cyan">Keycloak (OAuth2/JWT)</span>
          <span class="tag tag-emerald">MySQL</span>
          <span class="tag tag-amber">Docker / GitLab CI/CD</span>
        </div>
      </div>

      <!-- Project 02: Adrik News & Media Platform -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Project 02: Adrik News & Media Platform</span>
          </div>
          <span class="project-client">Arimac Digital · Client: Adrik, Kuwait</span>
        </div>
        <div class="project-summary">
          Backend developer on a bilingual (English/Arabic) news and media platform for a Kuwait-based client, with paid subscriptions, newsletters, and a mobile app. Built as three Node.js BFF services connecting the web, mobile, and admin frontends to the core backend API.
        </div>
        <ul class="project-bullets">
          <li>Developed and maintained <strong>Node.js/Express BFF services</strong> for web, mobile, and admin applications, aggregating and orchestrating calls to the core backend API.</li>
          <li>Implemented authentication and user management with <strong>Keycloak (OAuth2/OIDC, JWT)</strong>, including email and social-media signup/login, token refresh, password reset, and token validation middleware for protected routes.</li>
          <li>Built APIs for content and engagement features, including region-based news feeds, search, category menus, paginated articles, comments, bookmarks, likes, author follows, and click tracking.</li>
          <li>Integrated subscription and payment flows with <strong>OneSignal push notifications</strong> and <strong>SMS delivery</strong> for newsletters and app download links.</li>
          <li>Containerized services with <strong>Docker</strong> and deployed to <strong>Kubernetes</strong> through GitLab CI/CD pipelines across development, UAT, and production environments.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Node.js</span>
          <span class="tag tag-blue">Express.js</span>
          <span class="tag tag-cyan">Axios</span>
          <span class="tag tag-purple">Keycloak</span>
          <span class="tag tag-indigo">OneSignal</span>
          <span class="tag tag-amber">SMS Gateway API</span>
          <span class="tag tag-emerald">Kubernetes / Docker</span>
        </div>
      </div>

      <!-- Project 03: DIMO Gate Pass Management System -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Project 03: DIMO Gate Pass Management System</span>
          </div>
          <span class="project-client">Arimac Digital · Client: DIMO Lanka</span>
        </div>
        <div class="project-summary">
          Backend developer on a vehicle gate-pass and dispatch management platform for a large enterprise client, built as two Spring Boot microservices within a larger microservices architecture.
        </div>
        <ul class="project-bullets">
          <li>Developed a BFF/API gateway service handling <strong>Keycloak OAuth2/JWT authentication</strong>, role-based approval workflows, <strong>Kafka-based audit event publishing</strong>, and integrations with <strong>SAP, Google Maps, Microsoft Graph/Azure AD, Strapi CMS, and AWS S3</strong>.</li>
          <li>Built the core Gate Pass domain service, implementing business logic and persistence using <strong>MySQL with Flyway-managed database schema migrations</strong>.</li>
          <li>Implemented secure file-upload handling using <strong>AWS S3 with ClamAV virus scanning</strong>, and integrated external enterprise services to support vehicle orders, distance calculation, user management, and content management.</li>
          <li>Containerized both services using <strong>Docker</strong> and supported CI/CD workflows through <strong>Jenkins and GitLab</strong>, with automated code quality and test coverage checks (SonarQube, JaCoCo).</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Java 21</span>
          <span class="tag tag-blue">Spring Boot 3.4.5</span>
          <span class="tag tag-cyan">Spring Security</span>
          <span class="tag tag-purple">Spring Kafka</span>
          <span class="tag tag-emerald">MySQL / Flyway</span>
          <span class="tag tag-indigo">AWS S3 / ClamAV</span>
          <span class="tag tag-amber">Jenkins / GitLab CI/CD</span>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Viranga Lakshan · Software Engineer</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Application Code Generator (Without AI) Proposal</div>
      <div class="page-number">Page 2 of 3</div>
    </div>
  </div>

  <!-- ==================== PAGE 3: PROJECTS 04, 05, SKILLS & FIXED-PRICE PLAN ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Section: Professional Projects Experience (Continued) -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
        Professional Projects Experience (Continued)
      </div>

      <!-- Project 04: Al Ain Museum V2 -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Project 04: Al Ain Museum V2 – Sitecore Headless (In Progress)</span>
          </div>
          <span class="project-client">Arimac Digital · Client: Al Ain Museum, UAE</span>
        </div>
        <div class="project-summary">
          Frontend and CMS developer working on the rebuild of a multi-site Sitecore ecosystem, developing a scalable Next.js/React frontend and integrating Sitecore Headless CMS through REST APIs.
        </div>
        <ul class="project-bullets">
          <li>Leading the frontend and Sitecore integration development for the V2 platform, using <strong>Next.js, React, TypeScript, and Sitecore Helix principles</strong>.</li>
          <li>Replaced previous GraphQL content integration with <strong>REST API-based retrieval</strong>, providing greater control over content rendering and integration.</li>
          <li>Implemented custom logic to recursively traverse and render nested Sitecore content structures, supporting complex item hierarchies.</li>
          <li>Customized <strong>C#/.NET components</strong> and collaborated with stakeholders for a major government cultural institution platform.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Sitecore</span>
          <span class="tag tag-cyan">Next.js / React</span>
          <span class="tag tag-cyan">TypeScript</span>
          <span class="tag tag-purple">C#</span>
          <span class="tag tag-purple">.NET</span>
          <span class="tag tag-indigo">Sitecore Helix</span>
          <span class="tag tag-emerald">REST APIs</span>
        </div>
      </div>

      <!-- Project 05: Holsten Arabia -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Project 05: Holsten Arabia – Umbraco Headless</span>
          </div>
          <span class="project-client">Arimac Digital · Client: Holsten Arabia</span>
        </div>
        <div class="project-summary">
          Frontend and CMS developer on a headless CMS-based web platform for a global beverage brand, using Umbraco with a modern Next.js/React frontend to deliver a multilingual digital experience.
        </div>
        <ul class="project-bullets">
          <li>Developed and maintained the <strong>Next.js/React frontend</strong> using TypeScript, integrating content from Umbraco through RESTful APIs.</li>
          <li>Worked with <strong>Umbraco Headless CMS</strong>, developing and managing custom content types, components, and structured content.</li>
          <li>Developed and customized <strong>C#/.NET components</strong> and integrations to support content delivery and frontend requirements.</li>
          <li>Implemented responsive frontend experiences and contributed to platform stability and performance across different devices and screen sizes.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Umbraco</span>
          <span class="tag tag-cyan">Next.js / React</span>
          <span class="tag tag-cyan">TypeScript</span>
          <span class="tag tag-purple">C#</span>
          <span class="tag tag-purple">.NET</span>
          <span class="tag tag-emerald">REST APIs</span>
        </div>
      </div>

      <!-- Skills Matrix Across Required Languages -->
      <div class="section-title" style="margin-top: 8px;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
        Multi-Language Technical Competencies (Job Mandatory Skills)
      </div>
      <div class="skills-matrix">
        <div class="skill-category">
          <div class="skill-cat-title">C#, .NET & Java</div>
          <div class="skill-cat-items">C#, .NET, Java 21, Spring Boot 3, Spring Modulith, OOP, Class/DTO Scaffolding, Strong Typing</div>
        </div>
        <div class="skill-category">
          <div class="skill-cat-title">JS, TS & Desktop/Web UI</div>
          <div class="skill-cat-items">JavaScript (ES6+), TypeScript, Electron, Node.js, React, HTML5, CSS3, Tailwind CSS</div>
        </div>
        <div class="skill-category">
          <div class="skill-cat-title">PHP, Python & Engines</div>
          <div class="skill-cat-items">PHP 8, Laravel Lumen, Python, Mustache, Jinja2, AST Parsers, JSON/YAML Schema, REST APIs</div>
        </div>
      </div>

      <!-- Fixed Price Delivery Plan -->
      <div class="plan-box">
        <div style="font-size: 10px; font-weight: 700; color: #1e1b4b; margin-bottom: 5px; display: flex; justify-content: space-between;">
          <span>📦 $200 Fixed-Price Execution Plan & Deliverables</span>
          <span style="color: #10b981;">Turnaround: 3 to 5 Days</span>
        </div>
        <div class="plan-grid">
          <div class="plan-step">
            <strong>1. Input & Template Definition</strong>
            Confirm schema structure (JSON/YAML or GUI inputs) and define target boilerplate templates.
          </div>
          <div class="plan-step">
            <strong>2. Core Engine Build & Testing</strong>
            Develop the deterministic generator engine, error-checking, and formatters for output code.
          </div>
          <div class="plan-step">
            <strong>3. Packaging & Handover</strong>
            Deliver complete source code, executable application, sample templates, and a quick video demo.
          </div>
        </div>
      </div>

      <!-- CTA Box -->
      <div class="cta-box">
        <div class="cta-content">
          <h3>Ready to Build Your Non-AI Code Generator</h3>
          <p>Available to start immediately and deliver a polished, reliable solution within your $200 budget.</p>
        </div>
        <div class="cta-badge">⚡ Ready to Begin Today</div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Viranga Lakshan · Software Engineer</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Application Code Generator (Without AI) Proposal</div>
      <div class="page-number">Page 3 of 3</div>
    </div>
  </div>

</body>
</html>
"""

html_path = os.path.abspath("Viranga_Lakshan_Code_Generator_Proposal.html")
pdf_path = os.path.abspath("Viranga_Lakshan_Code_Generator_Proposal.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_path}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_url = "file:///" + html_path.replace("\\", "/")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_url
]

subprocess.run(cmd, check=True)

if os.path.exists(pdf_path):
    reader = PdfReader(pdf_path)
    page_count = len(reader.pages)
    file_size = os.path.getsize(pdf_path)
    print(f"SUCCESS: PDF generated at {pdf_path}")
    print(f"Pages: {page_count}, Size: {file_size} bytes")
else:
    print("ERROR: PDF file not found!")

