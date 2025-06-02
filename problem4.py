import os
# choose the directory whose content you want to disply
path = '/'

entries = os.listdir(path)

print(f"Contents of '{path}':")
# avove command will displt the content of the directory
for entry in entries:
    print(entry)
