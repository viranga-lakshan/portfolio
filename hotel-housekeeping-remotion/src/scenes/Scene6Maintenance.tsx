import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { BellIcon, WrenchIcon, CheckCircleSolidIcon } from "../icons";

export const Scene6Maintenance: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene6_vo.mp3");
  const popSrc = staticFile("assets/sfx_pop.wav");

  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Stepper state: Open (frame 0-60) -> In progress (frame 60-110) -> Fixed (frame 110+)
  const isInProgress = frame >= 60 && frame < 110;
  const isFixed = frame >= 110;

  // Push notifications slide-ins
  const notif1 = spring({ frame: frame - 25, fps, config: THEME.springs.gentle });
  const notif2 = spring({ frame: frame - 65, fps, config: THEME.springs.gentle });
  const notif3 = spring({ frame: frame - 110, fps, config: THEME.springs.gentle });

  const n1X = interpolate(notif1, [0, 1], [300, 0]);
  const n2X = interpolate(notif2, [0, 1], [300, 0]);
  const n3X = interpolate(notif3, [0, 1], [300, 0]);

  // Exit transition (last 15 frames)
  const exitOpacity = interpolate(frame, [165, 180], [1, 0], {
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
      {(frame === 25 || frame === 65 || frame === 110) && (
        <Audio src={popSrc} volume={0.35} />
      )}

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 36,
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
            backgroundColor: "rgba(245, 158, 11, 0.15)",
            border: `1.5px solid ${THEME.status.cleaning.color}`,
            color: THEME.status.cleaning.color,
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
              backgroundColor: THEME.status.cleaning.color,
              boxShadow: "0 0 10px #F59E0B",
            }}
          />
          Engineering & Smart Alerts
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
          Repairs tracked. <span style={{ color: THEME.accentTeal }}>Nothing forgotten.</span>
        </h2>
      </div>

      {/* Split View: Left (Maintenance Request Card) & Right (Push Notifications) */}
      <div
        style={{
          display: "flex",
          gap: 50,
          width: "100%",
          maxWidth: 1600,
          opacity: enterOpacity,
        }}
      >
        {/* Left: Maintenance Ticket matching Proposal Page 3 */}
        <div
          style={{
            flex: 1.1,
            backgroundColor: "#FFFFFF",
            borderRadius: 26,
            border: `2px solid ${isFixed ? "#10B981" : "#E2E8F0"}`,
            padding: 34,
            boxShadow: isFixed
              ? "0 25px 60px rgba(16, 185, 129, 0.3)"
              : "0 25px 50px rgba(0,0,0,0.35)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            color: "#0F172A",
          }}
        >
          <div>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div
                  style={{
                    backgroundColor: "rgba(245, 158, 11, 0.15)",
                    padding: 10,
                    borderRadius: 14,
                  }}
                >
                  <WrenchIcon size={28} color="#D97706" />
                </div>
                <div>
                  <div style={{ fontSize: 13, color: "#64748B", fontWeight: 700, textTransform: "uppercase" }}>
                    Maintenance Request
                  </div>
                  <div style={{ fontSize: 32, fontWeight: 800, color: "#0F172A" }}>
                    AC not cooling · Room 305
                  </div>
                </div>
              </div>

              <div
                style={{
                  backgroundColor: isFixed ? "#ECFDF5" : "#FEF2F2",
                  color: isFixed ? "#065F46" : "#991B1B",
                  fontWeight: 700,
                  fontSize: 16,
                  padding: "6px 16px",
                  borderRadius: 16,
                }}
              >
                {isFixed ? "RESOLVED ✓" : "URGENT"}
              </div>
            </div>

            <div style={{ fontSize: 16, color: "#475569", fontWeight: 500, marginTop: 14 }}>
              Reported by Sara with photo · Urgent · Engineering Team
            </div>

            {/* Stepper matching Proposal Page 3 */}
            <div style={{ marginTop: 28 }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#64748B", textTransform: "uppercase", marginBottom: 12 }}>
                Resolution Progress:
              </div>
              <div style={{ display: "flex", gap: 12 }}>
                {/* Step 1: Open */}
                <div
                  style={{
                    flex: 1,
                    padding: "12px",
                    borderRadius: 14,
                    textAlign: "center",
                    backgroundColor: "#F1F5F9",
                    color: "#475569",
                    fontWeight: 700,
                    fontSize: 16,
                    border: "1.5px solid #CBD5E1",
                  }}
                >
                  1. Open
                </div>

                {/* Step 2: In Progress */}
                <div
                  style={{
                    flex: 1,
                    padding: "12px",
                    borderRadius: 14,
                    textAlign: "center",
                    backgroundColor: isInProgress ? "#FFFBEB" : isFixed ? "#ECFDF5" : "#F8FAFC",
                    color: isInProgress ? "#92400E" : isFixed ? "#065F46" : "#94A3B8",
                    fontWeight: 700,
                    fontSize: 16,
                    border: `1.5px solid ${isInProgress ? "#FDE68A" : isFixed ? "#A7F3D0" : "#E2E8F0"}`,
                  }}
                >
                  2. In progress
                </div>

                {/* Step 3: Fixed */}
                <div
                  style={{
                    flex: 1,
                    padding: "12px",
                    borderRadius: 14,
                    textAlign: "center",
                    backgroundColor: isFixed ? "#ECFDF5" : "#F8FAFC",
                    color: isFixed ? "#065F46" : "#94A3B8",
                    fontWeight: 700,
                    fontSize: 16,
                    border: `1.5px solid ${isFixed ? "#A7F3D0" : "#E2E8F0"}`,
                  }}
                >
                  3. Fixed ✓
                </div>
              </div>
            </div>
          </div>

          {/* Proposal Bottom Notice */}
          <div
            style={{
              marginTop: 24,
              padding: "14px 18px",
              borderRadius: 14,
              backgroundColor: isFixed ? "#ECFDF5" : "#F8FAFC",
              border: `1px solid ${isFixed ? "#A7F3D0" : "#E2E8F0"}`,
              fontSize: 15,
              color: isFixed ? "#065F46" : "#64748B",
              fontWeight: 600,
            }}
          >
            {isFixed
              ? "✓ Room 305 automatically returned to service & ready to sell!"
              : "Room set Out of Order automatically until fixed, then returned to service."}
          </div>
        </div>

        {/* Right: Instant Push Alerts Feed */}
        <div
          style={{
            flex: 0.9,
            display: "flex",
            flexDirection: "column",
            gap: 16,
            justifyContent: "center",
          }}
        >
          {/* Alert 1 */}
          <div
            style={{
              transform: `translateX(${n1X}px)`,
              opacity: notif1,
              backgroundColor: "#1E293B",
              borderRadius: 20,
              padding: "18px 24px",
              border: "1.5px solid #334155",
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
              display: "flex",
              alignItems: "center",
              gap: 18,
            }}
          >
            <div
              style={{
                width: 48,
                height: 48,
                borderRadius: 14,
                backgroundColor: "rgba(16, 185, 129, 0.2)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <CheckCircleSolidIcon size={28} color="#10B981" />
            </div>
            <div>
              <div style={{ fontSize: 13, color: THEME.accentTeal, fontWeight: 700, textTransform: "uppercase" }}>
                Front Desk Notification
              </div>
              <div style={{ fontSize: 18, fontWeight: 700, color: "#FFFFFF", marginTop: 2 }}>
                Room 204 is Ready to sell
              </div>
              <div style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>
                Passed inspection · Floor 2 unlocked
              </div>
            </div>
          </div>

          {/* Alert 2 */}
          <div
            style={{
              transform: `translateX(${n2X}px)`,
              opacity: notif2,
              backgroundColor: "#1E293B",
              borderRadius: 20,
              padding: "18px 24px",
              border: "1.5px solid #334155",
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
              display: "flex",
              alignItems: "center",
              gap: 18,
            }}
          >
            <div
              style={{
                width: 48,
                height: 48,
                borderRadius: 14,
                backgroundColor: "rgba(239, 68, 68, 0.2)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <BellIcon size={26} color="#EF4444" />
            </div>
            <div>
              <div style={{ fontSize: 13, color: "#F87171", fontWeight: 700, textTransform: "uppercase" }}>
                Supervisor Alert
              </div>
              <div style={{ fontSize: 18, fontWeight: 700, color: "#FFFFFF", marginTop: 2 }}>
                Room 310 Failed Inspection
              </div>
              <div style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>
                Returned to housekeeper: Extra bath towels required
              </div>
            </div>
          </div>

          {/* Alert 3 */}
          <div
            style={{
              transform: `translateX(${n3X}px)`,
              opacity: notif3,
              backgroundColor: "#1E293B",
              borderRadius: 20,
              padding: "18px 24px",
              border: "1.5px solid #334155",
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
              display: "flex",
              alignItems: "center",
              gap: 18,
            }}
          >
            <div
              style={{
                width: 48,
                height: 48,
                borderRadius: 14,
                backgroundColor: "rgba(20, 184, 166, 0.2)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <WrenchIcon size={26} color="#14B8A6" />
            </div>
            <div>
              <div style={{ fontSize: 13, color: THEME.accentTeal, fontWeight: 700, textTransform: "uppercase" }}>
                Maintenance Alert
              </div>
              <div style={{ fontSize: 18, fontWeight: 700, color: "#FFFFFF", marginTop: 2 }}>
                New Repair: Shower Leak · Room 112
              </div>
              <div style={{ fontSize: 13, color: "#94A3B8", marginTop: 2 }}>
                Assigned to Engineering · Normal Priority
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
