"""CSC111 Project

Title: Am I Infected?
Group Members: Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal

This module contains methods to input information from data files about diseases and symptoms and take inputs from
user's about their health information.

Copyright and Usage Information
===============================

This file is Copyright (c) 2023 Avni Agrawal, Aina Merchant, Paarth Arya, Reeya Bansal.
"""
from diagnostic_graph import DiseaseDiagnostic
from structural_nodes import UserData

# TODO - update Representation Invariants


class Runner:
    """Runner to bring together all data classes

    Representation Invariants:
    - diagnostic_graph:
    Graph of disease and symptom data
    - users:
    List of users that have used the software so far

    """
    diagnostic_graph: DiseaseDiagnostic
    users: list[UserData]

    def load_diagnostic_graph(self, disease_data_file: str, symptom_data_file: str) -> None:
        """Initialise diagnostic_graph"""
        # Call load method from DiseaseDiagnostic to load data

    def runner(self) -> None:
        """Run the whole software"""
        # 1. Create UserData's object
        # 2. Take inputs of symptoms and call DiseaseDiagnostic.next_symptom_path and
        # DiseaseDiagnostic.next_diseases_path to progress through our diagnostic_graph
        # 3. Input more symptoms from the user, if any, after the diseases list is returned and call
        # UserData.load_symptom to add symptoms to the user
        # 4. When list of diseases is returned by DiseaseDiagnostic.next_diseases_path, call
        # UserData.calculate_probabilities to get probabilities and plot them
