import sys

if __name__ == 'main':
	print("=== Analyse du Système d'Inventaire ===")
	inventory: dict[str, int] = {}

	index: int = 1
	for arg in sys.argv[1:]:
		item = arg.split(':')[0]
		index = index + 1

		if item in sys.argv[index:]:

		if len(item) != 2:
			print("Error - invalid parameter 'hello')

# Redundant item 'sword' - discardin
# Error - invalid parameter 'hello'
# Quantity error for 'key': invalid literal for int() with base 10: 'value'
# Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
# Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
# Total quantity of the 5 items: 12
