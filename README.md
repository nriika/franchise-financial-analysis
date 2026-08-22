
# FreshBrew Franchise Financial Analysis & ROI Automation

## Project Overview

This project presents a financial analysis, franchise investment evaluation, ROI dashboard, and AI-enabled lead qualification workflow for **FreshBrew**, including an illustrative **Scale100x franchise expansion scenario**.

The project combines financial modelling, scenario analysis, payback analysis, franchise revenue projections, lead scoring, ROI visualization, and an automation prototype into one decision-support framework.

The objective is to evaluate:

- Franchise investment feasibility
- Revenue and profitability under different scenarios
- Operating costs and operating profit
- Investment payback
- Scale100x franchise revenue potential
- Franchise lead qualification and prioritization
- Potential operational time savings through automation
- Key risks and human checkpoints in an AI-enabled workflow

> **Important:** The financial assumptions used in this project are illustrative modelling assumptions created for the assignment. They should not be interpreted as actual FreshBrew or Scale100x commercial pricing, financial disclosures, or guaranteed business results.

---

## Project Objectives

The project was developed to answer the following business questions:

1. Is the franchise investment financially viable?
2. How does profitability change under conservative, base, and optimistic revenue scenarios?
3. How long would it take to recover the initial investment?
4. What could Scale100x revenue look like over a three-year illustrative scenario?
5. Which franchise leads should receive the highest sales priority?
6. How could AI and automation reduce manual lead-processing time?
7. What risks should be considered when implementing an AI-enabled lead qualification process?

---

## Repository Structure

    franchise-financial-analysis/
    │
    ├── financial-model/
    │   ├── screenshots/
    │   │   ├── assumptions.png
    │   │   ├── monthly-P&L.png
    │   │   ├── payback.png
    │   │   ├── scalex_projection.png
    │   │   ├── sensitivity.png
    │   │   └── lead-scoring.png
    │   │
    │   ├── FreshBrew_Franchise_Financial_Model.xlsx
    │   └── README.md
    │
    ├── roi-dashboard/
    │   ├── screenshots/
    │   │   ├── dashboard_inputs.png
    │   │   ├── investment_decision.png
    │   │   ├── profit_scenario_chart.png
    │   │   ├── revenue_scenarios.png
    │   │   └── unit_economics.png
    │   │
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── AI-Development-Notes.md
    │   └── README.md
    │
    └── README.md

---

# 1. Financial Model

The `financial-model` folder contains the Excel-based financial model developed for the FreshBrew franchise analysis.

The model converts the core assumptions into monthly and annual financial outputs and evaluates franchise economics under multiple scenarios.

### Financial Model Components

The financial model includes:

- Base Case Assumptions
- Franchise / Scale100x Assumptions
- Revenue Ramp-up Assumptions
- Year 1 Monthly P&L
- Franchise Payback Analysis
- Scale100x 3-Year Revenue Projection
- Revenue Sensitivity Analysis
- Qualification Checks
- Lead Scoring

---

## Base Case Assumptions

The model uses the following illustrative assumptions:

| Assumption | Value |
|---|---:|
| Initial Investment | ₹20,00,000 |
| Base Monthly Revenue | ₹8,00,000 |
| Conservative Monthly Revenue | ₹6,00,000 |
| Optimistic Monthly Revenue | ₹10,00,000 |
| COGS | 30% of revenue |
| Monthly Rent | ₹1,00,000 |
| Monthly Staff Cost | ₹1,80,000 |
| Marketing | 6% of revenue |
| Monthly Utilities | ₹30,000 |
| Other Monthly Costs | ₹40,000 |
| Franchise Fee | ₹5,00,000 |
| Royalty | 5% of revenue |
| Scale100x Fee per Successful Deal | ₹50,000 |
| Monthly Revenue Ramp-up | ₹50,000 |
| Scale100x Annual Deal Growth | 100% |
| Initial Month Revenue | ₹5,00,000 |

These values are used as modelling assumptions for the assignment and are not presented as verified company pricing.

---

