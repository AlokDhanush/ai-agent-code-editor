import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path)) 

    if abs_file_path.startswith(abs_working_dir):
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f"File '{file_path}' written successfully." 
    else:
        return "Error: Attempt to write outside the working directory."
    


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or creates a new file with the specified content (and creates parent dirs safely), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file as string",
            ),
        },
    ),
)