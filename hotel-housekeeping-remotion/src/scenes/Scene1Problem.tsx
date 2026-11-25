import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { PaperChecklistIcon, WalkieTalkieIcon, PhoneChatIcon, ClockIcon } from "../icons";

export const Scene1Problem: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene1_vo.mp3");
  const whooshSrc = staticFile("assets/sfx_whoosh.wav");

  // Subtle camera drift for calm human cinematic feel
  const cameraZoom = interpolate(frame, [0, 225], [1.0, 1.03], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Typewriter effect for headline
  const fullText = "Which rooms are ready? Nobody knows.";
  const typedCount = Math.floor(
    interpolate(frame, [15, 75], [0, fullText.length], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );
  const displayedText = fullText.slice(0, typedCount);
  const showCursor = frame < 120 ? Math.floor(frame / 8) % 2 === 0 : false;

  // Background subtle red urgency breathing
  const redTint = interpolate(frame, [40, 180], [0.05, 0.22], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Center collapse into focus singularity at frames 190–225
  const collapseSpring = spring({
    frame: frame - 192,
    fps,
    config: { damping: 20, mass: 0.8, stiffness: 100 },
  });
  const collapseScale = interpolate(collapseSpring, [0, 1], [1, 0.04], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const collapseOpacity = interpolate(frame, [192, 222], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Smooth luxury spring entry for problem cards
  const s1 = spring({ frame: frame - 15, fps, config: THEME.springs.gentle });
  const s2 = spring({ frame: frame - 30, fps, config: THEME.springs.gentle });
  const s3 = spring({ frame: frame - 45, fps, config: THEME.springs.gentle });
  const s4 = spring({ frame: frame - 60, fps, config: THEME.springs.gentle });

  // Organic gentle floating motion (human-like floating, not jerky shaking)
  const floatY1 = Math.sin((frame + 0) * 0.05) * 6;
  const floatY2 = Math.cos((frame + 30) * 0.04) * 6;
  const floatY3 = Math.sin((frame + 60) * 0.045) * 5;
  const floatY4 = Math.cos((frame + 90) * 0.05) * 5;

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
      }}
    >
      <Audio src={voSrc} volume={1.0} />
      {frame >= 190 && <Audio src={whooshSrc} volume={0.4} />}

      {/* Luxury ambient radial glows */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `radial-gradient(circle at center, rgba(239, 68, 68, ${redTint}) 0%, rgba(10, 17, 32, 0.95) 75%)`,
          pointerEvents: "none",
        }}
      />

      {/* Subtle architectural dot grid */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundImage: `radial-gradient(rgba(255, 255, 255, 0.06) 1.5px, transparent 1.5px)`,
          backgroundSize: "48px 48px",
          opacity: 0.6,
        }}
      />

      {/* Main Container with slow cinematic drift and center collapse */}
      <div
        style={{
          transform: `scale(${collapseScale * cameraZoom})`,
          opacity: collapseOpacity,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          position: "relative",
          width: "100%",
          height: "100%",
        }}
      >
        {/* Floating Problem Cards (Glassmorphic Luxury Cards) */}
        {/* 1. Paper Checklists (Top-Left) */}
        <div
          style={{
            position: "absolute",
            top: 200,
            left: 280,
            transform: `translateY(${floatY1}px) rotate(-6deg) scale(${s1})`,
            backgroundColor: "rgba(17, 28, 48, 0.85)",
            backdropFilter: "blur(16px)",
            padding: "24px 32px",
            borderRadius: 24,
            border: `1.5px solid rgba(239, 68, 68, 0.4)`,
            boxShadow: "0 25px 50px rgba(0,0,0,0.5), 0 0 30px rgba(239, 68, 68, 0.15)",
            display: "flex",
            alignItems: "center",
            gap: 20,
          }}
        >
          <div
            style={{
              width: 64,
              height: 64,
              borderRadius: 18,
              backgroundColor: "rgba(239, 68, 68, 0.15)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <PaperChecklistIcon size={40} color="#EF4444" />
          </div>
          <div>
            <div style={{ color: "#FFFFFF", fontSize: 22, fontWeight: 700 }}>Paper Checklists</div>
            <div style={{ color: "#EF4444", fontSize: 16, fontWeight: 600 }}>Lost & delayed in halls</div>
          </div>
        </div>

        {/* 2. Walkie Talkies (Top-Right) */}
        <div
          style={{
            position: "absolute",
            top: 190,
            right: 280,
            transform: `translateY(${floatY2}px) rotate(5deg) scale(${s2})`,
            backgroundColor: "rgba(17, 28, 48, 0.85)",
            backdropFilter: "blur(16px)",
            padding: "24px 32px",
            borderRadius: 24,
            border: `1.5px solid rgba(245, 158, 11, 0.4)`,
            boxShadow: "0 25px 50px rgba(0,0,0,0.5), 0 0 30px rgba(245, 158, 11, 0.15)",
            display: "flex",
            alignItems: "center",
            gap: 20,
          }}
        >
          <div
            style={{
              width: 64,
              height: 64,
              borderRadius: 18,
              backgroundColor: "rgba(245, 158, 11, 0.15)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <WalkieTalkieIcon size={40} color="#F59E0B" />
          </div>
          <div>
            <div style={{ color: "#FFFFFF", fontSize: 22, fontWeight: 700 }}>Radio Noise</div>
            <div style={{ color: "#F59E0B", fontSize: 16, fontWeight: 600 }}>Constant calls & static</div>
          </div>
        </div>

        {/* Center Main Typewriter Focus */}
        <div style={{ textAlign: "center", maxWidth: 1100, zIndex: 10 }}>
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: 10,
              padding: "8px 24px",
              borderRadius: 30,
              backgroundColor: "rgba(239, 68, 68, 0.18)",
              border: `1.5px solid rgba(239, 68, 68, 0.4)`,
              color: "#F87171",
              fontSize: 20,
              fontWeight: 700,
              textTransform: "uppercase",
              letterSpacing: "0.1em",
              marginBottom: 24,
            }}
          >
            <span
              style={{
                width: 10,
                height: 10,
                borderRadius: "50%",
                backgroundColor: "#EF4444",
                boxShadow: "0 0 10px #EF4444",
              }}
            />
            The Daily Operational Gap
          </div>

          <h1
            style={{
              ...THEME.typography.headline,
              fontSize: 78,
              color: THEME.textPrimary,
              margin: 0,
              minHeight: 180,
              letterSpacing: "-0.04em",
              textShadow: "0 10px 40px rgba(0,0,0,0.6)",
            }}
          >
            {displayedText}
            {showCursor && <span style={{ color: "#EF4444" }}>|</span>}
          </h1>

          <p
            style={{
              ...THEME.typography.subhead,
              fontSize: 34,
              color: THEME.textSecondary,
              marginTop: 12,
              opacity: interpolate(frame, [80, 110], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
            }}
          >
            Only <span style={{ color: "#FFFFFF", fontWeight: 700 }}>18%</span> of hotels use modern task software. The rest face daily chaos.
          </p>
        </div>

        {/* 3. WhatsApp Groups (Bottom-Left) */}
        <div
          style={{
            position: "absolute",
            bottom: 180,
            left: 320,
            transform: `translateY(${floatY3}px) rotate(4deg) scale(${s3})`,
            backgroundColor: "rgba(17, 28, 48, 0.85)",
            backdropFilter: "blur(16px)",
            padding: "24px 32px",
            borderRadius: 24,
            border: `1.5px solid rgba(59, 130, 246, 0.4)`,
            boxShadow: "0 25px 50px rgba(0,0,0,0.5), 0 0 30px rgba(59, 130, 246, 0.15)",
            display: "flex",
            alignItems: "center",
            gap: 20,
          }}
        >
          <div
            style={{
              width: 64,
              height: 64,
              borderRadius: 18,
              backgroundColor: "rgba(59, 130, 246, 0.15)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <PhoneChatIcon size={40} color="#3B82F6" />
          </div>
          <div>
            <div style={{ color: "#FFFFFF", fontSize: 22, fontWeight: 700 }}>Messy WhatsApp</div>
            <div style={{ color: "#60A5FA", fontSize: 16, fontWeight: 600 }}>Unread messages & missed tasks</div>
          </div>
        </div>

        {/* 4. Clock / Lobby Delays (Bottom-Right) */}
        <div
          style={{
            position: "absolute",
            bottom: 190,
            right: 320,
            transform: `translateY(${floatY4}px) rotate(-5deg) scale(${s4})`,
            backgroundColor: "rgba(17, 28, 48, 0.85)",
            backdropFilter: "blur(16px)",
            padding: "24px 32px",
            borderRadius: 24,
            border: `1.5px solid rgba(168, 85, 247, 0.4)`,
            boxShadow: "0 25px 50px rgba(0,0,0,0.5), 0 0 30px rgba(168, 85, 247, 0.15)",
            display: "flex",
            alignItems: "center",
            gap: 20,
          }}
        >
          <div
            style={{
              width: 64,
              height: 64,
              borderRadius: 18,
              backgroundColor: "rgba(168, 85, 247, 0.15)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <ClockIcon size={40} color="#A855F7" />
          </div>
          <div>
            <div style={{ color: "#FFFFFF", fontSize: 22, fontWeight: 700 }}>Lobby Waiting</div>
            <div style={{ color: "#C084FC", fontSize: 16, fontWeight: 600 }}>Guests waiting to check in</div>
          </div>
        </div>
      </div>
    </div>
  );
};
