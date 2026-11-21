import os
import pypdf
from playwright.sync_api import sync_playwright

def generate_pdf():
    base_dir = r"c:\Users\Viranga\Downloads\upwrok new\Axiom_Global_US_Smart_QR_Restaurant_Proposal"
    images_dir = os.path.join(base_dir, "images")
    output_pdf = os.path.join(base_dir, "Axiom_Global_US_Smart_QR_Restaurant_Proposal.pdf")
    html_file = os.path.join(base_dir, "us_proposal_template.html")

    # Local image URLs formatted for file://
    img_cover = "file:///" + os.path.join(images_dir, "us_restaurant_cover.jpg").replace("\\", "/")
    img_journey = "file:///" + os.path.join(images_dir, "customer_journey_table.jpg").replace("\\", "/")
    img_waiter = "file:///" + os.path.join(images_dir, "smart_waiter_call.jpg").replace("\\", "/")
    img_payment = "file:///" + os.path.join(images_dir, "digital_bill_payment.jpg").replace("\\", "/")
    img_kitchen = "file:///" + os.path.join(images_dir, "kitchen_display_kds.jpg").replace("\\", "/")
    img_menu = "file:///" + os.path.join(images_dir, "smart_menu_food.jpg").replace("\\", "/")
    img_upsell = "file:///" + os.path.join(images_dir, "ai_upselling_pairing.jpg").replace("\\", "/")
    img_analytics = "file:///" + os.path.join(images_dir, "restaurant_analytics_laptop.jpg").replace("\\", "/")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>A Smarter Way to Serve Every Table — US Restaurant Proposal</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  *, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  :root {{
    --black: #111111;
    --dark: #222222;
    --charcoal: #374151;
    --muted: #6b7280;
    --light-muted: #9ca3af;
    --border: #e5e7eb;
    --card-bg: #f9fafb;
    --badge-bg: #f3f4f6;
    --badge-text: #4b5563;
    --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }}

  body {{
    font-family: var(--font-main);
    background: #ffffff;
    color: var(--black);
    font-size: 8.5pt;
    line-height: 1.45;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .page {{
    width: 210mm;
    min-height: 297mm;
    max-height: 297mm;
    position: relative;
    page-break-after: always;
    overflow: hidden;
    background: #ffffff;
    padding: 18mm 20mm 18mm 20mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* HEADER & FOOTER */
  .page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border);
    padding-top: 3.5mm;
    margin-top: 4mm;
    font-size: 7.2pt;
    color: var(--light-muted);
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }}

  .page-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }}

  /* COVER PAGE */
  .cover-page {{
    padding: 20mm 20mm 20mm 20mm;
  }}

  .cover-black-box {{
    background: #111111;
    color: #ffffff;
    padding: 30px 34px;
    margin-bottom: 5mm;
  }}

  .cover-kicker {{
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #9ca3af;
    margin-bottom: 14px;
  }}

  .cover-h1 {{
    font-size: 30pt;
    line-height: 1.1;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.02em;
    margin-bottom: 14px;
  }}

  .cover-subtitle {{
    font-size: 10.5pt;
    line-height: 1.45;
    color: #d1d5db;
    max-width: 90%;
    font-weight: 400;
  }}

  .cover-photo {{
    width: 100%;
    height: 110mm;
    object-fit: cover;
    margin-bottom: 5mm;
  }}

  .cover-bottom {{
    border-top: 1px solid var(--border);
    padding-top: 4mm;
  }}

  .cover-proposal-line {{
    font-size: 9pt;
    font-weight: 700;
    color: var(--black);
    margin-bottom: 3px;
  }}

  .cover-prepared-for {{
    font-size: 8pt;
    color: var(--muted);
  }}

  /* HEADINGS */
  .page-title {{
    font-size: 20pt;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -0.02em;
    margin-bottom: 3.5mm;
  }}

  .section-h2 {{
    font-size: 16pt;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -0.02em;
    margin-bottom: 3mm;
  }}

  .lead-p {{
    font-size: 9pt;
    line-height: 1.45;
    color: var(--charcoal);
    margin-bottom: 5mm;
  }}

  /* PAGE 2 TOC */
  .toc-list {{
    list-style: none;
    margin-bottom: 6mm;
  }}

  .toc-item {{
    font-size: 9.5pt;
    font-weight: 700;
    color: var(--black);
    padding: 2.2mm 0;
    border-bottom: 1px solid #f3f4f6;
    text-decoration: underline;
    text-underline-offset: 3px;
    text-decoration-color: #d1d5db;
  }}

  .divider-line {{
    width: 100%;
    height: 1px;
    background: var(--border);
    margin: 4mm 0 5mm 0;
  }}

  .scope-note-title {{
    font-size: 11.5pt;
    font-weight: 800;
    color: var(--black);
    margin-bottom: 2.5mm;
  }}

  .scope-note-p {{
    font-size: 8.5pt;
    line-height: 1.45;
    color: var(--charcoal);
  }}

  /* TWO COLUMN FEATURE SECTION */
  .feature-block {{
    display: flex;
    flex-direction: column;
    margin-bottom: 6mm;
  }}

  .feature-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    align-items: start;
  }}

  .feature-badge {{
    display: inline-block;
    font-size: 6.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    background: var(--badge-bg);
    color: var(--badge-text);
    padding: 2px 7px;
    margin-bottom: 2mm;
  }}

  .feature-h3 {{
    font-size: 13pt;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -0.01em;
    margin-bottom: 2mm;
  }}

  .feature-desc {{
    font-size: 8.2pt;
    color: var(--charcoal);
    line-height: 1.45;
    margin-bottom: 2.5mm;
  }}

  .feature-bullets {{
    margin-left: 4.5mm;
    font-size: 8pt;
    color: var(--charcoal);
    line-height: 1.4;
    margin-bottom: 3mm;
  }}

  .feature-bullets li {{
    margin-bottom: 1.2mm;
  }}

  .business-value {{
    font-size: 8pt;
    color: var(--charcoal);
    line-height: 1.45;
    background: #f9fafb;
    border-left: 2px solid var(--black);
    padding: 2.5mm 3.5mm;
  }}

  .business-value strong {{
    color: var(--black);
  }}

  .feature-photo {{
    width: 100%;
    height: 48mm;
    object-fit: cover;
    border: 1px solid var(--border);
  }}

  /* TABLES */
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin-bottom: 5mm;
  }}

  th {{
    background: #111111;
    color: #ffffff;
    text-align: left;
    padding: 7px 10px;
    font-weight: 700;
    font-size: 7.5pt;
    letter-spacing: 0.05em;
  }}

  td {{
    padding: 7px 10px;
    border-bottom: 1px solid var(--border);
    color: var(--charcoal);
    vertical-align: top;
    line-height: 1.4;
  }}

  tr:nth-child(even) td {{
    background: #f9fafb;
  }}

  /* PAGE 8 PRICING STYLES */
  .investment-hero-box {{
    background: #f9fafb;
    border: 1px solid var(--border);
    padding: 6mm 8mm;
    margin-bottom: 5mm;
  }}

  .inv-tag {{
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 2mm;
  }}

  .inv-price {{
    font-size: 28pt;
    font-weight: 800;
    color: var(--black);
    letter-spacing: -0.02em;
    margin-bottom: 1.5mm;
  }}

  .inv-sub {{
    font-size: 8.5pt;
    color: var(--charcoal);
  }}

  .options-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 5mm;
  }}

  .option-card {{
    background: #ffffff;
    border: 1px solid var(--border);
    padding: 4mm 5mm;
  }}

  .opt-title {{
    font-size: 9pt;
    font-weight: 800;
    color: var(--black);
    margin-bottom: 2mm;
  }}

  .opt-price {{
    font-size: 14pt;
    font-weight: 800;
    color: var(--black);
    margin-bottom: 1.5mm;
  }}

  .opt-sub {{
    font-size: 7.8pt;
    color: var(--muted);
    line-height: 1.35;
  }}

  .section-h4 {{
    font-size: 10.5pt;
    font-weight: 800;
    color: var(--black);
    margin-bottom: 2mm;
  }}

  .clean-bullets {{
    margin-left: 4.5mm;
    font-size: 8pt;
    color: var(--charcoal);
    line-height: 1.45;
    margin-bottom: 4mm;
  }}

  .clean-bullets li {{
    margin-bottom: 1.5mm;
  }}
