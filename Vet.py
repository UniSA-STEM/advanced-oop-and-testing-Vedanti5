'''
File: Vet.py
Description: A brief description of this Python module.
Author: Vedanti Ganjale
ID: 110439713
Username: ganvy010
This is my own work as defined by the University's Academic Integrity Policy.
'''
from datetime import date
from staff import StaffMember
class Veterinarian(StaffMember):
    def __init__(self, name):
        super().__init__(name, role="veterinarian")

    def treat(self, animal, issue_index=0, notes=None):
        """Treat an animal by adding notes and resolving or updating treatment plan."""
        if 0 <= issue_index < len(animal.health_issues):
            if notes:
                animal.health_issues[issue_index]["notes"].append(notes)
            # example: mark resolved and update flags
            animal.under_treatment = False
            animal.displayed = True
            animal.health_issues[issue_index]["resolved"] = True
            animal.health_issues[issue_index]["resolved_date"] = date.today().isoformat()
            print(f"[Vet {self.name}] Treated {animal.name}, issue #{issue_index} marked resolved.")
            return True
        print(f"[Vet {self.name}] No such issue index {issue_index} for {animal.name}.")
        return False
