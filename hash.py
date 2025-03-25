"""
Created on Monday March 24 14:25:41 2025
@author: Kimia Ketabforoosh
"""

# -----hash table-----
# measure ASCII code
names = ["Kimia", "Sarah", "Alison", "Marcus", "Albert"]
for name in names:
    hash = 0
    for c in name:
        hash += ord(c)

    print(name, hash % 10)
# Still not the best option for the hash because it might group people in the same group.


# -----SHA256 Brute Force-----
import hashlib
