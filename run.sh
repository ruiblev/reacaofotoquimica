#!/bin/bash

# Navigate to the directory containing this script
cd "$(dirname "$0")"

# Activate the virtual environment
source venv/bin/activate

# Run the Streamlit application
streamlit run app.py