</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover-page">
  <div class="page-body">
    <div class="cover-black-box">
      <div class="cover-kicker">UNITED STATES • RESTAURANT & HOSPITALITY TECHNOLOGY</div>
      <h1 class="cover-h1">A smarter way<br>to serve every table.</h1>
      <div class="cover-subtitle">
        Secure QR ordering, a smoother guest experience and clearer restaurant operations — in one digital platform.
      </div>
    </div>

    <img src="{img_cover}" alt="Modern Restaurant Table" class="cover-photo">

    <div class="cover-bottom">
      <div class="cover-proposal-line">Commercial proposal &nbsp;|&nbsp; Proposed investment: <strong>US$2,000</strong></div>
      <div class="cover-prepared-for">Prepared for independent restaurants, dining groups and hotel food-and-beverage operations in the United States.</div>
    </div>
  </div>
</div>

<!-- PAGE 2: PROPOSAL OVERVIEW -->
<div class="page">
  <div class="page-body">
    <h1 class="page-title">Proposal overview</h1>
    <p class="lead-p">
      A practical digital ordering experience built around the table: customers scan, verify, browse and order, while restaurant teams receive orders through the kitchen workflow.
      <br><span style="font-size:8pt; color:var(--muted);">Use the links below to jump to each section. The page footer also links back to this contents page.</span>
    </p>

    <div class="toc-list">
      <div class="toc-item">01 Product concept & customer journey</div>
      <div class="toc-item">02 Smart waiter calling</div>
      <div class="toc-item">03 Digital bill & payment</div>
      <div class="toc-item">04 Live order tracking</div>
      <div class="toc-item">05 Smart digital menu & dietary filtering</div>
      <div class="toc-item">06 AI-powered upselling</div>
      <div class="toc-item">07 Restaurant analytics dashboard</div>
      <div class="toc-item">08 Suggested rollout & delivery plan</div>
      <div class="toc-item">09 Trial, investment & payment options</div>
    </div>

    <div class="divider-line"></div>

    <div class="scope-note-title">Important scope note</div>
    <p class="scope-note-p">
      The secure QR/table verification and customer-to-kitchen ordering flow are described as the existing product foundation based on the supplied product description. The six capabilities in this proposal are recommended enhancements. Their exact implementation scope, integrations and acceptance criteria should be confirmed before development begins.
    </p>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>2</span>
  </div>
