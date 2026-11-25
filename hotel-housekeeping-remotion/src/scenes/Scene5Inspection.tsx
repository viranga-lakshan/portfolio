import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { ReadyIcon, ToInspectIcon, CheckSquareIcon, AssignedIcon } from "../icons";

export const Scene5Inspection: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene5_vo.mp3");

  // Entrance spring for split view
  const enterSpring = spring({
    frame: frame - 5,
    fps,
    config: { damping: 16, mass: 0.8, stiffness: 100 },
  });
  const enterY = interpolate(enterSpring, [0, 1], [40, 0]);
  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Tap "Pass" at frame 50
  const isTappingPass = frame >= 46 && frame <= 60;
  const passScale = isTappingPass
    ? interpolate(frame, [46, 52, 60], [1, 0.9, 1])
    : 1.0;
  const isPassed = frame >= 52;

  // Green glow ripple on Room 203
  const passedGlow = isPassed ? Math.sin((frame - 52) * 0.2) * 10 + 25 : 0;

  // Exit transition
  const exitOpacity = interpolate(frame, [225, 240], [1, 0], {
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
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "40px 100px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 36,
          transform: `translateY(${enterY}px)`,
          opacity: enterOpacity,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "8px 22px",
            borderRadius: 30,
            backgroundColor: "rgba(168, 85, 247, 0.15)",
            border: `1px solid ${THEME.status.toInspect.color}`,
            color: THEME.status.toInspect.color,
            fontSize: 22,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 16,
          }}
        >
          Supervisor Quality Control
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            fontSize: 66,
            color: THEME.textPrimary,
            margin: 0,
          }}
        >
          Inspected. Ready to sell. <br />
          <span style={{ color: THEME.status.ready.color }}>Front desk knows instantly.</span>
        </h2>
      </div>

      {/* Interactive Split View: Left (Supervisor Pass Screen) & Right (Live Board Update) */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 60,
          width: "100%",
          maxWidth: 1600,
          transform: `translateY(${enterY}px)`,
          opacity: enterOpacity,
        }}
      >
        {/* Left Card: Supervisor Inspection Card */}
        <div
          style={{
            flex: 1,
            backgroundColor: THEME.surface,
            borderRadius: 28,
            border: `2px solid ${isPassed ? THEME.status.ready.color : THEME.border}`,
            padding: 36,
            boxShadow: isPassed
              ? `0 20px 60px rgba(34, 197, 94, 0.35)`
              : "0 20px 50px rgba(0,0,0,0.5)",
            position: "relative",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <div>
              <div style={{ fontSize: 18, color: THEME.textSecondary, fontWeight: 600 }}>
                Inspection Queue
              </div>
              <div style={{ fontSize: 44, fontWeight: 800, color: THEME.textPrimary }}>
                Room 203
              </div>
            </div>
            <div
              style={{
                backgroundColor: isPassed ? THEME.status.ready.bg : THEME.status.toInspect.bg,
                border: `2px solid ${isPassed ? THEME.status.ready.color : THEME.status.toInspect.color}`,
                color: isPassed ? THEME.status.ready.color : THEME.status.toInspect.color,
                padding: "8px 20px",
                borderRadius: 20,
                fontSize: 20,
                fontWeight: 800,
                display: "flex",
                alignItems: "center",
                gap: 8,
              }}
            >
              {isPassed ? <ReadyIcon size={22} color="#22C55E" /> : <ToInspectIcon size={22} color="#A855F7" />}
              {isPassed ? "Ready to Sell" : "Waiting Inspection"}
            </div>
          </div>

          {/* Housekeeper metadata & score */}
          <div
            style={{
              margin: "24px 0",
              padding: 20,
              borderRadius: 18,
              backgroundColor: "#0F172A",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <div style={{ fontSize: 14, color: THEME.textMuted }}>Cleaned By</div>
              <div style={{ fontSize: 22, fontWeight: 700, color: THEME.textPrimary }}>
                Sara Perera (Housekeeper #4)
              </div>
            </div>

            <div style={{ textAlign: "right" }}>
              <div style={{ fontSize: 14, color: THEME.textMuted }}>Inspection Score</div>
              <div style={{ fontSize: 26, fontWeight: 800, color: THEME.status.ready.color }}>
                100% (All Items Passed)
              </div>
            </div>
          </div>

          {/* Action Buttons: Pass vs Send Back */}
          <div style={{ display: "flex", gap: 18 }}>
            <div
              style={{
                flex: 1,
                transform: `scale(${passScale})`,
                backgroundColor: isPassed ? THEME.status.ready.color : "#16A34A",
                color: "#FFFFFF",
                borderRadius: 18,
                padding: "18px 0",
                textAlign: "center",
                fontSize: 24,
                fontWeight: 800,
                cursor: "pointer",
                boxShadow: isPassed
                  ? `0 0 ${passedGlow}px rgba(34, 197, 94, 0.8)`
                  : "0 10px 25px rgba(22, 163, 74, 0.4)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: 12,
              }}
            >
              <CheckSquareIcon size={28} color="#FFFFFF" />
              {isPassed ? "PASSED & APPROVED ✓" : "Tap to PASS"}
            </div>

            <div
              style={{
                width: 170,
                backgroundColor: "rgba(239, 68, 68, 0.12)",
                border: "2px solid rgba(239, 68, 68, 0.4)",
                color: "#EF4444",
                borderRadius: 18,
                padding: "18px 0",
                textAlign: "center",
                fontSize: 20,
                fontWeight: 700,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                opacity: isPassed ? 0.35 : 1,
              }}
            >
              Send Back
            </div>
          </div>
        </div>

        {/* Right Card: Front Desk Live Board Immediate Sync */}
        <div
          style={{
            flex: 1,
            backgroundColor: THEME.surface,
            borderRadius: 28,
            border: `2px solid ${THEME.border}`,
            padding: 36,
            boxShadow: "0 20px 50px rgba(0,0,0,0.5)",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
            <div>
              <div style={{ fontSize: 18, color: THEME.textSecondary, fontWeight: 600 }}>
                Front Desk Terminal
              </div>
              <div style={{ fontSize: 32, fontWeight: 800, color: THEME.textPrimary }}>
                Instant Board Sync (0ms delay)
              </div>
            </div>
            <div
              style={{
                padding: "6px 14px",
                borderRadius: 20,
                backgroundColor: "rgba(34, 197, 94, 0.15)",
                color: THEME.status.ready.color,
                fontSize: 16,
                fontWeight: 700,
              }}
            >
              Live Socket Connected
            </div>
          </div>

          {/* Mini Room Grid Highlight */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(3, 1fr)",
              gap: 16,
              marginBottom: 24,
            }}
          >
            {/* Room 201 */}
            <div
              style={{
                backgroundColor: THEME.status.ready.bg,
                border: `2px solid ${THEME.status.ready.color}`,
                borderRadius: 16,
                padding: 16,
              }}
            >
              <div style={{ fontSize: 24, fontWeight: 800, color: THEME.textPrimary }}>201</div>
              <div style={{ display: "flex", alignItems: "center", gap: 6, color: THEME.status.ready.color, fontSize: 15, fontWeight: 700 }}>
                <ReadyIcon size={18} color={THEME.status.ready.color} /> Ready
              </div>
            </div>

            {/* Room 202 */}
            <div
              style={{
                backgroundColor: THEME.status.assigned.bg,
                border: `2px solid ${THEME.status.assigned.color}`,
                borderRadius: 16,
                padding: 16,
              }}
            >
              <div style={{ fontSize: 24, fontWeight: 800, color: THEME.textPrimary }}>202</div>
              <div style={{ display: "flex", alignItems: "center", gap: 6, color: THEME.status.assigned.color, fontSize: 15, fontWeight: 700 }}>
                <AssignedIcon size={18} color={THEME.status.assigned.color} /> Assigned
              </div>
            </div>

            {/* Room 203 — The Hero Room that turns Green! */}
            <div
              style={{
                backgroundColor: isPassed ? THEME.status.ready.bg : THEME.status.toInspect.bg,
                border: `3px solid ${isPassed ? THEME.status.ready.color : THEME.status.toInspect.color}`,
                borderRadius: 16,
                padding: 16,
                boxShadow: isPassed ? `0 0 30px rgba(34, 197, 94, 0.7)` : "none",
                transform: isPassed ? "scale(1.05)" : "scale(1.0)",
              }}
            >
              <div style={{ fontSize: 24, fontWeight: 800, color: THEME.textPrimary }}>203</div>
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 6,
                  color: isPassed ? THEME.status.ready.color : THEME.status.toInspect.color,
                  fontSize: 15,
                  fontWeight: 700,
                }}
              >
                {isPassed ? <ReadyIcon size={18} color="#22C55E" /> : <ToInspectIcon size={18} color="#A855F7" />}
                {isPassed ? "Ready to Sell" : "To Inspect"}
              </div>
            </div>
          </div>

          {/* Front Desk Notification Banner */}
          <div
            style={{
              padding: "16px 20px",
              borderRadius: 16,
              backgroundColor: isPassed ? "rgba(34, 197, 94, 0.2)" : "rgba(255,255,255,0.05)",
              border: `1px solid ${isPassed ? THEME.status.ready.color : THEME.border}`,
              display: "flex",
              alignItems: "center",
              gap: 16,
            }}
          >
            <ReadyIcon size={28} color={isPassed ? "#22C55E" : THEME.textMuted} />
            <div>
              <div style={{ fontSize: 18, fontWeight: 700, color: THEME.textPrimary }}>
                {isPassed ? "Notification: Room 203 Ready for Guest Check-in" : "Listening for supervisor approvals..."}
              </div>
              <div style={{ fontSize: 14, color: THEME.textSecondary }}>
                {isPassed ? "Front desk staff can assign guest keycard immediately." : "Updates broadcast live across all screens."}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
