
import streamlit as st
import pandas as pd
import joblib
import os

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HOMENIQ | House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOAD MODEL
# ============================================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "house_price_model.pkl"
)

@st.cache_resource
def load_model():
    if not os.path.isfile(MODEL_PATH):
        st.error("❌ Model file not found.")
        st.write("Looking for model at:")
        st.code(MODEL_PATH)
        st.write("Files available in app directory:")
        st.write(os.listdir(os.path.dirname(os.path.abspath(__file__))))

        return None

    return joblib.load(MODEL_PATH)


model = load_model()
    


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

/* ------------------------------------------------------------
   GLOBAL
------------------------------------------------------------ */

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background:
        radial-gradient(circle at 5% 10%, rgba(34,115,220,0.08), transparent 25%),
        radial-gradient(circle at 95% 20%, rgba(34,115,220,0.08), transparent 25%),
        #F5F8FC;
    color: #10233D;
}

.block-container {
    max-width: 1450px;
    padding-top: 25px;
    padding-bottom: 30px;
}

/* ------------------------------------------------------------
   ANIMATIONS
------------------------------------------------------------ */

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

@keyframes floatCard {
    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 15px 40px rgba(32, 101, 201, 0.18);
    }

    50% {
        box-shadow: 0 20px 55px rgba(32, 101, 201, 0.35);
    }
}

/* ------------------------------------------------------------
   LOGO
------------------------------------------------------------ */

.logo-card {
    animation: fadeUp 0.8s ease;
}

.logo-title {
    font-size: 38px;
    font-weight: 800;
    color: #10233D;
    letter-spacing: -1.5px;
    line-height: 1;
}

.logo-title span {
    color: #1769E0;
}

.logo-subtitle {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #75839A;
    margin-top: 8px;
}

/* ------------------------------------------------------------
   NAVIGATION BUBBLES
------------------------------------------------------------ */

div[data-testid="stHorizontalBlock"] .stButton > button {
    width: 100%;
    min-height: 56px !important;
    border-radius: 999px !important;

    background: #FFFFFF !important;
    color: #10233D !important;

    border: 1.5px solid #D7E1EC !important;

    font-size: 14px !important;
    font-weight: 800 !important;

    transition: all 0.3s ease !important;

    box-shadow: 0 6px 18px rgba(20, 50, 90, 0.05);
}

div[data-testid="stHorizontalBlock"] .stButton > button:hover {
    background: #1769E0 !important;
    color: white !important;

    border-color: #1769E0 !important;

    transform: translateY(-4px) !important;

    box-shadow: 0 12px 30px rgba(23, 105, 224, 0.25) !important;
}

/* ------------------------------------------------------------
   HERO
------------------------------------------------------------ */

.hero-card {
    margin-top: 35px;
    min-height: 500px;

    border-radius: 34px;

    background:
        linear-gradient(
            90deg,
            rgba(8, 25, 48, 0.94) 0%,
            rgba(12, 35, 65, 0.88) 42%,
            rgba(12, 35, 65, 0.28) 68%,
            rgba(12, 35, 65, 0.05) 100%
        ),
        url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1800&q=90');

    background-size: cover;
    background-position: center;

    display: flex;
    align-items: center;

    overflow: hidden;

    box-shadow: 0 25px 70px rgba(16, 35, 61, 0.18);

    animation: fadeUp 0.9s ease;
}

.hero-content {
    max-width: 700px;
    padding: 65px 8%;
}

.hero-badge {
    display: inline-block;

    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.25);

    color: #CFE5FF;

    padding: 9px 18px;

    border-radius: 999px;

    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

.hero-title {
    margin-top: 22px;

    color: #FFFFFF;

    font-family: 'Playfair Display', serif;

    font-size: 74px;
    line-height: 1.05;

    font-weight: 800;

    letter-spacing: -2px;
}

.hero-title span {
    color: #75B6FF;
}

.hero-text {
    color: #D6E4F4;

    font-size: 18px;
    line-height: 1.8;

    margin-top: 22px;

    max-width: 620px;
}

.hero-stat-row {
    display: flex;
    gap: 15px;
    margin-top: 35px;
}

