# GroundWell Sound & Wellness Center — Upwork Proposal & Technical Blueprint Package

**Project:** Wix Website Build from Existing Mockup with CMS & Acuity Scheduling  
**Client Budget:** $2,000.00 Fixed-Price (Agreed & Accepted)  
**Interactive Mockup Reference:** [tinyurl.com/groundwellcentersite](https://tinyurl.com/groundwellcentersite)  
**Agency:** Axiom Global  
**Technical Lead:** Avishka Meddegoda (Senior Full-Stack & System Architect, 6+ Years Exp)  
**Delivery Lead & Solutions Architect:** Viranga Lakshan (`virangalakshanz@gmail.com` | `+94 71 378 1359` | `https://axiomglobal.tech`)  

---

## 📁 Package Directory Manifest

```
GroundWell_Sound_Wellness_Wix_Acuity_Proposal/
│
├── GroundWell_Sound_Wellness_Wix_Acuity_Proposal.pdf  # 14-Page Executive Client Proposal & Blueprint PDF
├── UPWORK_PROPOSAL_COVER_LETTER.md                   # Complete copy-paste cover letter for Upwork proposal box
├── UPWORK_DIRECT_CLIENT_MESSAGE.md                   # Direct client communication & Q&A messaging format
├── proposal_template.html                            # Compiled high-resolution HTML template used for PDF generation
├── create_groundwell_proposal_pdf.py                 # Automated Python script using Playwright & PyPDF
├── README.md                                         # This documentation file
└── images/                                           # Curated imagery & agency assets
    ├── sound_bowls_hero.jpg
    ├── wellness_sanctuary.jpg
    ├── reiki_meditation.jpg
    ├── tuning_forks_sound.jpg
    ├── acuity_booking_flow.jpg
    ├── community_sound_bath.jpg
    ├── axiom_logo.png
    └── team_office.jpg
```

---

## 💎 Key Scope & Technical Architecture

1. **14 Core Website Pages + 1 Booking Hub:**
   * Home, Sound, Reiki, Tuning Forks, Somatics, Drumming, Mentorship, Classes & Events, Individual Sessions (Dedicated Acuity Booking Hub), Certifications & Training, About, Contact & Visit, Sound Instruments, Gift Certificates.
2. **2 Shared Wix CMS Dynamic Templates (Populated with ~17 initial entries):**
   * `Offerings_Events` (~13 entries: Classes, workshops, sound baths, mentorship)
   * `Offerings_Certifications` (~4 entries: Multi-day certifications & training)
   * Chronological filtering (`Date >= Today`), category filtering across modality pages, and home page feature flags.
3. **Acuity Scheduling Engine with Room Conflict Prevention:**
   * Multi-practitioner calendar integration.
   * Acuity **Rooms & Resources** lock engine to prevent double-booking shared physical treatment suites.
   * Digital intake forms and liability waivers.
   * Integrated payments via Stripe/PayPal with promo coupon support.
   * Built-in gift certificate purchase & redemption flows.
4. **Mobile Optimization:**
   * High-performance mobile navigation drawer.
   * Context-preserving group booking lightboxes/overlays to eliminate mobile iFrame clipping and scroll trapping.
5. **Interactive Enhancements:**
   * Custom minimalist sound sample player for singing bowls & tuning forks.
   * Compact practitioner biography cards with "Read More / Read Less" expandable toggles.
   * 3 reusable modal lightboxes (Booking, FAQs/Policies, Terms & Privacy).
   * Instagram visual grid & newsletter subscription hook.
6. **SEO & Handover:**
   * Local business schema (`HealthAndBeautyBusiness`), canonical tags, Open Graph meta.
   * Custom recorded Loom video training session for client autonomy.
   * 30 days of post-launch warranty support.

---

## 💳 Verified 2026 Platform Subscriptions

* **Wix Core Plan:** **$29 / month** (billed annually at $348/year) or $36 / month (monthly).
* **Acuity Scheduling Standard Plan (formerly Growing):** **$27 / month** (billed annually at $324/year) or $34 / month (monthly).
  * *Note:* The Standard plan is strictly required for GroundWell because it provides **up to 6 calendars**, enabling multi-practitioner scheduling and room conflict locks via Acuity's Rooms & Resources feature, as well as gift certificate sales and SMS text reminders.

---

## 🚀 How to Re-compile the Proposal PDF

If any modifications are made to `create_groundwell_proposal_pdf.py`, re-run the generator:

```powershell
python "create_groundwell_proposal_pdf.py"
```

The script automatically executes headless Chromium via Playwright, renders print styles, and asserts that the resulting PDF is strictly 14 pages.

