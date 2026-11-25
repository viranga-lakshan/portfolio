import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { DirtyIcon, AssignedIcon, CleaningIcon, ReadyIcon, ToInspectIcon, OutOfOrderIcon } from "../icons";

interface RoomState {
  num: number;
  type: string;
  floor: number;
  initialStatus: "dirty" | "assigned" | "cleaning" | "ready";
  changeFrame?: number;
  newStatus?: "dirty" | "assigned" | "cleaning" | "ready";
  secondChangeFrame?: number;
  secondStatus?: "dirty" | "assigned" | "cleaning" | "ready";
}

const ROOMS_CONFIG: RoomState[] = [
  { num: 101, type: "King", floor: 1, initialStatus: "ready" },
  { num: 102, type: "Twin", floor: 1, initialStatus: "dirty", changeFrame: 70, newStatus: "assigned" },
  { num: 103, type: "Suite", floor: 1, initialStatus: "cleaning", changeFrame: 170, newStatus: "ready" },
  { num: 104, type: "King", floor: 1, initialStatus: "dirty", changeFrame: 90, newStatus: "assigned", secondChangeFrame: 190, secondStatus: "cleaning" },
  { num: 105, type: "King", floor: 1, initialStatus: "dirty", changeFrame: 110, newStatus: "cleaning" },
  { num: 106, type: "Twin", floor: 1, initialStatus: "assigned" },

  { num: 107, type: "Suite", floor: 1, initialStatus: "dirty", changeFrame: 130, newStatus: "assigned" },
  { num: 108, type: "King", floor: 1, initialStatus: "assigned", changeFrame: 140, newStatus: "cleaning" },
  { num: 109, type: "Twin", floor: 1, initialStatus: "dirty" },
  { num: 110, type: "King", floor: 1, initialStatus: "dirty", changeFrame: 160, newStatus: "cleaning" },
  { num: 111, type: "Twin", floor: 1, initialStatus: "dirty" },
  { num: 112, type: "Suite", floor: 1, initialStatus: "cleaning", changeFrame: 180, newStatus: "ready" },

  { num: 113, type: "King", floor: 2, initialStatus: "dirty", changeFrame: 150, newStatus: "assigned" },
  { num: 114, type: "King", floor: 2, initialStatus: "dirty" },
  { num: 115, type: "Twin", floor: 2, initialStatus: "cleaning", changeFrame: 200, newStatus: "ready" },
  { num: 116, type: "Suite", floor: 2, initialStatus: "dirty", changeFrame: 120, newStatus: "assigned" },
  { num: 117, type: "King", floor: 2, initialStatus: "dirty" },
  { num: 118, type: "Twin", floor: 2, initialStatus: "ready" },

  { num: 119, type: "King", floor: 2, initialStatus: "dirty" },
  { num: 120, type: "Suite", floor: 2, initialStatus: "dirty", changeFrame: 220, newStatus: "ready" },
  { num: 121, type: "Twin", floor: 3, initialStatus: "dirty", changeFrame: 100, newStatus: "assigned" },
  { num: 122, type: "King", floor: 3, initialStatus: "cleaning", changeFrame: 210, newStatus: "ready" },
  { num: 123, type: "Suite", floor: 3, initialStatus: "dirty" },
  { num: 124, type: "Twin", floor: 3, initialStatus: "dirty" },
];

