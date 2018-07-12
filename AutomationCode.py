
from lackey import *
from Patients import Patients


USERNAME = "ADTEDREG"
DEPARTMENT = "SMH ED"
PATIENT_NUMBER = 1  # This is the number that dictates the patient name, if the patient exists already, raise it


def main():
    patients = Patients(PATIENT_NUMBER)
    patients.addPatients("patientsData.csv", 5)
    login()

    for patient in patients.list:
        # --------------------------
        # Workflow for each patient
        # goes here now
        # --------------------------


def login():
    App.focus("Hyperspace - URMC POC")
    click("UserNameField.png")  # Username text field
    type(USERNAME + Key.TAB)
    type("model" + Key.ENTER)  # Password
    type(Key.TAB, KeyModifier.SHIFT)
    type(DEPARTMENT + Key.ENTER * 3)
    wait(4)
    popup("Please ensure the Epic Theme is set to default \n press ok to proceed")

def createPatient(patient):
    click("PatientStation.png")
    wait(1)
    type(patient["name"] + Key.TAB)
    type(Key.TAB)
    type(patient["sex"] + Key.TAB)
    type(patient["dob"])
    click("FindPatient.png")
    wait(2)
    if exists("GoBack.png"):  # Catches the situation where epic finds similar patient to yours
        click("GoBack.png")
        click("New.png")
        wait(1)
        if exists("New.png"):
            click("New.png")
            wait(1)
            type("1" + Key.ENTER)
        else:
            popup("The patient you are trying to create already exists. \n Change the number in the Patients() call at the top of your script")
            sys.exit("Program ended due to patient already existing")

    else:  # Normal path for creating patients
        click("Continue.png")
        wait(1)
        click("New.png")
    wait(3)


main()