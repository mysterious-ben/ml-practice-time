# ml-practice-time
Code snippets and tasks for ML workshops

## Installation

1. Clone the repository: `git clone git@github.com:mysterious-ben/ml-practice-time.git`
2. Install poetry: see https://python-poetry.org/docs/
3. Install dependencies: (in the project folder) `poetry install`

Plan B. If poetry doesn't work, create a virtual environment and install the dependencies using `pip install -r requirements.txt`.

### Test Installation

Run...
- `poetry run python test_keywords.py`
- `poetry run python test_chatbots.py`

**Warning:** `spacy-transformers` (used for the model `"en_core_web_trf"`) and `keybert` may cause dependency conflicts related to `torch` libraries. If this happen, disable these libraries or google for a solution.

## Project Struccture

- `keywords/` - entity and keyword extraction from text
- `chatbots/` - chatbot examples

Files named `answers_...` contain solutions to the tasks.
