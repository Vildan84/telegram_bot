def check_tel(s):
    if s.isdigit() and len(s) == 11:
        l = [i for i in s]
        edit_tel = ["+7"] + ["("] + l[1:4] + [")"] + l[4:7] + ["-"] + l[7:9] + ["-"] + l[9:]
        return "".join(edit_tel)

    elif s.isdigit():
        return s

    else:
        return False