.hero-stat {
    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(10px);

    border: 1px solid rgba(255,255,255,0.18);

    padding: 15px 20px;

    border-radius: 18px;

    min-width: 130px;
}

.hero-stat-number {
    color: #FFFFFF;

    font-size: 23px;
    font-weight: 800;
}

.hero-stat-label {
    color: #BFD3E9;

    font-size: 11px;
    font-weight: 700;

    margin-top: 3px;
}

/* ------------------------------------------------------------
   SECTION HEADINGS
------------------------------------------------------------ */

.section-kicker {
    color: #1769E0;

    font-size: 12px;
    font-weight: 800;

    letter-spacing: 2px;
}

.section-title {
    font-size: 48px;
    font-weight: 800;

    letter-spacing: -2px;

    color: #10233D;

    margin-top: 8px;
}

.section-text {
    color: #63728A;

    font-size: 16px;
    line-height: 1.8;

    margin-top: 10px;
}

/* ------------------------------------------------------------
   FEATURE CARDS
------------------------------------------------------------ */

.feature-card {
    height: 100%;

    background: #FFFFFF;

    border: 1px solid #E2EAF2;

    border-radius: 24px;

    padding: 28px;

    box-shadow: 0 12px 35px rgba(16, 35, 61, 0.06);

    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-8px);

    border-color: #A9C9F5;

    box-shadow: 0 22px 45px rgba(23, 105, 224, 0.14);
}

