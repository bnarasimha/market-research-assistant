# Market Research Assistant

A Streamlit-based web application that provides a beautiful visualization of market research between Narsi (A new AI tool), GitHub Copilot, and Cursor.

## Features

- Interactive comparison table
- Filterable product views
- Downloadable CSV export
- Detailed category-wise comparison
- Responsive design

## Installation

1. Clone the repository:

``` bash
git clone https://github.com/bnarasimha/market-research-assistant.git
```


2. Install required packages:

``` bash
pip install -r requirements.txt
```

3. Set the environment variables:  

- Create an Agent in GenAI Platform and get the endpoint and key.  
- Copy .env.example file and create a .env file in the root directory.
- Add the following variables:

``` bash
GENAI_AGENT_ENDPOINT=<your-agent-endpoint>
GENAI_AGENT_KEY=<your-agent-key>
```


4. Run the application:

``` bash
streamlit run app.py
```


5. Open your browser and navigate to `http://localhost:8501`


## Project Structure

- `app.py`: Main Streamlit application file.
- `main.py`: The main logic for the market research assistant.
- `product_research.py`: The logic for the product research task.
- `competitor_research.py`: The logic for the competitor research task.
- `comparison_research.py`: The logic for the comparison research task.
- `requirements.txt`: List of dependencies.
- `README.md`: This file.
