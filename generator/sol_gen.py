###===--- AlgoSols Star Generator ---===###


###===--- Imports ---===###


# General #
import random

# Python Files #
from generator import utils
from generator import anomaly_gen
from generator import attributes as att


###===--- Star Initialization ---===###
class Star:
    '''    
    Class for representing a generated star.
    
    ###===--- Attributes ---===###
    - Linked Attributes -
    Temperature: Int
    Luminosity: Int
    Color: Str
    Size: Int
    Life Stage: Str
    Stellar Class: Str
    Anomaly: None or Str
    Partner: None or Star

    - Mostly Independent Attributes -
    Position: Str
    System: None or Tuple of (Str, Int)
    Solar Flares: None or Tuple (Str, Int)


    ###===--- Methods ---===###
    Valuation: Determines the overall rarity of a star based on uncommon attributes.
    Supernova: Takes in a list of 3 stars and returns an anomalous star/object.
    '''

    def __init__(self, temperature, luminosity, color, size, life_stage, stellar_class, position, partner, local_system, sun_spots, solar_activity, anomaly):
        '''
        Initializes the star class.
        '''

        self.temperature = temperature
        self.luminosity = luminosity
        self.color = color
        self.size = size
        self.life_stage = life_stage
        self.stellar_class = stellar_class
        self.position = position
        self.partner = partner
        self.local_system = local_system
        self.sun_spots = sun_spots
        self.solar_activity = solar_activity
        self.anomaly = anomaly
    
    def __repr__(self):
      return (f"Algo Sol Attributes:\n"
              "---Depedent Variables---\n"
              f"Temperature: {self.temperature}\n"
              f"Luminosity: {self.luminosity}\n"
              f"Color: {self.color}\n"
              f"Size: {self.size}\n"
              f"Life Stage: {self.life_stage}\n"
              f"Stellar Class: {self.stellar_class}\n"
              f"Partner: {self.partner}\n"
              f"Anomaly: {self.anomaly}\n"
              "--- Independent Variables ---\n"
              f"Position: {self.position}\n"
              f"Local System: {self.local_system}\n"
              f"Sun Spots: {self.sun_spots}\n"
              f"Solar Activity: {self.solar_activity}\n")
    
    def value(self):
      pass


def gen_sol():
  '''
  This function uses RNG and logic to create a unique star.

  Returns: a star object.
  '''

  # Set the two base variables for the star.
  temp = utils.get_temp.rvs()
  lum = random.choices(utils.lum_lst, utils.lum_weight)[0]

  # Generate the rest of the attributes of the star using
  # 'stacked randomization' for subsequent attributes.
  color = att.gen_color(temp, lum)
  size = att.gen_size(color)
  life_stage = att.gen_stage(size, color)
  stellar_class = att.gen_stellar_class(color, lum)
  partner = att.gen_partner(color, size)

  # These attributes are randomized independent of previous
  # attribute assignments
  position = att.gen_position()
  local_system = att.gen_system()
  sun_spots = att.gen_spots()
  solar_activity = att.gen_solar()

  # The anomaly attribute is special and is decided based on
  # previous attributions to the star.
  generated_star = Star(temp, lum, color, size, life_stage, stellar_class, position, partner, local_system, sun_spots, solar_activity, None)

  # Pass the star to the anomaly generator and set the anomaly value
  # to its return value.
  anomaly = anomaly_gen.has_anomaly(generated_star)
  generated_star.anomaly = anomaly

  return generated_star