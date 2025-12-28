/**
 * Shared constants for the Fashion Retail Inventory application
 */

/** Chart colors for data visualization (10 colors) */
export const CHART_COLORS = [
    "#3b82f6", // Blue
    "#10b981", // Emerald
    "#f59e0b", // Amber
    "#ef4444", // Red
    "#8b5cf6", // Violet
    "#ec4899", // Pink
    "#06b6d4", // Cyan
    "#f97316", // Orange
    "#14b8a6", // Teal
    "#6366f1", // Indigo
] as const

/** Extended brand colors for store simulation (23 colors) */
export const BRAND_COLORS = [
    "#f97316", // orange
    "#3b82f6", // blue
    "#8b5cf6", // purple
    "#10b981", // green
    "#ef4444", // red
    "#f59e0b", // amber
    "#06b6d4", // cyan
    "#ec4899", // pink
    "#84cc16", // lime
    "#6366f1", // indigo
    "#14b8a6", // teal
    "#f43f5e", // rose
    "#a855f7", // violet
    "#22c55e", // emerald
    "#eab308", // yellow
    "#0ea5e9", // sky
    "#d946ef", // fuchsia
    "#64748b", // slate
    "#78716c", // stone
    "#dc2626", // red-600
    "#2563eb", // blue-600
    "#7c3aed", // violet-600
    "#059669", // emerald-600
] as const

/** Month name abbreviations */
export const MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
] as const

/** Festival configurations with default demand multipliers */
export const FESTIVALS = [
    { id: "new_year", name: "New Year Sale", defaultMultiplier: 1.8 },
    { id: "valentines", name: "Valentine's Day", defaultMultiplier: 1.3 },
    { id: "womens_day", name: "Women's Day", defaultMultiplier: 1.2 },
    { id: "songkran", name: "Songkran", defaultMultiplier: 1.4 },
    { id: "mothers_day", name: "Mother's Day", defaultMultiplier: 1.5 },
    { id: "midyear", name: "Mid-Year Sale", defaultMultiplier: 1.6 },
    { id: "fathers_day", name: "Father's Day", defaultMultiplier: 1.3 },
    { id: "back_to_school", name: "Back to School", defaultMultiplier: 1.7 },
    { id: "halloween", name: "Halloween", defaultMultiplier: 1.2 },
    { id: "singles_day", name: "Singles' Day (11.11)", defaultMultiplier: 2.5 },
    { id: "black_friday", name: "Black Friday", defaultMultiplier: 2.2 },
    { id: "cyber_monday", name: "Cyber Monday", defaultMultiplier: 2.0 },
    { id: "christmas", name: "Christmas", defaultMultiplier: 2.0 },
    { id: "year_end", name: "Year-End Sale", defaultMultiplier: 1.9 },
] as const

export type Festival = typeof FESTIVALS[number]