## Year 1 Monthly P&L

The Year 1 P&L models monthly revenue growth from an illustrative starting revenue of ₹5,00,000.

The revenue increases by ₹50,000 per month until reaching the ₹8,00,000 base-case monthly revenue level.

The P&L calculates:

- Revenue
- COGS
- Gross Profit
- Rent
- Staff Cost
- Marketing
- Utilities
- Other Costs
- Royalty
- Total Operating Expenses
- Operating Profit

Under the base case, Year 1 revenue is approximately **₹85,50,000**.

Year 1 operating profit is approximately **₹8,44,500**.

The model also shows that the business initially operates at a loss during the early revenue ramp-up months before becoming profitable.

---

## Franchise Payback Analysis

The payback analysis tracks the relationship between monthly operating profit and the initial investment.

The model includes:

- Monthly operating profit
- Cumulative profit
- Investment remaining

The analysis allows the user to see how the initial investment is progressively recovered through operating profits.

Based on the Year 1 base-case assumptions, the full initial investment is not recovered within the first year.

---

## Scale100x 3-Year Revenue Projection

The Scale100x projection models an illustrative three-year franchise deal scenario.

The assumptions include:

- Year 1 successful franchise deals: 50
- Annual deal growth: 100%
- Scale100x fee per successful deal: ₹50,000

This produces the following illustrative projection:

| Metric | Year 1 | Year 2 | Year 3 |
|---|---:|---:|---:|
| Successful Franchise Deals | 50 | 100 | 200 |
| Scale100x Revenue | ₹25,00,000 | ₹50,00,000 | ₹1,00,00,000 |

The projection is intended to demonstrate how revenue could scale under the stated illustrative assumptions.

---

## Revenue Sensitivity Analysis

The sensitivity analysis compares three monthly revenue scenarios:

- ₹6,00,000 Conservative Case
- ₹8,00,000 Base Case
- ₹10,00,000 Optimistic Case

For each scenario, the model calculates:

- Annual Revenue
- Annual COGS
- Annual Gross Profit
- Annual Marketing
- Annual Royalty
- Annual Fixed Costs
- Annual Operating Profit
- Initial Investment
- Simple Payback

This allows the financial viability of the franchise to be assessed under different revenue conditions rather than relying only on the base case.

---

## Qualification Checks

The model includes qualification checks for:

- Investment
- Revenue
- Experience

An overall qualification output is also included to provide a simple decision indicator.

---

## Lead Scoring

The financial model includes an illustrative franchise lead-scoring framework.

The factors considered are:

| Factor | Score | Max Score |
|---|---:|---:|
| Investment Capacity | 30 | 30 |
| Revenue Potential | 25 | 30 |
| F&B Experience | 15 | 20 |
| Existing Outlet Experience | 5 | 10 |
| Funding Requirement | 10 | 10 |
| **Total Lead Score** | **85** | **100** |

The illustrative lead receives a **HIGH** priority classification with the recommendation:

**Prioritize for sales call**

The scoring framework is intended to demonstrate a structured approach to franchise lead prioritization. 

---

# 2. ROI Dashboard

The `roi-dashboard` folder contains the interactive ROI dashboard developed using **Python and Streamlit**.

The dashboard converts the financial analysis into an interactive interface that allows users to explore key assumptions, compare revenue scenarios, evaluate profitability, understand unit economics, and assess the resulting investment decision.

The dashboard is designed to make the financial analysis easier to explore without requiring users to work directly with the underlying Excel model.

---

## Dashboard Features

The ROI dashboard includes the following major components:

- Dashboard Inputs
- Revenue Scenario Analysis
- Profit Scenario Analysis
- Unit Economics
- Investment Decision
- Interactive financial outputs

The dashboard allows users to modify relevant assumptions and observe how the resulting financial metrics change.

---

## Live Dashboard

The completed ROI dashboard has been deployed using Streamlit and is available at:

