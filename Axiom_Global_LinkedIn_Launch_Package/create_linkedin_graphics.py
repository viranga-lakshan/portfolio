import os
import asyncio
from playwright.async_api import async_playwright

OUT_DIR = r"c:\Users\Viranga\Downloads\upwrok new\Axiom_Global_LinkedIn_Launch_Package"
IMG_DIR = os.path.join(OUT_DIR, "images")
ASSET_DIR = os.path.join(OUT_DIR, "assets")
os.makedirs(IMG_DIR, exist_ok=True)

LOGO_PATH = os.path.join(ASSET_DIR, "axiom_logo_square.png").replace("\\", "/")

# Shared CSS styles
SHARED_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

body {{
    width: 1200px;
    height: 1200px;
    overflow: hidden;
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    -webkit-font-smoothing: antialiased;
    position: relative;
}}

/* Top Brand Header */
.brand-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    position: relative;
    z-index: 10;
}}

.brand-left {{
    display: flex;
    align-items: center;
    gap: 18px;
}}

.brand-logo-img {{
    width: 64px;
    height: 64px;
    border-radius: 14px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
}}

.brand-text-block {{
    display: flex;
    flex-direction: column;
}}

.brand-name {{
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.5px;
}}

.brand-tagline {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.9;
}}

.brand-badge {{
    font-size: 13px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 999px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}}

/* Bottom Footer (Clean, elegant, no URLs, no locations) */
.brand-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: auto;
    position: relative;
    z-index: 10;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 24px;
}}

.brand-footer.light {{
    border-top: 1.5px solid #F0CDD3;
}}

.footer-tagline {{
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #F4A5AE;
}}

.footer-action {{
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.5px;
}}

/* Ambient wine glow elements for light themes */
.ambient-wine-glow-1 {{
    position: absolute;
    width: 650px;
    height: 650px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(107, 20, 34, 0.12) 0%, rgba(107, 20, 34, 0) 70%);
    top: -120px;
    right: -100px;
    pointer-events: none;
    z-index: 1;
}}

.ambient-wine-glow-2 {{
    position: absolute;
    width: 550px;
    height: 550px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139, 30, 45, 0.08) 0%, rgba(139, 30, 45, 0) 70%);
    bottom: -80px;
    left: -80px;
    pointer-events: none;
    z-index: 1;
}}
"""

HTML_TEMPLATES = {
    # 1. Company Launch (Dark Wine Velvet Theme)
    "post_1_announcement.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 85% 15%, #6B1422 0%, #400B13 45%, #220509 100%);
    color: #FFFFFF;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #FFFFFF; }}
.brand-tagline {{ color: #F4A5AE; }}
.brand-badge {{ background: rgba(255, 255, 255, 0.12); color: #FFFFFF; border: 1px solid rgba(255, 255, 255, 0.2); }}

.hero-content {{
    margin-top: 60px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    z-index: 5;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #8B1E2D;
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 8px 18px;
    border-radius: 999px;
    box-shadow: 0 4px 15px rgba(139, 30, 45, 0.4);
}}

.main-title {{
    font-size: 74px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -2px;
}}

.main-title span.accent {{
    color: #F8B4BD;
    background: linear-gradient(90deg, #F8B4BD 0%, #FFFFFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.lead-text {{
    font-size: 24px;
    font-weight: 400;
    line-height: 1.5;
    color: #E2E8F0;
    max-width: 900px;
    margin-top: 10px;
}}

.pillars-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
}}

.pillar-card {{
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 20px;
    padding: 30px 26px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}}

.pillar-icon {{
    font-size: 32px;
}}

.pillar-title {{
    font-size: 20px;
    font-weight: 700;
    color: #FFFFFF;
}}

.pillar-desc {{
    font-size: 15px;
    line-height: 1.45;
    color: #CBD5E1;
}}

.ambient-glow {{
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: rgba(139, 30, 45, 0.25);
    filter: blur(120px);
    top: -100px;
    right: -100px;
    pointer-events: none;
}}
</style>
</head>
<body>
<div class="ambient-glow"></div>

<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">Official Announcement</div>
</div>

<div class="hero-content">
    <div class="category-pill">● Launching Worldwide</div>
    <div class="main-title">
        Engineering<br>
        <span class="accent">Intelligence.</span>
    </div>
    <div class="lead-text">
        We bridge the gap between enterprise-grade full-stack engineering and production AI workflows. Transforming complex challenges into scalable digital powerhouses.
    </div>

    <div class="pillars-grid">
        <div class="pillar-card">
            <div class="pillar-icon">⚡</div>
            <div class="pillar-title">Scalable SaaS Systems</div>
            <div class="pillar-desc">Sub-second reactive architectures built with Next.js, Node.js & high-concurrency microservices.</div>
        </div>
        <div class="pillar-card">
            <div class="pillar-icon">🤖</div>
            <div class="pillar-title">Production AI Workflows</div>
            <div class="pillar-desc">Conversational concierges, predictive routing, and autonomous agent systems designed for real ROI.</div>
        </div>
        <div class="pillar-card">
            <div class="pillar-icon">🛡️</div>
            <div class="pillar-title">Enterprise Reliability</div>
            <div class="pillar-desc">Mission-critical platforms built for Healthcare, Logistics, FinTech and Global PropTech.</div>
        </div>
    </div>
</div>

<div class="brand-footer">
    <div class="footer-tagline">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#F4A5AE;">Enterprise AI & Systems Engineering ➔</div>
</div>
</body>
</html>""",

    # 2. Capability Matrix (White Background Mixed with Wine Red Logo Color)
    "post_2_capabilities.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 85% 15%, #FDEEEF 0%, #FFF5F7 35%, #FFFFFF 68%, #FBF0F2 100%);
    color: #0F172A;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #4A0E17; }}
