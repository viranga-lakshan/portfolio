# Upwork Proposal Cover Letter

**Job Posting:** Wix Website Build from Existing Mockup with CMS & Acuity Scheduling  
**Client Budget:** $2,000.00 Fixed-Price (Agreed & Accepted)  
**Deliverable PDF:** `GroundWell_Sound_Wellness_Wix_Acuity_Proposal.pdf` (Attached)

---

### Copy-Paste Proposal Text for Upwork:

Hi there,

We have thoroughly reviewed your project brief and explored your interactive mockup at **tinyurl.com/groundwellcentersite** for **GroundWell Sound & Wellness Center**. We love the grounded, serene aesthetic, spacious editorial typography, and thoughtful community-first structure.

Our engineering team at **Axiom Global** is eager to build and launch this website for you on Wix with seamless Acuity Scheduling integration, adhering strictly to your **$2,000 fixed-price budget**.

Our team members bring rich engineering backgrounds from Sri Lanka's leading enterprise software companies (including Arimac Digital and top international tech consultancies), having built high-traffic platforms for clients across the **US, UK, Australia, the UAE, and the Middle East**. This project will be technically led and architected by **Avishka Meddegoda**, our Senior Full-Stack Engineer and Systems Architect (6+ years experience), ensuring rock-solid data architecture, seamless room-conflict booking logic, and an effortless day-to-day management experience for you.

---

### Critical 2026 Subscription Guidance (Verified Current Pricing)

To avoid unexpected operating expenses, here is the verified current 2026 platform pricing for your setup:

1. **Wix Core Plan:**
   * **$29 / month** (billed annually at $348/year) or $36 / month (monthly).
   * *Why it's required:* Provides custom domain connection, 50 GB storage (essential for audio sample streaming and high-res imagery), up to 5 collaborator seats, removal of Wix ads, and dynamic Wix CMS collection capability.
2. **Acuity Scheduling — Standard Plan (formerly 'Growing'):**
   * **$27 / month** (billed annually at $324/year) or $34 / month (monthly).
   * *Why Standard is strictly mandatory for GroundWell:* The Starter tier ($16/mo) allows only 1 calendar and omits room resource conflict management, text/SMS reminders, and gift certificate purchasing. The **Standard tier includes up to 6 calendars**, allowing you to set up individual practitioner schedules and link them to physical treatment rooms using Acuity's **Rooms & Resources** engine, preventing double-bookings. It also enables client gift certificate sales and automatic SMS appointment reminders.

---

### Answers to Your 6 Specific Review Questions

#### 1. How will you build the shared class and certification CMS templates so entering an offering once updates all relevant pages dynamically?
We configure two structured dynamic collections in Wix CMS:
* `Offerings_Events` (Classes, Sound Baths, Workshops, Mentorship)
* `Offerings_Certifications` (Multi-day training, practitioner certifications)

Each entry contains: Title, Slug, Modality (Sound, Reiki, Tuning Forks, Somatics, Drumming), Summary, Body Rich Text, Image, Instructor, Date & Time, Duration, Price, Acuity Booking URL, and a Homepage Featured toggle (`isFeaturedHome`).

We build **ONE master dynamic page template** for Events and **ONE for Certifications**. When you add an offering once in Wix:
* It generates its own SEO-friendly detail page (`/events/{slug}`).
* It automatically displays on the main **Classes & Events** hub, sorted chronologically (`Date >= Today`).
* It automatically populates the filtered repeater on the matching **Modality page** (e.g. Reiki events appear on the Reiki page).
* If toggled featured, it displays on the **Homepage**.
You never duplicate pages or touch design code—you simply add content.

#### 2. What is your experience with Acuity Scheduling? How will you handle multi-practitioner bookings and shared treatment room conflict prevention?
We have configured Acuity across multiple multi-modality wellness and healthcare clinics. To prevent room conflicts:
1. Each practitioner has their own dedicated calendar with custom working hours.
2. We configure your physical rooms as **Resources** in Acuity (*Manage Calendars > Rooms/Resources*), such as "Treatment Room 1 - Sound Suite" and "Treatment Room 2 - Reiki Studio".
3. Each individual service requires both the practitioner and the assigned Room Resource.
4. When a client books Practitioner A in Treatment Room 1, Acuity locks that room resource for the duration of the session. Even if Practitioner B is available, any service requiring Treatment Room 1 automatically displays as unavailable for that time window, eliminating double-bookings completely.
5. Intake forms, health waivers, payments (Stripe/PayPal), and automated confirmation/reminder sequences are fully wired into each service flow.

