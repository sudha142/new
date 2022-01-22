import re
pattern="cookie"
sequence="cookie"
if re.match(pattern,sequence):
    print("Match...!")
else:
    print("Not a match...!")