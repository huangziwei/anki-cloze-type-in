import sys

import pandas as pd
import spacy

# Load the German model for Spacy
nlp = spacy.load("de_core_news_lg")


# Read the CSV file
df = pd.read_csv(sys.argv[1])

# Process each row of the DataFrame
for idx, row in df.iterrows():
    # Process the sentence with Spacy
    print(idx, row["Sentence"], row["Cloze"])
    doc = nlp(row["Sentence"])

    # Find the word that matches the cloze
    for token in doc:
        if token.text == row["Cloze"]:
            # Get the POS and update the DataFrame
            if token.pos_ == "NOUN":
                # Determine the gender based on the article
                if row["Word"].startswith("der "):
                    df.loc[idx, "POS"] = "n. M."
                elif row["Word"].startswith("das "):
                    df.loc[idx, "POS"] = "n. N."
                elif row["Word"].startswith("die "):
                    df.loc[idx, "POS"] = "n. F."
                elif token.morph.get("Number")[0] == "Plur":
                    df.loc[idx, "POS"] = "n. Pl."
                else:
                    df.loc[idx, "POS"] = "n."
            elif token.pos_ == "ADP":
                df.loc[idx, "POS"] = "prep."
            elif token.pos_ == "ADJ":
                df.loc[idx, "POS"] = "adj."
            elif token.pos_ == "ADV":
                df.loc[idx, "POS"] = "adv."
            elif token.pos_ == "CONJ":
                df.loc[idx, "POS"] = "conj."
            elif token.pos_ == "VERB":
                df.loc[idx, "POS"] = "v."
            elif token.pos_ == "PRON":
                df.loc[idx, "POS"] = "pron."
            elif token.pos_ == "DET":
                df.loc[idx, "POS"] = "det."
            elif token.pos_ == "PROPN":
                df.loc[idx, "POS"] = "n. prop."
            elif token.pos_ == "NUM":
                df.loc[idx, "POS"] = "num."
            elif token.pos_ == "AUX":
                df.loc[idx, "POS"] = "aux."
            elif token.pos_ == "SCONJ":
                df.loc[idx, "POS"] = "conj."
            elif token.pos_ == "INTJ":
                df.loc[idx, "POS"] = "intj."
            elif token.pos_ == "PART":
                df.loc[idx, "POS"] = "part."
            break

# Save the updated DataFrame back to the CSV file
df.to_csv(sys.argv[1], index=False)
