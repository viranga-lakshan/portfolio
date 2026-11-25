import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { CheckSquareIcon, CheckCircleSolidIcon, MousePointerIcon } from "../icons";

export const Scene4HousekeeperApp: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene4_vo.mp3");
  const clickSrc = staticFile("assets/sfx_click.wav");
  const chimeSrc = staticFile("assets/sfx_chime.wav");

  // Phone slide-in spring from right
  const phoneSpring = spring({
    frame: frame - 6,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });
  const phoneX = interpolate(phoneSpring, [0, 1], [500, 0]);
  const phoneOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Left copy fade in
  const copyOpacity = interpolate(frame, [10, 35], [0, 1]);
  const copyY = interpolate(frame, [10, 35], [30, 0]);

  // Interactive Touch on "Start" at frame 40
  const isTappingStart = frame >= 36 && frame <= 48;
  const startTapScale = isTappingStart
    ? interpolate(frame, [36, 42, 48], [1, 0.9, 1])
    : 1.0;
  const isStarted = frame >= 42;

  // Running timer (simulated count up 18:42 -> 19:10)
  const baseSeconds = 18 * 60 + 42;
  const currentElapsed = isStarted
    ? Math.floor(interpolate(frame, [42, 280], [0, 28], { extrapolateRight: "clamp" }))
    : 0;
  const totalSeconds = baseSeconds + currentElapsed;
  const minutesStr = String(Math.floor(totalSeconds / 60)).padStart(2, "0");
  const secondsStr = String(totalSeconds % 60).padStart(2, "0");

  // Sequential Checklist Checkoffs
  const item1Done = frame >= 65;
  const item2Done = frame >= 95;
  const item3Done = frame >= 125;
  const item4Done = frame >= 155;

  // Touch on "Done" at frame 170
  const isTappingDone = frame >= 166 && frame <= 178;
  const doneTapScale = isTappingDone
    ? interpolate(frame, [166, 172, 178], [1, 0.9, 1])
    : 1.0;
  const isCompleted = frame >= 172;

  // Multilingual "Done" switching after completion (frames 180 to 275)
  // English -> Sinhala (නිමයි) -> Tamil (முடிந்தது) -> Arabic (تم)
  const langIndex = Math.floor(
    interpolate(frame, [180, 275], [0, 3.99], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const doneLanguages = [
    { text: "Done", lang: "English", code: "EN", color: "#3B82F6" },
    { text: "නිමයි", lang: "Sinhala", code: "SI", color: "#F59E0B" },
    { text: "முடிந்தது", lang: "Tamil", code: "TA", color: "#EC4899" },
    { text: "تم", lang: "Arabic", code: "AR", color: "#10B981" },
  ];
  const currentLang = doneLanguages[langIndex] || doneLanguages[0];

  // Touch cursor coordinates
  const cursorX = interpolate(
    frame,
    [15, 42, 60, 160, 172, 220],
    [320, 240, 280, 250, 250, 320],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const cursorY = interpolate(
    frame,
    [15, 42, 60, 160, 172, 220],
    [300, 240, 420, 620, 620, 700],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Exit transition (last 15 frames)
  const exitOpacity = interpolate(frame, [270, 285], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: THEME.bg,
        fontFamily,
        position: "relative",
        overflow: "hidden",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 140px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />
      {frame === 42 && <Audio src={clickSrc} volume={0.4} />}
      {frame === 172 && <Audio src={chimeSrc} volume={0.45} />}

      {/* Left Column: Executive Typography */}
      <div
        style={{
          width: 820,
          opacity: copyOpacity,
          transform: `translateY(${copyY}px)`,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "8px 24px",
            borderRadius: 30,
            backgroundColor: "rgba(20, 184, 166, 0.15)",
            border: `1.5px solid ${THEME.accentTeal}`,
            color: THEME.accentTeal,
            fontSize: 20,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 24,
          }}
        >
          <span
            style={{
              width: 9,
              height: 9,
              borderRadius: "50%",
              backgroundColor: THEME.accentTeal,
              boxShadow: "0 0 10px #14B8A6",
            }}
          />
          Mobile Housekeeper App (PWA)
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            color: THEME.textPrimary,
            margin: 0,
            fontSize: 70,
            letterSpacing: "-0.035em",
          }}
        >
          Simple for staff. <br />
          <span style={{ color: THEME.accentTeal }}>In their own language.</span>
        </h2>

        <p
          style={{
            ...THEME.typography.subhead,
            color: THEME.textSecondary,
            fontSize: 30,
            lineHeight: 1.45,
            marginTop: 22,
            marginBottom: 36,
          }}
        >
          Works on any smartphone with zero app store download. Large buttons, dark mode for corridors, and offline sync for weak Wi-Fi areas.
        </p>

        {/* Feature Highlights Pills */}
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
            <CheckCircleSolidIcon size={26} color="#10B981" />
            <span style={{ fontSize: 22, color: "#FFFFFF", fontWeight: 600 }}>
              Automatic priority room assignment (VIPs & early check-ins first)
            </span>
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
            <CheckCircleSolidIcon size={26} color="#10B981" />
            <span style={{ fontSize: 22, color: "#FFFFFF", fontWeight: 600 }}>
              Tailored checklists for checkout vs. stayover rooms
            </span>
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
            <CheckCircleSolidIcon size={26} color="#10B981" />
            <span style={{ fontSize: 22, color: "#FFFFFF", fontWeight: 600 }}>
              Multi-language: English, Sinhala, Tamil, Arabic & more
            </span>
          </div>
        </div>
      </div>

      {/* Right Column: iPhone Mockup matching Proposal Page 3 */}
      <div
        style={{
          transform: `translateX(${phoneX}px)`,
          opacity: phoneOpacity,
          position: "relative",
        }}
      >
        {/* Sleek Smartphone Chassis */}
        <div
          style={{
            width: 480,
            height: 940,
            backgroundColor: "#0B132B",
            borderRadius: 54,
            border: "12px solid #1E293B",
            boxShadow: "0 40px 100px rgba(0,0,0,0.65), 0 0 0 2px rgba(255,255,255,0.12)",
            position: "relative",
            overflow: "hidden",
            display: "flex",
            flexDirection: "column",
          }}
        >
          {/* Status Bar / Dynamic Island */}
          <div
            style={{
              height: 48,
              backgroundColor: "#0F172A",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "0 28px",
              color: "#94A3B8",
              fontSize: 14,
              fontWeight: 600,
            }}
          >
            <span>09:41</span>
            <div
              style={{
                width: 110,
                height: 24,
                backgroundColor: "#000000",
                borderRadius: 20,
              }}
            />
            <span>5G · 100%</span>
          </div>

          {/* App Header */}
          <div
            style={{
              padding: "18px 24px",
              backgroundColor: "#0F172A",
              borderBottom: "1.5px solid #1E293B",
            }}
          >
            <div style={{ fontSize: 22, fontWeight: 800, color: "#FFFFFF" }}>
              My rooms today
            </div>
            <div style={{ fontSize: 15, color: "#94A3B8", fontWeight: 500, marginTop: 2 }}>
              Nimal · Floor 2 · <span style={{ color: THEME.accentTeal, fontWeight: 700 }}>6 of 12 done</span>
            </div>
          </div>

          {/* Active Room Card matching Proposal Page 3 */}
          <div style={{ padding: "20px 24px", flex: 1, display: "flex", flexDirection: "column" }}>
            <div
              style={{
                backgroundColor: "#1E293B",
                borderRadius: 22,
                padding: "20px 22px",
                border: `1.5px solid ${isCompleted ? "#10B981" : "#334155"}`,
                boxShadow: isCompleted ? "0 10px 30px rgba(16, 185, 129, 0.25)" : "none",
                marginBottom: 16,
              }}
            >
              {/* Room Top Line */}
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <div>
                  <div style={{ fontSize: 30, fontWeight: 800, color: "#FFFFFF" }}>
                    Room 203
                  </div>
                  <div style={{ fontSize: 14, color: "#94A3B8", fontWeight: 600, marginTop: 2 }}>
                    Checkout · King · <span style={{ color: "#F59E0B" }}>Cleaning</span>
                  </div>
                </div>

                {/* Live Timer Pill */}
                <div
                  style={{
                    backgroundColor: "rgba(20, 184, 166, 0.15)",
                    border: `1.5px solid ${THEME.accentTeal}`,
                    padding: "6px 14px",
                    borderRadius: 14,
                    display: "flex",
                    alignItems: "center",
                    gap: 6,
                    color: THEME.accentTeal,
                    fontWeight: 800,
                    fontSize: 18,
                  }}
                >
                  <span style={{ width: 8, height: 8, borderRadius: "50%", backgroundColor: THEME.accentTeal }} />
                  {minutesStr}:{secondsStr}
                </div>
              </div>

              {/* Start Button if not started */}
              {!isStarted && (
                <div
                  style={{
                    marginTop: 16,
                    backgroundColor: THEME.accentTeal,
                    color: "#0F172A",
                    textAlign: "center",
                    padding: "12px",
                    borderRadius: 14,
                    fontWeight: 800,
                    fontSize: 17,
                    transform: `scale(${startTapScale})`,
                  }}
                >
                  Tap to Start Cleaning
                </div>
              )}

              {/* Checklist Items matching Proposal */}
              <div style={{ marginTop: 16, display: "flex", flexDirection: "column", gap: 10 }}>
                {/* Item 1 */}
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 12,
                    fontSize: 15,
                    color: item1Done ? "#FFFFFF" : "#94A3B8",
                    fontWeight: item1Done ? 600 : 400,
                  }}
                >
                  <div
                    style={{
                      width: 24,
                      height: 24,
                      borderRadius: 7,
                      backgroundColor: item1Done ? "#10B981" : "rgba(255,255,255,0.08)",
                      border: `1.5px solid ${item1Done ? "#10B981" : "#475569"}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    {item1Done && <span style={{ color: "#FFF", fontSize: 14, fontWeight: 900 }}>✓</span>}
                  </div>
                  <span>Bed made, linen changed</span>
                </div>

                {/* Item 2 */}
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 12,
                    fontSize: 15,
                    color: item2Done ? "#FFFFFF" : "#94A3B8",
                    fontWeight: item2Done ? 600 : 400,
                  }}
                >
                  <div
                    style={{
                      width: 24,
                      height: 24,
                      borderRadius: 7,
                      backgroundColor: item2Done ? "#10B981" : "rgba(255,255,255,0.08)",
                      border: `1.5px solid ${item2Done ? "#10B981" : "#475569"}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    {item2Done && <span style={{ color: "#FFF", fontSize: 14, fontWeight: 900 }}>✓</span>}
                  </div>
                  <span>Bathroom cleaned & sanitized</span>
                </div>

                {/* Item 3 */}
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 12,
                    fontSize: 15,
                    color: item3Done ? "#FFFFFF" : "#94A3B8",
                    fontWeight: item3Done ? 600 : 400,
                  }}
                >
                  <div
                    style={{
                      width: 24,
                      height: 24,
                      borderRadius: 7,
                      backgroundColor: item3Done ? "#10B981" : "rgba(255,255,255,0.08)",
                      border: `1.5px solid ${item3Done ? "#10B981" : "#475569"}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    {item3Done && <span style={{ color: "#FFF", fontSize: 14, fontWeight: 900 }}>✓</span>}
                  </div>
                  <span>Towels replaced</span>
                </div>

                {/* Item 4 */}
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 12,
                    fontSize: 15,
                    color: item4Done ? "#FFFFFF" : "#94A3B8",
                    fontWeight: item4Done ? 600 : 400,
                  }}
                >
                  <div
                    style={{
                      width: 24,
                      height: 24,
                      borderRadius: 7,
                      backgroundColor: item4Done ? "#10B981" : "rgba(255,255,255,0.08)",
                      border: `1.5px solid ${item4Done ? "#10B981" : "#475569"}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    {item4Done && <span style={{ color: "#FFF", fontSize: 14, fontWeight: 900 }}>✓</span>}
                  </div>
                  <span>Amenities restocked</span>
                </div>
              </div>

              {/* Quick Action Buttons */}
              <div style={{ display: "flex", gap: 8, marginTop: 18 }}>
                <div style={{ flex: 1, backgroundColor: "#334155", color: "#E2E8F0", textAlign: "center", padding: "8px 0", borderRadius: 10, fontSize: 13, fontWeight: 600 }}>
                  Problem
                </div>
                <div style={{ flex: 1, backgroundColor: "#334155", color: "#E2E8F0", textAlign: "center", padding: "8px 0", borderRadius: 10, fontSize: 13, fontWeight: 600 }}>
                  DND
                </div>
                <div style={{ flex: 1, backgroundColor: "#334155", color: "#E2E8F0", textAlign: "center", padding: "8px 0", borderRadius: 10, fontSize: 13, fontWeight: 600 }}>
                  Pause
                </div>
              </div>

              {/* Big Done Button with Multilingual Cycler */}
              <div
                style={{
                  marginTop: 14,
                  backgroundColor: isCompleted ? "#10B981" : THEME.accentTeal,
                  color: isCompleted ? "#FFFFFF" : "#0F172A",
                  textAlign: "center",
                  padding: "14px 0",
                  borderRadius: 14,
                  fontWeight: 800,
                  fontSize: 20,
                  transform: `scale(${doneTapScale})`,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: 10,
                  transition: "all 0.2s ease",
                  boxShadow: isCompleted ? "0 10px 25px rgba(16, 185, 129, 0.4)" : "none",
                }}
              >
                <span>{isCompleted ? currentLang.text : "Done"}</span>
                {isCompleted && (
                  <span
                    style={{
                      fontSize: 12,
                      padding: "2px 8px",
                      borderRadius: 10,
                      backgroundColor: "rgba(0,0,0,0.25)",
                      color: "#FFFFFF",
                      fontWeight: 700,
                    }}
                  >
                    {currentLang.lang}
                  </span>
                )}
              </div>
            </div>

            {/* Next in Queue matching Proposal */}
            <div style={{ marginTop: "auto" }}>
              <div style={{ fontSize: 13, color: "#64748B", fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase", marginBottom: 8 }}>
                Next in queue
              </div>
              <div style={{ display: "flex", justifyContent: "space-between", backgroundColor: "#1E293B", padding: "12px 16px", borderRadius: 14, marginBottom: 8 }}>
                <span style={{ fontWeight: 700, color: "#FFFFFF", fontSize: 16 }}>204</span>
                <span style={{ color: "#3B82F6", fontWeight: 600, fontSize: 14 }}>Stayover</span>
              </div>
              <div style={{ display: "flex", justifyContent: "space-between", backgroundColor: "#1E293B", padding: "12px 16px", borderRadius: 14 }}>
                <span style={{ fontWeight: 700, color: "#FFFFFF", fontSize: 16 }}>207</span>
                <span style={{ color: "#10B981", fontWeight: 700, fontSize: 14 }}>VIP · clean first</span>
              </div>
            </div>
          </div>

          {/* Simulated Touch Pointer */}
          <div
            style={{
              position: "absolute",
              left: cursorX,
              top: cursorY,
              pointerEvents: "none",
              zIndex: 100,
            }}
          >
            <MousePointerIcon size={32} color={THEME.accentTeal} />
          </div>
        </div>
      </div>
    </div>
  );
};
