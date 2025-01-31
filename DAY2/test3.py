x = "I am in RVU"  # single quote
y = "What is your name"  # double quotes
z = """Hello world"""  # triple quote
print(x, y, sep=";")
print(z, x, sep="=")
"""
# Configuring the output record separator:
# To change the output record separator, use the 'end' argument
"""
print(x, y, end="\n")
print(x, y, sep="\t\t ", end="\n")