.brand-tagline {{ color: #8B1E2D; }}
.brand-badge {{ background: #FCE8EC; color: #6B1422; border: 1.5px solid #F0CDD3; }}

.hero-content {{
    margin-top: 45px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: relative;
    z-index: 5;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #6B1422;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 7px 16px;
    border-radius: 999px;
    box-shadow: 0 4px 14px rgba(107, 20, 34, 0.25);
}}

.main-title {{
    font-size: 60px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #0F172A;
}}

.main-title span.wine {{
    color: #6B1422;
}}

.lead-text {{
    font-size: 21px;
    font-weight: 400;
    line-height: 1.45;
    color: #475569;
    max-width: 960px;
}}

.bento-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
    margin-top: 30px;
}}

.bento-card {{
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(12px);
    border: 1.5px solid #F0CDD3;
    border-radius: 20px;
    padding: 28px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: relative;
    box-shadow: 0 10px 28px rgba(74, 14, 23, 0.05);
}}

.bento-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.bento-number {{
    font-size: 14px;
    font-weight: 800;
    color: #8B1E2D;
    background: #FCE8EC;
    padding: 4px 12px;
    border-radius: 6px;
}}

.bento-icon {{
    font-size: 28px;
}}

.bento-title {{
    font-size: 22px;
    font-weight: 700;
    color: #0F172A;
}}

.bento-desc {{
    font-size: 15px;
    line-height: 1.5;
    color: #475569;
}}

.bento-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 6px;
}}

.bento-tag {{
    font-size: 12px;
    font-weight: 600;
    background: #FFF5F7;
    border: 1px solid #F0CDD3;
    padding: 4px 10px;
    border-radius: 6px;
    color: #6B1422;
}}
</style>
</head>
<body>
<div class="ambient-wine-glow-1"></div>
<div class="ambient-wine-glow-2"></div>

<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">Solutions Matrix</div>
</div>

