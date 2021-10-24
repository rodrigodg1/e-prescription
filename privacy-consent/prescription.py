

class Prescription:
    
    def __init__(self,personal_id,medication,diagnosis):
        self.personal_id = personal_id
        self.medication = medication
        self.diagnosis = diagnosis
        
    def get_personal_id(self):
        return self.personal_id
    
    def get_medication(self):
        return self.medication
    
    def get_diagnosis(self):
        return self.diagnosis
    
    
    #return all prescription items
    def get_prescription(self):
        return self.personal_id, self.medication, self.diagnosis