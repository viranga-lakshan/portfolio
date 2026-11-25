import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { MousePointerIcon } from "../icons";

export const Scene5Inspection: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene5_vo.mp3");
  const clickSrc = staticFile("assets/sfx_click.wav");
  const chimeSrc = staticFile("assets/sfx_chime.wav");

  // Entrance spring
  const enterSpring = spring({
    frame: frame - 6,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });
  const enterY = interpolate(enterSpring, [0, 1], [30, 0]);
  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Tap "Pass" at frame 45
  const isTappingPass = frame >= 40 && frame <= 52;
  const passScale = isTappingPass
    ? interpolate(frame, [40, 46, 52], [1, 0.9, 1])
    : 1.0;
  const isPassed = frame >= 46;

  // Green glow ripple on Room 203
  const passedGlow = isPassed ? Math.sin((frame - 46) * 0.15) * 12 + 25 : 0;

  // Cursor coordinates gliding to Pass button (around 450, 680)
  const cursorX = interpolate(
    frame,
    [10, 44, 60, 120],
    [700, 360, 360, 600],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const cursorY = interpolate(
    frame,
    [10, 44, 60, 120],
    [500, 680, 680, 500],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  // Exit transition (last 15 frames)
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
        padding: "30px 100px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />
      {frame === 46 && <Audio src={clickSrc} volume={0.4} />}
      {frame === 47 && <Audio src={chimeSrc} volume={0.5} />}

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 32,
          transform: `translateY(${enterY}px)`,
          opacity: enterOpacity,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "6px 22px",
            borderRadius: 30,
            backgroundColor: "rgba(168, 85, 247, 0.15)",
            border: `1.5px solid ${THEME.status.toInspect.color}`,
            color: THEME.status.toInspect.color,
            fontSize: 18,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 12,
          }}
        >
          <span
            style={{
              width: 9,
              height: 9,
              borderRadius: "50%",
              backgroundColor: THEME.status.toInspect.color,
              boxShadow: "0 0 10px #A855F7",
            }}
          />
          Supervisor Quality Control
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            fontSize: 60,
            color: THEME.textPrimary,
            margin: 0,
            letterSpacing: "-0.03em",
          }}
        >
          Inspected. Ready to sell. <br />
          <span style={{ color: THEME.status.ready.color }}>Front desk knows instantly.</span>
        </h2>
      </div>

      {/* Interactive Split View */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 50,
          width: "100%",
          maxWidth: 1600,
          transform: `translateY(${enterY}px)`,
          opacity: enterOpacity,
          position: "relative",
        }}
      >
        {/* Left: Supervisor Inspection Card matching Proposal Page 3 */}
        <div
          style={{
            flex: 1,
            backgroundColor: "#FFFFFF",
            borderRadius: 26,
            border: `2px solid ${isPassed ? THEME.status.ready.color : "#E2E8F0"}`,
            padding: 34,
            boxShadow: isPassed
              ? `0 25px 60px rgba(34, 197, 94, 0.35)`
              : "0 25px 50px rgba(0,0,0,0.35)",
            position: "relative",
            color: "#0F172A",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <div>
              <div style={{ fontSize: 14, color: "#64748B", fontWeight: 700, letterSpacing: "0.05em", textTransform: "uppercase" }}>
                Supervisor · Inspection
              </div>
              <div style={{ fontSize: 38, fontWeight: 800, color: "#0F172A", marginTop: 2 }}>
                Room 203
              </div>
            </div>

            <div
              style={{
                backgroundColor: isPassed ? THEME.status.ready.bgPastel : THEME.status.toInspect.bgPastel,
                border: `1.5px solid ${isPassed ? THEME.status.ready.borderPastel : THEME.status.toInspect.borderPastel}`,
                color: isPassed ? THEME.status.ready.textDark : THEME.status.toInspect.textDark,
                padding: "8px 18px",
                borderRadius: 16,
                fontSize: 18,
                fontWeight: 700,
                display: "flex",
                alignItems: "center",
                gap: 8,
              }}
            >
              <span
                style={{
                  width: 9,
                  height: 9,
                  borderRadius: "50%",
                  backgroundColor: isPassed ? THEME.status.ready.dot : THEME.status.toInspect.dot,
                }}
              />
              {isPassed ? "PASSED (100% Score)" : "Waiting Inspection"}
            </div>
          </div>

          {/* Photo Verification Pills matching Proposal Page 3 */}
          <div style={{ marginTop: 24 }}>
            <div style={{ fontSize: 15, fontWeight: 600, color: "#475569", marginBottom: 12 }}>
              Housekeeper Photo Proof:
            </div>
            <div style={{ display: "flex", gap: 16 }}>
              <div
                style={{
                  flex: 1,
                  height: 140,
                  backgroundColor: "#F8FAFC",
                  border: "1.5px solid #E2E8F0",
                  borderRadius: 16,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: 8,
                }}
              >
                <div style={{ fontSize: 32 }}>🛏️</div>
                <div style={{ fontSize: 16, fontWeight: 700, color: "#1E293B" }}>Bed photo</div>
                <div style={{ fontSize: 12, color: "#10B981", fontWeight: 600 }}>Verified sharp</div>
              </div>
              <div
                style={{
                  flex: 1,
                  height: 140,
                  backgroundColor: "#F8FAFC",
                  border: "1.5px solid #E2E8F0",
                  borderRadius: 16,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: 8,
                }}
              >
                <div style={{ fontSize: 32 }}>🚿</div>
                <div style={{ fontSize: 16, fontWeight: 700, color: "#1E293B" }}>Bathroom photo</div>
                <div style={{ fontSize: 12, color: "#10B981", fontWeight: 600 }}>Verified clean</div>
              </div>
            </div>
          </div>

          {/* Action Buttons matching Proposal Page 3 */}
          <div style={{ display: "flex", gap: 16, marginTop: 28 }}>
            <div
              style={{
                flex: 1.2,
                backgroundColor: "#10B981",
                color: "#FFFFFF",
                textAlign: "center",
                padding: "16px 0",
                borderRadius: 16,
                fontWeight: 800,
                fontSize: 20,
                transform: `scale(${passScale})`,
                boxShadow: isPassed ? "0 10px 30px rgba(16, 185, 129, 0.45)" : "none",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                gap: 8,
              }}
            >
              <span>{isPassed ? "Passed ✓" : "Pass Room"}</span>
            </div>

            <div
              style={{
                flex: 1,
                backgroundColor: "#FFFFFF",
                color: "#EF4444",
                border: "2px solid #FECACA",
                textAlign: "center",
                padding: "16px 0",
                borderRadius: 16,
                fontWeight: 700,
                fontSize: 18,
              }}
            >
              Send back
            </div>
          </div>
        </div>

        {/* Right: Instant Front Desk Live Board Update */}
        <div
          style={{
            flex: 1,
            backgroundColor: "#FFFFFF",
            borderRadius: 26,
            border: "1.5px solid #E2E8F0",
            padding: 34,
            boxShadow: "0 25px 50px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
            <div>
              <div style={{ fontSize: 14, color: "#64748B", fontWeight: 700, textTransform: "uppercase" }}>
                Front Desk Live Sync
              </div>
              <div style={{ fontSize: 26, fontWeight: 800, color: "#0F172A", marginTop: 2 }}>
                Instant Board Reflection
              </div>
            </div>
            <div
              style={{
                backgroundColor: isPassed ? "#ECFDF5" : "#F1F5F9",
                color: isPassed ? "#059669" : "#64748B",
                fontWeight: 700,
                fontSize: 15,
                padding: "6px 14px",
                borderRadius: 20,
              }}
            >
              {isPassed ? "SYNCED INSTANTLY" : "LISTENING..."}
            </div>
          </div>

          {/* Room 203 Focused Live Tile */}
          <div
            style={{
              backgroundColor: isPassed ? THEME.status.ready.bgPastel : THEME.status.toInspect.bgPastel,
              border: `2.5px solid ${isPassed ? THEME.status.ready.color : THEME.status.toInspect.color}`,
              borderRadius: 22,
              padding: "28px 32px",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              boxShadow: isPassed ? `0 15px ${passedGlow}px rgba(34, 197, 94, 0.4)` : "none",
              transition: "all 0.3s ease",
            }}
          >
            <div>
              <div style={{ fontSize: 44, fontWeight: 900, color: "#1E293B" }}>
                Room 203
              </div>
              <div style={{ fontSize: 18, color: "#64748B", fontWeight: 600, marginTop: 4 }}>
                Floor 2 · King Suite
              </div>
            </div>

            <div style={{ textAlign: "right" }}>
              <div
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: 8,
                  fontSize: 24,
                  fontWeight: 800,
                  color: isPassed ? THEME.status.ready.textDark : THEME.status.toInspect.textDark,
                }}
              >
                <span
                  style={{
                    width: 12,
                    height: 12,
                    borderRadius: "50%",
                    backgroundColor: isPassed ? THEME.status.ready.dot : THEME.status.toInspect.dot,
                  }}
                />
                {isPassed ? "Ready to sell" : "To inspect"}
              </div>
              <div style={{ fontSize: 15, color: isPassed ? "#059669" : "#64748B", fontWeight: 600, marginTop: 4 }}>
                {isPassed ? "Guest Check-in Unlocked ✓" : "Supervisor in room"}
              </div>
            </div>
          </div>

          {/* Surrounding Context Tiles (201, 202, 204) */}
          <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 14, marginTop: 18 }}>
            <div style={{ backgroundColor: THEME.status.cleaning.bgPastel, padding: "14px 16px", borderRadius: 14, border: `1px solid ${THEME.status.cleaning.borderPastel}` }}>
              <div style={{ fontSize: 20, fontWeight: 800, color: "#1E293B" }}>201</div>
              <div style={{ fontSize: 13, color: THEME.status.cleaning.textDark, fontWeight: 700 }}>● Cleaning</div>
            </div>
            <div style={{ backgroundColor: THEME.status.ready.bgPastel, padding: "14px 16px", borderRadius: 14, border: `1px solid ${THEME.status.ready.borderPastel}` }}>
              <div style={{ fontSize: 20, fontWeight: 800, color: "#1E293B" }}>202</div>
              <div style={{ fontSize: 13, color: THEME.status.ready.textDark, fontWeight: 700 }}>● Ready</div>
            </div>
            <div style={{ backgroundColor: THEME.status.assigned.bgPastel, padding: "14px 16px", borderRadius: 14, border: `1px solid ${THEME.status.assigned.borderPastel}` }}>
              <div style={{ fontSize: 20, fontWeight: 800, color: "#1E293B" }}>204</div>
              <div style={{ fontSize: 13, color: THEME.status.assigned.textDark, fontWeight: 700 }}>● Assigned</div>
            </div>
          </div>
        </div>

        {/* Mouse Pointer */}
        <div
          style={{
            position: "absolute",
            left: cursorX,
            top: cursorY,
            pointerEvents: "none",
            zIndex: 100,
          }}
        >
          <MousePointerIcon size={34} color={THEME.accentTeal} />
        </div>
      </div>
    </div>
  );
};
