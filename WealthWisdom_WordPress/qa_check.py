import re
from pypdf import PdfReader

pdf_path = r"C:\Users\Viranga\Downloads\upwrok new\WealthWisdom_WordPress\WealthWisdom_Client_Portal_Proposal_Viranga_Lakshan.pdf"

reader = PdfReader(pdf_path)
print(f"Total Pages: {len(reader.pages)}")

# Extract all text
full_text = ""
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"--- PAGE {i+1} character count: {len(text)} ---")
    full_text += f"\n[PAGE {i+1}]\n" + text

# Check QA criteria
forbidden = ["$", "R ", "USD", "ZAR", "%"]
print("\n--- FORBIDDEN STRINGS CHECK ---")
for f in forbidden:
    matches = [m.start() for m in re.finditer(re.escape(f), full_text)]
    print(f"'{f}': {len(matches)} matches")
    if matches:
        for idx in matches:
            print("   Context:", full_text[max(0, idx-30):min(len(full_text), idx+30)].replace("\n", " "))

# Check for words 'hour' and 'rate' as pricing
print("\n--- WORD 'HOUR' CHECK ---")
hour_matches = re.findall(r'\b\w*hour\w*\b', full_text, re.IGNORECASE)
print("Matches:", set(hour_matches))

print("\n--- WORD 'RATE' CHECK ---")
rate_matches = re.findall(r'\b\w*rate\w*\b', full_text, re.IGNORECASE)
print("Matches:", set(rate_matches))

# Check for other forbidden entities
print("\n--- CHECK FORBIDDEN MENTIONS ---")
for bad in ["MemberPress", "Ultimate Dashboard", "WP Rocket", "Pretoria"]:
    cnt = len(re.findall(re.escape(bad), full_text, re.IGNORECASE))
    print(f"'{bad}': {cnt} matches")

