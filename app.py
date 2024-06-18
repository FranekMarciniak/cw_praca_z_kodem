import numpy as np

def interesting_function(a, b):
    return a + b
def flatten_function(l):
    arr = np.array(l)
    return arr.flatten('F').tolist()

if __name__ == "__main__":
    print(f"12 + 32 = {interesting_function(12, 32)}")
    print(f"[1, 2, 3] = {flatten_function([1, 2, 3])}")
    print(f"[1, [2, 3]] = {flatten_function([[2, 3], [2, 3]])}")
