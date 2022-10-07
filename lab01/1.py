from PIL import Image
img = Image.open('pink-panther.jpg')
pixels = img.load()
new_img = Image.new(img.mode, img.size)
pixels_new = new_img.load()
for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
        r, b, g = pixels[i,j]
        avg = int(round((r + b + g) / 3))
        pixels_new[i,j] = (avg, avg, avg, 0)
print(new_img.size)
display(new_img) #run in colab
#new_img.show() - run in visual