import sys
if sys.argv[1] == "add":
    file = open("tasks.txt", "a")
    file.write("[ ] " + sys.argv[2] + "\n")
    file.close()
elif sys.argv[1] == "list":
    file = open("tasks.txt", "r")
    content = file.read()
    tasks = content.splitlines()
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    file.close()
elif sys.argv[1] == "delete":
    file = open("tasks.txt", "r")
    content = file.read()
    tasks = content.splitlines()
    index = int(sys.argv[2]) - 1
    del tasks[index]
    file = open("tasks.txt", "w")
    for t in tasks:
        file.write(t + "\n")
    file.close()
elif sys.argv[1] == "done":
    file = open("tasks.txt", "r")
    content = file.read()
    tasks = content.splitlines()
    index = int(sys.argv[2]) - 1
    tasks[index] = tasks[index].replace("[ ]", "[x]")
    file = open("tasks.txt", "w")
    for t in tasks:
        file.write(t + "\n")
    file.close()
