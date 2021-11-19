import itertools
import math
import os
import random

import tensorflow as tf
import numpy as np
# import rospy as rp

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from waymo_open_dataset import dataset_pb2 as open_dataset
from waymo_open_dataset.utils import \
    range_image_utils, transform_utils, frame_utils