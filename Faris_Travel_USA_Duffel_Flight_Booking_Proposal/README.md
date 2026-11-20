# FARIS TRAVEL USA — Duffel Flight Booking Engine Integration Proposal Package

**Project:** Flight Booking Website Developer – Duffel API Integration & Ticketing  
**Client:** FARIS TRAVEL USA (Michigan, United States &middot; [https://faristravelusa.com](https://faristravelusa.com))  
**Budget:** $1,000.00 USD Fixed-Price (Agreed & Accepted)  
**Strict Communication Policy:** 100% Upwork Exclusive (Strictly Agreed & Confirmed)  
**Agency:** Axiom Global  
**Technical Lead:** Avishka Meddegoda (Senior Systems Architect, 6+ Years Exp)  
**Delivery Lead & Solutions Architect:** Viranga Lakshan (Axiom Global &middot; Communication exclusively via Upwork)  

---

## 📁 Package Directory Manifest

```
Faris_Travel_USA_Duffel_Flight_Booking_Proposal/
│
├── Faris_Travel_USA_Duffel_Flight_Booking_Proposal.pdf  # 10-Page Executive Client Proposal & Blueprint PDF
├── UPWORK_PROPOSAL_COVER_LETTER.md                   # Complete copy-paste cover letter answering all client questions
├── UPWORK_DIRECT_CLIENT_MESSAGE.md                   # Direct client communication on Upwork chat
├── proposal_template.html                            # Compiled high-resolution HTML template used for PDF generation
├── create_faristravel_proposal_pdf.py                # Automated Python script using Playwright & PyPDF
├── README.md                                         # This documentation file
└── images/                                           # Curated imagery & agency assets
    ├── flight_hero.jpg
    ├── travel_booking_ui.jpg
    ├── airplane_wing.jpg
    ├── airport_terminal.jpg
    ├── team_office.jpg
    └── axiom_logo.png
```

---

## 💎 Key Scope & Technical Architecture

1. **Strict Upwork Communication Compliance:**
   * Prominently confirms agreement to communicate 100% exclusively through the Upwork platform (no WhatsApp, no phone calls, no FaceTime, no personal emails, no off-platform payments).
2. **Duffel Flights API & IATA Accreditation:**
   * Leverages Duffel's IATA accreditation so Faris Travel USA can issue live airline tickets without needing separate ARC/IATA licenses or bank guarantees.
   * Generates genuine **airline PNR locator codes** and **13-digit IATA electronic ticket numbers**.
3. **Preserving Existing FarisTravelUSA.com:**
   * Embeds directly into the existing website with zero downtime, preserving current domain, logo, and branding.
4. **Customer-Facing Experience:**
   * Multi-airline search (300+ airlines), dynamic price comparison, baggage & seat selection, passenger passport details entry, and secure card payment via Stripe.
5. **Agency Back-Office Admin & Markup Engine:**
   * In-office agent booking workflow for walk-in and phone customers.
   * Administrative markup controls: flat dollar markup (e.g. +$35/ticket) or percentage markup (+5%), with profits captured directly via Stripe.
6. **Lean Third-Party Costs ($0 Monthly Subscriptions):**
   * Duffel Starter plan: $0/month (pay-as-you-go ~$3/booking).
   * Stripe US account: 2.9% + 30¢ per transaction.
7. **Milestone Investment ($1,000 USD Fixed Price):**
   * Milestone 1 (40% — $400): Duffel Setup, Search Engine Integration & Live Fares on FarisTravelUSA.com (Days 1–5).
   * Milestone 2 (40% — $400): Passenger Booking, Stripe Checkout, Agency Markup Engine & Admin Portal (Days 6–10).
   * Milestone 3 (20% — $200): Live Ticketing QA, Staff Training Session, Documentation & Launch (Days 11–15, includes 30-day warranty).

---

## 🚀 How to Re-compile the Proposal PDF

```powershell
python "create_faristravel_proposal_pdf.py"
```

The script compiles headless Chromium via Playwright, renders print styles, and asserts `total_pages == 10`.

