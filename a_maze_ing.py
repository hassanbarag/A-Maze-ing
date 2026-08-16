#!/usr/bin/env python3

import random
import sys
import os
from mazegen.maze_generator import MazeGenerator
from config import load_config, Config
from animation import animate_path, not_animate_path
from mazegen.patterns_42 import PATTERN_42
from mazegen.style import (getValue, titelCustom, clearTerminal,
                           resetAllCustom, resetCustomPart,
                           printConfi, writeFile, isValidSGR,
                           resetCustomColors, resetCustomWH)


colors: dict[str, str] = {
        "WHITE": "107",
        "GREY": "100",
        "ORANGE": "48;5;208",
        "PURPLE": "48;5;129",
        "PINK": "45",
        "BLUE": "44",
        "YELLOW": "43",
        "GREEN": "42",
        "RED": "41",
        "BLACK": "40",
    }


# Funcion menu para escoger que color poner
def changeColor(part: str, file: str, pathV: bool) -> None:
    exit: bool = True
    option: str
    txt: str
    colorL: list[str] = list(colors.keys())

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Change color", file))
            printConfi(part, file)
            for i in range(len(colorL)):
                txt = str(i+1) + "."
                print(f"{txt.ljust(4)}{colorL[i].capitalize().ljust(8)}"
                      f"\x1b[{colors.get(colorL[i])}m \x1b[0m")
            print(f"{len(colorL) + 1}. Reset")
            print(f"{len(colorL) + 2}. Exit")
            option = input("\nOption: ")
            for c in range(len(colorL)):
                if (option == str(len(colorL) + 1)):
                    resetCustomPart(part)
                elif (option == str(len(colorL) + 2)):
                    exit = False
                elif (option == str(c + 1)):
                    writeFile(part, colorL[c])
            try:
                if (int(option) > (len(colorL) + 2)):
                    print("\nInvalid number\n")
                    input("Press 'Enter' to continue ")
            except Exception:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion menu para escoger el color por la gama de color de 0 a 255
def customizeColor(part: str, file: str, pathV: bool) -> None:
    exit: bool = True
    option: str

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Customize Color", file))
            printConfi(part, file)
            print("Write a valid SGR (Select Graphic Rendition) value\n"
                  "(type 'reset' to return to the default option or "
                  "'exit' to quit)")
            option = input("\nOption: ")
            try:
                if (option.lower() == "reset"):
                    resetCustomPart(part)
                elif (option.lower() == "exit"):
                    exit = False
                elif (isValidSGR(option)):
                    writeFile(part, option)
                else:
                    print("\nInvalid number\n")
                    input("Press 'Enter' to continue ")
            except Exception:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion menu para escoger un caracter
