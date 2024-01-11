class Patient:
    def __init__(self, f_name, l_name, ssn) -> None:
        self._f_name = f_name
        self._l_name = l_name
        self._ssn = ssn

    # def get_Doctor(self, patient_ssn):
    #     return Clinic.get_Doctor(Clinic, patient_ssn)

    @property
    def lname(self):
        return self._f_name
    
    @property
    def fname(self):
        return self._f_name

    @property
    def ssn(self):
        return self._ssn