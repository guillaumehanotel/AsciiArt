from PIL import Image
import os
import sys


def get_char_from_rgb(character_ramp, value):
    threshold = 255 / len(character_ramp)
    index = int(round(value / threshold, 0))
    return character_ramp[index - 1]


# Conversion de l'image originale en image en niveau de gris
def convert_img_to_grayscale(image_path, maxsize):
    img = Image.open(image_path).convert('LA')
    img.thumbnail(maxsize, Image.ANTIALIAS)
    grey_image_path = image_path.split('.')[0] + '_grey.png'
    img.save(grey_image_path)
    return grey_image_path


def draw_image_to_file(image_path, character_ramp):
    rgb_img = Image.open(image_path).convert('RGB')
    width, height = rgb_img.size
    file = open(image_path.split('.')[0] + ".txt", "w")
    for x in range(1, height):
        for y in range(1, width):
            r, g, b = rgb_img.getpixel((y, x))
            file.write(get_char_from_rgb(character_ramp, r))
        file.write("\n")
    file.close()
    os.remove(image_path)


def parse_argument(args):
    if len(args) == 1:
        print("Should pass image file as argument")
        sys.exit()
    else:
        arg = args[1]
        if arg.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
            print("The file is not an image")
            sys.exit()
        else:
            return arg


def main():
    image_path = parse_argument(sys.argv)
    maxsize = (350, 350)

    long_char_ramp = True
    long_character_ramp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    short_character_ramp = " .:-=+*#%@"
    character_ramp = long_character_ramp if long_char_ramp else short_character_ramp

    grey_image_path = convert_img_to_grayscale(image_path, maxsize)
    draw_image_to_file(grey_image_path, character_ramp)


if __name__ == "__main__":
    main()
