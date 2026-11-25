import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, Img, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";

export const Scene2LogoReveal: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene2_vo.mp3");
  const logoSrc = staticFile("assets/logo.png");

  // Logo spring animation
  const logoSpring = spring({
    frame: frame - 10,
    fps,
    config: { damping: 13, mass: 0.7, stiffness: 110 },
  });

  // Title spring
  const titleSpring = spring({
    frame: frame - 25,
    fps,
    config: { damping: 15, mass: 0.8, stiffness: 100 },
  });

  // Tagline fade & slide
  const taglineOpacity = interpolate(frame, [45, 75], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const taglineY = interpolate(frame, [45, 75], [30, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Axio Global Team Pill
  const teamOpacity = interpolate(frame, [70, 95], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Outro fade to Scene 3 (last 15 frames)
  const exitOpacity = interpolate(frame, [135, 150], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Pulsing teal glow ring
  const pulse = Math.sin(frame * 0.12) * 12;

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
        opacity: exitOpacity,
      }}
    >
      <Audio src={voSrc} volume={1.0} />

      {/* Background radial glow */}
      <div
        style={{
          position: "absolute",
          top: "40%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 900,
          height: 900,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(20, 184, 166, 0.22) 0%, transparent 65%)`,
          filter: "blur(40px)",
        }}
      />

      {/* Logo Image */}
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
            inset: -12,
            borderRadius: 60,
            boxShadow: `0 0 ${40 + pulse}px rgba(20, 184, 166, 0.5)`,
            pointerEvents: "none",
          }}
        />
        <Img
          src={logoSrc}
          style={{
            width: 180,
            height: 180,
            borderRadius: 44,
            boxShadow: "0 25px 60px rgba(0,0,0,0.5)",
          }}
        />
      </div>

      {/* Product Name */}
      <div
        style={{
          transform: `scale(${titleSpring})`,
          textAlign: "center",
        }}
      >
        <h1
          style={{
            ...THEME.typography.headline,
            fontSize: 88,
            color: THEME.textPrimary,
            margin: 0,
            letterSpacing: "-0.04em",
          }}
        >
          {THEME.productName}
        </h1>
      </div>

      {/* Tagline */}
      <div
        style={{
          opacity: taglineOpacity,
          transform: `translateY(${taglineY}px)`,
          textAlign: "center",
          marginTop: 20,
        }}
      >
        <p
          style={{
            ...THEME.typography.subhead,
            fontSize: 42,
            color: THEME.accentTeal,
            fontWeight: 600,
            margin: 0,
            letterSpacing: "-0.01em",
          }}
        >
          {THEME.tagline}
        </p>
      </div>

      {/* Team Badge */}
      <div
        style={{
          opacity: teamOpacity,
          marginTop: 40,
          padding: "10px 28px",
          borderRadius: 40,
          backgroundColor: THEME.surface,
          border: `1px solid ${THEME.borderLight}`,
          color: THEME.textSecondary,
          fontSize: 22,
          fontWeight: 600,
          letterSpacing: "0.06em",
          textTransform: "uppercase",
        }}
      >
        By <span style={{ color: THEME.textPrimary, fontWeight: 700 }}>{THEME.teamName}</span>
      </div>
    </div>
  );
};

