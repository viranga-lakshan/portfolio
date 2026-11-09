import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ----------------- BANNER 1: MAIN COVER -----------------
html_banner_1 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 80% 20%, #1e1b4b 0%, #0f172a 50%, #030712 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 70px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  /* Background glow */
  .glow-1 {
    position: absolute;
    top: -100px;
    right: -100px;
    width: 500px;
    height: 500px;
    background: rgba(37, 99, 235, 0.25);
    filter: blur(120px);
    border-radius: 50%;
  }
  .glow-2 {
    position: absolute;
    bottom: -150px;
    left: -100px;
    width: 550px;
    height: 550px;
    background: rgba(16, 185, 129, 0.15);
    filter: blur(140px);
    border-radius: 50%;
  }

  /* Top Bar */
  .top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .author-tag {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .avatar {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #06b6d4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    font-size: 20px;
    color: #ffffff;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
  }
  .author-name {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -0.3px;
    color: #ffffff;
  }
  .author-role {
    font-size: 13px;
    color: #94a3b8;
    font-weight: 600;
  }
  .exp-pill {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1.5px solid rgba(52, 211, 153, 0.4);
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }

  /* Main Headline */
  .hero-content {
    position: relative;
    z-index: 2;
    margin: auto 0;
  }
  .tagline {
    color: #38bdf8;
    font-size: 15px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 12px;
  }
  .headline {
    font-size: 52px;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -1.5px;
    margin-bottom: 18px;
    background: linear-gradient(135deg, #ffffff 40%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .headline span {
    background: linear-gradient(135deg, #60a5fa 0%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .sub-headline {
    font-size: 20px;
    color: #94a3b8;
    max-width: 820px;
    line-height: 1.45;
    font-weight: 500;
  }

  /* Tech Grid */
  .tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    position: relative;
    z-index: 2;
    margin-top: 24px;
  }
  .tech-badge {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 15px;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .tech-badge.highlight {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.3), rgba(6, 182, 212, 0.3));
    border-color: #38bdf8;
    color: #ffffff;
  }

  /* Bottom Metrics */
  .bottom-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    position: relative;
    z-index: 2;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }
  .metric-box {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px 18px;
  }
  .metric-val {
    font-size: 22px;
    font-weight: 900;
    color: #38bdf8;
  }
  .metric-lbl {
    font-size: 12px;
    color: #94a3b8;
    font-weight: 600;
    margin-top: 2px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
</style>
</head>
<body>
  <div class="glow-1"></div>
  <div class="glow-2"></div>

  <div class="top-bar">
    <div class="author-tag">
      <div class="avatar">V</div>
      <div>
        <div class="author-name">Viranga Lakshan</div>
        <div class="author-role">Full Stack & Microservices Engineer</div>
      </div>
    </div>
    <div class="exp-pill">✓ 4+ Years Enterprise Exp · Arimac Digital</div>
  </div>

  <div class="hero-content">
    <div class="tagline">Enterprise Web Application Development</div>
    <div class="headline">
      Full Stack Web Apps &<br>
      <span>Spring Boot 3 Microservices</span>
    </div>
    <div class="sub-headline">
      High-performance web applications, resilient backend microservices, and modern responsive frontends with React, Next.js, Java 21, and Kafka.
    </div>

    <div class="tech-pills">
      <div class="tech-badge highlight">☕ Java 21 / Spring Boot 3</div>
      <div class="tech-badge highlight">⚛️ Next.js 14 / React</div>
      <div class="tech-badge">TypeScript</div>
      <div class="tech-badge">Kafka Event Streams</div>
      <div class="tech-badge">Keycloak OAuth2 / JWT</div>
      <div class="tech-badge">Docker & CI/CD</div>
      <div class="tech-badge">PostgreSQL / MySQL</div>
    </div>
  </div>

  <div class="bottom-bar">
    <div class="metric-box">
      <div class="metric-val">4+ Years</div>
      <div class="metric-lbl">Industry Experience</div>
    </div>
    <div class="metric-box">
      <div class="metric-val">99.9%</div>
      <div class="metric-lbl">High-Availability Uptime</div>
    </div>
    <div class="metric-box">
      <div class="metric-val">Microservices</div>
      <div class="metric-lbl">Decoupled Clean Code</div>
    </div>
    <div class="metric-box">
      <div class="metric-val">100%</div>
      <div class="metric-lbl">On-Time Delivery</div>
    </div>
  </div>
</body>
</html>"""

# ----------------- BANNER 2: ENTERPRISE PROJECTS SHOWCASE -----------------
html_banner_2 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 20% 20%, #0f172a 0%, #091328 60%, #030712 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 55px 65px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .glow-1 {
    position: absolute;
    top: -80px;
    left: -80px;
    width: 450px;
    height: 450px;
    background: rgba(99, 102, 241, 0.2);
    filter: blur(120px);
    border-radius: 50%;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1.5px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 18px;
    position: relative;
    z-index: 2;
  }
  .header h2 {
    font-size: 32px;
    font-weight: 900;
    letter-spacing: -0.5px;
    color: #ffffff;
  }
  .header h2 span {
    color: #38bdf8;
  }
  .header-subtitle {
    font-size: 14px;
    color: #94a3b8;
    margin-top: 4px;
  }
  .company-badge {
    background: rgba(37, 99, 235, 0.2);
    border: 1px solid rgba(56, 189, 248, 0.4);
    color: #38bdf8;
    padding: 7px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
  }

  /* Projects Grid */
  .projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin: 22px 0;
    position: relative;
    z-index: 2;
  }
  .project-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 18px 22px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  }
  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }
  .card-title {
    font-size: 17px;
    font-weight: 800;
    color: #ffffff;
  }
  .client-tag {
    font-size: 11px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 6px;
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(52, 211, 153, 0.3);
  }
  .card-desc {
    font-size: 12.5px;
    color: #94a3b8;
    line-height: 1.45;
    margin-bottom: 12px;
  }
  .card-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .pill {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 3px 9px;
    border-radius: 5px;
    font-size: 11px;
    font-weight: 600;
    color: #cbd5e1;
  }

  /* Footer banner */
  .footer-cta {
    background: linear-gradient(90deg, #1e1b4b 0%, #1e3a8a 100%);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 12px;
    padding: 14px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .cta-text {
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
  }
  .cta-sub {
    font-size: 12px;
    color: #93c5fd;
  }
  .btn-contact {
    background: #10b981;
    color: #ffffff;
    font-weight: 800;
    padding: 8px 18px;
    border-radius: 8px;
    font-size: 13px;
  }
</style>
</head>
<body>
  <div class="glow-1"></div>

  <div class="header">
    <div>
      <h2>Proven Enterprise Portfolio <span>(Arimac Digital)</span></h2>
      <div class="header-subtitle">Real-world production platforms built for major international corporate clients</div>
    </div>
    <div class="company-badge">Enterprise Track Record</div>
  </div>

  <div class="projects-grid">
    <!-- Project 1 -->
    <div class="project-card">
      <div class="card-top">
        <div class="card-title">DIMO Gate Pass Management</div>
        <div class="client-tag">DIMO Lanka</div>
      </div>
      <div class="card-desc">
        Enterprise vehicle dispatch system built as Spring Boot microservices with Kafka event streaming, Keycloak OAuth2/JWT, and SAP / Azure AD integrations.
      </div>
      <div class="card-tech">
        <span class="pill">Java 21</span>
        <span class="pill">Spring Boot 3.4.5</span>
        <span class="pill">Spring Kafka</span>
        <span class="pill">MySQL / Flyway</span>
        <span class="pill">Docker</span>
      </div>
    </div>

    <!-- Project 2 -->
    <div class="project-card">
      <div class="card-top">
        <div class="card-title">Adrik News & Media Platform</div>
        <div class="client-tag">Adrik, Kuwait</div>
      </div>
      <div class="card-desc">
        Bilingual media platform with paid subscriptions, mobile app BFF APIs, OneSignal push notifications, SMS delivery, and Kubernetes deployments.
      </div>
      <div class="card-tech">
        <span class="pill">Node.js</span>
        <span class="pill">Express BFF</span>
        <span class="pill">OneSignal</span>
        <span class="pill">Keycloak</span>
        <span class="pill">Kubernetes</span>
      </div>
    </div>

    <!-- Project 3 -->
    <div class="project-card">
      <div class="card-top">
        <div class="card-title">Multi-Tenant E-Commerce Platform</div>
        <div class="client-tag">Enterprise Client</div>
      </div>
      <div class="card-desc">
        Microservices-based e-commerce ecosystem with Node.js BFF orchestration, Laravel Lumen domain services, Strapi headless CMS, and Keycloak security.
      </div>
      <div class="card-tech">
        <span class="pill">Node.js / Express</span>
        <span class="pill">PHP 8 / Lumen</span>
        <span class="pill">Strapi CMS</span>
        <span class="pill">GitLab CI/CD</span>
      </div>
    </div>

    <!-- Project 4 -->
    <div class="project-card">
      <div class="card-top">
        <div class="card-title">Al Ain Museum & Holsten Arabia</div>
        <div class="client-tag">UAE & Global Brand</div>
      </div>
      <div class="card-desc">
        Next.js & React headless CMS digital experiences using TypeScript, Sitecore Helix, Umbraco CMS, and custom C#/.NET integrations.
      </div>
      <div class="card-tech">
        <span class="pill">Next.js</span>
        <span class="pill">React / TypeScript</span>
        <span class="pill">C# / .NET</span>
        <span class="pill">Sitecore / Umbraco</span>
      </div>
    </div>
  </div>

  <div class="footer-cta">
    <div>
      <div class="cta-text">Ready to bring enterprise quality to your custom web application</div>
      <div class="cta-sub">Clean code · Comprehensive testing · 4+ years software company experience</div>
    </div>
    <div class="btn-contact">Viranga Lakshan</div>
  </div>
</body>
</html>"""

# ----------------- BANNER 3: ARCHITECTURE & RELIABILITY -----------------
html_banner_3 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 80% 80%, #064e3b 0%, #0f172a 50%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 55px 70px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .glow-1 {
    position: absolute;
    bottom: -80px;
    right: -80px;
    width: 450px;
    height: 450px;
    background: rgba(16, 185, 129, 0.2);
    filter: blur(130px);
    border-radius: 50%;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1.5px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 16px;
    position: relative;
    z-index: 2;
  }
  .header h2 {
    font-size: 32px;
    font-weight: 900;
    color: #ffffff;
  }
  .header h2 span {
    color: #34d399;
  }
  .header-subtitle {
    font-size: 14px;
    color: #94a3b8;
    margin-top: 4px;
  }

  /* 3 Architecture Pillars */
  .pillars-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin: auto 0;
    position: relative;
    z-index: 2;
  }
  .pillar-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    padding: 24px 20px;
    border-top: 4px solid #10b981;
  }
  .pillar-card:nth-child(2) { border-top-color: #38bdf8; }
  .pillar-card:nth-child(3) { border-top-color: #818cf8; }

  .pillar-icon {
    font-size: 32px;
    margin-bottom: 12px;
  }
  .pillar-title {
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
  }
  .pillar-desc {
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.5;
  }
  .pillar-list {
    margin-top: 14px;
    list-style: none;
    font-size: 12px;
    color: #cbd5e1;
  }
  .pillar-list li {
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .pillar-list li::before {
    content: "✓";
    color: #34d399;
    font-weight: bold;
  }

  /* Bottom Trust Strip */
  .trust-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px 24px;
    position: relative;
    z-index: 2;
  }
  .trust-item {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .trust-icon {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(52, 211, 153, 0.15);
    color: #34d399;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 16px;
  }
  .trust-title {
    font-size: 13px;
    font-weight: 700;
    color: #ffffff;
  }
  .trust-desc {
    font-size: 11px;
    color: #94a3b8;
  }
</style>
</head>
<body>
  <div class="glow-1"></div>

  <div class="header">
    <div>
      <h2>Architecture & Engineering Standards</h2>
      <div class="header-subtitle">Engineered for maintainability, high concurrency, and zero downtime</div>
    </div>
  </div>

  <div class="pillars-grid">
    <div class="pillar-card">
      <div class="pillar-icon">🏛️</div>
      <div class="pillar-title">Clean Architecture & DDD</div>
      <div class="pillar-desc">
        Modular services built with Domain-Driven Design principles to ensure low coupling and high maintainability.
      </div>
      <ul class="pillar-list">
        <li>Spring Modulith & DDD</li>
        <li>OpenAPI (Swagger) Contracts</li>
        <li>Layered Controller-Service-Repo</li>
      </ul>
    </div>

    <div class="pillar-card">
      <div class="pillar-icon">⚡</div>
      <div class="pillar-title">High Speed & Reliability</div>
      <div class="pillar-desc">
        Asynchronous event processing and multi-level caching ensuring sub-second response times under heavy loads.
      </div>
      <ul class="pillar-list">
        <li>Apache Kafka Event Streams</li>
        <li>Redis Caching & Session Stores</li>
        <li>Flyway Automated Migrations</li>
      </ul>
    </div>

    <div class="pillar-card">
      <div class="pillar-icon">🔒</div>
      <div class="pillar-title">Security & DevOps Ready</div>
      <div class="pillar-desc">
        Enterprise authentication protocols and automated CI/CD deployment pipelines with automated quality gates.
      </div>
      <ul class="pillar-list">
        <li>Keycloak (OAuth2 / OIDC / JWT)</li>
        <li>Docker & Kubernetes Ready</li>
        <li>SonarQube Quality Standards</li>
      </ul>
    </div>
  </div>

  <div class="trust-strip">
    <div class="trust-item">
      <div class="trust-icon">★</div>
      <div>
        <div class="trust-title">Independent Execution</div>
        <div class="trust-desc">Self-driven with transparent daily updates</div>
      </div>
    </div>
    <div class="trust-item">
      <div class="trust-icon">💬</div>
      <div>
        <div class="trust-title">Fast Communication</div>
        <div class="trust-desc">Responsive via Slack, Teams & Upwork</div>
      </div>
    </div>
    <div class="trust-item">
      <div class="trust-icon">🚀</div>
      <div>
        <div class="trust-title">Production Quality</div>
        <div class="trust-desc">Tested, documented & ready to deploy</div>
      </div>
    </div>
  </div>
</body>
</html>"""

banners = [
    ("banner_1_fullstack.html", "Upwork_Project_Banner_1_FullStack.png", html_banner_1),
    ("banner_2_projects.html", "Upwork_Project_Banner_2_EnterpriseProjects.png", html_banner_2),
    ("banner_3_architecture.html", "Upwork_Project_Banner_3_Architecture.png", html_banner_3),
]

for html_file, png_file, content in banners:
    html_abs = os.path.abspath(html_file)
    png_abs = os.path.abspath(png_file)
    with open(html_abs, "w", encoding="utf-8") as f:
        f.write(content)
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,800",
        f"--screenshot={png_abs}",
        "file:///" + html_abs.replace("\\", "/")
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {png_file} (Size: {os.path.getsize(png_abs)} bytes)")
    if os.path.exists(html_abs):
        os.remove(html_abs)

print("All 3 Upwork banners successfully generated!")

