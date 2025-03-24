"""
Created on Monday March 24 14:25:41 2025
@author: Kimia Ketabforoosh
"""

# measure ASCII code
names = ["Kimia", "Sarah", "Alison", "Marcus", "Albert"]
for name in names:
    hash = 0
    for c in name:
        hash += ord(c)

    print(name, hash % 10)
