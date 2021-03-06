# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ws2812', [dirname(__file__)])
        except ImportError:
            import _ws2812
            return _ws2812
        if fp is not None:
            try:
                _mod = imp.load_module('_ws2812', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ws2812 = swig_import_helper()
    del swig_import_helper
else:
    import _ws2812
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Color_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Color_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Color_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _ws2812.Color_t_r_set
    __swig_getmethods__["r"] = _ws2812.Color_t_r_get
    if _newclass:r = _swig_property(_ws2812.Color_t_r_get, _ws2812.Color_t_r_set)
    __swig_setmethods__["g"] = _ws2812.Color_t_g_set
    __swig_getmethods__["g"] = _ws2812.Color_t_g_get
    if _newclass:g = _swig_property(_ws2812.Color_t_g_get, _ws2812.Color_t_g_set)
    __swig_setmethods__["b"] = _ws2812.Color_t_b_set
    __swig_getmethods__["b"] = _ws2812.Color_t_b_get
    if _newclass:b = _swig_property(_ws2812.Color_t_b_get, _ws2812.Color_t_b_set)
    def __init__(self): 
        this = _ws2812.new_Color_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ws2812.delete_Color_t
    __del__ = lambda self : None;
Color_t_swigregister = _ws2812.Color_t_swigregister
Color_t_swigregister(Color_t)


def init(*args):
  return _ws2812.init(*args)
init = _ws2812.init

def clear():
  return _ws2812.clear()
clear = _ws2812.clear

def show():
  return _ws2812.show()
show = _ws2812.show

def Wheel(*args):
  return _ws2812.Wheel(*args)
Wheel = _ws2812.Wheel

def colorWipe(*args):
  return _ws2812.colorWipe(*args)
colorWipe = _ws2812.colorWipe

def rainbow(*args):
  return _ws2812.rainbow(*args)
rainbow = _ws2812.rainbow

def rainbowCycle(*args):
  return _ws2812.rainbowCycle(*args)
rainbowCycle = _ws2812.rainbowCycle

def theaterChase(*args):
  return _ws2812.theaterChase(*args)
theaterChase = _ws2812.theaterChase

def theaterChaseRainbow(*args):
  return _ws2812.theaterChaseRainbow(*args)
theaterChaseRainbow = _ws2812.theaterChaseRainbow

def setBrightness(*args):
  return _ws2812.setBrightness(*args)
setBrightness = _ws2812.setBrightness

def getBrightness():
  return _ws2812.getBrightness()
getBrightness = _ws2812.getBrightness

def RGB2Color(*args):
  return _ws2812.RGB2Color(*args)
RGB2Color = _ws2812.RGB2Color

def Color(*args):
  return _ws2812.Color(*args)
Color = _ws2812.Color

def setPixelColor(*args):
  return _ws2812.setPixelColor(*args)
setPixelColor = _ws2812.setPixelColor

def setPixelColorT(*args):
  return _ws2812.setPixelColorT(*args)
setPixelColorT = _ws2812.setPixelColorT

def getPixelColor(*args):
  return _ws2812.getPixelColor(*args)
getPixelColor = _ws2812.getPixelColor

def numPixels():
  return _ws2812.numPixels()
numPixels = _ws2812.numPixels

def getPixels():
  return _ws2812.getPixels()
getPixels = _ws2812.getPixels

def setPWMBit(*args):
  return _ws2812.setPWMBit(*args)
setPWMBit = _ws2812.setPWMBit

def getPWMBit(*args):
  return _ws2812.getPWMBit(*args)
getPWMBit = _ws2812.getPWMBit

def dumpLEDBuffer():
  return _ws2812.dumpLEDBuffer()
dumpLEDBuffer = _ws2812.dumpLEDBuffer

def dumpPWMBuffer():
  return _ws2812.dumpPWMBuffer()
dumpPWMBuffer = _ws2812.dumpPWMBuffer

def dumpPWMStatus():
  return _ws2812.dumpPWMStatus()
dumpPWMStatus = _ws2812.dumpPWMStatus

def dumpPWMControl(*args):
  return _ws2812.dumpPWMControl(*args)
dumpPWMControl = _ws2812.dumpPWMControl

def dumpPWMDMAC():
  return _ws2812.dumpPWMDMAC()
dumpPWMDMAC = _ws2812.dumpPWMDMAC

def dumpPWM():
  return _ws2812.dumpPWM()
dumpPWM = _ws2812.dumpPWM

def dumpDMARegs():
  return _ws2812.dumpDMARegs()
dumpDMARegs = _ws2812.dumpDMARegs

def dumpControlBlock(*args):
  return _ws2812.dumpControlBlock(*args)
dumpControlBlock = _ws2812.dumpControlBlock

def dumpTransferInformation(*args):
  return _ws2812.dumpTransferInformation(*args)
dumpTransferInformation = _ws2812.dumpTransferInformation

def dumpDMA():
  return _ws2812.dumpDMA()
dumpDMA = _ws2812.dumpDMA

def terminate(*args):
  return _ws2812.terminate(*args)
terminate = _ws2812.terminate
# This file is compatible with both classic and new-style classes.


