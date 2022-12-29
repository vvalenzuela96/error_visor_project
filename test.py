""" 
Script para probar logger

@author Victor Valenzuela M
"""

import error_visor as EV

class TestLogger:
    def testing_logger():
        try:
            print('Test de excepcion repr')

            #Raise FileNotFoundError forced to test logger
            with open('a'):
                pass

        except FileNotFoundError as ex:
            error = EV.Error(
                description='Error de prueba',
                priority=EV.Priority.HIGH,
                ex=ex
                )
            EV.Logger.err(error)

TestLogger.testing_logger() #This class method is like a run()