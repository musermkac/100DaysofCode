hugeNumberAsStr = open('hello.txt').read()
hugeNumberAsStr = hugeNumberAsStr.strip().replace('\n', '')

f = open("demofile4.txt", "w")
f.write(hugeNumberAsStr)
f.close()

print(hugeNumberAsStr)