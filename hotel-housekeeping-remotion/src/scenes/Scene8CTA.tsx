import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, Img, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";

export const Scene8CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const voSrc = staticFile("assets/scene8_vo.mp3");
  const logoSrc = staticFile("assets/logo.png");

  // Entrance spring
  const logoSpring = spring({
    frame: frame - 5,
    fps,
    config: { damping: 14, mass: 0.7, stiffness: 110 },
  });

  const textSpring = spring({
    frame: frame - 18,
    fps,
    config: { damping: 16, mass: 0.8, stiffness: 100 },
  });

  const infoOpacity = interpolate(frame, [30, 60], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Gentle teal glow pulse
  const pulse = Math.sin(frame * 0.14) * 16 + 25;

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

      {/* Background Radial Glow */}
      <div
        style={{
          position: "absolute",
          top: "45%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 1000,
          height: 1000,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(20, 184, 166, 0.28) 0%, transparent 65%)`,
          filter: "blur(50px)",
        }}
      />

      {/* Centered Logo with pulsing glow */}
      <div
        style={{
          transform: `scale(${logoSpring})`,
          marginBottom: 32,
          position: "relative",
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: -14,
            borderRadius: 60,
            boxShadow: `0 0 ${pulse}px rgba(20, 184, 166, 0.6)`,
            pointerEvents: "none",
          }}
        />
        <Img
          src={logoSrc}
          style={{
            width: 170,
            height: 170,
            borderRadius: 42,
            boxShadow: "0 25px 60px rgba(0,0,0,0.5)",
          }}
        />
      </div>

      {/* Main Headline */}
      <div
        style={{
          transform: `scale(${textSpring})`,
          textAlign: "center",
        }}
      >
        <h1
          style={{
            ...THEME.typography.headline,
            fontSize: 78,
            color: THEME.textPrimary,
            margin: 0,
            letterSpacing: "-0.03em",
          }}
        >
          Book your free demo today
        </h1>

        <p
          style={{
            ...THEME.typography.subhead,
            fontSize: 38,
            color: THEME.accentTeal,
            fontWeight: 600,
            marginTop: 18,
            marginBottom: 0,
          }}
        >
          Turn messy housekeeping into a live, organized flow.
        </p>
      </div>

      {/* Website / Contact & Team Attribution */}
      <div
        style={{
          opacity: infoOpacity,
          marginTop: 48,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 16,
        }}
      >
        {/* Contact Pill */}
        <div
          style={{
            padding: "16px 44px",
            borderRadius: 40,
            backgroundColor: THEME.surface,
            border: `2px solid ${THEME.accentTeal}`,
            color: THEME.textPrimary,
            fontSize: 32,
            fontWeight: 800,
            letterSpacing: "0.02em",
            boxShadow: `0 12px 35px ${THEME.accentTealGlow}`,
            display: "flex",
            alignItems: "center",
            gap: 16,
          }}
        >
          <span style={{ color: THEME.accentTeal }}>👉</span>
          <span>{THEME.contact}</span>
        </div>

        {/* Team Axio Global Signature */}
        <div
          style={{
            marginTop: 8,
            color: THEME.textSecondary,
            fontSize: 22,
            fontWeight: 600,
            letterSpacing: "0.05em",
            textTransform: "uppercase",
          }}
        >
          Engineered by <span style={{ color: THEME.textPrimary, fontWeight: 700 }}>{THEME.teamName}</span>
        </div>
      </div>
    </div>
  );
};

