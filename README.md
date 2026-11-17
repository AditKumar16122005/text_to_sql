# Text to SQL Query Generator

A Streamlit-based web application that leverages Large Language Models to translate natural language questions into executable SQL queries. The application connects to a local SQLite database and displays the retrieved data directly in the UI.

## 📁 Project Structure

* `app.py`: The main Streamlit application file containing the frontend UI and user interaction logic.
* `sql.py`: The backend Python script handling database connections, query execution, and potentially the LLM prompting logic.
* `student.db`: A local SQLite database containing sample student data used for testing and running queries.
* `requirments.txt`: The list of Python dependencies required to run the project.

## 🛠️ Tech Stack & Dependencies

* [**Streamlit**](https://streamlit.io/)**:** For building the interactive web interface.
* [**Groq**](https://groq.com/)**:** (Inferred from `qroq`) For fast LLM inference to convert text prompts into SQL.
* [**python-dotenv**](https://pypi.org/project/python-dotenv/)**:** For securely managing environment variables like API keys.
* **SQLite:** The lightweight database engine used (`student.db`).

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed on your machine.

### Installation

1. **Clone the repository or extract the project files:**
   Navigate to the `text_to_sql-main` directory.

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirments.txt
   ```
   *(Note: Ensure your requirements file has the correct spellings, e.g., `groq` and `python-dotenv`)*

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys (e.g., Groq API key) if required by the application:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

### Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

This will launch a local server and open the application in your default web browser (usually at `http://localhost:8501`).

## 💡 Usage

1. Open the web interface.
2. Type a natural language question into the prompt box (e.g., *"How many students have a grade higher than 85?"*).
3. The LLM will process the text and generate a valid SQL query.
4. The application will execute the generated SQL query against `student.db` and display the results on the screen.
