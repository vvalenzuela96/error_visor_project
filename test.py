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
            EV.Logger.err(EV.Error(
                description='Error de prueba',
                ex=ex,
                priority=EV.Priority.HIGH
                ))
            EV.Logger.err(EV.Warning(
                description='Advertencia de prueba',
                ex=ex,
                follow_me=False
                ))

TestLogger.testing_logger() #This class method is like a run()