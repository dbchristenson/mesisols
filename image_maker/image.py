###===--- Image Maker ---===###


###===--- Imports ---===###

# General #
from PIL import Image, ImageDraw, ImageFilter
import random, os

# Python Files #
from generator import utils
from generator.sol_gen import gen_sol
from image_maker import json


###===--- Image Generator Functions ---===###
def gen_collection(n):
  '''
  This function generates a collection of MesiSol images and
  their corresponding metadata.
  
  Inputs:
    n: int representing how many should be generated
  
  Returns: a collection of images and json data.
  '''

  for sol_num in range(n):
    star = gen_sol()

    gen_image(star, sol_num)


def gen_image(star, code='0'):
  '''
  This function generates the png file for one MesiSol NFT.
  
  Inputs:
    star: class
  
  Returns: a png image that represents the star.
  '''

  json.gen_json(star, code)

  # Link each visual attribute of the star to more readable
  # variables for navigating the images.
  size, color = (star.size, star.color) # str, str
  sun_spots = star.sun_spots # str
  background = star.position  # str
  flares = star.solar_activity  # str
  if star.local_system:
    p_type, p_num = star.local_system  # str, int
  binary = star.partner # str
  anomaly = star.anomaly # str

  # Convert the sizes to match the image.
  for dimension in utils.img_size_dict.items():
    img_key, val = dimension

    if size in val:
      img_size = img_key

      if img_size == 'special':
        img_size = random.choice(['small', 'medium', 'large'])
    
    if size in ['Cephied', 'Undefined']:
      img_size = random.choice(['small', 'medium', 'large'])
  
  # Convert the planets to match the Image
  if star.local_system:
    for planet_type in utils.img_p_dict.items():
      img_key, val = planet_type

      if p_type in val:
        sys_type = img_key
  
  # Define the paths for image selection. This setup allows for modularity
  # and the addition of extra images to increase randomization.
  root = 'image_maker/textures'
  base_path = f'{root}/base/{img_size}.png'

  # The spots, local system, position and flares attributes have different texture
  # meaning they must have their folder listed for selection of image.
  bg_path = f'{root}/backgrounds/{background}/'
  bg_lst = os.listdir(bg_path)

  spots_path = f'{root}/spots/{sun_spots}/{color}/'
  spots_lst = os.listdir(spots_path)

  if star.local_system:
    planet_path = f'{root}/planets/{sys_type}/'
    planet_lst = os.listdir(planet_path)
  
  flare_path = f'{root}/flares/{color}/{img_size}/{flares}/'
  flare_lst = os.listdir(flare_path)

  # Open each image in a new variable.
  bg = Image.open(bg_path + random.choice(bg_lst)).convert('RGBA')
  flare = Image.open(flare_path + random.choice(flare_lst)).convert('RGBA')
  base = Image.open(base_path).convert('RGBA')
  spots = Image.open(spots_path + random.choice(spots_lst)).convert('RGBA')


  ### Image Creation ###
  

  # Because stars may appear in front of planets, paste the
  # local system in first.
  if star.local_system:
    for planet_idx in range(p_num):
      planet = Image.open(planet_path + random.choice(planet_lst)).convert('RGBA')
      bg.paste(planet, (0,0), planet)
  
  # Anomalies generally interfere with the rest of the image creation
  # process so handle their case first then decide if the rest needs to be
  # generated or not.
  anomaly_img = None
  cont = False

  if anomaly:
    if binary:
      anomaly_path = f'{root}/anomaly/binary/{binary}.png'
      cont = True
    elif anomaly == 'Supernova':

      nova_material = None

      nova_age = random.choice(['Old', 'Young'])
      nova_material = random.choice(['Poor', 'Rich'])
      
      anomaly_path = f'{root}/anomaly/Supernova/{nova_age}/{nova_material}.png'
    elif anomaly == 'Eclipse':
      anomaly_path = f'{root}/base/{size}.png'
      cont = True
    elif anomaly == 'Pulsar':
      anomaly_path = f'{root}/anomaly/Pulsar/pulsar.png'
      cont = True
    elif anomaly == 'Mira Variable Star':
      anomaly_path = f'{root}/anomaly/Mira Variable Star/{color}.png'
    elif anomaly == 'Blackhole':
      anomaly_path = f'{root}/anomaly/Blackhole/Blackhole.png'
    elif anomaly == 'Supermassive Blackhole':
      bg = Image.open(f'{root}/backgrounds/Rogue/rogue2.png)').convert('RGBA')
      anomaly_path = f'{root}/anomaly/Supermassive Blackhole/smb.png'

    anomaly_img = Image.open(anomaly_path).convert('RGBA')
    bg.paste(anomaly_img, (0,0), anomaly_img)
  else:
    cont = True
  
  # Then construct the rest of the star.
  if cont:
    bg.paste(base, (0,0), base)
    bg.paste(flare, (0,0), flare)
    bg.paste(spots, (0,0), base)
  
  if anomaly == 'Eclipse':
    bg.paste(anomaly_img, (0,0), base)
  
  # Save the completed image to the correct folder.
  img_path = 'image_maker/star_pngs'
  bg.save(f'{img_path}/MesiSol{code}.png')