import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, Img, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";

export const Scene2LogoReveal: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene2_vo.mp3");
  const logoSrc = staticFile("assets/logo.png");
  const chimeSrc = staticFile("assets/sfx_chime.wav");

  // Smooth luxury spring physics
  const logoSpring = spring({
    frame: frame - 8,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });

  const titleSpring = spring({
    frame: frame - 22,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });

  // Tagline fade and smooth slide
  const taglineOpacity = interpolate(frame, [40, 70], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const taglineY = interpolate(frame, [40, 70], [25, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Team Axio Global Pill
  const teamOpacity = interpolate(frame, [65, 95], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Subtle continuous camera float (scale 0.98 to 1.025)
  const cameraZoom = interpolate(frame, [0, 180], [0.98, 1.025], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Outro transition (last 15 frames)
  const exitOpacity = interpolate(frame, [165, 180], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Gentle emerald radial aura pulse
  const pulse = Math.sin(frame * 0.08) * 16;

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
      {frame >= 12 && frame <= 50 && <Audio src={chimeSrc} volume={0.45} />}

      {/* Atmospheric luxury background glows */}
      <div
        style={{
          position: "absolute",
          top: "42%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 950,
          height: 950,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(16, 185, 129, 0.22) 0%, rgba(20, 184, 166, 0.1) 45%, transparent 70%)`,
          filter: "blur(50px)",
        }}
      />

      <div
        style={{
          transform: `scale(${cameraZoom})`,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {/* Logo Badge with luminous aura */}
        <div
          style={{
            transform: `scale(${logoSpring})`,
            marginBottom: 28,
            position: "relative",
          }}
        >
          <div
            style={{
              position: "absolute",
              inset: -16,
              borderRadius: 65,
              boxShadow: `0 0 ${50 + pulse}px rgba(16, 185, 129, 0.55)`,
              pointerEvents: "none",
            }}
          />
          <Img
            src={logoSrc}
            style={{
              width: 180,
              height: 180,
              borderRadius: 44,
              boxShadow: "0 30px 70px rgba(0,0,0,0.6)",
            }}
          />
        </div>

        {/* Product Title */}
        <div
          style={{
            transform: `scale(${titleSpring})`,
            textAlign: "center",
          }}
        >
          <h1
            style={{
              ...THEME.typography.headline,
              fontSize: 94,
              color: THEME.textPrimary,
              margin: 0,
              letterSpacing: "-0.04em",
              textShadow: "0 15px 40px rgba(0,0,0,0.6)",
            }}
          >
            {THEME.productName}
          </h1>

          <div
            style={{
              fontSize: 26,
              color: THEME.textSecondary,
              fontWeight: 600,
              letterSpacing: "0.06em",
              textTransform: "uppercase",
              marginTop: 10,
            }}
          >
            {THEME.subTitle}
          </div>
        </div>

        {/* Tagline */}
        <div
          style={{
            opacity: taglineOpacity,
            transform: `translateY(${taglineY}px)`,
            textAlign: "center",
            marginTop: 24,
          }}
        >
          <p
            style={{
              ...THEME.typography.subhead,
              fontSize: 44,
              color: THEME.accentTeal,
              fontWeight: 600,
              margin: 0,
              letterSpacing: "-0.01em",
            }}
          >
            {THEME.tagline}
          </p>
        </div>

        {/* Team Axio Global Verified Pill */}
        <div
          style={{
            opacity: teamOpacity,
            marginTop: 36,
            display: "inline-flex",
            alignItems: "center",
            gap: 12,
            padding: "10px 28px",
            borderRadius: 30,
            backgroundColor: "rgba(255, 255, 255, 0.06)",
            border: `1.5px solid rgba(255, 255, 255, 0.15)`,
            boxShadow: "0 10px 30px rgba(0,0,0,0.3)",
          }}
        >
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: "50%",
              backgroundColor: THEME.accentEmerald,
              boxShadow: "0 0 10px #10B981",
            }}
          />
          <span
            style={{
              color: THEME.textPrimary,
              fontSize: 20,
              fontWeight: 700,
              letterSpacing: "0.08em",
              textTransform: "uppercase",
            }}
          >
            By {THEME.teamName}
          </span>
        </div>
      </div>
    </div>
  );
};
