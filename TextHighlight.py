x = "Hello World!"
for i in range(len(x)):
    print((x[0:i+1] + "\n")*500, end="")
