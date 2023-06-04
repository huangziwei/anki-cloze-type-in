# An Anki deck for language learning with cloze type-in 

## About this deck

The code and data in this repo are designed to help myself learn German by typing in the answers. It is based on the [Cloze (fill-in-the-blank) type](https://apps.ankiweb.net/docs/manual.html#cloze-deletion) of [Anki](https://apps.ankiweb.net/) cards.

## Format of the Note

Each note in the Anki deck is designed to support language learning with the following fields:

1. Sentence: A sentence in the target language with the cloze deletion.
2. Rank: The rank of the word being learned.
3. Word: The target word to learn.
4. Definition: The definition of the word.
5. Translation: The translation of the sentence into the learner's first language.
6. Note: Any additional notes for the word and sentence (e.g., related grammar).
7. CEFR: The Common European Framework of Reference for Languages (CEFR) level of the word.

Check out the [raw data](./raw/german_10000_reverse.csv) for an example.

## Usage

First, preprocess the raw CSV file:

```shell
python ./raw/preprocess.py ./pre/input.csv
```

This will generate a new CSV file named "input_preproc.csv", where specified words in each sentence are wrapped with the cloze deletion syntax.

Next, generate the Anki deck:

```shell
python build_deck.py ./pre/input_preproc.csv
```

This will create an Anki deck named "input_preproc.apkg" in `decks/` that can be imported into Anki.

## Customization

You can personalize the appearance of your Anki cards by editing the HTML templates (`front.html` and `back.html`) and the CSS file (`style.css`).

## Data

I am working on a few decks for German language learning. The data sources are: 

1. Goethe Zertifikat Wortliste A1, A2, and B1;
1. [German Top 10000 Most Common Words](https://mostusedwords.com/products/4-german-frequency-dictionaries-set-top-10000-most-common-german-words). 
2. Goethe Z]