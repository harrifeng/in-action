def main():
    dp(11)


def dp(size):
    min = ['inf'] * (size + 1)
    min[0] = 0
    v = [1, 3, 5]
    for i in range(1, size+1):
        for vj in v:
            if vj <= i and min[i-vj] + 1 < min[i]:
                min[i] = min[i-vj] + 1

    for i, v in enumerate(min):
        print i, v


if __name__ == '__main__':
    main()
