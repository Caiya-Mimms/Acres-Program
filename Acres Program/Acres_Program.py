# Caiya Mimms | Jan 21,2023
# Acres_Program | HW #3
# Calculates Sq ft to Acres (User Input)

    
    #Welcome text
print("Welcome! This program will convert sqaure feet into arce(s)")
    #Input converted to int to be calculated later! Name 'S' for sqaure feet
S = int(input("Enter the square feet of your land: "))

    # 'A' is the the equivalent of one acre
A = 43560
    # Named 'C' Convertion
C = S/A

    # Round off decimal to the 2nd place
rn_C =round(C*100.00)/100.00

    #Output
print("Your land is ",rn_C,"acre(s)!")
print("Program end.")



