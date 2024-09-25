import time
import asyncio
import threading
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from bluetooth_check import check_airpods_connected


async def switch_audio_output_to_airpods():
    """
    Switch audio output to Space Pods Pro using pycaw.
    """
    devices = AudioUtilities.GetSpeakers()  # Get the audio output devices
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # List all available devices and look for Space Pods Pro
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process is not None:  # Check for NoneType before accessing name()
            if "Space Pods Pro" in session.Process.name():  # Check for Space Pods Pro
                print("Switching audio output to Space Pods Pro...")
                # Here you can implement specific settings, like volume adjustment if needed.
                return True

    print("Space Pods Pro not found in available audio outputs.")
    return False


async def main():
    print("Looking for Space Pods Pro connection...")

    while True:
        if await check_airpods_connected():  # Await the async function properly
            print("Space Pods Pro connected!")
            if await switch_audio_output_to_airpods():
                print("Audio output switched successfully!")
            else:
                print("Failed to switch audio output.")
        else:
            print("Space Pods Pro not connected yet.")

        # Check every 10 seconds (adjust as needed)
        time.sleep(10)


def run_event_loop():
    """Run the asyncio event loop in a separate thread to ensure proper thread configuration."""
    asyncio.run(main())


if __name__ == "__main__":
    # Run the event loop in a new thread
    loop_thread = threading.Thread(target=run_event_loop)
    loop_thread.start()
