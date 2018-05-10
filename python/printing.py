print("Hey, I'm a print statement!")
print('Now I\'m a print statement with an escaped single quote.')
print("I am a %s print statement." % "string interpolated")
print("There is now $%f embedded in this statement." % 32.2523213)
print("But we'll round down and make sure it's exactly $%.2f." % 32.2500000)
variables = "variables"
print("We can put %s in here." % variables)
print("And we can %s %s %s." % ("interpolate", "multiple", "strings"))
