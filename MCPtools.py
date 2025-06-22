
from pathlib import Path
import os
import platform
import psutil
import subprocess
import json
# MCPtools.py
base_dir = Path("./test")

def read_file(name: str) -> str:
    """Return file content. If not exist, return error message.
    """
    print(f"(read_file {name})")
    try:
        with open(base_dir / name, "r") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"An error occurred: {e}"

def list_files() -> list[str]:
    print("(list_file)")
    file_list = []
    for item in base_dir.rglob("*"):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list

def rename_file(name: str, new_name: str) -> str:
    print(f"(rename_file {name} -> {new_name})")
    try:
        new_path = base_dir / new_name
        if not str(new_path).startswith(str(base_dir)):
            return "Error: new_name is outside base_dir."

        os.makedirs(new_path.parent, exist_ok=True)
        os.rename(base_dir / name, new_path)
        return f"File '{name}' successfully renamed to '{new_name}'."
    except Exception as e:
        return f"An error occurred: {e}"
    
def get_host_info() -> str:
    """get host information
    Returns:
        str: the host information in JSON string
    """
    info: dict[str, str] = {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "memory_gb": str(round(psutil.virtual_memory().total / (1024**3), 2)),
    }

    cpu_count = psutil.cpu_count(logical=True)
    if cpu_count is None:
        info["cpu_count"] = "-1"
    else:
        info["cpu_count"] = str(cpu_count)
    
    try:
        cpu_model = subprocess.check_output(
            ["sysctl", "-n", "machdep.cpu.brand_string"]
        ).decode().strip()
        info["cpu_model"] = cpu_model
    except Exception:
        info["cpu_model"] = "Unknown"

    return json.dumps(info, indent=4)

if __name__ == "__main__":
    # This will print the JSON-formatted host info when you run:
    #   python MCPtools.py
    print(get_host_info())
