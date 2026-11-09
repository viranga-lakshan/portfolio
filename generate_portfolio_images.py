import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ----------------- PORTFOLIO IMAGE: PROJECT 04 (AL AIN MUSEUM) -----------------
html_p4 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 85% 15%, #2a1b0a 0%, #0f172a 55%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 75px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .glow-gold {
    position: absolute;
    top: -90px;
    right: -90px;
    width: 520px;
    height: 520px;
    background: rgba(245, 158, 11, 0.18);
    filter: blur(140px);
    border-radius: 50%;
  }

  /* Header */
  .top-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .client-badge {
    background: rgba(245, 158, 11, 0.15);
    border: 1px solid rgba(245, 158, 11, 0.4);
    color: #fbbf24;
    padding: 7px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .company-label {
    font-size: 14px;
    color: #94a3b8;
    font-weight: 600;
  }
  .company-label strong {
    color: #38bdf8;
  }

  /* Hero */
  .hero {
    position: relative;
    z-index: 2;
    margin: 20px 0;
  }
  .project-tag {
    color: #38bdf8;
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
  }
  .project-title {
    font-size: 46px;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -1.2px;
    margin-bottom: 14px;
    background: linear-gradient(135deg, #ffffff 40%, #fed7aa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .project-desc {
    font-size: 18px;
    color: #cbd5e1;
    max-width: 900px;
    line-height: 1.5;
  }

  /* Feature Grid */
  .features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    position: relative;
    z-index: 2;
    margin-bottom: 14px;
  }
  .feature-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px 18px;
    border-left: 3.5px solid #f59e0b;
  }
  .feature-card:nth-child(2) { border-left-color: #38bdf8; }
  .feature-card:nth-child(3) { border-left-color: #a855f7; }

  .feature-title {
    font-size: 14px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }
  .feature-text {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.4;
  }

  /* Tech Pills */
  .tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    position: relative;
    z-index: 2;
  }
  .tech-pill {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 7px 15px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    color: #f1f5f9;
  }
  .tech-pill.highlight {
    background: rgba(245, 158, 11, 0.2);
    border-color: #f59e0b;
    color: #fbbf24;
  }

  /* Footer */
  .footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px;
    position: relative;
    z-index: 2;
    font-size: 13px;
    color: #94a3b8;
  }
  .author-tag {
    font-weight: 700;
    color: #ffffff;
  }
  .role-tag {
    color: #38bdf8;
    font-weight: 700;
  }
</style>
</head>
<body>
  <div class="glow-gold"></div>

  <div class="top-meta">
    <div class="client-badge">🏛️ UAE Cultural Institution</div>
    <div class="company-label">Built at: <strong>Arimac Digital</strong></div>
  </div>

  <div class="hero">
    <div class="project-tag">Enterprise Headless CMS Platform</div>
    <div class="project-title">Al Ain Museum V2<br>Sitecore Headless & Next.js</div>
    <div class="project-desc">
      Architecting the multi-site rebuild for UAE’s national cultural landmark using Next.js, React, TypeScript, and Sitecore Helix modular principles.
    </div>
  </div>

  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-title">Next.js & React Frontend</div>
      <div class="feature-text">High-performance responsive rendering following Sitecore Helix architecture standards.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">REST API Retrieval Engine</div>
      <div class="feature-text">Engineered direct REST integration for granular control over content presentation.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">C# & .NET Customization</div>
      <div class="feature-text">Customized server components to recursively traverse complex nested CMS hierarchies.</div>
    </div>
  </div>

  <div class="tech-pills">
    <div class="tech-pill highlight">Next.js</div>
    <div class="tech-pill highlight">React</div>
    <div class="tech-pill">TypeScript</div>
    <div class="tech-pill highlight">Sitecore Headless CMS</div>
    <div class="tech-pill">Sitecore JSS</div>
    <div class="tech-pill">C# / .NET</div>
    <div class="tech-pill">REST APIs</div>
  </div>

  <div class="footer-bar">
    <div class="author-tag">Viranga Lakshan · <span class="role-tag">Frontend & CMS Developer</span></div>
    <div>Arimac Digital — Client: Al Ain Museum, UAE</div>
  </div>
