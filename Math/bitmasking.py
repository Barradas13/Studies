def add(set, element):
    return (set | (1 << (element - 1)))

def remove(set, element):
    return (set ^ (1 << (element - 1)))

def display(set, element):
    return (set & (1 << (element - 1)))

def displayAll(set, N):
    for i in range(1, N + 1):
        if set & (1 << (i - 1)):
            print(i)


if __name__ == "__main__":
    set = 15
    displayAll(set, 10)
    set = remove(set, 1)
    print(display(set, 1))