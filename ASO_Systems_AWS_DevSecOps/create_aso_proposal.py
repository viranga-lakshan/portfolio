import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AWS DevSecOps Engineering & Cloud Security Proposal - ASO Systems</title>
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
    font-size: 8.8pt;
    line-height: 1.42;
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
    border-bottom: 2px solid #0284c7;
    padding-bottom: 8px;
    margin-bottom: 12px;
  }
  .brand-title {
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-badge {
    background: #0284c7;
    color: #ffffff;
    font-size: 7.5pt;
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
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0369a1 100%);
    color: #ffffff;
    border-radius: 6px;
    padding: 12px 14px;
    margin-bottom: 12px;
  }
  .hero-title {
    font-size: 12.5pt;
    font-weight: 800;
    letter-spacing: -0.3px;
    margin: 0 0 4px 0;
    color: #ffffff;
  }
  .hero-desc {
    font-size: 8.3pt;
    color: #e2e8f0;
    margin: 0 0 10px 0;
    line-height: 1.4;
  }
  .hero-pills {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
  }
  .hero-pill {
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.22);
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 7.4pt;
    font-weight: 600;
    color: #f8fafc;
  }
  .hero-pill strong {
    color: #38bdf8;
  }

  /* Section Styling */
  .section {
    margin-bottom: 11px;
  }
  .section-title {
    font-size: 9.6pt;
    font-weight: 800;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    border-left: 3.5px solid #0284c7;
    padding-left: 7px;
    margin: 0 0 7px 0;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .section-title .tagline {
    font-size: 7.6pt;
    font-weight: 500;
    color: #64748b;
    text-transform: none;
  }

  /* Cards & Grids */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9px;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 9px 11px;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 4px;
  }
  .card-title {
    font-size: 8.8pt;
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
    font-size: 8pt;
    color: #334155;
    margin: 0 0 5px 0;
    line-height: 1.35;
  }
  .card-bullets {
    margin: 0;
    padding-left: 14px;
    font-size: 7.8pt;
    color: #475569;
    line-height: 1.35;
  }
  .card-bullets li {
    margin-bottom: 3px;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.7pt;
    margin-top: 4px;
  }
  table.matrix-table th {
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 5px 8px;
    font-weight: 700;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  table.matrix-table td {
    padding: 5.5px 8px;
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

  /* Team member card */
  .member-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 3px solid #0284c7;
    border-radius: 5px;
    padding: 9px 10px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .member-name {
    font-size: 9.5pt;
    font-weight: 800;
    color: #0f172a;
  }
  .member-role {
    font-size: 7.8pt;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .member-creds {
    font-size: 7.3pt;
    color: #64748b;
    margin-bottom: 6px;
    line-height: 1.3;
  }
  .skill-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 3.5px;
    margin-top: 5px;
  }
  .chip {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    color: #334155;
    font-size: 6.8pt;
    font-weight: 600;
    padding: 1.5px 4.5px;
    border-radius: 3px;
  }

  /* Highlights callout */
  .callout-box {
    background: #f0fdf4;
    border-left: 3.5px solid #16a34a;
    border-radius: 4px;
    padding: 7px 10px;
    margin-top: 6px;
  }
  .callout-title {
    font-size: 8pt;
    font-weight: 700;
    color: #15803d;
    margin-bottom: 2px;
  }
  .callout-text {
    font-size: 7.6pt;
    color: #166534;
    line-height: 1.35;
    margin: 0;
  }

  /* Footer */
  .page-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.3pt;
    color: #94a3b8;
  }
  .footer-links a {
    color: #0284c7;
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
          DevSecOps Engineering Squad <span class="brand-badge">Enterprise Cloud</span>
        </div>
        <div class="brand-sub">AWS Cloud Architecture • Automated CI/CD • KMS Encryption • Disaster Recovery</div>
      </div>
      <div class="meta-block">
        <strong>Client:</strong> ASO Systems<br>
        <strong>Engagement:</strong> 40 hrs/week Dedicated Squad<br>
        <strong>Cutover Target:</strong> October 2027<br>
        <strong>Blended Rate:</strong> $55.00 / hr
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">Production AWS DevSecOps & Enterprise Reliability Partnership</div>
      <div class="hero-desc">
        A senior, battle-tested 3-engineer cloud squad providing end-to-end infrastructure engineering, immutable IaC deployments, container orchestration (ECS / Fargate / Docker), cryptographic data protection (AWS KMS / Secrets Manager), and automated cross-region disaster recovery to guarantee operational readiness for ASO Systems' October 2027 production cutover.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">AWS Core: <strong>ECS • Fargate • EC2 • RDS</strong></div>
        <div class="hero-pill">IaC & CI/CD: <strong>Terraform • GitLab CI • GitHub Actions</strong></div>
        <div class="hero-pill">Security: <strong>AWS KMS • IAM RBAC • ClamAV • Secrets Manager</strong></div>
        <div class="hero-pill">Compliance: <strong>GDPR & Korean PIPA Controls</strong></div>
        <div class="hero-pill">Availability: <strong>40 Hrs/Wk • Contract-to-Hire</strong></div>
      </div>
    </div>

    <!-- Executive Overview -->
    <div class="section">
      <div class="section-title">
        1. Executive Summary & Squad Delivery Model
        <span class="tagline">3 Specialized Engineers, 1 Unified Rate, Zero Skill Gaps</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">The Engineering Squad Advantage</span>
            <span class="card-badge">Cost & Speed</span>
          </div>
          <p class="card-p">
            Enterprise cloud operations require diverse competencies: cloud systems architecture, low-level database tuning, automated deployment pipelines, and compliance governance. Rather than relying on a single engineer who must divide attention, ASO Systems receives a <strong>coordinated 3-person squad</strong> billed at a single, blended hourly rate:
          </p>
          <ul class="card-bullets">
            <li><strong>Continuous Execution:</strong> Parallel workstreams across Terraform IaC, container pipelines, and database replication without context switching.</li>
            <li><strong>Enterprise Resilience:</strong> Eliminates single-point-of-failure risk; knowledge is shared across the squad with strict runbook governance.</li>
            <li><strong>Optimized Cost:</strong> Full access to a Lead Architect, Cloud DBA, and Compliance Delivery Lead at <strong>$55.00/hr</strong> (within your $50–$70/hr range).</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Direct Alignment with ASO Systems Mandate</span>
            <span class="card-badge">Mission Scope</span>
          </div>
          <p class="card-p">
            Our squad directly maps to every technical objective outlined in your enterprise specification:
          </p>
          <ul class="card-bullets">
            <li><strong>Zero-Trust AWS Foundation:</strong> Complete isolation of Dev, Staging, and Production VPCs with strict IAM least-privilege boundaries and AWS Secrets Manager.</li>
            <li><strong>Automated Disaster Recovery:</strong> Cross-region PostgreSQL/RDS replication, automated health checks, controlled writer promotion, and data reconciliation routines.</li>
            <li><strong>Cryptographic Data Lifecycle:</strong> Application-layer encryption with AWS KMS envelope keys, automated annual rotation, and regulatory retention/secure deletion.</li>
            <li><strong>October 2027 Cutover Governance:</strong> Rigorous load testing, simulated DR failovers, runbook authoring, and seamless transition to internal operations.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Technical Scope Alignment Table -->
    <div class="section">
      <div class="section-title">
        2. Technical Capability Alignment Matrix
        <span class="tagline">Mapping ASO Systems Requirements to Proven Implementation Tools</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 26%;">ASO Systems Operational Requirement</th>
            <th style="width: 38%;">Squad Implementation Strategy & Tooling</th>
            <th style="width: 36%;">Verified Real-World Precedent</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Containerized Infrastructure (ECS / Fargate)</strong></td>
            <td>Terraform modular IaC managing Amazon ECS task definitions, Fargate serverless compute, Application Load Balancers (ALB), and auto-scaling triggers.</td>
            <td>Multi-tenant e-commerce platform & Adrik microservices containerized with Docker and orchestrated in production.</td>
          </tr>
          <tr>
            <td><strong>Automated CI/CD & Deployment Controls</strong></td>
            <td>Multi-stage pipelines (GitLab CI / GitHub Actions) with SonarQube quality gates, container image vulnerability scanning, manual approvals, and instant rollbacks.</td>
            <td>DIMO Lanka Gate Pass CI/CD with SonarQube & JaCoCo gates; automated deployment across Dev, UAT, and Production.</td>
          </tr>
          <tr>
            <td><strong>Database Operations & Cross-Region DR</strong></td>
            <td>Amazon RDS (PostgreSQL/MySQL) multi-AZ setup, cross-region read replicas, automated snapshot management, and controlled writer promotion scripts.</td>
            <td>End-to-end production data migration and continuous RDS operations for SINGER Sri Lanka PLC financial workflows.</td>
          </tr>
          <tr>
            <td><strong>Security, KMS Keys & Secrets Management</strong></td>
            <td>AWS KMS envelope encryption with annual customer-managed key (CMK) rotation, AWS Secrets Manager dynamic credential injection, and IAM policy auditing.</td>
            <td>Keycloak OAuth2/OIDC token verification middleware, AWS S3 file encryption with automated ClamAV antivirus scanning.</td>
          </tr>
          <tr>
            <td><strong>Privacy & Regulatory Controls (GDPR / PIPA)</strong></td>
            <td>Structured data retention lifecycles, cryptographic erasure protocols, immutable audit event logs via Kafka/CloudTrail, and PII anonymization pipelines.</td>
            <td>Cross-system data governance on Castle Visualizer and Arimac eCom SaaS enterprise client platforms.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout-box">
      <div class="callout-title">Immediate Availability & Long-Term Roadmap</div>
      <div class="callout-text">
        Our squad is immediately available for 40 hours per week under an ongoing contract-to-hire arrangement. We are committed to supporting ASO Systems through all critical development sprints, DR recovery drills, the October 2027 production cutover, and subsequent operational acceptance.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>ASO Systems • Senior AWS DevSecOps Lead Technical Proposal</span>
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
        <div class="brand-title">Meet The DevSecOps Squad <span class="brand-badge">Roles & Expertise</span></div>
        <div class="brand-sub">Complementary Engineering Specializations Dedicated to ASO Systems</div>
      </div>
      <div class="meta-block">
        <strong>Engagement Model:</strong> Squad-as-a-Service<br>
        <strong>Lead Contact:</strong> Viranga Lakshan<br>
        <strong>Timezone:</strong> UTC+5:30 (Extensive Global Overlap)
      </div>
    </div>

    <!-- Squad Member Cards -->
    <div class="section">
      <div class="section-title">
        3. Squad Engineering Profiles
        <span class="tagline">Lead Architect + Cloud Infrastructure/DBA + Compliance Delivery Lead</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Cloud Architect & DevSecOps Lead</div>
            <div class="member-creds">Associate Software Engineer, Arimac Lanka • 4+ Years Enterprise Experience</div>
            <p class="card-p">
              Leads AWS cloud architecture, containerized infrastructure (ECS/Fargate/Docker), Terraform IaC, and security engineering. Expert in zero-trust networking, Keycloak/OIDC identity management, and automated CI/CD pipeline governance with automated security scanning.
            </p>
            <ul class="card-bullets">
              <li>Architected microservices with Docker, Kubernetes, and GitLab CI/CD for international media & e-com platforms.</li>
              <li>Engineered AWS S3 secure file ingestion with ClamAV antivirus scanning and Spring Kafka audit events.</li>
              <li>Authored multi-environment Terraform configs and SonarQube/JaCoCo automated pipeline gates.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">AWS ECS/Fargate</span>
            <span class="chip">Docker</span>
            <span class="chip">Terraform</span>
            <span class="chip">GitLab CI / Jenkins</span>
            <span class="chip">Keycloak / OIDC</span>
            <span class="chip">AWS S3 / ClamAV</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Cloud Infrastructure & Database Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Enterprise Core Systems & Database Operations</div>
            <p class="card-p">
              Specializes in production database operations, Amazon RDS management, message-driven microservices (RabbitMQ, Kafka), and serverless execution. Hands-on experience executing live enterprise database migrations and high-availability operational support.
            </p>
            <ul class="card-bullets">
              <li>Designed and executed full data migration to Amazon RDS (MySQL) for SINGER Sri Lanka PLC financial platform.</li>
              <li>Built enterprise stock-flow and tracking platform integrated with AWS Lambda and Amazon RDS.</li>
              <li>Implemented automated DB backup routines, point-in-time recovery, and multi-tier reconciliation.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Amazon RDS</span>
            <span class="chip">AWS Lambda</span>
            <span class="chip">PostgreSQL / MySQL</span>
            <span class="chip">RabbitMQ / Kafka</span>
            <span class="chip">AWS EC2</span>
            <span class="chip">DB Recovery & DR</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">DevOps Delivery & Security Compliance Lead</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise SaaS & Data Platforms</div>
            <p class="card-p">
              Orchestrates Agile sprint execution, release governance, regulatory data compliance (GDPR/PIPA), and technical documentation. Bridges technical engineering with executive risk management, disaster recovery runbooks, and cross-functional team coordination.
            </p>
            <ul class="card-bullets">
              <li>Managed 4 engineering squads delivering enterprise multi-tenant digital commerce SaaS platforms.</li>
              <li>Led delivery of Castle Visualizer enterprise data integration platform for Australian corporate client.</li>
              <li>Formulated QA test validation against strict acceptance criteria and audit compliance standards.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Release Governance</span>
            <span class="chip">GDPR / PIPA Auditing</span>
            <span class="chip">Sprint Coordination</span>
            <span class="chip">DR Runbooks</span>
            <span class="chip">Risk Management</span>
            <span class="chip">QA Acceptance</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Core DevSecOps Pillars -->
    <div class="section">
      <div class="section-title">
        4. Core AWS DevSecOps & Security Pillars
        <span class="tagline">Enterprise Standards Applied Across All ASO Systems Environments</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Infrastructure as Code & Automated Pipelines</span>
            <span class="card-badge">Terraform & CI/CD</span>
          </div>
          <p class="card-p">
            <strong>Immutable Infrastructure:</strong> 100% of AWS resources (VPCs, ECS task definitions, security groups, RDS parameter groups) declared in modular Terraform with remote state locking via S3 and DynamoDB.
          </p>
          <p class="card-p">
            <strong>Multi-Stage CI/CD Security:</strong> GitLab CI / GitHub Actions workflows enforcing static code analysis (SonarQube), container CVE scanning (Trivy), automated integration tests, manual staging-to-production approval gates, and zero-downtime blue/green rollbacks.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Disaster Recovery & Database High Availability</span>
            <span class="card-badge">RTO < 30m • RPO < 5m</span>
          </div>
          <p class="card-p">
            <strong>Cross-Region DR:</strong> Multi-AZ deployment in primary AWS region with cross-region asynchronous read replicas. Automated CloudWatch alarms trigger controlled database writer promotion runbooks.
          </p>
          <p class="card-p">
            <strong>Data Reconciliation:</strong> Post-failover reconciliation scripts verifying transaction sequence numbers, resolving split-brain scenarios, and ensuring data integrity before opening client traffic.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Cryptographic Security & KMS Key Lifecycle</span>
            <span class="card-badge">AWS KMS & Secrets</span>
          </div>
          <p class="card-p">
            <strong>Envelope Encryption:</strong> Sensitive data encrypted at application level using AWS KMS Customer Master Keys (CMK) and AES-256 GCM data keys. Secrets dynamically injected via AWS Secrets Manager with zero hardcoded credentials.
          </p>
          <p class="card-p">
            <strong>Automated Rotation:</strong> Seamless annual key rotation and re-encryption workflows with cryptographic audit logs streamed directly to AWS CloudTrail.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Regulatory Data Compliance & SRE Monitoring</span>
            <span class="card-badge">GDPR & PIPA Controls</span>
          </div>
          <p class="card-p">
            <strong>Compliant Data Lifecycle:</strong> Automated S3 lifecycle rules and RDS snapshot pruning enforcing GDPR / Korean PIPA data retention mandates, cryptographic deletion, and immutable audit logs.
          </p>
          <p class="card-p">
            <strong>Centralized Observability:</strong> CloudWatch metric dashboards, VPC Flow Logs, CloudTrail security auditing, anomaly alerting via PagerDuty/Slack, and detailed operational runbooks.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>ASO Systems • Senior AWS DevSecOps Lead Technical Proposal</span>
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
        <div class="brand-title">Verified Production Track Record <span class="brand-badge">Real Projects</span></div>
        <div class="brand-sub">Enterprise AWS, Containerization, Database Operations, and Release Governance</div>
      </div>
      <div class="meta-block">
        <strong>Clients Served:</strong> Enterprise, Multinational, Gov<br>
        <strong>Architecture:</strong> Microservices & Event-Driven<br>
        <strong>Compliance:</strong> High-Security & Enterprise Audit
      </div>
    </div>

    <!-- Project 1: DIMO Gate Pass -->
    <div class="section">
      <div class="section-title">
        5. Enterprise Case Studies & Technical Precedents
        <span class="tagline">Production Systems Built and Operated by Squad Members</span>
      </div>

      <div class="card" style="margin-bottom: 9px;">
        <div class="card-header">
          <div>
            <span class="card-title">DIMO Gate Pass Management System</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: DIMO Lanka (Enterprise Automobile & Logistics) • Lead: Viranga Lakshan</span>
          </div>
          <span class="card-badge">Security & CI/CD</span>
        </div>
        <p class="card-p">
          <strong>Architecture & Infrastructure:</strong> Mission-critical enterprise vehicle dispatch and gate security platform built as high-throughput Spring Boot microservices with Spring Kafka event streaming, Keycloak OAuth2/JWT security, and MySQL persistence with Flyway migrations.
        </p>
        <ul class="card-bullets">
          <li><strong>Secure File Handling with ClamAV & AWS S3:</strong> Architected secure file-upload ingestion pipeline to AWS S3 with automated asynchronous ClamAV virus scanning, quarantine buckets, and IAM role-delegated presigned URLs.</li>
          <li><strong>Containerization & CI/CD Quality Gates:</strong> Containerized microservices using Docker; implemented robust Jenkins and GitLab CI/CD pipelines integrating automated SonarQube static code quality analysis and JaCoCo test coverage verification before artifact promotion.</li>
          <li><strong>Multi-Role Approval Workflows:</strong> Built role-based access control (RBAC) and audit event publishing across SAP, Azure AD / Microsoft Graph, Google Maps API, and internal security personnel.</li>
        </ul>
        <div style="margin-top: 4px; font-size: 7.2pt; color: #475569;">
          <strong>Tech Stack:</strong> Docker, AWS S3, Jenkins, GitLab CI/CD, Keycloak, Spring Kafka, MySQL Flyway, ClamAV, SonarQube, JaCoCo, Java 21 / Spring Boot.
        </div>
      </div>

      <!-- Project 2: SINGER Sri Lanka RDS Migration -->
      <div class="card" style="margin-bottom: 9px;">
        <div class="card-header">
          <div>
            <span class="card-title">Enterprise Financial Operations & Amazon RDS Migration</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: SINGER Sri Lanka PLC (DMS Electronics) • Lead: Janith Kavishka</span>
          </div>
          <span class="card-badge">Amazon RDS & Lambda</span>
        </div>
        <p class="card-p">
          <strong>Database Operations & Cloud Migration:</strong> Engineered production database migration to <strong>Amazon RDS (MySQL)</strong> for an island-wide financial field collection, batch-wise transaction tracking, and mobile receipt generation platform.
        </p>
        <ul class="card-bullets">
          <li><strong>Zero-Downtime Migration & Data Integrity:</strong> Managed schema re-architecting, continuous data replication, and high-volume reconciliation during cutover, ensuring zero data loss across millions of financial records.</li>
          <li><strong>AWS Serverless & Event Streaming:</strong> Built multi-tier distribution tracking platform utilizing <strong>AWS Lambda</strong> integrated with Amazon RDS and Spring Boot backend microservices using RabbitMQ for reliable, message-driven transaction processing.</li>
          <li><strong>Production DBA Support:</strong> Ongoing query optimization, automated snapshot lifecycle scheduling, index tuning, and uninterrupted operational support for enterprise clients.</li>
        </ul>
        <div style="margin-top: 4px; font-size: 7.2pt; color: #475569;">
          <strong>Tech Stack:</strong> Amazon RDS, AWS Lambda, Docker, Java / Spring Boot, RabbitMQ, React, Next.js, MySQL, Enterprise Backup & Replication.
        </div>
      </div>

      <!-- Project 3 & 4 Grid -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Adrik News & E-Com SaaS</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Adrik (Kuwait) & Arimac</span>
            </div>
            <span class="card-badge">Kubernetes & OIDC</span>
          </div>
          <p class="card-p">
            <strong>Bilingual Media & Multi-Tenant SaaS:</strong> Backend microservices connecting web and mobile applications to core APIs. Containerized with Docker and deployed to <strong>Kubernetes</strong> via GitLab CI/CD across Dev, UAT, and Production.
          </p>
          <ul class="card-bullets">
            <li>Keycloak OAuth2/OIDC authentication with JWT validation middleware and token refresh routines.</li>
            <li>Multi-tenant database schema isolation and dynamic tenant provisioning.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Castle Visualizer & Arimac eCom</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Castle Group (Australia) • PM: Lithumitha</span>
            </div>
            <span class="card-badge">Release Governance</span>
          </div>
          <p class="card-p">
            <strong>Enterprise Data Platform & SaaS Delivery:</strong> Multi-dashboard analytics platform consolidating data across legacy ERP and operational business systems into real-time reporting plane.
          </p>
          <ul class="card-bullets">
            <li>Sprint planning and release governance across 4 engineering squads with strict change management.</li>
            <li>Enforced rigorous QA acceptance criteria, audit compliance tracking, and incident post-mortems.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>ASO Systems • Senior AWS DevSecOps Lead Technical Proposal</span>
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
        <div class="brand-title">Execution Blueprint & Cutover Roadmap <span class="brand-badge">October 2027</span></div>
        <div class="brand-sub">Structured Phasing to Ensure Production Hardening, Disaster Recovery, and Operational Readiness</div>
      </div>
      <div class="meta-block">
        <strong>Commitment:</strong> 40 hrs/wk Dedicated<br>
        <strong>Target Cutover:</strong> October 2027<br>
        <strong>Rate:</strong> $55.00/hr Squad Total
      </div>
    </div>

    <!-- Roadmap to October 2027 -->
    <div class="section">
      <div class="section-title">
        6. Phased Technical Execution Blueprint
        <span class="tagline">From Baseline IaC Hardening to October 2027 Production Cutover & Handover</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 1: Environment Isolation & IaC Foundation</span>
            <span class="card-badge">Months 1–3</span>
          </div>
          <ul class="card-bullets">
            <li>Audit current infrastructure and codify all resources into clean, modular <strong>Terraform</strong> scripts with state locking in Amazon S3/DynamoDB.</li>
            <li>Establish strictly isolated VPCs for Development, Staging, and Production with public/private subnet topology and NAT gateways.</li>
            <li>Implement AWS IAM role-based least privilege, enforce MFA for console access, and configure AWS Secrets Manager for all environment credentials.</li>
            <li>Deploy containerized base environments using Docker on Amazon ECS / AWS Fargate behind Application Load Balancers.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 2: Secure CI/CD & KMS Key Lifecycles</span>
            <span class="card-badge">Months 4–7</span>
          </div>
          <ul class="card-bullets">
            <li>Build automated CI/CD pipelines (GitLab CI / GitHub Actions) integrating SonarQube SAST, Trivy container security scans, and automated unit test gates.</li>
            <li>Implement AWS KMS envelope encryption for sensitive database columns and S3 artifacts with automated annual CMK rotation.</li>
            <li>Configure centralized observability: AWS CloudWatch container insights, CloudTrail audit logs, and proactive PagerDuty alerting.</li>
            <li>Establish GDPR and Korean PIPA data retention lifecycles, automated backup archiving, and secure cryptographic deletion scripts.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 3: Database High Availability & DR Drills</span>
            <span class="card-badge">Months 8–14</span>
          </div>
          <ul class="card-bullets">
            <li>Deploy Amazon RDS (PostgreSQL/MySQL) multi-AZ primary cluster with automated asynchronous cross-region read replica for disaster recovery.</li>
            <li>Script automated DR failover workflows: controlled writer promotion, DNS routing updates via Route 53, and application reconnection pooling.</li>
            <li>Conduct quarterly simulated DR exercises to test cross-region recovery, measure RTO/RPO, and validate post-failover data reconciliation routines.</li>
            <li>Optimize database performance: connection pooling, query indexing, slow-query logging, and storage auto-scaling.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Phase 4: Load Testing, Cutover & Handover</span>
            <span class="card-badge">Months 15–18+ (Oct 2027)</span>
          </div>
          <ul class="card-bullets">
            <li>Lead comprehensive pre-cutover performance and load testing simulating peak enterprise transaction volumes on ECS and RDS.</li>
            <li>Coordinate third-party penetration testing, vulnerability remediation, and security posture sign-off.</li>
            <li><strong>Lead October 2027 Production Cutover:</strong> Execute synchronized cutover runbook with zero downtime, live data verification, and hypercare standby.</li>
            <li>Deliver comprehensive operational runbooks, disaster recovery procedures, and conduct structured handover sessions for internal teams.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Operating Agreement & Commercials -->
    <div class="section">
      <div class="section-title">
        7. Engagement Terms & Operational SLA
        <span class="tagline">Predictable, Transparent Enterprise Partnership</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Dedicated Bandwidth</span>
            <span class="card-badge">Commitment</span>
          </div>
          <p class="card-p">
            <strong>40 Hours / Week:</strong> Continuous coverage across development, testing, recovery drills, and cutover. Direct participation in daily standups and sprint planning.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Single Blended Rate</span>
            <span class="card-badge">Cost Certainty</span>
          </div>
          <p class="card-p">
            <strong>$55.00 / Hour:</strong> Transparent hourly billing covering the entire 3-person squad under a single Upwork contract-to-hire agreement, with zero hidden fees.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Cross-Functional Synergy</span>
            <span class="card-badge">Collaboration</span>
          </div>
          <p class="card-p">
            Active, collaborative integration with ASO Systems' software architects, .NET developers, QA engineers, and external security compliance auditors.
          </p>
        </div>
      </div>
    </div>

    <!-- Call to action box -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #0284c7;">
      <div class="callout-title" style="color: #0f172a;">Next Steps & Technical Discovery Call</div>
      <div class="callout-text" style="color: #334155;">
        We welcome a technical discussion with ASO Systems engineering leadership to review your current AWS architecture, evaluate your October 2027 cutover milestones, and present our Terraform and DR runbook templates. We are ready to begin immediately upon award.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>ASO Systems • Senior AWS DevSecOps Lead Technical Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\ASO_Systems_AWS_DevSecOps"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "ASO_Systems_AWS_DevSecOps_Team_Proposal.pdf")
    
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

