import os
import unittest
from carcanex.can.parser import CANParser
from carcanex.dbc.manager import DBCManager

class TestCarCANexFoundation(unittest.TestCase):
    def test_directory_structure(self):
        """Verify that basic project directories exist."""
        dirs = ['carcanex', 'carcanex/can', 'carcanex/car', 'carcanex/safety', 'carcanex/dbc']
        for d in dirs:
            self.assertTrue(os.path.isdir(d), f"Directory {d} does not exist")

    def test_imports(self):
        """Verify that core modules can be imported."""
        try:
            from carcanex.can.parser import CANParser
            from carcanex.dbc.manager import DBCManager
        except ImportError as e:
            self.fail(f"Failed to import core modules: {e}")

    def test_can_parser_init(self):
        """Verify CANParser initialization."""
        parser = CANParser()
        self.assertIsInstance(parser.dbc_manager, DBCManager)

if __name__ == '__main__':
    unittest.main()
