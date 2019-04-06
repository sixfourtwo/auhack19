import numpy as np
import cv2

fn = 'simple.jpg'

img = cv2.imread(fn, 0)      # 1 chan, grayscale!
imf = np.float32(img)/255.0  # float conversion/scale
dst = cv2.dct(imf)           # the dct
img = np.uint8(dst)*255.0    # convert back

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()