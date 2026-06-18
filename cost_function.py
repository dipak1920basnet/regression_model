def calc_error(Y_true, Y_pred):
    return (Y_true - Y_pred) ** 2

def cost_J(Y,Pred):
    m = len(Y)
    total_error = 0
    for i in range(m):
        total_error += calc_error(Y[i], Pred[i])
    cost = total_error/(2*m)
    return cost 

