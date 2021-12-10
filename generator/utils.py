###===--- Utility Module ---===###

###===--- Imports ---===###
from scipy.stats import truncnorm
import numpy as np

# This place is probably kind of a mess, it is basically
# for storing random variables to run the program.

# Temperature
# Function for taking sample in a range using a gaussian distro.
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

get_temp = get_truncated_normal(7000, 3000, 1000, 30000)

# Luminosity classes and weights
lum_lst = [*range(8)]
lum_weight = [1, 4, 15, 20, 25, 15, 15, 5]

# Colors
color_lst = ['Black', 'Brown', 'Dynamic', 'Red',
            'Orange', 'Yellow', 'White', 'Blue']

# Sizes
size_lst = ['Neutron Star', 'Subdwarf', 'Dwarf', 'Subgiant',
            'Giant', 'Supergiant', 'Cepheid', 'Undefined']
img_size_dict = {
  'small': ['Neutron Star', 'Subdwarf'],
  'medium': ['Dwarf', 'Subgiant'],
  'large': ['Giant', 'Supergiant'],
  'special': ['Cepheid', 'Undefined']
}

# Life Stages
stage_lst = ['Protostar', 'Main Sequence', 'Post Sequence',
             'Near Death', 'Post Death', 'Undefined']

stage_arr = np.array([[4, 4, 4, 4, 4, 4, 4, 4], [3, 0, 0, 0, 0, 1, 1, 1],
                     [3, 1, 1, 1, 1, 1, 3, 3], [2, 2, 1, 1, 1, 1, 1, 1],
                     [3, 3, 3, 3, 2, 2, 2, 2], [4, 3, 3, 3, 3, 2, 2, 2],
                     [1, 1, 1, 1, 1, 0, 0, 0], [5, 5, 5, 5, 5, 5, 5, 5]])

# Stellar Classes
class_lst = ['M', 'K', 'G', 'F', 'A', 'B', 'O', 'S']

# Positions
position_lst = ['Disk', 'Globular Cluster', 'Halo',
                'Bulge', 'Nucleus', 'Rogue']
position_weight = [30, 20, 15, 15, 10, 10]

# Local System
system = get_truncated_normal(1, 2.5, 0, 4)
system_type_lst = ['Barren', 'Exposed', 'Habitable', 'Civilized', 'Advanced']
system_type_weight = [30, 25, 20, 20, 15]

img_p_dict = {
  'low': ['Barren', 'Exposed'],
  'medium': ['Habitable', 'Civilized'],
  'high': ['Advanced']
}


# Sun Spots
# spot_severity describes the overall texturization of the star.
spot_severity = ['Low', 'Medium', 'High']

# Solar Activity
flares = ['Low', 'Medium', 'High']
flare_weight = [40, 35, 25]

# Anomalies
anomaly_lst = ['Binary Star', 'Pulsar', 'Mira Variable Star', 'Super Nova', 'Eclipse', 'Blackhole', 'Supermassive Blackhole']
