import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Scale100x ROI Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# DESIGN SYSTEM
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background-color: #0A0A0F;
        color: #FFFFFF;
    }

    .main {
        background-color: #0A0A0F;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #0A0A0F !important;
    }

    [data-testid="stMain"] {
        background-color: #0A0A0F !important;
    }

    .block-container {
        max-width: 1400px !important;
        padding-top: 0.25rem !important;
        padding-bottom: 0.20rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: auto !important;
    }

    html, body {
        margin: 0 !important;
        padding: 0 !important;
    }

    h1, h2, h3, h4 {
        color: #FFFFFF !important;
        font-family: "Inter", sans-serif;
    }

    p, label, span {
        font-family: "Inter", sans-serif;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    [data-testid="stMetricLabel"] {
        color: #9CA3AF !important;
    }


    /* ========================================================
       STREAMLIT HEADER
       ======================================================== */

    [data-testid="stHeader"] {
        background-color: #0A0A0F !important;
    }


    /* ========================================================
       STREAMLIT SPACING
       ======================================================== */

    div[data-testid="stVerticalBlock"] {
        gap: 0.45rem;
    }

    div[data-testid="column"] {
        min-width: 0;
    }

    [data-testid="stElementContainer"] {
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        margin: 0 !important;
        padding: 0 !important;
    }

    hr {
        border-color: #27272A;
        margin: 0.25rem 0 !important;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] {
        background-color: #18181F;
        border: 1px solid #3F3F46;
        border-radius: 7px;
    }

    div[data-baseweb="input"] input {
        color: #FFFFFF !important;
        background-color: #18181F !important;
    }

    div[data-baseweb="input"] button {
        background-color: #18181F !important;
        color: #D1D5DB !important;
    }


    /* ========================================================
       NUMBER INPUT LABELS
       ======================================================== */

    div[data-testid="stNumberInput"] label {
        color: #D1D5DB !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        margin-bottom: 2px !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

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


    /* ========================================================
       HIDE STREAMLIT HEADING ANCHORS
       ======================================================== */

    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }


    /* ========================================================
       HIDE DEFAULT STREAMLIT FOOTER
       ======================================================== */

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.html("""
<div style="
    width:100%;
    text-align:center;
    padding:0;
    margin:0 0 7px 0;
    box-sizing:border-box;
">

    <div style="
        font-size:28px;
        font-weight:800;
        color:#FFFFFF;
        letter-spacing:-0.8px;
        line-height:1.05;
        margin:0 0 3px 0;
    ">
        Scale100x ROI Dashboard
    </div>

    <div style="
        font-size:14px;
        font-weight:600;
        color:#D1D5DB;
        line-height:1.1;
        margin:0 0 2px 0;
    ">
        FreshBrew Franchise Expansion Decision Tool
    </div>

    <div style="
        font-size:10px;
        color:#9CA3AF;
        line-height:1.1;
        margin:0;
    ">
        Interactive franchise unit economics, profitability, payback and scenario analysis
    </div>

</div>
""")


# ============================================================
# FRANCHISE ASSUMPTIONS
# ============================================================

st.html("""
<div style="
    color:#FFFFFF;
    font-size:16px;
    font-weight:700;
    line-height:1.1;
    margin:2px 0 3px 0;
    padding:0;
">
    Franchise Assumptions
</div>
""")


input_col1, input_col2, input_col3, input_col4, input_col5, input_col6 = st.columns(6)


with input_col1:

    monthly_revenue = st.number_input(
        "Monthly Revenue (₹)",
        min_value=0,
        value=800000,
        step=50000
    )


with input_col2:

    cogs_percentage = st.number_input(
        "COGS (%)",
        min_value=0.0,
        max_value=100.0,
        value=30.0,
        step=1.0
    )


with input_col3:

    initial_investment = st.number_input(
        "Investment (₹)",
        min_value=0,
        value=2000000,
        step=100000
    )


with input_col4:

    rent = st.number_input(
        "Monthly Rent (₹)",
        min_value=0,
        value=100000,
        step=10000
    )


with input_col5:

    staff_cost = st.number_input(
        "Staff Cost (₹)",
        min_value=0,
        value=180000,
        step=10000
    )


with input_col6:

    marketing_percentage = st.number_input(
        "Marketing (%)",
        min_value=0.0,
        max_value=100.0,
        value=6.0,
        step=1.0
    )


# ============================================================
# FIXED ASSUMPTIONS
# ============================================================

utilities = 30000
other_costs = 40000
royalty_percentage = 5.0


# ============================================================
# FINANCIAL CALCULATIONS
# ============================================================

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

    simple_payback = (
        initial_investment / annual_operating_profit
    )

else:

    simple_payback = None


if initial_investment > 0:

    roi = (
        annual_operating_profit / initial_investment
    )

else:

    roi = 0


# ============================================================
# KEY FINANCIAL METRICS
# ============================================================

st.html("""
<div style="
    color:#FFFFFF;
    font-size:16px;
    font-weight:700;
    line-height:1.1;
    margin:5px 0 3px 0;
    padding:0;
">
    Key Financial Metrics
</div>
""")


kpi_data = [

    (
        "Monthly Revenue",
        f"₹{monthly_revenue:,.0f}"
    ),

    (
        "Gross Profit",
        f"₹{gross_profit:,.0f}"
    ),

    (
        "Operating Profit",
        f"₹{operating_profit:,.0f}"
    ),

    (
        "Simple Payback",
        (
            f"{simple_payback:.2f} yrs"
            if simple_payback is not None
            else "Not achievable"
        )
    ),

    (
        "Annual ROI",
        f"{roi * 100:.1f}%"
    )

]


kpi_cols = st.columns(5)


for col, (label, value) in zip(kpi_cols, kpi_data):

    with col:

        kpi_card = f"""
        <div style="
            background:#18181F;
            border:1px solid #3F3F46;
            border-radius:9px;
            padding:9px 13px;
            min-height:65px;
            box-sizing:border-box;
        ">

            <div style="
                color:#9CA3AF;
                font-size:10px;
                margin-bottom:3px;
                line-height:1.1;
            ">
                {label}
            </div>

            <div style="
                color:#FFFFFF;
                font-size:20px;
                font-weight:700;
                line-height:1.15;
            ">
                {value}
            </div>

        </div>
        """

        st.html(kpi_card)


# ============================================================
# INVESTMENT DECISION
# ============================================================

if operating_profit <= 0:

    decision = "NO-GO"

    explanation = (
        "The franchise is not generating positive monthly operating profit."
    )

    decision_bg = "#3B1118"
    decision_border = "#EF4444"
    decision_text = "#FCA5A5"


elif simple_payback is not None and simple_payback <= 2:

    decision = "GO"

    explanation = (
        "Positive operating profit with a payback period of two years or less."
    )

    decision_bg = "#0B2F24"
    decision_border = "#10B981"
    decision_text = "#6EE7B7"


else:

    decision = "REVIEW"

    explanation = (
        "The franchise is profitable, but the payback period requires further review."
    )

    decision_bg = "#33250A"
    decision_border = "#F59E0B"
    decision_text = "#FCD34D"


# ============================================================
# SCENARIO CALCULATIONS
# ============================================================

scenario_revenues = {

    "₹6L Conservative": 600000,

    "₹8L Base Case": 800000,

    "₹10L Optimistic": 1000000

}


scenario_results = []


for scenario_name, revenue in scenario_revenues.items():

    scenario_cogs = (
        revenue * (cogs_percentage / 100)
    )

    scenario_gross_profit = (
        revenue - scenario_cogs
    )

    scenario_marketing = (
        revenue * (marketing_percentage / 100)
    )

    scenario_royalty = (
        revenue * (royalty_percentage / 100)
    )

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

    scenario_annual_profit = (
        scenario_operating_profit * 12
    )


    if scenario_annual_profit > 0:

        scenario_payback = (
            initial_investment
            / scenario_annual_profit
        )

    else:

        scenario_payback = None


    if initial_investment > 0:

        scenario_roi = (
            scenario_annual_profit
            / initial_investment
        )

    else:

        scenario_roi = 0


    scenario_results.append({

        "name": scenario_name,

        "revenue": revenue,

        "operating_profit": scenario_operating_profit,

        "annual_profit": scenario_annual_profit,

        "payback": scenario_payback,

        "roi": scenario_roi

    })


# ============================================================
# INVESTMENT OUTLOOK
# ============================================================

st.html("""
<div style="
    color:#FFFFFF;
    font-size:16px;
    font-weight:700;
    line-height:1.1;
    margin:5px 0 3px 0;
    padding:0;
">
    Investment Outlook
</div>
""")


decision_col, profit_col, payback_col = st.columns(
    [1.00, 1.35, 1.35],
    gap="small"
)


# ============================================================
# DECISION CARD
# ============================================================

with decision_col:

    decision_card = f"""

    <div style="
        background:#18181F;
        border:1px solid #3F3F46;
        border-radius:9px;
        padding:10px 13px;
        height:200px;
        box-sizing:border-box;
    ">

        <div style="
            color:#9CA3AF;
            font-size:10px;
            margin-bottom:5px;
            line-height:1.1;
        ">
            Investment Recommendation
        </div>


        <div style="
            display:inline-block;
            background:{decision_bg};
            border:1px solid {decision_border};
            border-radius:7px;
            padding:5px 15px;
            color:{decision_text};
            font-size:20px;
            font-weight:800;
            margin-bottom:6px;
            line-height:1.2;
        ">
            {decision}
        </div>


        <div style="
            color:#D1D5DB;
            font-size:10px;
            line-height:1.3;
            margin-bottom:8px;
        ">
            {explanation}
        </div>


        <div style="
            border-top:1px solid #3F3F46;
            padding-top:7px;
        ">

            <div style="
                color:#9CA3AF;
                font-size:9px;
                margin-bottom:2px;
            ">
                Annual Operating Profit
            </div>

            <div style="
                color:#FFFFFF;
                font-size:18px;
                font-weight:700;
                margin-bottom:6px;
            ">
                ₹{annual_operating_profit:,.0f}
            </div>


            <div style="
                color:#9CA3AF;
                font-size:9px;
                margin-bottom:2px;
            ">
                Annual ROI
            </div>

            <div style="
                color:#FFFFFF;
                font-size:18px;
                font-weight:700;
            ">
                {roi * 100:.1f}%
            </div>

        </div>

    </div>

    """

    st.html(decision_card)


# ============================================================
# OPERATING PROFIT CHART
# ============================================================

with profit_col:

    st.html("""
    <div style="
        color:#FFFFFF;
        font-size:14px;
        font-weight:700;
        line-height:1.1;
        margin:0 0 1px 0;
        padding:0;
    ">
        Operating Profit by Scenario
    </div>
    """)


    profit_chart_data = [

        {
            "Scenario": result["name"],
            "Operating Profit": result["operating_profit"]
        }

        for result in scenario_results

    ]


    st.vega_lite_chart(

        profit_chart_data,

        {

            "background": "#18181F",

            "width": "container",

            "height": 165,

            "padding": {
                "left": 5,
                "right": 5,
                "top": 5,
                "bottom": 5
            },

            "mark": {

                "type": "bar",

                "color": "#2563EB",

                "cornerRadiusTopLeft": 4,

                "cornerRadiusTopRight": 4,

                "size": 55

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

                    "title": None,

                    "axis": {

                        "labelColor": "#A1A1AA",

                        "labelFontSize": 9,

                        "labelAngle": 0,

                        "labelPadding": 5,

                        "domain": False,

                        "ticks": False

                    }

                },


                "y": {

                    "field": "Operating Profit",

                    "type": "quantitative",

                    "title": None,

                    "axis": {

                        "labelColor": "#A1A1AA",

                        "labelFontSize": 9,

                        "format": "~s",

                        "gridColor": "#27272A",

                        "domain": False,

                        "ticks": False

                    }

                },


                "tooltip": [

                    {
                        "field": "Scenario",
                        "type": "nominal"
                    },

                    {
                        "field": "Operating Profit",
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
                    "gridOpacity": 0.7
                }

            }

        },

        use_container_width=True

    )


# ============================================================
# PAYBACK CHART
# ============================================================

with payback_col:

    st.html("""
    <div style="
        color:#FFFFFF;
        font-size:14px;
        font-weight:700;
        line-height:1.1;
        margin:0 0 1px 0;
        padding:0;
    ">
        Simple Payback by Scenario
    </div>
    """)


    payback_chart_data = [

        {
            "Scenario": result["name"],

            "Payback": (
                result["payback"]
                if result["payback"] is not None
                else 0
            )

        }

        for result in scenario_results

    ]


    st.vega_lite_chart(

        payback_chart_data,

        {

            "background": "#18181F",

            "width": "container",

            "height": 165,

            "padding": {

                "left": 5,
                "right": 5,
                "top": 5,
                "bottom": 5

            },

            "mark": {

                "type": "bar",

                "color": "#10B981",

                "cornerRadiusTopLeft": 4,

                "cornerRadiusTopRight": 4,

                "size": 55

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

                    "title": None,

                    "axis": {

                        "labelColor": "#A1A1AA",

                        "labelFontSize": 9,

                        "labelAngle": 0,

                        "labelPadding": 5,

                        "domain": False,

                        "ticks": False

                    }

                },


                "y": {

                    "field": "Payback",

                    "type": "quantitative",

                    "title": None,

                    "axis": {

                        "labelColor": "#A1A1AA",

                        "labelFontSize": 9,

                        "format": ".0f",

                        "gridColor": "#27272A",

                        "domain": False,

                        "ticks": False

                    }

                },


                "tooltip": [

                    {
                        "field": "Scenario",
                        "type": "nominal"
                    },

                    {
                        "field": "Payback",
                        "type": "quantitative",
                        "format": ".2f"
                    }

                ]

            },


            "config": {

                "view": {
                    "stroke": "transparent"
                },

                "axis": {
                    "gridOpacity": 0.7
                }

            }

        },

        use_container_width=True

    )


