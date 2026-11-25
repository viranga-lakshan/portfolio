import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { WrenchIcon, BellIcon, ReadyIcon, DirtyIcon } from "../icons";

export const Scene6Maintenance: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene6_vo.mp3");

  // Entrance
  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Ticket status transition (Open -> In Progress -> Fixed)
  const isFixed = frame >= 110;
  const isInProgress = frame >= 50 && frame < 110;

  let statusLabel = "OPEN (Urgent)";
  let statusColor = "#EF4444";
  let statusBg = "rgba(239, 68, 68, 0.15)";
  if (isFixed) {
    statusLabel = "FIXED & VERIFIED ✓";
    statusColor = "#22C55E";
    statusBg = "rgba(34, 197, 94, 0.15)";
  } else if (isInProgress) {
    statusLabel = "IN PROGRESS (Engineering)";
    statusColor = "#F59E0B";
    statusBg = "rgba(245, 158, 11, 0.15)";
  }

  // Notification slide-in springs
  const notif1Spring = spring({ frame: frame - 25, fps, config: THEME.springs.bouncy });
  const notif2Spring = spring({ frame: frame - 65, fps, config: THEME.springs.bouncy });
  const notif3Spring = spring({ frame: frame - 110, fps, config: THEME.springs.bouncy });

  const n1X = interpolate(notif1Spring, [0, 1], [400, 0]);
  const n2X = interpolate(notif2Spring, [0, 1], [400, 0]);
  const n3X = interpolate(notif3Spring, [0, 1], [400, 0]);

  // Exit transition
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
        padding: "40px 100px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 40,
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
            backgroundColor: "rgba(245, 158, 11, 0.15)",
            border: `1px solid ${THEME.status.cleaning.color}`,
            color: THEME.status.cleaning.color,
            fontSize: 22,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 16,
          }}
        >
          Engineering & Smart Alerts
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            fontSize: 66,
            color: THEME.textPrimary,
            margin: 0,
          }}
        >
          Repairs tracked. <span style={{ color: THEME.accentTeal }}>Nothing forgotten.</span>
        </h2>
      </div>

      {/* Split Content: Left (Maintenance Issue Card) & Right (Notification Feed) */}
      <div
        style={{
          display: "flex",
          gap: 60,
          width: "100%",
          maxWidth: 1600,
          opacity: enterOpacity,
        }}
      >
        {/* Left: Maintenance Ticket */}
        <div
          style={{
            flex: 1.1,
            backgroundColor: THEME.surface,
            borderRadius: 28,
            border: `2px solid ${isFixed ? THEME.status.ready.color : THEME.border}`,
            padding: 36,
            boxShadow: isFixed
              ? "0 20px 60px rgba(34, 197, 94, 0.3)"
              : "0 20px 50px rgba(0,0,0,0.5)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
          }}
        >
          <div>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <div
                  style={{
                    backgroundColor: "rgba(245, 158, 11, 0.2)",
                    padding: 12,
                    borderRadius: 16,
                  }}
                >
                  <WrenchIcon size={28} color="#F59E0B" />
                </div>
                <div>
                  <div style={{ fontSize: 16, color: THEME.textSecondary, fontWeight: 600 }}>
                    Maintenance Ticket #1042
                  </div>
                  <div style={{ fontSize: 32, fontWeight: 800, color: THEME.textPrimary }}>
                    AC Not Cooling – Room 305
                  </div>
                </div>
              </div>

              {/* Status Badge */}
              <div
                style={{
                  backgroundColor: statusBg,
                  border: `2px solid ${statusColor}`,
                  color: statusColor,
                  padding: "8px 18px",
                  borderRadius: 20,
                  fontSize: 18,
                  fontWeight: 800,
                }}
              >
                {statusLabel}
              </div>
            </div>

            {/* Photo Attachment & Details */}
            <div
              style={{
                marginTop: 24,
                padding: 20,
                borderRadius: 20,
                backgroundColor: "#0F172A",
                display: "flex",
                gap: 20,
                alignItems: "center",
              }}
            >
              {/* Photo Thumbnail representation */}
              <div
                style={{
                  width: 130,
                  height: 100,
                  borderRadius: 14,
                  backgroundColor: "#1E293B",
                  border: "2px dashed #475569",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: 6,
                }}
              >
                <span style={{ fontSize: 26 }}>📷</span>
                <span style={{ fontSize: 12, color: THEME.textSecondary, fontWeight: 600 }}>
                  Photo Attached
                </span>
              </div>

              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 18, fontWeight: 700, color: THEME.textPrimary }}>
                  Reported by Housekeeper Nimal
                </div>
                <div style={{ fontSize: 15, color: THEME.textSecondary, marginTop: 4 }}>
                  "Thermostat error code E4. Room automatically set to Out of Order."
                </div>
                <div style={{ fontSize: 14, color: THEME.accentTeal, marginTop: 8, fontWeight: 600 }}>
                  Assigned to: Senior HVAC Technician (Kasun)
                </div>
              </div>
            </div>
          </div>

          {/* Bottom Auto Status Bar */}
          <div
            style={{
              marginTop: 24,
              padding: "14px 20px",
              borderRadius: 14,
              backgroundColor: isFixed ? "rgba(34, 197, 94, 0.15)" : "rgba(255,255,255,0.05)",
              border: `1px solid ${isFixed ? THEME.status.ready.border : THEME.border}`,
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <span style={{ fontSize: 16, color: THEME.textPrimary, fontWeight: 600 }}>
              {isFixed
                ? "Room 305 automatically restored to Available pool"
                : "Preventing double-booking while engineering repairs"}
            </span>
            <span
              style={{
                fontSize: 14,
                color: isFixed ? THEME.status.ready.color : THEME.status.dirty.color,
                fontWeight: 700,
              }}
            >
              {isFixed ? "Auto-Unlocked" : "Locked Out of Order"}
            </span>
          </div>
        </div>

        {/* Right: Live Notification Pop-up Stream */}
        <div
          style={{
            flex: 0.9,
            display: "flex",
            flexDirection: "column",
            gap: 16,
            justifyContent: "center",
          }}
        >
          {/* Notification 1 */}
          <div
            style={{
              transform: `translateX(${n1X}px)`,
              backgroundColor: THEME.surface,
              borderRadius: 20,
              border: `2px solid ${THEME.status.ready.color}`,
              padding: "20px 24px",
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
            }}
          >
            <div
              style={{
                backgroundColor: THEME.status.ready.bg,
                padding: 12,
                borderRadius: 14,
              }}
            >
              <ReadyIcon size={28} color="#22C55E" />
            </div>
            <div>
              <div style={{ fontSize: 20, fontWeight: 800, color: THEME.textPrimary }}>
                Room 204 is ready
              </div>
              <div style={{ fontSize: 15, color: THEME.textSecondary }}>
                Cleaned by Sara • Approved by Supervisor
              </div>
            </div>
          </div>

          {/* Notification 2 */}
          <div
            style={{
              transform: `translateX(${n2X}px)`,
              backgroundColor: THEME.surface,
              borderRadius: 20,
              border: `2px solid ${THEME.status.dirty.color}`,
              padding: "20px 24px",
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
            }}
          >
            <div
              style={{
                backgroundColor: THEME.status.dirty.bg,
                padding: 12,
                borderRadius: 14,
              }}
            >
              <DirtyIcon size={28} color="#EF4444" />
            </div>
            <div>
              <div style={{ fontSize: 20, fontWeight: 800, color: THEME.textPrimary }}>
                Room 310 sent back
              </div>
              <div style={{ fontSize: 15, color: THEME.textSecondary }}>
                Reason: Balcony glass needs wiping
              </div>
            </div>
          </div>

          {/* Notification 3 */}
          <div
            style={{
              transform: `translateX(${n3X}px)`,
              backgroundColor: THEME.surface,
              borderRadius: 20,
              border: `2px solid ${THEME.accentTeal}`,
              padding: "20px 24px",
              display: "flex",
              alignItems: "center",
              gap: 16,
              boxShadow: "0 15px 35px rgba(0,0,0,0.4)",
            }}
          >
            <div
              style={{
                backgroundColor: "rgba(20, 184, 166, 0.2)",
                padding: 12,
                borderRadius: 14,
              }}
            >
              <BellIcon size={28} color={THEME.accentTeal} />
            </div>
            <div>
              <div style={{ fontSize: 20, fontWeight: 800, color: THEME.textPrimary }}>
                AC fixed in 305
              </div>
              <div style={{ fontSize: 15, color: THEME.textSecondary }}>
                Repaired by Kasun • Ready for guest check-in
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

