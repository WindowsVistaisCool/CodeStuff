import json
import time

def store(file, read=False, key=None, val=None, onestring=None):
    x = None
    try:
        with open(file, 'r') as v:
            x = json.load(v)
    except:
        return
    if read is True:
        if key is None:
            return x
        return x[key]
    else:
        if key is None:
            with open(file, 'w') as v:
                json.dump(onestring, v, indent=4)
        else:
            x[key] = val
            with open(file, 'w') as v:
                json.dump(x, v, indent=4)

def firstBoot():
    print("Welcome to Birdo's adaptation of the Hunter XC model sprinkler control timer. Starting configuration...")
    while True:
        zones = input("How many zones do you have on the system: ")
        if zones in ["2", "4", "6", "8"]:
            store('config.json', False, 'numbzones', zones)
            print("Done")
            break
        else:
            print("Invaid number!")
            continue
    while True:
        mvalve = input("Do you have a master valve (y or n): ")
        if mvalve == 'y':
            store('config.json', False, 'mvalve', True)
            print("Done")
            break
        elif mvalve == 'n':
            store('config.json', False, 'mvalve', False)
            print("Done")
            break
        else:
            print("Invalid entry! Please enter 'y' or 'n'")
            continue
    while True:
        psr = input("Do you have a pump start relay (y or n): ")
        if psr == 'y':
            store('config.json', False, 'psr', True)
            print("Done")
            break
        elif psr == 'n':
            store("config.json", False, 'psr', False)
            print("Done")
            break
        else:
            print("Invalid entry! Please enter 'y' or 'n'")
            continue
    while True:
        sens = input("Do you have a sensor installed (y or n): ")
        if sens == 'y':
            store('config.json', False, 'sensor', True)
            print("Done")
            break
        elif sens == 'n':
            store('config.json', False, 'sensor', False)
            print("Done")
            break
        else:
            print("Invalid entry! Please enter 'y' or 'n'")
            continue
    store('config.json', False, 'firstBoot', False)
    print("Setup complete!")
    main()

def manualAllZones():
    pass

def manualOneZone(zoneToStart):
    zones = store('zones.json', True)
    checkedZone = False
    for zone in zones:
        if zoneToStart == zone:
            checkedZone = True
    if checkedZone == False: return

def setWaterDays():
    pass

def setDateTime():
    pass

def standby():
    print("The controller is now in standby mode")

def main():
    standby()

def startup():
    checkFirstBoot = store('config.json', True, 'firstBoot')
    if checkFirstBoot == True:
        firstBoot()
    else:
        main()

startup()
