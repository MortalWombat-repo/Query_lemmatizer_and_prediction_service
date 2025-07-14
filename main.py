import pickle
import spacy
import string
import sys
from langdetect import detect, DetectorFactory, LangDetectException
DetectorFactory.seed = 0

def prediction(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if text == '':
        print("You did not enter anything.")
        sys.exit()

    try:
        lang = detect(text)

        if lang != "hr":
            print("The text does not appear to be in Croatian.")
            sys.exit()

    except LangDetectException as e:
        print("Could not detect language. Please revise your input.")
        print(f"Error: {e}")
        sys.exit()

    # translation table that maps punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    nlp = spacy.load("hr_core_news_md")

    def spacy_lemmatize_hr(text):
        doc = nlp(text)
        return " ".join([token.lemma_ for token in doc])

    # Load the model from the file
    with open('spacy_model.bin', 'rb') as f:
        model = pickle.load(f)


    lemmatized_text = spacy_lemmatize_hr(text)

    # Wrap the lemmatized text in a list, because it doesn't accept a string.
    lemmatized_input = [lemmatized_text]

    # Collect output for returning and then printing
    output = []

    proba = model.predict_proba(lemmatized_input)
    for input_text, probs in zip(lemmatized_input, proba):
        output.append(f"\nInput: {input_text}")
        for cls, prob in zip(model.classes_, probs):
            output.append(f"Class: {cls}, Probability: {prob:.4f}")

    predicted = model.predict(lemmatized_input)[0]
    output.append(f"\nPredicted class: {predicted}")

    return "\n".join(output)

def main():
    text = "Ne mogu se prijaviti na svoj račun."
    print(prediction(text))

if __name__ == "__main__":
    main()