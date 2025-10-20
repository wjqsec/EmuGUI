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
    exec_folder = pf.retrieveExecFolder()
    file_path = Path(f"{exec_folder}/plugins/{arch}_default_additions.json")
    if not file_path.exists():
        return False
    with open(file_path, "r") as f:
        data = json.load(f)    
    key = f"{arch}_machines"
    if key not in data:
        return False           
    if new_machine in data[key]:
        return False              
    data[key].append(new_machine)                    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return True