Hash_Star = input()
no_hash = 0
no_star = 0
for i in Hash_Star:
    if i == "#":
        no_hash += 1
    else:
        no_star += 1
if no_star > no_hash:
    print(no_star - no_hash)
elif no_hash > no_star:
    print(no_star - no_hash)
else:
    print(no_star - no_hash)