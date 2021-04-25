import re
pattern=r"spam"
if(re.match(pattern,"eggspamsausagespam")):
    print("Match")
else:
    print("No Match")

if re.search(pattern,"eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern,"eggspamsausagespam"))
for x in re.finditer(pattern,"eggspamsausagespam"):
    print(x.string)
