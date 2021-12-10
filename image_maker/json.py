###===--- Json Generator ---===###


###===--- Imports ---===###
import json


def gen_json(star, code):
  '''
  This function generates the ARC69 metadata for
  showing the attributes of a generated image.

  Inputs:
    star: Star obj
    code: str that represents which MesiSol the json
          data applies to.
  
  Returns: a file with the attributes of the MesiSol
  recorded on it.
  '''

  # Json data requires indentation so set up
  # a variable to handle it with consistency.
  ind = '    '

  # Parse out all relevant attributes of the star
  temp = str(star.temperature)
  lum = str(star.luminosity)
  size, color = (star.size, star.color) # str, str
  life_stage = star.life_stage
  stellar_class = star.stellar_class
  activity = star.sun_spots # str
  position = star.position  # str
  flares = star.solar_activity  # int

  # Some attributes might be parsed to be split if they
  # do not exist.
  if star.local_system:
    p_type, p_num = star.local_system  # str, int
  else:
    p_type = None
    p_num = 0
  if star.partner:
    binary = 'True'
  else:
    binary = 'False'
  anomaly = star.anomaly # str

  metadata2 = ('{'f'\n{ind}"standard": "arc69",'
                  f'\n{ind}"description": "MesiSol {code}",'
                  f'\n{ind}"attributes": ['

                  # Temperature
                  f'\n{ind}{ind}'
                  '{"trait_type":"Temperature",'
                  f'\n{ind}{ind}"value":"{temp}"\n{ind}{ind}' '},'

                  # Luminosity
                  f'\n{ind}{ind}'
                  '{"trait_type":"Luminosity",'
                  f'\n{ind}{ind}"value":"{lum}"\n{ind}{ind}' '},'

                  # Color
                  f'\n{ind}{ind}'
                  '{"trait_type":"Color",'
                  f'\n{ind}{ind}"value":"{color}"\n{ind}{ind}' '},'

                  # Size
                  f'\n{ind}{ind}'
                  '{"trait_type":"Size",'
                  f'\n{ind}{ind}"value":"{size}"\n{ind}{ind}' '},'

                  # Life Stage
                  f'\n{ind}{ind}'
                  '{"trait_type":"Life Stage",'
                  f'\n{ind}{ind}"value":"{life_stage}"\n{ind}{ind}' '},'

                  # Stellar Class
                  f'\n{ind}{ind}'
                  '{"trait_type":"Stellar Class",'
                  f'\n{ind}{ind}"value":"{stellar_class}"\n{ind}{ind}' '},'

                  # Solar Activity (Texture)
                  f'\n{ind}{ind}'
                  '{"trait_type":"Solar Activity",'
                  f'\n{ind}{ind}"value":"{activity}"\n{ind}{ind}' '},'

                  # Flares (Solar Activity) (I know this is confusing lol)
                  f'\n{ind}{ind}'
                  '{"trait_type":"Flares",'
                  f'\n{ind}{ind}"value":"{flares}"\n{ind}{ind}' '},'

                  # Position
                  f'\n{ind}{ind}'
                  '{"trait_type":"Position",'
                  f'\n{ind}{ind}"value":"{position}"\n{ind}{ind}' '},'

                  # Local System
                  f'\n{ind}{ind}'
                  '{"trait_type":"Local System",'
                  f'\n{ind}{ind}"value":"{p_type}"\n{ind}{ind}' '},'
                  
                  # Anomaly
                  f'\n{ind}{ind}'
                  '{"trait_type":"Anomaly",'
                  f'\n{ind}{ind}"value":"{anomaly}"\n{ind}{ind}' '},'

                  f'{ind}{ind}\n{ind}]\n'
  '}')

  with open(f'image_maker/star_json/MesiSolsMetadata{code}.json', 'w+') as j:
    j.write(metadata2)
  
  j.close
