import React from "react";
import { Series, staticFile, interpolate, useCurrentFrame } from "remotion";
import { Audio } from "@remotion/media";
import { Scene1Problem } from "./scenes/Scene1Problem";
import { Scene2LogoReveal } from "./scenes/Scene2LogoReveal";
import { Scene3RoomBoard } from "./scenes/Scene3RoomBoard";
import { Scene4HousekeeperApp } from "./scenes/Scene4HousekeeperApp";
import { Scene5Inspection } from "./scenes/Scene5Inspection";
import { Scene6Maintenance } from "./scenes/Scene6Maintenance";
import { Scene7Dashboard } from "./scenes/Scene7Dashboard";
import { Scene8CTA } from "./scenes/Scene8CTA";

export const HousekeepingPromo: React.FC = () => {
  const frame = useCurrentFrame();

  // Background music with 1s fade-in (frames 0-30) and 2s fade-out (frames 1740-1800)
  const musicSrc = staticFile("assets/music.mp3");

  const musicVolume = interpolate(
    frame,
    [0, 30, 1740, 1800],
    [0, 0.28, 0.28, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );

  return (
    <div style={{ flex: 1, backgroundColor: "#0F172A", width: "100%", height: "100%" }}>
      {/* Background ambient music bed */}
      <Audio src={musicSrc} volume={musicVolume} />

      {/* Series of scenes sequentially running for exactly 1800 frames (60s) */}
      <Series>
        {/* Scene 1: The problem (0–8s = 240 frames) */}
        <Series.Sequence durationInFrames={240}>
          <Scene1Problem />
        </Series.Sequence>

        {/* Scene 2: Logo reveal (8–13s = 150 frames) */}
        <Series.Sequence durationInFrames={150}>
          <Scene2LogoReveal />
        </Series.Sequence>

        {/* Scene 3: Live Room Board (13–24s = 330 frames) */}
        <Series.Sequence durationInFrames={330}>
          <Scene3RoomBoard />
        </Series.Sequence>

        {/* Scene 4: Housekeeper App (24–34s = 300 frames) */}
        <Series.Sequence durationInFrames={300}>
          <Scene4HousekeeperApp />
        </Series.Sequence>

        {/* Scene 5: Inspection (34–42s = 240 frames) */}
        <Series.Sequence durationInFrames={240}>
          <Scene5Inspection />
        </Series.Sequence>

        {/* Scene 6: Maintenance + Alerts (42–48s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene6Maintenance />
        </Series.Sequence>

        {/* Scene 7: Owner Dashboard (48–54s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene7Dashboard />
        </Series.Sequence>

        {/* Scene 8: Call to Action (54–60s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene8CTA />
        </Series.Sequence>
      </Series>
    </div>
  );
};