<div class="hero-content">
    <div class="category-pill">Core Engineering Pillars</div>
    <div class="main-title">What We Build: <span class="wine">The Axiom Stack</span></div>
    <div class="lead-text">
        From whiteboard architecture to high-throughput platforms, we provide complete lifecycle engineering for fast-scaling enterprises.
    </div>

    <div class="bento-grid">
        <div class="bento-card">
            <div class="bento-header">
                <span class="bento-number">01</span>
                <span class="bento-icon">🤖</span>
            </div>
            <div class="bento-title">AI Workflows & Agents</div>
            <div class="bento-desc">Custom LLM agents, automated document extraction, 24/7 client concierges, and predictive analytics engines.</div>
            <div class="bento-tags">
                <span class="bento-tag">LangChain</span>
                <span class="bento-tag">Vector DBs</span>
                <span class="bento-tag">RAG Pipelines</span>
            </div>
        </div>

        <div class="bento-card">
            <div class="bento-header">
                <span class="bento-number">02</span>
                <span class="bento-icon">⚡</span>
            </div>
            <div class="bento-title">Full-Stack Web & SaaS</div>
            <div class="bento-desc">High-speed, reactive applications with bulletproof state management, modern APIs, and clean UX design.</div>
            <div class="bento-tags">
                <span class="bento-tag">Next.js 14</span>
                <span class="bento-tag">React</span>
                <span class="bento-tag">Node.js</span>
                <span class="bento-tag">GraphQL</span>
            </div>
        </div>

        <div class="bento-card">
            <div class="bento-header">
                <span class="bento-number">03</span>
                <span class="bento-icon">🏥</span>
            </div>
            <div class="bento-title">Healthcare & Regulated Tech</div>
            <div class="bento-desc">HIPAA-conscious clinical scheduling, multi-pharmacy APIs, and zero-fail patient workflow systems.</div>
            <div class="bento-tags">
                <span class="bento-tag">Clinical Sync</span>
                <span class="bento-tag">E-Rx APIs</span>
                <span class="bento-tag">Audit Trails</span>
            </div>
        </div>

        <div class="bento-card">
            <div class="bento-header">
                <span class="bento-number">04</span>
                <span class="bento-icon">📦</span>
            </div>
            <div class="bento-title">Logistics & Real Estate Engines</div>
            <div class="bento-desc">Automated 2-way calendar viewing bookings, multi-carrier freight rate calculations, and live GPS pins.</div>
            <div class="bento-tags">
                <span class="bento-tag">CalSync</span>
                <span class="bento-tag">WhatsApp API</span>
                <span class="bento-tag">Freight Aggregation</span>
            </div>
        </div>
    </div>
</div>

<div class="brand-footer light">
    <div class="footer-tagline" style="color:#6B1422;">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#6B1422;">Enterprise Architecture ➔</div>
