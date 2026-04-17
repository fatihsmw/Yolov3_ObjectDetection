#Inference for ONNX mode1

import cv2
cuda=True
w="yolov7.tiny.onnx"
#img=cv2.imread('horse.jpg') #image-based execute!

import time
import requests
import random
import numpy as np
import onnxruntime as ort
from PIL import Image
from pathlib import Path
from collections import OrdereDict, namedtuple
