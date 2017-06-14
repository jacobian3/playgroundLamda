file = "/Users/jacobian3/version-control/tabula_rasa/script_data/pyku.txt"
unique_items = set()

for item in open(file).read().split():
    item = item.lower()
    unique_items.add(item)

print(unique_items)
