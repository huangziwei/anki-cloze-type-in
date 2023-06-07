import sys

import genanki
import pandas as pd

# Load the modified CSV file
df = pd.read_csv(sys.argv[1], sep=",", encoding="utf-8")

# Replace NaN values with empty strings
df = df.fillna("")
df = df.sort_values(by=["Rank"])

# Read the HTML templates and CSS
with open("templates/front.html", "r") as file:
    front_html = file.read()
with open("templates/back.html", "r") as file:
    back_html = file.read()
with open("templates/style.css", "r") as file:
    css = file.read()

if sys.argv[2]:
    deck_name = sys.argv[2]
else:
    deck_name = sys.argv[1].split("/")[-1].split(".")[0]

note_type = "Cloze Type-In"

# Define the Model
model = genanki.Model(
    1550428389,
    name=note_type,
    fields=[
        {"name": "Sentence"},
        {"name": "Rank"},
        {"name": "Word"},
        {"name": "POS"},
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
    model_type=genanki.Model.CLOZE,
)

# Create a deck
deck = genanki.Deck(2059400110, deck_name)

# Create a note for each row in df and add to the deck
for index, row in df.iterrows():
    note = genanki.Note(
        model=model,
        fields=[
            row["Sentence"],
            str(row["Rank"]),
            row["Word"],
            row["POS"],
            row["Definition"],
            row["Translation"],
            str(row["Note"]),
            row["CEFR"],
        ],
    )
    deck.add_note(note)

# Save the deck to a file
genanki.Package(deck).write_to_file(f"./decks/{deck_name}.apkg")
