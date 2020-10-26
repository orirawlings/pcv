from PIL import Image, ImageFilter
from numpy import *
from pylab import *
from scipy.ndimage import filters
import sys
import math

# Implement an unsharp masking operation (https://en.wikipedia.org/wiki/Unsharp_masking)
# by blurring an image and then subtracting the blurred version from the
# original. This gives a sharpening effect to the image. Try this on both color
# and grayscale images.
if __name__ == '__main__':
    sigma, scale, threshold = 2, 1.5, 10
    for path in sys.argv[1:]:
        im = array(Image.open(path)).astype('float32')
        if len(im.shape) == 3:
            blur = empty_like(im)
            for i in range(im.shape[2]):
                blur[:,:,i] = filters.gaussian_filter(im[:,:,i], sigma)
        else:
            blur = filters.gaussian_filter(im, sigma)
        mask = ((im - blur) * scale)
        mask = (abs(mask) > threshold) * mask
        unsharp = clip(im + mask, 0, 255).astype('uint8')

        axis('off')
        if len(im.shape) == 2:
            gray()
        result = concatenate([im.astype('uint8'), unsharp], axis=1)
        imshow(result)
        show()
