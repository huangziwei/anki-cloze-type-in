import sys

import pandas as pd


# Function to apply the cloze wrap to each part of the Gloze field
def apply_cloze(sentence, gloze):
    parts = gloze.split()
    for part in parts:
        sentence = sentence.replace(part, "{{c1::" + part + "}}")
    return sentence


# Load the CSV file
df = pd.read_csv(sys.argv[1], sep=",", encoding="utf-8")

# Remove rows where Sentence is empty
df = df.dropna(subset=["Sentence"])

# Wrap the Gloze word with {{c1::}} in the Sentence field
df["Sentence"] = df.apply(
    lambda row: apply_cloze(row["Sentence"], row["Gloze"]),
    axis=1,
)

# Save the modified dataframe to a new CSV file
df.to_csv(sys.argv[2], index=False)
