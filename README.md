# Learning-Langchain

This repository is a hands-on learning project focused on LangChain and modern LLM workflows. It includes examples for working with chat models, embeddings, prompt templates, structured outputs, and simple Streamlit-based demos.

## Overview

The project is organized around practical LangChain use cases rather than a single app. It demonstrates how to:

- connect to different LLM providers
- build prompt-driven chat experiences
- use local and hosted Hugging Face models
- generate embeddings and compare document similarity
- work with structured outputs and Pydantic/TypedDict schemas
- create lightweight UI demos with Streamlit

## Project Structure

```text
Learning-Langchain/
├── Models/
│   ├── 1.LLM/
│   │   └── demo.py
│   ├── 2.ChatBots/
│   │   ├── chatmodel_HF_local.py
│   │   ├── chatmodel_huggingFace.py
│   │   ├── chatmodel_OpenRouter.py
│   ├── 3.Embedding_Models/
│   │   ├── embed_local.py
│   │   ├── embedOpenRouterDocs.py
│   │   └── embedOpenRouterQuery.py
│   └── Document_Similarity_Application/
│       └── document_similarity.py
├── Output/
│   ├── demo_TypeDict.py
│   ├── demoPydantic.py
│   ├── dictOp.py
│   ├── jsonStructuredOp.py
│   └── pydanticOp.py
├── Prompts/
│   ├── chat_history.txt
│   ├── dynamic_prompts_ui.py
│   ├── messagePlaceholder.py
│   ├── prompt_generator.json
│   ├── prompt_generator.py
│   ├── static_prompts_ui.py
│   ├── using_Ext_prompt.py
│   └── chatBot/
│       ├── betterChatBot.py
│       ├── dynamicChat.py
│       ├── messagesContextChatbot.py
│       └── normal_context_chatbot.py
├── .devcontainer/
│   └── setup.sh
├── drf3.1.py
├── requirements.txt
├── test.py
├── README.md
└── .gitignore
```

## Included Examples

### Models

- LLM integration examples using OpenRouter and Hugging Face
- Chat model wrappers for local and remote inference
- Embedding generation for text and document retrieval

### Prompts

- static and dynamic prompt templates
- prompt generation utilities with JSON prompt files
- conversation history examples and chat UI demos

### Output Handling

- Pydantic structured output examples
- TypedDict-based data extraction
- JSON schema extraction patterns

### Document Similarity

- simple semantic similarity examples using embeddings and vector comparison

## Setup

### Option 1: Local virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Option 2: GitHub Codespaces / Dev Container

The repository includes a dev container setup that creates a Python 3.12 environment and installs dependencies automatically:

```bash
bash .devcontainer/setup.sh
```

This creates the `.venv312` environment and installs the packages listed in `requirements.txt`.

## Environment Variables

Several scripts call `load_dotenv()` and expect API keys or access tokens to be defined in a `.env` file.

Example:

```env
OPENROUTER_API_KEY=your_openrouter_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

If you are using a local Hugging Face model, the token may not be required depending on the model and environment.

## Running the Examples

Examples can be run directly with Python. For example:

```bash
python "Models/1.LLM/demo.py"
python "Models/2.ChatBots/chatmodel_huggingFace.py"
python "Output/pydanticOp.py"
```

Some prompt and UI demos use Streamlit:

```bash
streamlit run "Prompts/using_Ext_prompt.py"
```

## Dependencies

The project uses LangChain packages, model integrations, environment management, and supporting ML libraries from `requirements.txt`, including:

- `langchain`
- `langchain-core`
- `langchain-openai`
- `langchain-openrouter`
- `langchain-huggingface`
- `langchain-google-genai`
- `langchain-anthropic`
- `streamlit`
- `python-dotenv`
- `pydantic[email]`
- `transformers`
- `sentence-transformers`
- `numpy`
- `scikit-learn`

## Notes

- This project is intended for learning and experimentation, not for production deployment.
- Some examples connect to external providers, so internet access and valid credentials may be required.
- Local model examples may require more memory and disk space depending on the model you choose.
- The repository is best used as a practical reference set for learning LangChain concepts.

## License

This project does not currently include a separate license file. If you plan to reuse or distribute the code, confirm the intended licensing before doing so.
