import streamlit as st
import pandas as pd
import joblib

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Gamer Engagement Predictor",
    page_icon="🎮",
    layout="wide"
)

# ---------------------------------
# Custom CSS - Final Fixed UI
# ---------------------------------
st.markdown("""
<style>
    /* ===============================
       Main App Background
    =============================== */
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        color: #0f172a;
    }

    /* ===============================
       Fix Streamlit Top Header / Deploy / Menu Visibility
    =============================== */
    [data-testid="stHeader"] {
        background: rgba(248, 250, 252, 0.95) !important;
        color: #0f172a !important;
    }

    [data-testid="stToolbar"] {
        color: #0f172a !important;
    }

    [data-testid="stToolbar"] button,
    [data-testid="stToolbar"] button *,
    [data-testid="stHeader"] button,
    [data-testid="stHeader"] button *,
    [data-testid="stBaseButton-header"],
    [data-testid="stBaseButton-header"] * {
        color: #0f172a !important;
        fill: #0f172a !important;
        stroke: #0f172a !important;
    }

    [data-testid="stToolbar"] svg,
    [data-testid="stHeader"] svg {
        color: #0f172a !important;
        fill: #0f172a !important;
        stroke: #0f172a !important;
    }

    /* ===============================
       Normal Text Visibility
    =============================== */
    h1, h2, h3, h4, h5, h6,
    p, li, label,
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #0f172a !important;
    }

    /* ===============================
       Sidebar
    =============================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #1e1b4b 100%);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {
        color: #f8fafc !important;
    }

    /* Sidebar alert text fix */
    [data-testid="stSidebar"] [data-testid="stAlert"] p,
    [data-testid="stSidebar"] [data-testid="stAlert"] div {
        color: #0f172a !important;
    }

    /* ===============================
       Hero Section
    =============================== */
    .hero {
        padding: 38px;
        border-radius: 26px;
        background: linear-gradient(135deg, #7c3aed, #2563eb, #06b6d4);
        color: white !important;
        text-align: center;
        margin-bottom: 28px;
        box-shadow: 0 15px 35px rgba(37, 99, 235, 0.25);
    }

    .hero h1,
    .hero p {
        color: white !important;
    }

    .hero h1 {
        font-size: 44px;
        font-weight: 900;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.95;
        margin-bottom: 0;
    }

    /* ===============================
       Cards
    =============================== */
    .info-card {
        background: #ffffff;
        color: #0f172a !important;
        padding: 24px;
        border-radius: 22px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
        margin-bottom: 20px;
    }

    .info-card h1,
    .info-card h2,
    .info-card h3,
    .info-card h4,
    .info-card p,
    .info-card li,
    .info-card span {
        color: #0f172a !important;
    }

    .small-muted {
        color: #64748b !important;
        font-size: 14px;
    }

    /* ===============================
       Tabs
    =============================== */
    [data-baseweb="tab"] p {
        color: #0f172a !important;
        font-weight: 700 !important;
    }

    [aria-selected="true"] p {
        color: #2563eb !important;
    }

    /* ===============================
       Inputs / Selectboxes
    =============================== */
    label,
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] p {
        color: #0f172a !important;
        font-weight: 700 !important;
    }

    input,
    textarea,
    [data-baseweb="input"] input,
    [data-baseweb="textarea"] textarea {
        color: #0f172a !important;
        background-color: #ffffff !important;
    }

    [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-color: #cbd5e1 !important;
    }

    [data-baseweb="select"] span,
    [data-baseweb="select"] div {
        color: #0f172a !important;
    }

    [role="listbox"] {
        background-color: #ffffff !important;
    }

    [role="option"] {
        color: #0f172a !important;
        background-color: #ffffff !important;
    }

    [role="option"]:hover {
        background-color: #e0e7ff !important;
        color: #0f172a !important;
    }

    /* ===============================
       File Uploader
    =============================== */
    [data-testid="stFileUploaderDropzone"] {
        border-radius: 18px;
        border: 2px dashed #7c3aed;
        background: #faf5ff;
    }

    [data-testid="stFileUploaderDropzone"] p,
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small {
        color: #0f172a !important;
    }

    [data-testid="stFileUploader"] button,
    [data-testid="stFileUploader"] button * {
        background-color: #111827 !important;
        color: #ffffff !important;
        border-color: #111827 !important;
    }

    /* ===============================
       Expander
    =============================== */
    [data-testid="stExpander"] {
        background-color: #ffffff;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
    }

    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] li,
    [data-testid="stExpander"] summary {
        color: #0f172a !important;
    }

    /* ===============================
       Metrics
    =============================== */
    [data-testid="stMetric"] {
        background: #ffffff;
        padding: 16px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] p {
        color: #475569 !important;
        font-weight: 700;
    }

    [data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-size: 28px;
        font-weight: 900;
    }

    /* ===============================
       Prediction Result Card
    =============================== */
    .result-card {
        padding: 34px;
        border-radius: 26px;
        text-align: center;
        color: white !important;
        margin-top: 22px;
        margin-bottom: 22px;
        box-shadow: 0 16px 35px rgba(15, 23, 42, 0.20);
    }

    .result-card div {
        color: inherit !important;
    }

    .high {
        background: linear-gradient(135deg, #16a34a, #22c55e);
        color: white !important;
    }

    .medium {
        background: linear-gradient(135deg, #f59e0b, #facc15);
        color: #111827 !important;
    }

    .low {
        background: linear-gradient(135deg, #dc2626, #ef4444);
        color: white !important;
    }

    .result-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .result-value {
        font-size: 46px;
        font-weight: 900;
    }

    /* ===============================
       Main Buttons
    =============================== */
    div.stButton > button,
    div.stFormSubmitButton > button {
        height: 3.3em;
        border-radius: 15px;
        font-size: 17px;
        font-weight: 800;
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        transition: 0.3s;
    }

    div.stButton > button *,
    div.stFormSubmitButton > button * {
        color: white !important;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.35);
        color: white !important;
    }

    div.stButton > button:hover *,
    div.stFormSubmitButton > button:hover * {
        color: white !important;
    }

    /* ===============================
       Download Buttons
    =============================== */
    div.stDownloadButton > button {
        height: 3.1em;
        border-radius: 15px;
        font-size: 16px;
        font-weight: 800;
        background: linear-gradient(135deg, #059669, #10b981) !important;
        color: white !important;
        border: none !important;
    }

    div.stDownloadButton > button * {
        color: white !important;
    }

    div.stDownloadButton > button:hover {
        color: white !important;
        box-shadow: 0 8px 22px rgba(16, 185, 129, 0.35);
    }

    div.stDownloadButton > button:hover * {
        color: white !important;
    }

    /* ===============================
       Alerts
    =============================== */
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] div {
        color: #0f172a !important;
    }

    /* ===============================
       Code Blocks
    =============================== */
    code {
        color: #0f172a !important;
        background-color: #f1f5f9 !important;
    }

    pre {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
    }

    /* ===============================
       Dataframe Text
    =============================== */
    [data-testid="stDataFrame"] {
        color: #0f172a !important;
    }

    /* ===============================
       Footer
    =============================== */
    .footer {
        text-align: center;
        color: #64748b !important;
        margin-top: 40px;
        padding-bottom: 20px;
        font-size: 14px;
    }

    .footer p,
    .footer span,
    .footer div {
        color: #64748b !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Load Trained Model
# ---------------------------------
@st.cache_resource
def load_model():
    return joblib.load("final_model.pkl")


try:
    model = load_model()
except FileNotFoundError:
    st.error("❌ `final_model.pkl` not found. Please place it in the same folder as this app.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ---------------------------------
# Constants
# ---------------------------------
engagement_mapping = {
    0: "Low",
    1: "Medium",
    2: "High"
}

engagement_icons = {
    "Low": "📉",
    "Medium": "⚡",
    "High": "🔥"
}

engagement_classes = {
    "Low": "low",
    "Medium": "medium",
    "High": "high"
}

model_feature_columns = [
    "Age",
    "PlayTimeHours",
    "InGamePurchases",
    "SessionsPerWeek",
    "AvgSessionDurationMinutes",
    "PlayerLevel",
    "AchievementsUnlocked",
    "Gender",
    "Location",
    "GameGenre",
    "GameDifficulty"
]

expected_csv_columns = [
    "PlayerID",
    "Age",
    "Gender",
    "Location",
    "GameGenre",
    "PlayTimeHours",
    "InGamePurchases",
    "GameDifficulty",
    "SessionsPerWeek",
    "AvgSessionDurationMinutes",
    "PlayerLevel",
    "AchievementsUnlocked"
]

numeric_columns = [
    "Age",
    "PlayTimeHours",
    "InGamePurchases",
    "SessionsPerWeek",
    "AvgSessionDurationMinutes",
    "PlayerLevel",
    "AchievementsUnlocked"
]

categorical_columns = [
    "Gender",
    "Location",
    "GameGenre",
    "GameDifficulty"
]

# ---------------------------------
# Helper Functions
# ---------------------------------
def get_engagement_label(value):
    try:
        value_int = int(value)
        if value_int in engagement_mapping:
            return engagement_mapping[value_int]
    except Exception:
        pass

    return str(value).strip().title()


def get_probability_dataframe(input_df):
    probabilities = model.predict_proba(input_df)[0]

    if hasattr(model, "classes_"):
        model_classes = model.classes_
    else:
        model_classes = list(range(len(probabilities)))

    probability_df = pd.DataFrame({
        "Engagement Level": [get_engagement_label(c) for c in model_classes],
        "Probability": probabilities
    })

    order_map = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    probability_df["Order"] = probability_df["Engagement Level"].map(order_map).fillna(99)
    probability_df = probability_df.sort_values("Order").drop(columns="Order")

    return probability_df


def show_prediction_result(result):
    result_class = engagement_classes.get(result, "medium")
    result_icon = engagement_icons.get(result, "🎮")

    st.markdown(f"""
    <div class="result-card {result_class}">
        <div class="result-title">Predicted Engagement Level</div>
        <div class="result-value">{result_icon} {result}</div>
    </div>
    """, unsafe_allow_html=True)


def show_probability_section(input_df):
    try:
        probability_df = get_probability_dataframe(input_df)

        st.subheader("📈 Prediction Confidence")

        highest_probability = probability_df["Probability"].max()

        st.metric(
            label="Highest Confidence",
            value=f"{highest_probability:.2%}"
        )

        st.bar_chart(
            probability_df.set_index("Engagement Level")["Probability"]
        )

        st.markdown("#### Confidence Breakdown")

        for _, row in probability_df.iterrows():
            level = row["Engagement Level"]
            probability = row["Probability"]
            icon = engagement_icons.get(level, "🎮")

            st.write(f"**{icon} {level}** — {probability:.2%}")
            st.progress(float(probability))

        probability_display = probability_df.copy()
        probability_display["Probability"] = probability_display["Probability"].map(lambda x: f"{x:.2%}")

        st.dataframe(
            probability_display,
            use_container_width=True,
            hide_index=True
        )

    except Exception:
        st.info("Prediction confidence is not available for this model.")


def format_probability_columns(df):
    formatted_df = df.copy()

    probability_cols = [
        col for col in formatted_df.columns
        if col.startswith("Probability_") or col == "PredictionConfidence"
    ]

    for col in probability_cols:
        formatted_df[col] = formatted_df[col].map(
            lambda x: f"{x:.2%}" if pd.notnull(x) else ""
        )

    return formatted_df


# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.title("🎮 App Guide")

    st.markdown("""
    This app predicts a player's engagement level based on gameplay behavior.

    ### Engagement Levels
    - 🔴 **Low**
    - 🟡 **Medium**
    - 🟢 **High**

    ### Features
    - 🎯 Single player prediction
    - 📂 CSV batch prediction
    - 📊 Confidence scores
    - ⬇ Download predicted CSV
    """)

    st.divider()

    st.success("✅ Model Loaded Successfully")

    st.markdown("""
    ### Tip
    Higher weekly sessions, longer session duration, more achievements, and higher player level usually indicate stronger engagement.
    """)

# ---------------------------------
# Hero Header
# ---------------------------------
st.markdown("""
<div class="hero">
    <h1>🎮 Gamer Engagement & Retention Predictor</h1>
    <p>Predict whether a gamer has Low, Medium, or High engagement using machine learning.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# Tabs
# ---------------------------------
single_tab, batch_tab, about_tab = st.tabs([
    "🎯 Single Prediction",
    "📂 Batch CSV Prediction",
    "ℹ️ About Project"
])

# =================================================
# Single Prediction Tab
# =================================================
with single_tab:
    st.markdown("""
    <div class="info-card">
        <h3>🧑‍💻 Single Player Prediction</h3>
        <p class="small-muted">
            Enter one player's details and predict their engagement level instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("single_prediction_form"):
        st.subheader("👤 Player Profile")

        profile_col1, profile_col2, profile_col3, profile_col4 = st.columns(4)

        with profile_col1:
            age = st.number_input(
                "Age",
                min_value=10,
                max_value=100,
                value=25,
                step=1
            )

        with profile_col2:
            gender = st.selectbox(
                "Gender",
                ["Male", "Female"]
            )

        with profile_col3:
            location = st.selectbox(
                "Location",
                ["Asia", "Europe", "USA", "Other"]
            )

        with profile_col4:
            play_time_hours = st.number_input(
                "Play Time Hours",
                min_value=0.0,
                value=20.0,
                step=1.0
            )

        st.divider()

        st.subheader("🎮 Gameplay Behavior")

        behavior_col1, behavior_col2 = st.columns(2)

        with behavior_col1:
            in_game_purchases = st.number_input(
                "💰 In-Game Purchases",
                min_value=0,
                value=5,
                step=1
            )

            sessions_per_week = st.number_input(
                "🎯 Sessions Per Week",
                min_value=0,
                value=10,
                step=1
            )

            avg_session_duration = st.number_input(
                "⏱ Average Session Duration Minutes",
                min_value=0.0,
                value=60.0,
                step=5.0
            )

        with behavior_col2:
            player_level = st.number_input(
                "🏆 Player Level",
                min_value=1,
                value=10,
                step=1
            )

            achievements_unlocked = st.number_input(
                "🥇 Achievements Unlocked",
                min_value=0,
                value=20,
                step=1
            )

            game_genre = st.selectbox(
                "🎮 Game Genre",
                [
                    "Action",
                    "Adventure",
                    "RPG",
                    "Simulation",
                    "Sports",
                    "Strategy"
                ]
            )

            game_difficulty = st.selectbox(
                "⚔️ Game Difficulty",
                [
                    "Easy",
                    "Medium",
                    "Hard"
                ]
            )

        submitted = st.form_submit_button(
            "🚀 Predict Engagement Level",
            use_container_width=True
        )

    if submitted:
        input_df = pd.DataFrame({
            "Age": [age],
            "PlayTimeHours": [play_time_hours],
            "InGamePurchases": [in_game_purchases],
            "SessionsPerWeek": [sessions_per_week],
            "AvgSessionDurationMinutes": [avg_session_duration],
            "PlayerLevel": [player_level],
            "AchievementsUnlocked": [achievements_unlocked],
            "Gender": [gender],
            "Location": [location],
            "GameGenre": [game_genre],
            "GameDifficulty": [game_difficulty]
        })

        input_df = input_df[model_feature_columns]

        try:
            with st.spinner("Predicting engagement level..."):
                prediction = model.predict(input_df)[0]
                result = get_engagement_label(prediction)

            show_prediction_result(result)
            show_probability_section(input_df)

        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")

# =================================================
# Batch Prediction Tab
# =================================================
with batch_tab:
    st.markdown("""
    <div class="info-card">
        <h3>📂 Batch Prediction</h3>
        <p class="small-muted">
            Upload a CSV file containing multiple player records. The app will predict engagement for every player and allow you to download the results.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📌 Required CSV Format", expanded=True):
        st.markdown("Your CSV file should contain these columns exactly:")

        st.code(", ".join(expected_csv_columns))

        sample_df = pd.DataFrame({
            "PlayerID": [1, 2, 3],
            "Age": [25, 30, 22],
            "Gender": ["Male", "Female", "Male"],
            "Location": ["Asia", "Europe", "USA"],
            "GameGenre": ["Action", "RPG", "Strategy"],
            "PlayTimeHours": [20, 35, 15],
            "InGamePurchases": [5, 10, 2],
            "GameDifficulty": ["Medium", "Hard", "Easy"],
            "SessionsPerWeek": [10, 15, 6],
            "AvgSessionDurationMinutes": [60, 90, 45],
            "PlayerLevel": [12, 25, 8],
            "AchievementsUnlocked": [20, 45, 10]
        })

        st.markdown("#### Example CSV Preview")
        st.dataframe(sample_df, use_container_width=True, hide_index=True)

        template_csv = sample_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Sample CSV Template",
            data=template_csv,
            file_name="sample_players_template.csv",
            mime="text/csv",
            use_container_width=True
        )

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"],
        key="batch_csv_uploader"
    )

    if uploaded_file is not None:
        try:
            uploaded_signature = f"{uploaded_file.name}_{uploaded_file.size}"

            if st.session_state.get("uploaded_signature") != uploaded_signature:
                st.session_state["uploaded_signature"] = uploaded_signature
                st.session_state["batch_result_df"] = None

            batch_df = pd.read_csv(uploaded_file)

            # Clean column names
            batch_df.columns = batch_df.columns.str.strip()

            # Remove unnamed index columns
            batch_df = batch_df.loc[:, ~batch_df.columns.str.contains("^Unnamed")]

            st.subheader("👀 Uploaded File Preview")
            st.dataframe(batch_df.head(10), use_container_width=True)

            total_players = len(batch_df)

            metric_col1, metric_col2, metric_col3 = st.columns(3)

            with metric_col1:
                st.metric("Total Rows", total_players)

            with metric_col2:
                st.metric("Required Columns", len(expected_csv_columns))

            with metric_col3:
                st.metric("Model Features", len(model_feature_columns))

            missing_columns = [
                col for col in expected_csv_columns
                if col not in batch_df.columns
            ]

            if missing_columns:
                st.error("❌ Your CSV file is missing these required columns:")
                st.write(missing_columns)

            else:
                st.success("✅ CSV format looks good!")

                clean_batch_df = batch_df.copy()

                # Convert numeric columns
                for col in numeric_columns:
                    clean_batch_df[col] = pd.to_numeric(clean_batch_df[col], errors="coerce")

                # Clean categorical columns
                for col in categorical_columns:
                    clean_batch_df[col] = clean_batch_df[col].astype(str).str.strip()

                missing_value_counts = clean_batch_df[model_feature_columns].isna().sum()
                missing_value_counts = missing_value_counts[missing_value_counts > 0]

                if not missing_value_counts.empty:
                    st.error("❌ Some required columns contain empty or invalid values:")
                    st.dataframe(
                        missing_value_counts.reset_index().rename(
                            columns={
                                "index": "Column",
                                0: "Missing/Invalid Values"
                            }
                        ),
                        use_container_width=True,
                        hide_index=True
                    )

                else:
                    include_probabilities = st.checkbox(
                        "Add prediction confidence/probability columns if supported by model",
                        value=True
                    )

                    if st.button("🚀 Predict Uploaded File", use_container_width=True):
                        try:
                            with st.spinner("Running batch predictions..."):
                                prediction_input = clean_batch_df[model_feature_columns]

                                predictions = model.predict(prediction_input)

                                result_df = batch_df.copy()
                                result_df["EngagementPrediction"] = [
                                    get_engagement_label(p) for p in predictions
                                ]

                                if include_probabilities:
                                    try:
                                        probabilities = model.predict_proba(prediction_input)

                                        if hasattr(model, "classes_"):
                                            model_classes = model.classes_
                                        else:
                                            model_classes = list(range(probabilities.shape[1]))

                                        for idx, class_value in enumerate(model_classes):
                                            label = get_engagement_label(class_value)
                                            result_df[f"Probability_{label}"] = probabilities[:, idx]

                                        result_df["PredictionConfidence"] = probabilities.max(axis=1)

                                    except Exception:
                                        st.info("Probability columns were not added because this model does not support predict_proba.")

                                st.session_state["batch_result_df"] = result_df

                            st.success("✅ Batch predictions completed!")

                        except Exception as e:
                            st.error(f"❌ Batch prediction failed: {e}")

                    if st.session_state.get("batch_result_df") is not None:
                        result_df = st.session_state["batch_result_df"]

                        st.subheader("📊 Prediction Results Preview")

                        preview_df = format_probability_columns(result_df.head(20))
                        st.dataframe(preview_df, use_container_width=True)

                        st.subheader("📈 Prediction Summary")

                        summary_df = (
                            result_df["EngagementPrediction"]
                            .value_counts()
                            .reset_index()
                        )
                        summary_df.columns = ["Engagement Level", "Count"]

                        low_count = int(
                            summary_df.loc[
                                summary_df["Engagement Level"] == "Low",
                                "Count"
                            ].sum()
                        )

                        medium_count = int(
                            summary_df.loc[
                                summary_df["Engagement Level"] == "Medium",
                                "Count"
                            ].sum()
                        )

                        high_count = int(
                            summary_df.loc[
                                summary_df["Engagement Level"] == "High",
                                "Count"
                            ].sum()
                        )

                        count_col1, count_col2, count_col3 = st.columns(3)

                        with count_col1:
                            st.metric("📉 Low", low_count)

                        with count_col2:
                            st.metric("⚡ Medium", medium_count)

                        with count_col3:
                            st.metric("🔥 High", high_count)

                        st.bar_chart(
                            summary_df.set_index("Engagement Level")["Count"]
                        )

                        st.dataframe(
                            summary_df,
                            use_container_width=True,
                            hide_index=True
                        )

                        csv = result_df.to_csv(index=False).encode("utf-8")

                        st.download_button(
                            label="⬇ Download Predicted CSV",
                            data=csv,
                            file_name="predicted_players.csv",
                            mime="text/csv",
                            use_container_width=True
                        )

        except Exception as e:
            st.error(f"❌ Error while processing file: {e}")