</div>

<!-- PAGE 3: 01 PRODUCT CONCEPT & CUSTOMER JOURNEY -->
<div class="page">
  <div class="page-body">
    <h2 class="section-h2">01 Product concept & customer journey</h2>
    <p class="lead-p" style="margin-bottom:3.5mm;">
      The platform is designed to reduce friction between guests, service staff and the kitchen. A customer uses a phone browser—without installing a separate app—to access the restaurant’s digital ordering experience.
    </p>

    <img src="{img_journey}" alt="Customer Journey at Table" style="width:100%; height:98mm; object-fit:cover; margin-bottom:4mm; border:1px solid var(--border);">

    <div style="font-size:11pt; font-weight:800; color:var(--black); margin-bottom:2.5mm;">Proposed customer journey</div>
    <ul class="clean-bullets" style="margin-bottom:3.5mm;">
      <li><strong>Scan:</strong> The guest scans the QR code assigned to their table.</li>
      <li><strong>Verify:</strong> The system validates the active table session using the restaurant's configured security flow.</li>
      <li><strong>Browse:</strong> The guest views the menu, item details and available options.</li>
      <li><strong>Order:</strong> The guest submits an order associated with the correct table.</li>
      <li><strong>Prepare:</strong> The kitchen receives the order through the configured kitchen workflow.</li>
    </ul>

    <div style="font-size:8.2pt; color:var(--charcoal); line-height:1.45; background:#f9fafb; padding:2.5mm 3.5mm; border-left:2px solid var(--black);">
      <strong>Core positioning:</strong> secure, app-free table ordering that helps restaurants serve guests more smoothly and coordinate orders more clearly.
    </div>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>3</span>
  </div>
</div>

