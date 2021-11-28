###===--- Image Maker ---===###


###===--- Imports ---===###

# General #
from PIL import Image, ImageDraw, ImageFilter
from image_maker import textures

# Python Files #
from generator import utils
from generator.sol_gen import gen_sol


###===--- Image Generator Functions ---===###

def gen_image(star, code=0):
  '''
  This function generates the png file for one AlgoSol NFT.
  
  Inputs:
    star: class
  
  Returns: a png image that represents the star.
  '''

  # Link each visual attribute of the star to more readable
  # variables for navigating the images.
  background = star.position
  size, color = (star.size, star.color) # str, str
  sun_spots = star.sun_spots # str
  background = star.position  # str
  flares = star.solar_flares  # int
  p_type, p_num = star.local_system  # str, int

  # Convert the sizes to match the image.
  for dimension in utils.img_size_dict.items():
    img_key, val = dimension

    if size in val:
      img_size = img_key
  
  # Convert the planets to match the Image
  for planet_type in utils.img_p_dict.items():
    img_key, val = planet_type

    if size in val:
      sys_type = img_key

  # Assign new variables to each image using f strings to search for the file.
  bg = Image.open(f'image_maker/textures/backgrounds/{background}.png')
  base = Image.open(f'image_maker/textures/base/{img_size}/{color}.png')
  spots = Image.open(f'image_maker/textures/spots/{sun_spots}/{color}.png')

  # Planets/flares are a special case because we need to select multiple
  # images depending on the condition so create a variable for its directory.
  planet_dir = f'image_maker/textures/planets/{sys_type}'
  flare_dir = f'image_maker/textures/{color}/{flares}'

  bg.paste(base)


  # Save the completed image to the correct folder.
  img_path = 'image_maker/star_pngs'
  bg.save(f"{img_path}/algosol.png")


def gen_collection(n):
  '''
  This function generates the png files for a collection
  of n size of algosols.

  Inputs:
    n: int representing how many images to generate
  
  Returns:
    fills up the star_pngs folder with n amount of a star images.
  '''

  for star_idx in range(1, n + 1):
    star = gen_sol()

    gen_image(star, star_idx)