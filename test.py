
import error_visor as EV

from inspect import currentframe, getframeinfo

def info():
    trak = getframeinfo(currentframe().f_back)
    return trak


frame_info = info()
print(frame_info.lineno)

class TestLogger:
    def testing_logger():
        try:
            print('Test de excepcion repr')
            with open('a'):
                pass
        except FileNotFoundError as ex:
            print(ex.args)
            print('###################################')
            print(ex.__cause__)
            print('###################################')
            print(ex.__context__)
            print('###################################')
            print(ex.__dict__)
            print('###################################')
            print(ex.__doc__)
            EV.Logger.err(EV.Error(description='Error de prueba', ex=ex, priority=EV.Priority.HIGH))
            print('###################################')
            # print(ex.__annotations__)
            # print('###################################')
            # print(ex.__annotations__)
            # print('###################################')
            # print(ex.__annotations__)
            # print('###################################')
            # print(ex.__annotations__)
            # print('###################################')
            # print(ex.__annotations__)


TestLogger.testing_logger()