def adstock_transform(spend, decay):
    adstock = []

    for i, value in enumerate(spend):
        if i == 0:
            adstock.append(value)
        else:
            adstock.append(value + decay * adstock[i - 1])

    return adstock


def hill_saturation(x, alpha, gamma):
    return (x ** alpha) / (x ** alpha + gamma ** alpha)