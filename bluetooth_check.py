import asyncio
from bleak import BleakScanner

async def check_airpods_connected():
    """
    Check if Space Pods Pro are connected via Bluetooth.
    """
    devices = await BleakScanner.discover()
    print("Detected devices:")
    for device in devices:
        # Print the name of each device discovered
        print(f"Device: {device.name}")
        if device.name and "Space Pods Pro" in device.name:
            return True
    return False

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.run_until_complete(check_airpods_connected()):
        print("Space Pods Pro connected!")
    else:
        print("Space Pods Pro not connected.")
