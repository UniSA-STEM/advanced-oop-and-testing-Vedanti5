'''
File: main.py
Description: A brief description of this Python module.
Author: Vedanti Ganjale
ID: 110439713
Username: ganvy010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
from Vet import Veterinarian
from staff import StaffMember
from zoo import Zoo

def main():
    print("\n=== TinyTown Zoo Demo ===\n")

    # Create the zoo manager
    zoo = Zoo("TinyTown Zoo")
    print(f"Created zoo: {zoo.name}\n")

    # Create animals
    leo = Animal("Leo", "Lion", "mammal", 5, "meat")
    polly = Animal("Polly", "Parrot", "bird", 2, "seeds")
    pingu = Animal("Pingu", "Penguin", "bird", 3, "fish")
    sally = Animal("Sally", "Seal", "mammal", 4, "fish")
    print("Created animals:", leo.name, polly.name, pingu.name, sally.name, "\n")

    # Add animals to the zoo registry
    zoo.add_animal(leo)
    zoo.add_animal(polly)
    zoo.add_animal(pingu)
    zoo.add_animal(sally)
    print()

    # Create enclosures
    lion_den = Enclosure("E1", 200, "savannah", "mammal", max_animals=3)
    aviary = Enclosure("E2", 80, "aviary", "bird", max_animals=6)
    seal_pool = Enclosure("E3", 120, "aquatic", "mammal", max_animals=2)  # seal classified as mammal in our simple model
    print("Created enclosures:", lion_den.id, aviary.id, seal_pool.id, "\n")

    # Add enclosures to zoo
    zoo.add_enclosure(lion_den)
    zoo.add_enclosure(aviary)
    zoo.add_enclosure(seal_pool)
    print()

    # Create staff
    alice = Zookeeper("Alice")
    dr_bob = Veterinarian("Dr Bob")
    zoo.add_staff(alice)
    zoo.add_staff(dr_bob)
    print()

    # Assign staff to animals/enclosures
    zoo.assign_staff_to_animal("Alice", "Leo")
    zoo.assign_staff_to_enclosure("Alice", "E1")
    zoo.assign_staff_to_animal("Dr Bob", "Leo")
    print()

    # Assign animals to enclosures
    print("Assign animals to enclosures:")
    zoo.assign_animal_to_enclosure("Leo", "E1")    # lion -> lion den
    zoo.assign_animal_to_enclosure("Polly", "E2")  # parrot -> aviary
    zoo.assign_animal_to_enclosure("Pingu", "E2")  # penguin -> aviary (works because category "bird")
    zoo.assign_animal_to_enclosure("Sally", "E3")  # seal -> seal_pool
    print()

    # Show enclosure statuses
    print("Enclosure statuses (after assignment):")
    for eid, status in zoo.enclosure_statuses().items():
        print(f" - {eid}: {status}")
    print()

    # Record a health issue for Leo (this will mark him under treatment and hide him from display)
    print("Recording a health issue for Leo:")
    leo.report_health_issue("Limping left paw", 40, treatment_plan="rest & anti-inflammatory", notes=["Seen limping by keeper"])
    print("Leo under_treatment:", leo.under_treatment)
    print()

    # Try daily routine (zookeeper will avoid feeding an animal under treatment)
    print("Running daily routine:")
    zoo.run_daily_routine()
    print()

    # Vet treats Leo
    print("Vet treating Leo now:")
    dr_bob.treat(leo, 0, notes="X-ray clear, continue rest")
    print("Leo under_treatment after treatment:", leo.under_treatment)
    print()

    # Reports
    print("Animals by species report:")
    print(zoo.animals_by_species())
    print()

    print("Enclosure statuses (final):")
    for eid, status in zoo.enclosure_statuses().items():
        print(f" - {eid}: {status}")
    print()

    print("Health report for all animals:")
    print(zoo.health_report_all())
    print()

    print("Demo finished.")

if __name__ == "__main__":
    main()