#!/bin/bash
# I created this script to automate the virtual environment setup: it checks if .venv exists, creates it if needed, 
# activates the environment, and installs dependencies from requirements.txt.

echo "Checking virtual environment..."

# Checking if .venv exists
if [ ! -d ".venv" ]; then
  echo ".venv not found. Creating..."
  python -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/Scripts/activate

if [ $? -eq 0 ]; then
    echo ".venv activated successfully!"
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "Failed to activate .venv"
fi