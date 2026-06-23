# train the model with Gradient Descent 

"""
1) 

"""

import sumpy as sp 


# Calculate Gradient 

def Gradient(parameter_value, parameter:str, function:str):
    # get the gradient of function with respect to the parameter
    x = sp.Symbol(parameter)
    df = sp.diff(function, x)
    value = df.subs(x, parameter_value)
    return value


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
    weight_Gradient, bias_gradient = Gradient("w", function), Gradient("b", function)
    # return updated weight and bias
    return update(w,alpha,weight_Gradient), update(b,alpha, bias_gradient)


"""
def train_model(w,b,alpha,cost_function,epochs):
    w_history = [-1]*epochs
    b_history = [-1]*epochs
    w_history.append(w)
    b_history.append(b)
    for i in epochs:
        w,b = Gradient_descent(w,b,alpha,cost_function)
    return w_history,b_history
"""