'''
File: zookeeper.py
Description: A brief description of this Python module.
Author110439713
Username: ganvy010
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import StaffMember
class Zookeeper(StaffMember):
    def __init__(self, name):
        super().__init__(name, role="zookeeper")

    # zookeeper-specific convenience methods could be added here
