cover_letter = """I will build this on LearnDash + WooCommerce with ONE custom plugin for the financial snapshots, keeping client financial data separate from course access. Fixed-price quotes for prototype and full system follow right after a short discovery call.

Key approach:
1. Lean Stack: LearnDash handles your six-week courses and coach reviews, while WooCommerce links to PayPal for enrolment. We avoid secondary membership plugins, eliminating dual-system access conflicts.
2. Permanent Financial Layer: Balance sheets (Net Worth, Surplus, and dated snapshots from your wireframe) live in custom tables. Access is gated by login only, never by course expiry. Expired clients retain full access to their financial history and can log in to renew anytime.
3. Security: Sensitive fields use application-level encryption (PHP Libsodium with keys outside the database), backed by session-level data isolation and Solid Security hardening.

Timeline & Feasibility:
A prototype by 1 December 2026 is fully achievable for the core prototype scope. Full system completion before year-end is feasible only as a stretch; my committed delivery date is 16 January 2027 to account for the South African holiday period and allow thorough testing.

My recent builds were on other stacks (Umbraco, Laravel, Spring Boot) with directly transferable architecture for per-user data isolation. To prove this on WordPress, I can deploy a working demo of the snapshot module on staging before contract.

Two questions:
1. Are cohorts on fixed calendar dates, or rolling individual start dates?
2. For renewals, do you prefer one-time extensions or automated recurring billing via PayPal?

I have attached a 4-page technical proposal mapping your wireframe to this architecture, and look forward to our call.

Viranga Lakshan"""

print(f"Character count: {len(cover_letter)} (Target: 1,200 to 1,800)")

with open(r"C:\Users\Viranga\Downloads\upwrok new\WealthWisdom_WordPress\UPWORK_COVER_LETTER.txt", "w", encoding="utf-8") as f:
    f.write(cover_letter)
