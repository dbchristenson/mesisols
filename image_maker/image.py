from PIL import Image
from image_maker import textures

def gen_image():

  open_bg = Image.open('simple_bg')
  open_ov = Image.open('simple_star')
  convert_bg = open_bg.convert("RGBA")
  convert_ov = open_ov.convert("RGBA")

  new_img = Image.blend(convert_bg, convert_ov, 0.5)

  new_img.save("new.png","PNG")