from patient import Patient
from exceptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor

class Clinic:
    def __init__(self, name) -> None:
        self._name = name
        self._patient_list: list[Patient] = []
        self._doctor_list: list[Doctor] = []
        self.somethig = None

    def add_patient(self, new_patient:Patient): ###
        self._patient_list.append(new_patient)
        return new_patient

    def get_patient(self, ssn): ###
        for person in self._patient_list:
            if person.ssn == ssn:
                return person
        else:
            return NoSuchPatient(ssn)
    
    def add_doctor(self, new_doctor:Doctor): ###
        self._doctor_list.append(new_doctor)
        return new_doctor
    
    def get_doctor(self, id): ###
        for doctor in self._doctor_list:
            if doctor.id == id:
                return doctor
        else:
            return NoSuchDoctor(id)
    
    def assign_Patient_to_Doctor(self, ssn, id): ###
        patient: Patient = self.get_patient(ssn)
        doctor: Doctor = self.get_doctor(id)
        if patient != NoSuchPatient:
            if doctor != NoSuchDoctor:
                patient._doctor = doctor
                doctor.add_patient(patient)
                return f"{ssn}-SSN bemor {id}-ID shifokorga biriktirildi"
            else:
                return NoSuchDoctor(id)
        else:
            return NoSuchPatient(ssn)
        
    def get_Doctor(self, patient_ssn): ###
        for patient in self._patient_list:
            if patient.ssn == patient_ssn:
                if patient._doctor != None:
                    return patient._doctor
                else:
                    return f"{patient.ssn}-SSN bemor doctorga biriktirilmagan"
        return NoSuchPatient(patient_ssn)    

    def get_Patients(self, doctor_id): ###
        doctor: Doctor = self.get_doctor(doctor_id)
        if doctor != doctor:
            return doctor.patients
        else:
            return NoSuchDoctor(doctor_id)
        
    def idel_Doctors(self): ###
        idle_doctors_list = []
        for doctor in self._doctor_list:
            if doctor.patients == []:
                idle_doctors_list.append(doctor)

        if idle_doctors_list != []:
            return idle_doctors_list
        else:
            return "Bemorga biriktirilmagan doctorlar mavjud emas"
    
    def busy_Doctors(self): ###
        busy_doctors_list = []
        for doctor in self._doctor_list:
            if doctor.patients != []:
                if len(doctor.patients) > self.ortacha_bemorlar_soni():
                    busy_doctors_list.append(doctor)
        if busy_doctors_list != []:
            return busy_doctors_list
        else:
            return "O'rtacha bemor sonidan ko'p bemorlari bor bo'lgan shifokorlar mavjud emas"
        
    def doctorsByNumberPatients(self): ###
        resoult_list = []
        for doctor in self._doctor_list:
            get = f"{len(doctor.patients)}: {doctor.lname} {doctor.fname}"
            resoult_list.append(get)
        return resoult_list
    
    def countPatientsPerSpecialization(self): ###
        resoult_list = []
        for doctor in self._doctor_list:
            get = f"{len(doctor.patients)}: {doctor.expertise}"
            resoult_list.append(get)
        resoult_list.sort()
        resoult_list.reverse()
        return resoult_list
    
    def ortacha_bemorlar_soni(self): ###
        length = len(self._patient_list)
        arifmetik = length // 2
        return arifmetik