# AI Development Notes — ROI Dashboard

## 1. Project Overview

The ROI Dashboard was developed as the working prototype for the FreshBrew Franchise Expansion Decision Tool. AI assistance was used for the initial development, financial logic implementation, Streamlit development, debugging, and UI refinement.

The final prototype allows a user to enter key franchise assumptions and evaluate unit economics, profitability, ROI, payback period, investment recommendation, and revenue scenarios.

---

## 2. AI Prompts Used During Development

The following are consolidated prompts representing the main AI-assisted development requests used during the project.

### Prompt 1 — Build the ROI Dashboard

> Create a working ROI dashboard for the FreshBrew franchise expansion decision tool using Python and Streamlit. The dashboard should allow the user to enter monthly revenue, COGS percentage, initial investment, monthly rent, staff cost and marketing percentage, and calculate gross profit, operating expenses, operating profit, annual operating profit, ROI and simple payback period. It should also provide an investment recommendation based on profitability and payback period.

### Prompt 2 — Add Scenario Analysis

> Add a revenue scenario analysis to the ROI dashboard with three cases: ₹6 lakh Conservative, ₹8 lakh Base Case and ₹10 lakh Optimistic. For each scenario calculate monthly operating profit, annual operating profit, payback period and annual ROI, and provide a GO, REVIEW or NO-GO decision.

### Prompt 3 — Improve the Dashboard UI

> Improve the Streamlit dashboard design so that it looks professional and suitable for a portfolio project. Use a dark theme, clear section headings, visually distinct cards for key metrics and financial information, and make the investment decision and scenario analysis easy to understand.

### Prompt 4 — Improve the Scenario Cards

> Make the revenue scenario analysis display the three scenarios as separate cards. Each card should clearly show monthly revenue, monthly operating profit, payback period, annual ROI and the corresponding GO, REVIEW or NO-GO decision with visually distinct decision styling.

### Prompt 5 — Improve the Investment Decision Section

> Redesign the Investment Decision section as a clear card that highlights the recommendation, explanation and Annual ROI, while maintaining the existing financial calculations and decision logic.

---

## 3. What AI Got Wrong

The AI-generated output required several rounds of testing and refinement before the dashboard reached its final form.

The main issues encountered were:

- The initial dashboard styling did not provide enough visual distinction between section headings, content and cards.
- Some cards and decision elements were difficult to distinguish against the dark background.
- The scenario cards required repeated adjustments to spacing, sizing, borders and decision styling.
- The Investment Decision section required redesigning so that the recommendation, explanation and Annual ROI were clearly presented together.
- The dashboard header required refinement to make the main title more prominent and visually separated from the subtitle and description.
- The chart and other sections required layout adjustments to avoid excessive stretching.
- Streamlit produced a warning regarding the deprecated `use_container_width` parameter, which required updating to the newer `width` parameter.
- AI-generated code was not treated as automatically correct; the financial outputs and presentation were tested and reviewed before finalizing the prototype.

---

## 4. What Was Fixed Manually

The generated dashboard was manually reviewed and refined throughout development.

The following changes were made:

- Verified the financial calculations against the underlying financial model.
- Tested the dashboard using the base-case assumptions.
- Adjusted CSS and HTML styling to improve card visibility and contrast.
- Improved spacing, padding, borders and sizing of dashboard cards.
- Redesigned the Investment Decision section to clearly display the recommendation and Annual ROI.
- Added separate visual cards for the Conservative, Base Case and Optimistic revenue scenarios.
- Added visually distinct decision states for GO, REVIEW and NO-GO.
- Refined the dashboard header and overall page width.
- Adjusted the chart presentation so it fit the dashboard more appropriately.
- Updated deprecated Streamlit configuration usage.
- Organized the final Python file and screenshots into a GitHub-ready project structure.
- Manually reviewed the final dashboard before treating it as the completed prototype.

---

## 5. Base Case Validation

The final dashboard was tested using the following base-case assumptions:

| Input | Value |
|---|---:|
| Monthly Revenue | ₹8,00,000 |
| COGS | 30% |
| Initial Investment | ₹20,00,000 |
| Monthly Rent | ₹1,00,000 |
| Monthly Staff Cost | ₹1,80,000 |
| Marketing | 6% |

The resulting outputs were:

| Metric | Result |
|---|---:|
| Gross Profit | ₹5,60,000 |
| Monthly Operating Profit | ₹1,22,000 |
| Annual Operating Profit | ₹14,64,000 |
| Simple Payback | 1.37 years |
| Annual ROI | 73.2% |
| Investment Decision | GO |

The scenario analysis was also tested at:

- ₹6 lakh — Conservative
- ₹8 lakh — Base Case
- ₹10 lakh — Optimistic

---

## 6. What I Would Improve With One More Day

With one additional day, I would improve the dashboard by adding a more detailed sensitivity analysis, allowing users to test a wider range of revenue and cost assumptions rather than only the predefined scenarios.

I would also:

- Add additional financial KPIs and visualizations.
- Improve input validation.
- Further refine responsiveness and user experience.
- Add clearer explanations of the financial assumptions.
- Provide more flexibility in the scenario analysis.
- Improve the dashboard's usability for a non-technical business user.

---

## 7. Role of AI in the Development Process

AI was used as a development and problem-solving assistant rather than as a substitute for validation.

The final prototype involved human review of the financial logic, testing of outputs, iterative UI refinement, debugging, and organization of the project for presentation.

The development process therefore followed an iterative cycle:

**AI-assisted generation → testing → identify issues → manual correction → retesting → final prototype**
