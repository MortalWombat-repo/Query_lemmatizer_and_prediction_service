# .streamlit/postInstall.sh
#!/bin/bash
# Activate the virtual environment
source /home/adminuser/venv/bin/activat
# Install hr_core_news_md
python -m pip install https://github.com/explosion/spacy-models/releases/download/hr_core_news_md-3.8.0/hr_core_news_md-3.8.0-py3-none-any.whl
