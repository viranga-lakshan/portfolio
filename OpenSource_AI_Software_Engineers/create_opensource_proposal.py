import os
import subprocess
import pypdfium2 as pdfium

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Senior Software Engineering Proposal - Open Source & Systems Development</title>
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
    border-bottom: 2px solid #059669;
    padding-bottom: 8px;
    margin-bottom: 11px;
  }
  .brand-title {
    font-size: 13.5pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.4px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand-badge {
    background: #059669;
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
    background: linear-gradient(135deg, #0f172a 0%, #064e3b 55%, #059669 100%);
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
    color: #6ee7b7;
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
    border-left: 3.5px solid #059669;
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
    background: #ecfdf5;
    color: #047857;
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

  /* Pipeline Flow for Optimization */
  .pipeline-flow {
    display: flex;
    align-items: stretch;
    gap: 7px;
    margin-top: 4px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 7px;
  }
  .pipeline-col {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .pipeline-col.accent {
    border-top: 3px solid #059669;
    flex: 1.35;
  }
  .pipeline-badge {
    display: inline-block;
    font-size: 6.7pt;
    font-weight: 700;
    color: #059669;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
  }
  .pipeline-title {
    font-size: 8.3pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 3px;
  }
  .pipeline-p {
    font-size: 7.4pt;
    color: #475569;
    line-height: 1.3;
    margin: 0;
  }
  .pipeline-bullets {
    margin: 0;
    padding-left: 12px;
    font-size: 7.2pt;
    color: #334155;
    line-height: 1.28;
  }
  .pipeline-bullets li {
    margin-bottom: 2px;
  }
  .pipeline-bullets code, .pipeline-p code {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 1px 3px;
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
    border-top: 3px solid #059669;
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
    color: #059669;
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
    color: #059669;
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
          Open Source & Systems Engineering <span class="brand-badge">Polyglot SWE</span>
        </div>
        <div class="brand-sub">Java • Python • C++ • TypeScript • Algorithmic Optimization • Complex Codebase Refactoring</div>
      </div>
      <div class="meta-block">
        <strong>Focus:</strong> Open-Source Development & AI Technical Benchmarks<br>
        <strong>Availability:</strong> Immediate Onboarding (Within 24–48 Hours)<br>
        <strong>Core Languages:</strong> Java 21, Python 3.x, C++, TypeScript, C#<br>
        <strong>Model:</strong> Senior Software Engineering Team
      </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
      <div class="hero-title">High-Velocity Open Source Engineering, Bug Triage & Algorithmic Optimization</div>
      <div class="hero-desc">
        A senior, battle-tested software engineering team proficient in reading, debugging, and refactoring large-scale open-source codebases. Combining deep polyglot fluency across Java, Python, C++, and TypeScript with rigorous algorithmic problem-solving, automated test coverage, and clear technical documentation to solve complex software engineering challenges.
      </div>
      <div class="hero-pills">
        <div class="hero-pill">Languages: <strong>Java 21 • Python 3.12 • C++ • TypeScript • C#</strong></div>
        <div class="hero-pill">Workflows: <strong>Git • GitHub PRs • Issue Triage • SWE-bench</strong></div>
        <div class="hero-pill">Discipline: <strong>Clean Code • Algorithm Profiling • Unit Testing</strong></div>
        <div class="hero-pill">Execution: <strong>Reproducible Bug Fixes • High-Performance Refactoring</strong></div>
        <div class="hero-pill">Onboarding: <strong>Ready within 24–48 Hours of Selection</strong></div>
      </div>
    </div>

    <!-- Executive Overview -->
    <div class="section">
      <div class="section-title">
        1. Engineering Capabilities & Core Strengths
        <span class="tagline">Mastering Unfamiliar Repositories Quickly and Delivering Production-Grade Code</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Navigating & Mastering Existing Codebases</span>
            <span class="card-badge">Code Mastery</span>
          </div>
          <p class="card-p">
            In advanced open-source and AI benchmark environments, the primary hurdle is rapidly understanding architectural patterns, dependency graphs, and implicit assumptions across massive repos:
          </p>
          <ul class="card-bullets">
            <li><strong>Fast Architectural Deconstruction:</strong> Quickly parsing call graphs, module boundaries, and concurrency patterns in multi-thousand-line repositories.</li>
            <li><strong>Root-Cause Debugging:</strong> Isolating edge-case defects, memory leaks, race conditions, and numerical inaccuracies using systematic reproduction harnesses.</li>
            <li><strong>Minimal-Diff Refactoring:</strong> Writing surgical, idiomatic code modifications that solve the issue cleanly without introducing regressions or side-effects.</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-header">
            <span class="card-title">Algorithmic Rigor & Clean Code Standards</span>
            <span class="card-badge">Engineering Depth</span>
          </div>
          <p class="card-p">
            We treat code quality as an uncompromising foundation across all programming languages:
          </p>
          <ul class="card-bullets">
            <li><strong>Complexity Optimization:</strong> Analyzing Big-O time and space complexity, replacing O(n²) bottlenecks with O(n log n) or O(1) structures.</li>
            <li><strong>Defensive Testing & Verification:</strong> Backing every feature and bug fix with thorough unit tests (JUnit, pytest, Catch2, Jest) and edge-case assertions.</li>
            <li><strong>Exemplary Documentation:</strong> Writing clear, human-readable PR descriptions, documenting architectural trade-offs, and providing reproducible verification steps.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Language & Tech Matrix -->
    <div class="section">
      <div class="section-title">
        2. Technical Proficiency & Language Matrix
        <span class="tagline">Production Depth Across the Entire Required Tech Stack</span>
      </div>
      <table class="matrix-table">
        <thead>
          <tr>
            <th style="width: 22%;">Language & Stack</th>
            <th style="width: 44%;">Core Competencies & Engineering Applications</th>
            <th style="width: 34%;">Verified Precedents</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Java (8, 17, 21)</strong></td>
            <td>Object-oriented design, multi-threading, concurrency utilities, Spring Boot microservices, memory optimization, JVM garbage collection tuning, and JUnit testing.</td>
            <td>DIMO Gate Pass enterprise microservices, Kafka event streaming, and SINGER financial platforms.</td>
          </tr>
          <tr>
            <td><strong>Python (3.8–3.12)</strong></td>
            <td>Data structures, async I/O, algorithmic problem-solving, FastAPI/Flask services, data pipelines, pytest suites, and deterministic mathematical calculations.</td>
            <td>*InvoiceIQ* automated reconciliation engine with SHA-256 idempotency and data parsing pipelines.</td>
          </tr>
          <tr>
            <td><strong>C / C++</strong></td>
            <td>Pointer arithmetic, manual memory management (RAII), STL containers and algorithms, low-level data structures, profiling, and performance-critical systems.</td>
            <td>Academic systems programming, competitive programming problem solving, and algorithm implementation.</td>
          </tr>
          <tr>
            <td><strong>TypeScript / JavaScript</strong></td>
            <td>Modern ES6+, asynchronous event loops, Node.js backend services, typed domain modeling, React/Next.js architectures, and Jest/Mocha unit test suites.</td>
            <td>Adrik Kuwait bilingual BFF microservices, Al Ain Museum V2 frontend, and enterprise dashboard platforms.</td>
          </tr>
          <tr>
            <td><strong>Git & Open Source Tooling</strong></td>
            <td>Advanced git branching, rebasing, interactive conflict resolution, bisecting regression commits, GitHub Actions CI/CD pipelines, and pull request reviews.</td>
            <td>Active GitHub contributions, multi-environment CI/CD deployment pipelines, and code review governance.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Callout -->
    <div class="callout-box">
      <div class="callout-title">Immediate Availability: Ready to Begin Within 24–48 Hours</div>
      <div class="callout-text">
        We understand this project requires immediate engagement. Our engineers are available to begin onboarding, repository access setup, and technical screening/assessment tasks within 24 to 48 hours of acceptance.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Senior Software Engineers • Open Source Development Proposal</span>
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
        <div class="brand-title">Engineering Methodology & Problem Solving <span class="brand-badge">Methodology</span></div>
        <div class="brand-sub">Systematic Debugging, Algorithmic Optimization, and Codebase Refactoring</div>
      </div>
      <div class="meta-block">
        <strong>Approach:</strong> Test-Driven & Root-Cause Analysis<br>
        <strong>Quality Gates:</strong> SonarQube, JaCoCo, Pytest<br>
        <strong>Git Etiquette:</strong> Atomic Commits & Clear PR Walkthroughs
      </div>
    </div>

    <!-- 4-Step Problem Solving Framework -->
    <div class="section">
      <div class="section-title">
        3. Systematic Problem-Solving & Bug Triage Lifecycle
        <span class="tagline">How We Approach Complex Bugs and Feature Implementations in Open Source</span>
      </div>
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <span class="card-title">1. Minimal Reproduction Harness</span>
            <span class="card-badge">Step 1</span>
          </div>
          <p class="card-p">
            Before changing a single line of code, we isolate the reported bug by writing a failing unit test or minimal reproduction script. This guarantees unambiguous proof of the defect and provides an objective benchmark for verifying the eventual fix.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">2. Root-Cause Analysis & Tracing</span>
            <span class="card-badge">Step 2</span>
          </div>
          <p class="card-p">
            Using interactive debuggers, stack trace analysis, and `git bisect` when necessary, we pinpoint the exact commit, invariant violation, off-by-one condition, or type mismatch that caused the issue—ensuring we treat the underlying defect rather than symptoms.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">3. Surgical, Idiomatic Refactoring</span>
            <span class="card-badge">Step 3</span>
          </div>
          <p class="card-p">
            We implement the fix or new feature strictly following the repository's established style guides, architectural conventions, and design patterns. We maintain minimal diff footprints to facilitate rapid peer review and reduce regression surface area.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">4. Verification, Edge Cases & Documentation</span>
            <span class="card-badge">Step 4</span>
          </div>
          <p class="card-p">
            We expand test coverage to include boundary conditions (nulls, empty collections, overflow values, concurrent access). We document the technical reasoning, changes made, and verification steps in clean, structured Markdown pull requests.
          </p>
        </div>
      </div>
    </div>

    <!-- Algorithmic Optimization Deep Dive -->
    <div class="section">
      <div class="section-title">
        4. Algorithmic Optimization & Complexity Engineering
        <span class="tagline">Transforming Sluggish Execution into High-Throughput Performance</span>
      </div>
      <div class="diagram-box">
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [BOTTLENECK IDENTIFICATION]  CPU Profiling / Flamegraphs / Memory Profilers (py-spy, JProfiler) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [ALGORITHMIC RE-ENGINEERING]                                                                     │
│  ├── Inefficient Lookups: Replacing linear list searches O(N) with Hash Tables / Sets O(1)        │
│  ├── Redundant Work: Memoization, Dynamic Programming, and caching repeated calculations         │
│  ├── Memory Footprint: Replacing bloated objects with primitive arrays, generators, or pools     │
│  └── Concurrency: Leveraging asynchronous I/O (asyncio, CompletableFuture) without deadlocks     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [BENCHMARK VERIFICATION]  Automated micro-benchmarks proving latency reduction and zero leakage   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
      </div>
    </div>

    <!-- Code Quality & Peer Review Standards -->
    <div class="section">
      <div class="section-title">
        5. Quality Standards, Pull Request Etiquette & Documentation
        <span class="tagline">Writing Code That Open-Source Maintainers Love to Merge</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">Atomic Git Commits</span>
            <span class="card-badge">Version Control</span>
          </div>
          <p class="card-p">
            Every commit encapsulates a single logical change with clear, conventional commit messages (`feat:`, `fix:`, `refactor:`, `test:`) enabling easy cherry-picking and rollback.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Automated Linting & Types</span>
            <span class="card-badge">Code Standards</span>
          </div>
          <p class="card-p">
            Strict adherence to language formatters and linters (Checkstyle, Black, Flake8, ESLint, Clang-Format), ensuring zero lint warnings and complete static type safety.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Comprehensive Runbooks</span>
            <span class="card-badge">Documentation</span>
          </div>
          <p class="card-p">
            Writing crystal-clear developer documentation, setup guides, API schemas, and architectural decision records (ADRs) that make solutions self-explanatory.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Senior Software Engineers • Open Source Development Proposal</span>
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
        <div class="brand-title">Verified International Engineering Precedents <span class="brand-badge">Track Record</span></div>
        <div class="brand-sub">Production Systems in Java, Python, TypeScript, Microservices & Event Architecture</div>
      </div>
      <div class="meta-block">
        <strong>International Scope:</strong> Sri Lanka, Kuwait, UAE, Australia<br>
        <strong>Backend Tech:</strong> Java 21, Python, Node.js, Spring Boot, Docker<br>
        <strong>Quality Gates:</strong> SonarQube, JaCoCo, JUnit, Pytest
      </div>
    </div>

    <!-- Case Studies -->
    <div class="section">
      <div class="section-title">
        6. Production Systems & Complex Problem Solving Case Studies
        <span class="tagline">Demonstrated Engineering Rigor on Real-World International Platforms</span>
      </div>

      <!-- DIMO Gate Pass -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">DIMO Enterprise Gate Pass & Logistics Management System</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: DIMO Lanka • Lead: Viranga Lakshan</span>
          </div>
          <span class="card-badge">Java 21 / Spring Boot</span>
        </div>
        <p class="card-p">
          <strong>Complex Microservices Architecture:</strong> Engineered high-concurrency microservices utilizing Java 21 and Spring Boot 3.4.5, managing API gateways, role-based approval hierarchies, and event-driven audit streaming.
        </p>
        <ul class="card-bullets">
          <li><strong>Automated Code Quality & Test Gates:</strong> Supported CI/CD workflows using Jenkins and GitLab pipelines enforcing automated SonarQube static code quality analysis and JaCoCo test coverage verification before artifact promotion.</li>
          <li><strong>Asynchronous Event Streaming:</strong> Implemented Spring Kafka publishing immutable audit events across distributed services, integrating with SAP ERP, Microsoft Graph, and AWS S3 with ClamAV virus scanning.</li>
          <li><strong>Database Migrations:</strong> Managed relational schema design and automated Flyway migrations in MySQL, ensuring zero downtime.</li>
        </ul>
      </div>

      <!-- InvoiceIQ & SINGER PLC -->
      <div class="card" style="margin-bottom: 8px;">
        <div class="card-header">
          <div>
            <span class="card-title">InvoiceIQ Reconciliation Engine & SINGER Sri Lanka PLC</span>
            <span style="font-size: 7.8pt; color: #64748b; margin-left: 6px;">Client: SINGER PLC & Open Systems • Janith Kavishka</span>
          </div>
          <span class="card-badge">Python & Java Systems</span>
        </div>
        <p class="card-p">
          <strong>Deterministic Financial Matching & Distribution Systems:</strong> Architected *InvoiceIQ*, an automated line-item reconciliation engine in Python and FastAPI performing deterministic 3-way matching with SHA-256 idempotency controls.
        </p>
        <ul class="card-bullets">
          <li><strong>Enterprise Java & Event Messaging:</strong> Built backend services using Java and Spring Boot with RabbitMQ for message-driven communication across distributed enterprise components.</li>
          <li><strong>Database Optimization & Migration:</strong> Executed zero-downtime database migration to Amazon RDS (MySQL) for nationwide transaction tracking, tuning complex queries and eliminating performance bottlenecks.</li>
        </ul>
      </div>

      <!-- Adrik Kuwait & Castle Visualizer Australia Grid -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Adrik Bilingual Media Platform</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Adrik (Kuwait) • Node.js / Kubernetes</span>
            </div>
            <span class="card-badge">Node / TypeScript</span>
          </div>
          <p class="card-p">
            Developed three Node.js/Express BFF microservices connecting web and mobile applications for a Kuwaiti media client. Deployed to Kubernetes via GitLab CI/CD with Keycloak OAuth2/OIDC authentication.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <span class="card-title">Castle Visualizer Analytics Platform</span>
              <span style="font-size: 7.2pt; color: #64748b; display: block;">Client: Castle Group (Australia) • Lithumitha</span>
            </div>
            <span class="card-badge">Data Systems</span>
          </div>
          <p class="card-p">
            Led delivery of enterprise multi-dashboard analytics platform consolidating data across legacy business systems into real-time reporting, managing requirements and rigorous QA acceptance criteria.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Senior Software Engineers • Open Source Development Proposal</span>
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
        <div class="brand-title">Squad Profiles & Onboarding Readiness <span class="brand-badge">Execution</span></div>
        <div class="brand-sub">Team Backgrounds, GitHub Contributions, Competitive Problem Solving & Immediate Availability</div>
      </div>
      <div class="meta-block">
        <strong>Onboarding:</strong> Available Within 24–48 Hours<br>
        <strong>Communication:</strong> Fluent English (Written & Verbal)<br>
        <strong>GitHub:</strong> github.com/viranga-lakshan
      </div>
    </div>

    <!-- Squad Member Profiles -->
    <div class="section">
      <div class="section-title">
        7. Meet The Software Engineering Squad
        <span class="tagline">Dedicated Problem Solvers with International Enterprise Experience</span>
      </div>
      <div class="grid-3">
        <!-- Viranga -->
        <div class="member-box">
          <div>
            <div class="member-name">Viranga Lakshan</div>
            <div class="member-role">Lead Software Engineer</div>
            <div class="member-creds">Associate Software Engineer, Arimac • 4+ Years Systems Experience</div>
            <p class="card-p">
              Polyglot software engineer specializing in Java 21, Spring Boot, Python, Node.js/TypeScript, C# .NET, Docker containerization, Kafka event streaming, and automated CI/CD code quality pipelines (SonarQube).
            </p>
            <ul class="card-bullets">
              <li>Architected microservices for international clients across Kuwait, UAE, and Sri Lanka.</li>
              <li>Hands-on experience refactoring complex distributed codebases and optimizing algorithms.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Java 21</span>
            <span class="chip">Python</span>
            <span class="chip">TypeScript</span>
            <span class="chip">Docker</span>
            <span class="chip">Git / CI/CD</span>
            <span class="chip">Kafka</span>
          </div>
        </div>

        <!-- Janith -->
        <div class="member-box">
          <div>
            <div class="member-name">Janith Kavishka</div>
            <div class="member-role">Senior Backend & Systems Engineer</div>
            <div class="member-creds">Programmer, DMS Electronics • Systems & Data Engineering</div>
            <p class="card-p">
              Expert in algorithmic design, data structures, Java, Python, Spring Boot, RabbitMQ, SQL query optimization, and building high-performance backend pipelines.
            </p>
            <ul class="card-bullets">
              <li>Architected *InvoiceIQ* 3-way automated matching engine with SHA-256 idempotency.</li>
              <li>Built distributed transaction processing and AWS serverless distribution platforms.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Java / Spring</span>
            <span class="chip">Python</span>
            <span class="chip">SQL Tuning</span>
            <span class="chip">RabbitMQ</span>
            <span class="chip">Algorithms</span>
            <span class="chip">AWS Lambda</span>
          </div>
        </div>

        <!-- Lithumitha -->
        <div class="member-box">
          <div>
            <div class="member-name">Lithumitha Ravikumar</div>
            <div class="member-role">Technical Delivery & QA Lead</div>
            <div class="member-creds">Associate Project Manager, Arimac • Enterprise Systems Governance</div>
            <p class="card-p">
              Bridges technical problem solving with structured delivery, code review tracking, issue triage, and acceptance testing across multi-squad engineering environments.
            </p>
            <ul class="card-bullets">
              <li>Managed 4 engineering squads delivering enterprise multi-tenant digital SaaS platforms.</li>
              <li>Coordinates technical documentation, PR reviews, and QA validation.</li>
            </ul>
          </div>
          <div class="skill-chips">
            <span class="chip">Issue Triage</span>
            <span class="chip">PR Review</span>
            <span class="chip">QA Testing</span>
            <span class="chip">Documentation</span>
            <span class="chip">Agile / Git</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Onboarding Commitment Grid -->
    <div class="section">
      <div class="section-title">
        8. Immediate Onboarding Protocol & Standards
        <span class="tagline">Zero Ramp-Up Delay — Delivering Value from Day One</span>
      </div>
      <div class="grid-3">
        <div class="card">
          <div class="card-header">
            <span class="card-title">24–48h Onboarding</span>
            <span class="card-badge">Availability</span>
          </div>
          <p class="card-p">
            Ready to clone repositories, configure local development sandboxes, review contribution guidelines, and tackle initial task tickets within 24–48 hours of acceptance.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Competitive Problem Solving</span>
            <span class="card-badge">Algorithms</span>
          </div>
          <p class="card-p">
            Strong foundation in algorithms and data structures (LeetCode / HackerRank style problem solving), ensuring rapid resolution of complex logic puzzles and edge cases.
          </p>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title">Clear Communication</span>
            <span class="card-badge">Collaboration</span>
          </div>
          <p class="card-p">
            Fluent written English communication for asynchronous GitHub PR discussions, technical RFCs, issue comments, and documentation.
          </p>
        </div>
      </div>
    </div>

    <!-- Call to action -->
    <div class="callout-box" style="background: #f8fafc; border-left: 3.5px solid #059669; margin-top: 4px;">
      <div class="callout-title" style="color: #0f172a;">Ready for Technical Screening & Immediate Project Tasks</div>
      <div class="callout-text" style="color: #334155;">
        We welcome any technical evaluation, coding challenge, or repository walk-through. Please review our public GitHub repositories and portfolio, and let us know the next steps for technical screening and onboarding.
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Senior Software Engineers • Open Source Development Proposal</span>
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
    base_dir = r"C:\Users\Viranga\Downloads\upwrok new\OpenSource_AI_Software_Engineers"
    html_file = os.path.join(base_dir, "proposal.html")
    pdf_file = os.path.join(base_dir, "OpenSource_Software_Engineering_Proposal.pdf")
    
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

