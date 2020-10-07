from PIL import Image
me = Image.open('me.png')
sea = Image.open('Sea.jpg')
campus =Image.open('campus.jpg')
sea.paste(me,(0,0),me)
sea.show()
