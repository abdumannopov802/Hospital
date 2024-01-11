class NoSuchPatient(Exception):
    def __init__(self, ssn) -> None:
        self._ssn = ssn
        self._message = f"{ssn} -> SSN bemor topilmadi"
        super().__init__(self._message)

class NoSuchDoctor(Exception):
    def __init__(self, id) -> None:
        self._ssn = id
        self._message = f"{id} -> ID doctor topilmadi"
        super().__init__(self._message)