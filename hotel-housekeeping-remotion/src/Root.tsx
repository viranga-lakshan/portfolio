import React from "react";
import { Composition } from "remotion";
import { HousekeepingPromo } from "./HousekeepingPromo";

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="HousekeepingPromo"
        component={HousekeepingPromo}
        durationInFrames={1800}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};

