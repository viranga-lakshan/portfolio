# Upwork Proposal & Cover Letter: Economic Architecture Advisory
**Client:** Economic Architecture Advisory (`econarc.com.sa`)  
**Project:** Website Design & Infrastructure Setup  
**Target Principals:** Haitham Al Rebh (Principal & Founder) & Roman J. Zytek, PhD (Partner)  
**Submission Ready:** Yes (Updated with CMS Technical Evaluation: Webflow vs. Umbraco 17 LTS & Direct Client Infrastructure Costs)

---

## 1. Upwork Proposal Cover Letter

**Subject:** Technical Evaluation & Proposal: Sovereign Bilingual Web Presence & Secure Infrastructure (`econarc.com.sa`)

Dear Haitham and Dr. Zytek,

We have carefully reviewed your project specification, the comprehensive **Brand Identity Guidelines 2026**, and your preference regarding CMS architecture. 

Your practice operates at a sovereign tier—advising at the complex intersection of macroeconomic policy, institutional diagnostics, financial system development, and productivity. A practice founded by former senior leadership from Saudi Arabia’s Ministry of Economy and Planning, G20 Working Group co-chairs, and former IMF economists requires a digital presence that reflects **quiet authority, analytical depth, and institutional credibility**. It must project the rigorous precision of an elite policy institution rather than a commercial agency.

To ensure your practice selects the optimal platform, we have conducted an objective technical evaluation comparing **Webflow CMS** against an enterprise self-hosted / cloud alternative, **Umbraco 17 LTS (ASP.NET Core)**. Both options meet sovereign standards, but each addresses distinct operational priorities.

---

### 1. CMS Technical Evaluation: Webflow vs. Umbraco 17 LTS

#### Recommendation: Webflow (Primary Choice for Speed, Visual Publishing & Zero DevOps)
* **Why it fits Economic Architecture Advisory best:**
  1. **Non-Technical Visual Editing:** Advisory staff and research fellows can draft, edit, and publish policy briefs, working papers, and announcements with visual on-page editing and zero developer dependency.
  2. **Turnkey Sovereign Infrastructure:** Hosting, global edge CDN (Fastly/AWS), automated SSL, and DDoS mitigation are fully managed by the platform, requiring zero ongoing server patching or database maintenance.
  3. **Native Arabic RTL & Localization:** Native Webflow Localization applies `dir="rtl"` automatically for Arabic locales, with per-locale typography, localized metadata, and clean hreflang tags for regional SEO.
  4. **Rapid 2–3 Week Delivery:** Bypasses backend plumbing, allowing our team to focus 100% of effort on typographic calibration, brand geometry, and research repository UX.
  5. **Research Library Handling:** The CMS handles up to 20,000 items. While native CMS file uploads are capped at 10 MB per PDF, we integrate high-capacity external storage (e.g., Cloudflare R2 / AWS S3) for long-form white papers, maintaining a seamless download experience.

