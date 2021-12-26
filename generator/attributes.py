###===--- Attribute Randomization Module ---===###


###===--- Imports ---===###
from generator import utils
import random
import numpy as np


###===--- Dependent Attributes ---===###

### Color Module ###
def gen_color(temperature, luminosity):
  '''
  This function generates the color of a star.
  
  Inputs:
    temperature: Int
    luminosity: Int
  
  Returns: a string that represents the color of the star.
  '''

  # Define the return variable, the ratio, and the percentile ranges
  color = 'Blue'
  ratio = int(temperature * luminosity)
  percentiles = {
  'zero' : (range(0, 7999), ['Black', 'Dynamic']),
  'ten' : (range(8000, 14999), ['Brown', 'Red', 'Orange']),
  'twofive' : (range(15000, 24999), ['Red', 'Orange', 'Yellow']),
  'fifty' : (range(25000, 37999), ['Orange', 'Yellow']),
  'sevenfive' : (range(38000, 50999), ['Yellow', 'White', 'Blue']),
  'ninety' : (range(51000, 63000), ['White', 'Blue'])
  }

  # Use a for loop to check the ratio for each range.
  for color_checks in percentiles:
    ratio_range, color_choice = percentiles[color_checks]
  
    if ratio in ratio_range:
      color = random.choice(color_choice)
      break

  return color


def color_analyze():
  '''
  This function generates csv file that stores 10,000 entries
  of the color ratio calculation.
  '''

  # Define the initial array to store.
  color_array = np.zeros(10000)

  # Take 10,000 samples and store them.
  for i in range(10000):
    temp = utils.get_temp.rvs()
    lum = random.choice(utils.lum_lst, utils.lum_weight)

    color_array[i] = int(temp * lum)
  
  np.savetxt('color_ratio.csv', color_array)


### Size Module ###
def gen_size(color):
  '''
  This function generates a star's size.

  Inputs:
    color: Str
  
  Returns: a string represnting the class size of a star.
  '''

  # Define the return variable, inital prob and the size sequence.
  size = None
  probabilities = None
  seq = utils.size_lst[:6]

  # Use conditionals to determine what the probablities of getting
  # each size class of star for each color.
  if color == 'Dynamic':
    probabilities = [15, 20, 20, 15, 30]
    seq = ['Subdwarf', 'Dwarf', 'Subgiant', 'Giant', 'Cepheid']
  elif color == 'Black':
    probabilities = [20, 30, 20, 30]
    seq = ['Neutron Star', 'Subdwarf', 'Dwarf', 'Undefined']
  elif color == 'Brown':
    probabilities = [60, 40]
    seq = ['Neutron Star', 'Subdwarf']
  elif color == 'Red':
    probabilities = [5, 35, 25, 15, 10, 10]
  elif color == 'Orange':
    probabilities = [0, 20, 42, 30, 5, 5]
  elif color == 'Yellow':
    probabilities = [0, 15, 55, 25, 4, 3]
  elif color == 'White':
    probabilities = [20, 25, 15, 25, 11, 4]
  elif color == 'Blue':
    probabilities = [25, 25, 17.5, 17.5, 12, 3]

  size = random.choices(seq, probabilities)[0]

  return size


def size_analyze():
  '''
  This function generates a csv file that stores 10,000 entries of
  calculation of sun size.
  '''

  # Define the initial array.
  size_array = np.zeros(10000)

  # Take 10,000 samples and store them.
  for i in range(10000):
    temp = utils.get_temp.rvs()
    lum = random.choice(utils.lum_lst, utils.lum_weight)

    color = gen_color(temp, lum)
    size_array[i] = utils.size_lst.index(gen_size(color))
  
  np.savetxt('size_analysis.csv', size_array)


### Life Stage Module ###
def gen_stage(size, color):
  '''
  This functions generates the approximate stage in its life
  cycle that a star is at.

  Inputs:
    size: Str
    color: Str
  '''

  # Define the return variable and the indexes
  # of the Star's size and color.
  life_stage = None
  size_idx = utils.size_lst.index(size)
  color_idx = utils.color_lst.index(color)

  # Find the value of the stage the Star is in by searching
  # a custom array.
  selected_stage = utils.stage_arr[size_idx, color_idx]
  life_stage = utils.stage_lst[selected_stage]

  return life_stage


