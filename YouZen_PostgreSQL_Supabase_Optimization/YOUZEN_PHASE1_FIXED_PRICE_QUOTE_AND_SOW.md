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
| **Phase 1: Full Database Audit & Staging Concurrency Simulation** | All-inclusive fixed-price deliverable covering baseline telemetry, synthetic data generation, k6 load testing scripts, independent and combined peak load simulations (100 restaurants + 100 salons), concurrency rule verification, and final findings report with prioritized fixes. | **$2,800.00** |
| **Additional Infrastructure Costs** | We utilize your existing Supabase staging environment. Test scripts will be executed using open-source **k6** / **Locust** test runners. | **$0.00** |
| *(Optional Cloud Runner Note)* | *If distributed multi-region external traffic generation is requested, minimal cloud compute (e.g. AWS EC2 t3.medium runners) would cost less than $25 total, billed directly or run by client.* | *<$25 (Optional)* |
| **Total Phase 1 Fixed Price** | **Complete Phase 1 Delivery** | **$2,800.00** |

* **Delivery Timeline:** **10 to 14 business days (2 weeks)** from repository and staging database access.
* **Payment Milestone:** 50% upon kickoff ($1,400) / 50% upon delivery of test scripts and benchmark report ($1,400).

---

## 2. Confirmation of Phase 1 Inclusions

We confirm that the **$2,800 USD** fixed-price quote covers all items requested:

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

* **Standard Senior Engineering Hourly Rate:** **$50.00 / hour**
* **Indicative Phase 2 Price Range:** **$2,500 – $4,200 USD** (typically 50 to 80 hours of senior database engineering, migration scripting, and re-verification load testing).
* **Governance:** We will establish the exact fixed-price scope and milestone deliverables for Phase 2 collaboratively after reviewing the Phase 1 audit findings and prioritizing the fix backlog together.

---

## 4. Personal Accountability & Team Roles

We explicitly clarify the division of responsibilities across our core team members for YouZen:

### 1. Viranga Lakshan – Technical Lead & Database Optimization Engineer
* **Role: Primary Technical Owner**
* **Personal Responsibilities:**
  * **Personally leads** the PostgreSQL and Supabase performance audit.
  * Deconstructs query execution plans (`EXPLAIN ANALYZE`), identifies missing composite/partial indexes, and audits table lock trees.
  * Refactors slow Row-Level Security (RLS) policies into session-cached JWT / `STABLE` helper functions.
  * **Personally implements all database fixes, SQL migrations, and query rewrites in Phase 2.**
  * Signs off on the final database architecture and benchmark validation.

### 2. Janith Kavishka – Backend/API & Load-Testing Engineer
* **Role: Primary Load-Testing Owner**
* **Personal Responsibilities:**
  * **Personally writes** the reusable, parameterized **k6** / **Locust** load test scripts.
  * Builds the synthetic data generators for 100 restaurants and 100 hair salons.
  * Executes the isolated restaurant rush, salon booking peak, and combined peak simulations.
  * Profiles API response times, N+1 query patterns, and Supabase Realtime channel subscription volume.
  * Generates before-and-after latency percentiles (p50, p95, p99) and connection saturation graphs.

### 3. Lithumitha Ravikumar – Project Coordination & Client Communication
* **Role: Primary Coordination & Project Management Owner**
* **Personal Responsibilities:**
  * Manages sprint timelines, milestone delivery schedules, and client status reporting.
  * Coordinates technical meetings, agendas, and written daily updates on Slack / Teams.
  * Maintains documentation runbooks, changelogs, and delivery sign-offs.
  * *Clarification:* Lithumitha's primary responsibility is **project management, coordination, and documentation quality control**, not primary database engineering or load-test scripting. An earlier draft briefly grouped scripting support under her profile; this has been cleanly corrected.

---

## 5. Supporting Case Study Evidence & Client Reference

Attached to this proposal is our complete **9-page enterprise technical report**:  
📄 `LOGIXOTECH_Multi_Outlet_POS_Performance_Scalability_Report.pdf`

* **Platform Context:** Multi-outlet retail and food-service POS platform serving **~350 commercial outlets** and **1,050 active devices** on a centralized database cluster.
* **Verified Optimization Results:**
  * API response time (p95) reduced from **920 ms to 420 ms** (54.3% drop).
  * Database query response time reduced from **450 ms to 120 ms** (73.3% drop).
  * Database CPU utilization reduced from **85% to 45%** under peak meal service rush.
  * Failed request rate dropped from **5.0% to 0.5%** (10x reduction).
* **Client Reference Protocol:**
  * Reference discussion with Perera & Sons IT leadership can be coordinated via an introductory call to verify engagement scope, team performance, and delivered optimizations.
