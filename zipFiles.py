from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", 'w') as zip:
#     for path in Path("packageCreation").rglob('*.*'):
#         zip.write(path)

with ZipFile("files.zip", 'r') as zip:
    print(zip.namelist())
    info = zip.getinfo("packageCreation/ecommerce/customer/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall('extract')