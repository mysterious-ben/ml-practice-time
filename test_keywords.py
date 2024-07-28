import keybert
import pytextrank  # noqa: F401
import spacy
import spacy.cli
import spacy.displacy
import spacy.tokens
# import spacy_transformers  # noqa: F401
from loguru import logger


def load_spacy_model(spacy_model_name: str):
    try:
        spacy_nlp = spacy.load(spacy_model_name)
        logger.debug(
            f"loaded spacy model name='{spacy_model_name}' path='{spacy_nlp.path}'"
        )
    except Exception as e:
        logger.debug(str(e))
        spacy.cli.download(spacy_model_name)
        logger.debug(f"downloaded spacy model from web name='{spacy_model_name}'")
        spacy_nlp = spacy.load(spacy_model_name)
        logger.debug(
            f"loaded spacy model name='{spacy_model_name}' path='{spacy_nlp.path}'"
        )


if __name__ == "__main__":
    load_spacy_model("en_core_web_sm")
    load_spacy_model("en_core_web_md")
    load_spacy_model("en_core_web_lg")
    # load_spacy_model("en_core_web_trf")

    text = "Apple is looking at buying U.K. startup for $1 billion. The stock price reaches the new record high $2. Elon Musk raised concerns."

    # Spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ents = list(doc.ents)
    print(ents)
    assert len(ents) > 1
    print("Spacy works fine!")

    # Spacy + Transformers
    # nlp = spacy.load("en_core_web_trf")
    # doc = nlp(text)
    # ents = list(doc.ents)
    # print(ents)
    # assert len(ents) > 1
    # print("Spacy + Transformers works fine!")

    # Spacy + TextRank
    nlp.add_pipe("textrank")
    doc = nlp(text)
    phrases = [phrase.text for phrase in doc._.phrases[:10]]
    print(phrases)
    assert len(phrases) > 1
    print("Spacy + TextRank works fine!")

    # KeyBERT
    kw_model = keybert.KeyBERT()
    keywords = kw_model.extract_keywords(text)
    print(keywords)
    assert len(keywords) > 1
    print("KeyBERT works fine!")
