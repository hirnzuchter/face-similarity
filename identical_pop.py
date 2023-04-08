#Populate Directory with Similars(identical)
#Copy into a notebook cell

with open("celebrities.txt", "r") as f:
    lines = f.readlines()
    f.close()
with open("celebrities.txt", "w") as f:
    random.shuffle(lines)
    f.writelines(lines)
    f.close()

with open("celebrities.txt") as f:
    celebs = f.readlines()
    f.close()

num_identicals = 200
for celeb in celebs[:num_identicals]:
    RIG.store_multiple(query_list=[celeb, celeb], dir="similars", quantity=1, store_keys=True, csv_path="references.csv", value=0)