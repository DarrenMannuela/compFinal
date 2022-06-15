from PIL import Image
from parser import Parser


parser = Parser()
parsed = parser.parse()
items = parsed['VariableDeclaration']
words = []
hl_ls = []
count = 1
image_length = 0

for i in items:
    for key, value in i.items():
        words.append(value)

for word in words:
    for char in word:
        image = Image.open(f'hl_symbols/{char}.png')
        hl_ls.append(image)
    image_space = Image.open(f'hl_symbols/space.png')
    hl_ls.append(image_space)

image_size = hl_ls[0].size
new_image = Image.new('RGB', (len(hl_ls)*image_size[0], image_size[1]), (250, 250, 250))

for hl in hl_ls:
    if count == 1:
        new_image.paste(hl, (0,0))
        new_image.save("output/translated.png", "PNG")
        count += 1
        image_length += image_size[0]
    elif count > 1:
        new_image.paste(hl, (image_length, 0))
        new_image.save("output/translated.png", "PNG")
        count += 1
        image_length += image_size[0]

new_image.show()