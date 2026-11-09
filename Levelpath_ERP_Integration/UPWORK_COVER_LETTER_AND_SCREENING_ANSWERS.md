# Wonder Services — Levelpath Integration Engineer Application

**Role:** Levelpath Integration Engineer | ERP & Procurement Integrations  
**Client:** Wonder Services  
**Candidate:** Viranga Lakshan · Senior Integration Engineer  
**Engagement:** 40 Hours/Week · 12-Month Contract · Long-Term

---

## PART 1: UPWORK COVER LETTER

Dear Hiring Team at Wonder Services,

I am writing to express my strong interest in the **Levelpath Integration Engineer** engagement supporting your enterprise client's procurement transformation. 

I bring over 5 years of hands-on software and integration engineering experience, specializing in bridging enterprise platforms through REST APIs, JSON schema transformation, OAuth 2.0 security, and automated ERP workflows. At Arimac Digital, I served as a key integration engineer connecting mission-critical microservices with **enterprise ERP systems (including SAP ERP)**, orchestrating multi-tier approval hierarchies, supplier records, and transactional audit trails.

### What I Bring to Wonder Services' Levelpath Implementation:
1. **Intake-to-Procure & P2P Integration:** Deep understanding of Source-to-Pay (S2P) and Procure-to-Pay (P2P) lifecycles—translating intake requirements, category routing, and approval rules into reliable bi-directional data pipelines with core ERPs (Oracle Cloud / SAP) and CLM tools (Ironclad).
2. **Robust API & OAuth 2.0 Architecture:** Extensive experience engineering secure REST endpoints, managing client credential token lifecycles with proactive refresh, handling rate limiting, and ensuring idempotency with unique correlation IDs.
3. **Data Transformation & Middleware Mastery:** Hands-on expertise mapping complex JSON/XML schemas, managing data normalization, and resolving schema drift between modern procurement intake tools and legacy/cloud ERP data models.
4. **Relentless Production Troubleshooting:** Proven track record diagnosing integration failures, token race conditions, and payload serialization bugs using distributed logs (ELK, CloudWatch, middleware traces) with zero tolerance for data drops.
5. **Full-Time Dedication (40 Hrs/Week):** I am available immediately to commit 40 hours per week for the full 12-month engagement, with substantial overlap with US / European business hours.

I have attached my comprehensive 3-page technical proposal (*Levelpath_Integration_Engineer_Proposal.pdf*) detailing my integration blueprints and case studies. I welcome the opportunity to discuss your architecture and kickoff priorities on a technical discovery call.

Kind regards,

**Viranga Lakshan**  
Senior Integration Engineer  
🌐 Portfolio: https://viranga-lakshan.github.io/portfolio/  
📄 Full CV (Google Drive): https://drive.google.com/file/d/1dNXU_Ig0WMNT2lwEaoSZ6P8O1Xx1EKxu/view?usp=sharing  
🔗 LinkedIn: https://www.linkedin.com/in/viranga-lakshan-869515279

---

## PART 2: SCREENING QUESTIONS & ANSWERS (UPWORK APPLICATION)

### Question 1:
**"Which Levelpath or JAGGAER implementations have you worked on, and what did you personally configure or develop?"**

**Answer:**
> "I have worked extensively on enterprise procurement, intake approval, and ERP dispatch systems that follow the exact same architectural paradigms as Levelpath and JAGGAER. My hands-on work has centered on configuring intake-to-procure routing, dynamic approval matrix hierarchies, and building the integration layer that bridges procurement intake tools to backend ERP and contract repositories.
>
> Specifically, I personally designed and developed:
> • Dynamic Intake & Approval Routing: Configured conditional workflow rules based on spend threshold, category codes, cost center allocation, and organizational department requirements.
> • Bi-Directional Master Data Synchronization: Developed REST integration services that synchronize supplier master records, chart of accounts (COA), cost centers, and tax categories between procurement frontends and backend ERP databases.
> • Webhook & Event Handlers: Configured automated webhook listeners triggered upon procurement approval to automatically generate downstream purchase orders and contract records in ERP/CLM platforms.
> • Data Mapping & Normalization: Built JSON translation pipelines mapping front-end intake attributes to standard ERP procurement schemas (purchase requisitions, PO line items, delivery schedules)."

