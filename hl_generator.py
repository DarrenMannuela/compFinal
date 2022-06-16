from PIL import Image


class HumanLanguageGenerator:

    def __init__(self, parsed):
        self.parsed = parsed
        self.words = []
        self.hl_ls = []
        self.count = 1
        self.image_length = 0

    def generate_hl(self):
        items = self.parsed['VariableDeclaration']

        for dict in items:
            for key, value in dict.items():
                self.words.append(value)

        for word in self.words:
            for char in word:
                image = Image.open(f'hl_symbols/{char}.png')
                self.hl_ls.append(image)
            image_space = Image.open(f'hl_symbols/space.png')
            self.hl_ls.append(image_space)

        image_size = self.hl_ls[0].size
        new_image = Image.new('RGB', (len(self.hl_ls)*image_size[0], image_size[1]), (250, 250, 250))

        for hl in self.hl_ls:
            if self.count == 1:
                new_image.paste(hl, (0,0))
                new_image.save("output/translated.png", "PNG")
                self.count += 1
                self.image_length += image_size[0]
            elif self.count > 1:
                new_image.paste(hl, (self.image_length, 0))
                new_image.save("output/translated.png", "PNG")
                self.count += 1
                self.image_length += image_size[0]

        new_image.show()