import generate_data
import model 

X = generate_data.X
y = generate_data.y

w = 2
b = 200


linear_model = model.linear_model(X, w, b)

print(linear_model)