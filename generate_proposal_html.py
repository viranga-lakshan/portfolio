html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upwork Proposal - Zangi Client Development - Viranga Lakshan</title>
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
      line-height: 1.45;
      font-size: 11.5px;
    }

    .page {
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      overflow: hidden;
      position: relative;
      background: #ffffff;
      padding: 16mm 18mm 14mm 18mm;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    /* Top Accent Line */
    .top-gradient-bar {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 6px;
      background: linear-gradient(90deg, #2563eb, #06b6d4, #6366f1, #3b82f6);
    }

    /* Header section */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1.5px solid #e2e8f0;
      margin-bottom: 14px;
    }

    .author-info h1 {
      font-size: 22px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .author-info .title {
      font-size: 12px;
      font-weight: 600;
      color: #2563eb;
      margin-top: 2px;
    }

    .contact-chips {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 4px;
      font-size: 10px;
      color: #475569;
    }

    .contact-item {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .contact-item a {
      color: #0284c7;
      text-decoration: none;
      font-weight: 500;
    }

    /* Hero / Project Banner */
    .hero-banner {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #1e293b 100%);
      color: #ffffff;
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 14px;
      position: relative;
      box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
    }

    .hero-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }

    .badge-client {
      background: rgba(6, 182, 212, 0.2);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-exp {
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(52, 211, 153, 0.4);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    .hero-title {
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #ffffff;
      margin-bottom: 6px;
    }

    .hero-desc {
      font-size: 10.5px;
      color: #cbd5e1;
      line-height: 1.5;
    }

    /* Metric cards */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 14px;
    }

    .metric-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      border-top: 3px solid #2563eb;
    }

    .metric-card:nth-child(2) { border-top-color: #06b6d4; }
    .metric-card:nth-child(3) { border-top-color: #10b981; }
    .metric-card:nth-child(4) { border-top-color: #8b5cf6; }

    .metric-value {
      font-size: 16px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    .metric-label {
      font-size: 9.5px;
      font-weight: 600;
      color: #64748b;
      margin-top: 2px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    /* Section Styles */
    .section-title {
      font-size: 13px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      letter-spacing: -0.2px;
    }

    .section-title svg {
      color: #2563eb;
      width: 16px;
      height: 16px;
    }

    .card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    /* Fit grid */
    .fit-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }

    .fit-item {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 12px;
    }

    .fit-header {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 4px;
    }

    .fit-icon-bullet {
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #eff6ff;
      color: #2563eb;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      font-weight: 800;
      flex-shrink: 0;
    }

    .fit-desc {
      font-size: 10px;
      color: #475569;
      line-height: 1.45;
    }

    /* Alignment Table */
    .table-container {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 10px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 10px;
    }

    th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      text-align: left;
      padding: 7px 10px;
      border-bottom: 1px solid #cbd5e1;
      font-size: 9.5px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    td {
      padding: 7px 10px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
      vertical-align: top;
      line-height: 1.4;
    }

    tr:last-child td {
      border-bottom: none;
    }

    .td-req {
      font-weight: 600;
      color: #0f172a;
      width: 32%;
    }

    .td-solution {
      width: 68%;
    }

    .tag {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 8.5px;
      font-weight: 600;
      margin-right: 4px;
      margin-bottom: 2px;
    }

    .tag-blue { background: #dbeafe; color: #1e40af; }
    .tag-cyan { background: #cffafe; color: #0e7490; }
    .tag-emerald { background: #d1fae5; color: #065f46; }
    .tag-purple { background: #ede9fe; color: #5b21b6; }

    /* Timeline / Phases */
    .phases-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }

    .phase-card {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 12px;
      background: #ffffff;
      position: relative;
      border-left: 3.5px solid #2563eb;
    }

    .phase-card:nth-child(2) { border-left-color: #06b6d4; }
    .phase-card:nth-child(3) { border-left-color: #10b981; }
    .phase-card:nth-child(4) { border-left-color: #8b5cf6; }

    .phase-badge {
      display: inline-block;
      font-size: 8.5px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 6px;
      border-radius: 4px;
      margin-bottom: 4px;
    }

    .phase-1 .phase-badge { background: #eff6ff; color: #1e40af; }
    .phase-2 .phase-badge { background: #ecfeff; color: #0e7490; }
    .phase-3 .phase-badge { background: #ecfdf5; color: #065f46; }
    .phase-4 .phase-badge { background: #f5f3ff; color: #5b21b6; }

    .phase-title {
      font-size: 11px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 4px;
    }

    .phase-list {
      list-style: none;
      font-size: 9.5px;
      color: #475569;
    }

    .phase-list li {
      position: relative;
      padding-left: 12px;
      margin-bottom: 3px;
      line-height: 1.35;
    }

    .phase-list li::before {
      content: "•";
      position: absolute;
      left: 0;
      color: #2563eb;
      font-weight: bold;
    }

    /* Deep dive banner */
    .deep-dive-box {
      background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
      border: 1px solid #bfdbfe;
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 12px;
    }

    .deep-dive-title {
      font-size: 11.5px;
      font-weight: 700;
      color: #1e3a8a;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
    }

    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }

    .pillar-item {
      background: #ffffff;
      border: 1px solid #dbeafe;
      border-radius: 6px;
      padding: 8px 10px;
    }

    .pillar-name {
      font-size: 10px;
      font-weight: 700;
      color: #1d4ed8;
      margin-bottom: 3px;
    }

    .pillar-text {
      font-size: 9px;
      color: #475569;
      line-height: 1.35;
    }

    /* Projects Showcase */
    .project-card {
      border: 1px solid #e2e8f0;
      border-radius: 9px;
      padding: 11px 13px;
      margin-bottom: 10px;
      background: #ffffff;
      transition: all 0.2s ease;
    }

    .project-card:last-child {
      margin-bottom: 0;
    }

    .project-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 5px;
    }

    .project-name {
      font-size: 11.5px;
      font-weight: 700;
      color: #0f172a;
    }

    .project-client {
      font-size: 9.5px;
      font-weight: 600;
      color: #2563eb;
      background: #eff6ff;
      padding: 2px 7px;
      border-radius: 4px;
    }

    .project-summary {
      font-size: 10px;
      color: #334155;
      line-height: 1.4;
      margin-bottom: 6px;
    }

    .project-bullets {
      list-style: none;
      font-size: 9.5px;
      color: #475569;
      margin-bottom: 6px;
    }

    .project-bullets li {
      position: relative;
      padding-left: 13px;
      margin-bottom: 3px;
      line-height: 1.35;
    }

    .project-bullets li::before {
      content: "✓";
      position: absolute;
      left: 0;
      color: #059669;
      font-weight: bold;
      font-size: 9px;
    }

    .project-tech {
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      padding-top: 4px;
      border-top: 1px dashed #f1f5f9;
    }

    /* Skills Grid */
    .skills-matrix {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 12px;
    }

    .skill-category {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 8px 10px;
    }

    .skill-cat-title {
      font-size: 9.5px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 2px;
    }

    .skill-cat-items {
      font-size: 9.5px;
      color: #475569;
      line-height: 1.4;
    }

    /* Callout & Availability */
    .cta-box {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
      color: #ffffff;
      border-radius: 10px;
      padding: 13px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .cta-content h3 {
      font-size: 13px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 2px;
    }

    .cta-content p {
      font-size: 10px;
      color: #93c5fd;
    }

    .cta-badge {
      background: #10b981;
      color: #ffffff;
      font-weight: 700;
      font-size: 10.5px;
      padding: 6px 12px;
      border-radius: 6px;
      box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
      white-space: nowrap;
    }

    /* Footer */
    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      border-top: 1px solid #e2e8f0;
      font-size: 9px;
      color: #94a3b8;
    }

    .footer-left {
      display: flex;
      gap: 12px;
    }

    .page-number {
      font-weight: 700;
      color: #2563eb;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Header -->
      <div class="header">
        <div class="author-info">
          <h1>VIRANGA LAKSHAN</h1>
          <div class="title">Full Stack Engineer & Client Solutions Specialist · 4+ Years Enterprise Experience</div>
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

      <!-- Hero Proposal Banner -->
      <div class="hero-banner">
        <div class="hero-meta">
          <span class="badge-client">Upwork Proposal</span>
          <span class="badge-exp">✓ 4 Years Industry Enterprise Experience</span>
        </div>
        <div class="hero-title">Technical Proposal: Zangi Client Development & Reliable Messaging Solution</div>
        <div class="hero-desc">
          A dedicated, end-to-end engineering proposal to build, configure, and integrate your custom <strong>Zangi Business Client</strong>. Engineered for flawless real-time messaging, zero message loss over unstable networks, robust encryption standards, and on-time independent delivery.
        </div>
      </div>

      <!-- Metric Highlights -->
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">4+ Years</div>
          <div class="metric-label">Industry Experience</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Enterprise</div>
          <div class="metric-label">Big Company Products</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">99.9% Uptime</div>
          <div class="metric-label">Reliable Architectures</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">35-40 hrs/wk</div>
          <div class="metric-label">Immediate Availability</div>
        </div>
      </div>

      <!-- Executive Overview -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Executive Summary & Proven Track Record
      </div>
      <div class="card" style="margin-bottom: 12px; font-size: 10.5px; line-height: 1.5; color: #334155;">
        Through my <strong>4 years of industry software development experience</strong> working at top technology firms including <strong>Arimac Lanka</strong> and <strong>SLT Digital Lab</strong>, I have engineered mission-critical products for high-profile international corporations across Kuwait, UAE, and Sri Lanka (including <em>Adrik Kuwait</em>, <em>DIMO Lanka</em>, <em>Al Ain Cultural Entity UAE</em>, and <em>Holsten Arabia</em>).<br><br>
        Building a stable, secure <strong>Zangi business client</strong> requires a deep understanding of client-side architecture, real-time message state synchronization, low-latency socket management, push notification wakeups, and cryptographic integrity. Having built distributed microservices, streaming event pipelines (Kafka/Redis), push notification infrastructures (OneSignal/SMS), and responsive client interfaces (React/Next.js/TypeScript), I have the proven background to deliver an enterprise-grade client solution autonomously and on schedule.
      </div>

      <!-- Why I Am The Right Fit -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        Core Strengths Aligned with Your Project
      </div>
      <div class="fit-grid">
        <div class="fit-item">
          <div class="fit-header">
            <span class="fit-icon-bullet">1</span>
            <span>Client-Side & UI Engineering</span>
          </div>
          <div class="fit-desc">
            Extensive experience crafting modular, bug-free client applications in TypeScript, React, Next.js, and modern state architectures (Zustand, Redux). Fast rendering and smooth user experiences.
          </div>
        </div>
        <div class="fit-item">
          <div class="fit-header">
            <span class="fit-icon-bullet">2</span>
            <span>Real-Time Messaging & Sockets</span>
          </div>
          <div class="fit-desc">
            Hands-on integration of real-time bidirectional communication, event orchestration, WebSockets, OneSignal push services, and Kafka streams with zero dropped payloads.
          </div>
        </div>
        <div class="fit-item">
          <div class="fit-header">
            <span class="fit-icon-bullet">3</span>
            <span>Reliable Low-Bandwidth Sync</span>
          </div>
          <div class="fit-desc">
            Built resilient offline-first message queueing, optimistic local UI updates, automatic reconnect backoff algorithms, and state reconciliation designed for unstable network conditions.
          </div>
        </div>
        <div class="fit-item">
          <div class="fit-header">
            <span class="fit-icon-bullet">4</span>
            <span>Enterprise Security & Auth</span>
          </div>
          <div class="fit-desc">
            Proven mastery of Keycloak (OAuth2/OIDC), JWT tokens, encrypted payload handling, device API keys, and adherence to strict private messaging security protocols.
          </div>
        </div>
      </div>

      <!-- Alignment Table -->
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th class="td-req">Your Project Requirements</th>
              <th class="td-solution">My Demonstrated Solution & Delivery Approach</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="td-req">Zangi Client Setup & Configuration</td>
              <td class="td-solution">Configure the Zangi client SDK/white-label ecosystem with your business branding, cluster endpoints, security keys, and environment-driven configurations.</td>
            </tr>
            <tr>
              <td class="td-req">Messaging Functionality Integration</td>
              <td class="td-solution">Implement direct 1-to-1 chat, group conversations, media attachments (images/documents/audio), delivered/read status receipts, and message history caching.</td>
            </tr>
            <tr>
              <td class="td-req">Reliable Communication & Network Resilience</td>
              <td class="td-solution">Heartbeat monitor, exponential backoff reconnection, local SQLite/IndexedDB queueing to guarantee delivery when network recovers, and FCM/APNs push triggers.</td>
            </tr>
            <tr>
              <td class="td-req">Independent Execution & Timely Delivery</td>
              <td class="td-solution">Full ownership: daily Git commits, transparent milestone demonstrations, clean documentation, and proactive communication without requiring micromanagement.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Viranga Lakshan · Software Engineer</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Zangi Client Development Proposal</div>
      <div class="page-number">Page 1 of 3</div>
    </div>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Section: Technical Roadmap -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
        Implementation Roadmap: 4-Phase Delivery Plan
      </div>

      <div class="phases-grid">
        <div class="phase-card phase-1">
          <span class="phase-badge">Phase 01 · Setup & Discovery</span>
          <div class="phase-title">Environment Setup & Architecture Design</div>
          <ul class="phase-list">
            <li>Analyze business functional specifications & target client environments.</li>
            <li>Initialize Zangi SDK / client codebase with secure credentials & cluster configs.</li>
            <li>Establish clean architecture: state management, local database, and API layers.</li>
            <li>Deliverable: Configured client repository, automated build pipeline, and auth test.</li>
          </ul>
        </div>

        <div class="phase-card phase-2">
          <span class="phase-badge">Phase 02 · Core Features</span>
          <div class="phase-title">Full Messaging Feature Integration</div>
          <ul class="phase-list">
            <li>Implement real-time 1-on-1 and multi-party group messaging channels.</li>
            <li>Integrate full message status lifecycle (Pending ➔ Sent ➔ Delivered ➔ Read).</li>
            <li>Develop media attachment handling (compression, upload, encrypted transmission).</li>
            <li>Deliverable: Functional messaging client with real-time bidirectional delivery.</li>
          </ul>
        </div>

        <div class="phase-card phase-3">
          <span class="phase-badge">Phase 03 · Reliability & Resilience</span>
          <div class="phase-title">Low-Bandwidth & Network Stability Engine</div>
          <ul class="phase-list">
            <li>Implement automated socket heartbeat with smart reconnect backoff logic.</li>
            <li>Offline message spooling: queue outgoing messages locally until connection resumes.</li>
            <li>Push notification integration (FCM/APNs/OneSignal) for background wakeups.</li>
            <li>Deliverable: Fault-tolerant communication resilient against 2G, Wi-Fi drops & handoffs.</li>
          </ul>
        </div>

        <div class="phase-card phase-4">
          <span class="phase-badge">Phase 04 · Hardening & Launch</span>
          <div class="phase-title">Security Audit, QA & Final Handover</div>
          <ul class="phase-list">
            <li>End-to-end stress testing under packet loss and poor latency conditions.</li>
            <li>Cryptographic verification and session token renewal safeguards.</li>
            <li>Comprehensive developer handover documentation & deployment walkthrough.</li>
            <li>Deliverable: Stable production-ready client, complete source code & post-launch support.</li>
          </ul>
        </div>
      </div>

      <!-- Deep Dive: Communication Reliability -->
      <div class="deep-dive-box">
        <div class="deep-dive-title">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          Technical Deep-Dive: How I Guarantee Unbreakable Communication
        </div>
        <div class="pillars-grid">
          <div class="pillar-item">
            <div class="pillar-name">1. Adaptive Reconnect Algorithm</div>
            <div class="pillar-text">
              Jittered exponential backoff prevents server connection storms while swiftly re-establishing sessions the instant cellular or Wi-Fi reconnects.
            </div>
          </div>
          <div class="pillar-item">
            <div class="pillar-name">2. Persistent Local Message Spool</div>
            <div class="pillar-text">
              Every message is persisted locally with unique client GUIDs before dispatch. If the socket drops mid-flight, deduplication prevents duplicate deliveries.
            </div>
          </div>
          <div class="pillar-item">
            <div class="pillar-name">3. Background Push Sync</div>
            <div class="pillar-text">
              Silent background push payloads trigger synchronization even when the app is minimized, ensuring instant notification and up-to-date inboxes upon opening.
            </div>
          </div>
        </div>
      </div>

      <!-- Work Availability & Terms -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        Availability, Communication & Working Style
      </div>
      <div class="card" style="margin-bottom: 0;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 10px;">
          <div>
            <div style="font-weight: 700; color: #0f172a; margin-bottom: 3px;">⏰ Project Availability</div>
            <p style="color: #475569; line-height: 1.45;">
              • <strong>Immediate Kickoff:</strong> Ready to begin within 24 hours of onboarding.<br>
              • <strong>Capacity:</strong> 35 – 40 hours per week dedicated to your project.<br>
              • <strong>Time Zone Overlap:</strong> Flexible scheduling to accommodate European, US, or Asian business hours for daily syncs.
            </p>
          </div>
          <div>
            <div style="font-weight: 700; color: #0f172a; margin-bottom: 3px;">💬 Communication & Reporting</div>
            <p style="color: #475569; line-height: 1.45;">
              • <strong>Daily Standup Reports:</strong> Clear breakdown of completed tasks, blockers, and next targets.<br>
              • <strong>Real-Time Responsiveness:</strong> Fast turnaround via Slack, Teams, or Upwork Messages.<br>
              • <strong>Clean Version Control:</strong> Semantic Git commits and feature PRs for transparent auditing.
            </p>
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
      <div>Zangi Client Development Proposal</div>
      <div class="page-number">Page 2 of 3</div>
    </div>
  </div>

  <!-- ==================== PAGE 3 ==================== -->
  <div class="page">
    <div class="top-gradient-bar"></div>

    <div class="page-content">
      <!-- Section: Relevant Projects from CV -->
      <div class="section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
        Relevant Project Experience from My CV (Enterprise & Big Companies)
      </div>

      <!-- Project 1: Adrik Media -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Adrik News & Media Platform</span>
            <span style="font-size: 9px; color: #64748b; margin-left: 6px;">(Bilingual Web, Mobile & Admin Ecosystem)</span>
          </div>
          <span class="project-client">Arimac Digital · Client: Adrik (Kuwait)</span>
        </div>
        <div class="project-summary">
          Engineered high-concurrency Node.js BFF microservices orchestrating communications between web, iOS/Android mobile applications, and admin consoles for a major Kuwait media enterprise.
        </div>
        <ul class="project-bullets">
          <li>Integrated <strong>OneSignal push notifications</strong> and <strong>SMS delivery gateway</strong> for instant breaking news alerts and real-time user communications.</li>
          <li>Built secure user authentication and session management using <strong>Keycloak (OAuth2/OIDC, JWT)</strong> with token refresh workflows and protected route guards.</li>
          <li>Containerized services with Docker and deployed to Kubernetes clusters via GitLab CI/CD pipelines, guaranteeing 99.9% uptime.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Node.js</span>
          <span class="tag tag-blue">Express.js</span>
          <span class="tag tag-cyan">OneSignal Push</span>
          <span class="tag tag-cyan">SMS Gateway</span>
          <span class="tag tag-purple">Keycloak / JWT</span>
          <span class="tag tag-emerald">Docker / Kubernetes</span>
        </div>
      </div>

      <!-- Project 2: TukTuk GPS Tracking -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">Police Tuk-Tuk Real-Time GPS Tracking API</span>
            <span style="font-size: 9px; color: #64748b; margin-left: 6px;">(High-Throughput Telemetry System)</span>
          </div>
          <span class="project-client">Production IoT & Telemetry Platform</span>
        </div>
        <div class="project-summary">
          Engineered high-frequency, fault-tolerant telemetry communication system for real-time fleet GPS tracking with sub-second transmission and dual-layer security.
        </div>
        <ul class="project-bullets">
          <li>Architected event streaming pipelines using <strong>Kafka</strong> and <strong>Redis caching</strong> to ingest and broadcast high-speed real-time data packets without drops.</li>
          <li>Enforced dual-layer authentication (JWT for operators + hardware device API keys) and geographic RBAC across 28+ secure endpoints.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Java 21</span>
          <span class="tag tag-blue">Spring Boot 3</span>
          <span class="tag tag-purple">Kafka Streaming</span>
          <span class="tag tag-purple">Redis</span>
          <span class="tag tag-emerald">Dual Auth / Security</span>
        </div>
      </div>

      <!-- Project 3: DIMO Lanka -->
      <div class="project-card">
        <div class="project-header">
          <div>
            <span class="project-name">DIMO Enterprise Gate Pass & Dispatch Management System</span>
          </div>
          <span class="project-client">Arimac Digital · Client: DIMO Lanka</span>
        </div>
        <div class="project-summary">
          Developed mission-critical microservices architecture managing vehicle dispatch, gate-pass tracking, and automated enterprise approval workflows for a leading conglomerate.
        </div>
        <ul class="project-bullets">
          <li>Developed API gateway handling <strong>Kafka-based audit event publishing</strong> and mission-critical external integrations with SAP and Azure AD.</li>
          <li>Implemented secure file/media handling pipelines with automated virus scanning, S3 storage, and high-availability database schema migrations.</li>
        </ul>
        <div class="project-tech">
          <span class="tag tag-blue">Spring Boot</span>
          <span class="tag tag-cyan">Kafka Events</span>
          <span class="tag tag-purple">SAP / Azure AD</span>
          <span class="tag tag-emerald">Docker CI/CD</span>
        </div>
      </div>

      <!-- Skills Matrix -->
      <div class="section-title" style="margin-top: 10px;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
        Technical Competencies Relevant to Zangi Client
      </div>
      <div class="skills-matrix">
        <div class="skill-category">
          <div class="skill-cat-title">Client-Side & Frontend</div>
          <div class="skill-cat-items">React.js, Next.js, TypeScript, JavaScript (ES6+), Zustand, Redux Toolkit, Tailwind CSS, Responsive UX</div>
        </div>
        <div class="skill-category">
          <div class="skill-cat-title">Messaging & Real-Time</div>
          <div class="skill-cat-items">WebSockets, Socket.io, Push Notifications (FCM / OneSignal), Kafka, Redis Pub/Sub, REST APIs, JSON-RPC</div>
        </div>
        <div class="skill-category">
          <div class="skill-cat-title">Security & Protocols</div>
          <div class="skill-cat-items">OAuth2/OIDC, Keycloak, JWT Auth, End-to-End Encryption Concepts, HTTPS/WSS, Local Encrypted Storage</div>
        </div>
      </div>

      <!-- CTA Box -->
      <div class="cta-box">
        <div class="cta-content">
          <h3>Ready to Kick Off Your Zangi Client Project</h3>
          <p>Available for an introductory discovery call or immediate onboarding on Upwork.</p>
        </div>
        <div class="cta-badge">⚡ Available Immediately (35-40h/wk)</div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-left">
        <span>Viranga Lakshan · Software Engineer</span>
        <span>virangalakshanz@gmail.com</span>
      </div>
      <div>Zangi Client Development Proposal</div>
      <div class="page-number">Page 3 of 3</div>
    </div>
  </div>

</body>
</html>
'''\nwith open('Viranga_Lakshan_Zangi_Client_Proposal.html', 'w', encoding='utf-8') as out:\n    out.write(html)\n