export const Scene3RoomBoard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene3_vo.mp3");

  // Entrance spring for the tablet mockup
  const tabletSpring = spring({
    frame: frame - 10,
    fps,
    config: { damping: 17, mass: 0.9, stiffness: 90 },
  });
  const tabletScale = interpolate(tabletSpring, [0, 1], [0.85, 1]);
  const tabletOpacity = interpolate(frame, [5, 25], [0, 1]);

  // Header fade-in
  const headerOpacity = interpolate(frame, [0, 30], [0, 1]);

  // Live counters calculations
  const readyCount = Math.floor(
    interpolate(frame, [70, 240], [0, 6], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const dirtyCount = Math.floor(
    interpolate(frame, [70, 240], [18, 9], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const cleaningCount = Math.floor(
    interpolate(frame, [70, 240], [4, 5], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  const assignedCount = Math.floor(
    interpolate(frame, [70, 240], [2, 4], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  // Exit transition (last 15 frames)
  const exitOpacity = interpolate(frame, [315, 330], [1, 0], {
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
        padding: "40px 60px",
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Top Header text */}
      <div
        style={{
          textAlign: "center",
          marginBottom: 24,
          opacity: headerOpacity,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 10,
            padding: "6px 20px",
            borderRadius: 30,
            backgroundColor: "rgba(20, 184, 166, 0.15)",
            border: `1px solid ${THEME.accentTeal}`,
            color: THEME.accentTeal,
            fontSize: 20,
            fontWeight: 700,
            textTransform: "uppercase",
            letterSpacing: "0.08em",
            marginBottom: 12,
          }}
        >
          <span
            style={{
              width: 10,
              height: 10,
              borderRadius: "50%",
              backgroundColor: THEME.accentTeal,
              boxShadow: "0 0 10px #14B8A6",
            }}
          />
          Manager & Front Desk Live View
        </div>

        <h2
          style={{
            ...THEME.typography.headlineSmall,
            color: THEME.textPrimary,
            margin: 0,
          }}
        >
          See every room's status — <span style={{ color: THEME.accentTeal }}>live.</span>
        </h2>
      </div>

      {/* Tablet Mockup Enclosure */}
      <div
        style={{
          width: 1460,
          height: 680,
          backgroundColor: "#0B1120",
          borderRadius: 28,
          border: `14px solid #1E293B`,
          boxShadow: "0 35px 80px rgba(0,0,0,0.65), 0 0 0 1px rgba(255,255,255,0.08)",
          transform: `scale(${tabletScale})`,
          opacity: tabletOpacity,
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
        }}
      >
        {/* Tablet Top App Bar */}
        <div
          style={{
            height: 72,
            backgroundColor: THEME.surface,
            borderBottom: `1px solid ${THEME.border}`,
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            padding: "0 28px",
          }}
        >
          {/* Hotel Name & Live Indicator */}
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <span style={{ fontSize: 24, fontWeight: 800, color: THEME.textPrimary }}>
              Ocean View Grand Resort
            </span>
            <span
              style={{
                fontSize: 16,
                fontWeight: 600,
                color: THEME.accentTeal,
                backgroundColor: "rgba(20, 184, 166, 0.15)",
                padding: "4px 12px",
                borderRadius: 20,
              }}
            >
              Floor 1–3 (24 Rooms)
            </span>
          </div>

          {/* Live Status Counters */}
          <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "6px 14px",
                borderRadius: 12,
                backgroundColor: THEME.status.ready.bg,
                border: `1px solid ${THEME.status.ready.border}`,
              }}
            >
              <ReadyIcon size={20} color={THEME.status.ready.color} />
              <span style={{ color: THEME.status.ready.color, fontSize: 18, fontWeight: 700 }}>
                Ready {readyCount}
              </span>
            </div>

            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "6px 14px",
                borderRadius: 12,
                backgroundColor: THEME.status.dirty.bg,
                border: `1px solid ${THEME.status.dirty.border}`,
              }}
            >
              <DirtyIcon size={20} color={THEME.status.dirty.color} />
              <span style={{ color: THEME.status.dirty.color, fontSize: 18, fontWeight: 700 }}>
                Dirty {dirtyCount}
              </span>
            </div>

            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "6px 14px",
                borderRadius: 12,
                backgroundColor: THEME.status.cleaning.bg,
                border: `1px solid ${THEME.status.cleaning.border}`,
              }}
            >
              <CleaningIcon size={20} color={THEME.status.cleaning.color} />
              <span style={{ color: THEME.status.cleaning.color, fontSize: 18, fontWeight: 700 }}>
                Cleaning {cleaningCount}
              </span>
            </div>

            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 8,
                padding: "6px 14px",
                borderRadius: 12,
                backgroundColor: THEME.status.assigned.bg,
                border: `1px solid ${THEME.status.assigned.border}`,
              }}
            >
              <AssignedIcon size={20} color={THEME.status.assigned.color} />
              <span style={{ color: THEME.status.assigned.color, fontSize: 18, fontWeight: 700 }}>
                Assigned {assignedCount}
              </span>
            </div>
          </div>
        </div>

        {/* Room Board Grid: 4 rows x 6 columns = 24 rooms */}
        <div
          style={{
            flex: 1,
            padding: "24px 28px",
            display: "grid",
            gridTemplateColumns: "repeat(6, 1fr)",
            gridTemplateRows: "repeat(4, 1fr)",
            gap: 16,
            backgroundColor: "#0F172A",
          }}
        >
          {ROOMS_CONFIG.map((room) => {
            // Determine active status based on current frame
            let curStatus = room.initialStatus;
            let justChanged = false;

            if (room.changeFrame && frame >= room.changeFrame) {
              curStatus = room.newStatus!;
              justChanged = frame - room.changeFrame < 25;
            }

            if (room.secondChangeFrame && frame >= room.secondChangeFrame) {
              curStatus = room.secondStatus!;
              justChanged = frame - room.secondChangeFrame < 25;
            }

            const statusObj = THEME.status[curStatus];

            // Render matching icon
            let IconComponent = DirtyIcon;
            if (curStatus === "ready") IconComponent = ReadyIcon;
            else if (curStatus === "cleaning") IconComponent = CleaningIcon;
            else if (curStatus === "assigned") IconComponent = AssignedIcon;

            // Flash / pulse on status change
            const popScale = justChanged ? 1.06 : 1.0;

            return (
              <div
                key={room.num}
                style={{
                  backgroundColor: statusObj.bg,
                  border: `2px solid ${statusObj.color}`,
                  borderRadius: 16,
                  padding: "12px 16px",
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "space-between",
                  transform: `scale(${popScale})`,
                  boxShadow: justChanged ? `0 0 20px ${statusObj.color}` : "none",
                  transition: "none",
                }}
              >
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <span style={{ fontSize: 26, fontWeight: 800, color: THEME.textPrimary }}>
                    {room.num}
                  </span>
                  <span
                    style={{
                      fontSize: 13,
                      fontWeight: 600,
                      color: THEME.textSecondary,
                      textTransform: "uppercase",
                      letterSpacing: "0.05em",
                    }}
                  >
                    {room.type}
                  </span>
                </div>

                <div style={{ display: "flex", alignItems: "center", gap: 8, marginTop: 4 }}>
                  <IconComponent size={22} color={statusObj.color} />
                  <span
                    style={{
                      fontSize: 16,
                      fontWeight: 700,
                      color: statusObj.color,
                      textTransform: "capitalize",
                    }}
                  >
                    {statusObj.label}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