### Stellar Class Module ###
def gen_stellar_class(color, luminosity):
  '''
  This function generates the stellar class of a star.
  
  Inputs:
    color: Str
    luminosity: Int
  
  Returns: a string that represents the star's stellar class
  '''

  # Define the return variable and establish if the star's luminosity
  # is above the median of the luminosity values.
  stellar_class = None
  high_lum = luminosity >= 6
  low_lum = luminosity <= 1

  # Get the normal colors of a star and the list of all stellar classes.
  norm_colors = ['Red', 'Orange', 'Yellow', 'White', 'Blue', 'Brown']
  class_lst = utils.class_lst

  # Use a conditional to assign stellar classes to a star.
  if color in norm_colors:
    color_index = norm_colors.index(color)
    stellar_class = class_lst[color_index]
  else:
    stellar_class = 'S'
    return stellar_class
    
  # Use a conditional to update the stellar class if the luminosity
  # condition is met in either direction.
  if high_lum:
    new_class_index = min(6, class_lst.index(stellar_class) + 1)
    stellar_class = class_lst[new_class_index]
  elif low_lum:
    new_class_index = max(0, class_lst.index(stellar_class) - 1)
    stellar_class = class_lst[new_class_index]
  
  return stellar_class


def class_analyze():
  '''
  This function generates a csv file that stores 10,000 entries of
  the index that corresponds to a star's stellar class.
  '''

  # Define the initial array.
  class_array = np.zeros(10000)

  for i in range(10000):
    temp = utils.get_temp.rvs()
    lum = random.choice(utils.lum_lst, utils.lum_weight)

    color = gen_color(temp, lum)
    class_array[i] = utils.class_lst.index(gen_stellar_class(color, lum))
  
  np.savetxt('class_analysis.csv', class_array)


# Partner Module #
def gen_partner(color, size):
  '''
  This function determines whether or not a star is eligible to
  have a second star orbiting with it.
  
  Inputs:
    color: Str
    size: Str
  
  Returns: another star class, but dumbed down.
  '''

  # Define the return variable and parameters for what is
  # needed to have a partner planet.
  sub_star = None
  chance = random.randint(1,100)

  # Conditional to check what color the binary star should be.
  binary_colors = ['Yellow', 'Orange', 'Red', 'Blue', 'White']
  binary_selection = [b_color for b_color in binary_colors if b_color != color]

  # Conditional to check if the star will be in a binary system.
  if color in binary_colors:
    if chance > 80:
      sub_star = random.choice(binary_selection)
  elif color == 'Dynamic':
    if chance > 50:
      sub_star = random.choice(binary_selection)

  return sub_star


###===--- Independent Attributes ---===###

### Position Module ###
def gen_position():
  '''
  This function generates where a planet is located inside the mesiverse.

  Returns: a string that represents the star's position in the galaxy.
  '''

  # Randomly pick the position for the star to be in.
  position = random.choices(utils.position_lst, utils.position_weight)[0]

  return position


### Local System Module ###
def gen_system():
  '''
  This functions generates a star's local solar system if any.
  
  Returns: a Tuple of Str and Int describing the type of solar system
  and how many planets are within it.
  '''

  num_planets = int(utils.system.rvs())

  if num_planets:
    system_type = random.choices(utils.system_type_lst, 
                                 utils.system_type_weight)[0]
  else:
    return None
  
  return (system_type, num_planets)


### Sun Spots Module ###
def gen_spots():
  '''
  This function generates a star's sun spot activity.
  Activity correlates to the overall texturedness of a star

  Returns: a string representation of the star's texture.
  '''
  
  return random.choice(utils.spot_severity)
  
  
### Solar Activty Module ###
def gen_solar():
  '''
  This functions generates a star's solar flare activity
  if there is any.
  
  Returns: an Str describing how severe the solar flares are.
  '''

  return random.choice(utils.flares)
