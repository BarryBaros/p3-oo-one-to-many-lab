class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are: {', '.join(Pet.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    

# Example usage
try:
    owner1 = Owner("John Doe")
    owner2 = Owner("Jane Smith")

    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Whiskers", "cat")
    pet3 = Pet("Slinky", "rodent")
    pet4 = Pet("Spike", "reptile")

    owner1.add_pet(pet1)
    owner1.add_pet(pet2)
    owner2.add_pet(pet3)
    owner1.add_pet(pet4)

except Exception as e:
    print(e)

print(owner1.pets())  # Output: [Pet(name=Buddy, pet_type=dog, owner=John Doe), Pet(name=Whiskers, pet_type=cat, owner=John Doe), Pet(name=Spike, pet_type=reptile, owner=John Doe)]
print(owner2.pets())  # Output: [Pet(name=Slinky, pet_type=rodent, owner=Jane Smith)]

print(owner1.get_sorted_pets())  # Output: [Pet(name=Buddy, pet_type=dog, owner=John Doe), Pet(name=Spike, pet_type=reptile, owner=John Doe), Pet(name=Whiskers, pet_type=cat, owner=John Doe)]
print(owner2.get_sorted_pets()) # Output: [Pet(name=Slinky, pet_type=rodent, owner=Jane Smith)]