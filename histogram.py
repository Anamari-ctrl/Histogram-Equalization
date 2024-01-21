from IPython.display import display, Math, Latex

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('../image_histogram/lung.png')

# display the image
plt.imshow(img, cmap='gray')
plt.show()