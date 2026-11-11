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

* **Delivery Timeline:** **10 business days (approximately two weeks)** from repository and staging database access.
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
* **Estimated Delivery Timeline:** **Approximately two additional weeks**, subject to the agreed scope.
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

## 5. Technical Case Study Reference & Client Reference

Attached to this quotation is our complete **9-page enterprise technical report**:  
📄 `LOGIXOTECH_Multi_Outlet_POS_Performance_Scalability_Report.pdf`

* **Platform Context:** 350 Business Locations – Illustrative Scalability Scenario (1,050 Simulated Active Devices) on a centralized database cluster.
* **Illustrative Benchmark Results:**
  * API response time (p95): **920 ms to 420 ms** (-54.3% latency drop).
  * Database query response time: **450 ms to 120 ms** (-73.3% latency drop).
  * Database CPU utilization: **85% to 45%** (-47.1% load reduction).
  * Failed request rate: **5.0% to 0.5%** (-90.0% error reduction).
  * Peak database connections: **450 to 250** (-44.4% pool efficiency).
  * Transaction processing error rate: **2.0% to 0.2%** (-90.0% reliability gain).

> **Disclaimer:** These figures are illustrative examples for a hypothetical performance optimization scenario. They are not verified historical measurements from the Perera & Sons POS project or LOGIXOTECH production testing.

* **Client Reference Protocol:**
  * **Client reference introductions may be arranged subject to client authorization and availability.** Verification discussions cover the nature and scope of the engagement, LOGIXOTECH's involvement, team responsibilities performed, scale supported, and optimization activities undertaken.

