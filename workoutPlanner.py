# This is a program designed to program "optimal" workouts based on a user's
# one rep max, to predict working set weights - per NCSA's training load chart

oneRepMax = int(input("This program assists in programming workouts for " + \
                      "compound lifts.\n" + "What is your one rep max?\n"))

def workoutPlanner(weight):
    goal = input("\nWhat are you planning to work towards?\n" + "Strength or" +\
          " Hypertrophy?\n")
    if goal.lower() == "strength" or goal.lower() == "s":
        workingWeight = weight * 0.87
        threeRepMax = weight * 0.93
        print("\nSince your goal is strength, your ideal working set weight"+\
              " would be " + str(workingWeight) + " lbs for 5 reps per set.")
        print("For your three rep max sets, you should be able to lift " + \
              str(threeRepMax) + " lbs for 3 reps per set instead.")
    elif goal.lower() == "hypertrophy" or goal.lower() == "h" or goal.lower()\
    == "hyper":
        workingWeight = weight * 0.8
        amrapWeight = weight * 0.7
        print("\nSince your goal is hypertrophy, your ideal working set " + \
              "weight would be in between " + str(workingWeight) + " lbs " + \
                "for 8 reps per set and " + str(amrapWeight) + " lbs for " + \
                "12 reps per set.")
    else:
        print("\nPlease enter the first letter or full word of the choices" +\
              " provided above.")
        return workoutPlanner(weight)

workoutPlanner(oneRepMax)