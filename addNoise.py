import numpy as np
from skimage.util import random_noise

# def sp_noise(image, prob=0.5):
#     '''
#     Add salt and pepper noise to image
#     prob: Probability of the noise
#     '''
#     output = image.copy()
#     if len(image.shape) == 2:
#         black = 0
#         white = 255

#     else:
#         colorspace = image.shape[2]
#         if colorspace == 3:
#             black = np.array([0,0,0], dtype='uint8')
#             white = np.array([255, 255, 255], dtype='uint8')
#         else: #RGBA
#             black = np.array([0, 0, 0, 255], dtype='uint8')
#             white = np.array([255, 255, 255, 255], dtype='uint8')
#     probs = np.random.random(output.shape[:2])
#     output[probs<(prob/2)] = black
#     output[probs>1-(prob/2)] = white
#     return output

def noisy(noise_typ, image):
    if noise_typ == None: return image
    elif noise_typ in ['s&p','salt','pepper']: 
        noise_img = random_noise(image, mode=noise_typ, amount=0.3)
    else:
        noise_img = random_noise(image, mode=noise_typ)
    noise_img = (255*noise_img).astype(np.uint8)
    return noise_img