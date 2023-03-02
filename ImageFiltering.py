from PIL import Image, ImageFilter


image_file = "cholesterol project\\cholesterol drug screening in scc47\\drug treatment for 24 hours during invasion10_11_22\\A939572 _lower chamber treatment\\jpeg\\10uM-1.jpg"
im = Image.open(image_file)


size = im.size
data = list(im.getdata())
blur_im = im.filter(ImageFilter.UnsharpMask(radius=4)) # Gaussian/Unsharp filter

im.close()

blur_im.save("blur test.jpg")
