
import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    
    counts = {}
    for row in reader:
        title = row["title"]
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1
def f(item):
    return item[1]            
for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(title, count, sep=" | ")   
        