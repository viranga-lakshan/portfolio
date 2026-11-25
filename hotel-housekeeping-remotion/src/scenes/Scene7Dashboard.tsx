import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";

export const Scene7Dashboard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene7_vo.mp3");
  const enterOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Stat Card Springs
  const c1Spring = spring({ frame: frame - 8, fps, config: THEME.springs.gentle });
  const c2Spring = spring({ frame: frame - 18, fps, config: THEME.springs.gentle });
  const c3Spring = spring({ frame: frame - 28, fps, config: THEME.springs.gentle });
  const c4Spring = spring({ frame: frame - 38, fps, config: THEME.springs.gentle });

  // Animated Numbers count up matching Proposal Page 5
  const roomsReady = Math.floor(
    interpolate(frame, [15, 80], [0, 42], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })
  );

  const cleanTime = Math.floor(
    interpolate(frame, [25, 90], [40, 24], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })
  );

  const passRate = Math.floor(
    interpolate(frame, [35, 100], [75, 96], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })
  );

  const openRepairs = Math.floor(
    interpolate(frame, [45, 105], [6, 2], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })
  );

  // Bars animate upward
  const barGrow = interpolate(frame, [40, 100], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

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
        padding: "20px 80px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 28,
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
            backgroundColor: "rgba(20, 184, 166, 0.15)",
            border: `1.5px solid ${THEME.accentTeal}`,
            color: THEME.accentTeal,
            fontSize: 18,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 10,
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
          General Manager & Owner Analytics
        </div>

        <h2
          style={{
            ...THEME.typography.headline,
            fontSize: 58,
            color: THEME.textPrimary,
            margin: 0,
            letterSpacing: "-0.03em",
          }}
        >
          Your whole hotel <span style={{ color: THEME.accentTeal }}>on one screen.</span>
        </h2>
        <div style={{ color: "#94A3B8", fontSize: 18, fontWeight: 500, marginTop: 4 }}>
          Today · Ocean View Hotel · <span style={{ color: "#10B981", fontWeight: 700 }}>Updated live</span>
        </div>
      </div>

      {/* 4 Animated Metric Cards matching Proposal Page 5 */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 24,
          width: "100%",
          maxWidth: 1600,
          marginBottom: 28,
        }}
      >
        {/* Card 1: Rooms Ready */}
        <div
          style={{
            transform: `scale(${c1Spring})`,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: `1.5px solid #E2E8F0`,
            padding: "24px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 16, color: "#64748B", fontWeight: 600 }}>Rooms ready</div>
          <div style={{ fontSize: 52, fontWeight: 900, color: "#10B981", marginTop: 4, letterSpacing: "-0.03em" }}>
            {roomsReady}
          </div>
          <div style={{ fontSize: 15, color: "#64748B", fontWeight: 600, marginTop: 4 }}>
            of 60 rooms total
          </div>
        </div>

        {/* Card 2: Avg Clean Time */}
        <div
          style={{
            transform: `scale(${c2Spring})`,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: `1.5px solid #E2E8F0`,
            padding: "24px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 16, color: "#64748B", fontWeight: 600 }}>Avg clean time</div>
          <div style={{ fontSize: 52, fontWeight: 900, color: THEME.accentTeal, marginTop: 4, letterSpacing: "-0.03em" }}>
            {cleanTime} <span style={{ fontSize: 26, fontWeight: 700 }}>min</span>
          </div>
          <div style={{ fontSize: 15, color: "#64748B", fontWeight: 600, marginTop: 4 }}>
            per checkout room
          </div>
        </div>

        {/* Card 3: Inspection Pass */}
        <div
          style={{
            transform: `scale(${c3Spring})`,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: `1.5px solid #E2E8F0`,
            padding: "24px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 16, color: "#64748B", fontWeight: 600 }}>Inspection pass</div>
          <div style={{ fontSize: 52, fontWeight: 900, color: "#8B5CF6", marginTop: 4, letterSpacing: "-0.03em" }}>
            {passRate}%
          </div>
          <div style={{ fontSize: 15, color: "#64748B", fontWeight: 600, marginTop: 4 }}>
            first time score
          </div>
        </div>

        {/* Card 4: Open Repairs */}
        <div
          style={{
            transform: `scale(${c4Spring})`,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: `1.5px solid #E2E8F0`,
            padding: "24px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 16, color: "#64748B", fontWeight: 600 }}>Open repairs</div>
          <div style={{ fontSize: 52, fontWeight: 900, color: "#F59E0B", marginTop: 4, letterSpacing: "-0.03em" }}>
            {openRepairs}
          </div>
          <div style={{ fontSize: 15, color: "#EF4444", fontWeight: 700, marginTop: 4 }}>
            1 urgent · in progress
          </div>
        </div>
      </div>

      {/* Bottom Section: Weekly Chart + Team Progress matching Proposal Page 5 */}
      <div
        style={{
          display: "flex",
          gap: 28,
          width: "100%",
          maxWidth: 1600,
        }}
      >
        {/* Left: Rooms Cleaned This Week Bar Chart */}
        <div
          style={{
            flex: 1.2,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: "1.5px solid #E2E8F0",
            padding: "22px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
            <div style={{ fontSize: 20, fontWeight: 800, color: "#0F172A" }}>
              Rooms cleaned this week
            </div>
            <div style={{ fontSize: 14, color: "#64748B", fontWeight: 600 }}>
              Total: 329 rooms
            </div>
          </div>

          <div style={{ display: "flex", alignItems: "flex-end", height: 160, gap: 20, paddingBottom: 10 }}>
            {[
              { day: "Mon", val: 38, h: 80 },
              { day: "Tue", val: 44, h: 96 },
              { day: "Wed", val: 41, h: 90 },
              { day: "Thu", val: 47, h: 105 },
              { day: "Fri", val: 52, h: 120 },
              { day: "Sat", val: 58, h: 140, isMax: true },
              { day: "Sun", val: 49, h: 112 },
            ].map((d) => (
              <div key={d.day} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 8 }}>
                <span style={{ fontSize: 13, fontWeight: 700, color: d.isMax ? "#0D9488" : "#64748B" }}>
                  {Math.floor(d.val * barGrow)}
                </span>
                <div
                  style={{
                    width: "100%",
                    height: d.h * barGrow,
                    backgroundColor: d.isMax ? "#0D9488" : "#99F6E4",
                    borderRadius: "8px 8px 4px 4px",
                    transition: "height 0.2s ease",
                  }}
                />
                <span style={{ fontSize: 14, fontWeight: 600, color: "#475569" }}>{d.day}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Right: Team Progress Bars */}
        <div
          style={{
            flex: 1,
            backgroundColor: "#FFFFFF",
            borderRadius: 22,
            border: "1.5px solid #E2E8F0",
            padding: "22px 28px",
            boxShadow: "0 20px 45px rgba(0,0,0,0.35)",
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 20, fontWeight: 800, color: "#0F172A", marginBottom: 16 }}>
            Team progress today
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {[
              { name: "Nimal", done: 8, total: 12, pct: 67, color: "#14B8A6" },
              { name: "Sara", done: 9, total: 10, pct: 90, color: "#10B981" },
              { name: "Kumari", done: 5, total: 11, pct: 45, color: "#3B82F6" },
              { name: "Ravi", done: 7, total: 12, pct: 58, color: "#14B8A6" },
            ].map((p) => (
              <div key={p.name}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 15, fontWeight: 700, marginBottom: 4 }}>
                  <span style={{ color: "#1E293B" }}>{p.name}</span>
                  <span style={{ color: "#64748B" }}>{p.done} / {p.total} rooms</span>
                </div>
                <div style={{ width: "100%", height: 10, backgroundColor: "#F1F5F9", borderRadius: 8, overflow: "hidden" }}>
                  <div
                    style={{
                      width: `${p.pct * barGrow}%`,
                      height: "100%",
                      backgroundColor: p.color,
                      borderRadius: 8,
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
