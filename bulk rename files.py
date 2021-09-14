import os 

def main():
    i = 0
    path = "C:/Users/NatashaNewbold/Code/Mini Python projects/test virtual/bulk rename/"
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()

