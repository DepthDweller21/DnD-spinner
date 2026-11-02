import json
from pathlib import Path


def read(fileName):
    BASE_DIR = Path(__file__).parent.parent.parent

    with open(BASE_DIR / "datatables" / f"{fileName}.json", "r") as file:
        data = json.load(file)
    
    return data

def write(fileName, new_data):
    BASE_DIR = Path(__file__).parent.parent.parent

    with open(BASE_DIR / "datatables" / f"{fileName}.json", "w") as file:
        json.dump(new_data, file, indent=4)
    
    return True


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
    # modify('smart','attribute',[])
    return


if __name__ == "__main__":
    main()