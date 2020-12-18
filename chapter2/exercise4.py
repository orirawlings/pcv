from pylab import *
import cv2 as cv
import sys

def match(desc1, desc2):
    bf = cv.BFMatcher()
    matches = bf.knnMatch(desc1,desc2,k=2)
    # Apply ratio test
    return [ m for m,n in matches if m.distance < 0.6*n.distance ]

def match_twosided(desc1, desc2):
    matches_12 = { m.queryIdx: m for m in match(desc1, desc2) }
    matches_21 = { m.queryIdx: m for m in match(desc2, desc1) }
    return [ m for m in matches_12.values() if m.trainIdx in matches_21 and matches_21[m.trainIdx].trainIdx == m.queryIdx ]

# Create copies of an image with different resolutions (for example, by halving
# the size a few times). Extract SIFT features for each image. Plot and match
# features to get a feel for how and when the scale independence breaks down.
if __name__ == '__main__':
    for path in sys.argv[1:]:
        im = cv.imread(path, cv.IMREAD_GRAYSCALE)
        sift = cv.SIFT_create()
        kp, desc = sift.detectAndCompute(im, None)

        iterations = 4
        fig, _axs = subplots(1, iterations)
        factor = 2
        for axs in _axs.flatten():
            im2 = cv.resize(im, None, fx=1.0/factor, fy=1.0/factor)
            kp1, des1 = sift.detectAndCompute(im,None)
            kp2, des2 = sift.detectAndCompute(im2,None)
            matches = [ [m] for m in match_twosided(des1, des2) ]
            axs.imshow(cv.drawMatchesKnn(im,kp1,im2,kp2,matches,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS))
            axs.axis('off')
            factor *= 2

        axis('off')
        show()