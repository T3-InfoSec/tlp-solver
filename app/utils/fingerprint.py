import platform
import hashlib
import uuid
import json
import os

def get_stable_system_info():
    """
    Collect stable system details that rarely change to ensure a consistent fingerprint.
    """
    system_info = {
        'system': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'node': platform.node(),
    }

    # Add hardware UUID or motherboard serial if available
    try:
        if platform.system() == 'Linux':
            with open('/sys/class/dmi/id/board_serial', 'r') as f:
                system_info['board_serial'] = f.read().strip()
        elif platform.system() == 'Darwin':  # macOS
            system_info['hardware_uuid'] = os.popen(
                "ioreg -rd1 -c IOPlatformExpertDevice | awk '/IOPlatformUUID/' | sed 's/.*= //'").read().strip()
        elif platform.system() == 'Windows':
            import subprocess
            command = "wmic csproduct get UUID"
            result = subprocess.check_output(command).decode().splitlines()
            system_info['hardware_uuid'] = result[1].strip()
    except Exception:
        system_info['board_serial'] = 'unknown'

    # Add fallback using uuid.getnode()
    system_info['fallback_uuid'] = str(uuid.getnode())
    return system_info

def generate_fingerprint():
    """
    Generate a unique and consistent fingerprint for the system.
    """
    system_info = get_stable_system_info()

    # Convert system info to a stable string representation
    info_str = json.dumps(system_info, sort_keys=True)

    # Generate SHA-256 hash of the system information
    fingerprint = hashlib.sha256(info_str.encode()).hexdigest()

    # Use first 12 characters for a shorter identifier
    short_fingerprint = fingerprint[:12]

    print(f"Generated system fingerprint: {short_fingerprint}")
    print(f"System info: {json.dumps(system_info, indent=2)}")

    return short_fingerprint
