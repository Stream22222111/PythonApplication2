arv=input("Sisesta arv")
if arv.isalpha():
    print(
        "See on tekst")
elif arv.isdigit():
    arv=int(arv)
    if arv>0:
        if arv%2==0:
            print(f"{arv} on paaris arv")
        else:
            print(f"{arv} on paaritu arv")
    else:
        print(f"{arv}-ei sobi")
else:
    print(f"{arv}-segatud tekst ja numbrid")





