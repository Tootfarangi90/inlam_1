import os


def AskUserYesOrNo(prompt_message):
    while True:
        try:
            ask_user = input(prompt_message).strip().lower()[0]
            if ask_user in ["y", "j", "y"]:
                return True
            elif ask_user in ["n"]:
                return False
            else:
                print("Ogiltigt svar, svara med ja eller nej")

        except KeyboardInterrupt:
            print("Programmet avslutas!")
            exit()
