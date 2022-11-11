#imported modules and submodules
import os


# Find illegal characters in string function
# better than the MATLAB version, this can be outsourced to a function
# rather than staying in main(). Uses two-dimensional iterative loop
# to match a list of 'verboten' characters to the specific element.
# in the source array. At the conclusion of the loop, the string
# should have only alphanumeric characters contained in it, and no
# whitespaces whatsoever 


destinationFile = "th}is i@s ou$r p{ro/%tot[ype st)rin*g"
illegalCharList = """!@#$%^&*()<>,./:;|"'{}[]+=?"""

print(destinationFile+"\n")
list_dF = list(destinationFile)

for i in range(0, len(list_dF)):
    for j in range(0, len(illegalCharList)):
        if(list_dF[i] == illegalCharList[j]):
            print("found illegal '{}' at index #{}, now removing.".format(illegalCharList[j], i))
            list_dF[i] = ''



destinationFile = ''.join(list_dF)
print(destinationFile)            


          


