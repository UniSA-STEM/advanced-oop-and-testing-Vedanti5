'''
File: staff.py
Description: A brief description of this Python module.
Author: Vedanti Ganjale
ID: 110439713
Username: ganvy010
This is my own work as defined by the University's Academic Integrity Policy.
'''

class StaffMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role     # e.g., "zookeeper", "veterinarian", "manager"
        self.assigned_animals = []     # list of Animal objects
        self.assigned_enclosures = []  # list of Enclosure objects

    def assign_animal(self, animal):
        if animal not in self.assigned_animals:
            self.assigned_animals.append(animal)
            print(f"[Staff {self.name}] Assigned to animal {animal.name}.")

    def assign_enclosure(self, enclosure):
        if enclosure not in self.assigned_enclosures:
            self.assigned_enclosures.append(enclosure)
            print(f"[Staff {self.name}] Assigned to enclosure {enclosure.id}.")

    def clean(self, enclosure, effort=10):
        # generic staff cleaning - zookeepers should use this
        if enclosure.clean(effort):
            print(f"[Staff {self.name}] cleaned enclosure {enclosure.id}.")
            return True
        return False

    def feed(self, animal):
        # generic feed - zookeepers override or use this
        if animal.under_treatment:
            print(f"[Staff {self.name}] Not feeding {animal.name} normally: animal under treatment.")
            return False
        print(f"[Staff {self.name}] fed {animal.name}.")
        return True

    def perform_health_check(self, animal):
        # generic check - veterinarians can call this
        info = animal.get_health_report()
        print(f"[Staff {self.name}] Health check for {animal.name}: {len(info['issues'])} issues, under_treatment={info['under_treatment']}.")
        return info




