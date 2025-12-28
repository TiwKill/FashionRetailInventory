/**
 * Configuration settings for a single brand's inventory management
 */
export type BrandConfig = {
    /** Starting inventory level */
    initial_stock: number
    /** Days between scheduled restocks */
    restock_days: number
    /** Units added per scheduled restock */
    restock_quantity: number
    /** Stock level that triggers automatic reorder */
    reorder_point: number
    /** Units added when reorder point is triggered */
    reorder_quantity: number
    /** Multiplier applied to base demand (1.0 = normal) */
    demand_multiplier: number
    /** Whether automatic reordering is enabled */
    enable_reorder: boolean
}

/** Brand configurations indexed by brand name */
export type BrandConfigs = Record<string, BrandConfig>

/**
 * Daily simulation data for a single brand
 */
export type DailyData = {
    day: number
    date: string
    brand: string
    demand: number
    sales: number
    stock_before: number
    stock_after: number
    revenue: number
    stockout: number
    lost_sales: number
    price_per_unit: number
    season: string
    season_type: string
    quarter: string
    festival: string
    festival_multiplier: number
}

export type MonthlyData = {
    month: number
    brand: string
    total_sales: number
    total_revenue: number
    avg_stock: number
    stockout_days: number
}

export type RestockEvent = {
    day: number
    brand: string
    quantity: number
    stock_before: number
    stock_after: number
    type: "periodic" | "reorder" // Added type field to distinguish restock types
}

export type ReorderPointEvent = {
    day: number
    brand: string
    stock_level: number
    reorder_point: number
    reorder_quantity: number
    triggered: boolean
}

export type FestivalEvent = {
    day: number
    date: string
    festival_name: string
    multiplier: number
    demand_increase: number
}

export type SeasonEvent = {
    day: number
    date: string
    season_name: string
    season_type: string
    multiplier: number
    demand_increase: number
}

export type BrandSummary = {
    brand: string
    total_units_sold: number
    total_revenue: number
    transactions: number
    restock_count: number
    stockout_days: number
    avg_stock: number
    final_stock: number
    lost_sales_rate: number
    avg_price: number
}

export type BestSellingProduct = {
    brand: string
    month: number
    product: string
    units_sold: number
}

export type MonthlyTrend = {
    month: number
    brand: string
    sales: number
    baseline_units: number
    growth_vs_baseline: number
    mom_growth: number | null
    seasonality_factor: number
    trend: "uptrend" | "downtrend" | "sideways"
    trend_score: number
}

export type TrendEvent = {
    month: number
    brand: string
    from_trend: string | null
    to_trend: string | null
    trend_score: number
    reason: string | null
}

export type ProductMonthlyTrend = {
    brand: string
    product: string
    month: number
    sales: number
    baseline_units: number
    growth_vs_baseline: number
    mom_growth: number | null
    trend: "uptrend" | "downtrend" | "sideways"
    trend_score: number
}

export type ProductTrendEvent = {
    month: number
    brand: string
    product: string
    from_trend: string
    to_trend: string
    trend_score: number
    reason: string
}

export type SimulationResponse = {
    daily_data: DailyData[]
    monthly_data: MonthlyData[]
    restock_events: RestockEvent[]
    reorder_point_events: ReorderPointEvent[] // Added reorder_point_events
    festival_events: FestivalEvent[] // Added festival_events
    season_events: SeasonEvent[] // Added season_events
    summary: BrandSummary[]
    best_selling_products: BestSellingProduct[]
    simulation_days: number
    monthly_trends: MonthlyTrend[] // Added monthly_trends for brand-level trends
    trend_events: TrendEvent[] // Added trend_events for brand-level trend changes
    product_monthly_trends: ProductMonthlyTrend[] // Added product_monthly_trends
    product_trend_events: ProductTrendEvent[] // Added product_trend_events
}

export type BrandParameters = {
    base_demand: number
    seasonality: Record<string, number>
    avg_price: number
    calculated_config: BrandConfig
}

export type BrandParametersResponse = Record<string, BrandParameters>

export const defaultConfigs: BrandConfigs = {
    NIKE: {
        initial_stock: 5000,
        restock_days: 15,
        restock_quantity: 3000,
        reorder_quantity: 1000, // Added reorder_quantity
        reorder_point: 1000,
        demand_multiplier: 1.2,
        enable_reorder: true, // Added enable_reorder
    },
    ADIDAS: {
        initial_stock: 4000,
        restock_days: 20,
        restock_quantity: 2500,
        reorder_quantity: 1000, // Added reorder_quantity
        reorder_point: 800,
        demand_multiplier: 1.0,
        enable_reorder: true, // Added enable_reorder
    },
    PUMA: {
        initial_stock: 3000,
        restock_days: 25,
        restock_quantity: 2000,
        reorder_quantity: 1000, // Added reorder_quantity
        reorder_point: 600,
        demand_multiplier: 0.9,
        enable_reorder: true, // Added enable_reorder
    },
    H_M: {
        initial_stock: 4000,
        restock_days: 20,
        restock_quantity: 2500,
        reorder_quantity: 1000, // Added reorder_quantity
        reorder_point: 800,
        demand_multiplier: 1.0,
        enable_reorder: true, // Added enable_reorder
    },
}
