import os
import shutil
import xlsxwriter

# Output paths
workspace_dir = r"c:\Users\Viranga\Downloads\upwrok new"
downloads_dir = r"c:\Users\Viranga\Downloads"
file_name = "Upwork_Client_Leads_Tracker.xlsx"

file_path = os.path.join(workspace_dir, file_name)

workbook = xlsxwriter.Workbook(file_path)

# ==================== FORMAT DEFINITIONS ====================
font_family = "Segoe UI"

# Colors
COLOR_NAVY = "#1B365D"
COLOR_NAVY_LIGHT = "#2C4C7E"
COLOR_HEADER_BG = "#1A365D"
COLOR_ZEBRA_LIGHT = "#F8FAFC"
COLOR_BORDER = "#CBD5E1"
COLOR_ACCENT_BLUE = "#0284C7"
COLOR_CARD_BG = "#F1F5F9"

# Format: Title & Subtitle
title_fmt = workbook.add_format({
    "font_name": font_family,
    "font_size": 16,
    "bold": True,
    "font_color": COLOR_NAVY,
    "valign": "vcenter"
})
subtitle_fmt = workbook.add_format({
    "font_name": font_family,
    "font_size": 9.5,
    "font_color": "#64748B",
    "valign": "vcenter"
})

# Format: KPI Summary Cards
kpi_card_label = workbook.add_format({
    "font_name": font_family,
    "font_size": 8.5,
    "bold": True,
    "font_color": "#475569",
    "bg_color": COLOR_CARD_BG,
    "align": "center",
    "valign": "vcenter",
    "top": 1, "bottom": 0, "left": 1, "right": 1,
    "top_color": COLOR_BORDER, "left_color": COLOR_BORDER, "right_color": COLOR_BORDER
})
kpi_card_val = workbook.add_format({
    "font_name": font_family,
    "font_size": 16,
    "bold": True,
    "font_color": COLOR_NAVY,
    "bg_color": COLOR_CARD_BG,
    "align": "center",
    "valign": "vcenter",
    "top": 0, "bottom": 1, "left": 1, "right": 1,
    "bottom_color": COLOR_BORDER, "left_color": COLOR_BORDER, "right_color": COLOR_BORDER
})

# Format: Table Header
header_fmt = workbook.add_format({
    "font_name": font_family,
    "font_size": 10,
    "bold": True,
    "font_color": "#FFFFFF",
    "bg_color": COLOR_HEADER_BG,
    "align": "center",
    "valign": "vcenter",
    "border": 1,
    "border_color": "#0F172A",
    "text_wrap": True
})

# Data Row Formats (Regular & Zebra)
def make_data_fmt(bg_color=None, align="left", bold=False, is_date=False, is_currency=False):
    d = {
        "font_name": font_family,
        "font_size": 9.5,
        "font_color": "#0F172A",
        "align": align,
        "valign": "vcenter",
        "border": 1,
        "border_color": COLOR_BORDER,
        "bold": bold,
        "text_wrap": True
    }
    if bg_color:
        d["bg_color"] = bg_color
    if is_date:
        d["num_format"] = "yyyy-mm-dd"
    if is_currency:
        d["num_format"] = "$#,##0"
    return workbook.add_format(d)

cell_id_white = make_data_fmt(align="center", bold=True)
cell_id_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT, align="center", bold=True)

cell_text_white = make_data_fmt()
cell_text_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT)

cell_bold_white = make_data_fmt(bold=True)
cell_bold_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT, bold=True)

cell_center_white = make_data_fmt(align="center")
cell_center_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT, align="center")

cell_date_white = make_data_fmt(align="center", is_date=True)
cell_date_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT, align="center", is_date=True)

cell_curr_white = make_data_fmt(align="right", is_currency=True)
cell_curr_zebra = make_data_fmt(bg_color=COLOR_ZEBRA_LIGHT, align="right", is_currency=True)

# Link Formats
link_fmt_white = workbook.add_format({
    "font_name": font_family,
    "font_size": 9.5,
    "font_color": "#0284C7",
    "underline": 1,
    "valign": "vcenter",
    "border": 1,
    "border_color": COLOR_BORDER,
    "text_wrap": True
})
link_fmt_zebra = workbook.add_format({
    "font_name": font_family,
    "font_size": 9.5,
    "font_color": "#0284C7",
    "underline": 1,
    "bg_color": COLOR_ZEBRA_LIGHT,
    "valign": "vcenter",
    "border": 1,
    "border_color": COLOR_BORDER,
    "text_wrap": True
})

