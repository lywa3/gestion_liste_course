import sys


def presentation(nom):
    print(f'Bienvenue, {nom}')


def is_digit(nombre: str):
    return bool(nombre.isdigit())


def string_is_digit(nombre_str: str):
    if nombre_str.isdigit():
        return int(nombre_str)


if __name__ == '__main__':
    msg_teste_taille_liste = "Votre liste contient actuellement {} élément{}"
    demarrage_programme = True
    liste_course = []

    print("""
    Bienvenue sur le programme de gestion de votre liste de course
    ---------------------------------------------------------------
    """)

    if demarrage_programme:
        nom_utilisateur = input("Votre nom : ")
        presentation(nom_utilisateur)
        demarrage_programme = False

    if len(liste_course) <= 0:
        print(msg_teste_taille_liste.format(len(liste_course), ""))
    elif len(liste_course) == 1:
        print(msg_teste_taille_liste.format(len(liste_course), ""))
    elif len(liste_course) > 1:
        print(msg_teste_taille_liste.format(len(liste_course), "s"))

    while True:
        print("""
        Menu du programme liste course
        -------------------------------
        1. Ajouter un élément à la liste
        2. Modifier un élément de la liste
        3. Retirer un élément de la liste
        4. Afficher la liste
        5. Changer l'ordre d'un element dans la liste
        6. Vider la liste
        7. Quitter le programme
        """)

        choix_programme = input("Votre choix : ")

        if choix_programme == "1":
            element = input("🎯 Entrez un élément à votre liste : ")
            if not is_digit(element):
                if element in liste_course:
                    liste_course.append(element)
                    print("""😙 Vous avez ajouté l'élément {} à votre liste de course""".format(element))
                else:
                    print("🙄 Vous avez déjà ajouté l'élément {} à votre liste de course".format(element))
            else:
                print("🙄 Votre élément n'est pas correct. Il n'a pas été ajouté")
        elif choix_programme == "2":
            if not len(liste_course) == 0:
                element = input("Entrez l'élément à modifier : ")
                update_element = input("Entrez le nouvel élément : ")
                if not element.isdigit() and not update_element.isdigit():
                    chaine_course = ", ".join(liste_course)
                    new_chaine_course = chaine_course.replace(element, update_element)
                    if chaine_course != new_chaine_course:
                        liste_course = new_chaine_course.split(", ")
                        print(f"""
                        -------------------------------------------------
                        Vous avez remplacé 
                        {element} par {update_element}
                        --------------------------------------------------
                        """)
                    else:
                        print(f"""
                        ----------------------------------------------
                        Erreur : Votre liste contient déjà l'élément
                        {element}
                        ----------------------------------------------
                        """)
                else:
                    print("""
                    ------------------------------------------
                    Erreur : Vos éléments ne sont pas correct
                    ------------------------------------------
                    """)
            else:
                print("""
                ----------------------------------------------
                Erreur : Votre liste ne contient aucun élément
                ----------------------------------------------
                """)
        elif choix_programme == "3":
            if not len(liste_course) == 0:
                element = input("Entrez l'élément à supprimer de votre liste : ")
                try:
                    liste_course.remove(element)
                except ValueError:
                    print("""
                    ----------------------------------------------------------------------------
                    Erreur : Cette élément n'existe pas dans votre liste. Vérifiez l'orthographe
                    ----------------------------------------------------------------------------
                    """)
                print(f"""
                -----------------------------------------------------
                Success : Vous avez supprimé {element} de votre liste
                -----------------------------------------------------
                """)
            else:
                print("""
                ----------------------------------------------
                Erreur : Votre liste ne contient aucun élément
                ----------------------------------------------
                """)
        elif choix_programme == "4":
            if not len(liste_course) == 0:
                i = 0
                print("""
                ----------------------------------------------
                Success : Votre liste.........................
                ----------------------------------------------""")
                for x in liste_course:
                    i = i + 1
                    print("""
                    {}. {}""".format(i, x))
            else:
                print("""
                ----------------------------------------------
                Erreur : Votre liste ne contient aucun élément
                ----------------------------------------------
                """)
        elif choix_programme == "5":
            print("""⚠ Attention ⚠ : Vous ne pouvez deplacer un element en tete de liste vers le bas.
            Mais seulement un element du bas vers le haut.""")
            move_element = input("Entrez l'élément à déplacer : ")
            new_position = input("Entrez la nouvelle position de lélément dans la liste : ")
            if new_position.isdigit() and (1 <= int(new_position) <= len(liste_course)) and (
                    int(new_position) - 1) >= 0:
                if not liste_course.count(move_element) == 0:
                    new_position = int(new_position) - 1
                    old_position = liste_course.index(move_element)
                    new_liste_course = []
                    for element in liste_course:
                        if liste_course.index(element) == new_position:
                            new_liste_course.append(move_element)
                            new_liste_course.append(element)
                        elif liste_course.index(element) == old_position:
                            continue
                        else:
                            new_liste_course.append(element)
                    liste_course = new_liste_course
                    print(f"""
                    ---------------------------------------------------------
                    Success : l'élément {move_element}
                    a bien été déplacé à la position {new_position + 1}
                    ---------------------------------------------------------
                    """)
                else:
                    print(f"""
                    ---------------------------------------------------------
                    Erreur : Votre liste ne contient pas l'élément
                    {move_element}
                    ---------------------------------------------------------
                    """)
            else:
                print(f"""
                ---------------------------------------------------------
                Erreur : Entrez un chiffre correct !
                ---------------------------------------------------------
                """)
        elif choix_programme == "6":
            if not len(liste_course) == 0 and liste_course.clear() is None:
                print("""
                ---------------------------------------------------------
                Success : Votre liste de course a été vidé de son contenu
                ---------------------------------------------------------
                """)
        elif choix_programme == "7":
            print("""À Bientôt !""")
            sys.exit()
        else:
            print("""
            ---------------------------------------------
            Erreur : Votre choix n'est pas pris en compte
            ---------------------------------------------
            """)

        print((("-" * 500) + "\n") * 5)
