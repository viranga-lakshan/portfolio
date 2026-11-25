import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { TimerIcon, CheckSquareIcon, BedIcon } from "../icons";

export const Scene4HousekeeperApp: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene4_vo.mp3");

  // Phone slide-in spring from right
  const phoneSpring = spring({
    frame: frame - 5,
    fps,
    config: { damping: 16, mass: 0.8, stiffness: 100 },
  });
  const phoneX = interpolate(phoneSpring, [0, 1], [600, 0]);
  const phoneOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Left copy fade in
  const copyOpacity = interpolate(frame, [15, 40], [0, 1]);
  const copyY = interpolate(frame, [15, 40], [30, 0]);

  // Finger Tap animation on "Start" at frame 50
  const isTappingStart = frame >= 46 && frame <= 60;
  const startTapScale = isTappingStart
    ? interpolate(frame, [46, 52, 60], [1, 0.88, 1])
    : 1.0;

  // Has started cleaning
  const isStarted = frame >= 52;

  // Animated Timer count (simulated minutes:seconds)
  const timerSeconds = Math.floor(
    interpolate(frame, [52, 190], [0, 865], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );
  const minutesStr = String(Math.floor(timerSeconds / 60)).padStart(2, "0");
  const secondsStr = String(timerSeconds % 60).padStart(2, "0");

  // Checklist items completion frames
  const item1Done = frame >= 80;
  const item2Done = frame >= 110;
  const item3Done = frame >= 140;
  const item4Done = frame >= 170;

  // Finger Tap animation on "Done" at frame 190
  const isTappingDone = frame >= 186 && frame <= 200;
  const doneTapScale = isTappingDone
    ? interpolate(frame, [186, 192, 200], [1, 0.9, 1])
    : 1.0;
  const isCompleted = frame >= 192;

  // Multilingual "Done" switching (frames 200 to 295)
  // English -> Sinhala (නිමයි) -> Tamil (முடிந்தது) -> Arabic (تم)
  const langIndex = Math.floor(
    interpolate(frame, [200, 290], [0, 3.99], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const doneLanguages = [
    { text: "Done", lang: "English", code: "EN", color: "#3B82F6" },
    { text: "නිමයි", lang: "Sinhala", code: "SI", color: "#F59E0B" },
    { text: "முடிந்தது", lang: "Tamil", code: "TA", color: "#EC4899" },
    { text: "تم", lang: "Arabic", code: "AR", color: "#22C55E" },
  ];
  const currentLang = doneLanguages[langIndex] || doneLanguages[0];

  // Exit transition
  const exitOpacity = interpolate(frame, [285, 300], [1, 0], {
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
        padding: "0 120px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Left Text & Feature Column */}
      <div
        style={{
          width: 780,
          opacity: copyOpacity,
          transform: `translateY(${copyY}px)`,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "8px 22px",
            borderRadius: 30,
            backgroundColor: "rgba(20, 184, 166, 0.15)",
            border: `1px solid ${THEME.accentTeal}`,
            color: THEME.accentTeal,
            fontSize: 22,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 20,
          }}
        >
          Mobile Housekeeper App (PWA)
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            color: THEME.textPrimary,
            margin: 0,
            fontSize: 68,
          }}
        >
          Simple for staff. <br />
          <span style={{ color: THEME.accentTeal }}>In their own language.</span>
        </h2>

        <p
          style={{
            ...THEME.typography.subhead,
            color: THEME.textSecondary,
            marginTop: 24,
            lineHeight: 1.5,
          }}
        >
          One-tap task start, instant room timers, and step-by-step checklists built for dark corridors.
        </p>

        {/* Multilingual Highlight Card */}
        <div
          style={{
            marginTop: 36,
            padding: "20px 28px",
            borderRadius: 20,
            backgroundColor: THEME.surface,
            border: `2px solid ${THEME.accentTeal}`,
            display: "flex",
            alignItems: "center",
            gap: 20,
            boxShadow: `0 10px 30px ${THEME.accentTealGlow}`,
          }}
        >
          <div
            style={{
              width: 58,
              height: 58,
              borderRadius: 16,
              backgroundColor: currentLang.color,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#FFFFFF",
              fontSize: 22,
              fontWeight: 800,
              boxShadow: `0 8px 20px rgba(0,0,0,0.3)`,
            }}
          >
            {currentLang.code}
          </div>
          <div>
            <div style={{ fontSize: 16, color: THEME.textSecondary, fontWeight: 600 }}>
              Live Translation Active ({currentLang.lang})
            </div>
            <div style={{ fontSize: 32, color: THEME.textPrimary, fontWeight: 800 }}>
              Status: <span style={{ color: THEME.accentTeal }}>{currentLang.text}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Right Column: Realistic Mobile Phone Mockup */}
      <div
        style={{
          width: 440,
          height: 880,
          backgroundColor: "#0B1120",
          borderRadius: 54,
          border: "14px solid #1E293B",
          boxShadow: "0 40px 90px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.1)",
          transform: `translateX(${phoneX}px)`,
          opacity: phoneOpacity,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
          position: "relative",
        }}
      >
        {/* Dynamic Island / Speaker Notch */}
        <div
          style={{
            position: "absolute",
            top: 14,
            left: "50%",
            transform: "translateX(-50%)",
            width: 130,
            height: 28,
            backgroundColor: "#1E293B",
            borderRadius: 20,
            zIndex: 50,
          }}
        />

        {/* Mobile Header */}
        <div
          style={{
            padding: "54px 24px 16px",
            backgroundColor: THEME.surface,
            borderBottom: `1px solid ${THEME.border}`,
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <div>
              <div style={{ fontSize: 14, color: THEME.textSecondary }}>Housekeeper Mode</div>
              <div style={{ fontSize: 24, fontWeight: 800, color: THEME.textPrimary }}>
                My Rooms Today
              </div>
            </div>
            <span
              style={{
                backgroundColor: "rgba(20, 184, 166, 0.2)",
                color: THEME.accentTeal,
                fontSize: 14,
                fontWeight: 700,
                padding: "6px 12px",
                borderRadius: 20,
              }}
            >
              5 Left
            </span>
          </div>
        </div>

        {/* Room 203 Active Cleaning Card */}
        <div style={{ flex: 1, padding: 20, display: "flex", flexDirection: "column", gap: 16 }}>
          <div
            style={{
              backgroundColor: isCompleted
                ? "rgba(34, 197, 94, 0.15)"
                : isStarted
                ? "rgba(245, 158, 11, 0.12)"
                : THEME.surface,
              borderRadius: 24,
              border: `2px solid ${
                isCompleted
                  ? THEME.status.ready.color
                  : isStarted
                  ? THEME.status.cleaning.color
                  : THEME.status.dirty.color
              }`,
              padding: 20,
              display: "flex",
              flexDirection: "column",
              gap: 14,
            }}
          >
            {/* Room Title & Priority Badge */}
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div>
                <span style={{ fontSize: 32, fontWeight: 800, color: THEME.textPrimary }}>
                  Room 203
                </span>
                <span style={{ fontSize: 14, color: THEME.textSecondary, marginLeft: 8 }}>
                  Deluxe King
                </span>
              </div>
              <span
                style={{
                  backgroundColor: "rgba(239, 68, 68, 0.2)",
                  color: "#EF4444",
                  fontSize: 12,
                  fontWeight: 700,
                  padding: "4px 10px",
                  borderRadius: 12,
                  textTransform: "uppercase",
                }}
              >
                VIP Checkout
              </span>
            </div>

            {/* Timer Row */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "10px 16px",
                backgroundColor: "rgba(0, 0, 0, 0.3)",
                borderRadius: 14,
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                <TimerIcon size={20} color={isStarted ? THEME.accentTeal : THEME.textMuted} />
                <span style={{ fontSize: 14, color: THEME.textSecondary }}>Clean Timer</span>
              </div>
              <span
                style={{
                  fontSize: 22,
                  fontWeight: 800,
                  color: isStarted ? THEME.textPrimary : THEME.textMuted,
                  fontVariantNumeric: "tabular-nums",
                }}
              >
                {minutesStr}:{secondsStr}
              </span>
            </div>

            {/* Checklist Items */}
            <div style={{ display: "flex", flexDirection: "column", gap: 10, marginTop: 4 }}>
              {/* Item 1 */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "10px 14px",
                  borderRadius: 12,
                  backgroundColor: item1Done ? "rgba(34, 197, 94, 0.12)" : "rgba(255,255,255,0.03)",
                  border: `1px solid ${item1Done ? "rgba(34, 197, 94, 0.4)" : THEME.border}`,
                }}
              >
                <CheckSquareIcon size={20} color={item1Done ? "#22C55E" : THEME.textMuted} />
                <span
                  style={{
                    fontSize: 15,
                    fontWeight: 600,
                    color: item1Done ? THEME.textPrimary : THEME.textSecondary,
                    textDecoration: item1Done ? "line-through" : "none",
                  }}
                >
                  Bed made with fresh linens
                </span>
              </div>

              {/* Item 2 */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "10px 14px",
                  borderRadius: 12,
                  backgroundColor: item2Done ? "rgba(34, 197, 94, 0.12)" : "rgba(255,255,255,0.03)",
                  border: `1px solid ${item2Done ? "rgba(34, 197, 94, 0.4)" : THEME.border}`,
                }}
              >
                <CheckSquareIcon size={20} color={item2Done ? "#22C55E" : THEME.textMuted} />
                <span
                  style={{
                    fontSize: 15,
                    fontWeight: 600,
                    color: item2Done ? THEME.textPrimary : THEME.textSecondary,
                    textDecoration: item2Done ? "line-through" : "none",
                  }}
                >
                  Bathroom sanitized & scrubbed
                </span>
              </div>

              {/* Item 3 */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "10px 14px",
                  borderRadius: 12,
                  backgroundColor: item3Done ? "rgba(34, 197, 94, 0.12)" : "rgba(255,255,255,0.03)",
                  border: `1px solid ${item3Done ? "rgba(34, 197, 94, 0.4)" : THEME.border}`,
                }}
              >
                <CheckSquareIcon size={20} color={item3Done ? "#22C55E" : THEME.textMuted} />
                <span
                  style={{
                    fontSize: 15,
                    fontWeight: 600,
                    color: item3Done ? THEME.textPrimary : THEME.textSecondary,
                    textDecoration: item3Done ? "line-through" : "none",
                  }}
                >
                  Towels replaced (4 sets)
                </span>
              </div>

              {/* Item 4 */}
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  padding: "10px 14px",
                  borderRadius: 12,
                  backgroundColor: item4Done ? "rgba(34, 197, 94, 0.12)" : "rgba(255,255,255,0.03)",
                  border: `1px solid ${item4Done ? "rgba(34, 197, 94, 0.4)" : THEME.border}`,
                }}
              >
                <CheckSquareIcon size={20} color={item4Done ? "#22C55E" : THEME.textMuted} />
                <span
                  style={{
                    fontSize: 15,
                    fontWeight: 600,
                    color: item4Done ? THEME.textPrimary : THEME.textSecondary,
                    textDecoration: item4Done ? "line-through" : "none",
                  }}
                >
                  Amenities & coffee restocked
                </span>
              </div>
            </div>

            {/* Action Buttons: START vs DONE */}
            {!isStarted ? (
              <div
                style={{
                  transform: `scale(${startTapScale})`,
                  backgroundColor: THEME.accentTeal,
                  color: "#0F172A",
                  borderRadius: 16,
                  padding: "16px 0",
                  textAlign: "center",
                  fontSize: 20,
                  fontWeight: 800,
                  boxShadow: "0 10px 25px rgba(20, 184, 166, 0.4)",
                  marginTop: 6,
                }}
              >
                Tap to Start Cleaning
              </div>
            ) : (
              <div
                style={{
                  transform: `scale(${doneTapScale})`,
                  backgroundColor: isCompleted ? "#22C55E" : THEME.status.cleaning.color,
                  color: "#0F172A",
                  borderRadius: 16,
                  padding: "16px 0",
                  textAlign: "center",
                  fontSize: 22,
                  fontWeight: 800,
                  boxShadow: isCompleted
                    ? "0 10px 25px rgba(34, 197, 94, 0.4)"
                    : "0 10px 25px rgba(245, 158, 11, 0.4)",
                  marginTop: 6,
                }}
              >
                {isCompleted ? `${currentLang.text} ✓` : "Tap when Done"}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
