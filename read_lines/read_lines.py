def read_lines(path):
    result=[]
    with open(path) as f:
      for line in f:
          cleaned=  line.strip()
          if len(cleaned)!=0:
           result.append(cleaned)
    return result

with open("sample.txt", "w") as f:
    f.write("hello\n\n  world  \n\nlast line\n")

assert read_lines("sample.txt") == ["hello", "world", "last line"]

with open("empty.txt", "w") as f:
    f.write("")

assert read_lines("empty.txt") == []
print("Checkpoint ok")