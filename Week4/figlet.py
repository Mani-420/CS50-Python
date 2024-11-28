# Figlet Problem 1


from pyfiglet import Figlet
import random, sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 0:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

message = input("Input: ")
print(figlet.renderText(message))