# Status Tag Formats (for visual badges)
status_colors = {
    "New Lead": {"bg": "#E0F2FE", "fg": "#0369A1"},            # Soft Blue
    "Proposal Sent": {"bg": "#FEF3C7", "fg": "#B45309"},       # Amber/Yellow
    "In Discussion": {"bg": "#E0E7FF", "fg": "#4338CA"},       # Indigo
    "Meeting Scheduled": {"bg": "#FCE7F3", "fg": "#BE185D"},   # Pink
    "Hired / Won": {"bg": "#DCFCE7", "fg": "#15803D"},         # Green
    "Follow Up Needed": {"bg": "#FFEDD5", "fg": "#C2410C"},    # Orange
    "Closed / Lost": {"bg": "#F1F5F9", "fg": "#64748B"}        # Slate Gray
}

# ==================== WORKSHEET 1: LEADS & CLIENT PIPELINE ====================
ws = workbook.add_worksheet("Leads & Client Pipeline")
ws.set_tab_color("#1B365D")
ws.hide_gridlines(0)

# Set Column Widths for comfortable continuous reading & filling
columns_config = [
    ("A", 7),    # ID
    ("B", 13),   # Date Added
    ("C", 22),   # Client / Company
    ("D", 15),   # Client Country
    ("E", 40),   # Job Title & Description
    ("F", 16),   # Contact Channel
    ("G", 32),   # Contact Details & Link
    ("H", 20),   # Upwork Job Link
    ("I", 15),   # Budget / Rate
    ("J", 20),   # Lead Status
    ("K", 16),   # Assigned Lead
    ("L", 18),   # Next Action / Date
    ("M", 34)    # Notes & Tech Stack
]

for col, width in columns_config:
    ws.set_column(f"{col}:{col}", width)

# Title Header Banner
ws.set_row(0, 24)
ws.write("A1", "UPWORK CLIENT LEADS & ENGAGEMENT TRACKER", title_fmt)
ws.set_row(1, 16)
ws.write("A2", "Structured pipeline for continuous lead logging, outreach tracking, client contacts, and proposal status.", subtitle_fmt)

# KPI Summary Cards (Row 3 & 4)
ws.set_row(2, 16)
ws.set_row(3, 26)

# Card 1: Total Leads
ws.write("B3", "TOTAL LEADS", kpi_card_label)
ws.write_formula("B4", '=COUNTA(A7:A100)', kpi_card_val)

# Card 2: Proposals Sent
ws.write("D3", "PROPOSALS SENT", kpi_card_label)
ws.write_formula("D4", '=COUNTIF(J7:J100, "*Proposal*")', kpi_card_val)

# Card 3: In Discussion / Meetings
ws.write("F3", "IN ACTIVE DISCUSSION", kpi_card_label)
ws.write_formula("F4", '=COUNTIF(J7:J100, "*Discussion*") + COUNTIF(J7:J100, "*Meeting*")', kpi_card_val)

# Card 4: Hired / Won
ws.write("H3", "HIRED / WON", kpi_card_label)
ws.write_formula("H4", '=COUNTIF(J7:J100, "*Won*")', kpi_card_val)

# Card 5: Follow Up Required
ws.write("J3", "FOLLOW UP NEEDED", kpi_card_label)
ws.write_formula("J4", '=COUNTIF(J7:J100, "*Follow*")', kpi_card_val)

# Table Header Row (Row 6 -> index 5)
ws.set_row(5, 32)
headers = [
    "ID",
    "Date Added",
    "Client / Company",
    "Client Country",
    "Job Title & Description",
    "Contact Channel",
    "Contact Details & Link",
    "Upwork Job Link",
    "Budget / Rate ($)",
    "Lead Status",
    "Assigned Lead",
    "Next Action / Date",
    "Notes & Tech Stack"
]

for col_idx, header_text in enumerate(headers):
    ws.write(5, col_idx, header_text, header_fmt)

# Freeze Panes at Row 7 (index 6) so header stays locked when scrolling!
ws.freeze_panes(6, 0)

# ==================== DATA ROWS ====================

