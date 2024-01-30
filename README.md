# Create Cohere Connector [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/dcarpintero/create-cohere-connector/) [![PyPi](https://img.shields.io/pypi/v/create-cohere-connector)](https://pypi.org/project/create-cohere-connector/)

Generates a custom Cohere Connector with one command. [Cohere Connectors](https://docs.cohere.com/docs/connectors) enable to combine Cohere's large language models (LLMs), which power the [Chat API](https://docs.cohere.com/docs/cochat-beta), with up-to-date factual information. They enhance Cohere's retrieval augmented generation (RAG) offering, and can respond to user questions and prompts with substantive, grounded generations that contain citations to external public or private knowledge bases.

Note that this is an experimental project. If something doesn’t work, please [file an issue](https://github.com/dcarpintero/create-cohere-connector/issues/new).

## 🧮 What is included?

Your environment will have everything you need to quickly prototype and deploy a custom Cohere Connector:

- ``API service`` implementing the required ``search`` endpoint using [FastAPI](https://fastapi.tiangolo.com/) (support for [Flask](https://flask.palletsprojects.com/) is planned). 
- ``Bearer Token Authentication`` using the Authorization header in HTTP requests. 
- ``Pydantic models`` for data validation and serialization.
- ``Client class`` to retrieve data from a custom data source.
- ``Deploy script`` to register your connector with Cohere.

## 🚀 Quickstart

1. Install ``create-cohere-connector`` package:

It is highly recommended to install this package within a virtual environment:

```sh
py -m venv .venv
.venv\scripts\activate
```

```sh
python3 -m venv .venv
source .venv/bin/activate
```

and then, run the installation:

```sh
pip3 install create-cohere-connector --user
```

2. Bootstrap your project:

```sh
create-cohere-connector
```

or

```sh
python -m create_cohere_connector.cli
```

This will prompt for a project name:

```sh
Project name [myconnector]: hello-connector
Api framework [FastAPI]: FastAPI
Authentication [Bearer]: Bearer
Caching [None]: None
```

generate the initial project structure:

```
myconnector
├── README.md
├── deploy.py
├── Dockerfile
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── provider
    ├── __init__.py
    ├── app.py
    ├── client.py
    └── datamodels.py
```

and install dependencies:

```sh
✅ Project created successfully!
```

3. Set environment variables

You might rename ``.env_template`` to ``.env``, and complete it.

4. Span a shell within the virtual environment

```sh
poetry shell
```

5. Start API service

Inside the ``provider`` directory:

```sh
poetry shell
uvicorn app:app --reload
```

if you encounter any trouble in this step, you might need to run:

```sh
poetry install --no-root
```

6. Deploy Cohere Connector

```sh
python deploy.py
```

## 👩‍💻 Contributions

If you would like to contribute, here are some features that we are planning to add:

- Flask support
- Semantic caching
- OAuth 2.0
- Data models scaffolding

## ⚖️ License

Create Cohere Connector is open source software licensed as Apache 2.0. 