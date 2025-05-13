n, *c = [*open(0)]
print(*sorted(sorted(list(set(c))), key=lambda x:len(x)), sep="", end="")