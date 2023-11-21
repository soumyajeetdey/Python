# define a dictionary and display output in certain format

def display_nested_dict(data, prefix=''):
    for key, value in data.items():
        if isinstance(value, dict):
            display_nested_dict(value, f"{prefix}.{key}" if prefix else key)
        else:
            full_key = f"{prefix}.{key}" if prefix else key
            print(f"{full_key.lstrip('.'):15} : {value}")

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
