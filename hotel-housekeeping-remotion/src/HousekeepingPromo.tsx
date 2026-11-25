import React from "react";
import { Series, staticFile, interpolate, useCurrentFrame } from "remotion";
import { Audio } from "@remotion/media";
import { THEME } from "./theme";
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

  // Background music bed with smooth 1.5s fade-in and 2s fade-out
  const musicSrc = staticFile("assets/music.mp3");

  const musicVolume = interpolate(
    frame,
    [0, 45, 1740, 1800],
    [0, 0.22, 0.22, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }
  );

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: THEME.bg,
        width: "100%",
        height: "100%",
        position: "relative",
      }}
    >
      {/* Background ambient luxury music bed */}
      <Audio src={musicSrc} volume={musicVolume} />

      {/* Series of scenes sequentially running for exactly 1,800 frames (60.00s @ 30fps) */}
      <Series>
        {/* Scene 1: The problem (0–7.5s = 225 frames) */}
        <Series.Sequence durationInFrames={225}>
          <Scene1Problem />
        </Series.Sequence>

        {/* Scene 2: Logo reveal (7.5–13.5s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene2LogoReveal />
        </Series.Sequence>

        {/* Scene 3: Live Room Board (13.5–24.0s = 315 frames) */}
        <Series.Sequence durationInFrames={315}>
          <Scene3RoomBoard />
        </Series.Sequence>

        {/* Scene 4: Housekeeper App (24.0–33.5s = 285 frames) */}
        <Series.Sequence durationInFrames={285}>
          <Scene4HousekeeperApp />
        </Series.Sequence>

        {/* Scene 5: Inspection & Live Sync (33.5–41.5s = 240 frames) */}
        <Series.Sequence durationInFrames={240}>
          <Scene5Inspection />
        </Series.Sequence>

        {/* Scene 6: Maintenance & Alerts (41.5–47.5s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene6Maintenance />
        </Series.Sequence>

        {/* Scene 7: Owner Dashboard (47.5–53.5s = 180 frames) */}
        <Series.Sequence durationInFrames={180}>
          <Scene7Dashboard />
        </Series.Sequence>

        {/* Scene 8: Call to Action (53.5–60.0s = 195 frames) */}
        <Series.Sequence durationInFrames={195}>
          <Scene8CTA />
        </Series.Sequence>
      </Series>
    </div>
  );
};
