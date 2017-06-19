file = "/Users/jacobian3/version-control/tabula_rasa/script_data/pyku.txt"

text = "we're certainly out of gouda but Python is great."

unique_items = set()

for item in open(file).read().split():
    item = item.lower()
    unique_items.add(item)

print(unique_items)
print

words = text.split()

for word in words:
    if word not in unique_items:
        print(word)

