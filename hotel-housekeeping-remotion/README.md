# RoomFlow — Hotel Housekeeping Management System
## 60-Second Animated Product Promo Video (Remotion 4.0 + Studio Voiceover)
### Built by Team Axio Global

This project is a high-impact, 60-second 16:9 (1920x1080 @ 30fps = 1800 frames) motion graphics product promo video engineered with **Remotion 4.0**, **React 19**, and **TypeScript**, featuring a full human-grade neural voiceover and ambient corporate electronic music bed.

---

## 🎯 Strategic Purpose
To demonstrate to hotel owners, general managers, and front desk supervisors how **RoomFlow** transforms chaotic housekeeping operations (lost paper checklists, walkie-talkie noise, endless WhatsApp messages) into an automated, real-time visual workflow that gets rooms ready for guests up to **21 minutes faster**.

---

## 🎨 Design System & Theme (`src/theme.ts`)

| Element | Specification | Rationale |
| :--- | :--- | :--- |
| **Canvas** | `1920 × 1080` (16:9 Widescreen) | Standard Full HD landscape video format |
| **FPS & Length** | `30 fps` • `1800 frames` = `60.00s` | Exact 1-minute pitch timing |
| **Background** | Dark Navy (`#0F172A`) | Premium SaaS aesthetic, high contrast |
| **Accent** | Vibrant Teal (`#14B8A6`) | Highlights live action, progress, and speed |
| **Typography** | Inter (`@remotion/google-fonts/Inter`) | Clean, modern sans-serif. Headlines 72px / 66px, subheads 36px / 38px |
| **Animation Style** | Smooth `spring()` physics | Organic spring mass/damping; zero jarring CSS keyframe jumps |

### Room Status Color & Icon Standard (Never Color Alone)
- 🔴 **Dirty:** `#EF4444` + Alert Pulse Icon
- 🔵 **Assigned:** `#3B82F6` + User Check Icon
- 🟠 **Cleaning:** `#F59E0B` + Broom / Sparkle Icon
- 🟣 **To Inspect:** `#A855F7` + Search Glass Icon
- 🟢 **Ready:** `#22C55E` + Verified Checkmark Icon
- ⚪ **Out of Order:** `#64748B` + Wrench / Ban Icon

---

## 🎬 8-Scene Sequence & Voiceover Alignment

| Scene # | Time & Frames | Title & Visual Scope | Voiceover Script |
| :---: | :---: | :--- | :--- |
| **01** | `00:00 – 00:08`<br>(0–240 frames) | **The Problem:** Paper checklists, walkie-talkie noise, endless WhatsApps, and check-in delays float and shake over a subtle red urgency tint before collapsing into the center. | *"Which rooms are ready? Nobody knows. Paper checklists, walkie-talkies, and messy chat groups mean delays, missed cleanings, and frustrated guests."* |
| **02** | `00:08 – 00:13`<br>(240–390 frames) | **Logo Reveal:** Stylized RoomFlow logo badge scales in with glowing teal pulse, tagline: *"Every room. Live. Ready faster."* and *"By Team Axio Global"*. | *"Meet RoomFlow by Team Axio Global. Every room. Live. Ready faster."* |
| **03** | `00:13 – 00:24`<br>(390–720 frames) | **Live Room Board:** Realistic tablet mockup showing 24 room tiles (Floor 1–3). Tiles transition live from Dirty &rarr; Assigned &rarr; Cleaning &rarr; Ready. Counters update: *Ready 0 &rarr; 6, Dirty 18 &rarr; 9*. | *"See every room's status live on one screen. Watch tiles update in real time as rooms get assigned, cleaned, and turned around."* |
| **04** | `00:24 – 00:34`<br>(720–1020 frames) | **Housekeeper Mobile App:** Mobile mockup slides in. Tap "Start" &rarr; live timer counts up &rarr; 4 checklist items tick off &rarr; tap "Done". Multilingual badge flips: English (*Done*), Sinhala (*නිමයි*), Tamil (*முடிந்தது*), Arabic (*تم*). | *"Housekeepers get a clear priority list. One tap starts the timer, checklists guide every task, and staff work effortlessly in their own language."* |
| **05** | `00:34 – 00:42`<br>(1020–1260 frames) | **Supervisor Inspection:** Split screen. Supervisor taps "Pass" on Room 203 &rarr; 100% inspection score glows green &rarr; front desk board immediately turns green with instant alert notification. | *"Supervisors inspect with a single tap. Once passed, the room turns green on the front desk board—ready to sell instantly."* |
| **06** | `00:42 – 00:48`<br>(1260–1440 frames) | **Maintenance & Alerts:** AC repair ticket #1042 with photo proof transitions from Open &rarr; In Progress &rarr; Fixed. Pop-ups slide in for Room 204 ready, Room 310 sent back, AC fixed in 305. | *"Maintenance requests include photo proof and live status tracking, with instant alerts keeping everyone aligned."* |
| **07** | `00:48 – 00:54`<br>(1440–1620 frames) | **Owner Analytics Dashboard:** 4 animated stat cards count up (*Rooms Ready 42, Avg Clean Time 24 min, Inspection Pass 96%, Open Repairs 2*). Bottom feature pills: *Works Offline, Multi-Language, Excel Import, Audit Reports*. | *"Hotel owners track cleaning times, inspection scores, and team progress on one comprehensive executive dashboard."* |
| **08** | `00:54 – 01:00`<br>(1620–1800 frames) | **Call to Action:** Centered pulsing logo with *"Book your free demo today"*, *"Turn messy housekeeping into a live, organized flow."*, contact pill `demo.axioglobal.tech`, and holding still for the final second. | *"Transform your housekeeping into a live, organized flow. Book your free demo today with Team Axio Global."* |

