import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LANDGUARD AI",
    page_icon="⛰️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    font-size: 20px;
    color: #666;
}

.risk-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.small-text {
    color: #666;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">⛰️ LANDGUARD AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Based Landslide Risk Monitoring & Early Warning System</div>',
    unsafe_allow_html=True
)

st.write("")

st.info(
    "SIH26001 | Disaster Management | "
    "AI-powered prediction and monitoring of landslide-prone areas"
)

# =========================================================
# CREATE SYNTHETIC TRAINING DATA
# =========================================================

np.random.seed(42)

N = 3000

data = pd.DataFrame({
    "rainfall": np.random.uniform(10, 400, N),
    "soil_moisture": np.random.uniform(10, 100, N),
    "slope": np.random.uniform(5, 70, N),
    "elevation": np.random.uniform(100, 4000, N),
    "historical_events": np.random.randint(0, 11, N)
})

# ---------------------------------------------------------
# Create realistic risk relationship
# ---------------------------------------------------------

risk_value = (
    0.012 * data["rainfall"]
    + 0.035 * data["soil_moisture"]
    + 0.055 * data["slope"]
    + 0.35 * data["historical_events"]
    - 0.00008 * data["elevation"]
)

# Add random environmental variation
risk_value += np.random.normal(0, 1.2, N)

# Use median so BOTH classes are guaranteed
threshold = np.median(risk_value)

data["landslide"] = (
    risk_value > threshold
).astype(int)

