# write a program to display output from a dictionary

def display_nested_dict(data, parent_key=''):
    for key, value in data.items():
        if isinstance(value, dict):
            display_nested_dict(value, f"{parent_key}.{key}" if parent_key else key)
        else:
            full_key = f"{parent_key}.{key}" if parent_key else key
            print(f"{full_key.lstrip('.')} : {value}")

data = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "image": {
        "url": "images/0001.jpg",
        "width": 200,
        "height": 200
    },
    "thumbnail": {
        "url": "images/thumbnails/0001.jpg",
        "width": 32,
        "height": 32
    }
}

display_nested_dict(data)