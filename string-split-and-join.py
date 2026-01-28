def split_and_join(line):
    ans = ""
    for c in line:
        if c == " ":
            ans += "-"
        else:
            ans += c
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
