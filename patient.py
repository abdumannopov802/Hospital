class Patient:
    def __init__(self, f_name, l_name, ssn) -> None:
        self._f_name = f_name
        self._l_name = l_name
        self._ssn = ssn
        self._doctor = None

    @property
    def lname(self):
        return self._f_name
    
    @property
    def fname(self):
        return self._f_name

    @property
    def ssn(self):
        return self._ssn
    
    @property
    def doctor(self):
        return self._doctor