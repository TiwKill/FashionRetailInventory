/**
 * Utility functions for chart visualization
 */

import { CHART_COLORS, BRAND_COLORS } from "./constants"

/**
 * Get a consistent color for a brand based on its position in the selected brands array
 * @param brand - The brand name to get color for
 * @param selectedBrands - Array of currently selected brands
 * @returns Hex color string
 */
export function getBrandColor(brand: string, selectedBrands: string[]): string {
    const index = selectedBrands.indexOf(brand)
    return CHART_COLORS[index % CHART_COLORS.length]
}

/**
 * Get a color from extended brand palette (for store simulation)
 * @param index - Index in the brand array
 * @returns Hex color string
 */
export function getExtendedBrandColor(index: number): string {
    return BRAND_COLORS[index % BRAND_COLORS.length]
}
