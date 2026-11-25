import { loadFont } from "@remotion/google-fonts/Inter";

// Load Inter font family with specific weights
export const { fontFamily } = loadFont("normal", {
  weights: ["400", "500", "600", "700", "800"],
  subsets: ["latin"],
  ignoreTooManyRequestsWarning: true,
});

export const THEME = {
  // Luxury Hotel SaaS Backgrounds & Surfaces
  bg: "#0A1120",              // Deep luxury midnight navy
  bgGradient: "linear-gradient(135deg, #0A1120 0%, #0F172A 50%, #091E3A 100%)",
  surface: "#111C30",          // Dark elevated container
  surfaceLuminous: "#FFFFFF",  // Luminous white UI mockups from proposal
  surfaceSubtle: "#F8FAFC",    // Clean subtle porcelain
  cardBorder: "rgba(255, 255, 255, 0.08)",
  cardBorderLight: "rgba(226, 232, 240, 0.8)",

  // Typography
  textPrimary: "#FFFFFF",
  textSecondary: "#94A3B8",
  textMuted: "#64748B",
  textDark: "#0F172A",
  textDarkSecondary: "#475569",

  // Accent Colors
  accentTeal: "#14B8A6",
  accentEmerald: "#10B981",
  accentTealGlow: "rgba(20, 184, 166, 0.35)",

  // Proposal Exact Room Status Design Tokens (Dual coded: Icon + Pastel Pill)
  status: {
    dirty: {
      color: "#EF4444",           // Deep Red
      dot: "#DC2626",
      bgPastel: "#FEF2F2",
      borderPastel: "#FECACA",
      textDark: "#991B1B",
      bgDark: "rgba(239, 68, 68, 0.15)",
      borderDark: "rgba(239, 68, 68, 0.35)",
      label: "Dirty",
    },
    assigned: {
      color: "#3B82F6",           // Royal Blue
      dot: "#2563EB",
      bgPastel: "#EFF6FF",
      borderPastel: "#BFDBFE",
      textDark: "#1E40AF",
      bgDark: "rgba(59, 130, 246, 0.15)",
      borderDark: "rgba(59, 130, 246, 0.35)",
      label: "Assigned",
    },
    cleaning: {
      color: "#F59E0B",           // Warm Amber
      dot: "#D97706",
      bgPastel: "#FFFBEB",
      borderPastel: "#FDE68A",
      textDark: "#92400E",
      bgDark: "rgba(245, 158, 11, 0.15)",
      borderDark: "rgba(245, 158, 11, 0.35)",
      label: "Cleaning",
    },
    toInspect: {
      color: "#A855F7",           // Elegant Purple
      dot: "#9333EA",
      bgPastel: "#FAF5FF",
      borderPastel: "#E9D5FF",
      textDark: "#6B21A8",
      bgDark: "rgba(168, 85, 247, 0.15)",
      borderDark: "rgba(168, 85, 247, 0.35)",
      label: "Inspect",
    },
    ready: {
      color: "#22C55E",           // Fresh Emerald Green
      dot: "#10B981",
      bgPastel: "#ECFDF5",
      borderPastel: "#A7F3D0",
      textDark: "#065F46",
      bgDark: "rgba(34, 197, 94, 0.15)",
      borderDark: "rgba(34, 197, 94, 0.35)",
      label: "Ready",
    },
    outOfOrder: {
      color: "#64748B",           // Muted Slate Grey
      dot: "#475569",
      bgPastel: "#F1F5F9",
      borderPastel: "#CBD5E1",
      textDark: "#334155",
      bgDark: "rgba(100, 116, 139, 0.15)",
      borderDark: "rgba(100, 116, 139, 0.35)",
      label: "DND / OOO",
    },
  },

  // Typography Scale
  typography: {
    headline: {
      fontSize: 72,
      fontWeight: 800,
      lineHeight: 1.15,
      letterSpacing: "-0.035em",
    },
    headlineSmall: {
      fontSize: 54,
      fontWeight: 700,
      lineHeight: 1.2,
      letterSpacing: "-0.025em",
    },
    subhead: {
      fontSize: 34,
      fontWeight: 500,
      lineHeight: 1.35,
    },
    body: {
      fontSize: 22,
      fontWeight: 400,
      lineHeight: 1.45,
    },
    caption: {
      fontSize: 17,
      fontWeight: 600,
      letterSpacing: "0.06em",
    },
  },

  // Calm, Human Executive Springs (high damping, no jerky cartoon bounce)
  springs: {
    gentle: { damping: 26, mass: 1.0, stiffness: 75 },
    smooth: { damping: 22, mass: 0.9, stiffness: 85 },
    snappy: { damping: 24, mass: 0.7, stiffness: 120 },
  },

  // Official Branding from Proposal
  productName: "RoomReady",
  tagline: "Every room. Live. Ready faster.",
  subTitle: "Hotel Housekeeping Management System",
  teamName: "Team Axio Global",
  email: "axiomglobal30@gmail.com",
  whatsapp: "+94 76 570 9425",
  ctaUrl: "demo.axioglobal.tech",
};
