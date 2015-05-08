
# coding: utf-8

# In[1]:

import unicornhat


# In[2]:

class morningstartup(object):
    def cycmorn(xcol, ycol):
        for y in range(8):
            for x in range(8):
                unicornhat.set_pixel(x, y, xcol, ycol)
                unicornhat.show()
                time.sleep(5)
                unicornhat

        time.sleep(10)
        unicornhat.off


# In[ ]:



