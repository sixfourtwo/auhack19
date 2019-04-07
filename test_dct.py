from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import math


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

def serve_msg(msg):
  bin_msg = str2bin(msg)
  for b in bin_msg:
    yield b

def _noYields(gen, noYields):
  s = ''
  ITERFLAG = True
  for _ in range(noYields):
    next_yield = next(gen, None)
    if next_yield is not None: s+=next_yield
    else: 
      ITERFLAG = False
      break
  return s, ITERFLAG


def int2bin(int):
  return "{0:b}".format(int)

def str2bin(text, encoding='utf-8', errors='surrogatepass'):
  bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
  return bits.zfill(8 * ((len(bits) + 7) // 8))

def bin2str(bits, encoding='utf-8', errors='surrogatepass'):
  n = int(bits, 2)
  return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def _end_of_msg(msg):
  if len(msg) > 22:
    if msg[-22:] == '1011110010111100101111':
      return True

def _encode_msg(x, msg_gen):
    noSnacks = int((math.log(abs(x),2))//4)
    next_yield, ITERFLAG = _noYields(msg_gen, noSnacks)
    # x_bin = int2bin(math.ceil(x))
    x_bin = int2bin(int(x))
    x_bin = x_bin[:-len(next_yield)]
    if x_bin != '':
      x_bin += next_yield
      return int(x_bin, 2), ITERFLAG
    else: return 0, ITERFLAG
    

def _decode_msg(x, msg):
  if not _end_of_msg(msg):
      noSnacks = int((math.log(abs(x),2))//4)
      x_bin = int2bin(int(x))
      msg += x_bin[-noSnacks:]
  return msg

def _maze_runner(coef, msg, MIN=255):
  ITERFLAG = True
  msg_gen = serve_msg(msg)
  for i,row in enumerate(coef):
    for j,x in enumerate(row):
      if abs(x) > MIN and ITERFLAG:
        x_bin, ITERFLAG = _encode_msg(x, msg_gen)
        coef[i,j] = x_bin


def _maze_derunner(coef, MIN=255):
  msg = ''
  for i,row in enumerate(coef):
    for j,x in enumerate(row):
      if abs(x) > MIN:
        msg = _decode_msg(x, msg)
  return bin2str(msg)

if __name__ == '__main__':
  image = open_image_as_array('yoda_lego_two.jpg')

  img2 = open_image_as_array('yoda_lego.jpg')
  img2_1 = str(img2[:,:,0].tolist()).replace('[','').replace(']','')
  img2_2 = str(img2[:,:,1].tolist()).replace('[','').replace(']','')
  img2_3 = str(img2[:,:,2].tolist()).replace('[','').replace(']','')

  # image = image[:,:,0]
  img_shp_row = image.shape[0]//8
  img_shp_col = image.shape[1]//8
  image = image[:img_shp_row*8, :img_shp_col*8]

  
  c1 = image[:,:,0]
  c2 = image[:,:,1]
  c3 = image[:,:,2]

  # [for row in range(image.shape[0]) for col in range(image.shape[1]) if image[row, col] > 10]
  
  coef1 = bdct(c1)
  _maze_runner(coef1, img2_1+'///')
  recon1 = ibdct(coef1)

  coef2 = bdct(c2)
  _maze_runner(coef2, 'dungo///')
  recon2 = ibdct(coef2)

  coef3 = bdct(c3)
  _maze_runner(coef3, 'blungo///')
  recon3 = ibdct(coef3)
  # _maze_runner(coef, 'Something is wrong in the state of Denmark. I like dungo in the mungo this is not a test. Whatzup whazup whatzup bitconneeeectSomething is wrong in the state of Denmark. I like dungo in the mungo this is not a test. Whatzup whazup whatzup bitconneeeectSomething is wrong in the state of Denmark. I like dungo in the mungo this is not a test. Whatzup whazup whatzup bitconneeeectSomething is wrong in the state of Denmark. I like dungo in thewrong in the state of Denmark. I like dungo in ///')
  col_img = np.ndarray((img_shp_row*8, img_shp_col*8, 3))
  col_img[:,:,0] = recon1
  col_img[:,:,1] = recon2
  col_img[:,:,2] = recon3
  col_img = col_img/255
  # print(coef[0,0])

  # plt.imshow(col_img)
  # plt.show()
  # fig = plt.figure()
  # ax1 = fig.add_subplot(1, 3, 1)
  # ax2 = fig.add_subplot(1, 3, 2)
  # ax3 = fig.add_subplot(1, 3, 3)
  
  # ax1.imshow(image, cmap='gray')
  # ax2.imshow(coef, cmap='gray')
  # ax3.imshow(recon, cmap='gray')
  # plt.show()

  yoda = _maze_derunner(bdct(recon1))
  yoda.split(' ')
  print(_maze_derunner(bdct(recon2)))
  print(_maze_derunner(bdct(recon3)))
