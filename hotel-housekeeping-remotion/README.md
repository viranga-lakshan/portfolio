# RoomReady — Animated Product Promo Video (Remotion)

A 60-second, 1080p 30fps animated SaaS promo video for **RoomReady: Hotel Housekeeping Management System** by **Team Axio Global**, custom-designed to demonstrate operational transformation to Hotel Owners, General Managers, and CEOs.

---

## Executive Summary & Direct Deliverables

- **Final Rendered Video:** [`out/housekeeping-promo.mp4`](file:///c:/Users/Viranga/Downloads/upwrok%20new/hotel-housekeeping-remotion/out/housekeeping-promo.mp4) *(1920x1080 @ 30fps, exactly 1,800 frames / 60.00s)*
- **Preview Gallery & High-Res Stills:** [`out/`](file:///c:/Users/Viranga/Downloads/upwrok%20new/hotel-housekeeping-remotion/out/)
  - `preview_scene1.png` — *The Problem & Daily Operational Gap*
  - `preview_scene2.png` — *RoomReady Brand Identity & Logo Reveal*
  - `preview_scene3.png` — *Luminous 24-Room Executive Live Tablet Board*
  - `preview_scene4.png` — *Housekeeper Mobile PWA App & Multilingual Completion*
  - `preview_scene5.png` — *Supervisor Photo Inspection & Instant Front Desk Sync*
  - `preview_scene6.png` — *Maintenance Photo Ticket & Multi-department Alerts*
  - `preview_scene7.png` — *General Manager KPI Dashboard & Weekly Analytics*
  - `preview_scene8.png` — *Executive Call to Action & Contact Cards*

---

## Remotion Commands

Run these inside the `hotel-housekeeping-remotion` directory:

```bash
cd "hotel-housekeeping-remotion"
```

### 1. Interactive Preview in Remotion Studio
```bash
npm run start
# Or directly:
npx remotion studio src/index.ts
```

### 2. Render Full 60-Second Production MP4
```bash
npm run build
# Or directly:
npx remotion render src/index.ts HousekeepingPromo out/housekeeping-promo.mp4
```

---

## 8-Scene Sequence Architecture (1,800 Frames / 60.00s)

| Scene | Duration | Frames | Key Visuals & Interactions | Voiceover & Audio Design |
|---|---|---|---|---|
| **1. The Problem** | 7.5s | `0 – 225` | Typewriter headline: *"Which rooms are ready? Nobody knows."* Glassmorphic floating problem cards (*Lost Paperwork, Walkie-Talkie Static, WhatsApp Chaos, Lobby Delays*). Gentle camera drift and center collapse into singularity. | Authoritative Christopher Neural VO: *"Which rooms are ready? Radios and paper lists leave front desk guessing, while guests wait."* Subtle whoosh transition SFX. |
| **2. Logo Reveal** | 6.0s | `225 – 405` | Radiant emerald particle aura. RoomReady luxury hotel penthouse keystone logo badge with smooth high-damping spring. Tagline: *"Every room. Live. Ready faster."* Verified badge: *"By Team Axio Global"*. | *"Meet RoomReady: every room, live, ready faster."* Crystalline hotel bell chime SFX. |
| **3. Live Room Board** | 10.5s | `405 – 720` | Luminous white tablet mockup matching Proposal Page 1. 24 room tiles across Floors 1–3 (*101–108, 201–208, 301–308*). Animated cursor clicks Room 102 & 105, transitioning from Dirty &rarr; Assigned &rarr; Cleaning &rarr; Ready. Dynamic counters update live (*Ready 9 &rarr; 13, Dirty 5 &rarr; 2*). | *"See every room in real time. Tiles update live as staff assign, clean, and turnover."* Subtle tactile click SFX. |
| **4. Housekeeper App** | 9.5s | `720 – 1005` | Sleek iPhone 16 frame matching Proposal Page 3. Room 203 with live running timer (*18:42*). Human touch clicks Start, 4 checklist items check off sequentially with emerald ticks. Tap Done triggers multilingual cycler: **Done &rarr; නිමයි &rarr; முடிந்தது &rarr; تم**. | *"Housekeepers follow clear checklists on mobile, with instant timers in their own language."* Soft click & chime SFX. |
| **5. Inspection & Sync** | 8.0s | `1005 – 1245` | Split screen: Supervisor Inspection Card with photo proof thumbnails (*Bed photo, Bathroom photo*). Tap Pass triggers emerald glow and 100% score pill. Right side: Room 203 instantly flips to green Ready to Sell on front desk live board. | *"Supervisors inspect with photos. Tap Pass, and the room turns green on front desk screens."* Emerald chime confirmation SFX. |
| **6. Maintenance & Alerts** | 6.0s | `1245 – 1425` | Split view: AC repair ticket with interactive stepper (*Open &rarr; In Progress &rarr; Fixed ✓*), automatically unlocking the room. Three push notification pills slide in (*Front Desk, Supervisor, Maintenance*). | *"Maintenance issues include photo proof, auto-locking the room until resolved."* Bubble alert pop SFX. |
| **7. Owner Dashboard** | 6.0s | `1425 – 1605` | General Manager & Owner Analytics dashboard matching Proposal Page 5. 4 animated metric cards (*Rooms Ready: 42, Avg Clean Time: 24 min, Pass Rate: 96%, Open Repairs: 2*). Weekly bar chart and team progress bars. | *"Track clean times, pass rates, and team progress on one live dashboard."* Balanced ambient bed. |
| **8. Call to Action** | 6.5s | `1605 – 1800` | Team Axio Global badge, radiant logo, headline *"Book your free live demo today"*. Three luxury contact cards (*Email, WhatsApp, Online Portal*) and 20% launch offer pill. Holds rock-solid for 2.0s without jitter. | *"Turn housekeeping into your edge. Book your free demo today."* Warm ambient resolution chord. |

---

## Audio Design & Studio Master

1. **Executive Voiceover:**
   - Narrator: Microsoft `en-US-ChristopherNeural` (deep, articulate, trustworthy executive baritone tone used by luxury brands).
   - Fine-tuned pacing (`+2%` to `+6%`) ensuring every clip finishes with 0.8s – 2.0s breathing room before transitions.
2. **Luxury Hotel Ambient Soundtrack:**
   - Custom synthesized Rhodes electric piano, velvet analog pads, deep acoustic bass, and delicate chimes playing an elegant hospitality progression (`Fmaj9` &rarr; `Am7` &rarr; `Bbmaj9` &rarr; `C9sus`).
   - Analog soft-saturation master curve with smooth 1.5s fade-in and 2.0s fade-out.
3. **High-End UI Sound Effects (SFX):**
   - `sfx_click.wav`: Tactile haptic button click.
   - `sfx_chime.wav`: Crystalline hotel bell chime for approvals and logo reveal.
   - `sfx_pop.wav`: Soft bubble notification sound.
   - `sfx_whoosh.wav`: Cinematic ambient transition sweep.
