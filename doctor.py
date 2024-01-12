from typing import Any
from patient import Patient

class Doctor(Patient):
    def __init__(self, f_name, l_name, ssn, id, expertise) -> None:
        super().__init__(f_name, l_name, ssn)
        self._id = id
        self._expertise = expertise

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
    def id(self):
        return self._id

    @property
    def expertise(self):
        return self._expertise
