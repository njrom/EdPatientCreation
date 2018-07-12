
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
        print(patient["name"])
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


main()