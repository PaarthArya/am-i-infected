"""CSC111 Project

Title: Am I Infected?
Group Members: Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal

This module contains the Python Class that is used to store, model and compute all data in relation to diseases and
their symptoms.

Copyright and Usage Information
===============================

This file is Copyright (c) 2023 Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal.
"""

from structural_nodes import Disease, Symptom, SymptomConnect, UserData
from typing import Optional

# TODO - update Representation Invariants


class DiseaseDiagnostic:
    """GRAPH OF DISEASES

    Instance Attributes:
    - _disease_nodes
    Collection of all diseases in this diagnostic software
    - _symptom_nodes
    Colletion of all symptoms in this diagnostic software
    - _current_symptom
    The last symptom input by the current user
    """
    _disease_nodes: dict[str, Disease]
    _symptom_nodes: dict[str, Symptom]
    _current_symptom: Optional[str]

    def __init__(self):
        self._disease_nodes = {}
        self._symptom_nodes = {}
        _current_symptom = None

    def load_disease_data(self, disease_data_file: str) -> None:
        """Load the disease data from the disease_data_file onto the disease_nodes

        Preconditions:
        - disease_data_file != ''
        """

    def load_syptom_data(self, symptom_data_file: str) -> None:
        """Load the disease data from the disease_data_file onto the disease_nodes

        Preconditions:
        - symptom_data_file != ''
        """

    def next_symptom_path(self, user: UserData, next_symptom: str) -> SymptomConnect:
        """Returns the connection from the user's current symptom to the next symptom

        If required number of symptoms have been covered, call next_diseases_path to return list of possible diseases
        """
        # Call UserData.load_symptom

    def next_diseases_path(self, user: UserData) -> list[Disease]:
        """Returns a list of all possible diseases based on input systems"""
        # Remember to reinitialise self._current_symptom to None once the current user's symptom data has been resolved
