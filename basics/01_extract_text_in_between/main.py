fname = "./input.txt"

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

ans = []

for line in content:
    startID = line.find('\"')
    newline = line[startID+1:]
    endID = newline.find('\"')
    ans.append(newline[:endID])

print(ans)