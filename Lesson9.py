class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

       
       
p1 = parrot("Polly", 5)
p2 = parrot("Molly", 3)
print('the species of the bbird is', p1.species)
print('the name of the parrot is', p1.name, 'The age of the parrot is', p1.age)
print('the name of the parrot is', p2.name, 'The age of the parrot is', p2.age)