# Safety check
if data["landslide"].nunique() < 2:
    data.loc[:N // 2, "landslide"] = 0
    data.loc[N // 2:, "landslide"] = 1

# =========================================================
# TRAIN ML MODEL
# =========================================================

features = [
    "rainfall",
    "soil_moisture",
    "slope",
    "elevation",
    "historical_events"
]

X = data[features]
y = data["landslide"]

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌧️ Environmental Data")

st.sidebar.markdown(
    "Adjust environmental conditions to simulate a location."
)

rainfall = st.sidebar.slider(
    "Rainfall (mm)",
    min_value=0,
    max_value=400,
    value=180
)

soil_moisture = st.sidebar.slider(
    "Soil Moisture (%)",
    min_value=0,
    max_value=100,
    value=70
)

slope = st.sidebar.slider(
    "Slope (degrees)",
    min_value=0,
    max_value=70,
    value=35
)

elevation = st.sidebar.slider(
    "Elevation (m)",
    min_value=0,
    max_value=4000,
    value=1500
)

historical_events = st.sidebar.slider(
    "Historical Landslide Events",
    min_value=0,
    max_value=10,
    value=3
)

st.sidebar.divider()

selected_location = st.sidebar.selectbox(
    "📍 Select Location",
    [
        "East Sikkim",
        "West Sikkim",
        "Tawang",
        "Aizawl",
        "Shillong",
        "Gangtok",
        "Darjeeling",
        "Itanagar",
        "Kohima",
        "Agartala"
    ]
)

predict_button = st.sidebar.button(
    "🔍 ANALYZE RISK",
    use_container_width=True
)

# =========================================================
# PREDICTION
# =========================================================

input_data = pd.DataFrame([{
    "rainfall": rainfall,
    "soil_moisture": soil_moisture,
    "slope": slope,
    "elevation": elevation,
    "historical_events": historical_events
}])

# Predict probability safely

probabilities = model.predict_proba(input_data)[0]

if 1 in model.classes_:
    class_index = list(model.classes_).index(1)
    probability = probabilities[class_index]
else:
    probability = 0.0

risk_score = int(round(probability * 100))

# =========================================================
# RISK CLASSIFICATION
# =========================================================

if risk_score >= 80:

    risk_level = "VERY HIGH"
    alert_message = "🚨 IMMEDIATE WARNING"
    action = "Deploy emergency response teams and inspect vulnerable zones."

elif risk_score >= 60:

    risk_level = "HIGH"
    alert_message = "⚠️ HIGH RISK"
    action = "Increase monitoring and prepare emergency response teams."

elif risk_score >= 40:

    risk_level = "MODERATE"
    alert_message = "🟡 MODERATE RISK"
    action = "Continue monitoring environmental conditions."

else:

    risk_level = "LOW"
    alert_message = "🟢 LOW RISK"
    action = "Normal monitoring recommended."

# =========================================================
# DASHBOARD METRICS
# =========================================================

st.header("📊 Current Risk Assessment")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Risk Score",
    f"{risk_score}%"
)

col2.metric(
    "Risk Level",
    risk_level
)

col3.metric(
    "Rainfall",
    f"{rainfall} mm"
)

col4.metric(
    "Soil Moisture",
    f"{soil_moisture}%"
)

# =========================================================
# ALERT
# =========================================================

st.subheader(f"📍 {selected_location}")

if risk_score >= 80:

    st.error(
        f"### {alert_message}\n\n"
        f"Landslide probability: **{risk_score}%**\n\n"
        f"Recommended action: {action}"
    )

elif risk_score >= 60:

    st.warning(
        f"### {alert_message}\n\n"
        f"Landslide probability: **{risk_score}%**\n\n"
        f"Recommended action: {action}"
    )

elif risk_score >= 40:

    st.warning(
        f"### {alert_message}\n\n"
        f"Landslide probability: **{risk_score}%**\n\n"
        f"Recommended action: {action}"
    )

else:

    st.success(
        f"### {alert_message}\n\n"
        f"Landslide probability: **{risk_score}%**\n\n"
        f"Recommended action: {action}"
    )

# =========================================================
# ENVIRONMENTAL FACTORS
# =========================================================

st.divider()

st.header("🔎 Environmental Risk Factors")

factor_data = pd.DataFrame({
    "Factor": [
        "Rainfall",
        "Soil Moisture",
        "Slope",
        "Elevation",
        "Historical Events"
    ],
    "Value": [
        rainfall,
        soil_moisture,
        slope,
        elevation / 40,
        historical_events * 10
    ]
})

fig_factors = px.bar(
    factor_data,
    x="Factor",
    y="Value",
    title="Current Environmental Conditions"
)

st.plotly_chart(
    fig_factors,
    use_container_width=True
)

# =========================================================
# WHY IS THIS AREA AT RISK?
# =========================================================

st.header("🧠 Why is this area at risk?")

reasons = []

if rainfall >= 200:
    reasons.append("🌧️ Very heavy rainfall detected.")
elif rainfall >= 150:
    reasons.append("🌧️ High rainfall detected.")

if soil_moisture >= 80:
    reasons.append("💧 Very high soil moisture.")
elif soil_moisture >= 65:
    reasons.append("💧 High soil moisture.")

if slope >= 45:
    reasons.append("⛰️ Very steep terrain.")
elif slope >= 30:
    reasons.append("⛰️ Steep terrain increases instability.")

if historical_events >= 5:
    reasons.append("📚 High historical landslide activity.")
elif historical_events >= 3:
    reasons.append("📚 Previous landslide activity exists.")

if elevation >= 2500:
    reasons.append("🏔️ High elevation terrain.")

if len(reasons) == 0:
    reasons.append(
        "Environmental conditions currently show relatively low risk."
    )

for reason in reasons:
    st.write("•", reason)

# =========================================================
# ML FEATURE IMPORTANCE
# =========================================================

st.divider()

st.header("🤖 AI Model Analysis")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=True
)

fig_importance = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Factors Influencing Landslide Prediction"
)

st.plotly_chart(
    fig_importance,
    use_container_width=True
)

# =========================================================
# GIS MAP
# =========================================================

st.divider()

st.header("🗺️ Northeast India Risk Map")

locations = pd.DataFrame({

    "Location": [
        "East Sikkim",
        "West Sikkim",
        "Tawang",
        "Aizawl",
        "Shillong",
        "Gangtok",
        "Darjeeling",
        "Itanagar",
        "Kohima",
        "Agartala"
    ],

    "Latitude": [
        27.33,
        27.29,
        27.58,
        23.73,
        25.58,
        27.34,
        27.04,
        27.08,
        25.67,
        23.83
    ],

    "Longitude": [
        88.61,
        88.12,
        91.86,
        92.72,
        91.89,
        88.61,
        88.26,
        93.60,
        94.11,
        91.28
    ],

    "Risk": [
        91,
        78,
        65,
        72,
        43,
        88,
        69,
        52,
        74,
        31
    ]
})