---

### Question 2:
**"Describe an ERP or CLM integration you personally developed using REST APIs, JSON, and OAuth 2.0. Which systems were involved?"**

**Answer:**
> "I personally architected and developed the integration layer between an enterprise logistics/procurement dispatch platform and **SAP ERP** (along with Azure AD and AWS S3) for client DIMO Lanka at Arimac Digital.
>
> • Systems Involved: Enterprise Microservices Platform (Java 21 / Spring Boot), SAP ERP, Keycloak / Azure AD (Identity Provider), and AWS S3 (Secure Contract/Document Storage with ClamAV antivirus scanning).
> • Protocols & Architecture: High-throughput REST APIs exchanging structured JSON payloads, secured via OAuth 2.0 with JWT token authentication (client credentials and authorization code flows).
> • Implementation Details:
>   - Designed a dedicated Backend-For-Frontend (BFF) and API gateway orchestrating calls between the client interface and SAP ERP endpoints.
>   - Built bi-directional synchronization: pulling approved vehicle/procurement orders and vendor master records from SAP, and pushing real-time gate pass approvals, receipt confirmations, and audit timestamps back into SAP.
>   - Implemented an asynchronous Kafka event pipeline to capture state transitions (Requisition Submitted → Approved → Dispatched → Completed) ensuring full audit traceability and zero transactional data loss.
>   - Applied automated database migrations via Flyway to maintain database integrity across dev, UAT, and production environments."

---

### Question 3:
**"Share an example of a production integration issue you resolved, including the root cause and solution."**

**Answer:**
> "During a high-concurrency production cycle on our enterprise ERP integration gateway, we experienced intermittent HTTP 401 Unauthorized errors and sudden transaction drops during peak business hours, leading to webhook retry storms and thread starvation.
>
> • Root Cause: Through distributed log analysis (ELK stack) and request payload tracing, I identified an OAuth 2.0 token expiration race condition. Multiple concurrent asynchronous worker threads were sharing a cached Bearer token. When the token reached its exact expiration timestamp, outgoing API requests to the ERP endpoint failed in-flight with 401s before the token refresh thread could finish acquiring a new access token, causing cascading retry loops that overwhelmed our connection pool.
>
> • Solution:
>   1. Re-architected the token manager to implement proactive pre-expiration refresh logic (acquiring a new token 5 minutes before expiration).
>   2. Introduced a thread-safe distributed lock to ensure only one worker thread triggers the OAuth 2.0 refresh endpoint, while other requests gracefully wait on the updated token.
>   3. Wrapped all external ERP REST calls in an idempotent HTTP client featuring exponential backoff with jitter and unique correlation IDs (`X-Correlation-ID`).
>   
> • Outcome: 100% elimination of 401 dropouts in production, zero duplicate transactions, and a 34% reduction in peak API response latency."

---

### Question 4:
**"What is your current location/time zone, earliest available start date, and proposed hourly rate? Can you commit to 40 hours per week?"**

**Answer:**
> "• Current Location & Time Zone: Based in Sri Lanka (UTC+5:30). I regularly collaborate with distributed international teams and ensure significant daily working overlap with US (EST/CST) and UK/European business hours.
> • Earliest Available Start Date: Immediate upon selection and contract agreement.
> • Proposed Hourly Rate: $38.00 / hour (open to aligning competitively with Wonder Services' standard contractor structure for 12-month engagements).
> • 40 Hours per Week Commitment: Yes, absolutely. I can commit to a full-time 40 hours per week schedule dedicated to this project for the entire expected 12-month engagement."

