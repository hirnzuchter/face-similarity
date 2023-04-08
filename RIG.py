from requests import get
import os
from PIL import Image
import io
import random

'''
"RIG": Retrieve Images on Google
'''
def gimgs(query, quantity=1):
    '''
    "gimgs" may be interpreted as "get images" or "google images"
    returns a list whose first component is a list of site urls 
    and whose second component is the list of corresponding images
    (the ones that are shown by a google image search)
    The quantity argument is how many search results should appear,
    The query is the string that you want to search for.
    '''
    content = str(get(f'https://google.com/search?q={query}&tbm=isch').content)
    site_urls = []
    img_urls = []
    iterator = 0
    while content.find("<a href") != -1 and iterator < quantity:
        index = content.find("<a h")
        content = content[index:]
        index = content.find('"')
        content = content[index+1:]
        index = content.find('?')
        site_urls.append(content[7:index])
        index = content.find('src="')
        content = content[index:]
        index = content.find('"')
        content = content[index+1:]
        index = content.find('"')
        img_urls.append(content[:index])
        iterator += 1
    return [site_urls, img_urls]

def store(query, dir, quantity=1, store_keys=False, csv_path=None, value=None):
    '''
    This populates a folder "dir" with images from a search query.
    The number of images is the "quantity" argument,
    "store_keys" allows you to store the keys to the images in a csv
    file at "csv_path", and "value" is the value that serves as 
    an index to the keys in the csv file.
    '''
    imgs = gimgs(query, quantity)[1]
    iterator = 1
    try:
        if store_keys == True and value != None:
            with open(f"{csv_path}", "a") as f:
                f.write(f"{value},")
                f.close()
        for img in imgs:
            i = random.randint(0, 99999999)
            temp = get(img).content
            os.system(f"touch {dir}/{i}.jpg")
            temp = io.BytesIO(temp)
            temp = Image.open(temp)
            temp.save(f"{dir}/{i}.jpg")
            if store_keys == True:
                with open(f"{csv_path}", "a") as f:
                    if iterator < quantity:
                        f.write(f"{i},")
                    else:
                        f.write(f"{i}\n")
                    f.close()
            iterator += 1
    except:
        with open(f"{csv_path}", "r") as f:
            lines = f.readlines()
            f.close()
        with open(f"{csv_path}", "w") as f:
            f.writelines(lines[:-1])
            f.close()


def store_multiple(query_list, dir, quantity=1, store_keys=False, csv_path=None, value=None):
    '''
    This populates a folder "dir" with images from a search query.
    The number of images is the "quantity" argument,
    "store_keys" allows you to store the keys to the images in a csv
    file at "csv_path", and "value" is the value that serves as 
    an index to the keys in the csv file.
    '''
    imgs = []
    for query in query_list:
        imgs.append(gimgs(query, quantity)[1][0])
    iterator = 1
    try:
        if store_keys == True and value != None:
            with open(f"{csv_path}", "a") as f:
                f.write(f"{value},")
                f.close()
        for img in imgs:
            i = random.randint(0, 99999999)
            temp = get(img).content
            os.system(f"touch {dir}/{i}.jpg")
            temp = io.BytesIO(temp)
            temp = Image.open(temp)
            temp.save(f"{dir}/{i}.jpg")
            if store_keys == True:
                with open(f"{csv_path}", "a") as f:
                    if iterator < quantity*len(query_list):
                        f.write(f"{i},")
                    else:
                        f.write(f"{i}\n")
                    f.close()
            iterator += 1
    except:
        with open(f"{csv_path}", "r") as f:
            lines = f.readlines()
            f.close()
        with open(f"{csv_path}", "w") as f:
            f.writelines(lines[:-1])
            f.close()