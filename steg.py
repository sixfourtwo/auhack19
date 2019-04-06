import numpy as np
import cv2
from scipy.fftpack import fft, dct
import matplotlib.pyplot as plt

fn = 'yoda_lego.jpg'

img = cv2.imread(fn, 0)

plt.imshow(img)
plt.gray()
plt.show()


enc = dct(img,2)

msb1 = "{0:b}".format(int(enc[0,0]))
msb2 = "{0:b}".format(int(enc[1,0]))
msb3 = "{0:b}".format(int(enc[2,0]))
msb4 = "{0:b}".format(int(enc[3,0]))

print()
print(enc[0,0])
print(enc[1,0])
print(enc[2,0])
print(enc[3,0])
print()

enc[0,0] = int(msb1[:-2] + '01', 2)
enc[1,0] = int(msb2[:-2] + '00', 2)
enc[2,0] = int(msb3[:-2] + '10', 2)
enc[3,0] = int(msb4[:-2] + '00', 2)

# print("{0:b}".format(int(enc[0,0])))
# print("{0:b}".format(int(enc[1,0])))
# print("{0:b}".format(int(enc[2,0])))
# print("{0:b}".format(int(enc[3,0])))
print()
print(enc[0,0])
print(enc[1,0])
print(enc[2,0])
print(enc[3,0])
print()


dec = dct(enc,3)

plt.imshow(dec)
plt.gray()
plt.show()

enc2 = dct(dec,2)

# print("{0:b}".format(int(enc2[0,0])))
# print("{0:b}".format(int(enc2[1,0])))
# print("{0:b}".format(int(enc2[2,0])))
# print("{0:b}".format(int(enc2[3,0])))


print(enc[0,0])
print(enc[1,0])
print(enc[2,0])
print(enc[3,0])
print()
# print(I)
# pic = dct(dct(I.T).T)
# plt.imshow(pic)
# plt.gray()
# plt.show()


# wave = list(range(256))
# # print(pic)
# pic = np.ndarray((256, 256))
# for i in range(256):
#     pic[:, i] = wave
# plt.imshow(pic)
# plt.gray()
# plt.show()


# # enc[0] = 20
# print(enc)




# wave = list(range(256))
# # print(pic)
# pic = np.ndarray((256, 256))
# for i in range(256):
#     pic[:, i] = wave

# # dct_pic = dct(pic, 2) 
# dct_wave = dct(wave, 2)
# print(dct_wave)

# print(dct_pic.shape)
# plt.imshow(dct_pic)
# plt.gray()
# plt.show()

# plt.imshow(pic)
# plt.gray()
# plt.show()


