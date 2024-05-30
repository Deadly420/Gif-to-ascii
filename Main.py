from PIL import Image, ImageSequence
import os
import time

gif_path = ""
gif_image = Image.open(gif_path)
new_width = 80
new_height = 30

def rgb_to_ansi(r, g, b):
    return "\033[38;2;{};{};{}m".format(r, g, b)

def pixel_to_ascii(r, g, b):
    brightness = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    ascii_chars = '@%#*+=-:. '
    ascii_index = int(brightness * (len(ascii_chars) - 1))
    return ascii_chars[ascii_index]

for frame in ImageSequence.Iterator(gif_image):
    frame = frame.resize((new_width, new_height))
    frame = frame.convert("RGB")

    ascii_frame = ""
    for y in range(frame.height):
        for x in range(frame.width):
            r, g, b = frame.getpixel((x, y))
            ascii_char = pixel_to_ascii(r, g, b)
            ascii_color = rgb_to_ansi(r, g, b)
            ascii_frame += ascii_color + ascii_char
        ascii_frame += "\033[0m\n"

    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_frame)

    time.sleep(0.1)