#### 3. What are the key differences or limitations between desktop and mobile when embedding Acuity booking tools, and how will you optimize the mobile experience?
* **Desktop:** The shared Individual Sessions page features a clean, seamless embedded Acuity widget with custom CSS padding matching the mockup's generous breathing room. Group offerings utilize clean lightbox pop-up modals containing the responsive Acuity scheduler so visitors never lose page context.
* **Mobile:** Full embedded iFrames on mobile screens often create awkward double scrollbars and viewport clipping. To optimize mobile:
  * For group classes and workshops, we use lightweight trigger buttons that open an optimized, full-screen overlay or initiate a dedicated, clean mobile-responsive Acuity booking flow.
  * All touch targets meet accessibility standards (minimum 44x44px), and client modality parameters are pre-filled so clients can select dates, sign digital waivers, and complete checkout with zero horizontal scrolling or pinching.

#### 4. Which content updates will the client manage in Wix CMS versus Acuity, and what would be required for full automated synchronization?
* **Managed in Wix CMS:** Marketing copy, rich descriptions, practitioner bios & photography, modality categories, image galleries, FAQs, and homepage featured toggles.
* **Managed in Acuity Scheduling:** Real-time practitioner calendar availability, working hours, pricing, payment gateways, coupon codes, digital intake waivers, and reminder sequences.
* **Standard Workflow (Included in $2,000):** When you set up an offering in Acuity, you copy its direct booking URL (or appointment type ID) into the single `Acuity_URL` field in the Wix CMS item. The Wix template dynamically binds that link to the "Book Session" button/modal.
* **Automated Sync Option (Quoted Separately):** If you desire two-way real-time programmatic sync (e.g., adding an event in Acuity automatically generating the Wix CMS item without manual copy-paste), we can deploy a webhook automation via **Make.com / Zapier or Wix Velo HTTP Functions** as an optional add-on for **$350**, or keep the straightforward standard workflow which takes less than 30 seconds per offering.

#### 5. Have you reviewed the interactive mockup at tinyurl.com/groundwellcentersite, and do you see any functionality that requires adjustment for Wix or Acuity?
Yes, we thoroughly audited `tinyurl.com/groundwellcentersite`. The layout, serene earthy color scheme, and typography are outstanding. Here are the practical implementation refinements we plan for:
1. **Simulated Booking in Mockup vs. Real Acuity:** The mockup displays simulated booking steps. In production, we will replace these with real Acuity Scheduling embeds and styled pop-up modals while maintaining the mockup's sleek visual framing.
2. **Compact Team Biographies:** The expandable "Read More / Read Less" bio functionality will be built using Wix Velo or native collapsibles to keep the About and Modality pages clean on mobile without page reflow lag.
3. **Sound Sample Audio Player:** We will implement an unobtrusive, elegant custom HTML5 audio player widget that matches GroundWell's minimalist aesthetic, allowing visitors to sample sound bowls and tuning forks seamlessly without heavy third-party player branding.
4. **Gift Certificate Flow:** Handled directly via Acuity's built-in gift certificate engine, allowing customers to purchase vouchers and recipients to redeem unique voucher codes during checkout.

#### 6. What is your timeline and process from project kickoff to launch and client handover?
We deliver this in **3 structured weekly sprints**:

* **Sprint 1 (Days 1–7): Global Architecture, 14 Core Pages & CMS Setup**
  * Global styling, typography, header/footer, mobile navigation drawer.
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
* **Warranty:** 30 days of post-launch technical support and bug fixing included at no extra charge.

We have attached our **14-page Executive Proposal & Technical Blueprint PDF** (`GroundWell_Sound_Wellness_Wix_Acuity_Proposal.pdf`) covering full database schemas, conflict prevention logic, mobile optimization plans, and launch checklists.

We are ready to start immediately. Let’s schedule a brief kickoff call or continue our discussion here on Upwork.

Warm regards,

**Viranga Lakshan**  
Lead Solutions Architect & Delivery Manager  
*Axiom Global*  
Technical Lead: **Avishka Meddegoda** (Senior Systems Architect, 6+ yrs)  
Email: virangalakshanz@gmail.com | Phone: +94 71 378 1359  
Web: [https://axiomglobal.tech](https://axiomglobal.tech)
