import numpy as np
def top_left_to_bottom_right(matrix):
    (m,n) = np.shape(matrix)
    path = []
    failedpoints=set()
    failedpoints.add((0,1))
    failedpoints.add((2,1))
    get_path(m-1, n-1, path, failedpoints)
    return path
def get_path(m,n, path, failedpoints):
    is_at_origin= (m==0) and (n==0)
    if m<0 or n<0:
        return False
    if (m,n) in failedpoints:
        return False
    if is_at_origin or get_path(m-1,n, path,failedpoints)or get_path(m, n-1, path,failedpoints):
        path.append((m,n))
        return True

    failedpoints.add((m,n))
    return False
matrix=[[1,0,1,1],[1,1,1,1],[1,0,1,1]]
print(top_left_to_bottom_right(matrix))