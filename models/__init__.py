import sys,os
dir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(dir)
from D3 import D3

from PerceptualLoss import LossNetwork as PerLoss
