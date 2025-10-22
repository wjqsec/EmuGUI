import json
import os
import services.pathfinder as pf
from pathlib import Path


def read_hw_plugin():
    exec_folder = pf.retrieveExecFolder()
    
    pluginContent = []
    pluginFiles = [f for f in os.listdir(f"{exec_folder}plugins/hw_additions") if os.path.isfile(os.path.join(f"{exec_folder}plugins/hw_additions", f))]

    for plugin in pluginFiles:
        with open(f"{exec_folder}plugins/hw_additions/{plugin}", "r+") as pluginFile:
            jsonplugin = json.load(pluginFile)
            pluginContent.append(jsonplugin)

    return pluginContent

def add_new_hw_plugin(arch: str, new_machine: str):
    if arch == "i386":
        arch = "x86"
    elif arch == "riscv":
        arch = "riscv32"
    exec_folder = pf.retrieveExecFolder()
    file_path = Path(f"{exec_folder}plugins/hw_additions/{arch}_default_additions.json")
    if not file_path.exists():
        print(f"File {file_path} does not exist")
        return False
    with open(file_path, "r") as f:
        data = json.load(f)    
    key = f"{arch}_machines"
    if key not in data:
        print("Key does not exist")
        return False           
    if new_machine in data[key]:
        print("Machine already exists")
        return False              
    data[key].append(new_machine)                    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return True

def insert_line_to_file(file_path: str, line_number: int, new_line: str):
    """
    Insert a line into a file at the given line number (1-based index).
    
    :param file_path: Path to the file
    :param line_number: Line number to insert at (1 = first line)
    :param new_line: The line content to insert (without newline)
    """
    print(f"Insert line into {file_path} at line {line_number}: {new_line}")
    # Read all lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Ensure newline at the end
    if not new_line.endswith('\n'):
        new_line += '\n'

    # Clamp line_number
    line_index = max(0, min(line_number - 1, len(lines)))

    # Insert new line
    lines.insert(line_index, new_line)

    # Write back
    with open(file_path, 'w') as f:
        f.writelines(lines)

def insert_line(content: str, line_number: int, new_line: str):
    """
    Insert a line into a file at the given line number (1-based index).
    
    :param file_path: Path to the file
    :param line_number: Line number to insert at (1 = first line)
    :param new_line: The line content to insert (without newline)
    """
    # Read all lines
    lines = content.splitlines(keepends=True)

    # Ensure newline at the end
    if not new_line.endswith('\n'):
        new_line += '\n'

    # Clamp line_number
    line_index = max(0, min(line_number - 1, len(lines)))

    # Insert new line
    lines.insert(line_index, new_line)
