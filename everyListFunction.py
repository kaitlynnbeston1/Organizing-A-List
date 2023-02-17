# Creating my list
programmingLanguages = ["python", "c", "visual basic", "javascript", "rust", "html", "julia", "css", "lua", "anonymous", "cobol"]
 
 
 # Getting the length of the list.
print(f"The length of the above programming languages list is {len(programmingLanguages)}.")


# Sorting the list using sorted()
print("The languages in the list are as follows:")
print(sorted(programmingLanguages))
print("In reverse order, that would be:")
print(sorted(programmingLanguages, reverse=True))


# reversing the list.
print("The original list in reverse order is as follows:")
programmingLanguages.reverse()
print(programmingLanguages)
# Undoing the reverse
print("Here is the original list:")
programmingLanguages.reverse()
print(programmingLanguages)


# Modifying the list.
print("Now, let's modify the list.")
# Removing items from the list.
print("HTML and CSS are markup languages, not programming languages. Who made this list anyway? NO matter, I'll just kick them off of the list.")
programmingLanguages.remove("html")
del programmingLanguages[6]
print("No one likes Cobol, so I'll also remove that using Python's reverse indexing.")
del programmingLanguages[-1]
print("Anonymous obviously isn't a programming language...")
notReal = programmingLanguages.pop(7)
print(f"{notReal} has been removed, because it doesn't exist.")
print(f"The list now has {len(programmingLanguages)} items.")
print("They are:")
for language in sorted(programmingLanguages):
    print(language)
# Adding languages to the list
print("C++ wasn't aded, so it will now be appended to the end of the list.")
programmingLanguages.append("c++")
print("Another influential programming language, Swift, wasn't added. Let's do that now.")
programmingLanguages.insert(4, "swift")
print("I almost forgot. Go is another influential programming language. Let's add it to the list.")
programmingLanguages[8] = "go"


# final form of our list.
for language in programmingLanguages:
    print(language)

# Perminantly alphabetically sorting the list.
programmingLanguages.sort()
print(programmingLanguages)


# Indexing
print(f"Fun fact: The languages I know are {programmingLanguages[0]} and a bit of {programmingLanguages[2]}")

