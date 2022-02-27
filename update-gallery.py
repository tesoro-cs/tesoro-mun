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
for i, name in enumerate(os.listdir(directory)):
    extension = name.split(".")
    extension = "." + extension[len(extension)-1]
    os.rename(directory + name, directory + str(i) + extension)


# <div class="slide"><img src="imgs/logo.png"></div>

# ("gallery/gallery.html", "w")
# galleryFile = galleryFile.split("<!-- DO NOT REMOVE - USED FOR UPDATING IMAGES -->")
# galleryFile[1] = "<div class=\"slide\"><img src=\"imgs/\"></div>" + "\n<!-- DO NOT REMOVE - USED FOR UPDATING IMAGES -->\n" + galleryFile[1]
# print(galleryFile)

