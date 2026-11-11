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
* **Platform:** Multi-tenant hospitality POS and online reservation system built on Next.js, Node.js, and Supabase / PostgreSQL.
* **The Problem:** During peak service hours (Friday/Saturday dinner rush), concurrent table checks and online orders triggered connection pool exhaustion in PgBouncer, severe table lock waits on `orders`/`ticket_items`, and elevated p95 API latency (>950ms), causing checkout freezes on floor terminals.
* **Our Intervention:**
  * Re-architected hot table writes using PostgreSQL row-level locking (`FOR UPDATE SKIP LOCKED`) and advisory locks to eliminate deadlock rollbacks during concurrent table checkout.
  * Optimized multi-tenant Row-Level Security (RLS) policies by replacing dynamic table lookups with session-cached JWT claims, reducing policy evaluation cost from `O(N)` subqueries to `O(1)` index lookups.
  * Replaced uncontrolled Supabase Realtime broadcast channels with filtered, tenant-scoped channel subscriptions and debounced client-side invalidations.
* **Measurable Results:**
  * **p95 query response time dropped from 950ms to 42ms** under peak simulated load.
  * Peak database CPU utilization decreased from **88% to 26%**.
  * Zero deadlocks or connection dropouts across 450+ concurrent POS terminals and staff mobile devices.

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
  * **Phase 1 (Audit & Staging Simulation):** 10 to 14 business days.
  * **Phase 2 (Remediation, Re-testing & Handover):** 10 to 14 business days.
* **Commercial Alignment:** We are completely aligned with your phased deliverable structure. We will confirm the exact scope and milestone deliverables during kickoff to match your preferred engagement terms.

Attached is our detailed **4-Page Architectural Proposal PDF** along with the technical CVs of our lead database and cloud systems architects.

We would welcome a brief technical discussion with you and the team this week to review your current staging setup and discuss telemetry findings.

Sincerely,

**Viranga Lakshan**  
Lead Solutions Architect & Database Systems Engineer  
Portfolio: https://viranga-lakshan.github.io/portfolio/  
GitHub: https://github.com/viranga-lakshan  
LinkedIn: https://linkedin.com/in/viranga-lakshan  
