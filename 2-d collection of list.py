fruits =       ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
flowers =      ["rose", "tulip", "daisy"]


groceries = [fruits, vegetables, flowers]

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()