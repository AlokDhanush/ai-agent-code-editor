## Overview
This project runs an AI agent that can call local functions (under functions/),execute Python files, and respond to queries. The repository contains a dispatcher (call_functions.py) and a main entry (main.py) to run the agent. In the above project the calculator directory is where the agent actually works on (read, write, edit or delete). 
<br>

## How to run the project?
Step 1: Run the below command in the terminal.<br>
  ```
  git clone https://github.com/AlokDhanush/ai-agent-code-editor.git
  ```

Step 2: Install 'uv' package by running the below command.<br>
  ```
  pip install uv
  ```

Step 3: Create a virtual environment <br>
  ```
  uv venv
  ```

Step 4: Activate your enviroment in the same directory.<br> 
  ```
  .\.venv\Scripts\activate
  ```

Step 5: Add dependencies to the project. <br>
  ```
  uv add google-genai==1.12.1
  uv add python-dotenv==1.1.0
  ```

Step 6: Generate an API key from [Gemini API Key](https://aistudio.google.com/apikey) and create a '.env' file in the working directory and paste your generated api key. <br>
  ```python
  GEMINI_API_KEY = your_api_key
  ```

Step 7: Run the file using the below command without verbose. Replace your query in the quotes. <br>
  ``` 
  uv run main.py "your query about the calculator directory"  
  ```

(OR) with verbose to see more detailed output of token counts. <br>
  
  ```
  uv run main.py "your query about the calculator directory" --verbose
  ```