# ============================================================
# SCENARIO SUMMARY
# ============================================================

st.html("""
<div style="
    color:#FFFFFF;
    font-size:14px;
    font-weight:700;
    line-height:1.1;
    margin:4px 0 2px 0;
    padding:0;
">
    Scenario Summary
</div>
""")


summary_html = """

<table style="
    width:100%;
    border-collapse:collapse;
    background:#18181F;
    border:1px solid #3F3F46;
    border-radius:8px;
    overflow:hidden;
    color:#FFFFFF;
    font-family:Inter,sans-serif;
    font-size:10px;
">

<tr style="
    background:#202027;
">

    <th style="
        padding:6px 8px;
        text-align:left;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        Scenario
    </th>


    <th style="
        padding:6px 8px;
        text-align:right;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        Monthly Revenue
    </th>


    <th style="
        padding:6px 8px;
        text-align:right;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        Monthly Profit
    </th>


    <th style="
        padding:6px 8px;
        text-align:right;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        Annual Profit
    </th>


    <th style="
        padding:6px 8px;
        text-align:right;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        Payback
    </th>


    <th style="
        padding:6px 8px;
        text-align:right;
        border-bottom:1px solid #3F3F46;
        color:#A1A1AA;
        font-weight:600;
    ">
        ROI
    </th>

</tr>

"""


