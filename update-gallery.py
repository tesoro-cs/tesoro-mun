from bs4 import BeautifulSoup as bs4
import os

galleryFile = open("gallery/gallery.html", "r")
galleryFile = bs4(galleryFile, features="html.parser")

# i=1
# for img in range(1,10):
#     insert = galleryFile.find(id="insert")
#     newImgDiv = galleryFile.new_tag("div")
#     newImg = galleryFile.new_tag("img")
#     newImg["src"] = "imgs/"
#     newImgDiv.append(newImg)
#     newImgDiv["class"] = "slide"
#     newImgDiv["id"] = i
#     print(newImgDiv)
#     i+=1

directory = "./gallery/imgs/"
count = 0
files = []
for i, name in enumerate(os.listdir(directory)):
    extension = name.split(".")
    extension = "." + extension[len(extension)-1]
    filename = directory + str(i+1) + extension
    os.rename(directory + name, filename)
    count+=1
    files.append(filename)


# slides = galleryFile.find_all(class_="slide")
# insert = galleryFile.find(id="insert")
container = galleryFile.find(id="slidecontainer")
for i in range(1,count+1):
    newImgDiv = galleryFile.new_tag("div")
    newImgDiv["class"] = "slide"
    newImgDiv["id"] = i
    newImg = galleryFile.new_tag("img")
    newImg["src"] = "imgs/" + files[i-1]
    newImgDiv.append(newImg)
    # newImgDiv.contents = newImg
    # newImgDiv.insert_after(insert)
    print(newImgDiv)
    container.append(newImgDiv)
print(galleryFile)
file = open("gallery/gallery.html", "wb")
file.write(galleryFile.prettify("utf-8"))
file.close

# <div class="slide"><img src="imgs/logo.png"></div>

# ("gallery/gallery.html", "w")
# galleryFile = galleryFile.split("<!-- DO NOT REMOVE - USED FOR UPDATING IMAGES -->")
# galleryFile[1] = "<div class=\"slide\"><img src=\"imgs/\"></div>" + "\n<!-- DO NOT REMOVE - USED FOR UPDATING IMAGES -->\n" + galleryFile[1]
# print(galleryFile)

