from datetime import date

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def is_eligible_to_vote(self):
        age = self.calculate_age()
        if age >= 18:
            return True
        else:
            return False

# Example usage
person1 = Person("John Doe", date(2004, 5, 2))
print(f"{person1.name} is {person1.calculate_age()} years old.")
if person1.is_eligible_to_vote():
    print(f"{person1.name} is eligible to vote.")
else:
    print(f"{person1.name} is not eligible to vote yet.")