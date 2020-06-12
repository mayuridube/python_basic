import zipfile

with zipfile.ZipFile("./example.zip", 'r') as zip_ref:
    zip_ref.extractall("./")
