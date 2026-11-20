# Direct Client Message & Q&A Response — Impact Health RX

**Project:** Compounding Pharmacy API Expert | Connect 20+ Pharmacies to Impact Health RX  
**Client Budget:** $5,000.00 Fixed-Price (Accepted in Full) & Contract-to-Hire  
**Technical Lead:** Avishka Meddegoda (Senior Systems Architect, 6+ Years Exp)  
**Solutions Architect & Delivery Lead:** Viranga Lakshan (Axiom Global)  
**Contact:** virangalakshanz@gmail.com | +94 71 378 1359 | [https://axiomglobal.tech](https://axiomglobal.tech)  
**Attachment:** `ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf` (12-Page Executive Blueprint)  

---

### Direct Upwork Message / Client Chat:

Hi there,

I have personally integrated compounding pharmacy APIs.

Our engineering team at **Axiom Global** has built and deployed production integrations with **Empower Pharmacy (503A/503B)**, **Hallandale Pharmacy**, **Red Rock Pharmacy**, **Tailor Made Compounding**, and **Belmar Pharma Solutions**. Our Technical Lead, **Avishka Meddegoda** (Senior Systems Architect, 6+ years experience), has personally architected medication catalog harmonization, dynamic markups, e-Prescribing workflows, order dispatch pipelines, and automated webhook tracking for healthcare platforms benchmarked against **Breakthrough Pharmacy Partners, OnlyScripts, and VITL**.

We reviewed your platform at `impacthealthrx.com`. We are ready to immediately evaluate your existing codebase, complete the backend, and systematically connect your 20+ compounding pharmacy network within your **$5,000.00 fixed-price budget**.

---

### Highlights of Our Architecture for Impact Health RX:

1. **Universal Pharmacy Adapter (Hexagonal Pattern):**
   We establish a canonical `PharmacyIntegrationPort` interface (`authenticate`, `syncCatalog`, `validateEligibility`, `submitOrder`, `pollStatus`, `requestRefill`, `handleWebhook`). This isolates individual pharmacy API differences (REST, JSON-RPC, or SFTP batch), allowing you to onboard new pharmacies in 2–4 days without touching core business logic.

2. **Dual Prescribing Workflows & Ledger:**
   * **Workflow 1 (Clinic Own Prescribers):** Validates prescriber licensure state against patient state, calculates wholesale + configurable platform markup, and dispatches directly to the selected pharmacy.
   * **Workflow 2 (50-State Provider Network):** Manages patient intake questionnaires, smart routes to licensed state providers, queues clinical chart reviews, and cleanly isolates the **$60 provider consultation fee** (fee applies to visit; consultation does not guarantee prescription).
   * **Financial Immutability:** Prices, wholesale costs, markups, consult fees, and shipping rates are locked at the second of checkout, ensuring accurate historical reporting and margin reconciliation.

3. **Mission-Critical Reliability & Error Handling:**
   * **Duplicate Prevention:** Enforces deterministic **Idempotency Keys** (`SHA256(clinic_id + patient_id + medication_id + timestamp)`) preventing double-billing or twin order injections.
   * **Outbox Pattern & DLQ:** Implements transactional queues with exponential backoff retries and Dead Letter Queue (DLQ) alerts for pharmacy API downtime or 5xx/429 errors.
   * **Refills & Tracking:** Manages refill countdowns and auto-routes expired prescriptions to the provider queue for renewal re-authorization. Dual-channel tracking binds directly to FedEx/UPS/USPS carrier webhooks.

4. **Rapid Timeline & Phased Delivery:**
   * **Days 1–5:** Codebase & Architecture Audit of `impacthealthrx.com` + normalized database schemas.
   * **Days 6–12:** 1st working pharmacy integration in sandbox (end-to-end ordering & status receipt).
   * **Week 4:** Production launch of MVP with top 2–3 connected pharmacies and dual workflows live.
   * **Weeks 5–10:** Industrialized rollout pipeline onboarding 3–5 compounding pharmacies per sprint.

5. **Team & Terms:**
   * Led directly by **Avishka Meddegoda** (Technical Lead) and **Viranga Lakshan** (Delivery Lead).
   * Available to start **immediately (within 24–48 hours)**.
   * Fully open to the **Contract-to-Hire** model for long-term network expansion.

We have attached our comprehensive **12-page Executive Proposal & Technical Blueprint PDF** (`ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf`) covering full database models, state machine tables, and integration code samples.

We are ready to sign an NDA, review your codebase, and begin Sprint 1 immediately. Let's schedule an introductory 15–20 minute kickoff discussion.

Warm regards,

**Viranga Lakshan**  
Lead Solutions Architect & Delivery Manager  
*Axiom Global*  
Technical Lead: **Avishka Meddegoda** (Senior Systems Architect, 6+ yrs)  
Email: virangalakshanz@gmail.com | Phone: +94 71 378 1359  
Website: [https://axiomglobal.tech](https://axiomglobal.tech)

