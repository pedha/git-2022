f = lambda x, y : ["PASS", x, y] if x > 3 and y < 100 else ["FAIL", x, y]
print(f(4,50))
