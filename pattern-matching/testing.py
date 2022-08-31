from typing import Dict
import transformations

py_raw:str = "assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True"
py:list[str] = transformations.py(py_raw)

rust_raw:str = "assert_eq!(candidate(&[1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3), true);"
rust:list[str] = transformations.rust(rust_raw)

asserts:Dict = transformations.save(py, rust)
print(asserts)

print(transformations.compare(asserts))