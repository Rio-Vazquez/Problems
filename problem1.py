def strip_evens(n):
    upper = n - 1
    solution=[]
    x=0
    while x<upper:
        if x%2 == 1:
            solution.append(x)
        x = x + 1
    return solution


def main():
    newdata = strip_evens(8)
    print(newdata)


if __name__ == "__main__":
    main()
