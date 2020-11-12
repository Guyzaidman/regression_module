import math


def summarize(x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    mean_x = sum_x / len(x)
    mean_y = sum_y / len(y)

    sum_xiyi = sum([x[i] * y[i] for i in range(len(x))])

    sum_x_squred = sum([i * i for i in x])
    sum_x__squred = sum(x) * sum(x)

    b1 = (sum_xiyi - (sum_x * sum_y / len(x))) / (sum_x_squred - (sum_x__squred / len(x)))
    b0 = mean_y - (b1 * mean_x)

    print("sum(x):" + str(sum_x))
    print("sum(y):" + str(sum_y) + "\n")

    print("avg(x):" + str(mean_x))
    print("avg(y):" + str(mean_y) + "\n")

    print("sum(x[i]*y[i]): " + str(sum_xiyi) + "\n")

    print("sum(x^2): " + str(sum_x_squred))
    print("(sum(x))^2: " + str(sum_x__squred) + "\n")

    print("Sxx: " + str(calculate_sii(x)))
    print("Syy: " + str(calculate_sii(y)))
    print("Sxy: " + str(calculate_sxy(x, y)) + "\n")

    print("b0: " + str(b0))
    print("b1: " + str(b1))


def calc_b0_b1(x, y):
    if len(x) != len(y):
        raise BaseException("x and y not of same length!")

    sum_x = sum(x)
    sum_y = sum(y)

    mean_x = sum_x / len(x)
    mean_y = sum_y / len(y)

    sum_xiyi = sum([x[i] * y[i] for i in range(len(x))])

    sum_x_squred = sum([i * i for i in x])
    sum_x__squred = sum(x) * sum(x)

    b1 = (sum_xiyi - (sum_x * sum_y / len(x))) / (sum_x_squred - (sum_x__squred / len(x)))
    b0 = mean_y - (b1 * mean_x)

    return b0, b1


def sse(x, y):
    b0, b1 = calc_b0_b1(x, y)
    print(b0, b1)

    y_hat = lambda x: b0 + b1 * x
    s = sum([math.pow(y[i] - y_hat(x[i]), 2) for i in range(len(y))])

    return s


def mse(x, y):
    return sse(x, y) / (len(x) - 2)


def calculate_sii(l):
    s = 0
    avg = sum(l) / len(l)
    for x in l:
        s += math.pow(x - avg, 2)
    return s


# need to check!!!
def calculate_sxy(x, y):
    if len(x) != len(y):
        raise BaseException("x and y not of same length!")

    s = 0
    avg_x = sum(x) / len(x)
    avg_y = sum(y) / len(y)
    for i, j in zip(x, y):
        xx = i - avg_x
        yy = j - avg_y
        s += xx * yy
    return s
