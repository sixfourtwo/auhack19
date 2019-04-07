from matplotlib import pyplot as plt
import binascii
from PIL import Image
import numpy as np

def auxcos(x,u):
  return np.cos( (np.pi/8) * (x + 0.5) * u )

def cosmat(M=8,N=8):
  C = np.array( [ [ auxcos(x,u) for u in range(N) ] 
               for x in range(M) ] ) / 2
  C[:,0] = C[:,0] / np.sqrt(2)
  # C[0,:] = C[0,:] / np.sqrt(2)
  return C

auxM = cosmat(8,8)
invM = np.linalg.inv(auxM)
auxT = np.transpose(auxM)
invT = np.transpose(invM)

def dct2(g):
  """
    Perform a 2D DCT transform on g, assuming that g is 8x8.
  """
  assert (8,8) == np.shape( g )
  return np.dot( auxT, np.dot( g, auxM ) )

def idct2(g):
  """
    Perform a 2D inverse DCT transform on g, assuming that g is 8x8.
  """
  assert (8,8) == np.shape( g )
  # return dot( invM, dot( g, invT ) )
  return np.dot( invT, np.dot( g, invM ) )

def bdct(C,f=dct2):
  """
    Make a blockwise (8x8 blocks) 2D DCT transform on the matrix C.
    The optional second parameter f specifies the DCT transform function.
    The height and width of C have to be divisible by 8.
  """
  (M,N) = np.shape(C)
  assert M%8 == 0
  assert N%8 == 0
  S = np.ndarray((M,N))
  for i in range(0,M,8):
    for j in range(0,N,8):
      S[i:(i+8),j:(j+8)] = f( C[i:(i+8),j:(j+8)] )
  return S
      
def ibdct(C): return bdct(C,f=idct2)

def open_image_as_array(filename):
  image = Image.open(filename)
  return np.asarray(image)


####################### Encode #####################

def encodeMsg(data, msg):
    
    # Run through data
    # pick pixels with data > 1024
    # change last 4 bits

#    binString = ' '.join(format(ord(x), 'b') for x in msg)
#    binString = bin(int.from_bytes(msg.encode(), 'big'))
#    binString = '{0:016b}'.format(int(msg,2))
    binString = [bin(ord(ch))[2:].zfill(8) for ch in msg]
#    binString = binString[2:]
    binStringCounter = 0
    
    smallBinString = []
    for i in binString:
        for k in range(0,8,2):
            smallBinString.append( binString[binStringCounter][k:k+2])
        binStringCounter = binStringCounter + 1 
    
#    print(chr(int(binString[0:8],2)))
    
    print(len(smallBinString))
    data = np.round(data)
    
    binIterator = 0
    rowCounter = 0
    colCounter = 0
    for row in data:
#    for row in range(0, len(data)):
        for x in row:
            if x > 255 and x < 512 and len(smallBinString) > binIterator: # and 1024 > x
                 msb = "{0:b}".format(int(x))
                 lsb = smallBinString[binIterator]
                 dataInjection = int(msb[:-2] + lsb,2)
                 data[rowCounter,colCounter] = dataInjection
            elif x > 512 and len(smallBinString) > binIterator: # and 1024 > x
                 msb = "{0:b}".format(int(x))
                 lsb = smallBinString[binIterator] + smallBinString[binIterator + 1]
                 dataInjection = int(msb[:-4] + lsb,2)
                 data[rowCounter,colCounter] = dataInjection     
                 
                 
                 binIterator += 1
            colCounter = colCounter + 1
        rowCounter = rowCounter + 1
    
    #decode the encoded picture
    return data

####################### Decode #####################

def decodeMsg(data):
    byteCounter = 0
    
    stringLen = 0;
    
    totalMsg = list()
    data = np.round(data)

    for row in data:
        for x in row:
            if x > 255 and x < 512: # and stringLen < 130:   
                # stringLen = stringLen + 2;                  
                msb = "{0:b}".format(int(x))[-2:]
                totalMsg.append(msb) # + msb2 + msb3 + msb4
                byteCounter += 2
                if byteCounter == 8:
                    byteCounter = 0
                    
#                    print(totalMsg[1:8])
#                    bin2int = int(totalMsg,2)
                    bin2int = totalMsg[0] + totalMsg[1] + totalMsg[2] + totalMsg[3]
                    word = chr(int(bin2int,2))
                    
                    if (word == '&'):
                        break;
                    totalMsg.clear()
                    print(word)
                    
            if x > 512: # and stringLen < 130:   
                # stringLen = stringLen + 2;                  
                msb = "{0:b}".format(int(x))[-4:]
                totalMsg.append(msb) # + msb2 + msb3 + msb4
                byteCounter += 4
                if byteCounter == 8:
                    byteCounter = 0
                    
#                    print(totalMsg[1:8])
#                    bin2int = int(totalMsg,2)
                    bin2int = totalMsg[0] + totalMsg[1]
                    word = chr(int(bin2int,2))
                    
                    if (word == '&'):
                        break;
                    totalMsg.clear()
                    print(word)
                

if __name__ == '__main__':
  image = open_image_as_array('yoda_lego.jpg')
  image = image[:,:,0]
#  print(image.shape[0]//8)
#  print(image.shape[1]//8)

  image = image[:61*8, :53*8]

  coef = bdct(image)
  
  encodedImg = encodeMsg(coef, "hello my &eee")
  recon = ibdct(encodedImg)
  
  coef2 = bdct(recon)
  decodeMsg(coef2)
  
  fig = plt.figure()
  ax1 = fig.add_subplot(1, 3, 1)
  ax2 = fig.add_subplot(1, 3, 2)
  ax3 = fig.add_subplot(1, 3, 3)
  
  ax1.imshow(image, cmap='gray')
  ax2.imshow(coef, cmap='gray')
  ax3.imshow(recon, cmap='gray')
  plt.show()

