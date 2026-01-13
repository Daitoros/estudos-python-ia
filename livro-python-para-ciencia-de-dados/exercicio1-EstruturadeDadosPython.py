
l = [
{
"name": "photo1.jpg",
"tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
},
{
"name": "photo2.jpg",
"tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
},
{
"name": "photo3.jpg",
"tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
},
{
"name": "photo4.jpg",
"tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
}
]

photo_groups = {}

for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        print(f"Intersecting photo {i} with photo {j}")

        intersection = l[i]['tags'].intersection(l[j]['tags'])
        if len(intersection) >= 1:
            photo_groups.setdefault("_".join(sorted(intersection)), [str(l[i]['name']),str(l[j]['name'])])
        intersection=0
print(photo_groups)