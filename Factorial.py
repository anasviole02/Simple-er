def main():
    def fact(n):
        f = 1
        for i in range(1,n+1):
            f = f * i
        return f

    x = fact(5)
    print(x)


if __name__ == '__main__':
    main()