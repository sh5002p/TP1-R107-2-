a = int(input("Entrez la première valeur : "))
b = int(input("Entrez la deuxième valeur : "))
c = int(input("Entrez la troisième valeur : "))
print("Les valeurs entrees sont : a = ",a,", b = ",b," et c = ",c)
print("Permuation : a ==> b, b ==> c, c ==> a")
a, b, c = c, a, b
print("Les valeurs permutees sont : a = ",a,", b = ",b,"et c = ",c)