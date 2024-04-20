import threading
from serial_decode import start_serial_thread, latest_values
import time

global AHR
global ASPO2
def update_latest_values():
    while True:
        global HR
        global SPO2
        global RT
        global BT
        HR = latest_values["HR"]
        SPO2 = latest_values["SpO2"]
        RT = latest_values["Ambient"]
        BT = latest_values["tObject"]
        BT = BT + 3 # rough calibration
        latest_values
        time.sleep(0.5)  #Update every 1 seconds
def debug_vitals():
    print(HR,SPO2,RT,BT)


def countdown_timer(duration):
    for remaining in range(duration, 0, -1):
        print(f"Time remaining: {remaining} seconds", end="\r")
        time.sleep(1)
    print(" " * 30, end="\r")  # Clear the countdown message

def get_blood_info():
    print("Please place your finger on the sensor...")
    
    hr_sum = 0
    spo2_sum = 0
    hr_count = 0
    spo2_count = 0
    
    hr_started = False
    spo2_started = False
    
    hr_start_time = 0
    spo2_start_time = 0
    
    while HR <= 10 or SPO2 <= 10:
        if HR <= 10:
            print("Waiting For a Pulse")
        if SPO2 <= 10:
            print("Waiting for SPO2 Reading")
        time.sleep(1)  # Wait for 1 second before checking again
    
    print("HR and SPO2 signal detected. Recording data...")
    
    while True:
        if not hr_started:
            hr_started = True
            hr_start_time = time.time()
            countdown_timer(10)  # Start the countdown timer for HR for 10 seconds
        
        if HR > 10:
            hr_sum += HR
            hr_count += 1
            spo2_sum += SPO2
            spo2_count += 1
            
        if time.time() - hr_start_time >= 10:
            hr_average = hr_sum / hr_count
            if spo2_count != 0:  # Ensure spo2_count is not zero before division
                spo2_average = spo2_sum / spo2_count
                return hr_average, spo2_average
            else:
                return hr_average, 0  # Return 0 as SPO2 if no data recorded
        
import time

def get_body_temperature():
    print("Please place your hand/arm over the sensor...")
    
    bt_sum = 0
    bt_count = 0
    
    bt_started = False
    bt_start_time = 0
    
    while True:
        # Simulating temperature readings for demonstration purposes
        # Replace these lines with actual temperature sensor readings

        
        if BT > 8 + RT or BT > 33:
            if not bt_started:
                bt_started = True
                bt_start_time = time.time()
                print("Body temperature exceeding thresholds. Recording data...")
                
            if time.time() - bt_start_time < 5:
                bt_sum += BT
                bt_count += 1
                #print(BT)
            else:
                bt_average = bt_sum / bt_count
                #print(f"Average body temperature over 5 seconds: {bt_average}°C")
                return bt_average
        else:
            print("Body temperature within normal range. Waiting...")
            #print(BT)
            bt_count = 0  # Reset the count if temperature falls within normal range
            time.sleep(1)  # Wait for 1 second before checking again

# Example usage


   

start_serial_thread()
# Start a thread to periodically print the latest values
print_thread = threading.Thread(target=update_latest_values)
print_thread.daemon = True
print_thread.start()
print("Decoder Running")
