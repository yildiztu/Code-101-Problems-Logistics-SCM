# PROBLEM NAME COMPARISON REPORT
## LaTeX Files vs Codebase Folders

### CRITICAL ISSUES FOUND:

## 1. P16 DUPLICATION ISSUE ⚠️
**TWO FOLDERS WITH NUMBER 16:**
- `16. The Storage Location Assignment Problem`
- `16. The Container Terminal Yard Truck Scheduling Problem`

**ACTION REQUIRED:** One of these should be renumbered to the correct number based on the LaTeX source.

## 2. PROBLEM NAME MISMATCHES (40 issues)

### Major Mismatches (Complete Different Problems):

| Line | LaTeX Name | Codebase Name | Issue |
|------|------------|---------------|-------|
| 3 | *Title extraction failed* | The Vehicle Routing Problem with Time Windows | LaTeX title corrupted |
| 4 | The FCFS Berth Scheduling Problem | The Inventory Routing Problem with Demand Uncertainty | **Different problems** |
| 7 | The Static Berth Allocation Problem: A Multi-Tier Optimization Approach | The Berth Allocation Problem | Extra detail in LaTeX |
| 8 | *Title extraction failed* | The Quay Crane Assignment Problem | LaTeX title corrupted |
| 14 | The Vessel Stowage Planning Problem (Export) | The Programmable Matter Container Stowage Problem | **Different problems** |
| 15 | The Vessel Re-stow Problem (Transshipment) | The Automated Guided Vehicle Traffic Management Problem | **Different problems** |
| 18 | The Yard Crane (RTG/RMG) Scheduling Problem | The Smart Container Terminal Integration Problem | **Different problems** |
| 19 | The SLAP for Reefer Containers Problem | The Port-Centric Distribution Network Optimization Problem | **Different problems** |
| 24 | *Title extraction failed* | The Static Truck Appointment System Problem | LaTeX title corrupted |
| 27 | *Title extraction failed* | The Integrated Berth & Crane Allocation Problem (BAP-QCAP) | LaTeX title corrupted |
| 29 | *Title extraction failed* | The Integrated Quay Crane & Yard Truck Scheduling Problem | LaTeX title corrupted |
| 30 | *Title extraction failed* | The Yard Pre-Marshalling for Exports Problem | LaTeX title corrupted |
| 38 | *Title extraction failed* | The Automation Investment Analysis Problem | LaTeX title corrupted |
| 63 | *Title extraction failed* | The Zone Picking & Pick-and-Pass Balancing Problem | LaTeX title corrupted |
| 74 | *Title extraction failed* | The VRP with Backhauls Problem | LaTeX title corrupted |
| 76 | *Title extraction failed* | The VRP with Split Deliveries (SDVRP) | LaTeX title corrupted |
| 81 | The 3D Container/Truck Loading Problem | The 3D Container | Truncated name |
| 85 | Problem 85 | The Uncapacitated Facility Location Problem | LaTeX missing title |
| 95 | *Title extraction failed* | The Supply Chain Network Design under Uncertainty Problem | LaTeX title corrupted |

### Minor Mismatches (Formatting/Character Differences):

| Line | LaTeX Name | Codebase Name | Issue |
|------|------------|---------------|-------|
| 26 | The Gate Automation \& Damage Detection Problem | The Gate Automation & Damage Detection Problem | LaTeX escape vs & |
| 28 | The Integrated Crane Assignment \& Scheduling Problem | The Integrated Crane Assignment & Scheduling Problem | LaTeX escape vs & |
| 34 | The Hazard \& IMDG Segregation Problem | The Hazard & IMDG Segregation Problem | LaTeX escape vs & |
| 36 | The Berth \& Quay Length Design Problem | The Berth & Quay Length Design Problem | LaTeX escape vs & |
| 39 | The Channel Dredging \& Deepening Investment Problem | The Channel Dredging & Deepening Investment Problem | LaTeX escape vs & |
| 40 | The Port Capacity \& Expansion Timing Problem | The Port Capacity & Expansion Timing Problem | LaTeX escape vs & |
| 42 | The Peak Energy Consumption \& Load Shifting Problem | The Peak Energy Consumption & Load Shifting Problem | LaTeX escape vs & |
| 48 | The Demand Forecasting Problem | The Demand Forecasting - Exponential Smoothing Problem | Extra detail in Codebase |
| 50 | The New Product Forecasting Problem (Look-Alike Modeling) | The New Product Forecasting Problem | Extra detail in LaTeX |
| 52 | *Title extraction failed* | The EOQ with Quantity Discounts Problem | LaTeX title corrupted |
| 56 | The Safety Stock \& Reorder Point (Q,r) Policy Problem | The Safety Stock & Reorder Point (Q,r) Policy Problem | LaTeX escape vs & |
| 58 | The ABC/XYZ Inventory Classification Problem | The ABC_XYZ Inventory Classification Problem | / vs _ |
| 65 | The 3D Pallet/Case Packing Problem | The 3D Pallet_Case Packing Problem | / vs _ |
| 66 | The Workforce Scheduling for Peak/Off-Peak Problem | The Workforce Scheduling for Peak_Off-Peak Problem | / vs _ |
| 67 | The Kitting \& Value-Added Service Scheduling Problem | The Kitting & Value-Added Service Scheduling Problem | LaTeX escape vs & |
| 68 | The AS/RS Task Interleaving Problem | The AS_RS Task Interleaving Problem | / vs _ |
| 77 | The Dynamic \& Real-Time VRP | The Dynamic & Real-Time VRP | LaTeX escape vs & |
| 79 | The Freight Carrier Selection \& Bidding Problem | The Freight Carrier Selection & Bidding Problem | LaTeX escape vs & |
| 95 | *Title extraction failed* | The Supply Chain Network Design under Uncertainty Problem | LaTeX title corrupted |
| 97 | The Last-Mile Delivery \& Micro-Fulfillment Problem | The Last-Mile Delivery & Micro-Fulfillment Problem | LaTeX escape vs & |
| 101 | The Supply Chain Finance \& Working Capital Optimization P | The Supply Chain Finance & Working Capital Optimization Problem | Truncated |

## 3. SUMMARY STATISTICS

- **Total Problems:** 101
- **Perfect Matches:** 61 (60.4%)
- **Mismatches:** 40 (39.6%)
- **Critical Issues:** 21 (completely different problems or title extraction failures)
- **Minor Issues:** 19 (formatting/character differences)

## 4. RECOMMENDATIONS

### Immediate Actions Required:

1. **Fix P16 Duplication:**
   - Check LaTeX files to determine which problem should be #16
   - Rename one folder to the correct number
   - Move notebooks accordingly

2. **Fix Major Mismatches:**
   - Lines 4, 14, 15, 18, 19: Completely different problems - verify correct numbering
   - Lines with title extraction failures: Check LaTeX source files
   - Line 85: Missing title in LaTeX source

3. **Fix Minor Formatting Issues:**
   - Replace `\&` with `&` in folder names
   - Replace `/` with `_` in folder names
   - Handle truncated names

### Priority Order:
1. **HIGH:** P16 duplication issue
2. **HIGH:** Major mismatches (different problems)
3. **MEDIUM:** Title extraction failures
4. **LOW:** Minor formatting issues

## 5. NEXT STEPS

1. Examine LaTeX files for problematic lines to extract correct titles
2. Verify correct numbering for P16 duplication
3. Create folder renaming script
4. Move notebooks to corrected folders
5. Validate all corrections

---
**Report Generated:** 2025-03-30
**Total Issues:** 40 mismatches + 1 duplication = 41 issues to resolve
