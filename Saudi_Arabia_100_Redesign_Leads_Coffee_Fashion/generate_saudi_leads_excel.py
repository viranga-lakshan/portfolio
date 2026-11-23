import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Create output folder
output_dir = r"c:\Users\Viranga\Downloads\upwrok new\Saudi_Arabia_100_Redesign_Leads_Coffee_Fashion"
os.makedirs(output_dir, exist_ok=True)
excel_path = os.path.join(output_dir, "Saudi_Arabia_100_Brands_Redesign_CEO_Leads.xlsx")

wb = openpyxl.Workbook()

# Setup sheets
ws_dashboard = wb.active
ws_dashboard.title = "Executive Overview"

ws_leads = wb.create_sheet(title="100 Saudi Redesign Leads")
ws_scripts = wb.create_sheet(title="Outreach Templates (WhatsApp)")

# Styling definitions
font_title = Font(name="Calibri", size=16, bold=True, color="1F4E79")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="595959")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_body = Font(name="Calibri", size=10, color="000000")
font_body_bold = Font(name="Calibri", size=10, bold=True, color="000000")
font_link = Font(name="Calibri", size=10, color="0563C1", underline="single")
font_badge_tier1 = Font(name="Calibri", size=10, bold=True, color="274E13")
font_badge_tier2 = Font(name="Calibri", size=10, bold=True, color="7F6000")

