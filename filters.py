from PIL import Image, ImageFilter, ImageEnhance


orig = Image.open('GUI/img/cat.png')
orig.show()

W, H = orig.size
req_height = 150  # px
ratio = W / H


print('Формат: ', orig.format)
print('Цветовая схема: ', orig.mode)
print('Размер: ', W, 'x', H)


cat_1 = orig.resize((int(req_height * ratio), req_height))
cat_1.show()  # , cat_1.save('cat_1.png')

cat_2 = orig.crop((75, 25, 325, 250))
cat_2.show()  # , cat_2.save('cat_2.png')

pixels = orig.load()
for x in range(W):
    for y in range(H):
        r, g, b = pixels[x, y]
        pixels[x, y] = g, b, r
orig.show()  # , orig.save('cat_3.png')

for x in range(W):
    for y in range(H):
        r, g, b = pixels[x, y]
        averaged = (r + g + b) // 3
        pixels[x, y] = averaged, averaged, averaged
orig.show()  # , orig.save('cat_4.png')

for x in range(W // 2):
    for y in range(H):
        r, g, b = pixels[x, y]
        averaged = (r + g + b) // 3
        pixels[x, y], pixels[W - x - 1, y] = pixels[W - x - 1, y], pixels[x, y]
orig.show()  # , orig.save('cat_5.png')

orig = orig.convert('RGBA')
print(orig.mode)

cat_6 = orig.filter(ImageFilter.BLUR)
cat_6.show()  # , cat_6.save('cat_6.png')

cat_7 = orig.filter(ImageFilter.BoxBlur(7))
cat_7.show()  # , cat_7.save('cat_7.png')

cat_8 = orig.filter(ImageFilter.GaussianBlur(10))
cat_8.show()  # , cat_8.save('cat_8.png')

cat_9 = orig.filter(ImageFilter.CONTOUR)
cat_9.show()  # , cat_9.save('cat_9.png')

cat_10 = ImageEnhance.Sharpness(orig).enhance(10.0)
cat_10.show()  # , cat_10.save('cat_10.png')
