import math


def humanbytes(size):
    if not size:
        return ""

    power = 1024
    n = 0
    Dic_powerN = {
        0: "",
        1: "KB",
        2: "MB",
        3: "GB",
        4: "TB"
    }

    while size > power:
        size /= power
        n += 1

    return f"{round(size,2)} {Dic_powerN[n]}"
