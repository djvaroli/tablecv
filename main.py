from PIL import Image

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pytesseract

path_to_image = "./test_images/test_image_1.png"
image = cv2.imread(path_to_image, 0)

