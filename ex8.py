formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "Hey",
    "I was doing just fine before i met you",
    "I drink too much thats an issue",
    "But i am okay."
)