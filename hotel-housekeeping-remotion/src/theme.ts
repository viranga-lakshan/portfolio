import { loadFont } from "@remotion/google-fonts/Inter";

// Load Inter font family with specific weights
export const { fontFamily } = loadFont("normal", {
  weights: ["400", "600", "700", "800"],
  subsets: ["latin"],
  ignoreTooManyRequestsWarning: true,
});

export const THEME = {
  // Backgrounds & Surface
  bg: "#0F172A",          // Dark navy
  surface: "#1E293B",     // Dark card surface
  surfaceElevated: "#334155", // Hover / elevated surface
  border: "#334155",
  borderLight: "#475569",

  // Typography
  textPrimary: "#FFFFFF",
  textSecondary: "#94A3B8",
  textMuted: "#64748B",

  // Accent
  accentTeal: "#14B8A6",
  accentTealGlow: "rgba(20, 184, 166, 0.35)",

  // Mandatory Room Status Colors (Never change, used consistently)
  status: {
    dirty: {
      color: "#EF4444",      // Red
      bg: "rgba(239, 68, 68, 0.15)",
      border: "rgba(239, 68, 68, 0.35)",
      label: "Dirty",
    },
    assigned: {
      color: "#3B82F6",      // Blue
      bg: "rgba(59, 130, 246, 0.15)",
      border: "rgba(59, 130, 246, 0.35)",
      label: "Assigned",
    },
    cleaning: {
      color: "#F59E0B",      // Amber
      bg: "rgba(245, 158, 11, 0.15)",
      border: "rgba(245, 158, 11, 0.35)",
      label: "Cleaning",
    },
    toInspect: {
      color: "#A855F7",      // Purple
      bg: "rgba(168, 85, 247, 0.15)",
      border: "rgba(168, 85, 247, 0.35)",
      label: "To Inspect",
    },
    ready: {
      color: "#22C55E",      // Green
      bg: "rgba(34, 197, 94, 0.15)",
      border: "rgba(34, 197, 94, 0.35)",
      label: "Ready",
    },
    outOfOrder: {
      color: "#64748B",      // Grey
      bg: "rgba(100, 116, 139, 0.15)",
      border: "rgba(100, 116, 139, 0.35)",
      label: "Out of Order",
    },
  },

  // Font typography scale
  typography: {
    headline: {
      fontSize: 72,
      fontWeight: 800,
      lineHeight: 1.15,
      letterSpacing: "-0.03em",
    },
    headlineSmall: {
      fontSize: 54,
      fontWeight: 700,
      lineHeight: 1.2,
      letterSpacing: "-0.02em",
    },
    subhead: {
      fontSize: 36,
      fontWeight: 500,
      lineHeight: 1.35,
    },
    body: {
      fontSize: 24,
      fontWeight: 400,
      lineHeight: 1.4,
    },
    caption: {
      fontSize: 18,
      fontWeight: 600,
      letterSpacing: "0.05em",
    },
  },

  // Animation Springs
  springs: {
    smooth: { damping: 16, mass: 0.8, stiffness: 100 },
    bouncy: { damping: 12, mass: 0.6, stiffness: 120 },
    snappy: { damping: 20, mass: 0.5, stiffness: 160 },
    gentle: { damping: 24, mass: 1.0, stiffness: 80 },
  },

  // Product branding
  productName: "RoomFlow",
  tagline: "Every room. Live. Ready faster.",
  teamName: "Team Axio Global",
  contact: "demo.axioglobal.tech",
};
