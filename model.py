# buuild a regression model
def regression(x,w,b):
    # apply a formula y = mx + c 
    """
    x = features 
    w = weight = m  = slope 
    b = c = bias 
    """
    return x*w+b

def linear_model(X,w,b):
    # check if we received 1 example of multiple of them 
    if type(X) == list:
        # preset the total values of target we are going to predict
        # and set a placeholder for the predictions
        y = [-1]*len(X)

        # loop through the each input data 
        for i in range(len(X)):
            # make predictions for the data and store it in y 
            y[i] =  regression(X[i], w, b)

        # return the predictions made for the input data 
        return y 
    
    # if there is single Value of x then simply call the regression model for the predictions
    return regression(X,w,b)