#### Alternative: Umbraco 17 LTS (Enterprise Alternative for Full Code Ownership & Unrestricted File Storage)
* **When to select Umbraco 17 LTS:**
  1. **Unrestricted Research Repository:** Native Media Library with zero file-size ceilings for large econometric datasets, comprehensive annual reports, and multi-megabyte research publications.
  2. **Examine (Lucene) Search Engine:** Deep full-text search across policy briefs, authors, and metadata.
  3. **Full Sovereign Code & Data Ownership:** Open-source ASP.NET Core (.NET 10) architecture hosted in the cloud or within dedicated GCC data centers, satisfying strict data residency mandates.
  4. **Our Proven Umbraco Track Record:** Our lead CMS engineer, **Viranga Lakshan**, previously engineered the bilingual digital platform for **Holsten Arabia** ([holstenarabia.me](https://holstenarabia.me)) using Umbraco with a modern Next.js/React frontend in the Middle East.

---

### 2. Client-Owned Project Infrastructure & Zero Agency Hosting Markup
In strict adherence to enterprise best practices, **we never host client applications on our personal or agency cloud servers**. 

From Day 1, all accounts, domain assets, and hosting environments are created directly in **Economic Architecture Advisory’s name**, ensuring you retain 100% legal ownership, data sovereignty, and freedom from vendor lock-in.

#### Transparent Monthly Project Infrastructure Costs (Paid Directly by Client to Vendors)
| Infrastructure Component | Webflow Architecture (Recommended) | Umbraco Cloud Alternative | Client Billing |
|---|---|---|---|
| **CMS Platform & Web Hosting** | **~$25 / mo** (Webflow Premium, billed yearly; 20k CMS items, 50 GB CDN) | **~$49.73 (€45) / mo** (Umbraco Cloud Starter; Azure hosting, managed SQL, Cloudflare CDN) | Direct to Vendor |
| **Bilingual Localization** | **$9 / mo** (Localize Essential; handles Arabic secondary locale) | **Included** (Native multi-culture language variants in Umbraco) | Direct to Vendor |
| **Forms & Inquiries Gateway** | **Included** (Webflow Native Forms with reCAPTCHA & inbox routing) | **Included** (Umbraco Cloud Forms included; €100/yr if self-hosted) | Direct to Vendor |
| **Domain Registration** | **~$1–2 / mo** (amortized; registered in client name at registrar) | **~$1–2 / mo** (same) | Direct to Registrar |
| **Monthly Platform Subtotal** | **~$34 / month** | **~$50 / month** | **Direct Vendor Cost** |
| **Enterprise Business Email** | **~$6–8 / user / mo** (Google Workspace or Microsoft 365) | **~$6–8 / user / mo** (same) | Direct to Google / Microsoft |

*Note: Agency development fees for design, engineering, and configuration are separate and will be aligned based on your platform choice.*

---

### 3. Cryptographic Email Hardening & Sovereign Security (`econarc.com.sa`)
For high-level communications with ministries, sovereign funds, and multilateral institutions, email deliverability and confidentiality cannot be compromised:
* **Custom Executive Routing:** Setup of Google Workspace or Microsoft 365 mailboxes (`haitham@econarc.com.sa`, `zytek@econarc.com.sa`, `inquiries@econarc.com.sa`).
* **SPF Protocol:** Strict authorized server definition (`v=spf1 include:_spf.google.com ~all`).
* **DKIM 2048-Bit Signing:** Cryptographic public/private key verification ensuring executive emails cannot be tampered with in transit.
* **DMARC Enforcement:** Strict policy (`p=quarantine` graduating to `p=reject`) with automated forensic aggregate reporting (`rua`) sent to a dedicated security mailbox.
* **DNSSEC & TLS 1.3:** Complete DNS root security and forced encrypted transport.

---

### 4. Dedicated Senior Engineering Team
Your project is executed directly by our cross-functional delivery team with deep Middle Eastern institutional track records:

1. **Viranga Lakshan — Senior CMS Full-Stack Developer (2+ Years Experience)**  
   *Lead CMS & Frontend Architect.* Built government cultural platforms in the UAE (**Al Ain Museum** - [alainmuseum.ae](https://alainmuseum.ae), **Natural History Museum Abu Dhabi** - [nhmad.ae](https://nhmad.ae)), regional Middle Eastern Umbraco portals (**Holsten Arabia** - [holstenarabia.me](https://holstenarabia.me)), and headless CMS sites (**Gravitee.io** - [gravitee.io](https://gravitee.io), **Moolee** - [moolee.mv](https://moolee.mv)).
2. **Avishka Meddegoda — Full-Stack Software Engineer (6+ Years Experience)**  
   *Cloud Architecture & Security Lead.* Specialist in cloud infrastructure, DNS engineering, and API security. Delivered enterprise platforms for major regional telecom operators (Ooredoo Algeria, Ooredoo Maldives). Author of published IEEE research.
3. **Janith Kavishka — Full-Stack Developer (2+ Years Experience)**  
   *Frontend & Localization Specialist.* Expert in React, Next.js, TypeScript, and responsive bilingual layouts. Experience with enterprise transaction workflows and AWS cloud infrastructure for multinational clients (SINGER Sri Lanka PLC).
4. **Lithumitha Ravikumar — Dedicated Project Manager (2 Years Experience)**  
   *Delivery Governance & Quality Assurance.* First Class Honours in Business Information Systems. Managed delivery coordination for UAE cultural platforms (Al Ain Museum) and Australian corporate investment portals (Guardian Funds, Castle Group).

---

### 5. Delivery Roadmap (2 to 4 Weeks)
* **Week 1:** Discovery, design system tokens (Midnight `#102C3A`, Copper `#C98352`, Warm Neutral `#F5F0E8`), English layouts for Home, Leadership, and the Six Advisory Domains.
* **Week 2:** Full template builds, Insights research repository with domain taxonomy, and validated inquiry forms.
* **Week 3:** Arabic locale implementation, Noto Sans Arabic typography calibration, RTL layout testing across iOS/Android, and domain DNS / email hardening.
* **Week 4:** End-to-end security & deliverability validation, Lighthouse performance audits, recorded editor training (1–2 hrs), and handover documentation.

---

### 6. Commercial Terms & Next Steps
We invite you to review our attached technical proposal: **`Economic_Architecture_Advisory_Web_Infrastructure_Proposal.pdf`**. 

Consistent with sovereign advisory engagements, **our professional development milestones and commercial terms will be aligned during our introductory discovery meeting** once your team confirms your platform preference (Webflow vs. Umbraco).

Are you available for a brief introductory call this week to review the comparison and discuss your infrastructure preferences?

Sincerely,  
**Viranga Lakshan, Avishka Meddegoda, Janith Kavishka & Lithumitha Ravikumar**  
*Enterprise Engineering & CMS Delivery Team*
