import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

/**
 * Convert brand name to API-compatible key format
 * Examples: "H&M" -> "h_m", "NEW BALANCE" -> "new_balance"
 */
export function brandToApiKey(brand: string): string {
  return brand
    .toLowerCase()
    .replace(/&/g, "_")
    .replace(/\s+/g, "_")
    .replace(/-/g, "_")
}

