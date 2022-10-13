if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coord_i = [i for i in range(x + 1)]
    coord_j = [j for j in range(y + 1)]
    coord_k = [k for k in range(z + 1)]

    coords = [[i, j, k] for i in coord_i for j in coord_j for k in coord_k if i + j + k != n]
    print(coords)

    # Example:
    """
    x = 1
    y = 1
    z = 2
    n = 3
    
    coords = [
        [0, 0, 0], 
        [0, 0, 1], 
        [0, 0, 2], 
        [0, 1, 0], 
        [0, 1, 1], 
        [0, 1, 2], 
        [1, 0, 0], 
        [1, 0, 1], 
        [1, 0, 2], 
        [1, 1, 0], 
        [1, 1, 1], 
        [1, 1, 2]
    ]
    """


