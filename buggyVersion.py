# Constants
SEATS_PER_CART = 6
COASTER_TIME = 10
 
# Program variables
peopleInLine = -1
numCarts = -1
waitTime = 0
cartFill = 0
placeInLine = -1
 
# Prompts user and updates variable storing number of people in line
while(peopleInLine < 0)
 placeInLine = int(input("How many people are in line? "))
 
# Prompts user and updates variable storing the number of carts
while(numcars < 0):
 numCarts = int(input("How many roller coaster carts are there? ")
 
# Prompts user and updates user’s position in line
while(placeInLine > 0): 
 placeInLine = int(input("What is your place in line? "))
 
# Calculates the total amount of seats in coaster
def calculateTotalSeats(seatsPerCart, cartNum):
 return seatsPerCart * cartNum
 
# Stores total seats in a variable
totalSeats = calculateTotalSeats(SEATS_PER_CART, numCarts)
 
# Calculates number of time coaster will run before user gets on
def numRuns(lineSpot openSeats):
 peopleInFront = lineSpot - 1
 if(peopleInFront < openSeats):
   return 0
 else if(peopleInFront = openSeats):
   return 1
 else:
   runCount = 1
   while((peopleInFront - openSeats) > openSeats):
       runCount += 1
       peopleInFront -= openSeats
   return runCount

# Calculates and returns wait time 
def calculateWaitTime(lineSpot):
 COASTER_TIME = 15
 coasterRuns = numRnus(lineSpot, openSeats)
 return int(coasterRuns) * COASTER_TIME
 
# Calculates number of empty seats (at the end)
def emptySeats(peopleInLine):
  return peopleInLine % SEATS_PER_CART
 
# Asks user if they want to know wait time (Prompts for yes or no answer)
print("Do you want to know your wait time?")
answer = str(input())

# Prints calculations if user wants
if(answer == "yes" or answer == "YES" and answer == "Yes"):
  print("Your wait time is " + (calculateWaitTime(placeInLine)) + " minutes")
  print("There will be" + str(emptySeats(peopleInLine)) + "empty seats on the coaster.")
