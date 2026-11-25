import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { MousePointerIcon } from "../icons";

interface RoomData {
  num: number;
  initialStatus: "ready" | "cleaning" | "dirty" | "inspect" | "assigned" | "ooo";
  changeFrame?: number;
  newStatus?: "ready" | "cleaning" | "dirty" | "inspect" | "assigned" | "ooo";
  secondChangeFrame?: number;
  secondStatus?: "ready" | "cleaning" | "dirty" | "inspect" | "assigned" | "ooo";
}

// 24 Rooms matching Page 1 of the official proposal!
const PROPOSAL_ROOMS: RoomData[] = [
  // Floor 1
  { num: 101, initialStatus: "ready" },
  { num: 102, initialStatus: "dirty", changeFrame: 80, newStatus: "assigned", secondChangeFrame: 170, secondStatus: "cleaning" },
  { num: 103, initialStatus: "ready" },
  { num: 104, initialStatus: "inspect", changeFrame: 220, newStatus: "ready" },
  { num: 105, initialStatus: "dirty", changeFrame: 120, newStatus: "cleaning" },
  { num: 106, initialStatus: "assigned" },
  { num: 107, initialStatus: "ready" },
  { num: 108, initialStatus: "ooo" }, // DND

  // Floor 2
  { num: 201, initialStatus: "cleaning", changeFrame: 240, newStatus: "ready" },
  { num: 202, initialStatus: "ready" },
  { num: 203, initialStatus: "dirty", changeFrame: 140, newStatus: "cleaning" },
  { num: 204, initialStatus: "inspect" },
  { num: 205, initialStatus: "ready" },
  { num: 206, initialStatus: "cleaning" },
  { num: 207, initialStatus: "assigned" },
  { num: 208, initialStatus: "dirty" },

  // Floor 3
  { num: 301, initialStatus: "ready" },
  { num: 302, initialStatus: "cleaning", changeFrame: 200, newStatus: "ready" },
  { num: 303, initialStatus: "ready" },
  { num: 304, initialStatus: "dirty", changeFrame: 160, newStatus: "assigned" },
  { num: 305, initialStatus: "inspect" },
  { num: 306, initialStatus: "ready" },
  { num: 307, initialStatus: "cleaning" },
  { num: 308, initialStatus: "dirty" },
];

