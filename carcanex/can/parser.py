import can
from typing import Iterator, Optional
from carcanex.dbc.manager import DBCManager

class CANParser:
    """
    Core CAN message parser.
    Handles reading from interfaces or log files and decoding messages via DBC.
    """
    def __init__(self, dbc_name: Optional[str] = None):
        self.dbc_manager = DBCManager()
        self.dbc_name = dbc_name

    def stream_from_interface(self, interface: str = 'can0') -> Iterator[dict]:
        """Stream decoded messages from a physical or virtual CAN interface."""
        bus = can.interface.Bus(interface, bustype='socketcan')
        
        try:
            for msg in bus:
                yield self._process_message(msg)
        finally:
            bus.shutdown()

    def stream_from_log(self, log_path: str) -> Iterator[dict]:
        """Stream decoded messages from a CAN log file."""
        # Simple implementation for ASC or similar log formats
        # In a real scenario, this would handle various log formats
        with can.LogReader(log_path) as reader:
            for msg in reader:
                yield self._process_message(msg)

    def _process_message(self, msg: can.Message) -> dict:
        """Internal helper to convert a raw CAN message to a decoded dict."""
        decoded = None
        if self.dbc_name:
            try:
                decoded = self.dbc_manager.decode_message(self.dbc_name, msg.arbitration_id, msg.data)
            except Exception:
                decoded = {"raw_data": msg.data.hex()}

        return {
            "timestamp": msg.timestamp,
            "id": msg.arbitration_id,
            "dlc": msg.dlc,
            "data": msg.data.hex(),
            "decoded": decoded,
            "is_extended": msg.is_extended_id
        }
