from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import sys

# Write a function that finds the outline of simple objects in images (for
# example, a square against a white background) using image gradients.

def outlines(image):
    x = filters.sobel(im, axis=1)
    y = filters.sobel(im, axis=0)
    return maximum(x > 0, y > 0)

if __name__ == '__main__':
    for path in sys.argv[1:]:
        im = array(Image.open(path).convert('L'))
        gray()
        axis('off')
        imshow(outlines(im))
        show()
