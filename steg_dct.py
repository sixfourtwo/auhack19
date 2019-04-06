from scipy.fftpack import fft, dct
import cv2
import matplotlib.pyplot as plt
import numpy as np

def _i2b(v):
    return "{0:b}".format(int(v))

def _b2i(b):
    return int(b,2)

def _encode_message():
    pass

def steg_dct(img, noSegBits, str2WM):
    enc = dct(dct(img,2).T,2)





fn = 'yoda_lego.jpg'

img = cv2.imread(fn, 0)

# plt.imshow(img)
# plt.gray()
# plt.show()

img = np.array(img, dtype=np.uint8)
print(1)
print(img)

enc = dct(dct(img,2).T,2) # dct encode

# print(enc[0,0])

dec = dct(dct(enc,3).T,3)
new_img = np.array(dec, dtype=np.uint8)

print(2)
print(new_img)

enc = dct(dct(new_img,2).T,2) # dct encode
dec = dct(dct(enc,3).T,3)
new_img = np.array(dec, dtype=np.uint8)
print(3)
print(new_img)

# print(enc[0,0])

# plt.imshow(dec)
# plt.gray()
# plt.show()


# print(enc)




