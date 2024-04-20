import threading
print("Importing Vitals Module")
import recordvitals
print("Sucess")
print("Loading whatsapp Module")
import getassist
print("Success")
import time
print("Loading report generator")
import report
print("Sucess")
print("import camera Learning module")
import Camera
print("Sucess")
import os

## Loading VAribles
normal_hr_ranges = {
    "0-2": (80, 130),   # Age 0-2: normal range (beats per minute)
    "3-5": (70, 110),   # Age 3-5: normal range (beats per minute)
    "6-12": (60, 100),  # Age 6-12: normal range (beats per minute)
    "13-18": (50, 90),  # Age 13-18: normal range (beats per minute)
    "19-30": (60, 100), # Age 19-30: normal range (beats per minute)
    "31-40": (60, 100), # Age 31-40: normal range (beats per minute)
    # Add more age ranges and their corresponding normal HR ranges as needed
}

severity = 0
AHR = 0
ABT = 0
ASPO2 = 0
Age = 0

def mtest():
    print("LocalTest")
def debug():
    print("Debug Active")
    time.sleep(2)
    print("Local Function Test")
    mtest()
    time.sleep(2)
    print("Starting Blood Tests")
    AHR, ASPO2 = recordvitals.get_blood_info()
    print("Global Varibles:")
    print(AHR)
    print(ASPO2)
    time.sleep(2)
    print("Starting BodyTemp Tests")
    ABT = recordvitals.get_body_temperature()
    print("Average Temperature is: ", ABT)
    print("Debug Complete")
#Main Code Functions
def getstarted():
    print("Welcome")
    time.sleep(1)
    x=input("Press Enter To Get Started")
    info()
def info():
    global Age
    Name = input("What is Your Name: ")
    Age = int(input("What is your Age: "))
    report.new(Name, Age)
    report.add2report("Name", Name)
    report.add2report("Age", Age)
    print("Hello " + Name +", Lets get your Vitals")
    vicollect()
def vicollect():
    global AHR
    global ABT
    global ASPO2
    time.sleep(3)
    print("Please place your finger on the oxygen sensor")
    time.sleep(2)
    print("Starting Data Collection")
    AHR, ASPO2 = recordvitals.get_blood_info()
    print("Thank you")
    time.sleep(1)
    print("Place your hand, arm or forehead over the temperature sensor")
    time.sleep(5)
    print("Starting Temperature Sensor")
    ABT = recordvitals.get_body_temperature()
    time.sleep(5)
    print("Data Collected")
    print("Average Heart Rate: ", AHR)
    print("Average Blood Oxygen: ", ASPO2)
    print("Body Temperature: ", ABT)
    time.sleep(1)
    print("Saving Data")
    report.add2report("AHR", AHR)
    report.add2report("ASPO2", ASPO2)
    report.add2report("ABT", ABT)
    print("Saved")
    option = input("you you have any cuts or bruises (y/n): ")
    if option =="y" or option=="Y":
        print("okay please present the injury to the camera")
        report.add2report("Photos", "YES")
        time.sleep(3)
        directory = ".\\users\\Current_User"
        Camera.take_photo(camera_index=0, file_name='photo.jpg')
        photoanal()
    else:
        print("okay skipping")
        report.add2report("Photos", "NO")
        report.add2report("PhotoAnalyst", "N/A")
        global severity
        severity = 0
        Calculate()
        #############
def photoanal():# hehe funnyword
    print("Image Taken, Analysing...")
    directory = ".\\users\\Current_User"
    image_name = "photo.jpg"  # Replace "your_image.jpg" with the name of your saved image file
    image_path = os.path.join(directory, image_name)
    class_name, confidence_score = Camera.process_saved_image(image_path)
    print("Determined Class: ", class_name)
    print("Confidence: ", confidence_score)
    picinfo = class_name + " " + str(confidence_score)
    report.add2report("PhotoAnalyst", picinfo)
    global severity
    if "Bruse - Major" in class_name or "Cuts - Major" in class_name:
        severity = 3
    elif "Cuts - Minor" in class_name:
        severity = 2
    else:
        severity = 1
    Calculate()
def is_hr_not_normal(age, hr):
    # Get the normal heart rate range for the given age
    normal_range = normal_hr_ranges.get(age)
    
    # If the age is not found in the dictionary, assume normal range as (60, 100)
    if normal_range is None:
        normal_range = (60, 100)
    
    # Check if the heart rate is too low or too high for the age
    if hr < normal_range[0] or hr > normal_range[1]:
        return True  # Heart rate is not normal
    else:
        return False  # Heart rate is normal
def is_body_temp_not_normal(age, body_temp):
    # Define normal body temperature ranges by age
    normal_temp_ranges = {
        "0-2": (36.4, 38),   # Age 0-2: normal range (°C)
        "3-5": (36.1, 37.8), # Age 3-5: normal range (°C)
        "6-12": (36.1, 37.8),# Age 6-12: normal range (°C)
        "13-18": (36.1, 37.8),# Age 13-18: normal range (°C)
        "19-30": (36.1, 37.8),# Age 19-30: normal range (°C)
        "31-40": (36.1, 37.8),# Age 31-40: normal range (°C)
        # Add more age ranges and their corresponding normal temperature ranges as needed
    }
    normal_range = normal_temp_ranges.get(age)

    # If the age is not found in the dictionary, assume normal range as (36.1, 37.8)
    if normal_range is None:
        normal_range = (36.1, 37.8)

    # Check if the body temperature is too low or too high for the age
    if body_temp < normal_range[0] or body_temp > normal_range[1]:
        return True  # Body temperature is not normal
    else:
        return False  # Body temperature is normal


def Calculate():
    print("All information complete, calculating urgency")
    #score based Highest = 6, Lowest = 1
    score = 0
    score =  score + severity
    age = Age
    heart_rate = AHR

    if is_hr_not_normal(age, heart_rate):
        score = score + 1
    else:
        score = score + 0

    if ASPO2 <= 95:
        score = score + 1
    else:
        score = score + 0
        
    if is_body_temp_not_normal(age, ABT):
        score = score + 1
    else:
        score = score + 0
    print("Final Score = ", score)
    report.add2report("severity", score)
    if score > 4:
        getassist.pinghelp()
        print("Weve assessed this situation to be severe, Assistance has been called")
    elif score <3:
        print("We've assessed this situation to be low, you can either wait or contact your GP of an appointment instead")
    else:
        print("We've assessed this situation to be moderate and information has been fowarded.")
        print("please take a seat and wait")
        time.sleep(10)
        input("Press enter to finish")
        afinish()

def afinish():
     print("Thank you for using this assessment booth")
     report.packreport()
     print("Report has been fowarded to the appropriate departments")
     time.sleep(5)
     print("Assessment will refresh in 10 seconds")
     time.sleep(10)
     getstarted()
    
    
    



if __name__ == "__main__":
    print("mainfile Loaded")
    getstarted()
    #debug()

