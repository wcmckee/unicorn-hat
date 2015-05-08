
# coding: utf-8

# In[14]:

import unittest
import unicornhat
import random
import hamcrest


# In[ ]:




# In[13]:

class TestUnicornHat(unittest.TestCase):
    #def setUp(self):
        #randz = self.random.randint(0,7)
        
        #unicornhat.set_pixel
        #unicornhat.ws2812.setPixelColorRGB
    
        
        
        
    #def test_turn_on_all(self):
        
    def test_index_is_none(self):
        #Test turning on a single 
        #led
        randz = random.randint(0,7)
        ind = unicornhat.get_index_from_xy(randz, randz)
        assert ind != None
    
    def test_wrong_int(self):
        #test if x is less than 
        #7 and more than 0.
        #If x is wrong - fail.
        intz = (9)
        if intz >= 7 or intz < 0:
            assert intz
        #assert highd
        #as
        #hamcrest.
        
    def test_setpixel(self):
        unicornhat.set_pixel()
        
    #def test_


# In[ ]:



