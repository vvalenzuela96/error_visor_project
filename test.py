
import error_visor as EV

EV.Logger.deposit()

from inspect import currentframe, getframeinfo

def info():
    return getframeinfo(currentframe().f_back)


frame_info = info()
print(frame_info)