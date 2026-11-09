import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ----------------- PORTFOLIO IMAGE: PROJECT 01 (MULTI-TENANT E-COMMERCE) -----------------
html_p1 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 85% 15%, #1e1b4b 0%, #0f172a 55%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 75px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .glow-purple {
    position: absolute;
    top: -90px; right: -90px;
    width: 520px; height: 520px;
    background: rgba(139, 92, 246, 0.2);
    filter: blur(140px);
    border-radius: 50%;
  }
  .top-meta {
    display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2;
  }
  .client-badge {
    background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.4);
    color: #c084fc; padding: 7px 18px; border-radius: 30px; font-size: 13px; font-weight: 800;
    letter-spacing: 0.5px; text-transform: uppercase;
  }
  .company-label { font-size: 14px; color: #94a3b8; font-weight: 600; }
  .company-label strong { color: #38bdf8; }
  .hero { position: relative; z-index: 2; margin: 20px 0; }
  .project-tag { color: #c084fc; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
  .project-title {
    font-size: 46px; font-weight: 900; line-height: 1.15; letter-spacing: -1.2px; margin-bottom: 14px;
    background: linear-gradient(135deg, #ffffff 40%, #e9d5ff 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .project-desc { font-size: 18px; color: #cbd5e1; max-width: 900px; line-height: 1.5; }
  .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; position: relative; z-index: 2; margin-bottom: 14px; }
  .feature-card {
    background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px; padding: 16px 18px; border-left: 3.5px solid #8b5cf6;
  }
  .feature-card:nth-child(2) { border-left-color: #38bdf8; }
  .feature-card:nth-child(3) { border-left-color: #10b981; }
  .feature-title { font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 4px; }
  .feature-text { font-size: 12px; color: #94a3b8; line-height: 1.4; }
  .tech-pills { display: flex; flex-wrap: wrap; gap: 8px; position: relative; z-index: 2; }
  .tech-pill {
    background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 7px 15px; border-radius: 8px; font-size: 13px; font-weight: 700; color: #f1f5f9;
  }
  .tech-pill.highlight { background: rgba(139, 92, 246, 0.2); border-color: #8b5cf6; color: #c084fc; }
  .footer-bar {
    display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px; position: relative; z-index: 2; font-size: 13px; color: #94a3b8;
  }
  .author-tag { font-weight: 700; color: #ffffff; }
  .role-tag { color: #c084fc; font-weight: 700; }
</style>
</head>
<body>
  <div class="glow-purple"></div>
  <div class="top-meta">
    <div class="client-badge">🛒 Enterprise E-Commerce Platform</div>
    <div class="company-label">Built at: <strong>Arimac Digital</strong></div>
  </div>
  <div class="hero">
    <div class="project-tag">Distributed Microservices Architecture</div>
    <div class="project-title">Multi-Tenant E-Commerce Platform<br>Node.js BFF & Laravel Lumen</div>
    <div class="project-desc">
      Architecting high-concurrency microservices, multi-tenant isolation, customer and admin BFF orchestration, and Strapi headless CMS integrations.
    </div>
  </div>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-title">Node.js BFF Orchestration</div>
      <div class="feature-text">API gateway aggregating multi-domain services for mobile and web portals.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Domain Microservices</div>
      <div class="feature-text">Orders, payments, shipping, products, promotions, and tenant management services.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Keycloak OAuth2 / OIDC</div>
      <div class="feature-text">Centralized token validation, role-based access control, and Docker CI/CD pipelines.</div>
    </div>
  </div>
  <div class="tech-pills">
    <div class="tech-pill highlight">Node.js</div>
    <div class="tech-pill highlight">Express.js</div>
    <div class="tech-pill highlight">PHP 8 / Lumen</div>
    <div class="tech-pill">Strapi CMS</div>
    <div class="tech-pill">Keycloak (OAuth2/JWT)</div>
    <div class="tech-pill">Docker</div>
    <div class="tech-pill">GitLab CI/CD</div>
    <div class="tech-pill">MySQL</div>
  </div>
  <div class="footer-bar">
    <div class="author-tag">Viranga Lakshan · <span class="role-tag">Backend & Full Stack Developer</span></div>
    <div>Arimac Digital — Enterprise E-Commerce Platform</div>
  </div>
</body>
</html>"""

# ----------------- PORTFOLIO IMAGE: PROJECT 02 (ADRIK MEDIA KUWAIT) -----------------
html_p2 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 85% 15%, #0c4a6e 0%, #0f172a 55%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 75px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .glow-cyan {
    position: absolute;
    top: -90px; right: -90px;
    width: 520px; height: 520px;
    background: rgba(6, 182, 212, 0.2);
    filter: blur(140px);
    border-radius: 50%;
  }
  .top-meta {
    display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2;
  }
  .client-badge {
    background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.4);
    color: #38bdf8; padding: 7px 18px; border-radius: 30px; font-size: 13px; font-weight: 800;
    letter-spacing: 0.5px; text-transform: uppercase;
  }
  .company-label { font-size: 14px; color: #94a3b8; font-weight: 600; }
  .company-label strong { color: #38bdf8; }
  .hero { position: relative; z-index: 2; margin: 20px 0; }
  .project-tag { color: #38bdf8; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
  .project-title {
    font-size: 46px; font-weight: 900; line-height: 1.15; letter-spacing: -1.2px; margin-bottom: 14px;
    background: linear-gradient(135deg, #ffffff 40%, #bae6fd 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .project-desc { font-size: 18px; color: #cbd5e1; max-width: 900px; line-height: 1.5; }
  .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; position: relative; z-index: 2; margin-bottom: 14px; }
  .feature-card {
    background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px; padding: 16px 18px; border-left: 3.5px solid #06b6d4;
  }
  .feature-card:nth-child(2) { border-left-color: #3b82f6; }
  .feature-card:nth-child(3) { border-left-color: #10b981; }
  .feature-title { font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 4px; }
  .feature-text { font-size: 12px; color: #94a3b8; line-height: 1.4; }
  .tech-pills { display: flex; flex-wrap: wrap; gap: 8px; position: relative; z-index: 2; }
  .tech-pill {
    background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 7px 15px; border-radius: 8px; font-size: 13px; font-weight: 700; color: #f1f5f9;
  }
  .tech-pill.highlight { background: rgba(6, 182, 212, 0.2); border-color: #06b6d4; color: #38bdf8; }
  .footer-bar {
    display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px; position: relative; z-index: 2; font-size: 13px; color: #94a3b8;
  }
  .author-tag { font-weight: 700; color: #ffffff; }
  .role-tag { color: #38bdf8; font-weight: 700; }
</style>
</head>
<body>
  <div class="glow-cyan"></div>
  <div class="top-meta">
    <div class="client-badge">🇰🇼 Client: Adrik (Kuwait)</div>
    <div class="company-label">Built at: <strong>Arimac Digital</strong></div>
  </div>
  <div class="hero">
    <div class="project-tag">High-Concurrency Media Platform</div>
    <div class="project-title">Adrik News & Media Platform<br>Node.js BFF & Kubernetes</div>
    <div class="project-desc">
      Bilingual (Arabic/English) media ecosystem serving thousands of active readers with real-time push notifications, subscriptions, and mobile BFF services.
    </div>
  </div>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-title">3 Node.js BFF Services</div>
      <div class="feature-text">High-performance gateways connecting Web, iOS/Android, and Admin portals.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Push Notifications & SMS</div>
      <div class="feature-text">OneSignal real-time breaking alerts and SMS gateway transactional delivery.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Kubernetes & CI/CD</div>
      <div class="feature-text">Docker containerization deployed across dev, UAT, and prod Kubernetes clusters.</div>
    </div>
  </div>
  <div class="tech-pills">
    <div class="tech-pill highlight">Node.js</div>
    <div class="tech-pill highlight">Express.js</div>
    <div class="tech-pill highlight">Kubernetes</div>
    <div class="tech-pill">Docker</div>
    <div class="tech-pill">Keycloak (OAuth2/JWT)</div>
    <div class="tech-pill">OneSignal Push</div>
    <div class="tech-pill">SMS Gateway API</div>
    <div class="tech-pill">GitLab CI/CD</div>
  </div>
  <div class="footer-bar">
    <div class="author-tag">Viranga Lakshan · <span class="role-tag">Backend Developer</span></div>
    <div>Arimac Digital — Client: Adrik, Kuwait</div>
  </div>
</body>
</html>"""

# ----------------- PORTFOLIO IMAGE: PROJECT 03 (DIMO LANKA GATE PASS) -----------------
html_p3 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 85% 15%, #0f2b5c 0%, #0f172a 55%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 75px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .glow-blue {
    position: absolute;
    top: -90px; right: -90px;
    width: 520px; height: 520px;
    background: rgba(37, 99, 235, 0.25);
    filter: blur(140px);
    border-radius: 50%;
  }
  .top-meta {
    display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 2;
  }
  .client-badge {
    background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4);
    color: #60a5fa; padding: 7px 18px; border-radius: 30px; font-size: 13px; font-weight: 800;
    letter-spacing: 0.5px; text-transform: uppercase;
  }
  .company-label { font-size: 14px; color: #94a3b8; font-weight: 600; }
  .company-label strong { color: #38bdf8; }
  .hero { position: relative; z-index: 2; margin: 20px 0; }
  .project-tag { color: #60a5fa; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
  .project-title {
    font-size: 46px; font-weight: 900; line-height: 1.15; letter-spacing: -1.2px; margin-bottom: 14px;
    background: linear-gradient(135deg, #ffffff 40%, #bfdbfe 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .project-desc { font-size: 18px; color: #cbd5e1; max-width: 900px; line-height: 1.5; }
  .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; position: relative; z-index: 2; margin-bottom: 14px; }
  .feature-card {
    background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px; padding: 16px 18px; border-left: 3.5px solid #2563eb;
  }
  .feature-card:nth-child(2) { border-left-color: #10b981; }
  .feature-card:nth-child(3) { border-left-color: #a855f7; }
  .feature-title { font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 4px; }
  .feature-text { font-size: 12px; color: #94a3b8; line-height: 1.4; }
  .tech-pills { display: flex; flex-wrap: wrap; gap: 8px; position: relative; z-index: 2; }
  .tech-pill {
    background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 7px 15px; border-radius: 8px; font-size: 13px; font-weight: 700; color: #f1f5f9;
  }
  .tech-pill.highlight { background: rgba(37, 99, 235, 0.25); border-color: #3b82f6; color: #93c5fd; }
  .footer-bar {
    display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px; position: relative; z-index: 2; font-size: 13px; color: #94a3b8;
  }
  .author-tag { font-weight: 700; color: #ffffff; }
  .role-tag { color: #60a5fa; font-weight: 700; }
</style>
</head>
<body>
  <div class="glow-blue"></div>
  <div class="top-meta">
    <div class="client-badge">🚗 Enterprise Client: DIMO Lanka</div>
    <div class="company-label">Built at: <strong>Arimac Digital</strong></div>
  </div>
  <div class="hero">
    <div class="project-tag">Enterprise Spring Boot Microservices</div>
    <div class="project-title">DIMO Gate Pass Management<br>Spring Boot 3.4.5 & Kafka</div>
    <div class="project-desc">
      Enterprise vehicle dispatch platform handling Keycloak OAuth2/JWT authentication, Kafka audit event publishing, SAP integrations, and MySQL schema migrations with Flyway.
    </div>
  </div>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-title">Spring Boot 3.4.5 & Java 21</div>
      <div class="feature-text">Two microservices: BFF/API gateway and Gate Pass core domain service.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Kafka Audit Streaming</div>
      <div class="feature-text">Asynchronous event publishing for audit tracking and approval workflows.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">SAP & Azure AD Integration</div>
      <div class="feature-text">Secure REST integrations with SAP, Google Maps, AWS S3 with ClamAV, and Azure AD.</div>
    </div>
  </div>
  <div class="tech-pills">
    <div class="tech-pill highlight">Java 21</div>
    <div class="tech-pill highlight">Spring Boot 3.4.5</div>
    <div class="tech-pill highlight">Spring Kafka</div>
    <div class="tech-pill">Spring Security</div>
    <div class="tech-pill">Keycloak (OAuth2/JWT)</div>
    <div class="tech-pill">MySQL / Flyway</div>
    <div class="tech-pill">Docker</div>
    <div class="tech-pill">AWS S3</div>
  </div>
  <div class="footer-bar">
    <div class="author-tag">Viranga Lakshan · <span class="role-tag">Backend Developer</span></div>
    <div>Arimac Digital — Client: DIMO Lanka</div>
  </div>
</body>
</html>"""

images = [
    ("temp_p1.html", "Upwork_Portfolio_Project_01_Ecommerce.png", html_p1),
    ("temp_p2.html", "Upwork_Portfolio_Project_02_AdrikMedia.png", html_p2),
    ("temp_p3.html", "Upwork_Portfolio_Project_03_DIMOGatePass.png", html_p3),
]

for html_file, png_file, content in images:
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

print("All Portfolio Project images successfully generated!")
