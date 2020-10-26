from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import sys
import math

# An alternative image normalization to histogram equalization is quotient
# image. A quotient image is obtained by dividing the image with a blurred
# version, I/(I * Gσ). Implement this and try it out on some sample images.
if __name__ == '__main__':
    sigma = 10
    for path in sys.argv[1:]:
        im = array(Image.open(path))
        quot = im/filters.gaussian_filter(im, sigma)
        quot = interp(quot, [quot.min(), quot.max()], [0, 1])
        imshow(quot)
        show()
