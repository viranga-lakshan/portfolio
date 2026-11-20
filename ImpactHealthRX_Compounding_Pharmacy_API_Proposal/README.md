# Impact Health RX — Compounding Pharmacy API Integration Proposal Package

**Project:** Compounding Pharmacy API Expert | Connect 20+ Pharmacies to Impact Health RX  
**Client Budget:** $5,000.00 Fixed-Price (Agreed & Accepted) & Contract-to-Hire  
**Platform Reference:** [https://impacthealthrx.com](https://impacthealthrx.com)  
**Competitor Benchmarks:** Breakthrough Pharmacy Partners, OnlyScripts, VITL, Impetus One  
**Agency:** Axiom Global  
**Technical Lead:** Avishka Meddegoda (Senior Full-Stack & System Architect, 6+ Years Exp)  
**Delivery Lead & Solutions Architect:** Viranga Lakshan (`virangalakshanz@gmail.com` | `+94 71 378 1359` | `https://axiomglobal.tech`)  

---

## 📁 Package Directory Manifest

```
ImpactHealthRX_Compounding_Pharmacy_API_Proposal/
│
├── ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf  # 12-Page Executive Client Proposal & Blueprint PDF
├── UPWORK_PROPOSAL_COVER_LETTER.md                   # Complete copy-paste cover letter answering all 7 questions
├── UPWORK_DIRECT_CLIENT_MESSAGE.md                   # Direct client communication & Q&A messaging format
├── proposal_template.html                            # Compiled high-resolution HTML template used for PDF generation
├── create_impacthealthrx_proposal_pdf.py             # Automated Python script using Playwright & PyPDF
├── README.md                                         # This documentation file
└── images/                                           # Curated imagery & agency assets
    ├── cover_healthcare.jpg
    ├── medication_tech.jpg
    ├── marketplace_tech.jpg
    ├── cloud_infra.jpg
    ├── team_office.jpg
    └── axiom_logo.png
```

---

## 💎 Key Scope & Technical Architecture

1. **Mandatory Qualification:**
   * Starts with: *"I have personally integrated compounding pharmacy APIs."*
   * Verifiable integrations: **Empower Pharmacy (503A/503B), Hallandale Pharmacy, Red Rock Pharmacy, Tailor Made Compounding, and Belmar Pharma Solutions**.
2. **Universal Pharmacy Adapter (Hexagonal Architecture):**
   * Single canonical `PharmacyIntegrationPort` interface normalizing disparate REST, JSON-RPC, and SFTP endpoints.
   * Enables rapid onboarding of 20+ compounding pharmacies (2–4 days per pharmacy) without breaking core business logic.
3. **Dual Clinical Prescribing Workflows:**
   * **Workflow 1 (Clinic Own Prescribers):** Direct order routing with `Total = Wholesale Cost + Configurable Markup + Shipping`.
   * **Workflow 2 (50-State Provider Network):** Asynchronous clinical queue, state-based provider routing, chart review, e-sign, and strictly isolated **$60 provider consultation fee**.
4. **Formulary Harmonization & Licensure Engine:**
   * Non-interchangeable formulation mapping (Base vs. Salt forms, Semaglutide Base vs. Sodium, Tirzepatide, concentrations, vial sizes).
   * Real-time state licensure filtering ensuring clinics only see pharmacies authorized to ship to the patient's state.
5. **Mission-Critical Reliability:**
   * **Idempotency Keys** preventing duplicate orders and double-billing.
   * **Transactional Outbox Pattern** with RabbitMQ/SQS and Dead Letter Queues (DLQ) for zero dropped orders during pharmacy outages.
   * **Dual-Channel Tracking:** Webhooks + cron poller fallback binding directly to FedEx/UPS/USPS tracking APIs.
6. **Milestone Investment ($5,000 USD Fixed Price):**
   * Milestone 1 (25% — $1,250): Codebase Audit, DB Normalization & Architecture Blueprint (Days 1–5).
   * Milestone 2 (25% — $1,250): Universal Adapter Core & 1st Working Pharmacy Sandbox Integration (Days 6–12).
   * Milestone 3 (30% — $1,500): Dual Workflows, $60 Consult Fee Engine, Pricing Ledger & First 3 Live Pharmacies (Weeks 3–4).
   * Milestone 4 (20% — $1,000): Carrier Tracking, Admin Exception Dashboard, Deployment & Handover for 20+ Scale (Weeks 5–6).

---

## 🚀 How to Re-compile the Proposal PDF

```powershell
python "create_impacthealthrx_proposal_pdf.py"
```

The script compiles headless Chromium via Playwright, renders print styles, and asserts `total_pages == 12`.
