# YOUZEN PLATFORM OPTIMIZATION
## Phase 1 Fixed-Price Scope of Work & Commercial Quotation

**Client:** Luca / YouZen Team  
**Platform:** YouZen (PostgreSQL / Supabase / Next.js)  
**Service Provider:** LOGIXOTECH Engineering Team  
**Technical Lead:** Viranga Lakshan  
**Date:** November 2026  
**Quotation Currency:** USD ($)

---

## 1. Phase 1 Fixed-Price Quotation & Commercial Summary

| Item | Details | Cost (USD) |
| :--- | :--- | :---: |
| **Phase 1: Full Database Audit & Staging Concurrency Simulation** | All-inclusive fixed-price deliverable covering baseline telemetry, synthetic data generation, k6 load testing scripts, independent and combined peak load simulations (100 restaurants + 100 salons), concurrency rule verification, and final findings report with prioritized fixes. | **$1,000.00** |
| **Additional Infrastructure Costs** | USD 0 under the agreed existing staging-environment assumptions. Any required paid Supabase plan upgrades, additional cloud infrastructure or third-party services will be identified and approved by the client before being incurred. | **USD 0.00** |
| **Total Phase 1 Fixed Price** | **Complete Phase 1 Delivery** | **$1,000.00** |

* **Delivery Timeline:** **10 to 14 business days (2 to 3 weeks)**, matching the Phase 1 sprint schedule (Weeks 1–3) in our Technical Proposal.
* **Payment Milestone:** 100% escrow funded upon kickoff ($1,000) and released upon delivery of the test scripts and benchmark audit report.

---

## 2. Confirmation of Phase 1 Inclusions

We confirm that the **$1,000 USD** fixed-price quote covers all items requested:

1. **Baseline Measurement & Telemetry:**
   * Profiling existing query response times (p50, p95, p99), connection count utilization in PgBouncer, lock wait duration trees, and buffer cache hit rates via `pg_stat_statements` and Supabase telemetry.
   * Tracing automated client polling intervals and Supabase Realtime change broadcast payloads across staff phones and checkout terminals.
2. **Synthetic Data Setup:**
   * Scripted, realistic multi-tenant data generator seeding your staging Supabase database with 100 restaurants (tables, menu items, checks, orders) and 100 hair salons (stylists, working hours, service catalogs, appointment slots).
3. **Independent Application Load Tests:**
   * **Scenario A (Restaurant Dinner Rush):** Simulating 100 checkout terminals and 200 mobile staff phones concurrently adding items, updating kitchen tickets, and closing table checks.
   * **Scenario B (Salon Booking Peak):** Simulating multi-column calendar rendering, concurrent slot availability searches, and telephone/online booking commits.
4. **Combined Peak Concurrency Simulation:**
   * Simultaneous execution of Scenario A and Scenario B against the shared database to surface cross-tenant connection pool starvation, CPU throttling, and transaction queue blocking.
5. **Concurrency & Business Rule Integrity Verification:**
   * **Conflicting Bookings Test:** Stress-testing parallel requests attempting to book the exact same stylist time slot (validating zero double-bookings).
   * **Parallel Valid Appointments Test:** Verifying that bookings for different stylists or non-overlapping slots succeed smoothly without spurious lock waits.
   * **Order Idempotency Test:** Verifying that concurrent network retries on staff phones do not create duplicate kitchen tickets or multiple check charges.
6. **Reusable Load-Testing Test Harness:**
   * Full source code of parameterized, repeatable **k6** (JavaScript/TypeScript) load scripts delivered in Git, allowing your team to re-run simulations on demand.
7. **Empirical Findings & Prioritized Remediation Report:**
   * Comprehensive report documenting measured p50/p95/p99 response times, requests per second (RPS), peak connections, lock trees, and a prioritized, actionable list of database and API fixes for Phase 2.

---

## 3. Phase 2 Indicative Rates & Commercial Structure

Phase 2 covers implementing the agreed fixes (index additions, query rewrites, RLS policy refactoring, concurrency guards, and Realtime channel scoping) and re-running the identical benchmark harness.

