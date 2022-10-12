import json

# 3 functions: dump for writing, load for reading, update for update

my_dict = {
    'apples': 12,
    'bananas': 13,
    'oranges': 15
}

# Write json data
with open('file.json', mode='w') as f:
    json.dump(my_dict, f, indent=4)

# Read json data
with open('file.json', mode='r') as f:
    data = json.load(f)


# Update: 2 steps process

# step 1 read and update the existing json
with open('file.json', mode='r') as f:
    data = json.load(f)
    data.update(my_dict)

# write the updated json
with open('file.json', mode='w') as f:
    json.dump(data, f, indent=4)


