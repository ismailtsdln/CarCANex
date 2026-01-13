import os
import cantools
from typing import Dict, Any

class DBCManager:
    """
    Manages loading and interaction with DBC files.
    Wraps cantools for high-performance parsing.
    """
    def __init__(self, dbc_dir: str = "carcanex/dbc"):
        self.dbc_dir = dbc_dir
        self.databases: Dict[str, cantools.database.can.Database] = {}

    def load_dbc(self, dbc_name: str) -> cantools.database.can.Database:
        """Load a DBC file by name from the dbc directory."""
        if dbc_name in self.databases:
            return self.databases[dbc_name]

        dbc_path = os.path.join(self.dbc_dir, dbc_name)
        if not os.path.exists(dbc_path):
            raise FileNotFoundError(f"DBC file not found: {dbc_path}")

        db = cantools.database.load_file(dbc_path)
        self.databases[dbc_name] = db
        return db

    def decode_message(self, dbc_name: str, message_id: int, data: bytes) -> Dict[str, Any]:
        """Decode a CAN message using a specific DBC."""
        db = self.load_dbc(dbc_name)
        return db.decode_message(message_id, data)

    def list_available_dbcs(self):
        """List all DBC files in the dbc directory."""
        if not os.path.exists(self.dbc_dir):
            return []
        return [f for f in os.listdir(self.dbc_dir) if f.endswith('.dbc')]