# =================================================
# About Tab
# =================================================
with about_tab:
    st.markdown("""
    <div class="info-card">
        <h3>ℹ️ About This Project</h3>
        <p>
            This machine learning application predicts gamer engagement levels based on player behavior and gameplay patterns.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Input Features")
        st.markdown("""
        - Player age
        - Gender
        - Location
        - Game genre
        - Play time hours
        - In-game purchases
        - Game difficulty
        - Sessions per week
        - Average session duration
        - Player level
        - Achievements unlocked
        """)

    with col2:
        st.subheader("🤖 Model Details")
        st.markdown("""
        The model was built using:

        - Scikit-Learn Pipelines
        - Feature Engineering
        - SelectKBest Feature Selection
        - Random Forest / XGBoost
        - Hyperparameter Tuning with RandomizedSearchCV
        """)

    st.divider()

    st.subheader("📂 CSV Upload Format")

    st.markdown("""
    Your uploaded CSV should contain:

    ```text
    PlayerID, Age, Gender, Location, GameGenre, PlayTimeHours,
    InGamePurchases, GameDifficulty, SessionsPerWeek,
    AvgSessionDurationMinutes, PlayerLevel, AchievementsUnlocked
    ```

    `PlayerID` is kept in the output CSV but is not used by the model for prediction.
    """)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("""
<div class="footer">
    Built with ❤️ using Streamlit and Machine Learning
</div>
""", unsafe_allow_html=True)