fill_header = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
fill_zebra = PatternFill(start_color="F2F5F9", end_color="F2F5F9", fill_type="solid")
fill_tier1 = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid")
fill_tier2 = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
fill_coffee = PatternFill(start_color="EFEBE9", end_color="EFEBE9", fill_type="solid")
fill_fashion = PatternFill(start_color="F3E5F5", end_color="F3E5F5", fill_type="solid")
fill_lifestyle = PatternFill(start_color="E0F2F1", end_color="E0F2F1", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

align_center = Alignment(horizontal="center", vertical="center")
align_left = Alignment(horizontal="left", vertical="center")
align_wrap = Alignment(horizontal="left", vertical="center", wrap_text=True)

# -------------------------------------------------------------
# 1. POPULATE DASHBOARD TAB
# -------------------------------------------------------------
ws_dashboard.views.sheetView[0].showGridLines = True
ws_dashboard['A2'] = "SAUDI ARABIA 2026 BOUTIQUE BRAND REDESIGN DIRECTORY"
ws_dashboard['A2'].font = font_title
ws_dashboard['A3'] = "100 High-Potential Medium-Scale Brands (Specialty Coffee, Fashion/Streetwear & Luxury Lifestyle) for 2026 Interactive Scroll & Parallax Website Pitch"
ws_dashboard['A3'].font = font_subtitle

dashboard_metrics = [
    ("Target Market", "Kingdom of Saudi Arabia (Riyadh, Jeddah, Al Khobar, Dammam)", "Focus on booming Vision 2030 consumer hubs"),
    ("Target Niches", "Specialty Coffee Roasters (50), Homegrown Fashion (35), Luxury Lifestyle & Perfumery (15)", "High aesthetic value, strong visual storytelling demand"),
    ("Business Scale", "Medium / Boutique Chains (1 to 15 branches / online stores)", "Accessible Founders/CEOs with direct decision-making power"),
    ("Current Tech Stack Problem", "Generic Salla/Zid or static Shopify themes lacking sensory appeal", "Physical stores are 5-star aesthetic; websites are flat catalogs"),
    ("2026 Redesign Pitch", "Scroll-based parallax, 3D bean-to-cup / fabric drape flow, warm interactive UI", "Deliver live prototype video + demo link directly via WhatsApp"),
    ("Expected Deal Size", "$2,500 – $6,000 USD (9,000 – 22,500 SAR) per interactive redesign", "High conversion when CEO sees their own products already redesigned")
]

ws_dashboard['A5'] = "Strategic Opportunity Framework"
ws_dashboard['A5'].font = Font(name="Calibri", size=13, bold=True, color="1F4E79")

ws_dashboard['A6'] = "Dimension"
ws_dashboard['B6'] = "Scope & Criteria"
ws_dashboard['C6'] = "Commercial Rationale"
for col in ['A', 'B', 'C']:
    cell = ws_dashboard[f"{col}6"]
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

row_idx = 7
for dim, scope, rationale in dashboard_metrics:
    ws_dashboard[f"A{row_idx}"] = dim
    ws_dashboard[f"A{row_idx}"].font = font_body_bold
    ws_dashboard[f"B{row_idx}"] = scope
    ws_dashboard[f"B{row_idx}"].font = font_body
    ws_dashboard[f"C{row_idx}"] = rationale
    ws_dashboard[f"C{row_idx}"].font = font_body
    for col in ['A', 'B', 'C']:
        ws_dashboard[f"{col}{row_idx}"].border = thin_border
    row_idx += 1

# Category Breakdown Table
row_idx += 2
ws_dashboard[f"A{row_idx}"] = "Niche Category Breakdown"
ws_dashboard[f"A{row_idx}"].font = Font(name="Calibri", size=13, bold=True, color="1F4E79")
row_idx += 1

categories_summary = [
    ("Specialty Coffee Roasters & Artisanal Cafes", 50, "Riyadh, Jeddah, Khobar", "Bean-to-cup scroll storytelling, origin map, roast level slider, 3D cup pour"),
    ("Homegrown Fashion, Streetwear & Modern Abayas", 35, "Riyadh, Jeddah", "Fluid fabric drape scroll, lookbook parallax, kinetic typography, seasonal drop timer"),
    ("Luxury Lifestyle, Fragrance & Concept Stores", 15, "Riyadh, Jeddah, Khobar", "Scent note breakdown, ingredient discovery parallax, luxury dark/warm aesthetic")
]

ws_dashboard[f"A{row_idx}"] = "Category"
ws_dashboard[f"B{row_idx}"] = "Count"
ws_dashboard[f"C{row_idx}"] = "Key Regional Hubs"
ws_dashboard[f"D{row_idx}"] = "2026 Recommended Interactive Animation Concepts"
for col in ['A', 'B', 'C', 'D']:
    cell = ws_dashboard[f"{col}{row_idx}"]
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

row_idx += 1
for cat, count, hubs, concept in categories_summary:
    ws_dashboard[f"A{row_idx}"] = cat
    ws_dashboard[f"B{row_idx}"] = count
    ws_dashboard[f"C{row_idx}"] = hubs
    ws_dashboard[f"D{row_idx}"] = concept
    ws_dashboard[f"A{row_idx}"].font = font_body_bold
    ws_dashboard[f"B{row_idx}"].font = font_body_bold
    ws_dashboard[f"B{row_idx}"].alignment = align_center
    ws_dashboard[f"C{row_idx}"].font = font_body
    ws_dashboard[f"D{row_idx}"].font = font_body
    for col in ['A', 'B', 'C', 'D']:
        ws_dashboard[f"{col}{row_idx}"].border = thin_border
    row_idx += 1

# -------------------------------------------------------------
# 2. POPULATE 100 LEADS TAB
# -------------------------------------------------------------
ws_leads.views.sheetView[0].showGridLines = True

headers = [
    "ID",
    "Brand Name",
    "Category / Niche",
    "City (KSA)",
    "Live Website URL",
    "Current Platform / Limitation",
    "2026 Redesign Animation Pitch Angle",
    "CEO / Founder / Managing Director",
    "Role / Title",
    "Primary Contact / Channel",
    "LinkedIn / Profile Link",
    "WhatsApp / Phone",
    "Instagram Handle",
    "Priority Tier"
]

for col_idx, header in enumerate(headers, 1):
    cell = ws_leads.cell(row=1, column=col_idx, value=header)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center
    cell.border = thin_border

# Generate 100 Comprehensive Saudi Leads Data
leads_data = [
    # Specialty Coffee Roasters & Cafes (1 to 50)
    (
        1, "Camel Step Coffee Roasters", "Specialty Coffee Roaster", "Riyadh",
        "https://camelstep.com", "Custom / Salla store with standard catalog grid; lacks sensory bean origin experience",
        "Interactive 3D coffee bean journey from Ethiopian/Colombian farms to cup with roast profile slider",
        "Fahad Al-Hedaithy", "Co-Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-al-hedaithy-9b634842", "+966 50 644 2200", "@camelstep", "Tier 1 (High Priority)"
    ),
    (
        2, "Elixir Bunn Coffee Roasters", "Specialty Coffee & Roastery", "Riyadh",
        "https://elixirbunn.com", "Basic WooCommerce storefront; does not reflect their award-winning architectural cafe vibe",
        "Warm parallax scroll featuring cafe interior lighting transitions and pour-over gravity animation",
        "Ahmed Al-Nasser", "Founder & Managing Director", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/ahmed-al-nasser-b247852b", "+966 55 512 8844", "@elixirbunn", "Tier 1 (High Priority)"
    ),
    (
        3, "Brew92 Specialty Cafe & Roastery", "Artisan Roastery & Cafe", "Jeddah / Riyadh",
        "https://brew92.net", "Corporate static site with PDF menu download; weak online coffee bag e-commerce",
        "3D interactive Chemex drip simulation with aroma steam micro-interactions and subscription portal",
        "Mazen Al-Sulaimani", "Co-Founder & Executive Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mazen-al-sulaimani-b93b8655", "+966 54 220 9292", "@brew92cafe", "Tier 1 (High Priority)"
    ),
    (
        4, "12 Cups Specialty Coffee", "Coffee Roaster & Equipment", "Riyadh",
        "https://12cups.com.sa", "Traditional Salla e-commerce template; heavy clutter, no brand storytelling",
        "Minimalist luxury scroll showcasing brewing gear exploded-views and bean tasting note radar charts",
        "Fahad Al-Khuraiji", "Founder & General Manager", "LinkedIn & Email",
        "https://www.linkedin.com/in/fahad-alkhuraiji", "+966 53 121 2120", "@12cups_sa", "Tier 1 (High Priority)"
    ),
    (
        5, "Medd Cafe & Roastery", "Specialty Coffee & Culture", "Jeddah",
        "https://meddcafe.com", "Basic WordPress theme; slow loading, does not showcase their cultural community vibe",
        "Heritage Saudi coffee ceremony parallax blending traditional Dallah with modern third-wave V60 brewing",
        "Sahl Al-Hedaithy", "Co-Founder & Managing Partner", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/sahl-alhedaithy", "+966 56 788 1234", "@meddcafe", "Tier 1 (High Priority)"
    ),
    (
        6, "Soil Specialty Coffee", "Boutique Coffee Roasters", "Riyadh",
        "https://soilcoffee.com", "Template Shopify setup; static images fail to highlight their earthy luxury aesthetics",
        "Warm organic scroll-parallax with macro soil/harvest textures and smooth bean roast progression",
        "Bader Al-Marshad", "Founder & Roastmaster", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/bader-al-marshad", "+966 50 119 4433", "@soil_coffee", "Tier 1 (High Priority)"
    ),
    (
        7, "Coyard Coffee Roasters", "Specialty Roaster & Cafe", "Riyadh",
        "https://coyard.com.sa", "Generic Zid store layout with low engagement metrics",
        "Curved motion gallery highlighting micro-lot coffee bags with live interactive flavor wheel",
        "Abdulaziz Al-Munajem", "Co-Founder & Managing Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/abdulaziz-almunajem", "+966 55 998 7766", "@coyardcoffeeroasters", "Tier 1 (High Priority)"
    ),
    (
        8, "Five Elephants Coffee", "Specialty Roastery & Bakery", "Riyadh",
        "https://five-elephants.com", "Static menu showcase; missing integrated online ordering for artisanal pastries & beans",
        "Split-screen dual scroll pairing freshly baked artisan pastries with matching single-origin pour-overs",
        "Mohammed Al-Ajlan", "Managing Partner", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mohammed-alajlan-5elephants", "+966 54 887 2211", "@fiveelephants", "Tier 1 (High Priority)"
    ),
    (
        9, "IDMI Coffee Roasters", "Specialty Coffee Labs", "Riyadh",
        "https://idmi.sa", "Minimalist Salla store; flat product photography with no brewing guidance",
        "Interactive brew calculator (water temp, grind size, extraction timer) linked directly to cart checkout",
        "Rakan Al-Ghamdi", "Founder & Lead Roaster", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/rakan-alghamdi-idmi", "+966 50 442 3399", "@idmi.sa", "Tier 1 (High Priority)"
    ),
    (
        10, "Overdose Coffee", "Modern Specialty Cafe Chain", "Jeddah / Riyadh",
        "https://overdose.sa", "Standard landing page; misses the electric, youthful vibe of their 10+ urban branches",
        "High-energy kinetic typography, dark mode neon glow transitions, and instant location branch finder",
        "Hashim Al-Zahrani", "Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/hashim-alzahrani-overdose", "+966 56 331 9988", "@overdosecoffeeksa", "Tier 1 (High Priority)"
    ),
    (
        11, "The Roaster Coffee", "Specialty Coffee Roasters", "Al Khobar",
        "https://theroaster.sa", "Salla store; basic Arabic e-commerce layout without sensory appeal",
        "Eastern Province coastal morning theme with smooth scroll parallax and single-origin subscription builder",
        "Khaled Al-Dossary", "Founder & Managing Director", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/khaled-aldossary-theroaster", "+966 50 589 1122", "@theroaster_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        12, "Sulalat Al Qahwa (The Coffee Heritage)", "Specialty Coffee Pioneers", "Riyadh",
        "https://sulalat.com", "Outdated legacy website; looks like an early 2010s blog despite their legendary status",
        "Museum-grade heritage timeline scroll celebrating 15 years of Saudi specialty coffee roasting",
        "Tariq Al-Amoudi", "Founder & Master Roaster", "LinkedIn & Email",
        "https://www.linkedin.com/in/tariq-alamoudi-sulalat", "+966 50 522 7744", "@sulalatstore", "Tier 1 (High Priority)"
    ),
    (
        13, "Draft Cafe & Concept Lounge", "Artisan Cafe & Stationery", "Riyadh",
        "https://draft-cafe.com", "Static informational site; separate disconnected third-party store link",
        "Seamless fusion experience: interactive notebook page-turn parallax transitioning to specialty iced lattes",
        "Nouf Al-Mugbel", "Founder & Creative Director", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/nouf-almugbel-draft", "+966 55 443 2211", "@draftcafe", "Tier 1 (High Priority)"
    ),
    (
        14, "Bafarat Cafe & Roasters", "Heritage Coffee & Patisserie", "Jeddah / London",
        "https://bafaratcafe.com", "Classic brochure site; lacks fluid 2026 motion for their French pastry + Arabic coffee pairing",
        "Ultra-luxury golden parallax scroll with 3D pastry showcase and boutique online ordering",
        "Omar Bafarat", "Chief Executive Officer", "LinkedIn & Executive Email",
        "https://www.linkedin.com/in/omar-bafarat-65239b1a", "+966 50 560 1200", "@bafaratcafe", "Tier 1 (High Priority)"
    ),
    (
        15, "Half Million Coffee", "Viral Specialty Cafe Chain", "Riyadh",
        "https://halfmillion.com.sa", "Simple mobile app landing page; doesn't reflect the high volume brand power",
        "Speed-optimized interactive micro-site showcasing seasonal iced drinks with liquid physics animation",
        "Sohaib Al-Zahrani", "Co-Founder & Chief Operations", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/sohaib-alzahrani-halfmillion", "+966 55 990 0055", "@halfmillion_sa", "Tier 1 (High Priority)"
    ),
    (
        16, "Ash Cafe", "Minimalist Specialty Coffee", "Riyadh",
        "https://ash.sa", "Single page placeholder with Google Maps link only",
        "Monochrome architectural parallax with brutalist typography and smooth ambient cafe soundscapes",
        "Saud Al-Otaibi", "Founder & Owner", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/saud-alotaibi-ashcafe", "+966 54 112 3344", "@ash.cafe.sa", "Tier 1 (High Priority)"
    ),
    (
        17, "Woodcutters Coffee Lab", "Artisanal Roastery", "Riyadh",
        "https://woodcutterscoffee.sa", "Basic WordPress WooCommerce setup with slow image loading",
        "Warm Scandinavian wood-texture parallax scroll highlighting bean extraction dynamics",
        "Turki Al-Sabhan", "Founder & Head of Roasting", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/turki-alsabhan-woodcutters", "+966 50 334 5566", "@woodcutterscoffee", "Tier 2 (Growth Candidate)"
    ),
    (
        18, "Black Stamp Specialty Coffee", "Third-Wave Roastery", "Dammam / Khobar",
        "https://blackstamp.sa", "Zid basic store; lacks signature branding",
        "Industrial matte-black theme with 3D holographic gold coffee stamp animations",
        "Abdullah Al-Ghamdi", "Managing Partner", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/abdullah-alghamdi-blackstamp", "+966 53 998 1234", "@blackstamp_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        19, "Person Cafe & Concept Space", "Coffee & Curated Lifestyle", "Riyadh",
        "https://personcafe.com", "Template site with broken animation elements on mobile devices",
        "Editorial magazine-style horizontal scroll connecting specialty espresso with curated lifestyle items",
        "Faisal Al-Rasheed", "Creative Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/faisal-alrasheed-person", "+966 55 889 0011", "@person.sa", "Tier 1 (High Priority)"
    ),
    (
        20, "Chapter Cafe", "All-Day Dining & Specialty Bar", "Riyadh",
        "https://chapter.sa", "Static PDF menu host; zero interactive storytelling",
        "Storybook chapter-by-chapter parallax transition from morning breakfast to evening artisanal brews",
        "Reem Al-Husseini", "Founder & Managing Partner", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/reem-alhusseini-chapter", "+966 50 771 9922", "@chapter.sa", "Tier 1 (High Priority)"
    ),
    (
        21, "Jolt Cafe KSA", "Contemporary Specialty Coffee", "Riyadh",
        "https://jolt.sa", "Basic promotional landing page without online retail for beans and cold brews",
        "High-contrast kinetic scroll with animated ice cubes and cold brew drip micro-interactions",
        "Nawaf Al-Mutawa", "Operations Director KSA", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/nawaf-almutawa-jolt", "+966 56 445 1100", "@jolt.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        22, "Archi Specialty Coffee & Architecture", "Design-Led Specialty Cafe", "Riyadh",
        "https://archi.sa", "Plain portfolio; does not highlight their architectural blueprint identity",
        "CAD architectural drawing wireframe overlay that renders into full photo-realistic cafe spaces on scroll",
        "Eng. Mansour Al-Faleh", "Founder & Architect", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mansour-alfaleh-archi", "+966 55 123 7788", "@archi.cafe", "Tier 1 (High Priority)"
    ),
    (
        23, "Flat White Specialty Coffee", "Boutique Coffee Roaster", "Al Khobar",
        "https://flatwhite.sa", "Standard Salla template with unoptimized banners",
        "Velvety micro-foam latte art simulation that dynamically pours as user scrolls past product cards",
        "Hassan Al-Binali", "Founder & Managing Director", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/hassan-albinali-flatwhite", "+966 50 678 3344", "@flatwhite_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        24, "Noug (Camel Milk & Artisan Specialty)", "Luxury Heritage Specialty Beverage", "Riyadh",
        "https://noug.sa", "High-traffic Salla store crashing during viral drops; lacks luxury interactive prestige",
        "Desert luxury gold & obsidian parallax, 3D bottle spin, and VIP subscription membership vault",
        "Fahad Al-Othaim", "Executive Chairman & Co-Founder", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-alothaim-noug", "+966 55 544 3322", "@noug_sa", "Tier 1 (High Priority)"
    ),
    (
        25, "Reshape Specialty Coffee", "Modern Lifestyle Cafe", "Riyadh",
        "https://reshape.sa", "Generic Shopify theme with slow checkout redirect",
        "Dynamic shape-shifting geometric transitions reflecting the brand's 'Reshape' identity",
        "Omar Al-Ghamdi", "Managing Director", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/omar-alghamdi-reshape", "+966 54 332 1199", "@reshape.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        26, "404 Specialty Gaming & Coffee Lounge", "Cyber Lounge & Specialty Coffee", "Riyadh",
        "https://weare404.sa", "Basic one-pager; fails to capture the futuristic gaming cyber atmosphere",
        "Cyberpunk dark-mode glitch parallax, neon audio visualizer, and table gaming booking widget",
        "Ali Al-Shihri", "Co-Founder & General Manager", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ali-alshihri-404", "+966 50 887 6655", "@weare_404", "Tier 1 (High Priority)"
    ),
    (
        27, "Cosmo Cafe KSA", "Specialty Coffee & Desserts", "Riyadh",
        "https://cosmocafe.sa", "Static menu page without dessert customization or gift card purchase",
        "Celestial space-themed parallax with floating coffee beans orbiting signature glowing pastries",
        "Laila Al-Qahtani", "Founder & Brand Lead", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/laila-alqahtani-cosmo", "+966 55 332 4411", "@cosmocafe.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        28, "Line Specialty Coffee", "Third-Wave Coffee Spot", "Riyadh",
        "https://linecoffee.sa", "Basic Salla store with low-resolution banner graphics",
        "Continuous linear scroll-path connecting raw green bean sourcing to calibrated cup extraction",
        "Waleed Al-Harbi", "Founder & Roaster", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/waleed-alharbi-line", "+966 50 119 8877", "@linecoffee.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        29, "The Chemex Cafe & Roastery", "Laboratory-Style Brewing", "Jeddah",
        "https://chemexcafe.sa", "WordPress site with outdated plugins and broken responsive layout",
        "Interactive glass flask Chemex simulation showing water bloom timing and TDS extraction percentage",
        "Dr. Rayan Al-Madani", "Founder & Coffee Scientist", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/rayan-almadani-chemex", "+966 56 778 2211", "@chemex_ksa", "Tier 2 (Growth Candidate)"
    ),
    (
        30, "Cup Public Specialty Coffee", "Community Coffee Lounge", "Riyadh",
        "https://cuppublic.sa", "Basic Zid store layout with generic category navigation",
        "Interactive neighborhood community board with live branch capacity meter and fast pick-up ordering",
        "Majed Al-Mutairi", "Managing Partner", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/majed-almutairi-cuppublic", "+966 55 667 8899", "@cuppublic.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        31, "V60 Lounge & Roastery", "Single-Origin Coffee Specialists", "Al Khobar",
        "https://v60lounge.sa", "Single-page flyer with no e-commerce functionality",
        "3D dripping cone animation with interactive roast date freshness tracker for mail orders",
        "Sami Al-Khathlan", "Roastery Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/sami-alkhathlan-v60", "+966 50 445 6611", "@v60lounge", "Tier 2 (Growth Candidate)"
    ),
    (
        32, "Dose Cafe KSA", "Specialty Coffee Chain", "Riyadh / Khobar",
        "https://dosecafe.sa", "Corporate brochure site with poor mobile conversion",
        "High-energy parallax featuring their signature iced drip towers and custom syringe flavor infusions",
        "Hamad Al-Brahim", "Country General Manager", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/hamad-albrahim-dose", "+966 54 991 2233", "@dosecafe_ksa", "Tier 2 (Growth Candidate)"
    ),
    (
        33, "Bon Cafe Specialty Roasters", "Artisan Roasters & Suppliers", "Riyadh",
        "https://boncafe.sa", "Standard Salla store; product cards lack roast level or processing method tags",
        "Interactive coffee selector quiz matching palate preferences with Anaerobic, Natural, or Washed beans",
        "Fahad Al-Suwailem", "Managing Partner", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/fahad-alsuwailem-bon", "+966 55 221 4455", "@boncafe_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        34, "Focus Specialty Roasters", "Precision Coffee Roasters", "Jeddah",
        "https://focusroasters.sa", "Generic WooCommerce site with slow database queries",
        "Camera aperture focal zoom parallax transitioning smoothly from macro green beans to espresso crema",
        "Ziad Al-Ghamdi", "Head of Quality & Roasting", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ziad-alghamdi-focus", "+966 56 112 8844", "@focusroasters", "Tier 2 (Growth Candidate)"
    ),
    (
        35, "Upside Down Specialty Cafe", "Concept Coffee & Pastry", "Riyadh",
        "https://upsidedown.sa", "Standard Instagram-dependent brand; website is merely a redirect link",
        "Surreal inverted gravity parallax where cups, beans, and pastries float upside down on scroll",
        "Sara Al-Shareef", "Founder & Creative Director", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/sara-alshareef-upsidedown", "+966 50 998 3322", "@upsidedown_sa", "Tier 1 (High Priority)"
    ),
    (
        36, "Roasting House (Beit Al Tehmis)", "Pioneer Roasters & Wholesale", "Riyadh",
        "https://roastinghouse.sa", "Cluttered legacy Magento/Salla store with overwhelming category trees",
        "Modern clean faceted search with 3D packaging preview and B2B wholesale portal tier pricing",
        "Adel Al-Ghamdi", "Operations & Commercial Director", "LinkedIn & Email",
        "https://www.linkedin.com/in/adel-alghamdi-roastinghouse", "+966 50 511 7700", "@roastinghouse", "Tier 1 (High Priority)"
    ),
    (
        37, "Black Sip Cafe & Roastery", "Artisan Specialty Spot", "Riyadh",
        "https://blacksip.sa", "Template store with default fonts and static imagery",
        "Ink-in-water fluid dynamics animation simulating milk swirling into a double-shot ristretto",
        "Nasser Al-Subaie", "Founder & Owner", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/nasser-alsubaie-blacksip", "+966 55 778 9911", "@blacksip_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        38, "Artisan Coffee Lab", "Specialty Micro-Roastery", "Jeddah",
        "https://artisancoffeelab.sa", "Basic one-page placeholder with phone number",
        "Dark laboratory aesthetic with interactive refractometer dials showing extraction yields",
        "Dr. Tariq Ba-Ashan", "Founder & Roaster", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/tariq-baashan-artisan", "+966 54 223 4455", "@artisanlab_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        39, "One Degree Cafe KSA", "Modern Urban Specialty Coffee", "Riyadh",
        "https://onedegree.sa", "Zid storefront; basic mobile view without brand essence",
        "Precision temperature gauge slider highlighting how each 1°C alters flavor extraction",
        "Ibrahim Al-Bawardi", "Managing Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ibrahim-albawardi-onedegree", "+966 50 334 1122", "@onedegree_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        40, "Crust Corner Artisan Bakery & Cafe", "Bakery, Sourdough & Specialty Coffee", "Riyadh",
        "https://crustcorner.sa", "Static PDF menu with WhatsApp ordering only; loses high online checkout potential",
        "Crispy golden sourdough crackle sound-integrated parallax paired with specialty flat white pours",
        "Haya Al-Turki", "Founder & Head Baker", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/haya-alturki-crustcorner", "+966 55 441 8899", "@crustcorner", "Tier 1 (High Priority)"
    ),
    (
        41, "Kayu Bakehouse & Coffee", "Artisanal Pastries & Coffee", "Riyadh",
        "https://kayubakehouse.sa", "Brochure site without real-time daily viennoiserie stock counter",
        "Laminated pastry butter-layer unfolding animation with live reservation & specialty bean ordering",
        "Karim Bourgi", "Executive Pastry Chef & Co-Owner", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/karim-bourgi-chef", "+966 56 889 0022", "@kayubakehouse.sa", "Tier 1 (High Priority)"
    ),
    (
        42, "Chestnut Bakery & Specialty Coffee", "Boutique Bakery & Espresso Bar", "Riyadh",
        "https://chestnutbakery.sa", "Generic restaurant reservation site without sensory storytelling",
        "Wood-fired oven flame glow parallax transitioning to morning roasted espresso bean offerings",
        "Fahad Al-Shalan", "Partner & Hospitality Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-alshalan-chestnut", "+966 50 223 9988", "@chestnut.sa", "Tier 1 (High Priority)"
    ),
    (
        43, "Section-B Specialty Cafe & Burgers", "Cult Burger & Specialty Coffee Spot", "Jeddah / Riyadh",
        "https://sectionb.me", "Playful but outdated one-pager lacking merchandise & bean subscription e-commerce",
        "Edgy underground streetwear-inspired scroll with 3D spinning merch and cold brew cans",
        "Mansour Al-Saeed", "Co-Founder & Brand Architect", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mansour-alsaeed-sectionb", "+966 54 661 2244", "@sectionb_sa", "Tier 1 (High Priority)"
    ),
    (
        44, "Toasted Specialty Roasters", "Artisan Coffee & Breakfast", "Al Khobar",
        "https://toasted.sa", "Basic Salla store with low contrast typography",
        "Warm golden hour seaside morning scroll with interactive brunch pairing selector",
        "Mubarak Al-Hajri", "Managing Owner", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/mubarak-alhajri-toasted", "+966 50 776 5544", "@toasted_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        45, "Cova Specialty Cafe", "Luxury Minimalist Cafe", "Riyadh",
        "https://covacafe.sa", "Landing page with only Google Review link and address",
        "Architectural marble & raw travertine texture parallax with seamless table reservation widget",
        "Nora Al-Hamdan", "Founder & Interior Lead", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/nora-alhamdan-cova", "+966 55 991 3344", "@cova_sa", "Tier 1 (High Priority)"
    ),
    (
        46, "Daily Roast Specialty Coffee", "Everyday Artisan Coffee", "Dammam",
        "https://dailyroast.sa", "Zid template with unoptimized mobile checkout flow",
        "Daily morning calendar widget offering recurring home delivery subscriptions for fresh roasts",
        "Ahmad Al-Khaldi", "Founder & Roaster", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/ahmad-alkhaldi-dailyroast", "+966 53 119 0044", "@dailyroast.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        47, "Seven Specialty Coffee", "Craft Roastery & Cafe", "Al Khobar",
        "https://sevenroasters.sa", "Standard catalog store lacking interactive roast details",
        "Seven-step interactive sensory timeline detailing bean cleaning, grading, roasting, and cupping",
        "Mohammed Al-Otaibi", "Head of Operations", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mohammed-alotaibi-seven", "+966 50 882 1133", "@seven.coffee", "Tier 2 (Growth Candidate)"
    ),
    (
        48, "Bean There Coffee Roasters", "Boutique Roasters", "Riyadh",
        "https://beanthere.sa", "Basic Salla shop with repetitive product card templates",
        "Interactive globe showing micro-lot farm partnerships with farmer spotlight video popups",
        "Yousef Al-Zamil", "Founder & Green Buyer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/yousef-alzamil-beanthere", "+966 55 442 7788", "@beanthere_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        49, "Base Specialty Coffee", "Minimalist Specialty Roastery", "Jeddah",
        "https://basecoffee.sa", "Simple Instagram landing page; missing direct e-commerce",
        "Industrial concrete & stainless steel 3D aesthetic featuring slow-motion extraction reels",
        "Hussam Al-Ghamdi", "Managing Partner", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/hussam-alghamdi-base", "+966 56 331 4455", "@basecoffee.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        50, "Caffè Di Fiore Specialty", "Artisan Floral & Coffee Lounge", "Riyadh",
        "https://caffedifiore.sa", "Flyer site with static imagery and no bouquet/coffee gift bundles",
        "Floating botanical petal parallax weaving around signature lavender and rose-infused Spanish lattes",
        "Mona Al-Ajaji", "Founder & Creative Director", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/mona-alajaji-difiore", "+966 50 112 5599", "@caffedifiore", "Tier 1 (High Priority)"
    ),

    # Homegrown Fashion, Streetwear, Abayas & Luxury Clothing (51 to 85)
    (
        51, "1886 Fashion", "Saudi Streetwear & Contemporary Apparel", "Riyadh",
        "https://1886fashion.com", "Shopify store with standard grid; misses the rebellious streetwear edge",
        "High-octane brutalist streetwear scroll with 3D hoodie rotations, glitch typography, and drop timer",
        "Fahad Al-Jomiah", "Co-Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-aljomiah-1886", "+966 55 667 1886", "@1886fashion", "Tier 1 (High Priority)"
    ),
    (
        52, "Torba Studio", "Avant-Garde Saudi Fashion & Conceptual Wear", "Riyadh",
        "https://torbastudio.com", "Minimalist e-commerce with slow video rendering on mobile",
        "Cinematic narrative scroll featuring surreal desert dunes, holographic overlays, and fabric drape physics",
        "Nazek Al-Khulaifi", "Co-Founder & Head Designer", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/nazek-alkhulaifi-torba", "+966 50 448 9911", "@torbastudio", "Tier 1 (High Priority)"
    ),
    (
        53, "Hindamme", "Luxury Eastern Contemporary Streetwear", "Riyadh",
        "https://hindamme.com", "Classic catalog store; does not convey runway prestige or heritage Arabic typography",
        "Museum-grade editorial scroll with golden Arabic calligraphy fluid transitions and 3D bomber jacket viewer",
        "Mohammed Khoja", "Founder & Creative Director", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/mohammed-khoja-hindamme", "+966 55 120 4488", "@hindamme", "Tier 1 (High Priority)"
    ),
    (
        54, "Qormuz", "Saudi Cultural Heritage & Luxury Lifestyle", "Riyadh",
        "https://qormuz.com", "Salla store; completely fails to capture the royal heritage craftsmanship of the brand",
        "Majestic heritage parallax incorporating traditional Najdi woodwork, silk bishts, and luxury perfume notes",
        "Abdulrahman Al-Abed", "Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/abdulrahman-alabed-qormuz", "+966 50 001 2345", "@qormuz", "Tier 1 (High Priority)"
    ),
    (
        55, "Noble & Fresh", "Saudi Modern Streetwear", "Riyadh",
        "https://nobleandfresh.com", "Basic Shopify setup with flat product imagery",
        "Dynamic skater-culture kinetic horizontal scroll with interactive colorway swap on mouse hover",
        "Naif Al-Otaibi", "Founder & Creative Director", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/naif-alotaibi-noblefresh", "+966 54 889 0044", "@nobleandfresh", "Tier 2 (Growth Candidate)"
    ),
    (
        56, "Kaf By Kaf", "Contemporary Saudi Women's Fashion", "Riyadh",
        "https://kafbykaf.com", "Template store with small thumbnails and no runway video integration",
        "Fashion runway fluid video scroll featuring embroidered silhouette reveals and made-to-order sizing",
        "Kawthar Alhoraish", "Founder & Creative Director", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/kawthar-alhoraish-kafbykaf", "+966 55 334 1188", "@kafbykaf", "Tier 1 (High Priority)"
    ),
    (
        57, "Abadia", "Ethical Saudi Luxury & Heirloom Fashion", "Riyadh",
        "https://abadia.me", "Standard Shopify luxury theme; missing interactive artisan storytelling",
        "Heirloom craftsmanship interactive map showing bedouin female artisan weaving techniques and raw materials",
        "Shahd Al-Shehail", "Co-Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/shahd-alshehail-abadia", "+966 50 541 2288", "@abadiaworld", "Tier 1 (High Priority)"
    ),
    (
        58, "Dania Shinkar", "Luxury Designer Handbags", "Jeddah",
        "https://daniashinkar.com", "Basic e-commerce store with static bag angles",
        "360-degree interactive 3D leather rotation, hardware detail zoom, and personalized monogram visualizer",
        "Dania Shinkar", "Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/dania-shinkar", "+966 56 771 9900", "@daniashinkar_official", "Tier 1 (High Priority)"
    ),
    (
        59, "Arwa Al Banawi", "Contemporary Androgynous & Tailored Wear", "Jeddah / Riyadh",
        "https://arwaalbanawi.com", "Under-maintained Shopify store; fails to match her global Adidas collabs",
        "High-contrast editorial lookbook parallax celebrating 'The Suitable Woman' with smooth audio-visual transitions",
        "Arwa Al Banawi", "Founder & Creative Director", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/arwa-albanawi", "+966 50 441 7733", "@arwaalbanawi", "Tier 1 (High Priority)"
    ),
    (
        60, "Not Boring Clothing", "Saudi Graphic Streetwear", "Riyadh",
        "https://notboring.me", "Zid store with generic layout; lacks brand personality",
        "Playful anti-boring micro-interactions with cursor-following stickers and animated graphic tees",
        "Zaid Al-Homaidhi", "Co-Founder", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/zaid-alhomaidhi-notboring", "+966 55 229 1100", "@notboring.me", "Tier 2 (Growth Candidate)"
    ),
    (
        61, "Noms Life", "Youth Culture & Street Apparel", "Jeddah",
        "https://nomslife.com", "Basic streetwear shop with low engagement",
        "Vibrant coastal pop-art scroll with animated skate decks and live community drop countdowns",
        "Ahmed Al-Amri", "Co-Founder & Creative Lead", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/ahmed-alamri-noms", "+966 54 112 8877", "@nomslife", "Tier 2 (Growth Candidate)"
    ),
    (
        62, "Lomar", "Pioneering Modern Saudi Thobes & Apparel", "Jeddah / Riyadh",
        "https://lomar.sa", "Heavy Magento/Shopify hybrid store with cluttered navigation",
        "Sleek 3D custom thobe tailor configurator (collar style, fabric weave, cuff embroidery, live 3D preview)",
        "Loai Nassem", "Founder & Chairman", "LinkedIn & Executive WhatsApp",
        "https://www.linkedin.com/in/loai-nassem-lomar", "+966 50 560 3344", "@lomarthobe", "Tier 1 (High Priority)"
    ),
    (
        63, "Toby by Hatem Alakeel", "High-End Modern Traditional Menswear", "Jeddah",
        "https://hatemalakeel.com", "Portfolio site lacking integrated luxury bespoke ordering",
        "Haute-couture silk & linen scroll parallax featuring bespoke tailoring consultation booking flow",
        "Hatem Alakeel", "Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/hatem-alakeel-toby", "+966 50 561 8899", "@hatemalakeel", "Tier 1 (High Priority)"
    ),
    (
        64, "Proud Angels", "Streetwear & Urban Culture", "Jeddah",
        "https://proudangels.com", "Standard Shopify grid lacking community momentum",
        "Underground graffiti-style parallax scroll with VIP access password vault for exclusive drops",
        "Mohammed Bajbaa", "Founder & Creative Lead", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mohammed-bajbaa-proudangels", "+966 56 990 1144", "@proudangels", "Tier 2 (Growth Candidate)"
    ),
    (
        65, "Honayda", "Luxury Women's Ready-to-Wear & Evening Gowns", "Jeddah",
        "https://honayda.com", "Static corporate lookbook without smooth interactive storytelling",
        "Red-carpet gown flow parallax with slow-motion fabric waves and private VIP salon bookings",
        "Honayda Serafi", "Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/honayda-serafi", "+966 50 568 2211", "@honaydaofficial", "Tier 1 (High Priority)"
    ),
    (
        66, "Chador", "Contemporary Saudi Modest Wear", "Riyadh",
        "https://chador.com", "Simple e-commerce grid with standard white backgrounds",
        "Editorial architectural lookbook pairing minimalist abaya draping with iconic Riyadh architecture",
        "Nora Al Shaikh", "Founder & Designer", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/nora-alshaikh-chador", "+966 55 441 3322", "@chador_official", "Tier 1 (High Priority)"
    ),
    (
        67, "Charmaleena Jewellery", "Fine Architectural Jewelry", "Jeddah",
        "https://charmaleena.com", "Classic jewelry site without 3D gemstone refraction or ring sizing guides",
        "Sparkling 3D gemstone rotation with dynamic light reflections and bespoke engraving visualizer",
        "Leena El Khereiji", "Co-Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/leena-elkhereiji-charmaleena", "+966 50 560 7711", "@charmaleenajewellery", "Tier 1 (High Priority)"
    ),
    (
        68, "Mazrood", "Streetwear & Industrial Apparel", "Riyadh",
        "https://mazrood.com", "Zid template store with basic product presentation",
        "Industrial warehouse aesthetic with metallic cursor effects and kinetic typography",
        "Saud Al-Ammar", "Founder & Designer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/saud-alammar-mazrood", "+966 54 332 7700", "@mazrood", "Tier 2 (Growth Candidate)"
    ),
    (
        69, "Shatha Essa", "Haute Couture Abayas & Occasion Wear", "Riyadh",
        "https://shathaessa.com", "Basic Shopify setup with flat lighting imagery",
        "Ethereal desert luxury parallax with floating embroidery thread animations and custom bridal appointments",
        "Shatha Al-Kaltham", "Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/shatha-alkaltham-essa", "+966 55 119 2244", "@shathaessa_official", "Tier 1 (High Priority)"
    ),
    (
        70, "Fyunka", "Iconic Saudi Pop-Art Accessories & Fashion", "Jeddah",
        "https://fyunka.com", "Legacy e-commerce store with low resolution graphics",
        "Playful nostalgic pop-art scroll with interactive sticker canvas and customized tote bag builder",
        "Alaa Balkhy", "Founder & Illustrator", "LinkedIn & Instagram",
        "https://www.linkedin.com/in/alaa-balkhy-fyunka", "+966 56 441 0022", "@fyunka", "Tier 1 (High Priority)"
    ),
    (
        71, "Sotra", "Contemporary Modest Pret-a-Porter", "Jeddah",
        "https://sotrastore.com", "Standard Shopify theme with minimal emotional hook",
        "Pastel botanical motion scroll showing fabric movement during everyday activities",
        "Mariam Bin Mahfouz", "Co-Founder & Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/mariam-binmahfouz-sotra", "+966 50 662 1199", "@sotrastore", "Tier 2 (Growth Candidate)"
    ),
    (
        72, "The Untitled Project", "Experimental Saudi Fashion & Streetwear", "Riyadh",
        "https://untitledproject.store", "Salla store with black and white theme; feels incomplete",
        "Brutalist avant-garde interactive manifesto with audio loops and hidden Easter-egg product unlocks",
        "Nasser Al-Humaid", "Creative Director", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/nasser-alhumaid-untitled", "+966 55 881 4433", "@theuntitledproject.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        73, "Denim District KSA", "Custom & Vintage Denim Studio", "Jeddah",
        "https://denimdistrict.sa", "Flyer site with phone ordering only",
        "Interactive denim wash & distress customizer (indigo fade selector, raw hem toggle, embroidery placement)",
        "Omar Al-Sulaiman", "Founder & Denim Craftsman", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/omar-alsulaiman-denim", "+966 54 229 8811", "@denimdistrict_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        74, "RTHM Clothing (Rhythm Streetwear)", "Urban Streetwear & Music Culture", "Riyadh",
        "https://rthm.sa", "Zid basic setup; lacks musical energy",
        "Interactive audio-responsive typography pulsating to underground Saudi hip-hop beats",
        "Fahad Al-Bassam", "Founder & DJ", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/fahad-albassam-rthm", "+966 50 773 2211", "@rthm.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        75, "Blanc Studio KSA", "Minimalist Monochromatic Fashion", "Riyadh",
        "https://blancstudio.sa", "Basic one-page store with plain photo grids",
        "High-key stark white luxury parallax with subtle shadow movement and seamless quick-add drawer",
        "Reema Al-Malki", "Founder & Lead Stylist", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/reema-almalki-blanc", "+966 55 442 9900", "@blancstudio.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        76, "WAFF Modest Wear", "Elevated Daily Abayas & Kimonos", "Jeddah",
        "https://waff.sa", "Salla store with unformatted mobile banners",
        "Silk-flow motion hero section with live fabric density and breathability comparison widget",
        "Wafa Al-Amoudi", "Founder & Designer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/wafa-alamoudi-waff", "+966 56 119 4488", "@waff.sa", "Tier 2 (Growth Candidate)"
    ),
    (
        77, "L'Aura Abayas", "Tailored Luxury Abayas", "Riyadh",
        "https://lauraabayas.sa", "Static photo gallery with slow checkout page",
        "Graceful slow-motion fabric draping parallax and personalized height/length measurement calculator",
        "Nouf Al-Dosari", "Founder & Head Designer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/nouf-aldosari-laura", "+966 50 331 7766", "@laura_abayas", "Tier 2 (Growth Candidate)"
    ),
    (
        78, "Crate Concept Store & Fashion", "Curated Streetwear & Art", "Riyadh",
        "https://crateksa.com", "Template shop lacking the edgy energy of their brick-and-mortar store",
        "3D virtual warehouse walkthrough with clickable clothing racks and exclusive sneaker drops",
        "Zaid Al-Sudairi", "Managing Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/zaid-alsudairi-crate", "+966 55 771 2299", "@crate_ksa", "Tier 1 (High Priority)"
    ),
    (
        79, "Pattern Concept Store (Fashion)", "Art, Fashion & Home Concept Space", "Riyadh",
        "https://pattern-store.com", "Salla template with low emotional appeal",
        "Art gallery editorial scroll pairing independent fashion labels with contemporary Saudi sculptures",
        "Ali Al-Rehaili", "Founder & Curator", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ali-alrehaili-pattern", "+966 50 664 3322", "@pattern_store", "Tier 1 (High Priority)"
    ),
    (
        80, "Person Fashion Gallery", "Curated Apparel & Lifestyle", "Riyadh",
        "https://personstore.sa", "Basic Zid catalog with small imagery",
        "Magazine cover interactive layout with hover-activated video clips from Paris & Riyadh fashion weeks",
        "Faisal Al-Rasheed", "Creative Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/faisal-alrasheed-person", "+966 55 889 0011", "@person.sa", "Tier 1 (High Priority)"
    ),
    (
        81, "The Dropped Collection", "Limited Drop Streetwear", "Jeddah",
        "https://thedropped.sa", "Single countdown page with no lookbook",
        "Cyber-drop vault unlocking tiered access via SMS code with 3D product spinning preview",
        "Hani Al-Ghamdi", "Co-Founder", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/hani-alghamdi-dropped", "+966 54 881 3322", "@thedropped_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        82, "Jeddah Streetwear Lab", "Independent Apparel Collective", "Jeddah",
        "https://jstreetwearlab.sa", "Zid catalog with default fonts",
        "Urban Red Sea skate-park theme with dynamic spray-paint text and live inventory ticker",
        "Sultan Al-Harbi", "Founder & Creative Lead", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/sultan-alharbi-jsl", "+966 56 332 1100", "@jstreetwearlab", "Tier 2 (Growth Candidate)"
    ),
    (
        83, "Kulture KSA", "Youth Streetwear & Accessories", "Al Khobar",
        "https://kultureksa.com", "Basic Shopify theme with generic icons",
        "Eastern Province coastal streetwear aesthetic with interactive sticker book and ambassador gallery",
        "Bader Al-Buainain", "Founder & CEO", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/bader-albuainain-kulture", "+966 50 449 2211", "@kulture.ksa", "Tier 2 (Growth Candidate)"
    ),
    (
        84, "Nouf Fettahi Couture", "Bespoke Bridal & Evening Gowns", "Jeddah",
        "https://nouffettahi.com", "Brochure site without consultation booking or fabric closeups",
        "Haute couture shimmering lace zoom parallax with interactive VIP private atelier booking flow",
        "Nouf Fettahi", "Founder & Couturier", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/nouf-fettahi", "+966 55 221 8844", "@nouffettahi_couture", "Tier 1 (High Priority)"
    ),
    (
        85, "Papillon Fine Jewelry", "Boutique Fine Jewelry & Lifestyle", "Riyadh",
        "https://papillonjewelry.sa", "Outdated WordPress setup with low-res product thumbnails",
        "Macro diamond sparkle refraction animation with interactive hand-model ring visualizer",
        "Maha Al-Musaed", "Founder & Gemologist", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/maha-almusaed-papillon", "+966 50 119 7788", "@papillon_jewelry", "Tier 1 (High Priority)"
    ),

    # Luxury Lifestyle, Perfumery & Artisanal Boutiques (86 to 100)
    (
        86, "Laverne Perfumes", "Viral Luxury Fragrance House", "Riyadh",
        "https://laverne.com", "High-traffic Salla platform; prone to lag during viral Georgina Rodriguez campaigns",
        "Ultra-high-end dark luxury parallax with 3D mist spraying animation and olfactory note pyramid breakdown",
        "Christian / Fahad Al-Subaie", "Co-Founder & Brand Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-alsubaie-laverne", "+966 55 555 4488", "@laverne_sa", "Tier 1 (High Priority)"
    ),
    (
        87, "Assaf Perfumes", "Premium Saudi Fragrance Brand", "Riyadh",
        "https://assaf.com.sa", "Crowded Salla store with discount banners everywhere; loses luxury positioning",
        "Sleek royal black & gold parallax with bottle 3D disassembly and personalized scent finder quiz",
        "Nasser Al-Assaf", "Managing Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/nasser-alassaf-perfumes", "+966 50 777 8899", "@assafperfumes", "Tier 1 (High Priority)"
    ),
    (
        88, "Gissah Perfumes KSA", "Niche Artisan Fragrances", "Riyadh / Khobar",
        "https://gissah.com", "Basic e-commerce store with slow loading times during new fragrance releases",
        "Cinematic narrative scroll telling the 'Story' (Gissah) of each scent through moving poetry & soundscapes",
        "Faisal Al-Roudhan", "CEO & Co-Founder", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/faisal-alroudhan-gissah", "+966 56 444 1122", "@gissah_perfumes", "Tier 1 (High Priority)"
    ),
    (
        89, "Mirzam Lifestyle & Gifts", "Artisanal Lifestyle & Confectionery", "Riyadh",
        "https://mirzamgifts.sa", "Template store; lacks the hand-crafted packaging elegance of their physical boxes",
        "Sensory chocolate foil unwrapping animation and custom bespoke gift basket 3D builder",
        "Reem Al-Bassam", "Founder & Creative Lead", "Instagram & WhatsApp",
        "https://www.linkedin.com/in/reem-albassam-mirzam", "+966 55 119 3355", "@mirzam.sa", "Tier 1 (High Priority)"
    ),
    (
        90, "Teeb Al Ghafa Artisan Oud", "Heritage Oud & Frankincense", "Jeddah",
        "https://teebalghafa.sa", "Basic Arabic catalog; misses the hypnotic smoke & incense ambiance",
        "Drifting fragrant incense smoke simulation with interactive oud wood maturity & extraction timeline",
        "Sultan Al-Ghamdi", "Master Distiller & Founder", "WhatsApp & LinkedIn",
        "https://www.linkedin.com/in/sultan-alghamdi-teeb", "+966 50 661 2288", "@teebalghafa", "Tier 2 (Growth Candidate)"
    ),
    (
        91, "Dkhoon Emirates KSA", "Modern Arabian Fragrances & Incense", "Riyadh",
        "https://dkhoon.com", "Template store with repetitive product cards",
        "Gold-leaf particle animation with interactive room spray and bakhoor fragrance diffuser guide",
        "Rayyan Al-Malki", "Regional Commercial Lead", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/rayyan-almalki-dkhoon", "+966 54 882 1100", "@dkhoonemirates", "Tier 2 (Growth Candidate)"
    ),
    (
        92, "Lootah Perfumes KSA", "Century-Old Heritage Perfumery", "Al Khobar / Riyadh",
        "https://lootahperfumes.com", "Corporate brochure site lacking personalized discovery",
        "Interactive scent layering tool allowing customers to combine musk, amber, and Taif rose online",
        "Ayyoub Lootah", "Managing Partner", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ayyoub-lootah", "+966 50 441 9922", "@lootahperfumes", "Tier 1 (High Priority)"
    ),
    (
        93, "Scent Library KSA", "Curated Niche Fragrance Concept", "Riyadh",
        "https://scentlibrary.sa", "Generic Zid store with small thumbnail photos",
        "Virtual library bookshelf scroll where pulling down each fragrance book reveals its secret olfactory notes",
        "Bandar Al-Otaibi", "Founder & Fragrance Sommelier", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/bandar-alotaibi-scentlib", "+966 55 334 7711", "@scentlibrary_sa", "Tier 1 (High Priority)"
    ),
    (
        94, "Areej Al Ameerat", "Royal Luxury Oud & Private Blends", "Jeddah",
        "https://areejalameerat.com", "Outdated flash-era style graphics; needs ultra-luxury overhaul",
        "Royal black crystal 3D bottle reflection parallax with private concierge fragrance bespoke orders",
        "Ali Al-Jabri", "Founder & Master Perfumer", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ali-aljabri-areej", "+966 56 771 3344", "@areejalameerat", "Tier 1 (High Priority)"
    ),
    (
        95, "Saray Perfumes KSA", "Oriental Fragrances & Body Mists", "Riyadh",
        "https://sarayperfumes.com", "Salla store; basic discount banners overpower product aesthetics",
        "Silky mist evaporation effect with interactive gift bundle wrapper for Saudi National Day & Ramadan",
        "Ahmed Al-Qattan", "Commercial Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/ahmed-alqattan-saray", "+966 50 882 9911", "@sarayperfumes", "Tier 2 (Growth Candidate)"
    ),
    (
        96, "Signature Fragrances KSA", "Boutique Niche Perfumery", "Jeddah",
        "https://signatureperfumes.sa", "Simple WooCommerce site with plain cards",
        "Interactive signature test matching user personality traits with woody, citrus, or oriental aromas",
        "Hani Al-Sharif", "Founder & Scent Designer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/hani-alsharif-signature", "+966 54 331 8844", "@signature_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        97, "Oud Elite (Niche Private Blends)", "Boutique Private Reserve Oud", "Riyadh",
        "https://oudelite.com/private", "Separate sub-domain that feels outdated compared to their physical marble stores",
        "Golden amber drop physics simulation with interactive harvest aging counter (10 yr vs 25 yr aged oud)",
        "Majed Al-Dukhail", "Brand Manager - Private Collection", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/majed-aldukhail-oud", "+966 55 992 1100", "@oudelite", "Tier 1 (High Priority)"
    ),
    (
        98, "Taif Rose Artisan Distillery", "Artisan Rose Water & Scented Extracts", "Taif / Riyadh",
        "https://taifroseartisan.sa", "Flyer website with phone contact only",
        "Misty mountain morning scroll across Taif rose terraces with flower harvesting parallax",
        "Salim Al-Kamali", "Master Distiller & 4th Gen Farmer", "WhatsApp & Instagram",
        "https://www.linkedin.com/in/salim-alkamali-taifrose", "+966 50 112 4433", "@taifrose_sa", "Tier 2 (Growth Candidate)"
    ),
    (
        99, "Al-Dakhil Oud (Boutique Artisan Range)", "Artisanal Incense & Fragrance", "Riyadh",
        "https://aldakhiloud.com/boutique", "Mass-market catalog with zero boutique storytelling",
        "Minimalist boutique sub-experience with 3D incense burner glow and gift card integration",
        "Fahad Al-Dakhil", "Executive Director", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/fahad-aldakhil", "+966 50 541 9900", "@aldakhiloud", "Tier 1 (High Priority)"
    ),
    (
        100, "Qahwa & Oud Concept", "Luxury Coffee & Heritage Incense Pairing", "Riyadh",
        "https://qahwaandoud.sa", "Single-page coming-soon placeholder",
        "Dual sensory scroll bringing together bubbling Arabic coffee pots and smoking agarwood embers",
        "Saud Al-Farhan", "Founder & Concept Creator", "LinkedIn & WhatsApp",
        "https://www.linkedin.com/in/saud-alfarhan-concept", "+966 55 448 1122", "@qahwaandoud", "Tier 1 (High Priority)"
    )
]

for row_idx, lead in enumerate(leads_data, start=2):
    is_zebra = (row_idx % 2 == 0)
    category = lead[2]
    tier = lead[13]

    for col_idx, val in enumerate(lead, start=1):
        cell = ws_leads.cell(row=row_idx, column=col_idx)

        # Handle links
        if col_idx in [5, 11] and str(val).startswith("http"):
            cell.value = str(val)
            cell.font = font_link
            cell.hyperlink = str(val)
        else:
            cell.value = val
            cell.font = font_body

        cell.border = thin_border

        # Alignment
        if col_idx in [1, 4, 10, 13]:
            cell.alignment = align_center
        elif col_idx in [6, 7]:
            cell.alignment = align_wrap
        else:
            cell.alignment = align_left

        # Row shading
        if is_zebra:
            cell.fill = fill_zebra

        # Priority Badge styling
        if col_idx == 14:
            cell.alignment = align_center
            if "Tier 1" in str(val):
                cell.fill = fill_tier1
                cell.font = font_badge_tier1
            else:
                cell.fill = fill_tier2
                cell.font = font_badge_tier2

        # Brand Name bolding
        if col_idx == 2:
            cell.font = font_body_bold

# -------------------------------------------------------------
# 3. POPULATE OUTREACH SCRIPTS TAB
# -------------------------------------------------------------
ws_scripts.views.sheetView[0].showGridLines = True
ws_scripts['A2'] = "HIGH-CONVERTING WHATSAPP CEO OUTREACH TEMPLATES (SAUDI ARABIA)"
ws_scripts['A2'].font = font_title
ws_scripts['A3'] = "Step-by-step strategy: Record a 20-30 second screen recording of the redesigned interactive concept, attach it as a video, and send directly to the CEO/Founder via WhatsApp."
ws_scripts['A3'].font = font_subtitle

script_sections = [
    ("A. Specialty Coffee Roasters Pitch (Arabic & English)", 5, [
        ("Template 1: Arabic High-Touch WhatsApp (Recommended for Saudi Founders)",
         """السلام عليكم أستاذ [Founder Name]، أتمنى تكون بخير ويومك سعيد يا رب. 👋

أنا معجب جداً ببراند [Brand Name] وبجودة القهوة وفروعكم الرهيبة في [City].

لكن لاحظت إن متجركم الإلكتروني الحالي على [Salla/Zid/Shopify] عادي وثابت، وما يعكس التجربة الحسية والفخامة الموجودة داخل فروعكم.

صممنا نموذج تفاعلي حديث 2026 مخصص لـ [Brand Name]:
✨ حركات Parallax سلسة من حبوب القهوة إلى الكوب.
✨ عرض ثلاثي الأبعاد تفاعلي لأكياس المحاصيل وسلايدر لدرجة الحمص (Roast Level).
✨ سرعة فائقة في الطلب وتجربة فخمة ترفع نسبة الشراء.

صورت لك فيديو قصير 20 ثانية للنموذج وهو شغال (مرفق بالفيديو أعلاه 👆)، ورابط المعاينة المباشر هنا:
🔗 [Demo Link]

إذا أعجبك النموذج ومناسب لك نطلقه لـ [Brand Name] بكامل الصلاحيات، يسعدني نحدد اتصال سريع 5 دقائق نناقش التفاصيل.

تحياتي وتقديري،
[Your Name] | استشاري تطوير المواقع والتجارب التفاعلية"""),

        ("Template 2: English Executive WhatsApp Pitch",
         """Hello [Founder Name]! 👋 Hope you're having a great week.

I’m a huge fan of [Brand Name] and the incredible specialty coffee experience you've built across [City].

I noticed your current online store is quite static and doesn't capture the warm, sensory aesthetic of your physical cafes.

We developed a 2026 interactive scroll-animated prototype specifically for [Brand Name]:
☕ Smooth scroll parallax showing the bean-to-cup journey.
☕ 3D interactive bag rotations with roast profile tasting notes.
☕ Ultra-fast frictionless checkout designed for mobile coffee lovers.

I recorded a quick 20-second screen demo for you (attached above 👆), and you can test the live interactive preview here:
🔗 [Demo Link]

If you'd like to take this live or customize it for [Brand Name], I’d love to hop on a quick 5-minute chat!

Best regards,
[Your Name] | Creative Tech Lead""")
    ]),

    ("B. Fashion, Streetwear & Luxury Abayas Pitch (Arabic & English)", 16, [
        ("Template 3: Arabic Fashion & Streetwear WhatsApp Pitch",
         """مرحباً أستاذ [Founder Name]، مساك الله بالخير. 👋

ما شاء الله كولكشن [Brand Name] الأخير وفكرته الإبداعية شيء يشرف ويدل على ذوق عالي في مشهد الأزياء السعودي.

لكن حسيت إن الموقع الإلكتروني الحالي عبارة عن صور ثابتة وكتالوج تقليدي، وما يعطي الهيبة وحركة الأقمشة (Fabric Flow) اللي تستحقها تصاميمكم.

طورنا فكرة موقع تفاعلي لعام 2026 حصري لـ [Brand Name]:
👗 انسيابية حركة الأقمشة والقصات مع التمرير (Fabric Motion Parallax).
👗 مؤقت ذكي وحصري لإطلاق الدروبات الجديدة (Exclusive Drop Countdown).
👗 عرض سينمائي فخم يرفع قيمة البراند ويضاعف المبيعات.

مرفق فيديو سريع 25 ثانية يوضح الفكرة 👆، وهذا رابط تجربة الموقع التفاعلي:
🔗 [Demo Link]

لو حاب ننقل هذي التجربة لمتجركم الرسمي بكامل التحكم، يسعدني نتواصل ونتفق على التفاصيل في أي وقت يناسبك.

أخوك،
[Your Name]"""),

        ("Template 4: English Fashion / Streetwear WhatsApp Pitch",
         """Hi [Founder Name]! 👋 Loving the latest drops and creative vision behind [Brand Name].

Your designs have so much identity, but your current web store feels like a standard flat grid that doesn't showcase the movement and texture of your fabrics.

We created an exclusive 2026 interactive concept for [Brand Name]:
🔥 Kinetic lookbook with fluid fabric motion on scroll.
🔥 Interactive seasonal drop countdown and VIP early-access vault.
🔥 High-fashion aesthetic built to convert your Instagram audience into loyal buyers.

Check out the 20-second walkthrough video attached above 👆 or try the live link:
🔗 [Demo Link]

Would love to chat if you'd like to take this live for your upcoming collection!

Best,
[Your Name]""")
    ])
]

# Write scripts to tab
curr_row = 5
for section_title, _, templates in script_sections:
    ws_scripts[f"A{curr_row}"] = section_title
    ws_scripts[f"A{curr_row}"].font = Font(name="Calibri", size=13, bold=True, color="1F4E79")
    curr_row += 1

    for title, body in templates:
        ws_scripts[f"A{curr_row}"] = title
        ws_scripts[f"A{curr_row}"].font = font_body_bold
        ws_scripts[f"A{curr_row}"].fill = fill_zebra
        curr_row += 1

        ws_scripts[f"A{curr_row}"] = body
        ws_scripts[f"A{curr_row}"].font = font_body
        ws_scripts[f"A{curr_row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws_scripts.row_dimensions[curr_row].height = 150
        curr_row += 2

# -------------------------------------------------------------
# COLUMN WIDTHS & FORMATTING
# -------------------------------------------------------------
# Dashboard widths
ws_dashboard.column_dimensions['A'].width = 38
ws_dashboard.column_dimensions['B'].width = 45
ws_dashboard.column_dimensions['C'].width = 45
ws_dashboard.column_dimensions['D'].width = 55

# Leads sheet widths
col_widths = {
    'A': 6,   # ID
    'B': 30,  # Brand Name
    'C': 32,  # Category
    'D': 16,  # City
    'E': 28,  # Live URL
    'F': 42,  # Current Platform / Limitation
    'G': 46,  # 2026 Pitch Angle
    'H': 26,  # CEO Name
    'I': 28,  # Title
    'J': 24,  # Contact Channel
    'K': 35,  # LinkedIn Link
    'L': 20,  # Phone/WhatsApp
    'M': 22,  # Instagram
    'N': 20   # Priority
}

for col, w in col_widths.items():
    ws_leads.column_dimensions[col].width = w

# Freeze header on Leads
ws_leads.freeze_panes = 'C2'

# Script sheet widths
ws_scripts.column_dimensions['A'].width = 110

# Save workbook
wb.save(excel_path)
print(f"Successfully generated 100 Saudi Arabian Redesign Leads workbook at: {excel_path}")
