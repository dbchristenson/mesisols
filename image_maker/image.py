from PIL import Image
from image_maker import textures

bg = Image.open("image_maker/textures/simple_bg.png")
ov = Image.open("image_maker/textures/simple_star.png")

def gen_image(bg, ov):

  convert_bg = bg.convert("RGBA")
  convert_ov = ov.convert("RGBA")

  new_img = Image.blend(convert_bg, convert_ov, 0.5)

  new_img.save("new.png","PNG")