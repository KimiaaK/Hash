"""
Created on Monday March 24 14:25:41 2025
@author: Kimia Ketabforoosh
"""

import hashlib

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
m = hashlib.sha256()
data = "my name is Kimia and 123456 is my student ID"

print("-----------------------------------")

i = 0
while True:
    current_data = data + str(i)
    m = hashlib.md5()  # create a new hash object each time
    m.update(current_data.encode("utf-8"))  # do NOT assign m = m.update()
    hash = m.hexdigest()
    # print(hash[-4:])

    if hash[-4:] == "1111":
        print(f"Found it! The string is {current_data} and the hash is {hash}")
        break
    else:
        i += 1  # keep searching
# i = 0
# while True:
#     data = data + str(i)
#     m = m.update(data.encode("utf-8"))
#     hash = m.hexdigest()
#     print(hash[-4:])

#     if hash[-4:] == "1111":
#         print(f"Found it! the string is {data} and the hash is {hash}")
#     else:
#         print(hash)
#         break
