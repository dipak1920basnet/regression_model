import matplotlib.pyplot as plt 
import numpy as np 


def Visualize_cost(Cost_list, W_list, b_list):
    
    ax = plt.figure().add_subplot(projection='3d')
    ax.legend()
    ax.set_xlim(0,7)
    ax.set_ylim(199,401)
    ax.set_zlim(0,700)

    W = []
    B = []

    for w in W_list:
        for b in b_list:
            W.append(w)
            B.append(b)

    print(W)
    print(B)

    ax.scatter(W, B, Cost_list)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()



# This block of code is generated with AI chat gpt guest mode
def Dcountour_3(Cost_list, W_list, b_list):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    W_grid, B_grid = np.meshgrid(W_list, b_list)
    Z = np.array(Cost_list).reshape(len(b_list), len(W_list))

    ax.contour3D(W_grid, B_grid, Z, 50, cmap='viridis')

    ax.set_xlim(0, 7)
    ax.set_ylim(199, 401)
    ax.set_zlim(0, 700)

    ax.set_xlabel('W')
    ax.set_ylabel('B')
    ax.set_zlabel('Cost')

    plt.show()