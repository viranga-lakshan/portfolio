import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";
import { PaperChecklistIcon, WalkieTalkieIcon, PhoneChatIcon, ClockIcon } from "../icons";

export const Scene1Problem: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Voiceover audio
  const voSrc = staticFile("assets/scene1_vo.mp3");

  // Typewriter effect for headline
  const fullText = "Which rooms are ready? Nobody knows.";
  const typedCount = Math.floor(
    interpolate(frame, [15, 80], [0, fullText.length], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );
  const displayedText = fullText.slice(0, typedCount);
  const showCursor = frame < 120 ? Math.floor(frame / 8) % 2 === 0 : false;

  // Background subtle red tint urgency
  const redTint = interpolate(frame, [60, 160], [0, 0.22], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Collapse into center at end (frames 200 to 235)
  const collapseSpring = spring({
    frame: frame - 200,
    fps,
    config: { damping: 14, mass: 0.6, stiffness: 140 },
  });
  const collapseScale = interpolate(collapseSpring, [0, 1], [1, 0.05], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const collapseOpacity = interpolate(frame, [200, 230], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Icon entry springs
  const s1 = spring({ frame: frame - 15, fps, config: THEME.springs.bouncy });
  const s2 = spring({ frame: frame - 30, fps, config: THEME.springs.bouncy });
  const s3 = spring({ frame: frame - 45, fps, config: THEME.springs.bouncy });
  const s4 = spring({ frame: frame - 60, fps, config: THEME.springs.bouncy });

  // Gentle shake animation between frames 90 and 195
  const isShaking = frame > 80 && frame < 200;
  const shakeOffset = isShaking ? Math.sin(frame * 0.45) * 4 : 0;
  const shakeRot = isShaking ? Math.cos(frame * 0.35) * 2.5 : 0;

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

      {/* Red urgency radial tint */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `radial-gradient(circle at center, rgba(239, 68, 68, ${redTint}) 0%, transparent 75%)`,
          pointerEvents: "none",
        }}
      />

      {/* Subtle grid background */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundImage: `radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px)`,
          backgroundSize: "40px 40px",
          opacity: 0.7,
        }}
      />

      {/* Main Container that collapses */}
      <div
        style={{
          transform: `scale(${collapseScale})`,
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
        {/* Floating Problem Icons */}
        {/* 1. Paper Checklist (Top-Left) */}
        <div
          style={{
            position: "absolute",
            top: 220,
            left: 320,
            transform: `translateY(${shakeOffset}px) rotate(${-12 + shakeRot}deg) scale(${s1})`,
            backgroundColor: THEME.surface,
            padding: 28,
            borderRadius: 24,
            border: `2px solid rgba(239, 68, 68, 0.4)`,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          <PaperChecklistIcon size={76} color="#EF4444" />
          <span style={{ color: "#EF4444", fontSize: 20, fontWeight: 700 }}>Lost Paperwork</span>
        </div>

        {/* 2. Walkie Talkie (Top-Right) */}
        <div
          style={{
            position: "absolute",
            top: 210,
            right: 320,
            transform: `translateY(${-shakeOffset}px) rotate(${15 + shakeRot}deg) scale(${s2})`,
            backgroundColor: THEME.surface,
            padding: 28,
            borderRadius: 24,
            border: `2px solid rgba(245, 158, 11, 0.4)`,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          <WalkieTalkieIcon size={76} color="#F59E0B" />
          <span style={{ color: "#F59E0B", fontSize: 20, fontWeight: 700 }}>Radio Noise</span>
        </div>

        {/* 3. Phone Chat Bubbles (Bottom-Left) */}
        <div
          style={{
            position: "absolute",
            bottom: 200,
            left: 360,
            transform: `translateY(${shakeOffset * 0.8}px) rotate(${8 - shakeRot}deg) scale(${s3})`,
            backgroundColor: THEME.surface,
            padding: 28,
            borderRadius: 24,
            border: `2px solid rgba(59, 130, 246, 0.4)`,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          <PhoneChatIcon size={76} color="#3B82F6" />
          <span style={{ color: "#3B82F6", fontSize: 20, fontWeight: 700 }}>Endless WhatsApps</span>
        </div>

        {/* 4. Clock spinning / delays (Bottom-Right) */}
        <div
          style={{
            position: "absolute",
            bottom: 190,
            right: 360,
            transform: `translateY(${-shakeOffset * 0.8}px) rotate(${-14 + shakeRot}deg) scale(${s4})`,
            backgroundColor: THEME.surface,
            padding: 28,
            borderRadius: 24,
            border: `2px solid rgba(168, 85, 247, 0.4)`,
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 12,
          }}
        >
          <ClockIcon size={76} color="#A855F7" />
          <span style={{ color: "#A855F7", fontSize: 20, fontWeight: 700 }}>Check-in Delays</span>
        </div>

        {/* Center Typography */}
        <div
          style={{
            maxWidth: 1100,
            textAlign: "center",
            zIndex: 10,
            padding: "0 40px",
          }}
        >
          <div
            style={{
              display: "inline-block",
              padding: "8px 24px",
              borderRadius: 30,
              backgroundColor: "rgba(239, 68, 68, 0.15)",
              border: "1px solid rgba(239, 68, 68, 0.4)",
              color: "#EF4444",
              fontSize: 22,
              fontWeight: 700,
              letterSpacing: "0.08em",
              textTransform: "uppercase",
              marginBottom: 28,
              opacity: interpolate(frame, [5, 25], [0, 1]),
            }}
          >
            The Daily Front Desk Dilemma
          </div>

          <h1
            style={{
              ...THEME.typography.headline,
              color: THEME.textPrimary,
              margin: 0,
              minHeight: 180,
            }}
          >
            {displayedText}
            {showCursor && (
              <span style={{ color: THEME.accentTeal, marginLeft: 4 }}>|</span>
            )}
          </h1>

          <p
            style={{
              ...THEME.typography.subhead,
              color: THEME.textSecondary,
              marginTop: 20,
              opacity: interpolate(frame, [80, 110], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              }),
            }}
          >
            Checklists get lost. Radios buzz. Guests wait at the lobby.
          </p>
        </div>
      </div>
    </div>
  );
};

