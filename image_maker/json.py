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

  if star.anomaly:
    anomaly = star.anomaly
  else:
    anomaly = 'None'

  {"trait_type":"Temperature","value":"1"},

  # Generate the metadata to be passed to the minter
  metadata2 = {
    'standard' : 'arc69',
    'external_url' : 'mesiverse.org',
    'attributes' : [
      {'trait_type':'Temperature', 'value':str(int(float(temp))) + 'K'},
      {'trait_type':'Luminosity', 'value':lum},
      {'trait_type':'Size', 'value':size},
      {'trait_type':'Color', 'value':color},
      {'trait_type':'Life Stage', 'value':life_stage},
      {'trait_type':'Stellar Class', 'value':stellar_class},
      {'trait_type':'Solar Activity', 'value':activity},
      {'trait_type':'Solar Flares', 'value':flares},
      {'trait_type':'Position', 'value':position},
      {'trait_type':'Local System', 'value':p_type},
      {'trait_type':'Anomaly', 'value':anomaly}
      ]
  }

  # Generates log of meta data making it possible to go back and see what
  # attribtues each MesiSol has.
  meta_log = json.dumps(metadata2)

  with open(f'image_maker/star_json/MesiSolsMetadata{code}.json', 'w+') as j:
    j.write(meta_log)
  
  j.close

  return json.dumps(metadata2)
