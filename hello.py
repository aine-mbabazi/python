def hello():
    print("Hello Akirachix")

    # functional arguments
def hello(name):
        print(f"Hello {name}")
def year_of_birth(name,age):
     print(f"Hello {name}, was born in {2024-age}")
# Default Arguments
def my_country(country="Uganda"):
      print(f"Hello AkiraChix from {country}")

def greet(*names):
    for name in names:
         print(f"Hello {names}")
         
# A function that takes a number of keyword arguments
def create_sentence(**words):
    print (words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence
# A function that accepts any number of positional arguments and key words
