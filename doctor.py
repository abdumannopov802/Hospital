from patient import Patient

class Doctor(Patient):
    def __init__(self, f_name, l_name, ssn, id, expertise) -> None:
        super().__init__(f_name, l_name, ssn)
        self._id = id
        self._expertise = expertise
        self._patients_list: list[Patient] = []

    def add_patient(self, patient):
        self._patients_list.append(patient)
        return self._patients_list
    
    def get_patient(self, patient_ssn):
        for patient in self._patients_list:
            if patient.ssn == patient_ssn:
                return f"{patient.ssn}-SSN bemorga biriktirilgan doctor -> {patient._ssn}"

    @property
    def lname(self):
        return self._l_name
    
    @property
    def fname(self):
        return self._f_name

    @property
    def ssn(self):
        return self._ssn
    
    @property
    def id(self):
        return self._id
    
    @property
    def patients(self):
        return self._patients_list
    
    @property
    def expertise(self):
        return self._expertise