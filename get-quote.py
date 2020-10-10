import random
def sport:

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  q = random.randint(0, last)
  print(quotes[q])

if __name__== "__main__":
  sport()