for result in scenario_results:

    payback_display = (

        f"{result['payback']:.2f} yrs"

        if result["payback"] is not None

        else "N/A"

    )


    summary_html += f"""

    <tr>

        <td style="
            padding:5px 8px;
            border-bottom:1px solid #27272A;
            color:#FFFFFF;
        ">
            {result["name"]}
        </td>


        <td style="
            padding:5px 8px;
            text-align:right;
            border-bottom:1px solid #27272A;
        ">
            ₹{result["revenue"]:,.0f}
        </td>


        <td style="
            padding:5px 8px;
            text-align:right;
            border-bottom:1px solid #27272A;
        ">
            ₹{result["operating_profit"]:,.0f}
        </td>


        <td style="
            padding:5px 8px;
            text-align:right;
            border-bottom:1px solid #27272A;
        ">
            ₹{result["annual_profit"]:,.0f}
        </td>


        <td style="
            padding:5px 8px;
            text-align:right;
            border-bottom:1px solid #27272A;
        ">
            {payback_display}
        </td>


        <td style="
            padding:5px 8px;
            text-align:right;
            border-bottom:1px solid #27272A;
        ">
            {result["roi"] * 100:.1f}%
        </td>

    </tr>

    """


summary_html += """

</table>

"""


st.html(summary_html)


# ============================================================
# FOOTNOTE
# ============================================================

st.html("""
<div style="
    text-align:center;
    color:#71717A;
    font-size:9px;
    line-height:1.1;
    margin:3px 0 0 0;
    padding:0;
">
    Illustrative financial model for franchise evaluation.
    Assumptions can be adjusted using the inputs above.
</div>
""")
