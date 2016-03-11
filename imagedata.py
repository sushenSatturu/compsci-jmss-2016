from PIL import Image
from PIL.ExifTags import TAGS
 
def get_exif(fn):
    ret = {}
    pic = Image.open(fn)
    info = pic._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag)
        ret[decoded] = value
    return ret

tags = get_exif("/Users/lindam/Pictures/fungus.JPG")

for tag in tags:
    print (tag)

print (tags["GPSInfo"])

