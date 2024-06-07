from typing import List

def read_file(file_path):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    li = []
    for line in lines:
            li.append(line)
    return li

print(read_file("File Handling and Data Processing/sample.txt"))

