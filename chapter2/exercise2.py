from PIL import Image
from chapter2 import harris
from numpy import *
from pylab import *
from scipy.ndimage import filters
import sys

# Incrementally apply stronger blur (or ROF de-noising) to an image and extract
# Harris corners. What happens?
if __name__ == '__main__':
    for path in sys.argv[1:]:
        im = array(Image.open(path).convert('F'))
        sigmas = lambda: range (0, 75, 3)
        imgs = list(map(lambda sigma: filters.gaussian_filter(im, sigma), sigmas()))
        ncols = 5
        nrows = math.ceil(float(len(imgs))/ncols)
        fig, _axs = subplots(nrows, ncols)
        axs = _axs.flatten()
        for i, img in enumerate(imgs):
            harrisim = harris.compute_harris_response(img)
            filtered_coords = harris.get_harris_points(harrisim, threshold=0.5)
            axs[i].imshow(img, cmap='gray')
            axs[i].plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords],'*')
            axs[i].axis('off')
        axis('off')
        show()
