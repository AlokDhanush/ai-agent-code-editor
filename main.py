import os 
from dotenv import load_dotenv 
from google import genai
import sys
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_functions import call_function

def main():
    load_dotenv() 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)  

    if len(sys.argv) < 2:
        print("I need a prompt argument!")
        sys.exit(1)

    system_prompt = """
            You are a helpful AI coding agent.

            When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

            - List files and directories
            - Read file contents
            - Write or modify files
            - Run Python scripts with optional command line arguments

            When the user asks about the code project - they are referring to the files in the current working directory and its subdirectories.
            You should figure it out how to run the project and how to run its tests, you'll always to test the tests and actual project 
            to verify that eveything is working correctly.

            All paths you provide should be relative to the working directory. 
            You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """
    
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    prompt = sys.argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_python_file,
        schema_write_file
       ]
    )
    
    config=types.GenerateContentConfig(
        system_instruction=types.Content(role="system", parts=[types.Part(text=system_prompt)]),
        tools=[available_functions]
    )
    
    MAX_ITER = 20
    for i in range(MAX_ITER):
        response = client.models.generate_content(
            model=	"gemini-2.0-flash",
            contents=messages,
            config=config
        )

        if response is None and response.usage_metadata is None:
            print("No response or usage metadata received.")
            return
        
        if verbose_flag:
            print("Prompt:", prompt)
            print("Prompt tokens:", response.usage_metadata.prompt_token_count) 
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        
        if response.function_calls:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue 
                messages.append(candidate.content)
    
        if response.function_calls:
            for function_call_part in response.function_calls:
                result =  call_function(function_call_part, verbose=verbose_flag)
                messages.append(result)
        else:
            print(response.text) 
            return 


main() 