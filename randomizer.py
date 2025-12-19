#First program will generate a random number between 2 set numbers.
#This number is based off of the current time(in seconds).

import datetime

def createRandomNumber(minNumber = 0,maxNumber = 100):
  currentTime = datetime.datetime.now()
  currentTime = datetime.time.now()

  #take only the seconds from the time
  #convert the string to int
  randomNumber = int(currentTime[:10])

  #creates a ceiling for the random number
  randomNumber = randomNumber % maxNumber
  #creates a floor for the random number
  if randomNumber <= minNumber:randomNumber += minNumber

  print(randomNumber)

minTime = int(input("minimum number-"))
maxTime = int(input("maximum number-"))
