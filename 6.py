print("alifasttahi")

vazn_be_pound = float(input ( "chand pound seyd kardi ?"))

# tabdil be kiloqram

vazn_be_kg =vazn_be_pound * 0.453
gheymat_be_dollar = vazn_be_kg * 2

if gheymat_be_dollar >= 5 :
    print ("Bravo ! your gift is Fishing hooks ! ")
    print ( "fisher man caught" , vazn_be_kg , "kilograms!")
    print ( "you have to give the fisherman " , gheymat_be_dollar , "dollars")
else :
    gheymat_be_dollar < 5 
    print (" You failed try again and keep trying ")
    print ( "fisher man caught" , vazn_be_kg , "kilograms!")
    print ( "you have to give the fisherman " , gheymat_be_dollar , "dollars!")
