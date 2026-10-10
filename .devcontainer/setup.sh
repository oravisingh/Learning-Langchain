
#!/usr/bin/env bash
set -euo pipefail

# Always run from the repository root
cd "$(dirname "$0")/.."

# Install uv if it is not already available
if ! command -v uv >/dev/null 2>&1; then
    if [ ! -x "$HOME/.local/bin/uv" ]; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
    fi
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create the Python 3.12 environment and install dependencies
if [ ! -x .venv312/bin/python ]; then
    uv venv --python 3.12 .venv312
fi
uv pip install --python .venv312/bin/python -r requirements.txt

echo "Environment setup complete!"
