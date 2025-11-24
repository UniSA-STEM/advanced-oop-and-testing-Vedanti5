'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


class AnimalError(Exception):
    """Raised when something invalid happens with an animal."""
    pass


class Animal:
    def __init__(self, name, species, category, age, diet):
        self.name = name
        self.species = species
        self.category = category  # e.g. "mammal", "bird", "reptile"
        self.age = age  # simple number
        self.diet = diet  # e.g. "meat", "plants", "fish"

        # health info
        self.under_treatment = False
        self.health_issues = []

    def report_health_issue(self, description, severity):
        """Add a health issue and mark the animal as under treatment."""
        if severity < 1 or severity > 100:
            raise AnimalError("Severity must be between 1 and 100.")

        self.health_issues.append({
            "description": description,
            "severity": severity
        })
        self.under_treatment = True

    def resolve_health(self):
        """Clear all issues and mark animal as healthy."""
        self.health_issues = []
        self.under_treatment = False

    def make_sound(self):
        """Return a generic sound."""
        return f"{self.name} the {self.species} makes a sound."

    def eat(self):
        return f"{self.name} is eating {self.diet}."

    def sleep(self):
        return f"{self.name} is sleeping now."

    def get_info(self):
        """Return simple details about the animal."""
        return {
            "name": self.name,
            "species": self.species,
            "category": self.category,
            "age": self.age,
            "diet": self.diet,
            "under_treatment": self.under_treatment,
            "health_issues": self.health_issues
        }