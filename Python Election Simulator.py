
import random, colorama, turtle
from termcolor import colored, cprint
from itertools import cycle

colorama.init()
"""
Remake of the electoral app with better functions!
"""

# Create random names

randNames = ["Oliver ", "George ", "Arthur ", "Arthur ", "Noah ", "Muhammad ", "Leo ",
             "Oscar ", "Harry ", "Archie ", "Jack ", "Henry ", "Charlie ", "Freddie ", "Theodore ",
             "Thomas "]

randLastNames = ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies",
                 "Patel", "Robinson", "Wright", "Thompson", "Evans", "Walker",
                 "White", "Roberts", "Green", "Hall", "Thomas", "Clarke"]

randomPoliticianName1 = random.choice(randNames) + random.choice(randLastNames)
randomPoliticianName2 = random.choice(randNames) + random.choice(randLastNames)
randomPoliticianName3 = random.choice(randNames) + random.choice(randLastNames)
randomPoliticianName4 = random.choice(randNames) + random.choice(randLastNames)
randomPoliticianName5 = random.choice(randNames) + random.choice(randLastNames)
randomPoliticianName6 = random.choice(randNames) + random.choice(randLastNames)

###### ASK FOR AGE

def ask_for_age_and_name():
    age = int(input("\n\tInsert your age here: "))
    name = input("\tInsert your name here: ")
    return age, name

###### DISPLAY PARTIES AND ASK FOR VOTE

def display_parties_and_ask_for_vote():
 #Show eligible parties
    print("\n\tThe parties that you can vote for in this election are: ")
    cprint(f"\t1. The Conservative Party of Pomabia", "blue")
    print(f"\t\tThe party leader is : {randomPoliticianName1}")
    cprint(f"\t2. The Liberal Party of Pomabia", "red")
    print(f"\t\tThe party leader is : {randomPoliticianName2}")
    cprint(f"\t3. The Pomabian Ecological Union", "green")
    print(f"\t\tThe party leader is : {randomPoliticianName3}")
    cprint(f"\t4. The Libertarian Party of Pomabia", "yellow")
    print(f"\t\tThe party leader is : {randomPoliticianName4}")
    cprint(f"\t5. The Pomabian National Front ", "cyan")
    print(f"\t\tThe party leader is : {randomPoliticianName4}")
    cprint(f"\t6. The Pomabian Worker's Front: ", "magenta")
    print(f"\t\tThe party leader is : {randomPoliticianName5}")

    #Ask for vote
    electionvote = int(input("\tInsert the number for the party you wish to vote for here: "))

    while electionvote <= 0 or electionvote > 6:
        print("\n\tERROR: Invalid party vote!")
        electionvote = int(input("\tInsert the number for the party you wish to vote for here: "))
    voteMessage(electionvote)
    return electionvote

###### DISPLAY MESSAGE AFTER VOTING

def voteMessage(vote):
    if vote  == 1:
        cprint("\n\tTHANK YOU FOR VOTING FOR THE CONSERVATIVE PARTY OF POMABIA!", "blue")
    elif vote  == 2:
        cprint("\n\tTHANK YOU FOR VOTING FOR THE LIBERAL PARTY OF POMABIA!", "red")
    elif vote == 3:
        cprint("\n\tPEACE MAN, THANKS FOR VOTING FOR THE ECOLOGICAL UNION!", "green")
    elif vote == 4:
        cprint("\n\tWELCOME FELLOW VENTURE CAPITALIST! THANK YOU FOR VOTING FOR THE LIBERTARIANS!" "yellow")
    elif vote == 5:
        cprint("\n\tOUR FELLOW PATRIOTS THANK YOU FOR VOTING FOR THE NATIONAL FRONT. WE WILL MAKE POMABIA GREAT AGAIN!", "cyan")
    else:
        cprint("\n\tWE APPRECIATE YOUR VOTE COMRADE!", "magenta")
    input("\n\t<<< PRESS ENTER TO SEE THE RESULTS >>>")

###### GENERAL VOTING API
def votingAPI(age):
    if age >= 18:
        print("\tCongratulations, you are eligible to vote!")
        display_parties_and_ask_for_vote()
    else:
        print("\n\tUnfortunately you cannot vote in this year's elections, \n\tplease try again next year.", "blue")
        print("""
   _.-._         ..-..         _.-._
   (_-.-_)       /|'.'|\       (_'.'_)
    .\-/.        \)\-/(/        ,-.-.
 __/ /-. \__   __/ ' ' \__   __/'-'-'\__
( (___/___) ) ( (_/-._\_) ) ( (_/   \_) )
 '.Oo___oO.'   '.Oo___oO.'   '.Oo___oO.'
 ELECTION DEPARTMENT OF THE SERENE REPUBLIC
  OF POMABIA
  unicornium humilitatem locutus est Anglis perfectus.""")

