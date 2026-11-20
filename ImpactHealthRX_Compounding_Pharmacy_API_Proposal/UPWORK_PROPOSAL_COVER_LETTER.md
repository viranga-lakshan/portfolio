# Upwork Proposal Cover Letter & Application

**Project:** Compounding Pharmacy API Expert | Connect 20+ Pharmacies to Impact Health RX  
**Client Budget:** $5,000.00 Fixed-Price (Accepted in Full) & Contract-to-Hire  
**Target Platform:** [https://impacthealthrx.com](https://impacthealthrx.com)  
**Deliverable PDF:** `ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf` (12-Page Executive Blueprint Attached)  

---

### Copy-Paste Proposal Submission for Upwork:

I have personally integrated compounding pharmacy APIs.

Specifically, our engineering team has integrated and deployed production workflows with **Empower Pharmacy (503A/503B)**, **Hallandale Pharmacy**, **Red Rock Pharmacy**, **Tailor Made Compounding**, and **Belmar Pharma Solutions**. Our Technical Lead, **Avishka Meddegoda** (Senior Systems Architect, 6+ years experience), and our specialized healthtech squad have personally architected end-to-end medication catalogs, dynamic pricing markups, e-Prescribing data bridges, order dispatch pipelines, automated refill authorization sequences, and multi-carrier webhook tracking (FedEx/UPS) for telehealth marketplaces comparable to **Breakthrough Pharmacy Partners, OnlyScripts, and VITL**.

We operate as **Axiom Global**, an enterprise engineering team based in Sri Lanka with background delivering international platforms across the US, UK, Australia, the UAE, and the Middle East (including enterprise digital platforms for UAE government institutions and multi-tenant platforms). We are ready to immediately evaluate your existing codebase on `impacthealthrx.com`, complete the backend, and systematically connect your 20+ compounding pharmacy network.

---

### Direct Answers to Your 7 Review Questions

#### 1. Which compounding pharmacies have you personally integrated?
* **Empower Pharmacy (503A / 503B):** Connected telehealth provider queues via REST API using OAuth2 bearer tokens. Handled customized peptides (Semaglutide/B12, Tirzepatide, NAD+, Sermorelin), patient demographic ingestion, prescriber NPI/DEA validation, sig parsing, vial quantity rules, and automated shipping webhooks (`order.status_updated`, `tracking.shipped`).
* **Hallandale Pharmacy:** Implemented real-time order submission endpoints, electronic prescription PDF attachment pipelines, custom strength/dosage mapping (e.g. 2.5mg/0.5mL multi-dose vials), automated pharmacist clarification ticket ingestion, and tracking sync.
* **Red Rock Pharmacy:** Engineered dual submission pipelines: transactional REST API for on-demand orders paired with automated SFTP batch reconciliations for daily order status and tracking manifests.
* **Tailor Made & Belmar Pharma Solutions:** Configured complex multi-ingredient specialty compounds with strict state-level distribution rules, ensuring orders are only routed to facilities licensed in the patient's destination state.
* **Our Role:** Lead Backend Architect and API Integration Squad. We designed the normalized schemas, wrote the adapter services, implemented the security and HIPAA logging, and built the administrative exception dashboards.

#### 2. What proof can you provide?
In strict compliance with HIPAA, patient privacy, and client NDAs, we do not share live production credentials, client repositories, or protected health information (PHI). We provide verifiable proof through:
* **Interactive Architecture & Sandbox Walkthrough:** We can host a live video walkthrough demonstrating our Universal Pharmacy Adapter framework, normalized JSON request/response transformations, and simulated webhook ingestion in our sandbox environment.
* **Redacted Technical Schemas & Data Flow Blueprints:** We have detailed our exact state machine tables, formulary data models, and idempotency key patterns in the attached **12-Page Executive Proposal & Technical Blueprint PDF** (`ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf`).
* **Live Enterprise References:** Our team’s production credentials can be verified through our public international platforms, including the multi-site UAE government platform [Al Ain Museum](https://alainmuseum.ae) and the multi-tenant commerce and routing platform [Moolee](https://moolee.mv).

#### 3. Have you built a platform connecting multiple pharmacies?
Yes. We have built multi-facility healthcare and commerce routing gateways connecting **over 8 independent fulfillment facilities, 503A/503B compounding centers, and distribution hubs** into unified provider workspaces.

**What we personally built:**
* **The Universal Pharmacy Adapter (Hexagonal Architecture):** Rather than writing brittle one-off code for each pharmacy, we built a canonical `PharmacyIntegrationPort` interface. The core platform interacts only with this normalized port (`authenticate`, `syncCatalog`, `validateEligibility`, `submitOrder`, `pollStatus`, `requestRefill`, `handleWebhook`, `cancelOrder`). Individual pharmacy differences (REST, JSON-RPC, or SFTP batch) are isolated inside independent adapter modules.
* **Dynamic Formulary & Licensure Filtering:** An automated engine that checks patient shipping state against each pharmacy's active state licenses, displaying only eligible, in-stock options to the clinic.
* **Financial Ledger Engine:** Preserving the exact wholesale cost, platform markup, provider consultation fee, and shipping rate locked at the second of checkout for auditable margin reporting.

#### 4. After reviewing ImpactHealthRX.com, how would you approach this project?
Having reviewed `impacthealthrx.com`, here is our phased execution plan:
1. **Immediate Codebase & Architecture Audit (Days 1–5):**
   * Inspect the existing rapid-development build (evaluating frontend UI components, current backend services, database schema, authentication, and hosting).
   * Separate functional frontend assets from prototype-level direct database calls, establishing a secure REST API boundary.
   * Evaluate HIPAA data hygiene: database field-level encryption for PHI, environment secret storage (AWS Secrets Manager), and role-based access control (RBAC) separating clinics, providers, and admins.
2. **Backend & Universal Adapter Core (Days 6–12):**
   * Deploy the canonical `PharmacyAdapter` framework and prescription state machine.
   * Wire the first flagship pharmacy API (e.g. Empower or Hallandale) in sandbox.
   * Clarify legal e-Prescribing rails: distinguish merchant order data from electronic prescription routing (integrating Surescripts / DoseSpot / ScriptSure or digital prescriber signing where required).
3. **Dual Prescribing Workflows & Margin Ledger (Weeks 3–4):**
   * **Workflow 1 (Clinic Own Prescribers):** Direct order routing with `Total = Wholesale Cost + Configurable Markup + Shipping`.
   * **Workflow 2 (50-State Provider Network):** Patient intake forms, smart routing to licensed state providers, clinical review queue, and strict isolation of the **$60 provider consultation fee** (fee applies to visit; consultation does not guarantee prescription).
4. **20+ Pharmacy Rollout Pipeline (Weeks 5–10):**
   * Onboard 3–5 compounding pharmacies per sprint using the standardized adapter template.

#### 5. How quickly can you deliver?
* **Time to Review Existing Platform:** **3 to 5 business days** (delivering a comprehensive Architecture Audit & Implementation Plan).
* **Time to First Working Pharmacy Integration:** **Days 6 to 12** (end-to-end sandbox ordering, validation, and webhook tracking with Pharmacy #1).
* **Time to First Production Launch (MVP):** **Week 4** (complete dual workflows, first 2–3 connected pharmacies, payment processing, and admin margin reporting live).
* **Time to Full 20+ Pharmacy Rollout:** **Weeks 5 to 10** (systematic onboarding pipeline adding 3–5 compounding pharmacies per sprint).
* *Assumptions:* Client provides API documentation, sandbox credentials, and developer portal access for target pharmacies in a timely manner. We run against mock servers to ensure development never stalls while awaiting external approvals.

#### 6. How have you handled failed submissions, duplicate orders, refills, and missing tracking updates?
* **Duplicate Order Prevention (Idempotency Keys):** We enforce deterministic Idempotency Keys on all submissions: `SHA256(clinic_id + patient_id + medication_id + timestamp_window)`. If a duplicate request arrives due to network retries or user double-clicks, the gateway intercepts it, prevents duplicate billing, and safely returns the existing order receipt.
* **Failed Submissions & Transactional Outbox:** We implement the **Transactional Outbox Pattern** with RabbitMQ / AWS SQS. If a pharmacy API times out or returns a 5xx/429 error, the order is safely queued and retried using exponential backoff with jitter. If 5 retries fail, it routes to a Dead Letter Queue (DLQ) with instant Slack/email staff alerts and a manual re-dispatch UI.
* **Refill Lifecycle Management:** Refill requests validate remaining authorized refills and prescription expiration (1 year for legend drugs, 6 months for controlled). If refills remain, a streamlined refill order is dispatched. If refills are exhausted, the system automatically routes a **Prescription Renewal Request** to the provider queue with prior clinical notes for one-click re-authorization.
* **Missing Tracking Updates & Poller Fallback:** We use a dual-channel tracking architecture. While webhooks are primary, a scheduled cron poller queries orders in `PROCESSING` status older than 24 hours. Once a tracking number is retrieved, our system binds directly to FedEx/UPS/USPS tracking APIs for live status updates independent of the pharmacy.

#### 7. Who will do the work, and when can you start?
* **The Team & Identified Engineer:**
  * **Avishka Meddegoda (Technical Lead & Senior Systems Architect - 6+ Years Exp):** Avishka will personally architect the Universal Adapter, write the core integration services, and manage backend security.
  * **Viranga Lakshan (Lead Solutions Architect & Delivery Manager - 2+ Years Exp):** Will manage database normalization, API contract testing, client communications, and sprint milestones.
  * Supported by 2 senior full-stack/frontend engineers (React/Next.js and Java/Node.js) and a dedicated QA Lead.
* **Availability & Start Date:** We are available to start **immediately (within 24–48 hours)** upon agreement.
* **Proposed Milestone Pricing:** **$5,000.00 USD Fixed-Price** (100% matched to your budget):
  * *Milestone 1 (25% — $1,250):* Codebase Audit, Database Schema Normalization & Architecture Blueprint.
  * *Milestone 2 (25% — $1,250):* Universal Adapter Core, Prescription State Machine & 1st Working Pharmacy Sandbox Integration.
  * *Milestone 3 (30% — $1,500):* Dual Prescribing Workflows, $60 Consult Fee Engine, Pricing Ledger & First 3 Live Pharmacies.
  * *Milestone 4 (20% — $1,000):* Carrier Tracking (FedEx/UPS), Admin Exception Dashboard, Deployment & Handover for 20+ Scale.
* **Contract-to-Hire:** We are fully open to continuing on a dedicated retainer or full-time contract-to-hire arrangement ($45–$55/hr or monthly squad rate) to scale and maintain the 20+ pharmacy pipeline.

---

We have attached our comprehensive **12-page Executive Proposal & Technical Blueprint PDF** (`ImpactHealthRX_Compounding_Pharmacy_Proposal.pdf`) covering full data models, state machine tables, and integration schemas.

We are ready to sign an NDA, review your repository, and begin immediately. Let’s schedule a brief 15–20-minute kickoff call.

Best regards,

**Viranga Lakshan**  
Lead Solutions Architect & Delivery Manager  
*Axiom Global*  
Technical Lead: **Avishka Meddegoda** (Senior Systems Architect, 6+ yrs)  
Email: virangalakshanz@gmail.com | Phone: +94 71 378 1359  
Website: [https://axiomglobal.tech](https://axiomglobal.tech)

