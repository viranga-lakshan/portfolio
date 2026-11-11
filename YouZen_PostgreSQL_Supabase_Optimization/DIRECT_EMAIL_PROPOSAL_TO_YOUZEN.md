# TECHNICAL PROPOSAL & DIRECT OUTREACH

**Recipient:** Romain Asenjo, Co-Founder & CTO — YOUZEN SAS  
**Contact:** hello@youzen.io / Technical Team  
**From:** Viranga Lakshan (Lead Solutions Architect & Database Systems Specialist) — viranga.lakshan@outlook.com  
**Subject:** Technical Plan: PostgreSQL & Supabase Concurrency Optimization for YouZen (100 Restaurants & 100 Salons)  

---

Dear Romain,

I am writing regarding the optimization and concurrency preparation of the shared PostgreSQL / Supabase architecture powering YouZen's restaurant and hair salon applications.

Supporting **100 restaurants** (100 active checkout terminals and 200 staff mobile phones during dinner rush) alongside **100 hair salons** (active appointment calendars, availability searches, and concurrent online/phone bookings) on a single shared PostgreSQL database is a critical inflection point. Without targeted concurrency controls, unoptimized multi-tenant Row-Level Security (RLS), and refined connection pooling, combined peak traffic risks lock contention, query latency spikes, and double-booking race conditions.

We have engineered high-throughput, multi-tenant PostgreSQL and Supabase systems across hospitality and scheduling verticals. We specialize in isolating database bottlenecks, engineering synthetic load-testing harnesses, eliminating lock waits, and optimizing Supabase Realtime synchronization.

---

### Key Technical Focus Areas for YouZen

| Domain | Immediate Investigation & Engineering Focus |
| :--- | :--- |
| **Realtime & Refresh Storms** | Audit 200 staff mobile clients and 100 POS screens to prevent Postgres WAL replication bloat and eliminate redundant polling on order and table status tables. |
| **Lock Contention & Race Conditions** | Implement deterministic row locking (`SELECT ... FOR UPDATE SKIP LOCKED`) and advisory locks on `orders`, `ticket_items`, and `appointments` to guarantee zero double-bookings or duplicate kitchen tickets under concurrent submission. |
| **Row-Level Security (RLS) Optimization** | Refactor tenant isolation policies on location-scoped tables. Replace dynamic table joins in RLS with session-cached JWT claims and `STABLE` helper functions to eliminate `O(N)` query overhead. |
| **Connection Pooling & PgBouncer** | Fine-tune transaction-mode connection pool limits and backend worker allocations to ensure peak spikes never cause connection starvation or timeouts. |
| **Query & Index Architecture** | Implement composite and partial indexes on high-churn status columns (e.g., `WHERE status = 'active'` or `WHERE scheduled_at >= CURRENT_DATE`) and ensure 100% covering index coverage on foreign keys. |

---

### Structured Two-Phase Roadmap

#### Phase 1: Baseline Audit & Synthetic Staging Load Testing (Weeks 1–2)
1. **Telemetry & Query Telemetry:** Profile `pg_stat_statements`, active lock trees, buffer cache hit ratios, and API latency percentiles (p50, p95, p99).
2. **Synthetic Data Harness:** Generate realistic multi-tenant data for 100 restaurants and 100 hair salons with appropriate data skew and relational depth.
3. **Repeatable Staging Load Scripts:** Develop automated k6 / Locust load-testing test scripts simulating:
   - Scenario A: Restaurant dinner rush (100 checkouts + 200 staff phones submitting orders, updating kitchen displays).
   - Scenario B: Salon peak booking rush (concurrent appointment searches, slot reservations, calendar refreshes).
   - Scenario C: Combined concurrent peak simulation.
4. **Phase 1 Baseline Report:** Comprehensive documentation of latency profiles, lock wait points, connection limits, and failure thresholds.

#### Phase 2: Implementation, Re-Verification & Operational Handover (Weeks 3–4)
1. **Targeted Code & Database Fixes:** Deploy optimized indexes, rewritten queries, RLS policy refactoring, concurrency guards, and Supabase Realtime channel filters.
2. **Verification Load Testing:** Re-run identical automated k6 tests against the optimized staging environment under identical peak loads.
3. **Before-and-After Deliverables:** Quantified comparison tables showing response time drops, throughput increases, peak connection stabilization, and zero transaction rollbacks.
4. **Capacity & Monitoring Handover:** Production rollout runbook, Grafana / Supabase monitoring thresholds, alerting rules, and long-term scaling guidelines.

---

### Technical Documents & CVs
* **Detailed Technical Proposal PDF:** [`YouZen_PostgreSQL_Supabase_Optimization_Proposal.pdf`](file:///C:/Users/Viranga/Downloads/upwrok%20new/YouZen_PostgreSQL_Supabase_Optimization/YouZen_PostgreSQL_Supabase_Optimization_Proposal.pdf)
* **Lead Engineer Profiles:**
  * **Viranga Lakshan:** Lead Solutions Architect & Database Systems Specialist ([CV](file:///C:/Users/Viranga/Downloads/upwrok%20new/YouZen_PostgreSQL_Supabase_Optimization/Viranga_Lakshan_CV.pdf) • [Portfolio](https://viranga-lakshan.github.io/portfolio/) • [GitHub](https://github.com/viranga-lakshan))
  * **Janith Kavishka:** Senior Systems & API Integration Engineer ([CV](file:///C:/Users/Viranga/Downloads/upwrok%20new/YouZen_PostgreSQL_Supabase_Optimization/Janith_Kavishka_CV.pdf))
  * **Lithumitha Ravikumar:** Senior Software & Data Engineer ([CV](file:///C:/Users/Viranga/Downloads/upwrok%20new/YouZen_PostgreSQL_Supabase_Optimization/Lithumitha_Ravikumar_CV.pdf))

We are available for an initial technical kickoff call to inspect your current schema, discuss staging environments, and begin Phase 1 telemetry immediately.

Best regards,

**Viranga Lakshan**  
Lead Solutions Architect & Database Systems Engineer  
viranga.lakshan@outlook.com  
Portfolio: https://viranga-lakshan.github.io/portfolio/  
GitHub: https://github.com/viranga-lakshan  

