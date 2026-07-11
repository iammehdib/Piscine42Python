import alchemy

print(rf"""=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: {alchemy.create_air()}
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth: """, end='')
print(f"{alchemy.create_earth()}")
