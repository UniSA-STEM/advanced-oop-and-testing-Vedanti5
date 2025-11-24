'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


class EnclosureError(Exception):
    """Custom error for enclosure problems."""
    pass


class Enclosure:
    def __init__(self, id, size_sqm, environment, allowed_category, max_animals=None):
        self.id = id
        self.size_sqm = size_sqm
        self.environment = environment
        self.allowed_category = allowed_category
        self.cleanliness = 100.0
        self.animals = []
        self.max_animals = max_animals

    def add_animal(self, animal):
        """Add an animal to the enclosure if rules are ok."""
        # rule 1: environment/category must match
        if animal.category != self.allowed_category:
            raise EnclosureError(
                f"Cannot add {animal.name}. "
                f"This enclosure only accepts {self.allowed_category} animals."
            )

        # rule 2: animal not under treatment
        if hasattr(animal, "under_treatment") and animal.under_treatment:
            raise EnclosureError(
                f"{animal.name} is under treatment and cannot be moved."
            )

        # rule 3: capacity
        if self.max_animals is not None and len(self.animals) >= self.max_animals:
            raise EnclosureError("Enclosure is full.")

        # passed all checks → add
        self.animals.append(animal)

    def remove_animal(self, animal_name):
        """Remove an animal by name."""
        for a in self.animals:
            if a.name == animal_name:

                # cannot remove if under treatment
                if hasattr(a, "under_treatment") and a.under_treatment:
                    raise EnclosureError(
                        f"{a.name} is under treatment and cannot be removed."
                    )

                self.animals.remove(a)
                return a

        raise EnclosureError(f"No animal named {animal_name} in this enclosure.")

    def list_animals(self):
        """Return animal names with species."""
        names = []
        for a in self.animals:
            names.append(f"{a.name} ({a.species})")
        return names

    def clean(self, effort=10):
        """Increase cleanliness by a small amount (max 100)."""
        if effort <= 0:
            raise ValueError("Cleaning effort must be positive.")

        self.cleanliness += effort
        if self.cleanliness > 100:
            self.cleanliness = 100  # cap at 100

    def report_status(self):
        """Return a dictionary with enclosure info."""
        return {
            "id": self.id,
            "environment": self.environment,
            "allowed_category": self.allowed_category,
            "cleanliness": self.cleanliness,
            "animals": self.list_animals(),
            "max_animals": self.max_animals,
            "current_count": len(self.animals)
        }

