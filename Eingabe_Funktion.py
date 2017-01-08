
# coding: utf-8

# In[ ]:




# In[9]:

from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


# In[15]:

def Add_special_Fkt():
    w = widgets.Dropdown(
    options=['1', '2', '3'],
    value='2',
    description='Funktion:',
    disabled=False,
    button_style='' # 'success', 'info', 'warning', 'danger' or ''
    )
    return w


# In[17]:




# In[ ]:



