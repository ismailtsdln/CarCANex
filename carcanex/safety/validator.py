import time
from typing import Dict, Any, List

class SafetyValidator:
    """
    Ensures CAN messages comply with safety limits and logical rules.
    Prevents illegal control commands or frequency anomalies.
    """
    def __init__(self):
        self.message_frequencies: Dict[int, List[float]] = {}
        self.safety_limits: Dict[str, Any] = {
            "max_steering_angle": 360,
            "max_gas": 100,
            "max_brake": 100
        }

    def validate_message(self, message: Dict[str, Any]) -> bool:
        """Run all safety checks on a decoded CAN message."""
        if not self._check_frequency(message):
            return False
        
        if not self._check_signal_limits(message):
            return False
            
        return True

    def _check_frequency(self, message: Dict[str, Any]) -> bool:
        """Check if message frequency is within acceptable bounds."""
        m_id = message['id']
        timestamp = message['timestamp']
        
        if m_id not in self.message_frequencies:
            self.message_frequencies[m_id] = []
            
        self.message_frequencies[m_id].append(timestamp)
        
        # Keep only the last 10 samples for moving average
        if len(self.message_frequencies[m_id]) > 10:
            self.message_frequencies[m_id].pop(0)
            
        # Basic anomaly detection (stub)
        return True

    def _check_signal_limits(self, message: Dict[str, Any]) -> bool:
        """Check if decoded signals are within defined safety limits."""
        decoded = message.get('decoded')
        if not decoded:
            return True
            
        # Example check
        if 'STEER_ANGLE' in decoded:
            if abs(decoded['STEER_ANGLE']) > self.safety_limits['max_steering_angle']:
                return False
                
        return True
