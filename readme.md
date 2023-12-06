# Embedded GPT

An AI model built on [Codellama](https://ollama.ai/thatguyjamal/codellama) to be a code assistant. The goal
is to build a tool where you can embed data into the AI and then use it to generate code based on any code software
you want. For example, if you want to learn how to use a new code library but the AI is not trained on it, you can
embed the library into the AI and then use it to get useful prompts.

## How to use

```bash
python3 -m venv embedded-gpt-env
source embedded-gpt-env/bin/activate.fish
pip install -r requirements.txt
```

Then run the following command:

```bash
python3 main.py
```

You will see a CLI prompt with instructions on how to use the AI.

## Notes

Im still new to python, so this code might be a bit messy. I will try to improve it in the future.

Also im learning about embedding and AI, this is just my process of learning. Right now the code only
works if you `ingest` the data first, then you can `prompt` it. I will try to make it work without
having to ingest the data first as it should just lookup the data on the database. However, im using
many tools ive never used before so I need to learn how to do that first.

*I will provide more information on how to use this in the future.*

## Todo
- [ ] Add support for pre-parse cleaning

Right now, everything in the html is embedded into the model. This is not ideal as there may be data
we don't need, so we should clean the data before embedding it into the model.

- [ ] Add support for full website embedding

right now the model only supports embedding web pages one url at a time. Ideally, I would want an
optional system where it will parse the website and for each anchor tag, it will fetch that pages content 
and embed it into the model. This will allow you to embed a full website into the model.

- [ ] Add support for different ollama models to be used.
- [ ] Test better params for web parsing in the `RecursiveCharacterTextSplitter` class.
- [ ] Better CLI UI/UX