import model 
from visualize_cost import Visualize_cost, Dcountour_3


X = [i for i in range(1,30,2)]
y = [i*2+200 for i in range(1,30,2)]

w = 2
b = 200


linear_model = model.linear_model(X, w, b)


from cost_function import cost_J

cost_list = []

w_list = [1,2,3,4,5]
b_list = [201,200]

for i in range(len(w_list)):
    for j in range(len(b_list)):
        pred = model.linear_model(X,w_list[i], b_list[j])
        cost_list.append(cost_J(y,Pred=pred))

Visualize_cost(cost_list, w_list, b_list)

Dcountour_3(cost_list, w_list, b_list)

print(cost_list)