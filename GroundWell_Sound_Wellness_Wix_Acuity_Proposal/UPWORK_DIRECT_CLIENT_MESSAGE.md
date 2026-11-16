# Direct Client Message & Proposal Submission — GroundWell Sound & Wellness Center

**Project:** Wix Website Build from Existing Mockup with CMS & Acuity Scheduling  
**Client Budget:** $2,000.00 Fixed-Price (Accepted in Full)  
**Proposed Delivery Timeline:** 3 Weeks (Sprint-based with staging previews)  
**Technical Lead:** Avishka Meddegoda (Senior Full-Stack Engineer & System Architect, 6+ Years Exp)  
**Delivery Lead & Solutions Architect:** Viranga Lakshan (Axiom Global)  
**Contact:** virangalakshanz@gmail.com | +94 71 378 1359 | [https://axiomglobal.tech](https://axiomglobal.tech)

---

### Upwork Proposal Cover Letter & Direct Client Message

Hi there,

I hope you're having a wonderful week.

We have thoroughly explored your interactive Figma mockup (`tinyurl.com/groundwellcentersite`) and the complete architectural specifications for **GroundWell Sound & Wellness Center**. We love the grounded, serene aesthetic, intentional typographic rhythm, and clean spatial hierarchy you've established.

Our engineering team at **Axiom Global** is ready to translate this vision into a high-performance, responsive Wix website integrated seamlessly with Acuity Scheduling for your exact **$2,000 fixed price budget**.

Our team members bring proven experience from Sri Lanka's leading enterprise software engineering companies (including Arimac Digital and top international tech consultancies), building digital platforms for enterprise clients across the **United States, United Kingdom, Australia, the UAE, and the Middle East**. This project will be technically led and architected by **Avishka Meddegoda**, our Senior Full-Stack & Systems Architect with 6+ years of enterprise platform experience, alongside CMS specialists dedicated to delivering an effortless, no-code operational workflow for your day-to-day management.

---

### Critical 2026 Subscription Guidance (Verified Current Pricing)

To ensure complete transparency and eliminate unexpected operating expenses, we verified current 2026 platform pricing and feature matrices:

1. **Wix Business Plan — Wix Core:**
   * **Cost:** **$29 / month** (billed annually at $348/year) or $36 / month (month-to-month).
   * **Why it's required:** Wix Core provides custom domain connection, 50 GB storage (essential for audio sample streaming and high-res imagery), up to 5 collaborator seats, removal of Wix ads, and full dynamic Wix CMS collection support.
2. **Acuity Scheduling Plan — Standard Tier (formerly 'Growing'):**
   * **Cost:** **$27 / month** (billed annually at $324/year) or $34 / month (month-to-month).
   * **Why Standard is strictly mandatory for GroundWell:** The entry-level Starter tier ($16/mo) allows only 1 calendar and completely lacks room resource management, text/SMS reminders, and gift certificate selling. The **Standard tier includes up to 6 calendars**, which is strictly necessary to assign individual practitioner schedules while linking shared treatment rooms through Acuity's **Rooms & Resources** engine to prevent physical double-bookings. It also enables client gift certificate purchasing and automatic appointment SMS reminders.

---

### Answers to Your 6 Specific Review Questions

#### 1. How will you build the shared class and certification CMS templates so entering an offering once updates all relevant pages dynamically?
We build two dynamic Wix CMS collections:
* `Offerings_Events` (Classes, Sound Baths, Workshops, Mentorship)
* `Offerings_Certifications` (Multi-day training, practitioner certifications)

Each collection item contains structured fields: `Title`, `Slug`, `Modality_Category` (Sound, Reiki, Tuning Forks, Somatics, Drumming), `Summary_Short`, `Body_Description_RichText`, `Cover_Image`, `Instructor_Ref`, `Date_Time_Start`, `Duration`, `Price_Display`, `Acuity_Direct_Booking_URL`, and a Boolean toggle `isFeaturedHome`.

We design **ONE master dynamic page template** for Events and **ONE for Certifications**. When you create a single entry in the Wix dashboard:
* It generates its own SEO-optimized canonical detail page (`/events/{slug}`).
* It automatically displays on the main **Classes & Events** hub, sorted chronologically (`Date_Time_Start >= Today`).
* It automatically populates the filtered repeater on the respective **Modality page** (e.g., Reiki events appear automatically on the Reiki page via dataset category filtering).
* If `isFeaturedHome` is checked, it immediately surfaces in the curated carousel on the **Homepage**.
You never duplicate pages or touch design code—you simply add content.

#### 2. What is your experience with Acuity Scheduling? How will you handle multi-practitioner bookings and shared treatment room conflict prevention?
We have extensive hands-on experience integrating Acuity Scheduling across wellness centers, clinics, and multi-disciplinary practices. 

To prevent physical room conflicts when multiple practitioners share treatment spaces:
1. We configure each practitioner with their own **Acuity Calendar** (e.g., Practitioner A, Practitioner B) and independent working hours.
2. We configure your physical rooms as **Resources** inside Acuity under *Manage Calendars > Rooms/Resources* (e.g., "Treatment Room 1 - Sound Sanctuary", "Treatment Room 2 - Reiki Suite").
3. Each individual appointment type is linked to both the practitioner and the required physical Room Resource.
4. When a client books Practitioner A in Treatment Room 1, Acuity instantly locks Treatment Room 1. Even if Practitioner B is on duty, any service requiring Treatment Room 1 automatically displays as unavailable for that exact timeslot, eliminating double-bookings completely.
5. Intake forms, health waivers, deposit payments (Stripe/PayPal), and automatic confirmation/reminder emails will be wired directly into each service flow.

#### 3. What are the key differences or limitations between desktop and mobile when embedding Acuity booking tools, and how will you optimize the mobile experience?
* **The Mobile Challenge:** Full embedded iFrames on mobile screens often suffer from nested scrollbars, awkward viewport clipping, and double-header confusion. In-page popups can also trigger browser viewport shifting on iOS Safari.
* **Our Optimization Strategy:**
  * **Desktop:** The shared Individual Sessions hub features an elegant, seamless embedded Acuity widget with custom CSS container padding matching the mockup's generous breathing room. Group offerings utilize clean lightbox pop-up modals containing the responsive Acuity scheduler so the visitor never loses their context.
  * **Mobile:** For group classes and workshops, we utilize lightweight trigger buttons that open an optimized, full-screen overlay or initiate a dedicated, clean mobile-responsive Acuity booking flow. We pre-fill client modality parameters and ensure standard touch-target sizing (min 44px) so clients can select dates, sign digital waivers, and complete checkout with zero horizontal scrolling or pinching.

#### 4. Which content updates will the client manage in Wix CMS versus Acuity, and what would be required for full automated synchronization?
* **Managed in Wix CMS:**
  * Marketing titles, rich text descriptions, practitioner bios & photography.
  * Modality categorizations, visual gallery assets, FAQs, and homepage feature toggles.
  * Educational and certification curriculum overviews.
* **Managed in Acuity Scheduling:**
  * Real-time practitioner calendar availability and time-off blocks.
  * Service pricing, payment gateways (Stripe/Square/PayPal), coupon/discount codes.
  * Digital intake questions, liability waivers, cancellation policies.
  * Automated email and SMS reminder sequences.
* **Synchronizing the two:**
  * **Standard Seamless Workflow (Included in $2,000):** When you create an offering in Acuity, you copy its direct booking URL (or appointment type ID) into the single `Acuity_URL` field in the Wix CMS item. The Wix template dynamically binds that link to the "Book Session" button/modal.
  * **Automated Sync Option (Quoted Separately):** If you desire two-way real-time programmatic sync (e.g., adding a class in Acuity automatically generating the Wix CMS item without manual copy-paste), we can deploy a custom webhook pipeline via **Make.com / Zapier or Wix Velo HTTP Functions**. We can deliver this advanced automation as a separate optional add-on for **$350**, or keep the straightforward standard workflow which takes less than 30 seconds per event.

#### 5. Have you reviewed the interactive mockup at tinyurl.com/groundwellcentersite, and do you see any functionality that requires adjustment for Wix or Acuity?
Yes, we thoroughly audited `tinyurl.com/groundwellcentersite`. The layout, serene earthy color scheme, and typography are outstanding. Here are the practical implementation refinements we plan for:
1. **Simulated Booking in Mockup vs. Real Acuity:** The mockup displays simulated booking steps. In production, we will replace these with real Acuity Scheduling embeds and styled pop-up modals while maintaining the mockup's sleek visual framing.
2. **Compact Team Biographies:** The expandable "Read More / Read Less" bio functionality will be built using Wix Velo or native collapsibles to keep the About and Modality pages clean on mobile without page reflow lag.
3. **Sound Sample Audio Player:** We will implement an unobtrusive, elegant custom HTML5 audio player widget that matches GroundWell's minimalist aesthetic, allowing visitors to sample sound bowls and tuning forks seamlessly without heavy third-party player branding.
4. **Gift Certificate Flow:** Handled directly via Acuity's built-in gift certificate engine, allowing customers to purchase vouchers and recipients to redeem unique voucher codes during checkout.

#### 6. What is your timeline and process from project kickoff to launch and client handover?
We deliver this in **3 structured weekly sprints**:

* **Sprint 1 (Days 1–7): Global Architecture, 14 Core Pages & CMS Setup**
  * Typography, global styles, header/footer, mobile navigation drawer.
  * Construction of 14 core pages following the mockup.
  * Schema creation for `Offerings_Events` and `Offerings_Certifications`.
  * Dynamic template construction, repeater bindings, category filters, and chronological sorting.
* **Sprint 2 (Days 8–14): Acuity Scheduling Engine & Interactive Features**
  * Acuity calendar, appointment type, and room resource setup.
  * Treatment room conflict prevention logic and digital intake waivers.
  * Modal lightboxes (Booking, FAQs/Policies, Terms).
  * Audio sample player integration, Instagram feed, and newsletter signup.
* **Sprint 3 (Days 15–21): Ingestion, Comprehensive Testing, SEO & Video Handover**
  * Populating the initial ~17 CMS entries (13 events/workshops + 4 certifications).
  * Cross-device QA (Desktop, Tablet, iOS Safari, Android Chrome).
  * Live end-to-end payment and booking dry-runs.
  * Foundational Local SEO, Schema markup (`HealthAndBeautyBusiness` / `LocalBusiness`), meta tags.
  * Custom Loom video training walk-through for zero-stress client management.

---

### Project Investment & Scope Confirmation

* **Total Fixed Investment:** **$2,000.00 USD** (100% matched to your budget)
  * Milestone 1 (40% — $800): Structure, 14 Pages & Wix CMS Dynamic Templates
  * Milestone 2 (40% — $800): Acuity Configuration, Room Conflicts, Waivers & Modals
  * Milestone 3 (20% — $400): Ingestion of 17 Offerings, Testing, SEO, Handover & Launch
* **Support:** 30 days of post-launch technical support and warranty included.

We have compiled a comprehensive **14-page Executive Proposal & Technical Blueprint PDF** containing the exact data schemas, room conflict diagrams, Wix vs. Acuity workflow maps, and SEO checklists.

We are ready to start immediately upon your approval. Would you be open to a brief introductory call or chat to align on kickoff details?

Warm regards,

**Viranga Lakshan**  
Lead Solutions Architect & Delivery Manager  
*Axiom Global*  
Technical Lead: **Avishka Meddegoda** (Senior Systems Architect, 6+ yrs)  
Email: virangalakshanz@gmail.com | Phone: +94 71 378 1359  
Web: [https://axiomglobal.tech](https://axiomglobal.tech)
