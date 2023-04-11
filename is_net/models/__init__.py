# Standard imports
from os.path import dirname, abspath
import sys

sys.path.append(dirname(dirname(abspath(__file__))))

from models.isnet import ISNetGTEncoder, ISNetDIS
