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


def gen_system_img(sys_type, num_planets):
  bg = Image.open('image_maker/textures/backgrounds/Rogue/rogue1.png')
  
  root = 'image_maker/textures'
  planet_path = f'{root}/planets/{sys_type}/'
  planet_lst = os.listdir(f'{root}/planets/{sys_type}')

  for planet_idx in range(num_planets):
    planet = Image.open(planet_path + random.choice(planet_lst)).convert('RGBA')
    bg.paste(planet, planet)
  
  img_path = 'image_maker/star_pngs'
  bg.save(f'{img_path}/planet_test.png')
  
  
  
