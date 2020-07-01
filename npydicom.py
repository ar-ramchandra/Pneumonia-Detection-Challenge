#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from PIL import Image
import os
import pydicom as dicom
import tryy
def img_to_npy(imgs, dcti, im_path, op_path, size ):
    '''imgs: list of image names, dcti:Dictionary of keys and list, im_path:path to images, 
    op_path: Path to save the file, with file name(with filename.npy), size: size of images in npy file '''
    for n,i in enumerate(imgs):
            #iterating through each file and writing all the metadata to a csv row-wise
            a = dicom.read_file(os.path.join(im_path, i), force = True) 
            print(f'{round((n/len(imgs))*100, 2)}% complete\r', end="")
            for j,k in zip(['PatientID'], ['pixel_array']):
                dcti[j].append(tryy.tryer(a, j))
                img = Image.fromarray(tryy.tryer(a, k))
                a_r = img.resize(size)
                a_rs = np.array(a_r)
                dcti[k].append(a_rs)

    print('saving to;', op_path)
    np.save(op_path, dcti) 
    print('clearning memory')
    dcti = {'PatientID' : [], 'pixel_array' : []}

