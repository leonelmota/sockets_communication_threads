from enum import Enum
from typing import Optional, Dict

class Type(Enum):
    REQ_ADD = 1
    REQ_REM = 2
    RES_ADD = 3
    RES_LIST = 4
    REQ_INF = 5
    RES_INF = 6
    ERROR = 7
    OK = 8
   
PATTERN:Dict[Type, str] = {
    Type.REQ_ADD:"01------",
    Type.REQ_REM:"02{:02d}----",
    Type.RES_ADD:"03----{:02d}",
    Type.RES_LIST:"04----{:02d}",
    Type.REQ_INF:"05{:02d}{:02d}--",
    Type.RES_INF:"06{:02d}{:02d}{}",
    Type.ERROR:"07--{:02d}{}",
    Type.OK:"08--{:02d}{}",
}
    
class Message:
    def __init__(self, type:Type, id_origin:Optional[int], id_destionation:Optional[int], payload:Optional[str]):
        self.type = type
        self.id_origin = id_origin
        self.id_destionation = id_destionation
        self.payload = payload
        
    def to_str(self, pattern:Dict[Type, str]=PATTERN) -> str:
        return pattern[self.type].format(self.id_origin, self.id_destination, self.payload)