<!-- PAGE 4: 02 SMART WAITER CALLING & 03 DIGITAL BILL & PAYMENT -->
<div class="page">
  <div class="page-body">
    <!-- Top Half: Feature 01 -->
    <div class="feature-block">
      <h2 class="section-h2" style="margin-bottom:2mm;">02 Smart Waiter Calling</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 01 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">Smart Waiter Calling</div>
          <p class="feature-desc">Give guests a simple way to request help from their table, without repeatedly trying to catch a waiter's attention.</p>
          <ul class="feature-bullets">
            <li>Call a waiter directly from the table menu.</li>
            <li>Request water, extra napkins, cutlery or other configured service items.</li>
            <li>Request the bill or ask for custom table assistance.</li>
            <li>Send the request to a staff dashboard with table number and elapsed time.</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> Staff can prioritize requests, reduce missed signals and provide a more responsive dining experience.
          </div>
        </div>
        <div>
          <img src="{img_waiter}" alt="Smart Waiter Calling" class="feature-photo">
        </div>
      </div>
    </div>

    <div class="divider-line" style="margin:2mm 0 4mm 0;"></div>

    <!-- Bottom Half: Feature 02 -->
    <div class="feature-block" style="margin-bottom:0;">
      <h2 class="section-h2" style="margin-bottom:2mm;">03 Digital Bill & Payment</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 02 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">Digital Bill & Payment</div>
          <p class="feature-desc">Let guests review their bill and, where supported integrations are available, complete payment directly from their phone.</p>
          <ul class="feature-bullets">
            <li>Display the current table bill and itemized charges in real time.</li>
            <li>Support payment through leading US processors (Stripe, Square, Toast, Clover).</li>
            <li>Enable contactless checkout via Apple Pay, Google Pay, and major credit cards.</li>
            <li>Offer split-bill workflows if supported by the POS/payment integration.</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> A smoother checkout reduces payment friction and staff workload. Payment-provider fees and onboarding are separate unless included in the final scope.
          </div>
        </div>
        <div>
          <img src="{img_payment}" alt="Digital Bill Payment" class="feature-photo">
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>4</span>
  </div>
</div>

<!-- PAGE 5: 04 LIVE ORDER TRACKING & 05 SMART DIGITAL MENU -->
<div class="page">
  <div class="page-body">
    <!-- Top Half: Feature 03 -->
    <div class="feature-block">
      <h2 class="section-h2" style="margin-bottom:2mm;">04 Live Order Tracking</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 03 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">Live Order Tracking</div>
          <p class="feature-desc">Show guests clear progress updates after they place an order, using statuses managed by restaurant staff.</p>
          <ul class="feature-bullets">
            <li>Order received and confirmed by kitchen.</li>
            <li>Preparing in the kitchen.</li>
            <li>Ready for pickup / expediter dispatch.</li>
            <li>Served (if staff confirm service in the system).</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> Guests have better visibility into their order status, while staff can reduce repeated status questions during peak rushes.
          </div>
        </div>
        <div>
          <img src="{img_kitchen}" alt="Kitchen Order Tracking KDS" class="feature-photo">
        </div>
      </div>
    </div>

    <div class="divider-line" style="margin:2mm 0 4mm 0;"></div>

    <!-- Bottom Half: Feature 04 (Replaced Arabic with Dietary / Smart Menu) -->
    <div class="feature-block" style="margin-bottom:0;">
      <h2 class="section-h2" style="margin-bottom:2mm;">05 Smart Digital Menu & Dietary Filtering</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 04 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">Dynamic Menu & Dietary Filters</div>
          <p class="feature-desc">Offer a rich, interactive menu experience with instant allergen filters, dietary tags, and flexible modifier options.</p>
          <ul class="feature-bullets">
            <li>Instant dietary filtering: Gluten-Free, Vegan, Vegetarian, Dairy-Free, and Nut Allergies.</li>
            <li>High-definition food photography, dish descriptions, and calorie/ingredient transparency.</li>
            <li>Configurable modifiers: meat temperatures, side substitutions, dressing choices, and add-ons.</li>
            <li>Real-time 86-list / out-of-stock item toggling directly from staff devices to prevent kitchen delays.</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> Clear dietary information builds diner trust, speeds up table decision-making, and eliminates awkward order remakes.
          </div>
        </div>
        <div>
          <img src="{img_menu}" alt="Smart Digital Menu Food" class="feature-photo">
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>5</span>
  </div>
</div>

