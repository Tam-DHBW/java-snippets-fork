import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)
print("JSON String:", json_string)

# Convert JSON string back to Python dictionary
python_dict = json.loads(json_string)
print("Python Dict:", python_dict)
