import os


# Funktion som tar in en prompt där man kan fråga användaren ja och nej frågor
def AskUserYesOrNo(prompt_message):
    while True:
        try:
            # Läser inmatning från användare och tar bort onödiga white spaces, gör om till små bokstäver och tar ut första tecknet
            ask_user = input(prompt_message).strip().lower()[0]
            # Om användaren svara 'ja(j)' eller yes(y)' returnerar funktionen True
            if ask_user in ["y", "j", "y"]:
                return True
            # Om användaren svarar 'nej(n)' eller 'no(n)' returneras False
            elif ask_user in ["n"]:
                return False
            else:
                # Om användaren svarar med något annat returneras detta meddelande
                print("Ogiltigt svar, svara med ja eller nej")

        except KeyboardInterrupt:
            # Om användare avbryter programmet med Ctrl+C
            print("Programmet avslutas!")
            exit()
