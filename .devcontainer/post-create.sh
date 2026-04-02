#!/bin/bash
set -e

echo "==> Installing system dependencies..."
sudo apt-get update -qq && sudo apt-get install -y --no-install-recommends graphviz

echo "==> Creating virtual environment..."
python3 -m venv .venv

echo "==> Installing dependencies..."
.venv/bin/pip install --upgrade pip --quiet
.venv/bin/pip install -e . --quiet

# Generate ubcode.toml from Codespaces Secrets (ENV vars) if available
echo "==> Configuring ubCode license..."
UBCODE_CONFIG_DIR="${HOME}/.config/ubcode"
UBCODE_CONFIG_FILE="${UBCODE_CONFIG_DIR}/ubcode.toml"

if [[ -n "${UBCODE_LICENSE_KEY}" && -n "${UBCODE_LICENSE_USER}" ]]; then
  mkdir -p "${UBCODE_CONFIG_DIR}"
  cat > "${UBCODE_CONFIG_FILE}" <<EOF
[license]
key = "${UBCODE_LICENSE_KEY}"
user = "${UBCODE_LICENSE_USER}"
EOF
  echo "    ubcode.toml written to ${UBCODE_CONFIG_FILE}"
else
  echo "    UBCODE_LICENSE_KEY or UBCODE_LICENSE_USER not set — skipping license config."
  echo "    Set them as Codespaces Secrets to enable the commercial ubCode license."
fi

echo "==> Setup complete. Run 'make html' to build docs, 'make test' to run tests."
