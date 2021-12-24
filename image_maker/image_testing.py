###===--- Image Tester ---===###

###===--- Imports ---===###

# General #
from PIL import Image, ImageDraw, ImageFilter
from image_maker import textures
import random, os

# Python Files #
from generator import utils
from generator.sol_gen import gen_sol

# from image_maker import image_testing
# image_testing.gen_system_img('low', 2)

root = 'image_maker/textures'


def gen_system_img(sys_type, num_planets):
  bg = Image.open('image_maker/textures/backgrounds/Disk/d1.png').convert('RGBA')
  
  planet_path = f'{root}/planets/{sys_type}/'
  planet_lst = os.listdir(f'{root}/planets/{sys_type}')

  img_path = 'image_maker/star_pngs'
  
  for planet_idx in range(num_planets):
    planet = Image.open(planet_path + random.choice(planet_lst)).convert('RGBA')
    planet.save(f'{img_path}/single_planet.png')
    bg.paste(planet, (0,0), planet)
  
  bg.save(f'{img_path}/planet_test.png')


def gen_tsol(n):
  for mesisol in range(n):
    star = gen_sol()

    # Parse out relevant attributes.
    bg = Image.new('RGBA', (700, 700))
    color = star.color
    size = star.size
    flares = star.solar_activity
    sun_spots = star.sun_spots

    # Convert the sizes so they match the bases.
    for dimension in utils.img_size_dict.items():
      img_key, val = dimension

      if size in val:
        img_size = img_key

    # Set up variables for the directory.
    root = 'image_maker/textures'
    base_path = f'{root}/base/{img_size}.png'

    # Find the necessary images.
    spots_path = f'{root}/spots/{sun_spots}/{color}/'
    spots_lst = os.listdir(spots_path)

    flare_path = f'{root}/flares/{color}/{img_size}/{flares}/'
    flare_lst = os.listdir(flare_path)

    flare = Image.open(flare_path + random.choice(flare_lst)).convert('RGBA')
    base = Image.open(base_path).convert('RGBA')
    spots = Image.open(spots_path + random.choice(spots_lst)).convert('RGBA')

    # Create the new image.
    bg.paste(base, (0,0), base)
    bg.paste(flare, (0,0), flare)
    bg.paste(spots, (0,0), base)

    rand_num = random.randint(0, 100000)

    # Save the image.
    img_path = 'image_maker/test_pngs'
    bg.save(f'{img_path}/examplesol{rand_num}.png')

