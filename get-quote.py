import random

def funcion():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  nueva_frase = "Another sentence for the program"
  nueva_frase_2 = "A second sentence"
  final_frase = "One final sentence"
  quotes.append(nueva_frase)
  quotes.append(nueva_frase_2)
  quotes.append(final_frase)
  for frase in quotes:
    formateada = frase.rstrip()
    print (formateada)
  #f.close()
  #last = 14
  #rnd = random.randint(0, last)
  #print(quotes[14], "\n", quotes[15], "\n", quotes[16], sep="")

if __name__== "__main__":
  funcion()
