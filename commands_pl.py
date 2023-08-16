import psutil


def temp():
    tempre = psutil.sensors_temperatures()
    temp = tempre['coretemp']
    return temp[2], temp[1]


def process():
    all_processes = psutil.process_iter()
    user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
    user_processes = str(user_processes)
    return user_processes.replace('psutil.Process', '\n')
