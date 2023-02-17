from pathlib import Path
from time import ctime

path = Path("")

files = [p for p in path.rglob("*.py")]

for file in files:
    print("{:<25}  {:>30} ".format(file.name, ctime(file.stat().st_ctime)))