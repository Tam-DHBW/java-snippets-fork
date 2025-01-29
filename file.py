# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello from Python!\n")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()

print(content)
