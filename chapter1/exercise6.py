from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import measurements
import sys

# Apply the label() function to a threshold image of your choice. Use
# histograms and the resulting label image to plot the distribution of object
# sizes in the image.
if __name__ == '__main__':
    threshold = 128
    for path in sys.argv[1:]:
        im = array(Image.open(path).convert('L'))
        im = im > threshold
        labels, num = measurements.label(im)
        print(num)
        subplot(1, 2, 1)
        axis('off')
        gray()
        imshow(im)
        subplot(1, 2, 2)
        hist(labels.flatten(), bins=num, log=True)
        show()
