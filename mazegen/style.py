import os

# Lista de los colores
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


# Funcion para verificar Si cumple la norma SGR
def isValidSGR(codigo: str) -> bool:
    partes = [p.strip() for p in codigo.split(";")]

    if not partes or any(p == "" for p in partes):
        return False
    try:
        nums = [int(p) for p in partes]
    except ValueError:
        return False
    n = nums[0]

    # 40–47: colores de fondo estándar
    if 40 <= n <= 47 and len(nums) == 1:
        return True

    # 49: restablecer color de fondo
    if n == 49 and len(nums) == 1:
        return True

    # 100–107: colores brillantes de fondo (extensión)
    if 100 <= n <= 107 and len(nums) == 1:
        return True

    # 48;5;N: modo 256 colores
    if n == 48 and len(nums) == 3 and nums[1] == 5:
        return 0 <= nums[2] <= 255

    # 48;2;R;G;B: modo RGB truecolor
    if n == 48 and len(nums) == 5 and nums[1] == 2:
        return all(0 <= c <= 255 for c in nums[2:])

    return False


# Funcion paara saber si un str es un int
def isInt(s: str) -> bool:
    try:
        int(s.strip())
        return True
    except ValueError:
        return False


# Funcion para imprimir el valor de 'custom.txt' o 'config.txt'
def getValue(part: str, file: str, num: int = 1) -> str:
    fList: list[str]
    txt: str
    txts: list[str] = []
    parts: list[str] = ["BACKGROUND", "WALL", "PATH", "START", "FINAL", "ICON"]

    try:
        with open("./custom.txt", "r", encoding="utf-8") as f:
            fList = f.readlines()
        for i in fList:
            if (part in i):
                txt = i.split("=", 1)[1].strip()
                if (len(txt) > 0):
                    txts.append(txt)
                else:
                    txts.append("")
    except Exception as err:
        print(f"Error in getValue [custom.txt] ({part}): {err}")
        input("Press 'Enter' to continue ")
        return ""

    try:
        with open(file, "r", encoding="utf-8") as f:
            fList = f.readlines()
        for i in fList:
            if ("#" not in i and part in i):
                txt = i.split("=", 1)[1].strip()
                if (len(txt) > 0):
                    txts.append(txt)
                else:
                    txts.append("")
    except Exception as err:
        print(f"Error in getValue [{file}] ({part}): {err}")
        input("Press 'Enter' to continue ")
        return ""

    try:
        if (num == 1):
            if (txts[0] == ""):
                return (txts[1].upper())
            else:
                return (txts[0].upper())
        elif (num == 2):
            txt = txts[0].upper() + ";" + txts[1].upper()
            return txt
    except Exception as err:
        if not (part in parts):
            print(f"Return error in getValue ({part}): {err}")
            input("Press 'Enter' to continue ")
            return ""

    return ""


# Funcion para poner los colore al laberinto
def iconColor(part: str, file: str) -> str | None:
    code: str | None
    txt: str = getValue(part, file)

    if not txt:
        return (None)
    elif (txt in colors.keys()):
        code = colors.get(txt)
        return (f"\x1b[{code}m \x1b[0m")
    elif (isValidSGR(txt)):
        return (f"\x1b[{txt}m \x1b[0m")
    elif (len(txt) == 1 and txt.isascii()
          and txt.isprintable()):
        return (txt)

    return None


# Funcion para poner un color
def printColor(color: str, part: str = "") -> str:
    code: str | None
    color = color.strip()

    if (part == "WIDTH" or part == "HEIGHT"):
        if (len(color.strip()) > 0):
            return (color)
    else:
        if not color:
            return ""
        elif (color in colors.keys()):
            code = colors.get(color)
            return (f"\x1b[{code}m \x1b[0m")
        elif (isValidSGR(color)):
            return (f"\x1b[{color}m \x1b[0m")
        elif (len(color) == 1 and color.isascii()
              and color.isprintable()):
            return (color)

    return ""


# Funcion para printear que valor estan puesto tanto en dafault como en custom
def printConfi(part: str, file: str) -> None:
    configL: list[str] = (getValue(part, file, 2)).split(";")
    lenColor: int = len(printColor(configL[1], part))

    print((f"\nDefault: {printColor(configL[1], part)}").ljust(15 + lenColor) +
          f"Custom: {printColor(configL[0], part)}\n".ljust(15 + lenColor))


# Funcion para crear el titulo
def titelCustom(text: str, file: str, di: str = "") -> str:
    try:
        number: int = int(getValue("WIDTH", file)) * 2 + 1
        simbol: str = "\x1b[107m \x1b[0m"

        if (di == "top"):
            return ((simbol * number) + "\n" +
                    text.center(number, " "))
        else:
            return (text.center(number, " ") + "\n" +
                    (simbol * number) + "\n")
    except Exception as err:
        print(f"Error titelCustom [{file}] -> {err}")

    return ""


# Funcion para resetear el archivo 'custom.txt'
def resetAllCustom() -> None:
    try:
        with open("./custom.txt", "w") as f:
            f.write("WIDTH=\nHEIGHT=\nEXIT=\nSEED=\nBACKGROUND=\nWALL=\n"
                    "PATH=\nSTART=\nFINAL=\nICON=\n")
    except Exception as err:
        print(f"Error Reset 'custom.txt' -> all: {err}\n")
        input("Press 'Enter' to continue ")


# Funcion para resetear una parte en 'custom.txt'
def resetCustomPart(part: str) -> None:
    try:
        lines: list[str]
        with open("./custom.txt", "r+", encoding="utf-8") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if part in lines[i]:
                    lines[i] = part + "=\n"
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    except Exception as err:
        print(f"Error Reset 'custom.txt' -> '{part}': {err}\n")
        input("Press 'Enter' to continue ")


# Funcion para resetear todo los valores de colores de 'custom.txt'
def resetCustomColors() -> None:
    parts: list[str] = ["BACKGROUND", "WALL", "PATH", "START", "FINAL", "ICON"]

    for p in parts:
        resetCustomPart(p)


# Funcion para resetear todo los valores de tamanyo de 'custom.txt'
def resetCustomWH() -> None:
    parts: list[str] = ["WIDTH", "HEIGHT"]

    for p in parts:
        resetCustomPart(p)


# Funcion para escribir en 'custom.txt'
def writeFile(part: str, text: str) -> None:
    file: str
    posicion: int
    newContent: str

    resetCustomPart(part)
    try:
        with open("./custom.txt", "r", encoding="utf-8") as f:
            file = f.read()
    except Exception as err:
        print(f"Error reading 'custom.txt': {err}\n")
        input("Press 'Enter' to continue ")

    posicion = file.find(part)
    newContent = (file[:(posicion + len(part) + 1)] +
                  text +
                  file[(posicion + len(part) + 1):])

    try:
        with open("./custom.txt", "w", encoding="utf-8") as f:
            f.write(newContent)
    except Exception as err:
        print(f"Error writing 'custom.txt': {err}\n")
        input("Press 'Enter' to continue ")


# Funcion para limpiar la terminal
def clearTerminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")
