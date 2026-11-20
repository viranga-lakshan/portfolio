# UPWORK SCREENING QUESTIONS & DIRECT ANSWERS

**Job Post:** Developer: build, migrate and launch  
**Client:** Five-lawyer independent business-law firm (Skopje, North Macedonia)  

---

### Question 1: Link 2 live WordPress sites you built with custom post types and Polylang or WPML.

**Answer:**

• **Castle Renewables Australia (Custom WordPress Architecture):**  
  Live URL: https://castlerenewables.com.au  
  Details: Custom WordPress build featuring Custom Post Types (CPTs) for renewable infrastructure assets, case study portfolios, and corporate capabilities with custom taxonomy filtering.

• **Data Management Systems (Pvt) Ltd – Software Division:**  
  Live URL: https://dmssw.com/  
  Details: Production WordPress platform for Sri Lanka’s pioneer software engineering house, built with custom post types for enterprise software solutions and responsive corporate design.  

*(Additional reference: LB Finance PLC & Sustainability Portal: https://www.lbfinance.com / https://sustainability.lbfinance.com)*

**Enterprise Multilingual CMS Context (Why You Are in Safe Hands):**  
Our core engineering team originates from Sri Lanka’s premier software engineering institutions, building massive international enterprise platforms across the UAE, Australia, and Europe. In addition to WordPress, we architect enterprise-grade CMS platforms:

• **Al Ain Museum V1 (Sitecore Headless CMS):**  
  Live URL: https://www.alainmuseum.ae/en  
  Details: Live government cultural institution platform. Headless Sitecore built on Helix principles, using GraphQL Layout Service, Next.js, React, and C#/.NET to deliver a high-speed, personalized multilingual experience.

• **Natural History Museum Abu Dhabi (Sitecore CMS):**  
  Live URL: https://www.nhmad.ae/  
  Details: High-traffic government digital experience platform. Built custom Sitecore components and templates in C#/.NET for personalized, multilingual content delivery and structured schema markup.

• **Holsten Arabia (Umbraco Headless CMS):**  
  Live URL: https://holstenarabia.me/en/  
  Details: Multilingual digital platform for a global beverage brand using Umbraco, Next.js frontend, and C#/.NET REST APIs for multi-market localization.

• **Gravitee.io (Storyblok Headless CMS):**  
  Live URL: https://www.gravitee.io/  
  Details: Global enterprise API platform utilizing Storyblok headless CMS and Astro framework for fast, content-driven page delivery.

*Comparison to WordPress:* Compared to enterprise engines like Sitecore and Umbraco—which require strict Helix architecture, headless GraphQL layouts, and complex multi-region multilingual synchronization—WordPress is comparatively lightweight and basic. Having mastered these multi-million dollar platforms, architecting your 70-field relational structure and executing a clean Divi migration is a straightforward, zero-risk task for our team.

---

### Question 2: In 3–4 lines: how do you keep rankings when a site's templates and URLs change?

**Answer:**
We begin by crawling all 400+ indexed URLs using Screaming Frog to create an exact baseline of current URLs, titles, H1s, and canonicals. For any URL whose slug must change, we implement strict 1:1 server-level 301 redirects (tested to eliminate redirect chains or loops). We preserve identical heading hierarchy, content structure, and internal link equity in the new block templates, configure clean XML sitemaps per language (Macedonian, English, German) with proper hreflang tags, and monitor Google Search Console indexing and 404 logs continuously post-launch.

---

### Question 3: A page type has about 70 structured fields with repeatable rows. What would you use with free plugins only (Secure Custom Fields, native blocks, other) and why?

**Answer:**
We use **Secure Custom Fields (SCF)** (the free, open-source WordPress.org fork of ACF) organized into structured tabs.  
Why SCF instead of native blocks for this specific 70-field legal use-case?  
1. **Relational Querying:** Use-case fields (Area, Audiences, Lead Lawyer, Reviewer) must be queried dynamically via `WP_Query` and meta queries in PHP templates so that Area, Audience, and Lawyer profile pages auto-aggregate their relevant cases without manual duplication.  
2. **Validation & Field Guide Compliance:** SCF enforces strict input rules (character limits, select dropdowns, required fields) so your lawyers cannot break template layouts.  
3. **Editor Usability:** 70 raw fields in native blocks create an overwhelming editing experience; SCF lets us group fields into intuitive tabs (*Overview*, *Procedural Steps*, *Taxonomies*, *Reviewers*) making content entry seamless for your team.

---

### Question 4: Have you migrated a site off Divi? How do you handle the leftover shortcodes in old posts?

**Answer:**
Yes. Divi leaves behind nested `[et_pb_*]` shortcode wrappers that pollute content when the builder is deactivated. We resolve this using a two-stage automated process:  
1. **Automated Database Script:** On staging, our backend engineer runs a custom PHP / WP-CLI script that parses `post_content` via regex, strips Divi layout shortcodes, and extracts pure semantic HTML (`<h2>`, `<h3>`, `<p>`, `<ul>`, `<blockquote>`, and image attachments).  
2. **Block Format Conversion & Verification:** The clean HTML is converted into native WordPress core blocks, mapping historical author categories into true WordPress author profiles. Every article is programmatically verified for missing media, broken links, and author attribution before client sign-off.

---

### Question 5: Can you launch by 17 December? Who besides you works on the project?

**Answer:**
Yes, we guarantee launch by 17 December 2026. The project is delivered by a dedicated two-engineer pod:  
• **Chamara Lahiru** (Lead WordPress Engineer, 6+ Years): Focuses on the Figma-to-block theme implementation, SCF field structures, and Polylang multilingual setup.  
• **Avishka Meddegoda** (Senior Backend Systems Architect, 6+ Years): Manages the staging environment, security hardening, automated Divi shortcode cleansing script, and 301 redirect mapping.  
• **Lithumitha Ravikumar** (Agile PM): Oversees sprint milestones to ensure templates are ready by 4 Dec, your team is supported during content entry (30 Nov – 11 Dec), and QA is locked by 15 Dec.
