import time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from bluetooth_check import check_airpods_connected

def switch_audio_output_to_airpods():
    """
    Switch audio output to Space Pods Pro using pycaw.
    """
    devices = AudioUtilities.GetSpeakers()  # Get the audio output devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # List all available audio devices to identify the AirPods
    sessions = AudioUtilities.GetAllSessions()
    print("Listing available audio sessions:")
    for session in sessions:
        process_name = session.Process and session.Process.name() or "Unknown"
        print(f"Detected session: {process_name}")  # Debugging line to show all devices

        if "Space Pods Pro" in process_name:
            print("Switching audio output to Space Pods Pro...")
            return True  # Return success once found

    print("Space Pods Pro not found in available audio outputs.")
    return False

def main():
    print("Looking for Space Pods Pro connection...")

    while True:
        if check_airpods_connected():  # No need for async/await here
            print("Space Pods Pro connected!")
            if switch_audio_output_to_airpods():
                print("Audio output switched successfully!")
            else:
                print("Failed to switch audio output.")
        else:
            print("Space Pods Pro not connected yet.")

        # Check every 10 seconds (adjust as needed)
        time.sleep(10)

if __name__ == "__main__":
    main()
