import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import textwrap

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HOMNIQ AI | House Price Prediction",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# =========================
# MODEL PATH
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "house_price_model.pkl"
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("⚠️ Model file not found.")
        st.write("Expected path:", MODEL_PATH)
        return None

    try:
        model = joblib.load(MODEL_PATH)
        return model

    except Exception as e:
        st.error("⚠️ Model file could not be loaded.")
        st.error(f"Error: {e}")
        return None


model = load_model()


# ============================================================
# IMPORTANT HTML RENDER FUNCTION
# THIS PREVENTS <div> CODE FROM SHOWING ON SCREEN
# ============================================================

def render_html(content):
    st.html(
        textwrap.dedent(content).strip()
    )


# ============================================================
# CSS
# ============================================================

render_html("""
<style>

/* =========================
   GLOBAL
========================= */

.stApp {
    background:
        radial-gradient(circle at 90% 5%, #e8f1ee 0%, transparent 25%),
        linear-gradient(135deg, #f7f8f6 0%, #eef3f0 100%);
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* Remove unnecessary Streamlit spaces */
[data-testid="stHeader"] {
    background: transparent;
}

/* =========================
   ANIMATIONS
========================= */

@keyframes fadeUp {
    0% {
        opacity: 0;
        transform: translateY(25px);
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floating {
    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 0 rgba(46, 125, 91, 0);
    }

    50% {
        box-shadow: 0 0 30px rgba(46, 125, 91, 0.18);
    }
}


/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #dfe7e2;
}

[data-testid="stSidebar"] * {
    color: #24342b;
}


/* =========================
   HERO
========================= */

.hero-card {
    position: relative;
    overflow: hidden;
    min-height: 300px;
    padding: 55px;
    border-radius: 28px;
    background:
        linear-gradient(
            90deg,
            rgba(20, 40, 31, 0.96) 0%,
            rgba(20, 40, 31, 0.82) 45%,
            rgba(20, 40, 31, 0.15) 100%
        ),
        url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1800&q=85");

    background-size: cover;
    background-position: center;

    animation: fadeUp 0.8s ease;
    box-shadow: 0 18px 45px rgba(25, 45, 34, 0.12);
}

.hero-tag {
    display: inline-block;
    background: rgba(255,255,255,0.16);
    color: #d9f2df;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 13px;
    letter-spacing: 1px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.08;
    color: white;
    max-width: 650px;
}

.hero-title span {
    color: #8ee0a8;
}

.hero-description {
    margin-top: 20px;
    color: #e5eee8;
    font-size: 18px;
    line-height: 1.7;
    max-width: 580px;
}

.hero-mini-stats {
    display: flex;
    gap: 28px;
    margin-top: 28px;
}

.hero-stat {
    color: white;
}

.hero-stat-number {
    font-size: 22px;
    font-weight: 800;
}

.hero-stat-label {
    font-size: 12px;
    opacity: 0.75;
}


/* =========================
   SECTION
========================= */

.section-title {
    margin-top: 35px;
    margin-bottom: 6px;
    font-size: 28px;
    font-weight: 750;
    color: #1d3127;
}

.section-subtitle {
    color: #718077;
    margin-bottom: 20px;
}


/* =========================
   CARDS
========================= */

.custom-card {
    background: rgba(255,255,255,0.96);
    border: 1px solid #e0e8e2;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 10px 30px rgba(38, 57, 45, 0.06);
    animation: fadeUp 0.7s ease;
}

.custom-card:hover {
    transform: translateY(-3px);
    transition: 0.3s;
    box-shadow: 0 18px 40px rgba(38, 57, 45, 0.10);
}


/* =========================
   RESULT CARD
========================= */

.result-card {
    background:
        linear-gradient(145deg, #16382a, #24513e);

    color: white;
    padding: 38px;
    border-radius: 25px;
    text-align: center;
    min-height: 350px;

    animation:
        fadeUp 0.8s ease,
        glow 3s infinite;
}

.result-label {
    font-size: 13px;
    letter-spacing: 1.5px;
    color: #b8dbc3;
}

.result-title {
    margin-top: 20px;
    font-size: 22px;
}

.price-value {
    font-size: 48px;
    font-weight: 800;
    margin: 15px 0;
    color: #91e7ad;
}

.result-description {
    color: #d8e8dc;
    line-height: 1.6;
}


/* =========================
   FEATURE CARDS
========================= */

.feature-card {
    background: white;
    border: 1px solid #e3ebe5;
    padding: 20px;
    border-radius: 18px;
    min-height: 130px;
}

.feature-icon {
    font-size: 28px;
}

.feature-title {
    font-size: 17px;
    font-weight: 700;
    color: #20352a;
    margin-top: 10px;
}

.feature-text {
    font-size: 13px;
    color: #748078;
    margin-top: 7px;
}


/* =========================
   FOOTER
========================= */

.footer {
    margin-top: 50px;
    padding: 25px;
    text-align: center;
    color: #66746b;
    border-top: 1px solid #dfe7e2;
}

.footer-name {
    color: #2f8256;
    font-weight: 800;
}


/* =========================
   BUTTON
========================= */

.stButton > button {
    width: 100%;
    height: 55px;

    border: none;
    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #2f7f58,
            #5bb77a
        );

    color: white;

    font-size: 17px;
    font-weight: 700;

    transition: all 0.3s ease;

    box-shadow:
        0 10px 20px
        rgba(47, 127, 88, 0.18);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 15px 28px
        rgba(47, 127, 88, 0.28);
}


/* =========================
   INPUTS
========================= */

.stNumberInput input {
    border-radius: 10px !important;
}

.stNumberInput label {
    font-weight: 600 !important;
    color: #324239 !important;
}


/* ============================================================
   RESPONSIVE DESIGN — keeps desktop design unchanged
   ============================================================ */

@media (max-width: 1100px) {
    .block-container {
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }
    .hero-card {
        padding: 42px;
    }
    .hero-title {
        font-size: 44px;
    }
}

@media (max-width: 768px) {
    .block-container {
        padding: 0.8rem 0.75rem 1.5rem 0.75rem;
        max-width: 100%;
    }

    .hero-card {
        min-height: 280px;
        padding: 30px 24px;
        border-radius: 22px;
        background-position: center;
    }

    .hero-title {
        font-size: 34px;
        line-height: 1.12;
        max-width: 100%;
    }

    .hero-description {
        font-size: 15px;
        line-height: 1.55;
        max-width: 100%;
        margin-top: 14px;
    }

    .hero-tag {
        font-size: 10px;
        padding: 7px 12px;
        margin-bottom: 12px;
    }

    .hero-mini-stats {
        flex-wrap: wrap;
        gap: 14px 22px;
        margin-top: 20px;
    }

    .hero-stat-number {
        font-size: 18px;
    }

    .hero-stat-label {
        font-size: 9px;
    }

    .section-title {
        font-size: 24px;
        margin-top: 25px;
    }

    .section-subtitle {
        font-size: 14px;
        line-height: 1.5;
    }

    .custom-card {
        padding: 18px;
        border-radius: 18px;
    }

    .result-card {
        min-height: 300px;
        padding: 28px 18px;
        border-radius: 20px;
    }

    .price-value {
        font-size: 38px;
    }

    .result-title {
        font-size: 19px;
    }

    .feature-card {
        min-height: auto;
        padding: 18px;
        margin-bottom: 12px;
    }

    .footer {
        margin-top: 30px;
        padding: 20px 10px;
        font-size: 13px;
    }

    /* Streamlit's native columns stack cleanly on small screens */
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap;
    }

    /* Prevent tables/charts from breaking the viewport */
    [data-testid="stDataFrame"],
    [data-testid="stArrowVegaLiteChart"],
    [data-testid="stVegaLiteChart"] {
        max-width: 100%;
        overflow-x: auto;
    }

    .stButton > button {
        height: 52px;
        font-size: 15px;
    }

    .stNumberInput input {
        font-size: 16px !important;
    }
}

@media (max-width: 480px) {
    .block-container {
        padding-left: 0.55rem;
        padding-right: 0.55rem;
    }

    .hero-card {
        padding: 24px 18px;
        min-height: 300px;
        border-radius: 18px;
    }

    .hero-title {
        font-size: 29px;
    }

    .hero-description {
        font-size: 14px;
    }

    .hero-mini-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
    }

    .hero-stat-number {
        font-size: 16px;
    }

    .hero-stat-label {
        font-size: 8px;
        line-height: 1.25;
    }

    .section-title {
        font-size: 21px;
    }

    .price-value {
        font-size: 32px;
    }

    .feature-title {
        font-size: 16px;
    }

    .feature-text {
        font-size: 12px;
    }
}

/* Slightly reduce sidebar width on medium screens */
@media (min-width: 769px) and (max-width: 1200px) {
    [data-testid="stSidebar"] {
        min-width: 240px;
        max-width: 260px;
    }
}

</style>
""")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    render_html("""
    <div style="
        padding: 20px 5px 25px 5px;
        border-bottom: 1px solid #e2e9e4;
        margin-bottom: 20px;
    ">
        <div style="
            font-size: 26px;
            font-weight: 800;
            color: #204431;
        ">
            🏡 HOMNIQ
        </div>

        <div style="
            color: #6f7f75;
            font-size: 13px;
            margin-top: 5px;
        ">
            AI Real Estate Intelligence
        </div>
    </div>
    """)

    page = st.radio(
        "Navigation",
        [
            "🏠 Prediction",
            "📊 Model Insights",
            "ℹ️ About Project"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    render_html("""
    <div style="
        background: #eef6f0;
        border: 1px solid #d9eadc;
        padding: 18px;
        border-radius: 15px;
        margin-top: 20px;
    ">
        <div style="
            font-weight: 700;
            color: #286040;
            margin-bottom: 7px;
        ">
            🤖 AI Powered
        </div>

        <div style="
            font-size: 13px;
            color: #637368;
            line-height: 1.5;
        ">
            Intelligent property value estimation using Machine Learning.
        </div>
    </div>
    """)


# ============================================================
# PREDICTION PAGE
# ============================================================

if page == "🏠 Prediction":

    # HERO
    render_html("""
    <div class="hero-card">

        <div class="hero-tag">
            ✦ MACHINE LEARNING • REAL ESTATE
        </div>

        <div class="hero-title">
            Predict Your <br>
            <span>House Price</span> with AI
        </div>

        <div class="hero-description">
            Get an intelligent property value estimate using a
            trained Machine Learning regression model.
        </div>

        <div class="hero-mini-stats">

            <div class="hero-stat">
                <div class="hero-stat-number">97.24%</div>
                <div class="hero-stat-label">BEST R² SCORE</div>
            </div>

            <div class="hero-stat">
                <div class="hero-stat-number">4</div>
                <div class="hero-stat-label">MODELS TESTED</div>
            </div>

            <div class="hero-stat">
                <div class="hero-stat-number">8</div>
                <div class="hero-stat-label">FEATURES USED</div>
            </div>

        </div>

    </div>
    """)

    render_html("""
    <div class="section-title">
        Property Information
    </div>

    <div class="section-subtitle">
        Enter the property details below to generate an estimated market price.
    </div>
    """)

    # MAIN LAYOUT
    col1, col2 = st.columns([1.25, 0.75], gap="large")

    # ========================================================
    # INPUT FORM
    # ========================================================

    with col1:

        render_html("""
        <div class="custom-card">
        """)

        c1, c2 = st.columns(2)

        with c1:
            overall_qual = st.number_input(
                "Overall Quality",
                min_value=1,
                max_value=10,
                value=6,
                step=1
            )

            gr_liv_area = st.number_input(
                "Living Area (sq ft)",
                min_value=300,
                value=1500,
                step=50
            )

            garage_cars = st.number_input(
                "Garage Capacity",
                min_value=0,
                max_value=5,
                value=2,
                step=1
            )

            total_bsmt_sf = st.number_input(
                "Basement Area (sq ft)",
                min_value=0,
                value=900,
                step=50
            )

        with c2:

            year_built = st.number_input(
                "Year Built",
                min_value=1800,
                max_value=2026,
                value=2005,
                step=1
            )

            full_bath = st.number_input(
                "Full Bathrooms",
                min_value=0,
                max_value=10,
                value=2,
                step=1
            )

            bedrooms = st.number_input(
                "Bedrooms",
                min_value=0,
                max_value=10,
                value=3,
                step=1
            )

            lot_area = st.number_input(
                "Lot Area (sq ft)",
                min_value=1000,
                value=8500,
                step=100
            )

        predict_button = st.button(
            "✨ Generate AI Price Estimate"
        )

        render_html("""
        </div>
        """)


    # ========================================================
    # RESULT SECTION
    # ========================================================

    with col2:

        if predict_button:

            input_data = pd.DataFrame({
                "OverallQual": [overall_qual],
                "GrLivArea": [gr_liv_area],
                "GarageCars": [garage_cars],
                "TotalBsmtSF": [total_bsmt_sf],
                "YearBuilt": [year_built],
                "FullBath": [full_bath],
                "BedroomAbvGr": [bedrooms],
                "LotArea": [lot_area]
            })

            prediction = model.predict(input_data)[0]

            render_html(f"""
            <div class="result-card">

                <div style="font-size:55px;">
                    🏠
                </div>

                <div class="result-label">
                    AI ESTIMATED PROPERTY VALUE
                </div>

                <div class="result-title">
                    Predicted House Price
                </div>

                <div class="price-value">
                    ${prediction:,.0f}
                </div>

                <div class="result-description">
                    Based on the entered property characteristics
                    and the trained Linear Regression model.
                </div>

                <div style="
                    margin-top: 25px;
                    padding-top: 20px;
                    border-top: 1px solid rgba(255,255,255,0.15);
                    font-size: 13px;
                    color: #c8dbce;
                ">
                    ✓ Model R² Score: 97.24%<br>
                    ✓ Prediction Status: Completed
                </div>

            </div>
            """)

        else:

            render_html("""
            <div class="result-card">

                <div style="
                    font-size: 70px;
                    animation: floating 3s ease-in-out infinite;
                ">
                    🏡
                </div>

                <div class="result-label">
                    AI PREDICTION DASHBOARD
                </div>

                <div class="result-title">
                    Your Property Estimate
                </div>

                <div style="
                    margin-top: 25px;
                    color: #d8e8dc;
                    line-height: 1.7;
                ">
                    Enter the property information and click
                    <b>Generate AI Price Estimate</b>
                    to receive a predicted house value.
                </div>

            </div>
            """)


    # ========================================================
    # FEATURES
    # ========================================================

    render_html("""
    <div class="section-title">
        Intelligent Property Analysis
    </div>

    <div class="section-subtitle">
        Combining real estate data with Machine Learning for smarter predictions.
    </div>
    """)

    f1, f2, f3 = st.columns(3)

    with f1:
        render_html("""
        <div class="feature-card">
            <div class="feature-icon">📐</div>
            <div class="feature-title">Property Features</div>
            <div class="feature-text">
                Analyzes living area, lot size, basement and room details.
            </div>
        </div>
        """)

    with f2:
        render_html("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Machine Learning</div>
            <div class="feature-text">
                Uses a trained regression model for intelligent price estimation.
            </div>
        </div>
        """)

    with f3:
        render_html("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">High Performance</div>
            <div class="feature-text">
                Final Linear Regression model achieved a 97.24% testing R² score.
            </div>
        </div>
        """)


# ============================================================
# MODEL INSIGHTS PAGE
# ============================================================

elif page == "📊 Model Insights":

    render_html("""
    <div class="section-title">
        Model Performance
    </div>

    <div class="section-subtitle">
        Comparison of Machine Learning models tested for house price prediction.
    </div>
    """)

    model_data = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Gradient Boosting",
            "Random Forest",
            "Decision Tree"
        ],

        "Testing R²": [
            0.972437,
            0.952775,
            0.867624,
            0.705922
        ],

        "RMSE": [
            12505.46,
            16368.98,
            27405.67,
            40847.69
        ]
    })

    st.dataframe(
        model_data,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        model_data.set_index("Model")["Testing R²"]
    )

    render_html("""
    <div class="custom-card" style="margin-top:25px;">

        <div style="
            font-size:22px;
            font-weight:800;
            color:#20352a;
        ">
            🏆 Final Model Selection
        </div>

        <div style="
            margin-top:15px;
            color:#68766d;
            line-height:1.8;
        ">
            Linear Regression was selected as the final model because
            it achieved the highest Testing R² score of <b>97.24%</b>
            and the lowest prediction error among the tested models.
        </div>

    </div>
    """)


# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ℹ️ About Project":

    render_html("""
    <div class="section-title">
        About HOMNIQ AI
    </div>

    <div class="section-subtitle">
        An end-to-end Machine Learning project for intelligent real estate price estimation.
    </div>

    <div class="custom-card">

        <div style="
            font-size:45px;
            margin-bottom:15px;
        ">
            🏡
        </div>

        <div style="
            font-size:25px;
            font-weight:800;
            color:#20352a;
        ">
            From Data to Prediction
        </div>

        <div style="
            margin-top:15px;
            color:#68766d;
            line-height:1.8;
            font-size:16px;
        ">

            HOMNIQ AI is a complete Machine Learning project
            designed to estimate house prices based on important
            property characteristics.

            <br><br>

            The project workflow includes data preprocessing,
            Exploratory Data Analysis, model training, evaluation,
            cross-validation and hyperparameter tuning.

            <br><br>

            Four regression algorithms were evaluated:
            Linear Regression, Decision Tree Regression,
            Random Forest Regression and Gradient Boosting Regression.

            <br><br>

            After comparing all model results, Linear Regression
            achieved the strongest performance with a Testing R²
            Score of 97.24%.

        </div>

    </div>
    """)


# ============================================================
# FOOTER
# ============================================================

render_html("""
<div class="footer">
    Developed by Shiza Eman
    <span class="footer-name">Shiza Eman</span>
    &nbsp; • &nbsp;
    "Machine Learning Project • Artificial Intelligence • Real Estate Intelligence"
</div>
""")