<!-- PAGE 6: 06 AI-POWERED UPSELLING & 07 RESTAURANT ANALYTICS -->
<div class="page">
  <div class="page-body">
    <!-- Top Half: Feature 05 -->
    <div class="feature-block">
      <h2 class="section-h2" style="margin-bottom:2mm;">06 AI-Powered Upselling</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 05 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">AI-Powered Upselling</div>
          <p class="feature-desc">Use relevant recommendations to help guests discover complementary items and meal upgrades while ordering.</p>
          <ul class="feature-bullets">
            <li>Suggest craft cocktails, wines, or beverages that pair with selected entrees.</li>
            <li>Recommend appetizers, side dishes, or premium dessert pairings.</li>
            <li>Highlight combo upgrades, protein additions, and chef specials.</li>
            <li>Use popular-item or rule-based recommendations as a first release; add AI personalization when sufficient dining data is captured.</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> Relevant suggestions can increase average check size by 15%–25%. Any sales uplift should be measured during a pilot rather than guaranteed.
          </div>
        </div>
        <div>
          <img src="{img_upsell}" alt="AI Food Pairing and Upsell" class="feature-photo">
        </div>
      </div>
    </div>

    <div class="divider-line" style="margin:2mm 0 4mm 0;"></div>

    <!-- Bottom Half: Feature 06 -->
    <div class="feature-block" style="margin-bottom:0;">
      <h2 class="section-h2" style="margin-bottom:2mm;">07 Restaurant Analytics Dashboard</h2>
      <div class="feature-grid">
        <div>
          <span class="feature-badge">FEATURE 06 | RECOMMENDED ENHANCEMENT</span>
          <div class="feature-h3">Restaurant Analytics Dashboard</div>
          <p class="feature-desc">Give owners and general managers a clearer view of sales and ordering activity through practical reports.</p>
          <ul class="feature-bullets">
            <li>Daily, weekly, and monthly sales summaries, subject to payment/POS data availability.</li>
            <li>Best-selling menu items and highest-margin categories.</li>
            <li>Peak dining periods and table occupancy trends.</li>
            <li>Average order value (AOV), table activity, and item cancellation logs.</li>
          </ul>
          <div class="business-value">
            <strong>Business value:</strong> Managers can identify popular products, peak table rush periods, and operational bottlenecks to support better purchasing and staffing decisions.
          </div>
        </div>
        <div>
          <img src="{img_analytics}" alt="Restaurant Analytics Dashboard" class="feature-photo">
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>6</span>
  </div>
</div>

<!-- PAGE 7: 08 SUGGESTED ROLLOUT & DELIVERY PLAN -->
<div class="page">
  <div class="page-body">
    <h2 class="section-h2" style="margin-bottom:1.5mm;">08 Suggested rollout & delivery plan</h2>
    <p class="lead-p" style="margin-bottom:4mm;">A phased rollout reduces risk and allows the restaurant to validate the experience before expanding the system.</p>

    <table>
      <thead>
        <tr>
          <th style="width:22%;">Stage</th>
          <th style="width:48%;">Focus</th>
          <th style="width:30%;">Outcome</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Discovery & confirmation</strong></td>
          <td>Confirm workflows, menu structure, staff roles, devices, payment/POS requirements and US compliance.</td>
          <td>Approved scope and acceptance criteria.</td>
        </tr>
        <tr>
          <td><strong>Core experience</strong></td>
          <td>Configure QR/table journey, menu experience, waiter requests and kitchen workflow.</td>
          <td>A working end-to-end ordering flow.</td>
        </tr>
        <tr>
          <td><strong>Enhancements</strong></td>
          <td>Implement agreed digital bill/payment, order tracking, dietary filters, upselling and analytics features.</td>
          <td>Enhanced guest and manager experience.</td>
        </tr>
        <tr>
          <td><strong>Testing & handover</strong></td>
          <td>User testing, staff walkthrough, issue fixes, pilot deployment and manager handover.</td>
          <td>Ready for the agreed launch environment.</td>
        </tr>
      </tbody>
    </table>

    <div style="font-size:11pt; font-weight:800; color:var(--black); margin-bottom:2.5mm; margin-top:2mm;">Items to confirm before kickoff</div>
    <ul class="clean-bullets" style="margin-bottom:4mm;">
      <li>Restaurant count, branches, tables, seating zones, and user roles.</li>
      <li>Whether a POS system is already in use (Toast, Square, Clover, Aloha) and whether its API is available.</li>
      <li>Selected US payment provider (Stripe, Square, etc.) and merchant onboarding requirements.</li>
      <li>Menu item details, dietary tags, modifiers, dish photos, ingredients, and allergen data.</li>
      <li>Hosting, domain, support, maintenance, and any third-party subscription costs.</li>
    </ul>

    <p style="font-size:7.8pt; color:var(--muted); line-height:1.45;">
      The final timeline depends on the confirmed scope, integration access, third-party approvals and timely provision of restaurant content.
    </p>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>7</span>
  </div>
