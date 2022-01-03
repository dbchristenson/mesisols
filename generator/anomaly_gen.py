###===--- Anomaly Initialization Module ---===###


###===--- Imports ---===###
import random


### Anomaly Module ###
def has_anomaly(Star):
  '''
  This function generates a star's anomalous property, if any.
  Stars may only have one anomalous property, but it is unlikely
  that the criteria for multiple anomalies will be met by a single
  star.

  Inputs:
    Star: Class

  Returns: a string representing the type of anomaly that the 
  star is or none if there is no anomaly.
  '''

  # Define the return variable
  anomaly_type = None

  ### Binary Star System Anomaly ###
  # Conditional to check if the Star is in a binary system.
  if Star.partner:
    anomaly_type = 'Binary Star'
    return anomaly_type
  

  ### Pulsar Anomaly ###

  # Conditional to check if the Star has Pulsar attributes.
  if Star.size == 'Neutron Star':
    chance = random.randint(1,100)

    if chance > 90:
      anomaly_type = 'Pulsar'
      return anomaly_type
  

  ### Super Nova ###
  nova_sizes = ['Giant', 'Supergiant']

  # Conditional to check if the Star has Super Nova attributes.
  if Star.size in nova_sizes and Star.life_stage == 'Near Death':
    chance = random.randint(1, 100)
    if chance > 25:
      anomaly_type = 'Supernova'
      return anomaly_type
  

  ### Eclipse ###
  eclipse_sizes = ['Subdwarf, Dwarf, Subgiant']
  if Star.local_system:
    planet_type, planet_num = Star.local_system

    # Conditional to check if the Star has Eclipse attributes.
    if (Star.size in eclipse_sizes and 
        Star.solar_activity == 'High' and
        planet_num > 0):

        chance = random.randint(1, 100)
        if chance > 10:
          anomaly_type = 'Eclipse'
          return anomaly_type

  
  ### Blackhole ###
  # Conditional to check if the Star has Black Hole attributes.
  if (Star.color == 'Black' and 
      Star.size == 'Undefined' and 
      Star.stellar_class == 'S'):

      # Stars can be Supermassive Black Holes by being in the
      # galaxy center.
      if Star.position == 'Galaxy Center':
        anomaly_type = 'Supermassive Blackhole'
      else:
        anomaly_type = 'Blackhole'

      Star.temperature = 1
  
  return anomaly_type



  