</div>
</body>
</html>""",

    # 3. PropTech Case Study / Problem Fix (Dark Wine Velvet Theme)
    "post_3_proptech_case.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 80% 20%, #5C121D 0%, #36080E 50%, #1A0307 100%);
    color: #FFFFFF;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #FFFFFF; }}
.brand-tagline {{ color: #F4A5AE; }}
.brand-badge {{ background: rgba(255, 255, 255, 0.12); color: #FFFFFF; border: 1px solid rgba(255, 255, 255, 0.2); }}

.hero-content {{
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #A32436;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 7px 16px;
    border-radius: 999px;
}}

.main-title {{
    font-size: 64px;
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -1.5px;
}}

.main-title span.leak {{
    color: #FFA5B0;
}}

.stat-split {{
    display: grid;
    grid-template-columns: 360px 1fr;
    gap: 28px;
    margin-top: 25px;
}}

.stat-card-big {{
    background: linear-gradient(135deg, rgba(163, 36, 54, 0.35) 0%, rgba(54, 8, 14, 0.6) 100%);
    border: 1.5px solid rgba(255, 255, 255, 0.18);
    border-radius: 24px;
    padding: 38px 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 12px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
}}

.big-number {{
    font-size: 96px;
    font-weight: 800;
    line-height: 1;
    color: #FFFFFF;
    letter-spacing: -2px;
}}

.big-number span {{
    color: #F8B4BD;
    font-size: 60px;
}}

.stat-caption {{
    font-size: 18px;
    line-height: 1.45;
    color: #E2E8F0;
}}

.solution-box {{
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 34px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 18px;
}}

.solution-title {{
    font-size: 21px;
    font-weight: 700;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.feature-row {{
    display: flex;
    align-items: flex-start;
    gap: 16px;
}}

.feature-check {{
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #10B981;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 800;
    flex-shrink: 0;
    margin-top: 2px;
}}

.feature-text {{
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.feature-h {{
    font-size: 17px;
    font-weight: 700;
    color: #FFFFFF;
}}

.feature-p {{
    font-size: 14px;
    color: #CBD5E1;
    line-height: 1.4;
}}

.result-bar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.35);
    padding: 14px 20px;
    border-radius: 14px;
    font-size: 15px;
    font-weight: 700;
    color: #6EE7B7;
}}
</style>
</head>
<body>
<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">PropTech Case Study</div>
</div>

<div class="hero-content">
    <div class="category-pill">The Real Estate Revenue Gap</div>
    <div class="main-title">
        The After-Hours<br>
        <span class="leak">Lead Leakage Problem.</span>
    </div>

    <div class="stat-split">
        <div class="stat-card-big">
            <div class="big-number">68<span>%</span></div>
            <div class="stat-caption">of buyers browse properties after 7:00 PM when agencies are closed. A passive web form loses them to competitors.</div>
        </div>

        <div class="solution-box">
            <div class="solution-title">⚡ How Axiom's Real Estate Engine Fixes It</div>
            
            <div class="feature-row">
                <div class="feature-check">✓</div>
                <div class="feature-text">
                    <div class="feature-h">24/7 AI Property Concierge</div>
                    <div class="feature-p">Engages buyers instantly, answers spec details, and qualifies mortgage readiness after hours.</div>
                </div>
            </div>

            <div class="feature-row">
                <div class="feature-check">✓</div>
                <div class="feature-text">
                    <div class="feature-h">Direct 2-Way Calendar Booking</div>
                    <div class="feature-p">Buyers choose available agent slots synced directly to Google/Outlook with automated travel buffers.</div>
                </div>
            </div>

            <div class="feature-row">
                <div class="feature-check">✓</div>
                <div class="feature-text">
                    <div class="feature-h">WhatsApp Route Reminders</div>
                    <div class="feature-p">Automated location pins and .ics calendar invites reduce viewing no-shows by 82%.</div>
                </div>
            </div>

            <div class="result-bar">
                <span>Verified Client Metric</span>
                <span>+42% Conversion to Viewing Bookings</span>
            </div>
        </div>
    </div>
</div>

<div class="brand-footer">
    <div class="footer-tagline">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#F4A5AE;">PropTech & Enterprise Systems ➔</div>
</div>
</body>
</html>""",

    # 4. Tech Stack & Engineering Rigor (White Background Mixed with Wine Red Logo Color)
    "post_4_tech_stack.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 85% 15%, #FDEEEF 0%, #FFF5F7 35%, #FFFFFF 68%, #FBF0F2 100%);
    color: #0F172A;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #4A0E17; }}
