### AI Code Review Agent

An intelligent, autonomous Code Review Agent built with OpenAI, PyGithub, ChromaDB, and Hindsight. The agent automates pull request reviews on GitHub, learns team coding preferences over time, remembers previous feedback to avoid repetitive suggestions, and logs analytical traces to Hindsight. 

### Key Features

* **Automated PR Reviews:** Integrates with GitHub to inspect pull request diffs and generate structured code reviews.
* **Persistent Team Memory:** Uses ChromaDB vector storage to learn architectural preferences, guidelines, and team corrections.
* **Anti-Repetition Engine:** Remembers past review comments and developer feedback to ensure it never repeats disputed or unwanted suggestions.
* **Hindsight Integration:** Tracks agent decisions, prompts, and outputs for observability, evaluation, and fine-tuning.
* **CLI and Webhook Ready:** Can be executed manually via command line or triggered automatically inside GitHub Actions workflows.

### Repository Structure

text

code_review_agent/
├── .env                  # API keys and environment configuration
├── .gitignore            # Ignored files (venvs, keys, vector db)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── config.py             # Configuration loader
├── main.py               # Entrypoint script for PR reviews & feedback ingestion
└── src/
    ├── __init__.py       # Package marker
    ├── github_client.py  # GitHub API interface
    ├── agent.py          # OpenAI LLM review logic
    ├── memory.py         # Vector memory (ChromaDB) for team rules
    └── hindsight_logger.py # Hindsight observability integration

Use code with caution.

### Requirements and Dependencies

* Python 3.10+
* OpenAI API Key (gpt-4-turbo access recommended)
* GitHub Personal Access Token (PAT) with repo scope
* Hindsight API Key (Optional for observability)

### Quick Start

### 1. Installation

Clone the repository and set up a virtual environment: 

bash

git clone https://github.com/your-org/code-review-agent.git
cd code-review-agent

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Use code with caution.

### 2. Environment Configuration

Create a .env file in the root directory: 

env

GITHUB_TOKEN=ghp_your_personal_access_token
OPENAI_API_KEY=sk-your_openai_api_key
HINDSIGHT_API_KEY=your_hindsight_api_key
CHROMA_DB_DIR=./chroma_data

Use code with caution.

### Usage

### Reviewing a Pull Request

Run the script by supplying the GitHub target repository (owner/repo) and the Pull Request number: 

bash

python main.py --repo "octocat/Hello-World" --pr 42

Use code with caution.

### Ingesting Team Feedback and Standards

To train the agent on team preferences or correct a previous review, pass the --feedback argument: 

bash

python main.py --repo "octocat/Hello-World" --pr 42 --feedback "We use pydantic models instead of dataclasses across this repository."

Use code with caution.

### Continuous Learning Workflow

1. **Review Execution:** When triggered, the agent pulls the PR code diff.
2. **Context Querying:** The agent searches ChromaDB for similar code patterns and past team corrections.
3. **Prompt Injection:** Team standards are dynamically injected into the OpenAI system prompt.
4. **Review Posting:** The generated review is posted to the GitHub PR comment thread.
5. **Observability Log:** Execution parameters and output traces are pushed to Hindsight.

### License

Distributed under the MIT License.
