"""CSC111 Project

Title: Am I Infected?
Group Members: Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal

This module contains a collection of Python classes that will be used to ultimately model a graph that stores all data
regarding symptoms and diseases and includes methods to diagnose diseases.

Copyright and Usage Information
===============================

This file is Copyright (c) 2023 Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal.
"""
from __future__ import annotations
from typing import Optional

# TODO - update Representation Invariants


class Symptom:
    """A node that represents a particular symptom

    Instance Attributes:
    - description:
        The one to two word name or description of the given symptom
    - connected_symptoms
        A mapping where the key is the name of a symptom and the value is a connection between the two symtpoms
    - connected_diseases
        A mapping where the key is the name of a disease and the value associaed is a connection between
        the symtom and the disease

    Representation Invariants:
    - name != ''

    """
    description: str
    connected_symptoms: dict[str, SymptomConnect]
    connected_diseases: dict[str, DiseaseConnect]
    # Instance Attributes to Consider:
    # severity
    # precautions

    def __init__(self, desc: str):
        self.description = desc
        self.connected_symptoms = {}
        self.connected_diseases = {}

    def add_symptom(self, symptom: Symptom) -> None:
        """Add symptom to the symptom's connections"""
        if symptom not in self.connected_symptoms:
            self.connected_symptoms[symptom.description] = SymptomConnect(self, symptom)

    def add_disease(self, disease: Disease) -> None:
        """Add disease to the symptom's connections"""
        if disease not in self.connected_symptoms:
            self.connected_diseases[disease.description] = DiseaseConnect(self, disease)


class Disease:
    """A node that represents a particular disease

    Instance Attributes:
    - description:
        The one to two word name or description of the given disease
    - connected_symptoms:
        A mapping where the key is the name of a symptom and the value associaed is a connection between
        the disease and its symptom

    Representation Invariants:
    - name != ''

    """
    description: str
    connected_symptoms: dict[str, DiseaseConnect]
    # Instance Attributes to Consider:
    # severity
    # precautions / cures

    def __init__(self, desc: str):
        self.description = desc
        self.connected_symptoms = {}

    def add_symptom(self, symptom: Symptom) -> None:
        """Add symptoms to the disease's connections"""
        if symptom not in self.connected_symptoms:
            self.connected_symptoms[symptom.description] = DiseaseConnect(symptom, self)


class SymptomConnect:
    """To establish a connection between two symptoms"""
    symptom_node1: Symptom
    symptom_node2: Symptom

    def __init__(self, symptom1: Symptom, symptom2: Symptom) -> None:
        self.symptom_node1 = symptom1
        self.symptom_node2 = symptom2


class DiseaseConnect:
    """To establish a connection between a symptom and a disease

    Instance Attributes:
    - symptom_node:
    Stores the name of the symptom
    - disease_node:
    """
    symptom_node: Symptom
    disease_node: Disease

    def __init__(self, symptom: Symptom, disease: Disease):
        self.symptom_node = symptom
        self.disease_node = disease


class UserData:
    """Stores all data for a particular user

    Instance Attributes
    - current_symptom:
    last symptom input by the user
    - symptoms:
    collection of all symptoms the user is experiencing
    """
    current_symptom: Optional[str]
    symptoms: list[str]

    def __init__(self) -> None:
        self.current_symptom = None
        self.symptoms = []

    def load_symptom(self, symptom: str) -> None:
        """Add the symptom tothe user's symptoms

        Preconditions:
        - symptom not in self.symptoms
        """
        self.symptoms.append(symptom)

    def calculate_probabilities(self, disease: list[Disease], plot: bool = True) -> dict[str, float]:
        """Based on the list of diseases (suggested by the diagnostic graph) calculate the probabilities by comparing
        the symptoms of the diseases with the symptoms input by the user
        """

    def plot_statistice(self, stats: dict[str, float]) -> None:
        """Plot the probabilities of diseases based on the calculations"""
