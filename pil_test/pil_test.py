from PIL import Image,ImageFilter

# im =Image.open('../huaji.jpg')
# w,h=im.size
# print(w,h)
# im.thumbnail((w/2,h/2))
# im.save('test.jpg','jpeg')

im=Image.open('test.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')