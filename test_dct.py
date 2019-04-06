from matplotlib import pyplot as plt
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


if __name__ == '__main__':
  image = open_image_as_array('yoda_lego.jpg')
  image = image[:,:,0]
  print(image.shape[0]//8)
  print(image.shape[1]//8)

  image = image[:61*8, :53*8]

  coef = bdct(image)
  recon = ibdct(coef)
  
  fig = plt.figure()
  ax1 = fig.add_subplot(1, 3, 1)
  ax2 = fig.add_subplot(1, 3, 2)
  ax3 = fig.add_subplot(1, 3, 3)
  
  ax1.imshow(image, cmap='gray')
  ax2.imshow(coef, cmap='gray')
  ax3.imshow(recon, cmap='gray')
  plt.show()

