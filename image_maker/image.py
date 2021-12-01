###===--- Image Maker ---===###


###===--- Imports ---===###

# General #
from PIL import Image, ImageDraw, ImageFilter
from image_maker import textures
import random, os

# Python Files #
from generator import utils
from generator.sol_gen import gen_sol

# bg = Image.open('image_maker/textures/backgrounds/Rogue/rogue1.png')
# base = Image.open('image_maker/textures/base/small/White.png')


###===--- Image Generator Functions ---===###

def gen_image(star, code='0'):
  '''
  This function generates the png file for one MesiSol NFT.
  
  Inputs:
    star: class
  
  Returns: a png image that represents the star.
  '''

  # Link each visual attribute of the star to more readable
  # variables for navigating the images.
  size, color = (star.size, star.color) # str, str
  sun_spots = star.sun_spots # str
  background = star.position  # str
  flares = star.solar_activity  # int
  if star.local_system:
    p_type, p_num = star.local_system  # str, int
  if star.partner:
    binary = star.partner # star obj
    binary_color = binary.color #str
  anomaly = star.anomaly # str

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
  
  # Define the paths for image selection. This setup allows for modularity
  # and the addition of extra images to increase randomization.
  root = 'image_maker/textures'
  bg_path = os.listdir(f'{root}/backgrounds/{background}')
  base_path = f'{root}/base/{img_size}/{color}.png'
  spots_path = os.listdir(f'{root}/spots/{sun_spots}/{color}')
  planet_path = os.listdir(f'{root}/planets/{sys_type}')
  flare_path = os.listdir(f'{root}/flares/{color}')
  binary_path = os.listdir(f'{root}/anomaly/binary/{binary_color}')
  nova_path = os.listdir(f'{root}/anomaly/Supernova/{color}.png')

  # Open each image in a new variable.
  bg = Image.open(random.choice(bg_path)).convert('RGBA')
  base = Image.open(base_path).convert('RGBA')
  spots = Image.open(random.choice(spots_path)).convert('RGBA')

  ### Image Creation ###
  
  # Because stars may appear in front of planets, paste the
  # local system in first.
  for planet_idx in range(p_num):
    planet = Image.open(random.choice(planet_path)).convert('RGBA')
    bg.paste(planet, (0,0), planet)
  
  # Then construct the rest of the star.
  bg.paste(base, (0,0), base)
  bg.paste(spots, (0,0), spots)
  
  for flare_idx in range(flares):
    flare = Image.open(random.choice(flare_path)).convert('RGBA')
    bg.paste(flare, (0,0), flare)
  
  if anomaly:
    if binary:
      anomaly_img = Image.open(random.choice(binary_path)).convert('RGBA')

    elif anomaly == 'Supernova':
      anomaly_img = Image.open(nova_path).convert('RGBA')
    
    

    bg.paste(anomaly_img)
  
  # Save the completed image to the correct folder.
  img_path = 'image_maker/star_pngs'
  bg.save(f'{img_path}/mesisol{code}.png')


def gen_collection(n):
  '''
  This function generates the png files for a collection
  of n size of mesisols.

  Inputs:
    n: int representing how many images to generate
  
  Returns:
    fills up the star_pngs folder with n amount of a star images.
  '''

  for star_idx in range(1, n + 1):
    star = gen_sol()

    gen_image(star, str(star_idx))