#!/bin/bash
set -e

echo "==> Creating virtual environment..."
python3 -m venv .venv

echo "==> Installing dependencies..."
.venv/bin/pip install --upgrade pip --quiet
.venv/bin/pip install -e . --quiet

echo "==> Setup complete. Run 'make html' to build docs, 'make test' to run tests."
