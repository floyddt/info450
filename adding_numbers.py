import sys

def add_them_all(filename):
    sum = 0
    ### Your code here
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line.strip():
                sum += int(line)
    ### End of your code
    return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))