import streamlit as st

st.set_page_config(page_title="Industrial Defect Inspection", layout="wide")
st.title("Industrial Defect Inspection")
st.info("Demo placeholder: connect a trained model to display an anomaly heatmap and ACCEPT/REJECT decision.")
uploaded = st.file_uploader("Upload a part image", type=["png", "jpg", "jpeg"])
if uploaded:
    st.image(uploaded, caption="Uploaded inspection image", use_container_width=True)
    st.warning("No model is connected yet. Add inference logic before using this for inspection.")