# Pre-filled verified records
initial_data = [
    # Row 1: From user screenshot
    {
        "id": "01",
        "date": "2026-10-24",
        "client": "Impact Health RX",
        "country": "United States",
        "desc": "Compounding Pharmacy API Expert | Connect 20+ Pharmacies to Impact Health RX\n(Posted 3 weeks ago)",
        "channel": "WhatsApp",
        "contact_label": "WhatsApp: +1 (802) 838-9347",
        "contact_url": "https://wa.me/18028389347",
        "upwork_label": "View Upwork Job",
        "upwork_url": "https://www.upwork.com/jobs/~02173648488037140975?referrer_url_path=%2Fnx%2Fsearch%2Fjobs%2Fdetails%2F~02173648488037140975",
        "budget": 2500,
        "status": "In Discussion",
        "assignee": "Viranga Lakshan",
        "next_action": "Follow up via WhatsApp",
        "notes": "Connect 20+ compounding pharmacies to API. Requires EHR/EMR & HIPAA compliance."
    },
    # Row 2: Economic Architecture Advisory
    {
        "id": "02",
        "date": "2026-11-13",
        "client": "Economic Architecture Advisory",
        "country": "Saudi Arabia",
        "desc": "Website Design & Infrastructure Setup (Bilingual AR/EN Sovereign Advisory Firm on econarc.com.sa)",
        "channel": "Direct Email",
        "contact_label": "Haitham.al.rebh@gmail.com",
        "contact_url": "mailto:Haitham.al.rebh@gmail.com",
        "upwork_label": "LinkedIn / Upwork",
        "upwork_url": "https://linkedin.com/in/viranga-lakshan-869515279",
        "budget": 3500,
        "status": "Proposal Sent",
        "assignee": "Viranga Lakshan",
        "next_action": "Awaiting review for intro call",
        "notes": "Sent 4-page sovereign proposal & 5 CVs. Webflow CMS + Noto Sans Arabic + Google Workspace email."
    },
    # Row 3: TribeAWL / ReplenishMD
    {
        "id": "03",
        "date": "2026-11-13",
        "client": "TribeAWL / ReplenishMD",
        "country": "United States",
        "desc": "Long Term Technical Lead (Business & Workforce Platform, Clinical Scheduling & Medication Management)",
        "channel": "Direct Email",
        "contact_label": "ReplenishMD Executive",
        "contact_url": "mailto:contact@replenishmd.com",
        "upwork_label": "View Upwork Job",
        "upwork_url": "https://www.upwork.com",
        "budget": 10000,
        "status": "In Discussion",
        "assignee": "Chamara Lahiru",
        "next_action": "Schedule 15-min tech call",
        "notes": "Client asked about medication apps, marketplaces & streaming. Sent 5-member team credentials & live links."
    },
    # Row 4: Selloship B2B Shipping Platform
    {
        "id": "04",
        "date": "2026-11-14",
        "client": "Selloship",
        "country": "India",
        "desc": "B2B Shipping Platform India (Multi-carrier freight aggregator, 15+ B2B carriers, E-Way Bill, Rate Engine)",
        "channel": "Upwork Chat",
        "contact_label": "Selloship Hiring Lead",
        "contact_url": "https://www.upwork.com",
        "upwork_label": "View Upwork Job",
        "upwork_url": "https://www.upwork.com",
        "budget": 20000,
        "status": "New Lead",
        "assignee": "Avishka Meddegoda",
        "next_action": "Draft 3-phase technical proposal",
        "notes": "Huge B2B logistics build. Carrier Adapter Pattern, NIC E-Way Bill API, CFT rate engine & weight dispute desk."
    }
]

# Write pre-filled rows
start_row = 6  # 0-indexed (Row 7 in Excel)

for i, row in enumerate(initial_data):
    current_row = start_row + i
    is_zebra = (i % 2 == 1)
    
    # Select formats based on zebra striping
    c_id = cell_id_zebra if is_zebra else cell_id_white
    c_txt = cell_text_zebra if is_zebra else cell_text_white
    c_bld = cell_bold_zebra if is_zebra else cell_bold_white
    c_cnt = cell_center_zebra if is_zebra else cell_center_white
    c_date = cell_date_zebra if is_zebra else cell_date_white
    c_curr = cell_curr_zebra if is_zebra else cell_curr_white
    c_link = link_fmt_zebra if is_zebra else link_fmt_white
    
    ws.set_row(current_row, 42)  # Generous row height for clean text wrapping
    
    ws.write(current_row, 0, row["id"], c_id)
    ws.write(current_row, 1, row["date"], c_date)
    ws.write(current_row, 2, row["client"], c_bld)
    ws.write(current_row, 3, row["country"], c_cnt)
    ws.write(current_row, 4, row["desc"], c_txt)
    ws.write(current_row, 5, row["channel"], c_cnt)
    
    # Clickable Contact Link
    if row.get("contact_url"):
        ws.write_url(current_row, 6, row["contact_url"], c_link, string=row["contact_label"])
    else:
        ws.write(current_row, 6, row["contact_label"], c_txt)
        
    # Clickable Upwork Link
    if row.get("upwork_url"):
        ws.write_url(current_row, 7, row["upwork_url"], c_link, string=row["upwork_label"])
    else:
        ws.write(current_row, 7, "-", c_cnt)
        
    ws.write(current_row, 8, row["budget"], c_curr)
    ws.write(current_row, 9, row["status"], c_cnt)
    ws.write(current_row, 10, row["assignee"], c_cnt)
    ws.write(current_row, 11, row["next_action"], c_txt)
    ws.write(current_row, 12, row["notes"], c_txt)

