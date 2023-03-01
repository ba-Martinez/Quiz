# Definindo a string a ser invertida
string = "O rato roeu a roupa do rei de Roma"

# Invertendo os caracteres da string
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprimindo a string invertida
print(f"{string_invertida}")
