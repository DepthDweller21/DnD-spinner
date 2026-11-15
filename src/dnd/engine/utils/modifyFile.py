import json
from pathlib import Path


def read(fileName,path=False):
    BASE_DIR = Path(__file__).parent.parent.parent

    if path == False:
        with open(BASE_DIR / "datatables" / f"{fileName}.json", "r") as file:
            data = json.load(file)
    else:
        with open(BASE_DIR / f"{fileName}", "r") as file:
            data = json.load(file)
    
    return data

def write(fileName, new_data,path=False):
    BASE_DIR = Path(__file__).parent.parent.parent

    if path == False:
        with open(BASE_DIR / "datatables" / f"{fileName}.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open(BASE_DIR / f"{fileName}", "w") as file:
            json.dump(new_data, file, indent=4)
    
    return True

def copyFile(source:str,destination:str):
    data = read(source,True)
    write(destination,data,True)


def add_property(fileName, key, value):
    existing_data = read(fileName)
    for item in existing_data:
        item[key]=value
    write(fileName, existing_data)
    return True

def delete_property(fileName, key):
    existing_data = read(fileName)
    for item in existing_data:
        del item[key]
    write(fileName, existing_data)
    return True


def main():
    # add_property('fight','attribute',[])
    return


if __name__ == "__main__":
    main()