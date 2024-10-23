import json

def json_extract(file_path):
    with open(file_path, "r") as f:
        json_object = json.load(f)
        titles = []
        contents = []

        # Loop through the sections
        for section in json_object["sections"]:
            titles.append(section["title"])
            contents.append(section["content"])

        return titles, contents