def customizeCaracter(part: str, file: str, pathV: bool) -> None:
    exit: bool = True
    option: str

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Customize caracter", file))
            printConfi(part, file)
            print("Enter a character\n(type 'reset' "
                  "to return to the default option or 'exit' "
                  "to quit)")
            option = input("\nOption: ")
            try:
                if (option.lower() == "reset"):
                    resetCustomPart(part)
                elif (option.lower() == "exit"):
                    exit = False
                else:
                    if (len(option) == 1 and option.isascii()
                            and option.isprintable()):
                        writeFile(part, option)
                    else:
                        print("\nInvalid character\n")
                        input("Press 'Enter' to continue ")
            except Exception:
                print("\nInvalid character\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion que controla que opcion se ha escogido y en que parte
def numberOptions(n: str, part: str, file: str, pathV: bool) -> None:
    if (n == "1"):
        changeColor(part, file, pathV)
    elif (n == "2"):
        customizeColor(part, file, pathV)
    else:
        customizeCaracter(part, file, pathV)


# Funcion menu para decidir que parte modificar
def optionParts(n: str, file: str, pathV: bool) -> None:
    exit: bool = True
    option: str

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Part", file))
            print("1. Background\n2. Wall\n3. Path\n"
                  "4. Start Point\n5. Final Point\n"
                  "6. Icon Number\n7. Exit")
            option = input("\nOption: ")
            if (option == "1"):
                numberOptions(n, "BACKGROUND", file, pathV)
            elif (option == "2"):
                numberOptions(n, "WALL", file, pathV)
            elif (option == "3"):
                numberOptions(n, "PATH", file, pathV)
            elif (option == "4"):
                numberOptions(n, "START", file, pathV)
            elif (option == "5"):
                numberOptions(n, "FINAL", file, pathV)
            elif (option == "6"):
                numberOptions(n, "ICON", file, pathV)
            elif (option == "7"):
                exit = False
            else:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion menu para customizar el laberinto
def menuCustom(file: str, pathV: bool) -> None:
    exit: bool = True
    option: str

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Customize A-Maze-Ing", file))
            print("1. Change color\n2. Customize color\n"
                  "3. Customize caracter\n4. Reset\n5. Exit")
            option = input("\nOption: ")
            if (option == "1"):
                optionParts(option, file, pathV)
            elif (option == "2"):
                optionParts(option, file, pathV)
            elif (option == "3"):
                optionParts(option, file, pathV)
            elif (option == "4"):
                resetCustomColors()
            elif (option == "5"):
                exit = False
            else:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcon menu para Modificar el Width/Height
def resizeWH(part: str, file: str, pathV: bool) -> None:
    exit: bool = True
    option: str
    listPart: list[str] = part.split(",")
    text: str = listPart[0].upper()

    while (exit):
        try:
            clearTerminal()

            if (mazePrintAnimate(file, pathV)):
                print(titelCustom(f"Resize {text.capitalize()}", file))
                printConfi(text, file)
                print("Enter an integer, type 'reset' to restore the "
                      "default value, or 'exit' to quit")
                if (len(listPart) > 1):
                    print("The minimum width is 10 and the maximum is 105, "
                          "and the minimum heigth is 7 and the maximum is 22")
                elif (text == "WIDTH"):
                    print("The minimum width is 10 and the maximum is 105.")
                else:
                    print("The minimum heigth is 7 and the maximum is 22.")
                print("")
                option = input("Option: ")
                if (option.lower() == "exit"):
                    exit = False
                elif (option.lower() == "reset"):
                    resetCustomPart(listPart[0].upper())
                    resetCustomPart(listPart[2].upper())
                    resetCustomPart("EXIT")
                elif (int(option) and
                      ((text == "WIDTH" and int(option) >= 10
                        and int(option) <= 105) or
                        (text == "HEIGHT" and int(option) >= 7
                         and int(option) <= 22))):
                    writeFile(text, option)
                    if (len(listPart) > 1):
                        if (listPart[1] == "="):
                            writeFile(listPart[2], option)
                        else:
                            if (text == listPart[0].upper()):
                                text = listPart[2].upper()
                            else:
                                text = listPart[0].upper()
                    x: int = int(getValue("WIDTH", file)) - 1
                    y: int = int(getValue("HEIGHT", file)) - 1
                    xy: str = str(x) + "," + str(y)
                    writeFile("EXIT", xy)
                else:
                    print("\nInvalid number\n")
                    input("Press 'Enter' to continue ")
            else:
                exit = False
        except Exception as err:
            print(err)
            print("\nMust be a number; letters or emojis are not allowed\n")
            input("Press 'Enter' to continue ")


# Funcion menu para cambiar el tamanyo del laberinto
def menuResize(file: str, pathV: bool) -> None:
    exit: bool = True
    option: str

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Resize Width/Height", file))
            print("1. Width\n2. Height\n3. Width/Height\n4. Width=Height\n"
                  "5. Reset\n6. Exit")
            option = input("\nOption: ")
            if (option == "1"):
                resizeWH("WIDTH", file, pathV)
            elif (option == "2"):
                resizeWH("HEIGHT", file, pathV)
            elif (option == "3"):
                resizeWH("WIDTH,/,HEIGHT", file, pathV)
            elif (option == "4"):
                resizeWH("HEIGHT,=,WIDTH", file, pathV)
            elif (option == "5"):
                resetCustomWH()
                resetCustomPart("EXIT")
            elif (option == "6"):
                exit = False
            else:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion Menu principal
def menuIndex(file: str) -> None:
    exit: bool = True
    option: str
    pathV: bool = True

    while (exit):
        clearTerminal()

        if (mazePrintAnimate(file, pathV)):
            print(titelCustom("Menu", file))
            print("1. Re-generate a new maze\n2. Show/Hide path from entry "
                  "to exit\n3. Maze Customize\n4. Show Path with animation\n"
                  "5. Resize Maze Width/Height\n6. All reset\n7. Exit")
            option = input("\nOption: ")
            if (option == "1"):
                randomSeed()
                if not (mazePrintAnimate(file, pathV, True)):
                    exit = False
            elif (option == "2"):
                if pathV:
                    pathV = False
                else:
                    pathV = True
            elif (option == "3"):
                menuCustom(file, pathV)
            elif (option == "4"):
                if (not mazePrintAnimate(file, pathV, True)):
                    exit = False
            elif (option == "5"):
                menuResize(file, pathV)
            elif (option == "6"):
                resetAllCustom()
            elif (option == "7"):
                os.remove("custom.txt")
                exit = False
            else:
                print("\nInvalid number\n")
                input("Press 'Enter' to continue ")
        else:
            exit = False


# Funcion para generar un nuevo seed
def randomSeed() -> None:
    num = random.randint(1, 999)
    writeFile("SEED", str(num))


def clamp(part: str, file: str, min_val: int, max_val: int) -> None:
    value: int = int(getValue(part, file))

    if value > max_val:
        writeFile(part, str(max_val))
    elif value < min_val:
        writeFile(part, str(min_val))


# funcion para printear el laberinto animado
def mazePrintAnimate(file: str, pathV: bool = True,
                     animate: bool = False) -> bool:
    try:
        clamp("WIDTH", file, 10, 105)
        clamp("HEIGHT", file, 7, 22)

        config: Config = load_config(file)

        maze: MazeGenerator = MazeGenerator(
            config.width,
            config.height,
            config.entry,
            config.exit,
            config.seed,
            config.perfect,
        )

        mW = round((int(getValue("WIDTH", file)) - 10) / 2)
        mH = round((int(getValue("HEIGHT", file)) - 5) / 2)
        maze.build_42_mask(PATTERN_42["4"], mW, mH)
        maze.build_42_mask(PATTERN_42["2"], mW + 5, mH)

        maze.dfs()

        path = maze.solve()

        maze.solution_path = path

        if (animate):
            animate_path(maze, path, 0.08, file, pathV)
        else:
            not_animate_path(maze, path, file, pathV)

        maze.export(config.output_file)
        return (True)
    except Exception as err:
        print(f"Error mazePrintAnimate [{file}] -> {err}")
        return (False)


def main() -> None:
    if (len(sys.argv) == 2):
        resetAllCustom()
        try:
            if (mazePrintAnimate(sys.argv[1], True, True)):
                menuIndex(sys.argv[1])
        except KeyboardInterrupt:
            print("\n\nExiting cleanly ✓")
            if os.path.exists("custom.txt"):
                os.remove("custom.txt")
            sys.exit(0)
    else:
        print("The program requires a .txt file to function.")


if __name__ == "__main__":
    main()
