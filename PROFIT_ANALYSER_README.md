# Profit Analyser Module

## Overview
The Profit Analyser helps farmers analyze tomato crop profitability with government-based subsidies and realistic market projections.

## Features

### Input Form
- **Crop Type**: Tomato, Cherry Tomato, Roma Tomato, Beefsteak Tomato
- **Growing Season**: Summer, Monsoon, Post Monsoon, Winter
- **Land Size**: Acres (decimal input)
- **Number of Plants**: Integer input
- **Farming Type**: Traditional, Modern/Scientific, Greenhouse
- **Organic Farming**: Yes/No

### Analysis Output

#### 1. Farm Details Summary
- Shows all input parameters in a clean card layout

#### 2. Expected Yield
- Total yield in kg and quintals
- Quality distribution:
  - Grade A (premium quality)
  - Grade B (standard quality)
  - Grade C (basic quality)

#### 3. Revenue Estimation
- Market Revenue (based on grade-wise pricing)
- MSP Revenue (Minimum Support Price)

#### 4. Input Costs & Subsidies
- Detailed cost breakdown:
  - Seeds & Seedlings
  - Fertilizers & Pesticides
  - Irrigation & Electricity
  - Labor Costs
  - Equipment & Maintenance
- Government subsidies:
  - PMKSY (Pradhan Mantri Krishi Sinchayee Yojana)
  - Soil Health Card
  - Organic Farming Scheme (if applicable)
  - Farm Mechanization
  - Seed Subsidy
- Net Input Cost (after subsidies)

#### 5. Profitability Analysis
- Net Profit
- Profit Margin (%)
- ROI - Return on Investment (%)
- AI-powered recommendations

## Backend Logic

### Data Sources
1. **Primary**: Government agriculture data (simulated)
   - MSP rates
   - Subsidy schemes (PMKSY, Organic Farming, etc.)
   - Yield benchmarks

2. **Fallback**: Realistic randomized values
   - Market prices with variance
   - Seasonal multipliers
   - Farming type efficiency factors

### Calculation Methodology

#### Yield Calculation
```
Base Yield = Plants × Yield per Plant × Season Multiplier × Organic Factor
```

Yield per plant varies by farming type:
- Traditional: 2.5-3.5 kg
- Modern/Scientific: 3.5-5.0 kg
- Greenhouse: 5.0-7.5 kg

#### Cost Calculation
- Seeds: Based on farming type and number of plants
- Fertilizers: Per acre cost × land size
- Irrigation: Per acre cost (higher for greenhouse)
- Labor: Per acre labor cost × land size
- Equipment: Per acre equipment cost × land size

#### Subsidy Calculation
Based on government schemes:
- Irrigation subsidy (PMKSY)
- Soil health support
- Organic farming incentives
- Mechanization support
- Seed subsidy

#### Profitability Metrics
```
Net Profit = Market Revenue - Net Input Cost
Profit Margin = (Net Profit / Revenue) × 100
ROI = (Net Profit / Net Input Cost) × 100
```

## UI Design
- Green theme matching the main application
- Card-based layout with icons
- Color-coded metrics (green for positive, red for negative)
- Responsive grid layouts
- Professional gradient backgrounds
- Clear visual hierarchy

## Routes

### GET `/profit-analyser`
Displays input form

### POST `/profit-analyser/analyse`
Processes form data and displays results

## Future Enhancements
- Real-time government API integration
- Historical data tracking
- Multi-season comparison
- Export reports as PDF
- Weather-based yield adjustments
- Market price predictions using ML
