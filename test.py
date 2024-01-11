from clinic import Clinic
from patient import Patient
from doctor import Doctor


clinic_1 = Clinic("Clinic_1")

patient1 = Patient('Ali', 'Aliev', 1)
patient2 = Patient('Ali', 'Aliev', 2)
patient3 = Patient('Ali', 'Aliev', 3)
patient4 = Patient('Ali', 'Aliev', 4)
patient5 = Patient('Ali', 'Aliev', 5)

doctor1 = Doctor("Vali", "Valiev", 10, 21, "A")
doctor2 = Doctor("Vali", "Valiev", 11, 22, "A")
doctor3 = Doctor("Vali", "Valiev", 12, 23, "A")
doctor4 = Doctor("Vali", "Valiev", 13, 24, "A")
doctor5 = Doctor("Vali", "Valiev", 14, 25, "A")

print(clinic_1.add_patient(patient1))
print(clinic_1.add_patient(patient2))
print(clinic_1.add_patient(patient3))
print(clinic_1.add_patient(patient4))
print(clinic_1.add_patient(patient5))

print(clinic_1.get_patient(1))
print(clinic_1.get_patient(2))
print(clinic_1.get_patient(3))
print(clinic_1.get_patient(4))
print(clinic_1.get_patient(5))

print(clinic_1.add_doctor(doctor1))
print(clinic_1.add_doctor(doctor2))
print(clinic_1.add_doctor(doctor3))
print(clinic_1.add_doctor(doctor4))
print(clinic_1.add_doctor(doctor5))

print(clinic_1.get_doctor(21))
print(clinic_1.get_doctor(22))
print(clinic_1.get_doctor(23))
print(clinic_1.get_doctor(24))
print(clinic_1.get_doctor(25))


print(clinic_1.assign_Patient_to_Doctor(1, 21))
print(clinic_1.assign_Patient_to_Doctor(2, 22))
print(clinic_1.assign_Patient_to_Doctor(3, 23))
print(clinic_1.assign_Patient_to_Doctor(4, 24))
print(clinic_1.assign_Patient_to_Doctor(5, 22))

print(clinic_1.get_Doctor(1))
print(clinic_1.get_Doctor(2))
print(clinic_1.get_Doctor(6))

print(clinic_1.get_Patients(22))
print(clinic_1.get_Patients(21))