---

## 🚀 How to Run & Preview

### 1. Interactive Preview in Remotion Studio
```bash
cd hotel-housekeeping-remotion
npm run start
# or: npx remotion studio src/index.ts
```
Opens the Remotion Studio in your browser at `http://localhost:3000` with frame-accurate scrubbing, play/pause, volume control, and timeline markers.

### 2. Render Full 60s MP4 Video
```bash
cd hotel-housekeeping-remotion
npm run build
# or: npx remotion render src/index.ts HousekeepingPromo out/housekeeping-promo.mp4
```

### 3. Render a Specific Still Frame
```bash
cd hotel-housekeeping-remotion
npx remotion still src/index.ts HousekeepingPromo out/thumbnail.png --frame=310
```

---

## 📁 Source File Tree
```
hotel-housekeeping-remotion/
├── out/
│   ├── housekeeping-promo.mp4       # The rendered Full HD 60s video
│   ├── preview_scene1.png           # Scene 1 Still Preview
│   ├── preview_scene2.png           # Scene 2 Still Preview
│   ├── preview_scene3.png           # Scene 3 Still Preview
│   ├── preview_scene4.png           # Scene 4 Still Preview
│   ├── preview_scene5.png           # Scene 5 Still Preview
│   ├── preview_scene6.png           # Scene 6 Still Preview
│   ├── preview_scene7.png           # Scene 7 Still Preview
│   └── preview_scene8.png           # Scene 8 Still Preview
├── public/
│   └── assets/
│       ├── logo.png                 # Stylized RoomFlow brand icon
│       ├── music.mp3                # Ambient corporate electronic bed (fade in/out)
│       └── scene1_vo.mp3 ... scene8_vo.mp3 # Studio-grade neural voiceovers
├── src/
│   ├── index.ts                     # Remotion Root registration
│   ├── Root.tsx                     # Composition declaration (1920x1080 @ 30fps)
│   ├── theme.ts                     # Dark navy, teal, status colors & typography
│   ├── icons.tsx                    # Pure SVG icons (Color + Icon ALWAYS)
│   ├── HousekeepingPromo.tsx        # Master composition with <Series> & Audio
│   └── scenes/
│       ├── Scene1Problem.tsx        # Chaos, paper, radio & typewriter text
│       ├── Scene2LogoReveal.tsx     # Brand reveal & spring scale
│       ├── Scene3RoomBoard.tsx      # Tablet mockup & live 24-room grid
│       ├── Scene4HousekeeperApp.tsx # Mobile PWA mockup & multilingual Done
│       ├── Scene5Inspection.tsx     # Supervisor pass & instant front desk sync
│       ├── Scene6Maintenance.tsx    # Photo maintenance ticket & alerts
│       ├── Scene7Dashboard.tsx      # 4 animated stat counters & feature pills
│       └── Scene8CTA.tsx            # Closing call to action & contact pill
├── package.json
└── tsconfig.json
```

