from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import sys
import math

# Take and image and apply Gaussian blur like in Figure 1-9. Plot the image
# contours for increasing values of σ. What happens? Can you explain why?
if __name__ == '__main__':
    for path in sys.argv[1:]:
        im = array(Image.open(path).convert('L'))
        imgs = list(map(lambda sigma: filters.gaussian_filter(im, sigma), range(0, 75, 3)))
        ncols = 5
        nrows = math.ceil(float(len(imgs))/ncols)
        fig, _axs = subplots(nrows, ncols)
        axs = _axs.flatten()
        for i, img in enumerate(imgs):
            axs[i].contour(img, origin='image')
        show()
