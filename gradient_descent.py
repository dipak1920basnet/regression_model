# train the model with Gradient Descent 

"""
1) 

"""

# Calculate Gradient 

def Gradient(parameter, function):
    # get the gradient of function with respect to the parameter
    pass


# Update the parameter
def update(parameter, alpha, gradient):
    return (parameter - (alpha * gradient))


def Gradient_descent(w,b,alpha,function):
    """
    w: weight
    b: bias
    alpha: learning rate
    function: function to minimize eg: cost
    """
    weight_Gradient, bias_gradient = Gradient(w, function), Gradient(b, function)
    # return updated weight and bias
    return update(w,alpha,weight_Gradient), update(b,alpha, bias_gradient)

    