</body>
</html>"""

# ----------------- PORTFOLIO IMAGE: PROJECT 05 (HOLSTEN ARABIA) -----------------
html_p5 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');
  * { margin:0; padding:0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 800px;
    background: radial-gradient(circle at 85% 15%, #064e3b 0%, #0f172a 55%, #020617 100%);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff;
    padding: 60px 75px;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .glow-emerald {
    position: absolute;
    top: -90px;
    right: -90px;
    width: 520px;
    height: 520px;
    background: rgba(16, 185, 129, 0.2);
    filter: blur(140px);
    border-radius: 50%;
  }

  /* Header */
  .top-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 2;
  }
  .client-badge {
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #34d399;
    padding: 7px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .company-label {
    font-size: 14px;
    color: #94a3b8;
    font-weight: 600;
  }
  .company-label strong {
    color: #38bdf8;
  }

  /* Hero */
  .hero {
    position: relative;
    z-index: 2;
    margin: 20px 0;
  }
  .project-tag {
    color: #34d399;
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
  }
  .project-title {
    font-size: 46px;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -1.2px;
    margin-bottom: 14px;
    background: linear-gradient(135deg, #ffffff 40%, #a7f3d0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .project-desc {
    font-size: 18px;
    color: #cbd5e1;
    max-width: 900px;
    line-height: 1.5;
  }

  /* Feature Grid */
  .features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    position: relative;
    z-index: 2;
    margin-bottom: 14px;
  }
  .feature-card {
    background: rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px 18px;
    border-left: 3.5px solid #10b981;
  }
  .feature-card:nth-child(2) { border-left-color: #06b6d4; }
  .feature-card:nth-child(3) { border-left-color: #3b82f6; }

  .feature-title {
    font-size: 14px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }
  .feature-text {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.4;
  }

  /* Tech Pills */
  .tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    position: relative;
    z-index: 2;
  }
  .tech-pill {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 7px 15px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    color: #f1f5f9;
  }
  .tech-pill.highlight {
    background: rgba(16, 185, 129, 0.2);
    border-color: #10b981;
    color: #34d399;
  }

  /* Footer */
  .footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 18px;
    position: relative;
    z-index: 2;
    font-size: 13px;
    color: #94a3b8;
  }
  .author-tag {
    font-weight: 700;
    color: #ffffff;
  }
  .role-tag {
    color: #34d399;
    font-weight: 700;
  }
</style>
</head>
<body>
  <div class="glow-emerald"></div>

  <div class="top-meta">
    <div class="client-badge">🌍 Global Beverage Brand</div>
    <div class="company-label">Built at: <strong>Arimac Digital</strong></div>
  </div>

  <div class="hero">
    <div class="project-tag">Multilingual Headless CMS Platform</div>
    <div class="project-title">Holsten Arabia<br>Umbraco Headless & Next.js</div>
    <div class="project-desc">
      Delivering a localized, high-speed digital experience for a global brand using Umbraco Headless CMS, modern Next.js/React frontend, and custom C#/.NET components.
    </div>
  </div>

  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-title">Next.js & TypeScript UI</div>
      <div class="feature-text">High-speed, responsive frontend delivering an engaging multilingual user journey.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">Umbraco Headless CMS</div>
      <div class="feature-text">Architected custom content types, components, and media integration via REST APIs.</div>
    </div>
    <div class="feature-card">
      <div class="feature-title">C# & .NET Integrations</div>
      <div class="feature-text">Customized server-side components and data delivery pipelines for peak performance.</div>
    </div>
  </div>

  <div class="tech-pills">
    <div class="tech-pill highlight">Next.js</div>
    <div class="tech-pill highlight">React</div>
    <div class="tech-pill">TypeScript</div>
    <div class="tech-pill highlight">Umbraco CMS</div>
    <div class="tech-pill">C# / .NET</div>
    <div class="tech-pill">RESTful APIs</div>
    <div class="tech-pill">Responsive UX</div>
  </div>

  <div class="footer-bar">
    <div class="author-tag">Viranga Lakshan · <span class="role-tag">Frontend & CMS Developer</span></div>
    <div>Arimac Digital — Client: Holsten Arabia</div>
  </div>
</body>
</html>"""

images = [
    ("temp_p4.html", "Upwork_Portfolio_Project_04_AlAinMuseum.png", html_p4),
    ("temp_p5.html", "Upwork_Portfolio_Project_05_HolstenArabia.png", html_p5),
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

print("Both Portfolio Project images successfully generated!")

