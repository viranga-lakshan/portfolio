import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { ReadyIcon, TimerIcon, ToInspectIcon, WrenchIcon } from "../icons";

export const Scene7Dashboard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene7_vo.mp3");

  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Stat Card Springs
  const c1Spring = spring({ frame: frame - 10, fps, config: THEME.springs.bouncy });
  const c2Spring = spring({ frame: frame - 22, fps, config: THEME.springs.bouncy });
  const c3Spring = spring({ frame: frame - 34, fps, config: THEME.springs.bouncy });
  const c4Spring = spring({ frame: frame - 46, fps, config: THEME.springs.bouncy });

  // Animated Numbers count up
  const roomsReady = Math.floor(
    interpolate(frame, [15, 85], [0, 42], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const cleanTime = Math.floor(
    interpolate(frame, [25, 95], [45, 24], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const passRate = Math.floor(
    interpolate(frame, [35, 105], [70, 96], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const openRepairs = Math.floor(
    interpolate(frame, [45, 115], [8, 2], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  // Bottom feature chips springs
  const chip1 = spring({ frame: frame - 60, fps, config: THEME.springs.bouncy });
  const chip2 = spring({ frame: frame - 75, fps, config: THEME.springs.bouncy });
  const chip3 = spring({ frame: frame - 90, fps, config: THEME.springs.bouncy });
  const chip4 = spring({ frame: frame - 105, fps, config: THEME.springs.bouncy });

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
          marginBottom: 44,
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
            backgroundColor: "rgba(20, 184, 166, 0.15)",
            border: `1px solid ${THEME.accentTeal}`,
            color: THEME.accentTeal,
            fontSize: 22,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 16,
          }}
        >
          General Manager & Owner Analytics
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            fontSize: 66,
            color: THEME.textPrimary,
            margin: 0,
          }}
        >
          Your whole hotel <span style={{ color: THEME.accentTeal }}>on one screen.</span>
        </h2>
      </div>

      {/* 4 Animated Metric Cards */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 28,
          width: "100%",
          maxWidth: 1640,
          marginBottom: 48,
        }}
      >
        {/* Card 1: Rooms Ready */}
        <div
          style={{
            transform: `scale(${c1Spring})`,
            backgroundColor: THEME.surface,
            borderRadius: 24,
            border: `2px solid ${THEME.status.ready.border}`,
            padding: 32,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 20, color: THEME.textSecondary, fontWeight: 600 }}>
              Rooms Ready
            </span>
            <div
              style={{
                backgroundColor: THEME.status.ready.bg,
                padding: 10,
                borderRadius: 14,
              }}
            >
              <ReadyIcon size={26} color="#22C55E" />
            </div>
          </div>
          <div style={{ marginTop: 20 }}>
            <div
              style={{
                fontSize: 68,
                fontWeight: 800,
                color: THEME.status.ready.color,
                lineHeight: 1,
                fontVariantNumeric: "tabular-nums",
              }}
            >
              {roomsReady}
            </div>
            <div style={{ fontSize: 16, color: THEME.textSecondary, marginTop: 10 }}>
              Out of 48 total keys (88%)
            </div>
          </div>
        </div>

        {/* Card 2: Avg Clean Time */}
        <div
          style={{
            transform: `scale(${c2Spring})`,
            backgroundColor: THEME.surface,
            borderRadius: 24,
            border: `2px solid ${THEME.accentTeal}`,
            padding: 32,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 20, color: THEME.textSecondary, fontWeight: 600 }}>
              Avg Clean Time
            </span>
            <div
              style={{
                backgroundColor: "rgba(20, 184, 166, 0.2)",
                padding: 10,
                borderRadius: 14,
              }}
            >
              <TimerIcon size={26} color={THEME.accentTeal} />
            </div>
          </div>
          <div style={{ marginTop: 20 }}>
            <div
              style={{
                fontSize: 68,
                fontWeight: 800,
                color: THEME.textPrimary,
                lineHeight: 1,
                fontVariantNumeric: "tabular-nums",
              }}
            >
              {cleanTime} <span style={{ fontSize: 32, color: THEME.textSecondary }}>min</span>
            </div>
            <div style={{ fontSize: 16, color: THEME.accentTeal, marginTop: 10 }}>
              ⚡ 21 mins faster per room
            </div>
          </div>
        </div>

        {/* Card 3: Inspection Pass Rate */}
        <div
          style={{
            transform: `scale(${c3Spring})`,
            backgroundColor: THEME.surface,
            borderRadius: 24,
            border: `2px solid ${THEME.status.toInspect.border}`,
            padding: 32,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 20, color: THEME.textSecondary, fontWeight: 600 }}>
              Inspection Pass
            </span>
            <div
              style={{
                backgroundColor: THEME.status.toInspect.bg,
                padding: 10,
                borderRadius: 14,
              }}
            >
              <ToInspectIcon size={26} color="#A855F7" />
            </div>
          </div>
          <div style={{ marginTop: 20 }}>
            <div
              style={{
                fontSize: 68,
                fontWeight: 800,
                color: THEME.status.toInspect.color,
                lineHeight: 1,
                fontVariantNumeric: "tabular-nums",
              }}
            >
              {passRate}%
            </div>
            <div style={{ fontSize: 16, color: THEME.textSecondary, marginTop: 10 }}>
              First-round compliance
            </div>
          </div>
        </div>

        {/* Card 4: Open Repairs */}
        <div
          style={{
            transform: `scale(${c4Spring})`,
            backgroundColor: THEME.surface,
            borderRadius: 24,
            border: `2px solid ${THEME.status.cleaning.border}`,
            padding: 32,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontSize: 20, color: THEME.textSecondary, fontWeight: 600 }}>
              Open Repairs
            </span>
            <div
              style={{
                backgroundColor: THEME.status.cleaning.bg,
                padding: 10,
                borderRadius: 14,
              }}
            >
              <WrenchIcon size={26} color="#F59E0B" />
            </div>
          </div>
          <div style={{ marginTop: 20 }}>
            <div
              style={{
                fontSize: 68,
                fontWeight: 800,
                color: "#F59E0B",
                lineHeight: 1,
                fontVariantNumeric: "tabular-nums",
              }}
            >
              {openRepairs}
            </div>
            <div style={{ fontSize: 16, color: THEME.textSecondary, marginTop: 10 }}>
              6 resolved today
            </div>
          </div>
        </div>
      </div>

      {/* Feature Chips Pop-In along the bottom */}
      <div
        style={{
          display: "flex",
          gap: 20,
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            transform: `scale(${chip1})`,
            padding: "14px 28px",
            borderRadius: 30,
            backgroundColor: THEME.surface,
            border: `1.5px solid ${THEME.border}`,
            color: THEME.textPrimary,
            fontSize: 22,
            fontWeight: 700,
            display: "flex",
            alignItems: "center",
            gap: 12,
            boxShadow: "0 10px 25px rgba(0,0,0,0.3)",
          }}
        >
          <span>📶</span> Works Offline
        </div>

        <div
          style={{
            transform: `scale(${chip2})`,
            padding: "14px 28px",
            borderRadius: 30,
            backgroundColor: THEME.surface,
            border: `1.5px solid ${THEME.border}`,
            color: THEME.textPrimary,
            fontSize: 22,
            fontWeight: 700,
            display: "flex",
            alignItems: "center",
            gap: 12,
            boxShadow: "0 10px 25px rgba(0,0,0,0.3)",
          }}
        >
          <span>🌐</span> Multi-Language
        </div>

        <div
          style={{
            transform: `scale(${chip3})`,
            padding: "14px 28px",
            borderRadius: 30,
            backgroundColor: THEME.surface,
            border: `1.5px solid ${THEME.border}`,
            color: THEME.textPrimary,
            fontSize: 22,
            fontWeight: 700,
            display: "flex",
            alignItems: "center",
            gap: 12,
            boxShadow: "0 10px 25px rgba(0,0,0,0.3)",
          }}
        >
          <span>📊</span> Excel & CSV Import
        </div>

        <div
          style={{
            transform: `scale(${chip4})`,
            padding: "14px 28px",
            borderRadius: 30,
            backgroundColor: THEME.surface,
            border: `1.5px solid ${THEME.border}`,
            color: THEME.textPrimary,
            fontSize: 22,
            fontWeight: 700,
            display: "flex",
            alignItems: "center",
            gap: 12,
            boxShadow: "0 10px 25px rgba(0,0,0,0.3)",
          }}
        >
          <span>📑</span> Audit Reports
        </div>
      </div>
    </div>
  );
};