##### Calculate percentages

def calculatePercentages():
    percentageCP = random.randint(1,9)
    percentageLP = random.randint(1,9)
    percentageEU = random.randint(1,9)
    percentageLibP = random.randint(1,9)
    percentagePNF = random.randint(1,9)
    percentagePWF = random.randint(1,9)

    finalPercent = 100 / (percentageCP + percentageLP + percentageEU + \
                          percentageLibP + percentagePNF + percentagePWF)

    percentageCP *= finalPercent
    percentageLP *= finalPercent
    percentageEU *= finalPercent
    percentageLibP *= finalPercent
    percentagePNF *= finalPercent
    percentagePWF *= finalPercent

    return percentageCP, percentageLP,percentageEU, percentageLibP, percentagePNF, \
           percentagePWF

##### Display graph with election results (Turtle)

def displayGraph(perc1,perc2,perc3,perc4,perc5,perc6):
    segmentLabels = cycle(["CPP", "LPP", "PEU", "LibtPP", "PNF", "PWF"])
    percentages = [perc1,perc2,perc3,perc4,perc5,perc6]
    percentagesCycle = cycle([perc1,perc2,perc3,perc4,perc5,perc6])
    colors = cycle(["blue", "red", "green", "yellow", "cyan", "magenta"]) # error here
    RADIUS = 200
    TOTAL = 100
# Create window
    win = turtle.Screen()
    win.title("Election Results")
    win.bgcolor("white")
    win.setup(width = 800, height = 600)
    win.tracer(0)
# Create text for election results
    topText = turtle.Pen()
    topText.speed(1)
    topText.penup()
    topText.hideturtle()
    topText.goto(0,250)
    topText.write("ELECTION RESULTS:", align="center", font=("Small Fonts", 24, "normal"))

# Create pie chart
    pieChart = turtle.Pen()
    pieChart.penup()
    pieChart.sety(-RADIUS)
    pieChart.pendown()
# range that goes over each of the different percentages
    for x in range (0, len(percentages)):
        pieChart.fillcolor(next(colors))
        pieChart.begin_fill()
        pieChart.circle(RADIUS, next(percentagesCycle) * 360 / TOTAL)
        position = pieChart.position()
        pieChart.goto(0,0)
        pieChart.end_fill()
        pieChart.setposition(position)
    pieChart.hideturtle()
# Draw labels for each of the party
    pieChart.penup()
    pieChart.sety(-RADIUS)
    for label in range (0, len(percentages)):
        pieChart.circle(RADIUS, next(percentagesCycle) * 360 / TOTAL / 2)
        pieChart.write(next(segmentLabels), align="center", font=("Small Fonts", 11, "normal"))
        pieChart.circle(RADIUS, next(percentagesCycle) * 360 / TOTAL / 2)
        
# If statement to determine who is the winner
    winnerMessage = turtle.Pen()
    winnerMessage.speed(1)
    winnerMessage.penup()
    winnerMessage.hideturtle()
    winnerMessage.goto(0, -250)
    winnerMessage.pendown()

    if perc1 > perc2 and perc1 > perc3 and perc1 > perc4 and perc1 > perc5 and perc1 > perc6:
        winnerMessage.write(f"The Conservative Party of Pomabia won with {perc1:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))

    elif perc2 > perc1 and perc2 > perc3 and perc2 > perc4 and perc2 > perc5 and perc2 > perc6:
        winnerMessage.write(f"The Liberal Party of Pomabia won with {perc2:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))

    elif perc3 > perc1 and perc3 > perc2 and perc3 > perc4 and perc3 > perc5 and perc3 > perc6:
        winnerMessage.write(f"The Pomabian Ecological Union won with {perc3:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))

    elif perc4 > perc1 and perc4 > perc2 and perc4 > perc3 and perc4 > perc5 and perc4 > perc6:
        winnerMessage.write(f"The Libertarian Party of Pomabia won with {perc4:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))

    elif perc5 > perc1 and perc5 > perc2 and perc5 > perc3 and perc5 > perc4 and perc5 > perc6:
        winnerMessage.write(f"The Pomabian National Front won with {perc5:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))

    else:
        winnerMessage.write(f"The Pomabian Worker's Front won with {perc6:.2f}% of the vote.", align="center", font=("Small Fonts", 12, "bold"))
    askQuit = turtle.textinput("PRESS CANCEL", " TO QUIT...")

######################## MAIN
def main():
    # Ask for your age
    yourAge, yourName = ask_for_age_and_name()
    # General voting API
    myVote = votingAPI(yourAge)
    # Calculate percentages
    percCP, percLP, percEU, percLibP, percPNF, percPWF = calculatePercentages()
    # Display results with a chart (Turtle)
    displayGraph(percCP, percLP, percEU, percLibP, percPNF, percPWF)

################### EXECUTE MAIN ############################
main()
