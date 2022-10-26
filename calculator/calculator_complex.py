def math_complex_to_list(s):
    result = []
    try:
        s = s.replace(' ', '')
        start = -1
        for j in range(len(s)):
            if s[j] in ('*', '/', '+', '-') and s[j - 1].isdigit():
                result.append(int(s[start + 2:j]))
                start = j
            elif s[j] == ")" and s[start] == "-":
                result.append(int(s[start:j - 1]))
            elif s[j] == ")" and s[start] == "+":
                result.append(int(s[start + 1:j - 1]))
            elif s[j] in ('*', '/', '+', '-') and s[j - 1] == ')':
                result.append(s[j])
                start = j
    except:
        return "Wrong input"

    return calc_list(result)


def calc_list(l):
    res = ""
    if l[2] == "+":
        if l[1] + l[-1] >= 0:
            res += str(l[0] + l[3]) + "+" + str(l[1] + l[-1]) + "i"
        else:
            res += str(l[0] + l[3]) + str(l[1] + l[-1]) + "i"
    elif l[2] == "-":
        if l[1] - l[-1] >= 0:
            res += str(l[0] - l[3]) + "+" + str(l[1] - l[-1]) + "i"
        else:
            res += str(l[0] - l[3]) + str(l[1] - l[-1]) + "i"
    elif l[2] == "*":
        if (l[0] * l[-1]) + (l[1] * l[3]) >= 0:
            res += str((l[0] * l[3]) + (l[1] * l[-1]) * -1) + "+" + str((l[0] * l[-1]) + (l[1] * l[3])) + "i"
        else:
            res += str((l[0] * l[3]) + (l[1] * l[-1]) * -1) + str((l[0] * l[-1]) + (l[1] * l[3])) + "i"

    elif l[2] == "/":
        numerator = [(l[0] * l[3] + l[1] * l[-1])] + [l[0] * (l[-1] * -1) + l[1] * l[3]]
        denominator = [l[3] * l[3] + l[-1] * l[-1]]
        if numerator[1] > 0:
            if numerator[0] == 0:
                res += str(numerator[1]) + "i" + "/" + str(denominator[0])
            elif numerator[1] == 0:
                res += str(numerator[0]) + "+" + "i" + "/" + str(denominator[0])
            else:
                res += str(numerator[0]) + "+" + str(numerator[1]) + "i" + "/" + str(denominator[0])
        else:
            if numerator[0] == 0:
                res += "-" + str(numerator[1]) + "i" + "/" + str(denominator[0]) + "i"
            elif numerator[1] == 0:
                res += str(numerator[0]) + "+" + "i" + "/" + str(denominator[0])
            else:
                res += str(numerator[0]) + str(numerator[1]) + "+" + "i" + "/" + str(denominator[0])

    return res
