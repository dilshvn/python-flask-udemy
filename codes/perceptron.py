#PERCEPTRON

#1st mathematical model of perceptron (1940)
    #example,
        #takes 3 binary inputs, sums them, checks if >= theta and < theta
        #when theta = 1,
            #if sum >= 1: output = 1
            #if sum < 1: output = 0
        #if output = 1,
            #1 of 3 inputs has to be 1 -> OR gate
        #if output = 3,
            #all 3 inputs has to be 1 -> AND gate
    #inhibitary input ->  when inhibitray input = 1, output = 0

#2nd and modern model of perceptron (1958)
    #all inputs have weights (w1, w2, w3) and go through to be a function
    #example,
        #f(x) = x**2
        #when input x = 2, output = 4
    #no inhibitaries
    #perceptrons can work in serial and parallel -> makes a neural network
