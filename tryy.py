#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def tryer(a, b):
    
    if b == 'pixel_array':
        return(a.pixel_array)
    else:
        try:
            return(getattr(a, b))
        except AttributeError:
            return('No')

