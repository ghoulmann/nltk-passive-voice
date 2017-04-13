import proselint

suggest = proselint.tools.lint

fh = open("data/example.txt", "r")
raw_text = fh.read()
fh.close()

suggestions = suggest(raw_text)
for suggestion in suggestions:
    print(str(suggestion[2]) + ": " + suggestion[1] + " \(" + suggestion[8]) + "\)")
