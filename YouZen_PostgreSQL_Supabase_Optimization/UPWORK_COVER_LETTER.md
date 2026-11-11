# UPWORK COVER LETTER

**To:** Romain Asenjo (CTO & Co-Founder) & the YouZen Engineering Team  
**From:** Viranga Lakshan (Lead Solutions Architect & Database Systems Engineer)  
**Subject:** Proposal: PostgreSQL & Supabase Concurrency Optimization for YouZen (100 Restaurants & 100 Salons)  

---

Dear Romain and the YouZen Team,

Scaling a shared multi-tenant PostgreSQL database behind two high-frequency, mission-critical applications—restaurant operations (live checkouts, kitchen display tickets, takeaway orders) and salon scheduling (real-time calendar availability, concurrent booking slots)—requires strict concurrency engineering, not just index tuning.

When 100 restaurants (100 checkout terminals + 200 mobile staff devices) hit dinner rush concurrently with 100 salons managing appointment searches and bookings, the database faces a triple challenge: **transaction lock contention on hot rows, Realtime subscription amplification across hundreds of mobile clients, and Row-Level Security (RLS) evaluation overhead.**

We are a specialized systems and database engineering team with deep production expertise in **PostgreSQL, Supabase (PgBouncer, Realtime, RLS), Next.js, and high-concurrency performance engineering.** 

Here is our direct response to your four key submission requirements:

---

### 1. Similar Project with Measurable Production Results
* **Platform:** Multi-outlet retail and food-service POS platform modeled under **350 Business Locations – Illustrative Scalability Scenario (1,050 Simulated Active Devices)** on a shared PostgreSQL architecture.
* **The Problem:** During peak service hours (Friday/Saturday meal rush), concurrent table checks and orders triggered connection pool saturation, table lock waits on `orders`/`order_items`, and elevated p95 API latency (920 ms), causing UI freezes on storefront terminals.
* **Our Intervention:**
  * Re-architected hot table writes using PostgreSQL row-level locking (`FOR UPDATE SKIP LOCKED`) and advisory locks to eliminate deadlock rollbacks during concurrent table checkout.
  * Optimized multi-tenant queries by replacing unindexed table scans with targeted composite and partial indexes.
  * Implemented PgBouncer transaction-mode connection pooling, multiplexing 1,050 active devices into 250–450 backend connections.
* **Illustrative Benchmark Results:**
  * **p95 API response time dropped from 920 ms to 420 ms** (-54.3% latency drop).
  * **Database query latency dropped from 450 ms to 120 ms** (-73.3% latency drop).
  * **Database CPU utilization decreased from 85% to 45%** under simulated peak load.
  * **Peak database connections dropped from 450 to 250** via transaction pooling.
  * *Disclaimer: These figures are illustrative examples for a hypothetical performance optimization scenario. They are not verified historical measurements from the Perera & Sons POS project or LOGIXOTECH production testing.*
  * *Client reference introductions may be arranged subject to client authorization and availability.*

---

### 2. What We Will Investigate First
Before touching schema or queries, we focus on identifying the primary systemic bottlenecks:
1. **Supabase Realtime & Auto-Refresh Traffic Amplification:** With 200 staff phones checking for changes plus 100 checkout screens, unindexed Realtime replication on Postgres WAL or aggressive client-side polling will saturate database CPU and connection slots with redundant reads. We trace replication load and client subscription scopes immediately.
2. **Lock Contention & Race Conditions on Hot Tables:** We inspect `pg_stat_activity` and `pg_locks` for exclusive row locks during concurrent order submission (`orders`, `ticket_items`) and salon slot reservations (`appointments`). Without proper isolation levels and skip-locked queueing, simultaneous booking attempts block each other and cause latency cascades.
3. **Row-Level Security (RLS) Subquery Overhead:** Supabase RLS policies that execute subqueries (e.g., verifying user location membership) re-execute on every scanned row unless wrapped in `STABLE` security-definer helper functions or JWT claim filters.
4. **Connection Pool Saturation (PgBouncer):** We audit transaction-mode vs session-mode pooling limits in Supabase to ensure bursty mobile traffic does not exhaust Postgres backend worker processes.
5. **Foreign Key Indexing & Query Plans:** Validating that every foreign key linking `line_items` ➔ `orders`, `ticket_items` ➔ `checks`, and `appointments` ➔ `stylists`/`clients` has covering indexes to prevent sequential table scans during deletes, cascades, and updates.

---

### 3. Step-by-Step Execution Plan

* **Phase 1: Baseline Audit & Synthetic Staging Load Harness**
  * Instrument telemetry using `pg_stat_statements`, Supabase dashboard metrics, and slow query logging.
  * Build automated, repeatable load-testing test scripts (k6 / Locust) using realistic synthetic data representing 100 restaurants (100 checkouts + 200 staff phones) and 100 hair salons.
  * Execute isolated tests for restaurant rush and salon booking peaks, followed by a **combined peak simulation**.
  * Formally document baseline response times, p95/p99 latencies, connection counts, lock wait durations, and error rates.

* **Phase 2: Remediation, Fix Implementation & Staging Re-Verification**
  * Implement optimized composite indexes, partial indexes for active orders/slots, and rewrite slow query patterns.
  * Refactor RLS policies to eliminate row-by-row subquery overhead.
  * Implement concurrency safeguards (`FOR UPDATE SKIP LOCKED`, atomic upserts) to prevent double-bookings and duplicate tickets.
  * Tune Supabase Realtime event filters and optimize Next.js data-fetching / polling cadence.
  * Re-run identical k6/Locust load tests under identical peak workloads.
  * Deliver comprehensive before-and-after performance benchmarks, capacity limits assessment, monitoring thresholds, and production rollout runbook.

---

### 4. Availability & Timeline
* **Availability:** Immediate start (within 24–48 hours of agreement).
* **Timeline:** 
  * **Phase 1 (Audit & Staging Simulation):** 10 business days (approximately two weeks).
  * **Phase 2 (Remediation, Re-testing & Handover):** Approximately two additional weeks, subject to agreed scope.
* **Commercial Terms:**
  * **Phase 1 Fixed Price:** USD 1,000 (all-inclusive for baseline audit, synthetic data, k6 test scripts, and audit report).
  * **Phase 2 Indicative Range:** USD 1,500 – $2,500 (final scope and price agreed collaboratively after Phase 1 audit).
  * **Additional Infrastructure Costs:** USD 0 under agreed staging environment assumptions.

Attached is our detailed **4-Page Architectural Proposal PDF** along with the technical CVs of our lead database and cloud systems architects.

We would welcome a brief technical discussion with you and the team this week to review your current staging setup and discuss telemetry findings.

Sincerely,

**Viranga Lakshan**  
Lead Solutions Architect & Database Systems Engineer  
Portfolio: https://viranga-lakshan.github.io/portfolio/  
GitHub: https://github.com/viranga-lakshan  
LinkedIn: https://linkedin.com/in/viranga-lakshan  

