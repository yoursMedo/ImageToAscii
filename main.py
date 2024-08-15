from PIL import Image
at_file_path = "/Users/adit/Desktop/Scrap/Dreams/MakeASCII/Hero.png"

screen = Image.open(
    at_file_path
)

# Grey Image 
grayscreen = screen.convert("L")

# Converting image to smaller size 
new_width = 50
width,height = screen.size
aspect_ratio = height / width 

new_height = int(
    aspect_ratio * new_width * 0.8
)

resized_screen = grayscreen.resize(
    (
        new_width,
        new_height
    )
)

# Define the ASCII characters
ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

#  Convert to ascii
def pixel_to_ascii(image: Image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str



ascii_str = pixel_to_ascii(resized_screen)

ascii_str_len = len(ascii_str)
ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, ascii_str_len, new_width)])

print(ascii_img)