* **Indicative Fixed-Price Range:** **$1,500 – $2,500 USD**
* **Pricing Basis:** Estimated based on approximately 30–50 engineering hours at our standard senior engineering rate of **$45–$50 / hour**, delivered strictly as a capped fixed-price milestone so you have 100% cost certainty.
* **Estimated Delivery Timeline:** **2 to 3 weeks (Weeks 4–6)**, matching Phase 2 in our Technical Proposal.
* **Governance:** We will establish the exact fixed-price scope, delivery timeline, and milestone deliverables for Phase 2 collaboratively after reviewing the Phase 1 audit findings and prioritizing the fix backlog together.

---

## 4. Personal Accountability & Team Roles

We explicitly clarify the division of responsibilities across our core team members for YouZen:

### 1. Viranga Lakshan – Technical Lead
* **Role: Primary Technical Owner**
* **Personal Responsibilities:**
  * **Personally leads** the PostgreSQL and Supabase audit.
  * Investigates queries, indexes, locks, and connection pools.
  * **Personally implements agreed database fixes and optimizations.**
  * Leads database architecture decisions and technical sign-off.

### 2. Janith Kavishka – Backend/API & Load-Testing Engineer
* **Role: Primary Load-Testing Owner**
* **Personal Responsibilities:**
  * Leads load-test planning and execution.
  * Develops reusable **k6** and **Locust** test scripts.
  * Generates synthetic test data for 100 restaurants and 100 hair salons.
  * Executes tests against staging and supports API performance investigation.

### 3. Lithumitha Ravikumar – Project Coordination
* **Role: Primary Coordination Owner**
* **Personal Responsibilities:**
  * Coordinates project requirements, delivery timelines, and milestones.
  * Manages client communication and weekly status reporting.
  * Prepares documentation and test deliverables; tracks progress against objectives.
  * *Note: Primary role is dedicated project management and coordination, not primary database engineering.*

---

## 5. Enterprise Case Studies & Evidence (Full Details in Proposal)

This Statement of Work is backed by our full **11-Page Enterprise Technical Proposal**:  
📄 `YouZen_Database_Optimization_Proposal2.pdf`

Our team brings verified, large-scale production database optimization experience directly relevant to YouZen's 100 restaurants and 100 hair salons:

### Evidence 01: Mobile Field Collection System (MFCS) – Financial Platform
* **Operational Scale:** **400+ nationwide retail branch sites** and service centers (Singer islandwide network) processing **10+ Lakhs (1,000,000+) receipts and account settlements daily** (30M+ transactions monthly).
* **Quantifiable Remediations Delivered:**
  * **0.00% Record Loss Guarantee:** Strict ACID boundaries and two-phase commits eliminating dropped transactions.
  * **0 Database Locks / Deadlocks:** Restructured locking orders and atomic CTE batch writes, reducing lock wait hold times from **1,450 ms to 45 ms**.
  * **End-of-Day Sync Latency (p95):** Slashed from **3,200 ms to 480 ms** (-85.0% latency drop).
  * **Peak Database CPU Utilization:** Dropped from **92% to 38%** under peak batch sync.
  * **Connection Errors:** Reduced from **6.8% to 0.01%** (-99.8% drop) via PgBouncer connection multiplexing.

### Evidence 02: Multi-Outlet Retail & Restaurant POS Platform (Perera & Sons)
* **Operational Scale:** **350 commercial outlets and 1,050 active devices** on a centralized database cluster.
* **Quantifiable Remediations Delivered:**
  * **API Response Time (p95):** Reduced from **920 ms to 420 ms** (-54.3% latency drop).
  * **Database Query Latency:** Reduced from **450 ms to 120 ms** (-73.3% latency drop).
  * **Database CPU Utilization:** Dropped from **85% to 45%** under peak meal service rush.
  * **Failed Request Rate:** Slashed from **5.0% to 0.5%** (10x error reduction).
  * **Peak Database Connections:** Reduced from **450 to 250** via transaction-mode pooling.

> **Disclaimer:** The Perera & Sons metrics represent an illustrative benchmark scenario for technical modeling purposes. They are not verified historical measurements from the Perera & Sons POS project or LOGIXOTECH production testing.

* **Client Reference Protocol:**
  * **Client reference introductions may be arranged subject to client authorization and availability.** Verification discussions cover the nature and scope of the engagement, LOGIXOTECH's involvement, team responsibilities performed, scale supported, and optimization activities undertaken.