# ==================== BLANK FORMATTED ROWS FOR CONTINUOUS FILLING ====================
# Add 30 pre-formatted blank rows (ID 05 to 34)
total_blank_rows = 30
for j in range(total_blank_rows):
    current_row = start_row + len(initial_data) + j
    is_zebra = ((len(initial_data) + j) % 2 == 1)
    
    c_id = cell_id_zebra if is_zebra else cell_id_white
    c_txt = cell_text_zebra if is_zebra else cell_text_white
    c_bld = cell_bold_zebra if is_zebra else cell_bold_white
    c_cnt = cell_center_zebra if is_zebra else cell_center_white
    c_date = cell_date_zebra if is_zebra else cell_date_white
    c_curr = cell_curr_zebra if is_zebra else cell_curr_white
    
    ws.set_row(current_row, 32)
    
    next_id = f"{len(initial_data) + j + 1:02d}"
    ws.write(current_row, 0, next_id, c_id)
    ws.write_blank(current_row, 1, None, c_date)
    ws.write_blank(current_row, 2, None, c_bld)
    ws.write_blank(current_row, 3, None, c_cnt)
    ws.write_blank(current_row, 4, None, c_txt)
    ws.write_blank(current_row, 5, None, c_cnt)
    ws.write_blank(current_row, 6, None, c_txt)
    ws.write_blank(current_row, 7, None, c_txt)
    ws.write_blank(current_row, 8, None, c_curr)
    ws.write_blank(current_row, 9, None, c_cnt)
    ws.write_blank(current_row, 10, None, c_cnt)
    ws.write_blank(current_row, 11, None, c_txt)
    ws.write_blank(current_row, 12, None, c_txt)

# ==================== DATA VALIDATION (DROPDOWNS) ====================
# Range for all data rows: 7 to 50
max_row_idx = start_row + len(initial_data) + total_blank_rows - 1

# Dropdown: Country (Column D -> col 3)
countries_list = [
    "United States", "United Kingdom", "Canada", "Australia", 
    "Saudi Arabia", "United Arab Emirates", "Germany", "France", 
    "India", "Singapore", "Worldwide", "Other"
]
ws.data_validation(start_row, 3, max_row_idx, 3, {
    "validate": "list",
    "source": countries_list,
    "input_title": "Select Country",
    "input_message": "Choose from standard countries or type custom."
})

# Dropdown: Contact Channel (Column F -> col 5)
channels_list = [
    "WhatsApp", "Direct Email", "LinkedIn", "Upwork Chat", 
    "Phone / Call", "Website Form", "Other"
]
ws.data_validation(start_row, 5, max_row_idx, 5, {
    "validate": "list",
    "source": channels_list,
    "input_title": "Select Channel",
    "input_message": "Choose primary contact channel."
})

# Dropdown: Lead Status (Column J -> col 9)
status_list = [
    "New Lead", "Proposal Sent", "In Discussion", 
    "Meeting Scheduled", "Hired / Won", "Follow Up Needed", "Closed / Lost"
]
ws.data_validation(start_row, 9, max_row_idx, 9, {
    "validate": "list",
    "source": status_list,
    "input_title": "Lead Status",
    "input_message": "Update status as lead progresses."
})

# Dropdown: Team Lead (Column K -> col 10)
team_list = [
    "Viranga Lakshan", "Chamara Lahiru", "Avishka Meddegoda", 
    "Janith Kavishka", "Lithumitha Ravikumar"
]
ws.data_validation(start_row, 10, max_row_idx, 10, {
    "validate": "list",
    "source": team_list,
    "input_title": "Assignee",
    "input_message": "Assign lead owner from team."
})

# ==================== CONDITIONAL FORMATTING ====================
# Color code the Lead Status column (Column J -> col 9)
for status_name, colors in status_colors.items():
    status_fmt = workbook.add_format({
        "font_name": font_family,
        "font_size": 9.5,
        "bold": True,
        "font_color": colors["fg"],
        "bg_color": colors["bg"],
        "align": "center",
        "valign": "vcenter",
        "border": 1,
        "border_color": COLOR_BORDER
    })
    ws.conditional_format(start_row, 9, max_row_idx, 9, {
        "type": "cell",
        "criteria": "equal to",
        "value": f'"{status_name}"',
        "format": status_fmt
    })

# Add autofilter across the entire table range
ws.autofilter(5, 0, max_row_idx, len(headers) - 1)

workbook.close()
print(f"Generated Excel workbook at: {file_path}")

# Copy to Downloads root directory as well for easy 1-click access
downloads_file_path = os.path.join(downloads_dir, file_name)
try:
    shutil.copyfile(file_path, downloads_file_path)
    print(f"Copied Excel workbook to: {downloads_file_path}")
except Exception as e:
    print(f"Copy note: {e}")
