# ScrapeGenius.AI
ScrapeGenius.AI is a Python-powered AI web scraping tool that utilizes Streamlit for the user interface, Langchain for AI integration, and Selenium with a Chrome driver to handle automated browsing and web scraping. The project begins by setting up a virtual environment using Venv in VSCode, and dependencies are managed through a requirements text file.

The scraping logic resides in main.py, with genius.py dedicated to handling captchas and cleaning DOM content using Bright Data's scraping browser. In addition, Ollama, an LLM tool, is used in extract.py to parse and process the scraped data. Users can interact with the tool locally, launching the site via "source ScrapeGenius/bin/activate" to activate the virtual environment and "streamlit run main.py" to launch the website.

With ScrapeGenius.AI, users can scrape websites, process their DOM content, and leverage AI to extract and interpret information from any given URL.
