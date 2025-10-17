#pseudocode
# créer horaire_autobus(liste)
# def prochain_bus
# print horaire
# demander à l'utilisateur quelle bus il veut prendre
#if  comparer et dire la bus la plus proche s'il n'est pas dans la plage horaire
#if > 24 demander de rentrer un valeur plus petit que 24
#if not chiffre demander de rentrer un nombre avec l'entier qui represente l'heure et deux décimal
#
#######

list_horaire_autobus = [ 6.14 , 7.44 , 9.14 , 10.44, 12.14 , 13.44 , 15.14 , 16.44 , 18.14 , 19.44 , 21.14]
def prochain_bus(choix_utilisateur, list_horaire_bus):
    """
    :param choix_utilisateur: heure entrée par l'utilisateur
    :param list_horaire_bus: plage horaire des bus
    :return: horaire de bus la plus proche
    """
__name__ == "__main__"
print(list_horaire_autobus)
choix_utilisateur = (float(input("Quelle temps voudriez vous partir:(entier = heure, 2 décimal = minutes) ")))
# validation de valeur
if choix_utilisateur == ValueError:
    (float(input("rentrer un nombre")))
if choix_utilisateur > 24:
    input("rentrer une valeur qui rentre dans la plage horaire d'une journée(24h)")
elif choix_utilisateur < 0:
    input("rentrer une valeur qui rentre dans la plage horaire d'une journée(24h)")
# prochain bus la plus proche
if input(choix_utilisateur) == [id] in list_horaire_autobus:
    print("parfait: vous avez une bus en même temps! ")
    if choix_utilisateur <= 6.14:
        print("la prochaine bus est a 6.14")
    elif choix_utilisateur > 21.14:
        print("la prochaine bus est a 6.14")
    elif choix_utilisateur >= 6.15:
        print("la prochaine bus est a 7.44")
    elif choix_utilisateur >= 7.45:
        print("la prochaine bus est a 9.14")
    elif choix_utilisateur >= 9.14:
        print("la prochaine bus est a 10.44")
    elif choix_utilisateur >= 10.45:
        print("la prochaine bus est a 12.14")
    elif choix_utilisateur >= 12.15:
        print("la prochaine bus est a 13.44")
    elif choix_utilisateur >= 13.45:
        print("la prochaine bus est a 15.14")
    elif choix_utilisateur >= 15.15:
        print("la prochaine bus est a 16.44")
    elif choix_utilisateur >= 16.45:
        print("la prochaine bus est a 18.14")
    elif choix_utilisateur >= 18.15:
        print("la prochaine bus est a 19.44")
    elif choix_utilisateur >= 19.45:
        print("la prochaine bus est a 20.14")

