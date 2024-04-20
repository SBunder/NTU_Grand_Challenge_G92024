import serial
import re
import threading

# Global variables to store the latest values
latest_values = {
    "HR": 0.0,
    "SpO2": 0,
    "Ambient": 0.0,
    "tObject": 0.0
}

# Function to parse the received data and update variables
def parse_data(data):
    # Regular expression pattern to extract values
    pattern = r'HR:(\d+\.\d+)/ SpO2:(\d+)/ Ambient:(\d+\.\d+)/ tObject:(\d+\.\d+)'
    match = re.match(pattern, data)
    if match:
        # Extract values from the matched groups
        hr = float(match.group(1))
        spo2 = int(match.group(2))
        ambient = float(match.group(3))
        t_object = float(match.group(4))
        return hr, spo2, ambient, t_object
    else:
        return None

# Function to continuously read serial data and update variables
def read_serial():
    ser = serial.Serial('COM3', 9600, timeout=1)  # Adjust baudrate as per your device
    while True:
        # Read a line from serial port
        data = ser.readline().decode().strip()
        if data:
            # Parse the received data
            result = parse_data(data)
            if result:
                # Update the latest values
                global latest_values
                latest_values["HR"], latest_values["SpO2"], latest_values["Ambient"], latest_values["tObject"] = result
               
            else:
                print("Invalid data received:", data)

def start_serial_thread():
    serial_thread = threading.Thread(target=read_serial)
    serial_thread.daemon = True
    serial_thread.start()
