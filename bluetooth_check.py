import wmi

def check_airpods_connected():
    """
    Check if Space Pods Pro are connected using WMI to query Bluetooth devices.
    """
    try:
        # Create WMI instance
        wmi_service = wmi.WMI()
        
        # Query for Bluetooth devices (you might need to adjust this query depending on your system)
        devices = wmi_service.Win32_PnPEntity()
        
        for device in devices:
            # Check if the device has "Space Pods Pro" in the name
            if device.Name and "Space Pods Pro" in device.Name:
                print(f"Detected device: {device.Name}")
                return True

        return False

    except Exception as e:
        print(f"Error checking for Space Pods Pro: {e}")
        return False

if __name__ == "__main__":
    if check_airpods_connected():
        print("Space Pods Pro connected!")
    else:
        print("Space Pods Pro not connected.")
