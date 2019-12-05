import random

if __name__ == '__main__':
    for num in range(100):
        list = []
        while len(list) < 7:
            tmp = random.randint(1,33)
            if(list.count(tmp) > 0):
                continue
            list.append(tmp)
            print(tmp,end=' ')

        print('\033[31m',(random.randint(1,16)),'\033[0m')


