from libs import rumusMatematika
bangun_datar = rumusMatematika.bangun_datar

def userInput():
  for option, showList in enumerate(bangun_datar, start=1):
    print(f"{option}. {showList[0].title()}");

if __name__ == '__main__':
  userInput()