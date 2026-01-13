from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from carcanex.can.parser import CANParser

class CarInterface(ABC):
    """
    Base class for vehicle-specific interfaces.
    Standardizes how we interact with different car platforms.
    """
    def __init__(self, dbc_name: str, interface: str = 'can0'):
        self.parser = CANParser(dbc_name)
        self.interface = interface
        self.vehicle_state: Dict[str, Any] = {}

    @abstractmethod
    def get_signals(self) -> Dict[str, Any]:
        """Fetch the latest interpreted signals from the vehicle."""
        pass

    @abstractmethod
    def send_command(self, command_name: str, params: Dict[str, Any]):
        """Send a control command to the vehicle."""
        pass

    def update_state(self, message: Dict[str, Any]):
        """Internal method to update the local vehicle state snapshot."""
        if 'decoded' in message and message['decoded']:
            self.vehicle_state.update(message['decoded'])

class GenericVehicle(CarInterface):
    """
    A template for specific car model implementations.
    """
    def get_signals(self) -> Dict[str, Any]:
        return self.vehicle_state

    def send_command(self, command_name: str, params: Dict[str, Any]):
        print(f"Sending {command_name} to vehicle with params: {params}")
        # Logic to pack signals and send via CAN would go here
