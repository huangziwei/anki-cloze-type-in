import sys

import genanki
import pandas as pd

# Load the modified CSV file
df = pd.read_csv(sys.argv[1], sep=",", encoding="utf-8")

# Replace NaN values with empty strings
df = df.fillna("")

# Read the HTML templates and CSS
with open("front.html", "r") as file:
    front_html = file.read()
with open("back.html", "r") as file:
    back_html = file.read()
with open("style.css", "r") as file:
    css = file.read()

name = sys.argv[1].split("/")[-1].split(".")[0]

# Define the Model
model = genanki.Model(
    1607392319,
    name,
    fields=[
        {"name": "Sentence"},
        {"name": "Rank"},
        {"name": "Word"},
        {"name": "Definition"},
        {"name": "Translation"},
        {"name": "Note"},
        {"name": "CEFR"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": front_html,
            "afmt": back_html,
        },
    ],
    css=css,
)

# Create a deck
deck = genanki.Deck(2059400110, name)

# Create a note for each row in df and add to the deck
for index, row in df.iterrows():
    note = genanki.Note(
        model=model,
        fields=[
            row["Sentence"],
            str(row["Rank"]),
            row["Word"],
            row["Definition"],
            row["Translation"],
            str(row["Note"]),
            row["CEFR"],
        ],
    )
    deck.add_note(note)

# Save the deck to a file
genanki.Package(deck).write_to_file(f"./decks/{name}.apkg")
