'''CSC11 Project'''
from __future__ import annotations
from typing import Optional

class Disease:
    name: str
    symptoms: Optional[list]
    def __init__(self, name) -> None:
        """Initialize this disease """
        self.name = name
        self.symptoms = []

class Symptom:
    name = str
    diseases = Optional[list]

    def __init__(self, name) -> None:
        """Initialize this symptom """
        self.name = name
        self.diseases = []

    def connect_disease(self, disease: Disease):
        disease.symptoms.append(self)
        self.diseases.append(disease)

class FIN_GRAPH:
    diseases = list
    symptoms: list

    def __init__(self) -> None:
        """Initialize an empty FIN_GRAPH."""
        self.diseases = []
        self.symptoms = []

    def add_symptom(self, symp):
        symptom = Symptom(symp)
        self.symptoms.append(symptom)
        # return symptom -> could return the symptom too if we wish to first store the disease in a variable while
        # reading the file and then create a channel between each symptom and the disease

    def add_disease(self, dis):
        disease = Disease(dis)
        self.diseases.append(disease)

    # def connect_symptoms(self, symp1):
    #     for i in self.symptoms:
    # got stuck here
