import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Technical Partnership Proposal - AI Development & Systems Integration</title>
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
    font-size: 8.5pt;
    line-height: 1.38;
  }
  .page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    padding: 12mm 15mm 11mm 15mm;
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
    border-bottom: 2px solid #2563eb;
    padding-bottom: 7px;
    margin-bottom: 10px;
  }
  .brand-title {
    font-size: 13pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.3px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-badge {
    background: #2563eb;
    color: #ffffff;
    font-size: 7pt;
    font-weight: 700;
    padding: 2.5px 7px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .brand-sub {
    font-size: 8pt;
    color: #475569;
    font-weight: 600;
    margin-top: 2px;
  }
  .meta-block {
    text-align: right;
    font-size: 7.8pt;
    color: #64748b;
    line-height: 1.35;
  }
  .meta-block strong {
    color: #0f172a;
  }

  /* Hero Banner */
  .hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
    color: #ffffff;
    border-radius: 6px;
    padding: 10px 13px;
    margin-bottom: 10px;
  }
  .hero-title {
    font-size: 11.5pt;
    font-weight: 800;
    letter-spacing: -0.2px;
    margin: 0 0 3px 0;
    color: #ffffff;
  }
  .hero-desc {
    font-size: 8pt;
    color: #e2e8f0;
    margin: 0 0 8px 0;
    line-height: 1.36;
  }
  .hero-pills {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }
  .hero-pill {
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.22);
    padding: 2px 7px;
    border-radius: 3px;
    font-size: 7.2pt;
    color: #f8fafc;
  }
  .hero-pill strong {
    color: #93c5fd;
  }

  /* Section Styling */
  .section {
    margin-bottom: 9.5px;
  }
  .section-title {
    font-size: 9.6pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 3.5px solid #2563eb;
    padding-left: 7px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.2px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .section-title .tagline {
    font-size: 7.5pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
  }

  /* Grid Layouts */
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
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
  }

  /* Cards */
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 7px 9px;
  }
  .card.highlight {
    background: #eff6ff;
    border-color: #bfdbfe;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 3.5px;
  }
  .card.highlight .card-header {
    border-color: #bfdbfe;
  }
  .card-title {
    font-size: 8.5pt;
    font-weight: 700;
    color: #0f172a;
  }
  .card-badge {
    font-size: 6.8pt;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 3px;
    background: #e2e8f0;
    color: #475569;
    text-transform: uppercase;
  }
  .card.highlight .card-badge {
    background: #dbeafe;
    color: #1d4ed8;
  }
  .card-p {
    font-size: 7.8pt;
    color: #334155;
    margin: 0 0 4px 0;
    line-height: 1.33;
  }
  .card-bullets {
    margin: 0;
    padding-left: 13px;
    font-size: 7.6pt;
    color: #475569;
    line-height: 1.33;
  }
  .card-bullets li {
    margin-bottom: 2px;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.6pt;
    margin-top: 2px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 4.5px 7px;
    font-weight: 700;
    font-size: 7.3pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  table.matrix-table td {
    padding: 4.5px 7px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
    color: #334155;
    line-height: 1.3;
  }
  table.matrix-table tr:nth-child(even) td {
    background: #f8fafc;
  }
  table.matrix-table td strong {
    color: #0f172a;
  }

  /* Visual Pipeline Flow */
  .pipeline-flow {
    display: flex;
    align-items: stretch;
    gap: 6px;
    margin-top: 3px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px;
  }
  .pipeline-col {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 7px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .pipeline-col.accent {
    border-top: 3px solid #2563eb;
    flex: 1.25;
  }
  .pipeline-badge {
    display: inline-block;
    font-size: 6.6pt;
    font-weight: 700;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }
  .pipeline-title {
    font-size: 8.1pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 3px;
  }
  .pipeline-p {
    font-size: 7.3pt;
    color: #475569;
    line-height: 1.3;
    margin: 0;
  }
  .pipeline-bullets {
    margin: 0;
    padding-left: 12px;
    font-size: 7.1pt;
    color: #334155;
    line-height: 1.28;
  }
  .pipeline-bullets li {
    margin-bottom: 1.5px;
  }
  .pipeline-bullets code, .pipeline-p code, .card-p code {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 0.5px 3px;
    border-radius: 3px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 6.9pt;
    color: #0f172a;
  }
  .pipeline-arrow {
    display: flex;
    align-items: center;
    color: #94a3b8;
    font-size: 10pt;
    font-weight: 700;
  }

  /* Callout */
  .callout-box {
    background: #eff6ff;
    border-left: 3.5px solid #2563eb;
    border-radius: 4px;
    padding: 6px 9px;
    margin-top: 5px;
  }
  .callout-title {
    font-size: 8.2pt;
    font-weight: 700;
    color: #1e40af;
    margin-bottom: 1.5px;
  }
  .callout-text {
    font-size: 7.6pt;
    color: #1e3a8a;
    line-height: 1.32;
  }

  /* SLA Badges */
  .sla-badge {
    display: inline-block;
    padding: 1.5px 5px;
    border-radius: 3px;
    font-weight: 700;
    font-size: 6.8pt;
    text-transform: uppercase;
  }
  .sla-crit { background: #fee2e2; color: #991b1b; }
  .sla-high { background: #fef3c7; color: #92400e; }
  .sla-med  { background: #e0f2fe; color: #075985; }
  .sla-low  { background: #f1f5f9; color: #475569; }

  /* Team Profile Card */
  .profile-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 7px 9px;
    margin-bottom: 6px;
  }
  .profile-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 3px;
  }
  .profile-name {
    font-size: 8.8pt;
    font-weight: 800;
    color: #0f172a;
  }
  .profile-role {
    font-size: 7.5pt;
    color: #2563eb;
    font-weight: 600;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.2pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #2563eb;
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
          Technical Partnership Proposal <span class="brand-badge">Agency Wing</span>
        </div>
        <div class="brand-sub">Dedicated Offshore AI Engineering, Systems Integration & Continuous Maintenance for IMM</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> IMM (20-Year Established US Agency)<br>
        <strong>Engagement:</strong> Technical Execution & White-Label Partner<br>
        <strong>Lead Contact:</strong> Viranga Lakshan (Solutions Architect)<br>
        <strong>Model:</strong> Boutique Agency (Tech Lead + Senior Engineers)
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Empowering IMM’s AI & Enterprise Integration Expansion</div>
      <div class="hero-desc">
        A high-caliber boutique engineering team designed to serve as IMM’s dedicated offshore technology wing. Delivering custom AI applications, autonomous agents, enterprise systems integration (APIs, CRMs, ERPs), and robust workflow automations with US-aligned coverage, guaranteed incident SLAs, and client-facing technical leadership.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Focus: <strong>Custom AI Agents • RAG • Folder/Doc Ingestion</strong></div>
        <div class="hero-pill">Integrations: <strong>HubSpot • Salesforce • ERPs • REST/GraphQL</strong></div>
        <div class="hero-pill">Automation: <strong>n8n • Make • Zapier • Event-Driven Python</strong></div>
        <div class="hero-pill">Support: <strong>8+ Hrs Daily Coverage • 1-Hour Critical SLA</strong></div>
        <div class="hero-pill">Ramp-Up: <strong>Ready to Pilot with a Paid Proof of Concept</strong></div>
      </div>
    </div>

    <!-- Section 1: Executive Overview -->
    <div class="section">
      <div class="section-title">
        1. Strategic Partnership Philosophy
        <span class="tagline">Why a Boutique Engineering Agency is the Ideal Model for IMM</span>
      </div>
      <div class="grid-2">
        <div class="card highlight">
          <div class="card-header">
            <span class="card-title">Agency-First White-Label Execution</span>
            <span class="card-badge">IMM Retains Control</span>
          </div>
          <p class="card-p">
            IMM owns client relationships, strategic direction, and project ownership. We operate seamlessly behind your brand or as your integrated technical branch:
          </p>
          <ul class="card-bullets">
            <li><strong>Client-Facing Solutions Engineer:</strong> Fluent English-speaking Technical Lead available to co-pilot discovery sessions, clarify technical scope, and architect solutions alongside IMM account leads.</li>
            <li><strong>Zero Junior Hand-Offs:</strong> You interface directly with senior architects and full-stack builders who write and maintain the codebase.</li>
            <li><strong>Transparent Velocity:</strong> Sprint planning, daily Slack updates, shared staging environments, and clean Git commits.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Practical Engineering Over Tech Hype</span>
            <span class="card-badge">Business Impact</span>
          </div>
          <p class="card-p">
            We value solid computer science fundamentals, maintainability, and tangible business ROI over bleeding-edge instability:
          </p>
          <ul class="card-bullets">
            <li><strong>Cost-Effective AI Architectures:</strong> Balancing LLM token economics (GPT-4o, Claude 3.5 Sonnet, local open-source models) with caching, semantic search, and deterministic logic.</li>
            <li><strong>Modular Systems Design:</strong> Decoupled microservices and webhook architectures that prevent vendor lock-in and simplify client scaling.</li>
            <li><strong>Defensive Engineering:</strong> Comprehensive schema validation, idempotency in payment/CRM syncs, and structured audit logs.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 2: Core Capability Pillars -->
    <div class="section">
      <div class="section-title">
        2. Core Technical Competency Pillars
        <span class="tagline">Comprehensive Engineering Across Modern Stacks</span>
      </div>
      <div class="grid-4">
        <div class="card">
          <div class="card-header">
            <span class="card-title">AI & Agents</span>
            <span class="card-badge">LLM / RAG</span>
          </div>
          <p class="card-p">
            Autonomous multi-agent systems (LangGraph, CrewAI), folder/document embeddings, vector stores (Pinecone, pgvector), and custom domain copilots.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Integrations</span>
            <span class="card-badge">APIs & CRMs</span>
          </div>
          <p class="card-p">
            Bidirectional sync across Salesforce, HubSpot, GoHighLevel, Zoho, ERPs, payment gateways, and bespoke legacy relational databases.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Automations</span>
            <span class="card-badge">n8n / Make</span>
          </div>
          <p class="card-p">
            Complex multi-branch workflows in n8n (cloud/self-hosted), Make, Zapier, paired with custom Python/Node serverless event microservices.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Cloud & Security</span>
            <span class="card-badge">AWS / GCP</span>
          </div>
          <p class="card-p">
            Docker containers, CI/CD pipelines, OAuth2/JWT auth, OWASP hardening, zero data retention for PII, and strict role-based access.
          </p>
        </div>
      </div>
    </div>

    <!-- Callout Box -->
    <div class="callout-box">
      <div class="callout-title">Proven Low-Risk Onboarding: Paid Proof of Concept (PoC)</div>
      <div class="callout-text">
        To initiate the partnership with zero risk to IMM’s client reputation, we propose starting with a tightly scoped, paid Proof of Concept, isolated API integration, or marketing automation pilot. This allows IMM leadership to assess our architectural rigor, communication velocity, and code quality before rolling us out across broader client accounts.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>IMM Technical Partnership Proposal • AI Development & Systems Integration</span>
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
        <div class="brand-title">Technical Capabilities & Architecture <span class="brand-badge">Stack & Deep Dive</span></div>
        <div class="brand-sub">Production-Ready AI Applications, Systems Integration, and Robust Workflow Pipelines</div>
      </div>
      <div class="meta-block">
        <strong>AI Stacks:</strong> LangChain, LangGraph, LlamaIndex, OpenAI, Anthropic<br>
        <strong>Automation:</strong> n8n, Make, Zapier, Python FastAPI, Celery<br>
        <strong>Data & Cloud:</strong> PostgreSQL, Redis, pgvector, Docker, AWS, GCP
      </div>
    </div>

    <!-- Section 3: Technical Capabilities Matrix -->
    <div class="section">
      <div class="section-title">
        3. Detailed Technical Capabilities Matrix
        <span class="tagline">What We Deliver for IMM and Your Client Base</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 22%;">Domain</th>
            <th style="width: 44%;">Core Technical Capabilities</th>
            <th style="width: 34%;">Practical Client Applications</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Custom AI & Agent Systems</strong></td>
            <td>LLM integrations (OpenAI GPT-4o, Claude 3.5 Sonnet, Gemini Flash), autonomous agent orchestration (LangGraph, CrewAI), folder/document ingestion engines, RAG pipelines with chunking and reranking, structured tool-use functions.</td>
            <td>Customer support AI agents, automated proposal builders, document Q&A tools, internal business copilots, and content transformation engines.</td>
          </tr>
          <tr>
            <td><strong>Enterprise Systems Integration</strong></td>
            <td>RESTful & GraphQL API engineering, webhook receivers with replay protection, ETL pipelines, bidirectional CRM sync (HubSpot, Salesforce, Zoho, HighLevel), ERP database connectors, and payment flows.</td>
            <td>Connecting disparate client CRMs with billing databases, synchronizing inventory across e-commerce channels, and building unified analytics hubs.</td>
          </tr>
          <tr>
            <td><strong>Workflow Automation & Ops</strong></td>
            <td>Advanced multi-step scenarios in self-hosted and cloud n8n, Make (Integromat), Zapier, supplemented with asynchronous Python/FastAPI queues (Redis, Celery) for high-volume transformations.</td>
            <td>Automated lead routing & scoring, automated invoice reconciliation, multi-channel client onboarding sequences, and automated data hygiene.</td>
          </tr>
          <tr>
            <td><strong>Software & Cloud Development</strong></td>
            <td>Full-stack architectures using Python (FastAPI, Django), Node.js/TypeScript, React/Next.js, PostgreSQL, Docker containerization, AWS (ECS, Lambda, RDS, S3), and automated GitHub Actions CI/CD.</td>
            <td>Bespoke client web portals, internal admin dashboards, microservices, and SaaS extension backends engineered for 99.9% uptime.</td>
          </tr>
          <tr>
            <td><strong>Security & Data Protection</strong></td>
            <td>OAuth 2.0 / JWT authentication, Role-Based Access Control (RBAC), end-to-end encryption in transit (TLS 1.3) and at rest (AES-256), OWASP compliance, and zero PII retention policies for AI prompts.</td>
            <td>HIPAA/GDPR-conscious client solutions, enterprise single sign-on (SSO), secure client data silos, and prompt injection defense barriers.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 4: Visual Architecture Component -->
    <div class="section">
      <div class="section-title">
        4. End-to-End Solution Architecture
        <span class="tagline">How We Architect Client AI & Automated Integration Pipelines</span>
      </div>

      <div class="pipeline-flow">
        <div class="pipeline-col">
          <div>
            <span class="pipeline-badge">Stage 01: Ingestion & Trigger</span>
            <div class="pipeline-title">Data Influx & Webhooks</div>
            <p class="pipeline-p">
              Capturing incoming events from client CRMs, forms, or cloud storage folders (PDFs, docs, tables) with payload signature verification and schema validation.
            </p>
          </div>
        </div>

        <div class="pipeline-arrow">➔</div>

        <div class="pipeline-col accent">
          <div>
            <span class="pipeline-badge">Stage 02: Processing & AI</span>
            <div class="pipeline-title">Workflow & Agent Engine</div>
            <ul class="pipeline-bullets">
              <li><strong>Orchestration:</strong> Multi-branch logic in <code>n8n</code> or custom <code>FastAPI</code>.</li>
              <li><strong>RAG & Context:</strong> Vector retrieval from <code>pgvector</code> / <code>Pinecone</code>.</li>
              <li><strong>Agent Execution:</strong> Task execution via tool calling and LLM reasoning.</li>
              <li><strong>Guardrails:</strong> Output formatting, prompt injection defense, and sanitization.</li>
            </ul>
          </div>
        </div>

        <div class="pipeline-arrow">➔</div>

        <div class="pipeline-col">
          <div>
            <span class="pipeline-badge">Stage 03: Delivery & Sync</span>
            <div class="pipeline-title">Destination & Auditing</div>
            <p class="pipeline-p">
              Writing enriched records back to client CRMs/ERPs, triggering marketing workflows, alerting team channels, and archiving audit trails for compliance.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 5: Marketing & Digital Automation Specialization -->
    <div class="section">
      <div class="section-title">
        5. Supporting IMM’s Digital Marketing Domain
        <span class="tagline">Enhancing Client Retention and Campaign ROI Through Automation</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Lead Nurturing & Scoring</span>
            <span class="card-badge">Conversion</span>
          </div>
          <p class="card-p">
            Automating multi-touch lead scoring using behavioral signals and AI summarization, alerting sales reps in real time when high-value prospects engage.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Attribution & Reporting Sync</span>
            <span class="card-badge">Analytics</span>
          </div>
          <p class="card-p">
            Pulling ad metrics, web analytics, and CRM deal closures into unified BigQuery/PostgreSQL dashboards to give IMM clients crystal-clear ROAS proof.
          </p>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Dynamic Content Personalization</span>
            <span class="card-badge">AI Marketing</span>
          </div>
          <p class="card-p">
            Using AI models to generate industry-tailored email copy variations and landing page content dynamically, increasing campaign open and click rates.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>IMM Technical Partnership Proposal • AI Development & Systems Integration</span>
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
        <div class="brand-title">Collaboration Model & Quality Standards <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Client-Facing Discovery Protocols, Agile Delivery, and Enterprise Development Etiquette</div>
      </div>
      <div class="meta-block">
        <strong>Communication:</strong> Slack, Teams, Zoom, Loom, ClickUp, Jira<br>
        <strong>Delivery:</strong> 2-Week Sprints, Staging Envs, Automated Tests<br>
        <strong>Timezone:</strong> Overlapping US Business Hours (EST / CST)
      </div>
    </div>

    <!-- Section 6: Client Discovery & White-Label Protocol -->
    <div class="section">
      <div class="section-title">
        6. Client Discovery & White-Label Collaboration Protocol
        <span class="tagline">Seamless Collaboration Between IMM Leadership and Our Technical Team</span>
      </div>
      <div class="grid-2">
        <div class="card highlight">
          <div class="card-header">
            <span class="card-title">Client-Facing Technical Lead Protocols</span>
            <span class="card-badge">Discovery Co-Pilot</span>
          </div>
          <p class="card-p">
            When IMM requires technical presence on client discovery calls, our Technical Lead steps in with complete professionalism:
          </p>
          <ul class="card-bullets">
            <li><strong>Representing IMM:</strong> We participate under IMM’s brand identity (e.g. using IMM email alias, Zoom backgrounds, and communication channels).</li>
            <li><strong>Translating Needs to Architecture:</strong> Actively listening to non-technical client requirements, validating integration feasibility, and proposing phased roadmaps.</li>
            <li><strong>Scoping & Architecture Documents:</strong> Producing rapid Architecture Decision Records (ADRs), system topology diagrams, and scoped sprint deliverables within 24 hours of discovery calls.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Daily Communication & Accountability</span>
            <span class="card-badge">Zero Friction</span>
          </div>
          <p class="card-p">
            You will never be left wondering about task status or upcoming blockers. We prioritize radical transparency:
          </p>
          <ul class="card-bullets">
            <li><strong>Async Standups & Loom Demos:</strong> Daily written progress summaries in Slack/Teams and 3-minute video walkthroughs of newly built features and automations.</li>
            <li><strong>Real-Time Collaboration:</strong> Immediate availability during US core working hours for technical syncs, code reviews, or urgent troubleshooting.</li>
            <li><strong>Versioned Documentation:</strong> Comprehensive technical runbooks, API contracts, schema definitions, and credentials stored securely in 1Password.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Section 7: Software Engineering & QA Lifecycle -->
    <div class="section">
      <div class="section-title">
        7. Development Lifecycle & Quality Assurance
        <span class="tagline">Building Scalable, Maintainable Systems from Day One</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Git & CI/CD Pipelines</span>
            <span class="card-badge">Automated Delivery</span>
          </div>
          <p class="card-p">
            Strict Git branching models (main, staging, feature branches) with GitHub Actions automating linting, static code analysis, and unit test suites before any pull request is merged.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Isolated Staging Envs</span>
            <span class="card-badge">Zero Production Risk</span>
          </div>
          <p class="card-p">
            Every client integration is built and thoroughly stress-tested in dedicated staging sandboxes with mock API payloads before promoting to live production environments.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Regression & Error Handling</span>
            <span class="card-badge">Self-Healing</span>
          </div>
          <p class="card-p">
            Automated retry mechanisms with exponential backoff for external API timeouts, dead-letter queues (DLQs) for failed webhook payloads, and instant alerts via Sentry.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 8: Security & Responsible AI Framework -->
    <div class="section">
      <div class="section-title">
        8. Security, Data Privacy & Responsible AI Framework
        <span class="tagline">Protecting IMM and Your Clients from Vulnerabilities and Data Leaks</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Zero PII Retention</span>
            <span class="card-badge">Privacy First</span>
          </div>
          <p class="card-p">
            Configuring commercial LLM endpoints with Zero Data Retention (ZDR) agreements. Client intellectual property and customer PII are never used to train external models.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Access Control & RBAC</span>
            <span class="card-badge">Principle of Least Privilege</span>
          </div>
          <p class="card-p">
            Fine-grained role-based permissions, scoped API keys with time-to-live restrictions, multi-factor authentication, and encrypted environment secret managers.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Prompt Injection Defense</span>
            <span class="card-badge">AI Safety</span>
          </div>
          <p class="card-p">
            Implementing dual-layer prompt guardrails, semantic input sanitization, and output schema enforcement (JSON Schema / Pydantic) to prevent prompt injection and system jailbreaks.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>IMM Technical Partnership Proposal • AI Development & Systems Integration</span>
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
        <div class="brand-title">Maintenance SLAs, Engagement & Team <span class="brand-badge">Long-Term Growth</span></div>
        <div class="brand-sub">Incident Severity Matrix, Dedicated Support Window, and Commercial Framework</div>
      </div>
      <div class="meta-block">
        <strong>Support Hours:</strong> 8+ Hours Daily US Coverage<br>
        <strong>P1 SLA:</strong> < 1-Hour Response Target<br>
        <strong>Engagement:</strong> Flexible PoC ➔ Dedicated Retainer
      </div>
    </div>

    <!-- Section 9: Maintenance & Support SLA Matrix -->
    <div class="section">
      <div class="section-title">
        9. Maintenance & Support SLA Matrix
        <span class="tagline">Guaranteed Response Times and Incident Escalation Hierarchy</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 14%;">Severity</th>
            <th style="width: 28%;">Incident Definition</th>
            <th style="width: 18%;">Response SLA</th>
            <th style="width: 20%;">Target Resolution</th>
            <th style="width: 20%;">Escalation Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="sla-badge sla-crit">P1 - Critical</span></td>
            <td>Complete production outage, payment gateway failure, critical data sync interruption affecting clients.</td>
            <td><strong>&lt; 1 Hour</strong></td>
            <td>&lt; 4 Hours or immediate rollback</td>
            <td>Immediate hot-page to Technical Lead & on-call engineer; client bridge opened.</td>
          </tr>
          <tr>
            <td><span class="sla-badge sla-high">P2 - High</span></td>
            <td>Core integration or AI workflow impaired with workaround available; degraded performance.</td>
            <td><strong>&lt; 2 Hours</strong></td>
            <td>Same business day (&lt; 8 Hours)</td>
            <td>Direct assignment to senior builder; daily progress reports to IMM manager.</td>
          </tr>
          <tr>
            <td><span class="sla-badge sla-med">P3 - Medium</span></td>
            <td>Minor functional bug, edge-case automation failure, UI display glitch not impeding revenue.</td>
            <td><strong>&lt; 4 Hours</strong></td>
            <td>Within 24–48 Hours</td>
            <td>Queued in active sprint backlog; resolved in next deployment cycle.</td>
          </tr>
          <tr>
            <td><span class="sla-badge sla-low">P4 - Low</span></td>
            <td>Feature enhancements, copy updates, non-critical technical maintenance, dependency bumps.</td>
            <td><strong>&lt; 1 Business Day</strong></td>
            <td>Scheduled Sprint Cycle</td>
            <td>Estimated during bi-weekly sprint planning session.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Section 10: Engagement Models -->
    <div class="section">
      <div class="section-title">
        10. Flexible Engagement & Partnership Models
        <span class="tagline">Designed to Start Lean and Scale Predictably as IMM Expands</span>
      </div>
      <div class="grid-3">
        <div class="card highlight">
          <div class="card-header">
            <span class="card-title">1. Paid Proof of Concept</span>
            <span class="card-badge">Lowest Risk</span>
          </div>
          <p class="card-p"><strong>Scope:</strong> Single AI agent, targeted API integration, or n8n automation workflow.</p>
          <p class="card-p"><strong>Structure:</strong> Fixed-price or milestone-based pilot.</p>
          <p class="card-p"><strong>Goal:</strong> Validate turnaround speed, architectural depth, and client communication firsthand.</p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">2. Dedicated Retainer</span>
            <span class="card-badge">Agency Partner</span>
          </div>
          <p class="card-p"><strong>Scope:</strong> Dedicated monthly engineering hours allocated across IMM's client projects.</p>
          <p class="card-p"><strong>Structure:</strong> Predictable monthly retainer with guaranteed team availability.</p>
          <p class="card-p"><strong>Goal:</strong> Acts as IMM’s internal engineering wing with priority queue and rapid turnaround.</p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">3. Project-Based Sprints</span>
            <span class="card-badge">On-Demand</span>
          </div>
          <p class="card-p"><strong>Scope:</strong> Large custom client platforms, end-to-end AI portals, or multi-system overhauls.</p>
          <p class="card-p"><strong>Structure:</strong> Milestone deliverables with defined acceptance criteria and warranty period.</p>
          <p class="card-p"><strong>Goal:</strong> Flexible scaling for surge client demand without fixed agency overhead.</p>
        </div>
      </div>
    </div>

    <!-- Section 11: Core Technical Team Profiles -->
    <div class="section">
      <div class="section-title">
        11. Dedicated Senior Engineering Team
        <span class="tagline">Full Resumes Attached in Proposal Package</span>
      </div>
      <div class="grid-3">
        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Viranga Lakshan</span>
            <span class="profile-role">Lead Solutions Architect</span>
          </div>
          <p class="card-p">
            <strong>Role for IMM:</strong> Technical Lead & client-facing solutions engineer. Fluent English speaker leading client discovery, system architecture, AI pipeline design, and security governance.
          </p>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Janith Kavishka</span>
            <span class="profile-role">Sr. Automation & Integration Eng.</span>
          </div>
          <p class="card-p">
            <strong>Role for IMM:</strong> Workflow automation and API specialist. Expert in n8n, Make, Zapier, Python FastAPI, webhook architectures, and bidirectional CRM/ERP synchronization.
          </p>
        </div>

        <div class="profile-box">
          <div class="profile-header">
            <span class="profile-name">Lithumitha Ravikumar</span>
            <span class="profile-role">Sr. Software & Data Engineer</span>
          </div>
          <p class="card-p">
            <strong>Role for IMM:</strong> Full-stack, database, and RAG engineer. Specialized in vector databases (Pinecone, pgvector), PostgreSQL tuning, Docker, and AWS/GCP cloud deployments.
          </p>
        </div>
      </div>
    </div>

    <!-- Section 12: Next Steps & Immediate Action -->
    <div class="callout-box">
      <div class="callout-title">Suggested Next Step: 30-Minute Architecture & Partnership Alignment Call</div>
      <div class="callout-text">
        We would be delighted to connect for a 30-minute introductory call to review IMM’s current client commitments, upcoming AI/integration needs, and identify a candidate pilot project to demonstrate our engineering velocity. We are available to start immediately.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>IMM Technical Partnership Proposal • AI Development & Systems Integration</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\IMM_AI_Development_Integration_Agency"
    html_path = os.path.join(base_dir, "proposal.html")
    pdf_path = os.path.join(base_dir, "IMM_AI_Development_Integration_Partnership_Proposal.pdf")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"HTML written to {html_path}")

    msedge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    msedge_bin = None
    for p in msedge_paths:
        if os.path.exists(p):
            msedge_bin = p
            break

    if not msedge_bin:
        raise FileNotFoundError("Microsoft Edge executable not found.")

    cmd = [
        msedge_bin,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]

    subprocess.run(cmd, check=True)
    print(f"PDF generated at {pdf_path}")

    # Verify page count and render PNGs
    pdf = pdfium.PdfDocument(pdf_path)
    total_pages = len(pdf)
    print(f"Total page count: {total_pages}")

    for i in range(total_pages):
        page = pdf[i]
        image = page.render(scale=2.0).to_pil()
        preview_path = os.path.join(base_dir, f"page_{i+1}.png")
        image.save(preview_path)
        print(f"Rendered page {i+1} to {preview_path}")

    success = (total_pages == 4)
    print(f"Success: {success}")
    return success

if __name__ == "__main__":
    generate_pdf()
