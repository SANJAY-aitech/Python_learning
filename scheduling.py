''' this program is about scheduling, instead of using Input function we can use sys.argv '''

import sys


if len(sys.argv) == 2:
    print("Usage:'Full Name and Last Name'")
    sys.exit()

full_name = " ".join(sys.argv[1:])


email = full_name.lower().replace(" ",".")+ "@company.com"

print("\n ---- Your Profile ----")
print("Full Name: ",full_name)  
print("Generated Email:",email)