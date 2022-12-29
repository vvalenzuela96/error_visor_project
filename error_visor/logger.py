"""
@author Victor Valenzuela M
@since 28-12-22
"""

import json
from inspect import currentframe, getframeinfo
from datetime import datetime
from enum import Enum
from types import FrameType


date_format = "%d/%m/%Y, %H:%M:%S"

class Priority(Enum):
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'

class Error():
    'Para acciones que generan problema'
    description:str
    timestamp:datetime
    priority:Priority
    ex:Exception

    def __init__(
            self,
            description:str='',
            timestamp:datetime=datetime.now(),
            priority:Priority=Priority.MID,
            ex:Exception=None) -> None:
        self.description = description
        self.timestamp = timestamp
        self.priority = priority
        self.ex = ex
    
    def __repr__(self) -> str:
        return f"""Error(
                        description={self.description},
                        timestamp={self.timestamp},
                        priority={self.priority}
                        ex={self.ex}
                    )
                    """

class Warning():
    'Para acciones que podrian generar problemas, pero funcionan igual'
    #TODO Warning class code

def _to_dict(obj:Error | Warning, frame:FrameType) -> dict:
    tb = getframeinfo(frame)
    if isinstance(obj, Error):
        return {
            'type': 'error',
            'description': obj.description,
            'timestamp': obj.timestamp.strftime(date_format),
            'priority': obj.priority.value,
            'ex_name': obj.ex.__class__.__name__,
            'ex_args': obj.ex.args,
            'line': tb.lineno,
            'filename': tb.filename.split('\\')[-1],
            'class': frame.f_code.co_qualname,
            'function': tb.function,
            'positions': tb.positions
        }
    elif isinstance(obj, Warning):
        pass #TODO Warning transformation to dict

class Logger():
    @staticmethod
    def err(error:Error, printable:bool=False) -> bool:
        frame = currentframe().f_back
        error_dict  = _to_dict(error, frame)

        try:
            with open('logs/log.ev', 'x') as file:
                file.write('[]')
        except FileExistsError as ex:
            pass

        with open('logs/log.ev', 'r') as file:
            lista:list = json.load(file)
        
        lista.append(error_dict)

        with open('logs/log.ev', 'w') as file:
            file.write(json.dumps(lista))