###===--- Image Maker ---===###


###===--- Imports ---===###

# General #
from PIL import Image, ImageDraw, ImageFilter
from image_maker import textures
import random, os

# Python Files #
from generator import utils
from generator.sol_gen import gen_sol
from image_maker import json


###===--- Image Generator Functions ---===###

# Star(0,0,'Red','Subdwarf','Main Sequence','M','Halo',None,('Barren',2),'Low','Low',None)

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
  flares = star.solar_activity  # str
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
  if p_type:
    for planet_type in utils.img_p_dict.items():
      img_key, val = planet_type

      if p_type in val:
        sys_type = img_key
  
  # Define the paths for image selection. This setup allows for modularity
  # and the addition of extra images to increase randomization.
  root = 'image_maker/textures'
  bg_path = f'{root}/backgrounds/{background}/' + background.lower() + '1.png'
  base_path = f'{root}/base/{img_size}.png'

  # The spots, local system, and flares attributes have different texture
  # meaning they must have their folder listed for selection of image.
  spots_path = f'{root}/spots/{sun_spots}/{color}/'
  spots_lst = os.listdir(spots_path)
  if star.local_system:
    planet_path = f'{root}/planets/{sys_type}/'
    planet_lst = os.listdir(planet_path)
  flare_path = f'{root}/flares/{color}/{img_size}/{flares}/'
  flare_lst = os.listdir(flare_path)

  # Open each image in a new variable.
  bg = Image.open(bg_path).convert('RGBA')
  flare = Image.open(flare_path + random.choice(flare_lst)).convert('RGBA')
  base = Image.open(base_path).convert('RGBA')
  spots = Image.open(spots_path + random.choice(spots_lst)).convert('RGBA')


  ### Image Creation ###
  

  # Because stars may appear in front of planets, paste the
  # local system in first.
  if p_num:
    for planet_idx in range(p_num):
      planet = Image.open(planet_path + random.choice(planet_lst)).convert('RGBA')
      bg.paste(planet, (0,0), planet)
  
  # Anomalies generally interfere with the rest of the image creation
  # process so handle their case first.
  '''
  anomaly_img = None

  if anomaly:
    if binary:
      binary_path = f'{root}/anomaly/binary/{binary_color}'
      anomaly_img = Image.open(binary_path).convert('RGBA')

    elif anomaly == 'Supernova':
      nova_path = f'{root}/anomaly/Supernova/{color}.png'
      anomaly_img = Image.open(nova_path).convert('RGBA')

  bg.paste(anomaly_img, (0,0), anomaly_img)
  '''
  
  # Then construct the rest of the star.
  bg.paste(flare, (0,0), flare)
  bg.paste(base, (0,0), base)
  bg.paste(spots, (0,0), base)
  
  # Save the completed image to the correct folder.
  img_path = 'image_maker/star_pngs'
  bg.save(f'{img_path}/MesiSol{code}.png')


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
    json.gen_json(star, str(star_idx))
    