export const Scene3RoomBoard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene3_vo.mp3");
  const clickSrc = staticFile("assets/sfx_click.wav");

  // Entrance spring for tablet
  const tabletSpring = spring({
    frame: frame - 6,
    fps,
    config: { damping: 24, mass: 1.0, stiffness: 80 },
  });
  const tabletScale = interpolate(tabletSpring, [0, 1], [0.9, 1]);
  const tabletOpacity = interpolate(frame, [0, 20], [0, 1]);

  // Subtle continuous camera drift
  const cameraZoom = interpolate(frame, [0, 315], [1.0, 1.025], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Dynamic live counters matching proposal metrics
  const readyCount = Math.floor(
    interpolate(frame, [70, 260], [9, 13], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const cleaningCount = Math.floor(
    interpolate(frame, [70, 260], [5, 6], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const dirtyCount = Math.floor(
    interpolate(frame, [70, 260], [5, 2], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  // Simulated Human Cursor Path:
  // Starts at (1200, 220), moves to Room 102 (420, 480) at frame 75, clicks at frame 80,
  // then glides to Room 105 (720, 480) at frame 115, clicks at frame 120,
  // then glides to Room 203 (520, 600) at frame 135, clicks at frame 140
  const cursorX = interpolate(
    frame,
    [20, 75, 95, 115, 135, 170, 240],
    [1150, 430, 430, 730, 530, 800, 1050],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );
  const cursorY = interpolate(
    frame,
    [20, 75, 95, 115, 135, 170, 240],
    [250, 480, 480, 480, 600, 680, 520],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const isClicking =
    (frame >= 78 && frame <= 85) ||
    (frame >= 118 && frame <= 125) ||
    (frame >= 138 && frame <= 145);

  const cursorScale = isClicking ? 0.85 : 1.0;

  // Exit transition (last 15 frames)
  const exitOpacity = interpolate(frame, [300, 315], [1, 0], {
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
        padding: "30px 60px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />
      {/* Sound effects on clicks */}
      {(frame === 80 || frame === 120 || frame === 140) && (
        <Audio src={clickSrc} volume={0.4} />
      )}

      {/* Background ambient lighting */}
      <div
        style={{
          position: "absolute",
          top: "30%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 1100,
          height: 700,
          background: "radial-gradient(circle, rgba(20, 184, 166, 0.12) 0%, transparent 70%)",
          filter: "blur(60px)",
          pointerEvents: "none",
        }}
      />

      {/* Top Header */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 20,
          opacity: tabletOpacity,
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
          Live Operations Center
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
          See every room's status — <span style={{ color: THEME.accentTeal }}>live.</span>
        </h2>
      </div>

      {/* Luminous Proposal Executive Tablet UI */}
      <div
        style={{
          transform: `scale(${tabletScale * cameraZoom})`,
          opacity: tabletOpacity,
          width: "100%",
          maxWidth: 1540,
          backgroundColor: "#FFFFFF",
          borderRadius: 28,
          boxShadow: "0 30px 80px rgba(0,0,0,0.45), 0 0 0 1px rgba(255,255,255,0.2)",
          padding: "28px 36px",
          position: "relative",
          color: "#0F172A",
        }}
      >
        {/* Tablet Top Header Bar */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderBottom: "1.5px solid #F1F5F9",
            paddingBottom: 18,
            marginBottom: 22,
          }}
        >
          <div>
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <span style={{ fontSize: 28, fontWeight: 800, color: "#0F172A", letterSpacing: "-0.02em" }}>
                Room Board
              </span>
              <span
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  gap: 6,
                  padding: "4px 12px",
                  borderRadius: 20,
                  backgroundColor: "#ECFDF5",
                  color: "#059669",
                  fontSize: 14,
                  fontWeight: 700,
                }}
              >
                <span
                  style={{
                    width: 7,
                    height: 7,
                    borderRadius: "50%",
                    backgroundColor: "#10B981",
                    boxShadow: "0 0 6px #10B981",
                  }}
                />
                LIVE
              </span>
            </div>
            <div style={{ fontSize: 16, color: "#64748B", fontWeight: 500, marginTop: 2 }}>
              Ocean View Hotel · Floors 1–3
            </div>
          </div>

          {/* Proposal Style Summary Metric Pills */}
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            {/* Ready Pill */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "8px 18px",
                borderRadius: 14,
                backgroundColor: THEME.status.ready.bgPastel,
                border: `1.5px solid ${THEME.status.ready.borderPastel}`,
                color: THEME.status.ready.textDark,
                fontWeight: 700,
                fontSize: 17,
              }}
            >
              <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.ready.dot }} />
              Ready {readyCount}
            </div>

            {/* Cleaning Pill */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "8px 18px",
                borderRadius: 14,
                backgroundColor: THEME.status.cleaning.bgPastel,
                border: `1.5px solid ${THEME.status.cleaning.borderPastel}`,
                color: THEME.status.cleaning.textDark,
                fontWeight: 700,
                fontSize: 17,
              }}
            >
              <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.cleaning.dot }} />
              Cleaning {cleaningCount}
            </div>

            {/* Dirty Pill */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "8px 18px",
                borderRadius: 14,
                backgroundColor: THEME.status.dirty.bgPastel,
                border: `1.5px solid ${THEME.status.dirty.borderPastel}`,
                color: THEME.status.dirty.textDark,
                fontWeight: 700,
                fontSize: 17,
              }}
            >
              <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.dirty.dot }} />
              Dirty {dirtyCount}
            </div>
          </div>
        </div>

        {/* 24-Room Grid (8 columns x 3 rows) matching Page 1 */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(8, 1fr)",
            gap: 12,
            marginBottom: 20,
          }}
        >
          {PROPOSAL_ROOMS.map((room) => {
            let currentStatus = room.initialStatus;
            if (room.secondChangeFrame && frame >= room.secondChangeFrame && room.secondStatus) {
              currentStatus = room.secondStatus;
            } else if (room.changeFrame && frame >= room.changeFrame && room.newStatus) {
              currentStatus = room.newStatus;
            }

            const statusTokens = {
              ready: {
                bg: THEME.status.ready.bgPastel,
                border: THEME.status.ready.borderPastel,
                dot: THEME.status.ready.dot,
                text: THEME.status.ready.textDark,
                label: "Ready",
              },
              cleaning: {
                bg: THEME.status.cleaning.bgPastel,
                border: THEME.status.cleaning.borderPastel,
                dot: THEME.status.cleaning.dot,
                text: THEME.status.cleaning.textDark,
                label: "Cleaning",
              },
              dirty: {
                bg: THEME.status.dirty.bgPastel,
                border: THEME.status.dirty.borderPastel,
                dot: THEME.status.dirty.dot,
                text: THEME.status.dirty.textDark,
                label: "Dirty",
              },
              inspect: {
                bg: THEME.status.toInspect.bgPastel,
                border: THEME.status.toInspect.borderPastel,
                dot: THEME.status.toInspect.dot,
                text: THEME.status.toInspect.textDark,
                label: "Inspect",
              },
              assigned: {
                bg: THEME.status.assigned.bgPastel,
                border: THEME.status.assigned.borderPastel,
                dot: THEME.status.assigned.dot,
                text: THEME.status.assigned.textDark,
                label: "Assigned",
              },
              ooo: {
                bg: THEME.status.outOfOrder.bgPastel,
                border: THEME.status.outOfOrder.borderPastel,
                dot: THEME.status.outOfOrder.dot,
                text: THEME.status.outOfOrder.textDark,
                label: "DND",
              },
            }[currentStatus];

            // Smooth spring bump when status changes
            const isJustChanged =
              (room.changeFrame && Math.abs(frame - room.changeFrame) < 15) ||
              (room.secondChangeFrame && Math.abs(frame - room.secondChangeFrame) < 15);
            const scaleBump = isJustChanged ? 1.05 : 1.0;

            return (
              <div
                key={room.num}
                style={{
                  backgroundColor: statusTokens.bg,
                  border: `1.5px solid ${statusTokens.border}`,
                  borderRadius: 16,
                  padding: "16px 14px",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "flex-start",
                  justifyContent: "space-between",
                  minHeight: 88,
                  transform: `scale(${scaleBump})`,
                  transition: "all 0.25s cubic-bezier(0.16, 1, 0.3, 1)",
                  boxShadow: isJustChanged ? "0 8px 20px rgba(0,0,0,0.12)" : "none",
                }}
              >
                <div style={{ fontSize: 24, fontWeight: 800, color: "#1E293B" }}>
                  {room.num}
                </div>
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 6,
                    fontSize: 15,
                    fontWeight: 700,
                    color: statusTokens.text,
                    marginTop: 4,
                  }}
                >
                  <span
                    style={{
                      width: 8,
                      height: 8,
                      borderRadius: "50%",
                      backgroundColor: statusTokens.dot,
                    }}
                  />
                  {statusTokens.label}
                </div>
              </div>
            );
          })}
        </div>

        {/* Legend at bottom matching Proposal Page 1 */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: 28,
            paddingTop: 14,
            borderTop: "1.5px solid #F1F5F9",
            color: "#64748B",
            fontSize: 15,
            fontWeight: 600,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.ready.dot }} />
            Ready to sell
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.cleaning.dot }} />
            Cleaning
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.toInspect.dot }} />
            To inspect
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.assigned.dot }} />
            Assigned
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.dirty.dot }} />
            Dirty
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <span style={{ width: 9, height: 9, borderRadius: "50%", backgroundColor: THEME.status.outOfOrder.dot }} />
            Do not disturb
          </div>
        </div>

        {/* Simulated Human Mouse Cursor */}
        <div
          style={{
            position: "absolute",
            left: cursorX,
            top: cursorY,
            transform: `scale(${cursorScale})`,
            pointerEvents: "none",
            zIndex: 100,
            transition: "transform 0.1s ease",
          }}
        >
          <MousePointerIcon size={34} color={THEME.accentTeal} />
        </div>
      </div>
    </div>
  );
};
