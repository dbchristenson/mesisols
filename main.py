###===--- MesiSols NFT Generator ---===###


###===--- Imports ---===###
import os
import re
from generator.sol_gen import gen_sol
from image_maker.image import gen_image
from image_maker.image import gen_collection
from minting.mint import mint_collection

def check_match():
  pngs = sorted(os.listdir('image_maker/star_pngs'))
  jsons = sorted(os.listdir('image_maker/star_json'))
  total_sols = len(pngs)

  for idx in range(total_sols):
    cur_png = pngs[idx]
    cur_json = jsons[idx]

    png_digits = re.sub(r"\D+", "", cur_png)
    json_digits = re.sub(r"\D+", "", cur_json)
    print(png_digits)
    print(json_digits)

    if png_digits != json_digits:
      return False
