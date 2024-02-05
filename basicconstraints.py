from activities import Activity as acts

class  PrecedenceConstraint:
  
  def __init__(self, firstActivity: acts, secondActivity: acts):
    self._firstActivity = firstActivity
    self._secondActivity = secondActivity

  def _get_firstActivity(self):
    return self._firstActivity
  
  def _get_secondActivity(self):
    return self._secondActivity
  
  getFirst = property(_get_firstActivity)
  getSecond = property(_get_secondActivity)

  def isSatisfied(self, startTimeFirst, startTimeSecond):
    endTimeFirst = startTimeFirst + self.getFirst.getDuration
    testSatisfied = int(endTimeFirst) <= int(startTimeSecond) # La seconde commence après la première
    if testSatisfied:
      return testSatisfied
    else:
      return False
    

# Classe executable Main
class Main:
  @staticmethod
  def run():
    firstObjet = acts("Se brosse les dents", 15)
    secondObjet = acts("Aller à l'école", 1)

    precedence_constraint = PrecedenceConstraint(firstObjet, secondObjet)

    print("Satisfaction de contrainte: ", precedence_constraint.isSatisfied(500, 515))
    print("Satisfaction de contrainte: ", precedence_constraint.isSatisfied(500, 513))
    print("Satisfaction de contrainte: ", precedence_constraint.isSatisfied(500, 518))


if __name__ == "__main__":
  Main.run()
  print("\n")


# Creation de la classe de Contrainte de type Meet
class MeetConstraint:

  def __init__(self, firstActivity: acts, secondActivity: acts):
    self._firstActivity = firstActivity
    self._secondActivity = secondActivity

  def _get_firstActivity(self):
    return self._firstActivity
  
  def _get_secondActivity(self):
    return self._secondActivity
  
  getFirst = property(_get_firstActivity)
  getSecond = property(_get_secondActivity)

  def isSatisfied(self, startTimeFirst, startTimeSecond):
    endTimeFirst = startTimeFirst + self.getFirst.getDuration
    if int(endTimeFirst) == int(startTimeSecond):
      return True
    else:
      return False


# Classe executable Main
class Main:
  @staticmethod
  def run():
    firstObjet = acts("Se brosse les dents", 15)
    secondObjet = acts("Aller à l'école", 1)

    meet_constraint = MeetConstraint(firstObjet, secondObjet)

    print("Satisfaction de contrainte: ", meet_constraint.isSatisfied(500, 515))
    print("Satisfaction de contrainte: ", meet_constraint.isSatisfied(500, 513))
    print("Satisfaction de contrainte: ", meet_constraint.isSatisfied(500, 518))


if __name__ == "__main__":
  Main.run()