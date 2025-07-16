import re
import streamlit as st
from main import prediction
from lingua import Language, LanguageDetectorBuilder
languages = [Language.CROATIAN, Language.BOSNIAN, Language.SERBIAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

st.set_page_config(page_title="Query classifier", layout="wide")


def parse_prediction_output(result_str: str):
    """Extract input text, class->prob mapping, and predicted class from prediction() output."""
    # Input line
    m_in = re.search(r'^Input:\s*(.*)$', result_str, re.MULTILINE)
    input_text = m_in.group(1).strip() if m_in else ""

    # Class lines
    class_probs = {}
    for cls, prob in re.findall(r'^Class:\s*([^,]+),\s*Probability:\s*([0-9.]+)', result_str, re.MULTILINE):
        class_probs[cls.strip()] = float(prob)

    # Predicted class
    m_pred = re.search(r'^Predicted class:\s*(.*)$', result_str, re.MULTILINE)
    predicted_class = m_pred.group(1).strip() if m_pred else None

    return input_text, class_probs, predicted_class

def main():
    st.title("Query Classification Service")

    with st.sidebar:
        st.markdown("## About")
        st.markdown("#### This service classifies queries into predefined categories.")

    text = st.text_input(
        "Please enter a term to classify.",
        value="",
        max_chars=100,
        key="query",
    )

    if st.button("Run the service"):
        if not text.strip():
            st.warning("You did not enter anything.")
            return

        try:
            lang = detector.detect_language_of(text)
            st.write(f"The detected language is **{lang.name.capitalize()}**")
        except Exception as e:
            lang = None
            st.warning(f"Could not detect language. Error: {e}")

        allowed = {Language.CROATIAN, Language.SERBIAN, Language.BOSNIAN}
        if lang and lang not in allowed:
            st.warning(f"The text appears to be in {lang.name.capitalize()}, not Croatian, Serbian or Bosnian.")

        # prediction service
        result_str = prediction(text.lower())
        if not result_str:
            st.error("Prediction failed. Please try again.")
            return

        input_text, class_probs, predicted_cls = parse_prediction_output(result_str)

        # Display results
        st.markdown(f"**Input:** {input_text}")
        st.subheader("Class probabilities")
        st.json(class_probs)

        st.subheader("Predicted class")
        st.success(predicted_cls)

        st.write("— cijena_paketa:", class_probs.get("cijena_paketa", 0.0))
        st.write("— ostalo:", class_probs.get("ostalo", 0.0))
        st.write("— problem_prijave:", class_probs.get("problem_prijave", 0.0))
        st.write("— reset_lozinke:", class_probs.get("reset_lozinke", 0.0))


if __name__ == "__main__":
    main()
