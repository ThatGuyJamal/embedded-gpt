# Surreal DB Documentation AI

I embedded this AI on the [Surreal DB](https://surrealdb.com) documentation. This assumes you have a working
[Ollama](https://ollama.ai) environment running and `codellama:7b` installed with ollama.

## How to use

```bash
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
works if you `ingest` the data first, then you can `query` it. I will try to make it work without
having to ingest the data first as it should just lookup the data on the database. However, im using
many tools ive never used before so I need to learn how to do that first.