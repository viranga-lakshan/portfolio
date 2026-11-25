import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, Img, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { THEME, fontFamily } from "../theme";

export const Scene8CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const voSrc = staticFile("assets/scene8_vo.mp3");
  const logoSrc = staticFile("assets/logo.png");
  const chimeSrc = staticFile("assets/sfx_chime.wav");

  // Entrance springs
  const logoSpring = spring({
    frame: frame - 6,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });

  const textSpring = spring({
    frame: frame - 18,
    fps,
    config: { damping: 22, mass: 0.9, stiffness: 85 },
  });

  const infoOpacity = interpolate(frame, [25, 55], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Calm subtle teal pulse
  const pulse = Math.sin(frame * 0.08) * 12 + 20;

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
      {frame === 10 && <Audio src={chimeSrc} volume={0.4} />}

      {/* Atmospheric ambient lighting */}
      <div
        style={{
          position: "absolute",
          top: "45%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 1100,
          height: 1100,
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(16, 185, 129, 0.22) 0%, rgba(20, 184, 166, 0.1) 45%, transparent 70%)`,
          filter: "blur(60px)",
          pointerEvents: "none",
        }}
      />

      {/* Team Axio Global Pill Badge at Top */}
      <div
        style={{
          opacity: infoOpacity,
          marginBottom: 20,
          display: "inline-flex",
          alignItems: "center",
          gap: 10,
          padding: "8px 24px",
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
            fontSize: 18,
            fontWeight: 700,
            letterSpacing: "0.1em",
            textTransform: "uppercase",
          }}
        >
          {THEME.teamName} · SRI LANKA
        </span>
      </div>

      {/* Centered Logo with radiant aura */}
      <div
        style={{
          transform: `scale(${logoSpring})`,
          marginBottom: 24,
          position: "relative",
        }}
      >
        <div
          style={{
            position: "absolute",
            inset: -14,
            borderRadius: 60,
            boxShadow: `0 0 ${pulse}px rgba(16, 185, 129, 0.6)`,
            pointerEvents: "none",
          }}
        />
        <Img
          src={logoSrc}
          style={{
            width: 160,
            height: 160,
            borderRadius: 40,
            boxShadow: "0 25px 60px rgba(0,0,0,0.6)",
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
            fontSize: 76,
            color: THEME.textPrimary,
            margin: 0,
            letterSpacing: "-0.035em",
            textShadow: "0 15px 40px rgba(0,0,0,0.6)",
          }}
        >
          Book your free live demo today
        </h1>

        <p
          style={{
            ...THEME.typography.subhead,
            fontSize: 34,
            color: THEME.accentTeal,
            fontWeight: 600,
            marginTop: 14,
            marginBottom: 0,
          }}
        >
          See RoomReady configured with your own hotel layout in 20 minutes.
        </p>
      </div>

      {/* Contact Cards matching Proposal Page 7 */}
      <div
        style={{
          opacity: infoOpacity,
          marginTop: 36,
          display: "flex",
          gap: 24,
          alignItems: "center",
        }}
      >
        {/* Email Card */}
        <div
          style={{
            padding: "16px 32px",
            borderRadius: 20,
            backgroundColor: "#FFFFFF",
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            alignItems: "center",
            gap: 14,
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 24 }}>✉️</div>
          <div>
            <div style={{ fontSize: 13, color: "#64748B", fontWeight: 700, textTransform: "uppercase" }}>Email Us</div>
            <div style={{ fontSize: 20, fontWeight: 800, color: "#0F172A" }}>{THEME.email}</div>
          </div>
        </div>

        {/* WhatsApp Card */}
        <div
          style={{
            padding: "16px 32px",
            borderRadius: 20,
            backgroundColor: "#FFFFFF",
            boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
            display: "flex",
            alignItems: "center",
            gap: 14,
            color: "#0F172A",
          }}
        >
          <div style={{ fontSize: 24 }}>💬</div>
          <div>
            <div style={{ fontSize: 13, color: "#64748B", fontWeight: 700, textTransform: "uppercase" }}>WhatsApp</div>
            <div style={{ fontSize: 20, fontWeight: 800, color: "#0F172A" }}>{THEME.whatsapp}</div>
          </div>
        </div>

        {/* Web Portal Card */}
        <div
          style={{
            padding: "16px 32px",
            borderRadius: 20,
            backgroundColor: "#10B981",
            boxShadow: "0 20px 40px rgba(16, 185, 129, 0.4)",
            display: "flex",
            alignItems: "center",
            gap: 14,
            color: "#FFFFFF",
          }}
        >
          <div style={{ fontSize: 24 }}>🌐</div>
          <div>
            <div style={{ fontSize: 13, color: "rgba(255,255,255,0.8)", fontWeight: 700, textTransform: "uppercase" }}>Schedule Online</div>
            <div style={{ fontSize: 20, fontWeight: 800, color: "#FFFFFF" }}>{THEME.ctaUrl}</div>
          </div>
        </div>
      </div>

      {/* Proposal Launch Offer Pill */}
      <div
        style={{
          opacity: infoOpacity,
          marginTop: 26,
          padding: "8px 24px",
          borderRadius: 20,
          backgroundColor: "rgba(245, 158, 11, 0.15)",
          border: "1.5px solid rgba(245, 158, 11, 0.4)",
          color: "#F59E0B",
          fontSize: 17,
          fontWeight: 700,
          letterSpacing: "0.03em",
        }}
      >
        ⭐ Launch Offer: 20% off setup for our first 3 partner hotels
      </div>
    </div>
  );
};