</div>

<!-- PAGE 8: 09 TRIAL, INVESTMENT & PAYMENT OPTIONS -->
<div class="page">
  <div class="page-body">
    <h2 class="section-h2" style="margin-bottom:1.5mm;">09 Trial, investment & payment options</h2>
    <p class="lead-p" style="margin-bottom:4mm;">A straightforward commercial offer for the proposed product scope.</p>

    <!-- Hero Investment Box -->
    <div class="investment-hero-box">
      <div class="inv-tag">TOTAL PROJECT INVESTMENT</div>
      <div class="inv-price">US$2,000</div>
      <div class="inv-sub">Two-week free trial period, followed by the client’s choice of payment option.</div>
    </div>

    <!-- Options Grid -->
    <div class="options-grid">
      <div class="option-card">
        <div class="opt-title">Option A — Full payment</div>
        <div class="opt-price">US$2,000</div>
        <div class="opt-sub">One payment after the two-week trial period.</div>
      </div>
      <div class="option-card">
        <div class="opt-title">Option B — 3 monthly instalments</div>
        <div class="opt-price">3 × US$667</div>
        <div class="opt-sub">Three monthly payments after the two-week trial period ($667 / month).</div>
      </div>
    </div>

    <!-- How the trial works -->
    <div class="section-h4">How the two-week trial works</div>
    <ul class="clean-bullets" style="margin-bottom:3.5mm;">
      <li>The client receives access to the agreed trial version for 14 days at no charge.</li>
      <li>At the end of the trial, the client chooses full payment or the three-month instalment plan.</li>
      <li>The US$2,000 project price is the same under both payment options (0% interest).</li>
      <li>Any additional features or third-party costs outside the agreed scope require separate approval.</li>
    </ul>

    <!-- Commercial Assumptions -->
    <div class="section-h4">Commercial assumptions to confirm in the agreement</div>
    <p style="font-size:7.8pt; color:var(--charcoal); line-height:1.4; margin-bottom:3.5mm;">
      The proposal assumes the two-week trial is provided before payment and that the selected payment plan begins after the trial. Confirm whether the trial includes all proposed enhancements or a defined pilot scope. Hosting, payment processing fees, POS vendor charges, SMS fees, taxes and ongoing support are not included unless expressly stated in the signed scope.
    </p>

    <!-- Next Step -->
    <div class="section-h4">Next step</div>
    <p style="font-size:7.8pt; color:var(--charcoal); line-height:1.4; margin-bottom:4mm;">
      Confirm the required features, restaurant workflows and integrations. Once the scope is approved, the project can move to kickoff and the two-week trial arrangement can be documented.
    </p>

    <div style="border-top:1px solid var(--border); padding-top:3mm;">
      <div style="font-weight:800; font-size:8.5pt; color:var(--black);">Smart QR Restaurant Ordering System</div>
      <div style="font-size:7.8pt; color:var(--muted);">A better-connected dining experience for restaurants and hospitality teams in the United States.</div>
    </div>
  </div>

  <div class="page-footer">
    <span>SMART QR RESTAURANT ORDERING | UNITED STATES</span>
    <span>8</span>
  </div>
</div>

</body>
</html>
"""

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML written to {html_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///" + html_file.replace("\\", "/"), wait_until="networkidle")
        page.pdf(
            path=output_pdf,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"}
        )
        browser.close()

    print(f"PDF successfully generated at: {output_pdf}")

    # Verify Page Count with pypdf
    reader = pypdf.PdfReader(output_pdf)
    total_pages = len(reader.pages)
    print(f"Total Page Count: {total_pages}")
    if total_pages == 8:
        print("PAGE COUNT VERIFICATION PASSED: Exactly 8 pages.")
    else:
        print(f"WARNING: Expected 8 pages, but got {total_pages}. Check layout heights.")

if __name__ == "__main__":
    generate_pdf()