**[FreshBrew ROI Dashboard](https://freshbrew-roi-dashboard.streamlit.app/)**

The live prototype provides an interactive version of the financial analysis developed as part of the project.

---

## Dashboard Inputs

The dashboard provides inputs for key financial assumptions used in evaluating the franchise opportunity.

These include relevant variables such as:

- Initial investment
- Revenue assumptions
- Cost assumptions
- Operating expenses
- Royalty assumptions
- Other financial inputs

The purpose of the input section is to allow users to test different assumptions rather than relying on a single fixed scenario.

---

## Revenue Scenario Analysis

The dashboard presents multiple revenue scenarios to demonstrate how different levels of monthly revenue affect franchise economics.

The analysis considers:

- Conservative scenario
- Base scenario
- Optimistic scenario

This allows users to compare the resulting revenue and profitability outcomes across different operating conditions.

---

## Profit Scenario Analysis

The profit analysis presents the impact of different revenue assumptions on operating profitability.

It allows the user to compare the expected operating performance across scenarios and understand the relationship between revenue and profit.

---

## Unit Economics

The unit economics section provides a consolidated view of the major financial components of operating a franchise unit.

The analysis considers the relationship between:

- Revenue
- Cost of goods sold
- Gross profit
- Operating expenses
- Royalty
- Operating profit
- Initial investment

This provides a simplified view of the economics of an individual franchise unit.

---

## Investment Decision

The dashboard translates the financial analysis into an investment-oriented decision view.

The decision is based on the financial outputs generated from the underlying assumptions and scenario analysis.

This section is intended to help users quickly understand the overall attractiveness of the franchise opportunity under the selected assumptions.

---

# 3. AI-Enabled Lead Qualification & Automation

The project also includes an illustrative AI-enabled workflow for franchise lead qualification and sales operations.

The objective of the workflow is to reduce repetitive manual work involved in collecting lead information, qualifying prospects, creating CRM records, and prioritising leads for consultant follow-up.

The proposed workflow is:

    Meta Ads
        ↓
    WhatsApp Conversation
        ↓
    AI Qualification
        ↓
    Lead Information Extraction
        ↓
    CRM Record Creation
        ↓
    Lead Scoring
        ↓
    Lead Prioritisation
        ↓
    Consultant Notification
        ↓
    Human Sales Follow-up
        ↓
    Deal / Next Action

---

## Automation Workflow

### 1. Lead Generation

A potential franchise prospect enters the funnel through a Meta advertisement.

### 2. WhatsApp Qualification

The prospect is directed into a WhatsApp conversation where initial qualification questions can be asked.

### 3. AI-Assisted Qualification

An AI agent can assist with collecting relevant information from the prospect, such as:

- Investment capacity
- Location
- Business or F&B experience
- Existing outlet experience
- Funding requirements
- Franchise interest

### 4. Information Extraction

The relevant information provided during the conversation can be structured into fields that can be used for lead qualification.

### 5. CRM Record

The lead information can then be transferred into a CRM system to create or update the corresponding lead record.

### 6. Lead Scoring

The lead is evaluated using the lead-scoring framework developed in the financial model.

### 7. Lead Prioritisation

Based on the resulting score and qualification information, the lead can be classified according to its priority.

### 8. Consultant Follow-up

High-priority or high-intent leads can be routed to a consultant for further discussion.

### 9. Human Decision

The consultant remains responsible for the final sales conversation, opportunity evaluation, and conversion decision.

---

# 4. Automation Time-Saving Analysis

The project includes an illustrative comparison between the existing manual lead-processing approach and the proposed automated workflow.

The analysis considers:

- Manual processing time per lead
- Automated processing time per lead
- Time saved per lead
- Illustrative monthly lead volume
- Total monthly time saved
- Potential monthly hours saved

The purpose of this analysis is to demonstrate the operational efficiency that could be achieved by automating repetitive lead qualification and administrative activities.

The estimated savings are illustrative and would depend on actual lead volume, workflow implementation, AI accuracy, CRM integration, and the level of human review required.

---

# 5. AI Risk & Human Oversight

Although AI can reduce repetitive manual work, the project recognises that automated lead qualification can introduce risks.

### Key Risks

Potential risks include:

- Incorrect interpretation of lead responses
- Incomplete information
- Incorrect lead classification
- Incorrect scoring
- False prioritisation
- Loss of context in automated conversations
- Over-reliance on automated recommendations

### Human Checkpoints

To address these risks, human oversight is retained at important stages of the workflow.

Human review should be considered particularly for:

- Ambiguous responses
- Incomplete lead information
- Borderline lead scores
- High-value prospects
- Unusual or complex cases
- Final sales and investment decisions

The proposed approach therefore uses AI as an **assistive tool rather than a complete replacement for human decision-making**.

---

# 6. Technology Stack

## Financial Model

- Microsoft Excel
- Financial modelling
- Scenario analysis
- Sensitivity analysis
- Formula-based calculations

## ROI Dashboard

- Python
- Streamlit
- Interactive financial calculations
- Data visualization

## Automation Workflow

- AI-assisted lead qualification
- WhatsApp-based lead interaction
- CRM workflow
- Lead scoring
- Automated prioritisation
- Human-in-the-loop review

## Version Control & Documentation

- GitHub
- Markdown
- Streamlit deployment

---

# 7. Screenshots

Screenshots of the completed work are included in the respective folders for documentation and reference.

## ROI Dashboard Screenshots

The dashboard screenshots are available in:

`roi-dashboard/screenshots/`

The folder contains screenshots covering:

- Dashboard Inputs
- Revenue Scenarios
- Profit Scenario Analysis
- Unit Economics
- Investment Decision

### Roi-Dashboard 

![Roi-Dashboard](roi-dashboard/screenshots/roi-dashboard.png)


---

## Financial Model Screenshots

The financial model screenshots are available in:

`financial-model/screenshots/`

The folder contains screenshots covering:

- Base Case Assumptions
- Year 1 Monthly P&L
- Franchise Payback Analysis
- Scale100x 3-Year Revenue Projection
- Revenue Sensitivity Analysis
- Lead Scoring

### Base Case Assumptions

![Base Case Assumptions](financial-model/screenshots/assumptions.png)

### Year 1 Monthly P&L

![Year 1 Monthly P&L](financial-model/screenshots/monthly-P&L.png)

### Franchise Payback Analysis

![Franchise Payback Analysis](financial-model/screenshots/payback.png)

### Scale100x 3-Year Revenue Projection

![Scale100x Projection](financial-model/screenshots/scalex_projection.png)

### Revenue Sensitivity Analysis

![Revenue Sensitivity Analysis](financial-model/screenshots/sensitivity.png)

### Lead Scoring

![Lead Scoring](financial-model/screenshots/lead-scoring.png)

---

# 8. Key Business Insights

The combined financial model and dashboard provide a structured view of the franchise opportunity.

### Revenue

The model evaluates the franchise under conservative, base, and optimistic monthly revenue scenarios, allowing the impact of revenue performance on profitability to be assessed.

### Profitability

The Year 1 P&L demonstrates the relationship between revenue, COGS, operating expenses, royalty, and operating profit.

The model also captures the initial loss-making period during the revenue ramp-up before the business reaches profitability under the base-case assumptions.

### Investment Recovery

The payback analysis tracks cumulative operating profit against the initial investment.

Under the base-case assumptions, the full initial investment is not recovered within Year 1.

### Revenue Sensitivity

The sensitivity analysis demonstrates that the financial outcome is highly dependent on the monthly revenue achieved.

Comparing ₹6 lakh, ₹8 lakh, and ₹10 lakh monthly revenue scenarios provides a clearer view of the range of possible operating outcomes.

### Scale100x Growth

The illustrative Scale100x projection demonstrates how revenue could increase over three years based on successful franchise deals and assumed annual deal growth.

The projection increases from:

**₹25,00,000 in Year 1**

to

**₹50,00,000 in Year 2**

and

**₹1,00,00,000 in Year 3**

under the stated assumptions.

### Lead Prioritisation

The lead-scoring framework provides a structured method for identifying higher-priority franchise prospects based on financial capacity, revenue potential, experience, existing operations, and funding requirements.

### Automation Opportunity

The proposed AI-enabled workflow demonstrates how repetitive lead qualification and administrative activities could potentially be automated.

This can allow consultants to spend more time on high-value conversations and conversion activities.

---

# 9. Project Deliverables

The repository contains the following major deliverables:

- Excel-based financial model
- Base case assumptions
- Year 1 monthly P&L
- Franchise payback analysis
- Revenue sensitivity analysis
- Scale100x three-year revenue projection
- Qualification checks
- Franchise lead-scoring framework
- Interactive ROI dashboard
- Live Streamlit prototype
- AI-enabled lead qualification workflow
- Automation time-saving analysis
- AI development notes
- Supporting screenshots
- Project documentation

---

# 10. Running the ROI Dashboard Locally

The ROI dashboard can be run locally using Python and Streamlit.

### Clone the Repository

    git clone https://github.com/nriika/franchise-financial-analysis.git

### Navigate to the Dashboard Folder

    cd franchise-financial-analysis/roi-dashboard

### Install Dependencies

    pip install -r requirements.txt

### Run the Application

    streamlit run app.py

The application will then be available through the local Streamlit server.

The deployed version can also be accessed through the live dashboard link provided above.

---

# 11. Repository Documentation

Detailed documentation for each component is available in its respective folder.

### Financial Model

See:

`financial-model/README.md`

for detailed information about the financial assumptions, Year 1 P&L, payback analysis, Scale100x projection, sensitivity analysis, qualification checks, and lead scoring.

### ROI Dashboard

See:

`roi-dashboard/README.md`

for detailed information about the dashboard, its functionality, screenshots, and local setup.

### AI Development Notes

See:

`roi-dashboard/AI-Development-Notes.md`

for documentation relating to the AI-assisted development and lead qualification workflow.

---

# 12. Assumptions & Limitations

This project is an illustrative financial and operational analysis created for assignment and portfolio purposes.

The results depend on the assumptions used in the financial model.

Important limitations include:

- Financial assumptions are illustrative.
- Revenue projections are scenario-based and are not forecasts.
- Actual franchise performance may differ from the model.
- Actual operating costs may vary depending on location and operating conditions.
- Franchise fees and royalty assumptions should be independently verified.
- Scale100x fee and deal-growth assumptions are illustrative modelling inputs.
- Scale100x projections do not represent guaranteed or contracted revenue.
- Payback analysis is based on the operating-profit assumptions used in the model.
- Lead scoring is a framework for prioritisation and does not guarantee lead conversion.
- AI-assisted qualification may produce incorrect or incomplete classifications.
- Automation time savings depend on actual implementation and workflow volume.
- Human review remains necessary for ambiguous, high-value, or complex leads.

---

# 13. Disclaimer

The financial model, ROI dashboard, Scale100x projection, lead scoring framework, and automation workflow are intended for **educational, analytical, and decision-support purposes**.

The assumptions and outputs should not be treated as verified financial statements, investment advice, commercial commitments, guaranteed returns, or forecasts of actual company performance.

Commercial assumptions, including franchise fees, royalty rates, Scale100x fees, revenue assumptions, operating costs, deal volumes, and growth rates, should be independently validated before being used for an actual business or investment decision.

---

# Conclusion

The FreshBrew Franchise Financial Analysis project combines financial modelling, scenario analysis, ROI evaluation, franchise lead scoring, and AI-enabled process automation into a single business decision-support framework.

The financial model provides the detailed analytical foundation, while the interactive ROI dashboard presents the key outputs in a more accessible and decision-oriented format.

The Scale100x projection provides an illustrative view of potential franchise-related revenue growth, while the lead-scoring and automation components demonstrate how franchise sales operations could be structured and streamlined.

Overall, the project demonstrates how **financial analysis, interactive technology, structured lead qualification, and AI-assisted automation** can be brought together to support franchise investment evaluation and operational decision-making.
