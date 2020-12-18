from PIL import Image
from chapter2 import harris
from numpy import *
from pylab import *
from scipy.ndimage import filters
import cv2 as cv
import sys

# An alternative corner detector to Harris is the FAST corner detector. There
# are a number of implementations, including a pure Python version available at
# http://www.edwardrosten.com/work/fast.html. Try this detector, play with the
# sensitivity threshold, and compare the corners with the ones from our Harris
# implementation.
if __name__ == '__main__':
    for path in sys.argv[1:]:
        im = array(Image.open(path).convert('F'))
        fig, _axs = subplots(1, 2)
        axs = _axs.flatten()

        harrisim = harris.compute_harris_response(im)
        filtered_coords = harris.get_harris_points(harrisim, threshold=0.2)
        axs[0].imshow(im, cmap='gray')
        axs[0].plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords],'*')
        axs[0].axis('off')

        cvimg = cv.imread(path,0)
        fast = cv.FastFeatureDetector_create(threshold=75)
        keypoints = fast.detect(cvimg, None)
        cvimg2 = cv.drawKeypoints(cvimg, keypoints, None, color=(255,0,0))
        axs[1].imshow(cvimg2)
        axs[1].axis('off')

        axis('off')
        show()