.feature-icon {
    width: 60px;
    height: 60px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: linear-gradient(135deg, #E5F1FF, #D4E8FF);

    border-radius: 18px;

    font-size: 28px;
}

.feature-title {
    margin-top: 20px;

    color: #10233D;

    font-size: 21px;
    font-weight: 800;
}

.feature-text {
    margin-top: 9px;

    color: #6C7B90;

    font-size: 13px;
    line-height: 1.7;
}

/* ------------------------------------------------------------
   PREDICTION CONTAINER
------------------------------------------------------------ */

.prediction-container {
    background: #FFFFFF;

    border: 1px solid #E2EAF2;

    border-radius: 30px;

    padding: 35px;

    box-shadow: 0 15px 45px rgba(16, 35, 61, 0.08);

    animation: fadeUp 0.8s ease;
}

.prediction-title {
    font-size: 36px;

    color: #10233D;

    font-weight: 800;

    letter-spacing: -1px;
}

.prediction-subtitle {
    color: #6C7B90;

    font-size: 14px;

    margin-top: 7px;
}

/* ------------------------------------------------------------
   INPUTS
------------------------------------------------------------ */

.stNumberInput label,
.stSelectbox label {
    color: #1E3555 !important;

    font-size: 14px !important;

    font-weight: 800 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    min-height: 48px;

    background: #F8FBFF !important;

    border: 1.5px solid #D7E2EF !important;

    border-radius: 14px !important;
}

input {
    color: #10233D !important;

    font-size: 15px !important;

    font-weight: 600 !important;
}

div[data-baseweb="select"] span {
    color: #10233D !important;

    font-weight: 600 !important;
}

/* ------------------------------------------------------------
   PREDICT BUTTON
------------------------------------------------------------ */

.predict-btn-container .stButton > button {
    min-height: 60px !important;

    background: linear-gradient(
        135deg,
        #1769E0,
        #0D3F86
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 18px !important;

    font-size: 16px !important;

    font-weight: 800 !important;

    animation: glow 3s infinite !important;
}

.predict-btn-container .stButton > button:hover {
    transform: translateY(-3px) !important;
}

/* ------------------------------------------------------------
   RESULT CARD
------------------------------------------------------------ */

.result-card {
    background:
        linear-gradient(
            135deg,
            #0D2B52,
            #1769E0
        );

    border-radius: 28px;

    padding: 45px 30px;

    text-align: center;

    color: white;

    min-height: 360px;

    display: flex;
    flex-direction: column;

    justify-content: center;

    animation: floatCard 5s ease-in-out infinite;

    box-shadow: 0 25px 55px rgba(23, 105, 224, 0.25);
}

.result-icon {
    font-size: 60px;
}

.result-label {
    color: #BFD9F8;

    font-size: 14px;

    font-weight: 800;

    letter-spacing: 1.5px;

    margin-top: 15px;
}

.result-price {
    color: white;

    font-size: 55px;

    font-weight: 800;

    margin-top: 12px;

    letter-spacing: -2px;
}

.result-note {
    margin-top: 18px;

    color: #D6E9FF;

    font-size: 13px;

    line-height: 1.7;
}

/* ------------------------------------------------------------
   SUMMARY CARDS
------------------------------------------------------------ */

.summary-card {
    background: #F7FAFE;

    border: 1px solid #E2EAF2;

    border-radius: 18px;

    padding: 20px;
}

.summary-label {
    color: #78869A;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1px;
}

.summary-value {
    color: #10233D;

    font-size: 19px;

    font-weight: 800;

    margin-top: 6px;
}

/* ------------------------------------------------------------
   FOOTER
------------------------------------------------------------ */

.footer-card {
    margin-top: 45px;

    background: #10233D;

    border-radius: 28px;

    padding: 30px;

    text-align: center;

    color: #BFD0E3;
}

.footer-title {
    color: white;

    font-size: 22px;

    font-weight: 800;
}

.footer-text {
    margin-top: 8px;

    font-size: 13px;
}

.footer-name {
    color: #75B6FF;

    font-weight: 800;
}

/* ------------------------------------------------------------
   MOBILE
------------------------------------------------------------ */

@media (max-width: 768px) {

    .hero-title {
        font-size: 46px;
    }

    .section-title {
        font-size: 34px;
    }

    .prediction-title {
        font-size: 30px;
    }

    .hero-card {
        min-height: 540px;
    }

    .hero-stat-row {
        flex-wrap: wrap;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER + NAVIGATION
# ============================================================

st.markdown("""
<div class="logo-card">
    <div class="logo-title">
        HOME<span>NIQ</span>
    </div>

    <div class="logo-subtitle">
        AI REAL ESTATE INTELLIGENCE
    </div>
</div>
""", unsafe_allow_html=True)


st.write("")

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("⌂  HOME", key="home_nav"):
        st.session_state.page = "Home"

with nav2:
    if st.button("✦  PREDICT", key="predict_nav"):
        st.session_state.page = "Predict"

with nav3:
    if st.button("▥  INSIGHTS", key="insights_nav"):
        st.session_state.page = "Insights"

with nav4:
    if st.button("◎  PROJECT", key="project_nav"):
        st.session_state.page = "Project"

with nav5:
    if st.button("START NOW  →", key="start_nav"):
        st.session_state.page = "Predict"


st.write("")
st.write("")


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero-card">
        <div class="hero-content">

            <div class="hero-badge">
                ✦ MACHINE LEARNING POWERED
            </div>

            <div class="hero-title">
                Know What Your<br>
                Home Is <span>Worth.</span>
            </div>

            <div class="hero-text">
                HOMENIQ uses Machine Learning to analyze important
                property features and generate intelligent house price
                predictions in seconds.
            </div>

            <div class="hero-stat-row">

                <div class="hero-stat">
                    <div class="hero-stat-number">
                        97.24%
                    </div>
                    <div class="hero-stat-label">
                        R² MODEL SCORE
                    </div>
                </div>

                <div class="hero-stat">
                    <div class="hero-stat-number">
                        8
                    </div>
                    <div class="hero-stat-label">
                        PROPERTY FEATURES
                    </div>
                </div>

                <div class="hero-stat">
                    <div class="hero-stat-number">
                        AI
                    </div>
                    <div class="hero-stat-label">
                        SMART VALUATION
                    </div>
                </div>

            </div>

        </div>
    </div>
    """, unsafe_allow_html=True)


    st.write("")
    st.write("")

    st.markdown("""
    <div class="section-kicker">
        WHY HOMENIQ
    </div>

    <div class="section-title">
        Smarter Property Decisions.
    </div>

    <div class="section-text">
        A modern Machine Learning application designed to transform
        property information into intelligent price predictions.
    </div>
    """, unsafe_allow_html=True)


    st.write("")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>

            <div class="feature-title">
                Machine Learning
            </div>

            <div class="feature-text">
                A trained Linear Regression model analyzes important
                property characteristics to estimate house values.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>

            <div class="feature-title">
                Instant Prediction
            </div>

            <div class="feature-text">
                Enter your property details and receive a house
                price prediction instantly.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>

            <div class="feature-title">
                Data Driven
            </div>

            <div class="feature-text">
                Predictions are generated from meaningful housing
                features and a carefully evaluated ML model.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# PREDICTION PAGE
# ============================================================

elif st.session_state.page == "Predict":

    st.markdown("""
    <div class="prediction-container">

        <div class="section-kicker">
            PROPERTY VALUATION
        </div>

        <div class="prediction-title">
            Estimate Your Property Value
        </div>

        <div class="prediction-subtitle">
            Enter your property information and let HOMENIQ
            calculate an AI-powered price prediction.
        </div>

    </div>
    """, unsafe_allow_html=True)


    st.write("")


    form_col, result_col = st.columns([1.15, 0.85], gap="large")


    # --------------------------------------------------------
    # PROPERTY FORM
    # --------------------------------------------------------

    with form_col:

        st.markdown("""
        <div class="prediction-container">

            <div class="prediction-title">
                🏠 Property Details
            </div>

            <div class="prediction-subtitle">
                Complete the details below to generate your prediction.
            </div>

        </div>
        """, unsafe_allow_html=True)


        st.write("")


        col1, col2 = st.columns(2)


        with col1:

            overall_qual = st.selectbox(
                "Overall Quality",
                options=list(range(1, 11)),
                index=5
            )

            gr_liv_area = st.number_input(
                "Living Area (sq ft)",
                min_value=100,
                max_value=20000,
                value=1800
            )

            garage_cars = st.selectbox(
                "Garage Capacity",
                options=[0, 1, 2, 3, 4, 5],
                index=2
            )

            year_built = st.number_input(
                "Year Built",
                min_value=1800,
                max_value=2026,
                value=2005
            )


        with col2:

            total_bsmt_sf = st.number_input(
                "Basement Area (sq ft)",
                min_value=0,
                max_value=10000,
                value=900
            )

            full_bath = st.selectbox(
                "Full Bathrooms",
                options=[0, 1, 2, 3, 4, 5],
                index=2
            )

            bedrooms = st.selectbox(
                "Bedrooms",
                options=[1, 2, 3, 4, 5, 6, 7, 8],
                index=2
            )

            lot_area = st.number_input(
                "Lot Area (sq ft)",
                min_value=500,
                max_value=100000,
                value=8500
            )


        st.write("")


        st.markdown('<div class="predict-btn-container">', unsafe_allow_html=True)

        predict_button = st.button(
            "GENERATE AI PRICE PREDICTION  →",
            key="main_predict_button"
        )

        st.markdown('</div>', unsafe_allow_html=True)


    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    with result_col:

        if predict_button:

            input_data = pd.DataFrame([[
                overall_qual,
                gr_liv_area,
                garage_cars,
                total_bsmt_sf,
                year_built,
                full_bath,
                bedrooms,
                lot_area
            ]], columns=[
                "OverallQual",
                "GrLivArea",
                "GarageCars",
                "TotalBsmtSF",
                "YearBuilt",
                "FullBath",
                "BedroomAbvGr",
                "LotArea"
            ])


            prediction = model.predict(input_data)[0]


            st.markdown(f"""
            <div class="result-card">

                <div class="result-icon">
                    🏡
                </div>

                <div class="result-label">
                    ESTIMATED HOUSE VALUE
                </div>

                <div class="result-price">
                    ${prediction:,.0f}
                </div>

                <div class="result-note">
                    Your Machine Learning prediction has been
                    successfully generated based on the provided
                    property characteristics.
                </div>

            </div>
            """, unsafe_allow_html=True)


        else:

            prediction = None


            st.markdown("""
            <div class="result-card">

                <div class="result-icon">
                    ✦
                </div>

                <div class="result-label">
                    READY FOR ANALYSIS
                </div>

                <div class="result-price">
                    HOMENIQ AI
                </div>

                <div class="result-note">
                    Enter the property details and generate an
                    intelligent house price prediction.
                </div>

            </div>
            """, unsafe_allow_html=True)


        st.write("")


        s1, s2 = st.columns(2)


        with s1:

            st.markdown(f"""
            <div class="summary-card">

                <div class="summary-label">
                    PROPERTY SIZE
                </div>

                <div class="summary-value">
                    {gr_liv_area:,} sq ft
                </div>

            </div>
            """, unsafe_allow_html=True)


        with s2:

            st.markdown(f"""
            <div class="summary-card">

                <div class="summary-label">
                    OVERALL QUALITY
                </div>

                <div class="summary-value">
                    {overall_qual} / 10
                </div>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# INSIGHTS PAGE
# ============================================================

elif st.session_state.page == "Insights":

    st.markdown("""
    <div class="section-kicker">
        MODEL PERFORMANCE
    </div>

    <div class="section-title">
        Behind the Prediction.
    </div>

    <div class="section-text">
        The project evaluates multiple regression algorithms and
        selects the best-performing model for deployment.
    </div>
    """, unsafe_allow_html=True)


    st.write("")
    st.write("")


    m1, m2, m3, m4 = st.columns(4)


    with m1:
        st.metric(
            "Best Model",
            "Linear Regression"
        )


    with m2:
        st.metric(
            "Testing R²",
            "0.9724"
        )


    with m3:
        st.metric(
            "RMSE",
            "$12,505"
        )


    with m4:
        st.metric(
            "MAE",
            "$10,432"
        )


    st.write("")
    st.write("")


    st.markdown("""
    <div class="prediction-container">

        <div class="prediction-title">
            Model Evaluation
        </div>

        <div class="prediction-subtitle">
            The following algorithms were compared during the project.
        </div>

    </div>
    """, unsafe_allow_html=True)


    st.write("")


    models = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Tuned Gradient Boosting",
            "Tuned Random Forest",
            "Tuned Decision Tree"
        ],

        "Testing R²": [
            0.972437,
            0.952775,
            0.867624,
            0.705922
        ],

        "MAE": [
            10431.66,
            13084.38,
            21414.52,
            33382.12
        ]
    })


    st.dataframe(
        models,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PROJECT PAGE
# ============================================================

elif st.session_state.page == "Project":

    st.markdown("""
    <div class="section-kicker">
        ABOUT THE PROJECT
    </div>

    <div class="section-title">
        House Price Prediction with AI.
    </div>

    <div class="section-text">
        This project is an end-to-end Machine Learning application
        designed to predict residential property prices from important
        housing characteristics.
    </div>
    """, unsafe_allow_html=True)


    st.write("")
    st.write("")


    a1, a2 = st.columns(2)


    with a1:

        st.markdown("""
        <div class="feature-card">

            <div class="feature-icon">
                🔬
            </div>

            <div class="feature-title">
                Project Workflow
            </div>

            <div class="feature-text">

                Data Preparation<br><br>

                Exploratory Data Analysis<br><br>

                Model Training<br><br>

                Cross Validation<br><br>

                Hyperparameter Tuning<br><br>

                Model Deployment

            </div>

        </div>
        """, unsafe_allow_html=True)


    with a2:

        st.markdown("""
        <div class="feature-card">

            <div class="feature-icon">
                🧰
            </div>

            <div class="feature-title">
                Technologies Used
            </div>

            <div class="feature-text">

                Python<br><br>

                Pandas & NumPy<br><br>

                Scikit-learn<br><br>

                Joblib<br><br>

                Streamlit<br><br>

                Machine Learning

            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer-card">

    <div class="footer-title">
        HOMENIQ — AI Real Estate Intelligence
    </div>

    <div class="footer-text">
        Developed by
        <span class="footer-name">
            Shiza Eman
        </span>
        &nbsp; | &nbsp;
        Machine Learning Project
        &nbsp; | &nbsp;
        2026
    </div>

</div>
""" )
