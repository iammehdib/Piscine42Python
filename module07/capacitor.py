from ex1 import HealingCreatureFactory, TransformCreatureFactory

print("Testing Creature with healing capability")
healing = HealingCreatureFactory()

print(" base:")
sprout = healing.create_base()
print(sprout.describe())
print(sprout.attack())
print(sprout.heal())

print(" evolved:")
bloom = healing.create_evolved()
print(bloom.describe())
print(bloom.attack())
print(bloom.heal())

print("")
print("Testing Creature with transform capability")
transform = TransformCreatureFactory()

print(" base:")
shift = transform.create_base()
print(shift.describe())
print(shift.attack())
print(shift.transform())
print(shift.attack())
print(shift.revert())

print(" evolved:")
morph = transform.create_evolved()
print(morph.describe())
print(morph.attack())
print(morph.transform())
print(morph.attack())
print(morph.revert())
