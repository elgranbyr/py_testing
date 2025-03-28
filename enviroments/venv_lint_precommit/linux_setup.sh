#!/bin/bash

set -e


CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$( dirname ${CURR_DIR} )"
VENV_DIR="${REPO_ROOT}/../venv"

rm -rf ${VENV_DIR}

if [ ! -d ${VENV_DIR} ]; then
    echo "Creating virtual environment in ${VENV_DIR}"
    python3 -m venv ${VENV_DIR}
fi
echo "activating virtual environment in ${VENV_DIR}"

ACTIVATE_PATH="${VENV_DIR}/bin/activate"
echo "activating virtual environment: source ${ACTIVATE_PATH}"

source ${ACTIVATE_PATH}
pip install -e ".[dev,lint,test]"
pre-commit install
