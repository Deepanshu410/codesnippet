import numpy as np

rng = np.random.default_rng() # np.random.default_rng(seed=1), setting a seed reproduces same results, not necessary 

print(rng.integers(low=1, high=7, size=(3, 2))) # second argument is exclusive, size=(row, column)

#floating point number:
print(np.random.uniform(low=-1, high=1, size=(3,2))) # uniform means every number has an equal chance of being selected

# Shuffling an array:
array = np.array([1,2,4,5]) 
rng.shuffle(array)
print(array)

# random choice:
fruits = np.array(["apple", "banana", "coconut", "pinapple"])
fruit = rng.choice(fruits, size=2)
print(fruit)
