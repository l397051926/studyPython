if __name__ == '__main__':
    import time
    for i in range(30):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        time.sleep(1)