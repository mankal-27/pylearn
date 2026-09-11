name = input("What's your name?")
print("Welcome,", name)

quantity = input("How many items? ")
total = int(quantity) * 19.99
print(total)

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("Wireless Mouse", "USB Cable", "HDMI Cable")
print("Wireless Mouse", "USB Cable", "HDMI Cable", sep=", ")
print("Wireless Mouse", "USB Cable", "HDMI Cable", sep=" | ")
print("Wireless Mouse", "USB Cable", "HDMI Cable", sep="")