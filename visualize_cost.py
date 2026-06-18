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