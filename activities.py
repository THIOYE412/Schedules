class Activity:
  """ Classe contenant les activites et leurs duree d'execution """

  def __init__(self, description: str, time: int):
    self._description = description
    self._time = time

  def _get_description(self):
    """ Recupere la description d'une activite """
    return self._description
  
  def _get_time(self):
    """ Recupere la duree d'une acivite """
    return self._time
  
  getDescription = property(_get_description)
  getDuration = property(_get_time)


class Main:
  @staticmethod
  def main():
    # Instanciation de deux activités
    firstActivity = Activity("Se lever", 500)
    SecondActivity = Activity("Se brosser les dents", 515)

    # Affichage de la description et la durée des activitées
    print(f""" Duree1                  Description1          
 {firstActivity.getDuration}                      {firstActivity.getDescription}""")
    
    print("\n")

    print(f""" Duree1                    Description2          
 {SecondActivity.getDuration}                  {SecondActivity.getDescription}""")




if __name__ == "__main__":
  Main.main()