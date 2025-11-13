from pathlib import Path


root_dir = Path(".")
for dir in root_dir.iterdir():
    for context_file in dir.glob("000_context.jsonld"):
        with open(context_file,"r") as f:
            data = f.read()
        rename_data = data.replace("http://es-vocab.ipsl.fr","https://espri-mod.github.io/mip-cmor-tables")
        # print(rename_data)
        with open(context_file,"w") as f:
            f.write(rename_data)

