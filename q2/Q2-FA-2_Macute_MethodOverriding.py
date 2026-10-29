class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8 # For senior 20% discount

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85 # For PH worker 15% discount

print("Hospital Billing System")
print("------------------------")

patients = {
    "Tokai Teio": Patient("Teio", 1000000.00),
    "Matikanetahnnhauser": SeniorPatient("Mambo", 1000000.00),
    "Agnes Tachyon": PhilHealthPatient("Tachyon", 1000000.00)
}

#output loops
for patient in patients:
    print()
    print(f"Patient Name: {patients[patient].get_name()}")
    print(f"Original Bill: {patients[patient].get_bill_amount()}")
    print(f"Final Bill: {patients[patient].calculate_bill()}")