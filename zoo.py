'''
File: zoo.py
Description: A brief description of this Python module.
Author: Vedanti Ganjale
ID: 110439713
Username: ganvy010
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = {}     # name -> Animal
        self.enclosures = {}  # id -> Enclosure
        self.staff = {}       # name -> StaffMember

    # --- CRUD ---
    def add_animal(self, animal):
        if animal.name in self.animals:
            print(f"[Zoo] Animal {animal.name} already exists.")
            return False
        self.animals[animal.name] = animal
        print(f"[Zoo] Added animal {animal.name}.")
        return True

    def remove_animal(self, name):
        a = self.animals.get(name)
        if not a:
            print(f"[Zoo] No animal named {name}.")
            return False
        if a.under_treatment:
            print(f"[Zoo] Cannot remove {name}: under treatment.")
            return False
        # remove from enclosures
        for e in self.enclosures.values():
            e.remove_animal(name)
        # remove from staff assignments
        for s in self.staff.values():
            s.assigned_animals = [x for x in s.assigned_animals if x.name != name]
        del self.animals[name]
        print(f"[Zoo] Removed animal {name}.")
        return True

    def add_enclosure(self, enclosure):
        if enclosure.id in self.enclosures:
            print(f"[Zoo] Enclosure {enclosure.id} already exists.")
            return False
        self.enclosures[enclosure.id] = enclosure
        print(f"[Zoo] Added enclosure {enclosure.id}.")
        return True

    def remove_enclosure(self, enclosure_id):
        e = self.enclosures.get(enclosure_id)
        if not e:
            print(f"[Zoo] No enclosure {enclosure_id}.")
            return False
        if len(e.animals) > 0:
            print(f"[Zoo] Cannot remove enclosure {enclosure_id}: animals inside.")
            return False
        del self.enclosures[enclosure_id]
        print(f"[Zoo] Removed enclosure {enclosure_id}.")
        return True

    def add_staff(self, staff_member):
        if staff_member.name in self.staff:
            print(f"[Zoo] Staff {staff_member.name} already exists.")
            return False
        self.staff[staff_member.name] = staff_member
        print(f"[Zoo] Added staff {staff_member.name} ({staff_member.role}).")
        return True

    def remove_staff(self, name):
        if name not in self.staff:
            print(f"[Zoo] No staff named {name}.")
            return False
        del self.staff[name]
        print(f"[Zoo] Removed staff {name}.")
        return True

    # --- assignments ---
    def assign_animal_to_enclosure(self, animal_name, enclosure_id):
        animal = self.animals.get(animal_name)
        enclosure = self.enclosures.get(enclosure_id)
        if not animal:
            print(f"[Zoo] No animal {animal_name}.")
            return False
        if not enclosure:
            print(f"[Zoo] No enclosure {enclosure_id}.")
            return False
        result = enclosure.add_animal(animal)
        return result

    def assign_staff_to_animal(self, staff_name, animal_name):
        staff = self.staff.get(staff_name)
        animal = self.animals.get(animal_name)
        if not staff or not animal:
            print(f"[Zoo] staff or animal not found.")
            return False
        staff.assign_animal(animal)
        return True

    def assign_staff_to_enclosure(self, staff_name, enclosure_id):
        staff = self.staff.get(staff_name)
        enclosure = self.enclosures.get(enclosure_id)
        if not staff or not enclosure:
            print(f"[Zoo] staff or enclosure not found.")
            return False
        staff.assign_enclosure(enclosure)
        return True

    # --- scheduling / daily routine ---
    def run_daily_routine(self):
        print(f"[Zoo] Running daily routine for {self.name}...")
        # zookeepers feed their animals and clean their enclosures
        for s in self.staff.values():
            if s.role == "zookeeper":
                for a in s.assigned_animals:
                    s.feed(a)
                for e in s.assigned_enclosures:
                    s.clean(e)
            if s.role == "veterinarian":
                for a in s.assigned_animals:
                    s.perform_health_check(a)
        print("[Zoo] Daily routine finished.")

    # --- reports ---
    def animals_by_species(self):
        result = {}
        for a in self.animals.values():
            result.setdefault(a.species, []).append(a.name)
        return result

    def enclosure_statuses(self):
        return {eid: e.report_status() for eid, e in self.enclosures.items()}

    def health_report_for_animal(self, animal_name):
        a = self.animals.get(animal_name)
        if not a:
            print(f"[Zoo] No animal {animal_name}.")
            return None
        return a.get_health_report()

    def health_report_all(self):
        return {name: a.get_health_report() for name, a in self.animals.items()}
