import unittest
import rust
        
exec_globals = {}
check_program:str = ("import rust" + "\n" 
+ "res:bool = rust.has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2],0.3)" + "\n" + "print(res)")
exec(check_program, exec_globals)


class TestRust(unittest.TestCase):
    def test_has_close_elements(self):
        a_list = [1.0, 2.0, 3.9, 4.0, 5.0, 2.2]
        self.assertTrue(rust.has_close_elements(a_list,0.3))
        
