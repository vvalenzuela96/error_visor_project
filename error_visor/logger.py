"""
@author Victor Valenzuela M
@since 28-12-22
"""

import json
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'

class Error():
    description:str
    timestamp:datetime
    priority:Priority

    def __init__(
            self,
            description:str,
            timestamp:datetime,
            priority:Priority) -> None:
        self.description = description
        self.timestamp = timestamp
        self.priority = priority
    
    def log():
        pass

class Warning():
    description:str
    timestamp:datetime
    

class Logger():
    @staticmethod
    def deposit():
        pass

