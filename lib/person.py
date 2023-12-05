#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:

    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

# Example usage:
#person1 = Person("john doe", "Engineer")
#print(person1.name)  # Output: John Doe
#print(person1.job)   # Output: Engineer

#person2 = Person("Jane Smith", "Artist")
#print(person2.name)  # Output: Jane Smith
#print(person2.job)   # Output: Artist

#person3 = Person("Bob Johnson", "Pilot")  # Output: Job must be in the list of approved jobs.
#person3.name = "ThisIsAVeryLongNameForAPerson"  # Output: Name must be a string under 25 characters.

