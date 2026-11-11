# Senior .NET CRM Developer – Technical Interview & Screening Prep Guide

This document prepares you for technical interviews, architectural discussions, and code review screenings for the **Senior Software Developer (C#, ASP.NET, CRM Platform)** position.

---

## 1. Core .NET Framework 4.8 & C# Architecture

### Q1: What are the main challenges when working in .NET Framework 4.8 compared to modern .NET (Core / .NET 8), and how do you navigate them?
* **Runtime & Performance:** .NET Framework 4.8 runs exclusively on Windows and relies on `System.Web.dll` and IIS. It lacks the Kestrel web server, modern JIT optimizations, and hardware intrinsics found in .NET 8.
* **Tight HttpContext Coupling:** Legacy code often directly references static `HttpContext.Current`, making unit testing and dependency injection difficult.
  * *Solution:* Wrap `HttpContext.Current` behind an abstraction (`IHttpContextService` or `IPrincipalProvider`) so business logic can be tested in isolation.
* **Dependency Injection:** .NET 4.8 lacks native DI container out of the box. Legacy projects typically use Autofac, Unity, or Castle Windsor.
  * *Solution:* Standardize on constructor injection; ensure scopes (Transient, Scoped/PerRequest, Singleton) are strictly respected to prevent memory leaks in long-lived services.
* **Garbage Collection & Memory Pressure:** Large Object Heap (LOH) fragmentation can occur when serializing large JSON payloads or manipulating large strings.
  * *Solution:* Utilize `ArrayPool<T>`, `MemoryStream` pooling, and stream-based serialization rather than loading massive strings into memory.

### Q2: How do you design an incremental migration path from .NET 4.8 to .NET 8 without stopping active feature delivery?
* **Strangler Fig Pattern:** Rather than a risky "big bang" rewrite, migrate edge services and high-traffic endpoints incrementally.
* **Shared Class Libraries via .NET Standard 2.0:** Extract shared domain models, business logic interfaces, and calculation engines into `.NET Standard 2.0` class libraries, which can be referenced simultaneously by both .NET Framework 4.8 and .NET 8 projects.
* **YARP (Yet Another Reverse Proxy):** Place a YARP proxy in front of the application. Routes that have been modernized to .NET 8 are handled by the new service, while legacy routes are transparently forwarded to the .NET 4.8 IIS application.
* **Entity Framework Modernization:** Migrate from heavy EF6 `.edmx` diagrams to Code-First mappings, preparing the schema mappings for EF Core.

---

## 2. Navigating Large Legacy Codebases Written by Others

### Q3: What is your systematic approach when inheriting a complex, undocumented legacy codebase?
1. **Establish a Working Local Environment & CI Baseline:** First ensure the solution compiles locally, automated tests run cleanly, and TeamCity build configurations pass.
2. **Characterization Tests (Golden Master Testing):** Before touching legacy logic, write integration/characterization tests capturing the existing inputs and outputs. This creates a safety harness guaranteeing zero regressions.
3. **Trace Hot Data Paths via Logging & APM:** Use Datadog APM and SQL Server Profiler to understand real-world execution paths, identifying where the application spends 80% of its execution time.
4. **Identify Seams for Decoupling (Michael Feathers' Techniques):** Introduce interfaces at natural boundaries (database access, third-party APIs) using Dependency Injection, allowing refactoring without rippling side effects.
5. **Incremental Small PRs:** Keep PRs tightly focused and accompanied by tests, making code reviews easy for teammates.

---

## 3. Hands-on AWS Architecture (Lambda, S3, EC2, DynamoDB)

### Q4: How do you leverage AWS services in a C# / ASP.NET CRM platform?
* **AWS S3 for Document & Attachment Storage:**
  * CRM platforms store customer contracts, email attachments, and profile pictures.
  * Never stream files directly through ASP.NET MVC web servers. Instead, generate **Pre-Signed S3 URLs** with short TTLs (e.g., 15 minutes) for direct client browser upload/download, offloading bandwidth and memory from EC2.
* **AWS Lambda for Asynchronous Processing:**
  * Heavy background tasks (lead scoring recalculations, CSV contact batch imports, daily sales digest generation) are offloaded to C# Lambda functions triggered by S3 events or SQS queues.
  * Mitigate Lambda cold starts using C# Ahead-of-Time (AOT) compilation or provisioned concurrency.
* **Amazon DynamoDB for Audit Trails & Activity Logs:**
  * CRM platforms generate high-velocity user activity logs (e.g., "User viewed contact", "Email opened", "Field modified").
  * DynamoDB handles massive write throughput cost-effectively. Use a single-table design with Partition Key `TenantID#EntityID` and Sort Key `Timestamp#ActivityID` for fast time-series queries.
* **AWS EC2 & Auto-Scaling:**
  * Host ASP.NET MVC apps behind Application Load Balancers (ALB) with SSL termination, health check endpoints (`/health`), and CloudWatch metric alarms for dynamic horizontal scaling.

---

## 4. DevOps, CI/CD & 24/7 Production On-Call

### Q5: How do you configure CI/CD in TeamCity and Octopus Deploy?
* **TeamCity (Continuous Integration):**
  * Configured as the build and test orchestrator: pulls latest branch code, restores NuGet dependencies, compiles in Release mode, runs NUnit/xUnit test suites, executes static code analysis (SonarQube), and packages artifacts into versioned NuGet/ZIP packages.
* **Octopus Deploy (Continuous Delivery):**
  * Manages environment progression: Development ➔ Staging ➔ UAT ➔ Production.
  * Handles environment-specific variable replacement (`web.config` transforms, connection strings, AWS credentials via IAM roles).
  * Executes zero-downtime blue/green or rolling deployments across EC2 targets, verifying IIS application pool warm-up before cutting over traffic.

### Q6: What is your protocol when PagerDuty pages you at 2:00 AM for a Sev-1 production incident?
1. **Acknowledge Immediately:** Acknowledge in PagerDuty within 5 minutes to prevent escalation to secondary engineers.
2. **Initial Triage & Impact Assessment:** Check Datadog APM dashboards to identify affected endpoints, error rates (5xx vs 4xx), database CPU/connections, and host health.
3. **Stabilize Production First (Mitigate Before Perfect Root Cause):** If a bad deployment caused the issue, trigger an automated rollback in Octopus Deploy immediately. If connection exhaustion, recycle the IIS pool or increase connection limits.
4. **Communicate Transparently:** Post real-time status updates to the internal incident Slack channel for engineering and customer support awareness.
5. **Root-Cause Investigation:** Dig into Datadog trace logs, exception stack traces, and slow query logs once production is stable.
6. **Blameless Post-Mortem & Remediation:** Document timeline, root cause, trigger, and actionable preventive items (e.g., adding missing index, adding circuit breaker, improving alert thresholds).

---

## 5. CRM Domain & Architectural Best Practices

### Q7: How do you ensure high performance and data isolation in a multi-tenant CRM platform?
* **Tenant Isolation:**
  * Ensure every table contains a indexed `TenantId`.
  * Enforce tenant scoping at the repository or EF query filter level so queries can never leak data across tenants.
* **Custom Fields & Extensibility:**
  * B2B CRMs allow users to add custom fields to Contacts, Deals, and Accounts.
  * Combine relational storage for core fields with JSONB / schemaless document storage for dynamic custom attributes, backed by indexed GIN / computed column indexes.
* **Concurrency Control:**
  * Use **Optimistic Concurrency** with `RowVersion` / `byte[]` timestamp columns on Deals and Contacts to prevent two sales reps from overwriting each other's edits.