fig_map = px.scatter_map(
    locations,
    lat="Latitude",
    lon="Longitude",
    hover_name="Location",
    hover_data={
        "Risk": True,
        "Latitude": False,
        "Longitude": False
    },
    color="Risk",
    size="Risk",
    zoom=5,
    height=600,
    color_continuous_scale="RdYlGn_r"
)

fig_map.update_layout(
    map_style="open-street-map",
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# =========================================================
# HIGH RISK LOCATIONS
# =========================================================

st.header("🚨 High-Risk Locations")

high_risk = locations[
    locations["Risk"] >= 70
].sort_values(
    "Risk",
    ascending=False
)

st.dataframe(
    high_risk,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# RESPONSE PRIORITY
# =========================================================

st.header("🚑 Emergency Response Prioritisation")

priority_data = pd.DataFrame({

    "Location": [
        "East Sikkim",
        "Gangtok",
        "West Sikkim",
        "Kohima",
        "Aizawl",
        "Tawang"
    ],

    "Risk Score": [
        91,
        88,
        78,
        74,
        72,
        65
    ],

    "Priority": [
        "CRITICAL",
        "CRITICAL",
        "HIGH",
        "HIGH",
        "HIGH",
        "MEDIUM"
    ],

    "Recommended Action": [
        "Deploy emergency team",
        "Inspect vulnerable roads",
        "Prepare emergency response",
        "Monitor vulnerable slopes",
        "Increase monitoring",
        "Continuous monitoring"
    ]
})

st.dataframe(
    priority_data,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# FIELD REPORTING
# =========================================================

st.divider()

st.header("📍 Citizen / Field Officer Reporting")

with st.form("field_report"):

    report_location = st.selectbox(
        "Location",
        locations["Location"]
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Landslide",
            "Road Blockage",
            "Slope Crack",
            "Slope Movement",
            "Flooding",
            "Other"
        ]
    )

    description = st.text_area(
        "Description",
        placeholder="Describe the observed condition..."
    )

    uploaded_image = st.file_uploader(
        "Upload Photo",
        type=["jpg", "jpeg", "png"]
    )

    submitted = st.form_submit_button(
        "📤 Submit Report"
    )

    if submitted:

        st.success(
            f"Field report submitted successfully for {report_location}."
        )

        st.write(
            f"**Report Type:** {report_type}"
        )

        if description:
            st.write(
                f"**Description:** {description}"
            )

        if uploaded_image:

            st.image(
                uploaded_image,
                caption="Uploaded Field Evidence"
            )

# =========================================================
# ALERT GENERATION
# =========================================================

st.divider()

st.header("🔔 Alert System")

if risk_score >= 80:

    st.error(
        f"🚨 ALERT GENERATED\n\n"
        f"Location: {selected_location}\n\n"
        f"Risk: {risk_score}%\n\n"
        f"Severity: VERY HIGH"
    )

elif risk_score >= 60:

    st.warning(
        f"⚠️ WARNING GENERATED\n\n"
        f"Location: {selected_location}\n\n"
        f"Risk: {risk_score}%\n\n"
        f"Severity: HIGH"
    )

else:

    st.success(
        "No emergency alert required under current simulated conditions."
    )

# =========================================================
# SYSTEM INFORMATION
# =========================================================

st.divider()

with st.expander("ℹ️ About LANDGUARD AI"):

    st.write("""
    LANDGUARD AI is a prototype disaster-management platform
    designed for SIH26001.

    The system combines:

    • Machine Learning based risk prediction
    • Environmental condition analysis
    • GIS-based risk visualization
    • Emergency response prioritisation
    • Citizen and field-officer reporting
    • Automated warning generation

    The current prototype uses synthetic demonstration data.
    It can later be connected to real weather APIs, satellite
    imagery, sensor networks and historical landslide datasets.
    """)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "LANDGUARD AI | SIH26001 | AI-Based Landslide Risk Monitoring & Early Warning System"
)