.brand-tagline {{ color: #8B1E2D; }}
.brand-badge {{ background: #FCE8EC; color: #6B1422; border: 1.5px solid #F0CDD3; }}

.hero-content {{
    margin-top: 45px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: relative;
    z-index: 5;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #6B1422;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 7px 16px;
    border-radius: 999px;
    box-shadow: 0 4px 14px rgba(107, 20, 34, 0.25);
}}

.main-title {{
    font-size: 58px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #0F172A;
}}

.main-title span.wine {{
    color: #6B1422;
}}

.lead-text {{
    font-size: 20px;
    font-weight: 400;
    line-height: 1.45;
    color: #475569;
    max-width: 960px;
}}

.stack-container {{
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-top: 24px;
}}

.stack-row {{
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(12px);
    border: 1.5px solid #F0CDD3;
    border-radius: 16px;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 24px rgba(74, 14, 23, 0.04);
}}

.stack-category {{
    display: flex;
    align-items: center;
    gap: 14px;
    width: 240px;
}}

.stack-cat-icon {{
    font-size: 24px;
}}

.stack-cat-name {{
    font-size: 17px;
    font-weight: 800;
    color: #4A0E17;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.stack-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: flex-end;
}}

.stack-pill {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    color: #1E293B;
    font-size: 14px;
    font-weight: 700;
    padding: 8px 16px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}}

.stack-pill.highlight {{
    background: #6B1422;
    color: #FFFFFF;
    border-color: #6B1422;
}}

.principle-banner {{
    margin-top: 10px;
    background: #FCE8EC;
    border-left: 4px solid #6B1422;
    padding: 16px 20px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    color: #4A0E17;
    display: flex;
    align-items: center;
    justify-content: space-between;
}}
</style>
</head>
<body>
<div class="ambient-wine-glow-1"></div>
<div class="ambient-wine-glow-2"></div>

<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">Engineering Standards</div>
</div>

<div class="hero-content">
    <div class="category-pill">Architecture Blueprint</div>
    <div class="main-title">Our Production <span class="wine">Tech Stack</span></div>
    <div class="lead-text">
        Zero hype frameworks. We engineer with battle-tested technologies designed for sub-second response times, zero data loss, and effortless horizontal scaling.
    </div>

    <div class="stack-container">
        <div class="stack-row">
            <div class="stack-category">
                <span class="stack-cat-icon">⚡</span>
                <span class="stack-cat-name">Frontend</span>
            </div>
            <div class="stack-badges">
                <span class="stack-pill highlight">Next.js 14</span>
                <span class="stack-pill">React</span>
                <span class="stack-pill">TypeScript</span>
                <span class="stack-pill">Tailwind CSS</span>
                <span class="stack-pill">Redux Toolkit</span>
            </div>
        </div>

        <div class="stack-row">
            <div class="stack-category">
                <span class="stack-cat-icon">⚙️</span>
                <span class="stack-cat-name">Backend</span>
            </div>
            <div class="stack-badges">
                <span class="stack-pill highlight">Node.js</span>
                <span class="stack-pill">Java Spring Boot</span>
                <span class="stack-pill">GraphQL</span>
                <span class="stack-pill">REST APIs</span>
                <span class="stack-pill">WebSockets</span>
            </div>
        </div>

        <div class="stack-row">
            <div class="stack-category">
                <span class="stack-cat-icon">🤖</span>
                <span class="stack-cat-name">AI & Data</span>
            </div>
            <div class="stack-badges">
                <span class="stack-pill highlight">LangChain / LlamaIndex</span>
                <span class="stack-pill">PostgreSQL / Supabase</span>
                <span class="stack-pill">Pinecone</span>
                <span class="stack-pill">Redis</span>
            </div>
        </div>

        <div class="stack-row">
            <div class="stack-category">
                <span class="stack-cat-icon">☁️</span>
                <span class="stack-cat-name">Cloud & Ops</span>
            </div>
            <div class="stack-badges">
                <span class="stack-pill highlight">AWS</span>
                <span class="stack-pill">Docker</span>
                <span class="stack-pill">GitHub Actions CI/CD</span>
                <span class="stack-pill">Postman / Jest</span>
            </div>
        </div>
    </div>

    <div class="principle-banner">
        <span>💡 Code Philosophy: Clean modular codebases, strict type-safety, and automated CI/CD testing on every commit.</span>
        <span>Enterprise Ready</span>
    </div>
</div>

<div class="brand-footer light">
    <div class="footer-tagline" style="color:#6B1422;">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#6B1422;">Engineering Rigor & Scale ➔</div>
</div>
</body>
</html>""",

    # 5. Healthcare / High-Stakes Systems (Dark Wine Velvet Theme)
    "post_5_healthtech_enterprise.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 85% 15%, #59101B 0%, #35080E 50%, #170205 100%);
    color: #FFFFFF;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #FFFFFF; }}
.brand-tagline {{ color: #F4A5AE; }}
.brand-badge {{ background: rgba(255, 255, 255, 0.12); color: #FFFFFF; border: 1px solid rgba(255, 255, 255, 0.2); }}

.hero-content {{
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    gap: 22px;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #8B1E2D;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 7px 16px;
    border-radius: 999px;
}}

.main-title {{
    font-size: 68px;
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -2px;
}}

.main-title span.accent {{
    color: #F8B4BD;
}}

.lead-text {{
    font-size: 23px;
    font-weight: 400;
    line-height: 1.5;
    color: #E2E8F0;
    max-width: 940px;
}}

.cards-container {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 25px;
}}

.security-card {{
    background: rgba(255, 255, 255, 0.05);
    border: 1.5px solid rgba(255, 255, 255, 0.14);
    border-radius: 20px;
    padding: 34px 26px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}}

.card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.card-icon {{
    font-size: 36px;
}}

.card-tag {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    background: rgba(248, 180, 189, 0.15);
    color: #F8B4BD;
    padding: 4px 10px;
    border-radius: 6px;
}}

.card-title {{
    font-size: 21px;
    font-weight: 700;
    color: #FFFFFF;
}}

.card-desc {{
    font-size: 15px;
    line-height: 1.5;
    color: #CBD5E1;
}}

.quote-box {{
    background: rgba(0, 0, 0, 0.25);
    border-left: 4px solid #F8B4BD;
    padding: 18px 24px;
    border-radius: 8px;
    margin-top: 20px;
    font-size: 16px;
    font-style: italic;
    color: #E2E8F0;
}}
</style>
</head>
<body>
<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">Mission-Critical Systems</div>
</div>

<div class="hero-content">
    <div class="category-pill">High-Stakes Architecture</div>
    <div class="main-title">
        When Software<br>
        <span class="accent">Cannot Fail.</span>
    </div>
    <div class="lead-text">
        Building consumer apps is about engagement. Building clinical, logistics, and fintech software is about absolute fault tolerance, data compliance, and zero downtime.
    </div>

    <div class="cards-container">
        <div class="security-card">
            <div class="card-top">
                <span class="card-icon">🛡️</span>
                <span class="card-tag">Compliance</span>
            </div>
            <div class="card-title">HIPAA & Data Privacy</div>
            <div class="card-desc">End-to-end data encryption at rest and in transit, granular role-based access, and immutable audit logs.</div>
        </div>

        <div class="security-card">
            <div class="card-top">
                <span class="card-icon">⚡</span>
                <span class="card-tag">Real-Time</span>
            </div>
            <div class="card-title">Provider Scheduling</div>
            <div class="card-desc">Sub-second double-booking prevention, automated state licensing checks, and multi-zone calendar sync.</div>
        </div>

        <div class="security-card">
            <div class="card-top">
                <span class="card-icon">🔌</span>
                <span class="card-tag">Integration</span>
            </div>
            <div class="card-title">Pharmacy & Courier APIs</div>
            <div class="card-desc">Resilient idempotent webhooks and message queues ensuring prescriptions and orders never drop.</div>
        </div>
    </div>

    <div class="quote-box">
        "In enterprise software, reliability is not a feature added at the end. It is the architecture you decide on Day 1."
    </div>
</div>

<div class="brand-footer">
    <div class="footer-tagline">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#F4A5AE;">High-Assurance Systems ➔</div>
</div>
</body>
</html>""",

    # 6. Dedicated Squad Model / Partnership (White Background Mixed with Wine Red Logo Color)
    "post_6_collaboration_squad.png": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{SHARED_CSS}
body {{
    background: radial-gradient(circle at 85% 15%, #FDEEEF 0%, #FFF5F7 35%, #FFFFFF 68%, #FBF0F2 100%);
    color: #0F172A;
    padding: 70px 80px;
    display: flex;
    flex-direction: column;
}}

.brand-name {{ color: #4A0E17; }}
.brand-tagline {{ color: #8B1E2D; }}
.brand-badge {{ background: #FCE8EC; color: #6B1422; border: 1.5px solid #F0CDD3; }}

.hero-content {{
    margin-top: 45px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: relative;
    z-index: 5;
}}

.category-pill {{
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #6B1422;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 7px 16px;
    border-radius: 999px;
    box-shadow: 0 4px 14px rgba(107, 20, 34, 0.25);
}}

.main-title {{
    font-size: 58px;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #0F172A;
}}

.main-title span.wine {{
    color: #6B1422;
}}

.lead-text {{
    font-size: 20px;
    font-weight: 400;
    line-height: 1.45;
    color: #475569;
    max-width: 960px;
}}

.timeline-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 25px;
}}

.timeline-card {{
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(12px);
    border: 1.5px solid #F0CDD3;
    border-radius: 18px;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: relative;
    box-shadow: 0 8px 24px rgba(74, 14, 23, 0.05);
}}

.timeline-step {{
    font-size: 12px;
    font-weight: 800;
    color: #8B1E2D;
    text-transform: uppercase;
    letter-spacing: 1px;
}}

.timeline-week {{
    font-size: 18px;
    font-weight: 800;
    color: #0F172A;
}}

.timeline-desc {{
    font-size: 13px;
    color: #475569;
    line-height: 1.45;
}}

.cta-banner {{
    margin-top: 25px;
    background: linear-gradient(135deg, #4A0E17 0%, #681523 100%);
    border-radius: 20px;
    padding: 30px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #FFFFFF;
    box-shadow: 0 10px 30px rgba(74, 14, 23, 0.25);
}}

.cta-left {{
    display: flex;
    flex-direction: column;
    gap: 6px;
}}

.cta-title {{
    font-size: 26px;
    font-weight: 800;
}}

.cta-subtitle {{
    font-size: 15px;
    color: #F8B4BD;
}}

.cta-btn {{
    background: #FFFFFF;
    color: #4A0E17;
    font-size: 16px;
    font-weight: 800;
    padding: 14px 28px;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
}}
</style>
</head>
<body>
<div class="ambient-wine-glow-1"></div>
<div class="ambient-wine-glow-2"></div>

<div class="brand-header">
    <div class="brand-left">
        <img class="brand-logo-img" src="{LOGO_PATH}" alt="Axiom">
        <div class="brand-text-block">
            <div class="brand-name">Axiom Global</div>
            <div class="brand-tagline">AI-Powered Software Solutions</div>
        </div>
    </div>
    <div class="brand-badge">Agile Squad Model</div>
</div>

<div class="hero-content">
    <div class="category-pill">Rapid Delivery Lifecycle</div>
    <div class="main-title">How We Build: <span class="wine">From Idea to Production</span></div>
    <div class="lead-text">
        Skip 6 months of hiring bottlenecks. Deploy dedicated, cross-functional engineering squads focused on rapid velocity, robust architecture, and enterprise scale.
    </div>

    <div class="timeline-grid">
        <div class="timeline-card">
            <div class="timeline-step">Stage 01</div>
            <div class="timeline-week">Week 1</div>
            <div class="timeline-desc">Architecture discovery, SRS documentation, database schema design, and interactive Figma wireframes.</div>
        </div>

        <div class="timeline-card">
            <div class="timeline-step">Stage 02</div>
            <div class="timeline-week">Weeks 2–4</div>
            <div class="timeline-desc">Rapid MVP build: core reactive frontend, authenticated APIs, and backend microservice integration.</div>
        </div>

        <div class="timeline-card">
            <div class="timeline-step">Stage 03</div>
            <div class="timeline-week">Weeks 4–6</div>
            <div class="timeline-desc">AI agent workflows, automated booking engines, rigorous QA testing, and security hardening.</div>
        </div>

        <div class="timeline-card">
            <div class="timeline-step">Stage 04</div>
            <div class="timeline-week">Week 6+</div>
            <div class="timeline-desc">Production deployment to AWS, zero-downtime CI/CD pipelines, and dedicated sprint scaling.</div>
        </div>
    </div>

    <div class="cta-banner">
        <div class="cta-left">
            <div class="cta-title">Ready to Architect Your Next System?</div>
            <div class="cta-subtitle">Partner with our Enterprise Solutions Architects & Engineering Leads.</div>
        </div>
        <div class="cta-btn">Book Architecture Call ➔</div>
    </div>
</div>

<div class="brand-footer light">
    <div class="footer-tagline" style="color:#6B1422;">AI-POWERED SOFTWARE SOLUTIONS</div>
    <div class="footer-action" style="color:#6B1422;">Global Dedicated Practice ➔</div>
</div>
</body>
</html>"""
}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1200, "height": 1200}, device_scale_factor=2)
        
        for filename, html in HTML_TEMPLATES.items():
            out_path = os.path.join(IMG_DIR, filename)
            await page.set_content(html, wait_until="load")
            await page.wait_for_timeout(400)
            img_bytes = await page.screenshot(type="png")
            with open(out_path, "wb") as f:
                f.write(img_bytes)
            print(f"Rendered: {out_path} ({len(img_bytes) / 1024:.1f} KB)")
                
        await browser.close()
    print("All 6 LinkedIn post graphics rendered successfully!")

if __name__ == "__main__":
    asyncio.run(main())
