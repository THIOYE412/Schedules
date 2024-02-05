from activities import Activity
from basicconstraints import PrecedenceConstraint

class TopologicalSorter:

  @staticmethod
  def bruteForceSort(activities, constraints):
    acts = activities.copy()
    result = []

    while len(acts) != 0:
      activity =  TopologicalSorter.auxiliary(acts, result, constraints)
      if activity is None:
        return None
      result.append(activity)
      acts.remove(activity)

    return result

  @staticmethod
  def auxiliary(objects, res, constraints):
    for obj in objects:
      ok = True
      for constraint in constraints:
        if constraint.getSecond == obj and constraint.getFirst not in res:
          ok = False
          break

      if ok:
        return obj

    return None
  
  @staticmethod
  def schedule(activities, constraints, startTime):
    result = TopologicalSorter.bruteForceSort(activities, constraints)

    if result is None:
      return None
    
    currentTime = startTime
    dictionaryOfSchedules = {}

    for activity in result:
       dictionaryOfSchedules[currentTime] = activity
       currentTime += activity.getDuration

    return dictionaryOfSchedules

class Main:

  @staticmethod
  def printResult(activities, constraints, startTime): 
    print("\n1. Ordonnancement")
    result = TopologicalSorter.bruteForceSort(activities, constraints)
    if result is None:
      print("Ordonnacement impossible ")
    else:
      for activity in result:
        print(f"{activity.getDescription}")

    print("\n2. Emploi du temps")
    schedule = TopologicalSorter.schedule(activities, constraints, startTime)
    if schedule is None:
      print("Planification d'emploi du temps impossible")
    else:
      print(f"Debut \t\t\t Description \t\t\t Durée")
      for startTime, activity in schedule.items():
        print(f"{startTime} \t\t {activity.getDescription} \t\t\t\t\t {activity.getDuration}")
    


 
# Exemple d'utilisation
if __name__ == "__main__":
  activities1 = [Activity("Se lever", 1), Activity("Prendre un petit déjeuner", 15),
               Activity("Se brosser les dents", 3), Activity("Prendre une douche", 10),
               Activity("S'habiller", 2), Activity("Aller au travail", 15)]

  constraints1 = [PrecedenceConstraint(activities1[0], activities1[1]),
                PrecedenceConstraint(activities1[0], activities1[4]),
                PrecedenceConstraint(activities1[1], activities1[2]),
                PrecedenceConstraint(activities1[1], activities1[3]),
                PrecedenceConstraint(activities1[2], activities1[5]),
                PrecedenceConstraint(activities1[3], activities1[4]),
                PrecedenceConstraint(activities1[4], activities1[5]),
                PrecedenceConstraint(activities1[0], activities1[3]),
                PrecedenceConstraint(activities1[1], activities1[5])]

  Main.printResult(activities1, constraints1, 500)

  activities2 = [Activity("Prendre connaissance du sujet d'examen", 30),
               Activity("Réviser", 300), Activity("Entrer dans la salle d'examen", 8)]

  constraints2 = [PrecedenceConstraint(activities2[1], activities2[2]),
                PrecedenceConstraint(activities2[2], activities2[0]),
                PrecedenceConstraint(activities2[0], activities2[1])]

  Main.printResult(activities2, constraints2, 500)

