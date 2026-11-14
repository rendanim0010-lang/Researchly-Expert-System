import streamlit as st
import joblib

#trained model
model = joblib.load("research_abstract_classifier.pkl")

#page configuration
st.set_page_config(
    page_title="Researchly Research Abstract Classifier",
    page_icon="📚"
)

#app heading
st.title("📚 Researchly")
st.subheader("Research Paper Classifing System")

st.write(
    "Enter a research abstract below to classify it as: "
    "**AI** or **Classical** research."
)

# Abstract input
abstract = st.text_area(
    "Research Abstract",
    height=250,
    placeholder="Paste research abstract..."
)

# Prediction button
if st.button("Classify Abstract"):

    if not abstract.strip():
        st.warning("Enter a research abstract.")

    else:
        prediction = model.predict([abstract])[0]

        st.subheader("Prediction")

        if prediction == "ai":
            st.success("AI Research")
        else:
            st.info("Classical Research")

        st.write(
            f"Predicted category: **{prediction.upper()}**"
        )