import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: The specified file {file_path} is outside the working directory." 
    
    if not os.path.isfile(abs_file_path):
        return f"Error: The specified path {file_path} is not a file." 
    
    file_content = ""
    try:
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            file_content = file.read(MAX_CHARS)
            if len(file_content) >= MAX_CHARS:
                file_content += f"[File {file_path} truncated at 10000 chars]"
                
            return file_content
        
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"
    


schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, from the working directory.",
            ),
        },
    ),
)