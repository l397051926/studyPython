if __name__ == '__main__':
    import time
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))