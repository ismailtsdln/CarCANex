from .main import main

__version__ = "0.1.0"
__author__ = "Ismail Tasdelen"

class CarCANex:
    """
    Main SDK entry point for CarCANex.
    Provides methods for parsing, monitoring, and analyzing CAN data.
    """
    def __init__(self, dbc_path=None):
        self.dbc_path = dbc_path
        self.explorer = None # Placeholder for core logic

    def parse_log(self, log_path):
        """Parse a CAN log file."""
        print(f"Parsing log {log_path} with DBC {self.dbc_path}")
        # Implementation will go here
        pass

    def start_monitor(self, interface="can0"):
        """Start real-time monitoring on a CAN interface."""
        print(f"Monitoring {interface}")
        # Implementation will go here
        pass
