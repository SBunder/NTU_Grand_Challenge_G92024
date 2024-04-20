import report
def Match(message):
    if message == "Chest pain":
        Cneed = 0
        svrty = 90  # High severity
    elif message == "Difficulty to breath":
        Cneed = 0
        svrty = 95  # High severity
    elif message == "Seizure":
        Cneed = 0
        svrty = 90  # High severity
    elif message == "Weakness":
        Cneed = 0
        svrty = 80  # Medium severity
    elif message == "Dizziness":
        Cneed = 0
        svrty = 70  # Medium severity
    elif message == "Fever":
        Cneed = 0
        svrty = 75  # Medium severity
    elif message == "Injury":
        Cneed = 1
        svrty = 80  # Medium severity
    elif message == "Pain":
        Cneed = 1
        svrty = 60  # Medium severity
    elif message == "Bleeding":
        Cneed = 1
        svrty = 85  # High severity
    elif message == "Urinary problems":
        Cneed = 0
        svrty = 75  # Medium severity
    elif message == "Eye/Ear Problems":
        Cneed = 0
        svrty = 70  # Medium severity
    elif message == "Nausea/vomiting/Diarrhoea":
        Cneed = 0
        svrty = 72  # Medium severity
    elif message == "Overdose":
        Cneed = 0
        svrty = 90  # High severity
    elif message == "Menstrual Issues":
        Cneed = 0
        svrty = 50  # Low severity
    elif message == "Sexual Health":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Diabetes":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Blood Pressure":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "High Temprature":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Sleep":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Allergy":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Heart":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "CandS":
        Cneed = 0
        svrty = 60  # Low severity
    elif message == "Burns":
        Cneed = 0
        svrty = 60 # Low severity
   
    else:
        print("Other Data Recieves, setting as Moderate and Enabling Camera")
        Cneed = 1
        svrty = 60
    return message, Cneed, svrty

    
    
