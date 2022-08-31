from typing import TypedDict
from typing import Dict

global ASSERTS


class Asserts(TypedDict):
    language: str
    logical_expr: list[str]

ASSERTS:Asserts

def py(raw:str) -> list[str]:
    #PYTHON
    raw:str = "assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True"

    no_prefix: str = raw.replace("assert candidate","")

    no_prefix: str = no_prefix.replace("(","")
    no_prefix: str = no_prefix.replace(")","")

    left,right = no_prefix.split(" == ")

    right.lower()
    right = right.lower()
    
    result:list[str] = [left,right]
    return result


def rust(raw:str) -> list[str]:
    #Rust
    raw:str = "assert_eq!(candidate(&[1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3), true);"

    no_prefix: str = raw.replace("assert_eq!(candidate(&","")

    left,right = no_prefix.split("), ")
    right = right.replace(");","")
    
   
    result:list[str] = [left,right]
    return result


def save(py:list[str], rust:list[str]) -> Dict:

    asserts:Dict = {}

    asserts["Python"] = py
    asserts["Rust"] = rust

    return asserts

def compare(statements:Dict) -> list[bool]:
    
    left:bool = statements["Python"][0] == statements["Rust"][0]
    right:bool = statements["Python"][1] == statements["Rust"][1]

    result:list[str] = [left,right]

    return  result
    