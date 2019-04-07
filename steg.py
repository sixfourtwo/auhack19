import numpy as np
import cv2
import binascii
from scipy.fftpack import fft, dct
import matplotlib.pyplot as plt

def encodeMsg(data, msg):
    
    enc = dct(data,2) #
    
    binString = ' '.join(format(ord(x), 'b') for x in msg)

    prevWord = 0
    iterator = 0
    
    for x in range(8, len(binString)+8, 8):
        currWord = binString[prevWord:x]
        prevWord = x
        
        msb = "{0:b}".format(int(enc[iterator,0]))
        enc[iterator,0] = int(msb[:-8] + currWord, 2)
        
        iterator += 1

    #decode the encoded picture
    return dct(enc,3)    

def decodeMsg(data):
    enc2 = dct(data,2)/850
    totalMsg = 0

    for x in range(0, 5,  1):
        msb = "{0:b}".format(int(enc2[x,0]))[-8:];
        totalMsg = int(msb,2 ) # + msb2 + msb3 + msb4
        print(chr(totalMsg))

    

    
fn = 'yoda_lego.jpg'

img = cv2.imread(fn, 0)

#plt.imshow(img)
#plt.gray()
#plt.show()


#enc = dct(img,2) # dct encode

# extract values for the first four pixels
#msb1 = "{0:b}".format(int(enc[0,0]))
#msb2 = "{0:b}".format(int(enc[1,0]))
#msb3 = "{0:b}".format(int(enc[2,0]))
#msb4 = "{0:b}".format(int(enc[3,0]))

#print the shit
#print()
#print(enc[0,0])
#print(enc[1,0])
#print(enc[2,0])
#print(enc[3,0])
#print()

# adjust the 2 lsb, 01001000 = H in ascii
#enc[0,0] = int(msb1[:-8] + '01001000', 2)
# enc[1,0] = int(msb2[:-2] + '00', 2)#
#enc[1,0] = int(msb2[:-4] + '1000', 2)
#enc[3,0] = int(msb4[:-2] + '00', 2)

# print("{0:b}".format(int(enc[0,0])))
# print("{0:b}".format(int(enc[1,0])))
# print("{0:b}".format(int(enc[2,0])))
# print("{0:b}".format(int(enc[3,0])))
#print()
#print(enc[0,0])
#print(enc[1,0])
#print(enc[2,0])
#print(enc[3,0])
#print()

#decode the encoded picture
dec = encodeMsg(img, "hello") #dct(enc,3)

#fig = plt.figure()
#plt.imshow(dec)
#plt.gray()
#plt.show()

decodeMsg(dec)

#enc2 = dct(dec,2)/850

# print("{0:b}".format(int(enc2[0,0])))
# print("{0:b}".format(int(enc2[1,0])))
# print("{0:b}".format(int(enc2[2,0])))
# print("{0:b}".format(int(enc2[3,0])))


#print(enc2[0,0])
#print(enc2[1,0])
#print(enc2[2,0])
#print(enc2[3,0])
#print()

#print(enc2[0,0]/dec[0,0])
#print(enc[0,0]/img[0,0])

#msb1 = "{0:b}".format(int(enc2[0,0]))[-8:];
#msb2 = "{0:b}".format(int(enc[1,0]))[-4:];
#msb3 = "{0:b}".format(int(enc[2,0]))[-2:];
#msb4 = "{0:b}".format(int(enc[3,0]))[-2:];

#totalMsg = int(msb1,2 ) # + msb2 + msb3 + msb4

#print(chr(totalMsg))

#msgToEncode(enc, "hello")

    

    #binValue = msg
#    msb1 = "{0:b}".format(int(enc[0,0]))
#    # adjust the 2 lsb, 01001000 = H in ascii
#    enc[0,0] = int(msb1[:-8] + '01001000', 2)
#    
#    #decode the encoded picture
#    return dec = dct(enc,3)
    
    


# fig.savefig('plot.jpg')
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


