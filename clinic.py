from patient import Patient
from exceptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor

class Clinic:
    def __init__(self, name) -> None:
        self._name = name
        self._patient_list: list[Patient] = []
        self._doctor_list: list[Doctor] = []
        self._patient_assigned_doctor = []
    
    @property
    def patient_to_doctor(self):
        for i in range(len(self._patient_assigned_doctor)):
            yield dict(self._patient_assigned_doctor[i])

    def add_patient(self, new_patient:Patient):
        self._patient_list.append(new_patient)
        return new_patient, "Bemor qo'shildi"

    def get_patient(self, ssn):
        for person in self._patient_list:
            if person.ssn == ssn:
                return person, "Bemor bor"
        else:
            return NoSuchPatient
    
    def add_doctor(self, new_doctor:Doctor):
        self._doctor_list.append(new_doctor)
        return new_doctor, "Doctor qo'shildi"
    
    def get_doctor(self, id):
        for doctor in self._doctor_list:
            if doctor.id == id:
                return doctor, "Doctor bor"
        else:
            return NoSuchPatient
    
    # def new_func(self, patient_ssn, doctor_id):
    #     while next(patient.ssn == patient_ssn for patient in self._patient_list):
    #         while next(doctor.id == doctor_id for doctor in self._doctor_list):
    #             for patient in self._patient_list:
    #                 if patient.ssn == patient_ssn:
    #                     yield patient.ssn
    #                     for doctor in self._doctor_list:
    #                         if doctor.id == doctor_id:
    #                             yield doctor.id
    #                             get = {patient.ssn: doctor.id}
    #         return NoSuchDoctor
    #     self._patient_assigned_doctor.append(get)
    #     return get, "Bemor docktorga biriktirildi"

    def assign_Patient_to_Doctor(self, patient_ssn:Patient.ssn, doctor_id:Doctor.id):
        for patient in self._patient_list:
            # if next(patient.ssn == patient_ssn for patient in self._patient_list):

                if patient.ssn == patient_ssn:
                    for doctor in self._doctor_list:

                        if doctor.id == doctor_id:
                            get = {patient_ssn : doctor_id}
                        # else:
                        #     return NoSuchDoctor, "Doctor topilmadi"
            # else:
            #     return NoSuchPatient, "Bemor topilmadi"
              
        self._patient_assigned_doctor.append( get )
        return get, "Bemor doctorga biriktirildi"
        
    def get_Doctor(self, patient_ssn):
        for i in range(len(self._patient_assigned_doctor)):
            assigned_info =  dict(self._patient_assigned_doctor[i])
            for ssn in assigned_info:
                if ssn == patient_ssn:
                    return f"{ssn}-SSNga biriktirilgan shifokor -> ID{assigned_info[ssn]}"
        return NoSuchPatient
    
    def get_Patients(self, doctor_id):
        res = []
        for i in range(len(self._patient_assigned_doctor)):
            assigned_info = dict(self._patient_assigned_doctor[i])
            for id in assigned_info:
                if assigned_info[id] == doctor_id:
                    get = f"{assigned_info[id]}_ID shifokoriga biriktirilgan bemor {id}-SSN"
                    res.append(get)
        if res == []:
            return NoSuchDoctor
        else:
            return res