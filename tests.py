# from functions.get_files_info import get_files_info 
# from functions.get_files_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator" 
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorems ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(run_python_file(working_directory, "main.py", ["5 + 10"]))
    # print(run_python_file(working_directory, "nonexistent.py"))

main() 