from matplotlib import pyplot as plt

# Initialize an empty python list to store the quotients (result of the polynomial division)
quotients = []


def poly_division(numerator, denominator, quotients):
    '''
    A python function to carry out polynomial division of a numerator
    and denominator
    :param numerator: a list of coefficients of the numerator equation in order of magnitude
    e.g 0.213z^2 + 0.1804z = [0.213, 0.1804, 0 , 0 ]
    note: numerator and denominator lists must be of same size
    :param denominator: a python tuple (immutable list) of parameters in the denominator
    (denominator value doesn't change during the division)
    :param quotients: an empty list in which the quotients/results will be stored
    '''
    # Python list to store the values to be subtracted from the numerator
    subtractor = []

    # Calculating the quotient by dividing the numerator and denominator
    quotient = numerator[0] / denominator[0]

    # Storing the value to the quotients list
    quotients.append(quotient)

    # Carrying out the long division process to get the next numerator
    # for the new sequence of division
    for i in denominator:
        subtractor_value = quotient * i
        subtractor.append(subtractor_value)
    new_numerator = []
    zip_object = zip(numerator, subtractor)
    for numerator_i, subtractor_i in zip_object:
        new_numerator.append(numerator_i - subtractor_i)
    new_numerator.pop(0)
    new_numerator.insert(len(new_numerator), 0)

    # Printing the result on completion
    if len(quotients) < 100:
        poly_division(new_numerator, denominator, quotients)
    else:
        print("k = ", quotients)
        return 0


def plot():
    '''
    Plots the result of the division on completion
    :return:
    '''
    k = [i for i in range(100)]
    plt.plot(k, quotients, drawstyle="steps-pre")
    plt.xlabel("k")
    plt.ylabel("y(k,0.5)")
    plt.suptitle("output response of the system y(k) as a function of k")
    plt.title("Plot")
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.show()


#poly_division([0.213, 0.1804,0,0], (1, -2.394, 2.181, -0.787), quotients)
#plot()

poly_division([0.058, 0.295, 0.041, 0], (1, -2.394, 2.181, -0.787), quotients)
plot()
