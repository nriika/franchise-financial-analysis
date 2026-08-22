import streamlit as st
import textwrap


st.set_page_config(
    page_title="Scale100x ROI Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# DESIGN SYSTEM
# -----------------------------

st.markdown("""
<style>

    .stApp {
        background-color: #0A0A0F;
        color: #FFFFFF;
    }

    .main {
        background-color: #0A0A0F;
    }

    /* Main dashboard container */
    .block-container {
        max-width: 1250px !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        margin: auto !important;
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: "Inter", sans-serif;
    }

    p, label, span {
        color: #D1D5DB;
        font-family: "Inter", sans-serif;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-family: "Inter", sans-serif;
    }

    [data-testid="stMetricLabel"] {
        color: #9CA3AF !important;
    }

    .stButton > button {
        background-color: #2563EB;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
        color: #FFFFFF;
    }

    hr {
        border-color: #27272A;
    }

    /* Remove heading anchor/link icons */
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }

    /* Keep custom HTML cards within their columns */
    div[data-testid="column"] {
        min-width: 0;
    }

</style>
""", unsafe_allow_html=True)

# -----------------------------
# DASHBOARD HEADER
# -----------------------------

header_html = """
<div style="
    text-align: center;
    padding: 18px 0 30px 0;
">

    <div style="
        font-size: 46px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -1.5px;
        margin-bottom: 10px;
    ">
        Scale100x ROI Dashboard
    </div>

    <div style="
        font-size: 22px;
        font-weight: 600;
        color: #D1D5DB;
        margin-bottom: 10px;
    ">
        FreshBrew Franchise Expansion Decision Tool
    </div>

    <div style="
        font-size: 15px;
        color: #9CA3AF;
    ">
        Evaluate franchise unit economics, payback and revenue scenarios.
    </div>

</div>
"""

st.html(textwrap.dedent(header_html))

st.divider()

# -----------------------------
# INPUTS
# -----------------------------

st.header("Franchise Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    monthly_revenue = st.number_input(
        "Monthly Revenue (₹)",
        min_value=0,
        value=800000,
        step=50000
    )

with col2:
    cogs_percentage = st.number_input(
        "COGS (%)",
        min_value=0.0,
        max_value=100.0,
        value=30.0,
        step=1.0
    )

with col3:
    initial_investment = st.number_input(
        "Initial Investment (₹)",
        min_value=0,
        value=2000000,
        step=100000
    )

st.divider()

st.header("Operating Costs")

cost_col1, cost_col2, cost_col3 = st.columns(3)

with cost_col1:
    rent = st.number_input(
        "Monthly Rent (₹)",
        min_value=0,
        value=100000,
        step=10000
    )

with cost_col2:
    staff_cost = st.number_input(
        "Monthly Staff Cost (₹)",
        min_value=0,
        value=180000,
        step=10000
    )

with cost_col3:
    marketing_percentage = st.number_input(
        "Marketing (% of Revenue)",
        min_value=0.0,
        max_value=100.0,
        value=6.0,
        step=1.0
    )

# Additional operating costs
utilities = 30000
other_costs = 40000
royalty_percentage = 5.0

# -----------------------------
# FINANCIAL CALCULATIONS
# -----------------------------

cogs = monthly_revenue * (cogs_percentage / 100)

gross_profit = monthly_revenue - cogs

marketing = monthly_revenue * (marketing_percentage / 100)

royalty = monthly_revenue * (royalty_percentage / 100)

total_operating_expenses = (
    rent
    + staff_cost
    + marketing
    + utilities
    + other_costs
    + royalty
)

operating_profit = gross_profit - total_operating_expenses

annual_revenue = monthly_revenue * 12

annual_operating_profit = operating_profit * 12

if annual_operating_profit > 0:
    simple_payback = initial_investment / annual_operating_profit
else:
    simple_payback = None

if initial_investment > 0:
    roi = annual_operating_profit / initial_investment
else:
    roi = 0

# -----------------------------
# KEY METRICS
# -----------------------------

st.divider()

st.header("Unit Economics")

metric_data = [
    ("Monthly Revenue", f"₹{monthly_revenue:,.0f}"),
    ("Gross Profit", f"₹{gross_profit:,.0f}"),
    ("Monthly Operating Profit", f"₹{operating_profit:,.0f}"),
    (
        "Simple Payback",
        f"{simple_payback:.2f} years"
        if simple_payback is not None
        else "Not achievable"
    )
]

metric_cols = st.columns(4)

for col, (label, value) in zip(metric_cols, metric_data):

    with col:

        metric_card = f"""
        <div style="
            background-color: #18181F;
            border: 1px solid #3F3F46;
            border-radius: 14px;
            padding: 22px;
            min-height: 120px;
            box-sizing: border-box;
        ">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 12px;
            ">
                {label}
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 28px;
                font-weight: 600;
            ">
                {value}
            </div>

        </div>
        """

        st.html(metric_card)


# -----------------------------
# PROFIT & LOSS
# -----------------------------

st.subheader("Monthly Profit & Loss")

pl_col1, pl_col2 = st.columns(2)

with pl_col1:

    revenue_card = f"""
    <div style="
        background-color: #18181F;
        border: 1px solid #3F3F46;
        border-radius: 14px;
        padding: 24px;
        min-height: 260px;
        box-sizing: border-box;
    ">

        <div style="
            color: #FFFFFF;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 20px;
        ">
            Revenue & Gross Profit
        </div>

        <div style="margin-bottom: 22px;">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                Revenue
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{monthly_revenue:,.0f}
            </div>

        </div>

        <div style="margin-bottom: 22px;">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                COGS
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{cogs:,.0f}
            </div>

        </div>

        <div>

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                Gross Profit
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{gross_profit:,.0f}
            </div>

        </div>

    </div>
    """

    st.html(revenue_card)


with pl_col2:

    profit_card = f"""
    <div style="
        background-color: #18181F;
        border: 1px solid #3F3F46;
        border-radius: 14px;
        padding: 24px;
        min-height: 260px;
        box-sizing: border-box;
    ">

        <div style="
            color: #FFFFFF;
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 20px;
        ">
            Operating Performance
        </div>

        <div style="margin-bottom: 22px;">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                Operating Expenses
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{total_operating_expenses:,.0f}
            </div>

        </div>

        <div style="margin-bottom: 22px;">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                Operating Profit
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{operating_profit:,.0f}
            </div>

        </div>

        <div>

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 6px;
            ">
                Annual Operating Profit
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 26px;
                font-weight: 600;
            ">
                ₹{annual_operating_profit:,.0f}
            </div>

        </div>

    </div>
    """

    st.html(profit_card)


# -----------------------------
# DECISION SIGNAL
# -----------------------------

st.divider()

st.header("Investment Decision")

if operating_profit <= 0:

    decision = "NO-GO"
    explanation = "The franchise is not generating positive monthly operating profit."

    decision_bg = "#3B1118"
    decision_border = "#EF4444"
    decision_text = "#FCA5A5"

elif simple_payback is not None and simple_payback <= 2:

    decision = "GO"
    explanation = "The franchise generates positive operating profit with a payback period of two years or less."

    decision_bg = "#0B2F24"
    decision_border = "#10B981"
    decision_text = "#6EE7B7"

else:

    decision = "REVIEW"
    explanation = "The franchise is profitable but the payback period requires further review."

    decision_bg = "#33250A"
    decision_border = "#F59E0B"
    decision_text = "#FCD34D"


decision_card = f"""
<div style="
    background-color: #18181F;
    border: 1px solid #3F3F46;
    border-radius: 14px;
    padding: 26px;
    margin-top: 10px;
    box-sizing: border-box;
">

    <div style="
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 30px;
        flex-wrap: wrap;
    ">

        <div style="
            flex: 1 1 500px;
            min-width: 0;
        ">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 10px;
            ">
                Investment Recommendation
            </div>

            <div style="
                display: inline-block;
                background-color: {decision_bg};
                border: 1px solid {decision_border};
                border-radius: 10px;
                padding: 8px 18px;
                color: {decision_text};
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 16px;
            ">
                {decision}
            </div>

            <div style="
                color: #D1D5DB;
                font-size: 15px;
                line-height: 1.6;
                max-width: 700px;
            ">
                {explanation}
            </div>

        </div>


        <div style="
            min-width: 180px;
            padding-left: 30px;
            border-left: 1px solid #3F3F46;
            box-sizing: border-box;
        ">

            <div style="
                color: #A1A1AA;
                font-size: 14px;
                margin-bottom: 8px;
            ">
                Annual ROI
            </div>

            <div style="
                color: #FFFFFF;
                font-size: 32px;
                font-weight: 600;
            ">
                {roi * 100:.1f}%
            </div>

        </div>

    </div>

</div>
"""

st.html(textwrap.dedent(decision_card))


# -----------------------------
# REVENUE SCENARIO ANALYSIS
# -----------------------------

st.divider()

st.header("Revenue Scenario Analysis")

st.write(
    "Compare franchise profitability at different monthly revenue levels."
)

scenario_revenues = {
    "₹6L Conservative": 600000,
    "₹8L Base Case": 800000,
    "₹10L Optimistic": 1000000
}

scenario_results = []

for scenario_name, revenue in scenario_revenues.items():

    scenario_cogs = revenue * (cogs_percentage / 100)

    scenario_gross_profit = revenue - scenario_cogs

    scenario_marketing = revenue * (marketing_percentage / 100)

    scenario_royalty = revenue * (royalty_percentage / 100)

    scenario_operating_expenses = (
        rent
        + staff_cost
        + scenario_marketing
        + utilities
        + other_costs
        + scenario_royalty
    )

    scenario_operating_profit = (
        scenario_gross_profit
        - scenario_operating_expenses
    )

    scenario_annual_profit = scenario_operating_profit * 12

    if scenario_annual_profit > 0:
        scenario_payback = (
            initial_investment / scenario_annual_profit
        )
    else:
        scenario_payback = None

    if initial_investment > 0:
        scenario_roi = (
            scenario_annual_profit / initial_investment
        )
    else:
        scenario_roi = 0

    scenario_results.append(
        {
            "name": scenario_name,
            "revenue": revenue,
            "operating_profit": scenario_operating_profit,
            "annual_profit": scenario_annual_profit,
            "payback": scenario_payback,
            "roi": scenario_roi
        }
    )


# -----------------------------
# DISPLAY SCENARIO CARDS
# -----------------------------

scenario_col1, scenario_col2, scenario_col3 = st.columns(3)

scenario_columns = [
    scenario_col1,
    scenario_col2,
    scenario_col3
]

for column, result in zip(scenario_columns, scenario_results):

    # Decision logic
    if result["payback"] is None:
        scenario_decision = "NO-GO"
        scenario_reason = "The scenario does not generate positive annual profit."
        decision_bg = "#3B1118"
        decision_border = "#EF4444"
        decision_text = "#FCA5A5"

    elif result["payback"] <= 2:
        scenario_decision = "GO"
        scenario_reason = "Payback is within 2 years."
        decision_bg = "#0B2F24"
        decision_border = "#10B981"
        decision_text = "#6EE7B7"

    elif result["payback"] <= 5:
        scenario_decision = "REVIEW"
        scenario_reason = "The franchise is profitable, but payback is longer."
        decision_bg = "#33250A"
        decision_border = "#F59E0B"
        decision_text = "#FCD34D"

    else:
        scenario_decision = "NO-GO"
        scenario_reason = "Payback is longer than 5 years."
        decision_bg = "#3B1118"
        decision_border = "#EF4444"
        decision_text = "#FCA5A5"

    with column:

        card_html = f"""
        <div style="
            background-color: #18181F;
            border: 1px solid #3F3F46;
            border-radius: 14px;
            padding: 22px;
            min-height: 430px;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        ">

            <div style="
                font-size: 21px;
                font-weight: 700;
                color: #FFFFFF;
                margin-bottom: 22px;
            ">
                {result["name"]}
            </div>

            <div style="margin-bottom: 20px;">
                <div style="
                    color: #A1A1AA;
                    font-size: 14px;
                    margin-bottom: 6px;
                ">
                    Monthly Revenue
                </div>

                <div style="
                    color: #FFFFFF;
                    font-size: 28px;
                    font-weight: 600;
                ">
                    ₹{result["revenue"]:,.0f}
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="
                    color: #A1A1AA;
                    font-size: 14px;
                    margin-bottom: 6px;
                ">
                    Monthly Operating Profit
                </div>

                <div style="
                    color: #FFFFFF;
                    font-size: 28px;
                    font-weight: 600;
                ">
                    ₹{result["operating_profit"]:,.0f}
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="
                    color: #A1A1AA;
                    font-size: 14px;
                    margin-bottom: 6px;
                ">
                    Payback Period
                </div>

                <div style="
                    color: #FFFFFF;
                    font-size: 28px;
                    font-weight: 600;
                ">
                    {f"{result['payback']:.2f} years" if result["payback"] is not None else "Not achievable"}
                </div>
            </div>

            <div style="margin-bottom: 22px;">
                <div style="
                    color: #A1A1AA;
                    font-size: 14px;
                    margin-bottom: 6px;
                ">
                    Annual ROI
                </div>

                <div style="
                    color: #FFFFFF;
                    font-size: 28px;
                    font-weight: 600;
                ">
                    {result["roi"] * 100:.1f}%
                </div>
            </div>

            <div style="
                background-color: {decision_bg};
                border: 1px solid {decision_border};
                border-radius: 10px;
                padding: 18px;
                margin-top: 10px;
            ">

                <div style="
                    color: {decision_text};
                    font-size: 20px;
                    font-weight: 700;
                    margin-bottom: 8px;
                ">
                    {scenario_decision}
                </div>

                <div style="
                    color: #D1D5DB;
                    font-size: 14px;
                    line-height: 1.5;
                ">
                    {scenario_reason}
                </div>

            </div>

        </div>
        """

        st.html(card_html)


# -----------------------------
# SCENARIO PROFIT CHART
# -----------------------------

st.divider()

st.header("Operating Profit by Revenue Scenario")

chart_data = [
    {
        "Scenario": "₹6L Conservative",
        "Monthly Operating Profit": scenario_results[0]["operating_profit"]
    },
    {
        "Scenario": "₹8L Base Case",
        "Monthly Operating Profit": scenario_results[1]["operating_profit"]
    },
    {
        "Scenario": "₹10L Optimistic",
        "Monthly Operating Profit": scenario_results[2]["operating_profit"]
    }
]

st.vega_lite_chart(
    chart_data,
    {
        "background": "#0A0A0F",

        "width": "container",

        "mark": {
            "type": "bar",
            "color": "#2563EB",
            "cornerRadiusTopLeft": 6,
            "cornerRadiusTopRight": 6
        },

        "encoding": {
            "x": {
                "field": "Scenario",
                "type": "nominal",
                "sort": [
                    "₹6L Conservative",
                    "₹8L Base Case",
                    "₹10L Optimistic"
                ],
                "title": "Scenario",
                "axis": {
                    "labelColor": "#A1A1AA",
                    "titleColor": "#A1A1AA",
                    "labelAngle": 0
                }
            },

            "y": {
                "field": "Monthly Operating Profit",
                "type": "quantitative",
                "title": "Monthly Operating Profit",
                "axis": {
                    "labelColor": "#A1A1AA",
                    "titleColor": "#A1A1AA",
                    "format": ",.0f"
                }
            },

            "tooltip": [
                {
                    "field": "Scenario",
                    "type": "nominal"
                },
                {
                    "field": "Monthly Operating Profit",
                    "type": "quantitative",
                    "format": ",.0f"
                }
            ]
        },

        "config": {
            "view": {
                "stroke": "transparent"
            },

            "axis": {
                "gridColor": "#27272A",
                "domainColor": "#27272A"
            }
        }
    },
    width="stretch"
)
