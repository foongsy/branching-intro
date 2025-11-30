# branching-intro

One-pager website for Git beginners to understand branching strategy, including worktree and common strategies.

## Setup

This project uses `uv` for Python dependency management.

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installed

### Installation

```bash
# Install dependencies
uv sync

# Run the Streamlit app
uv run streamlit run app.py
```

## Project Structure

- `app.py` - Main Streamlit application
- `pyproject.toml` - Project configuration and dependencies
- `README.md` - Project documentation

## Dependencies

- `streamlit` - Web framework for creating the interactive guide
- `streamlit-mermaid` - Component for rendering Git branching diagrams
