from carcanex.can.parser import CANParser
from carcanex.safety.validator import SafetyValidator
import time

class CANSimulator:
    """
    Simulates CAN bus activity by replaying logs or generating synthetic data.
    Useful for testing safety logic and interface implementations.
    """
    def __init__(self, dbc_name=None):
        self.parser = CANParser(dbc_name)
        self.validator = SafetyValidator()

    def replay_log(self, log_path: str, realtime: bool = True):
        """Replay a CAN log file."""
        last_timestamp = None
        
        for msg in self.parser.stream_from_log(log_path):
            if realtime and last_timestamp is not None:
                sleep_time = msg['timestamp'] - last_timestamp
                if sleep_time > 0:
                    time.sleep(sleep_time)
            
            # Run safety validation during replay
            is_safe = self.validator.validate_message(msg)
            
            yield {
                "message": msg,
                "is_safe": is_safe
            }
            
            last_timestamp = msg['timestamp']

    def generate_synthetic_data(self, signals: dict):
        """Generate synthetic CAN messages based on signal definitions (Stub)."""
        # This would use the DBC to pack data into raw CAN frames
        pass
