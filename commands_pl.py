import psutil


def temp():
    tempre = psutil.sensors_temperatures()
    temp = tempre['coretemp']
    return temp[2], temp[1]


# def process():
#     all_processes = psutil.process_iter()
#     user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
#     user_processes = list(user_processes)
#     len_process = len(user_processes)
#     divided_lists = [user_processes[i:i + 4] for i in range(0, len(user_processes), 4)]
#     print(divided_lists)
def process_1():
    all_processes = psutil.process_iter()
    user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
    user_processes = list(user_processes)
    len_process = len(user_processes)
    divided_lists = [user_processes[i:i + 4] for i in range(0, len(user_processes), 4)]
    print(divided_lists)

    return divided_lists[0]
def process_2():
    all_processes = psutil.process_iter()
    user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
    user_processes = list(user_processes)
    len_process = len(user_processes)
    divided_lists = [user_processes[i:i + 4] for i in range(0, len(user_processes), 4)]
    divided_lists_ls = str(divided_lists[1])

    return  divided_lists_ls
def process_3():
    all_processes = psutil.process_iter()
    user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
    user_processes = list(user_processes)
    len_process = len(user_processes)
    divided_lists = [user_processes[i:i + 4] for i in range(0, len(user_processes), 4)]
    print(divided_lists)
    return divided_lists[2]
def process_4():
    all_processes = psutil.process_iter()
    user_processes = [p for p in all_processes if p.username() == psutil.Process().username()]
    user_processes = list(user_processes)
    len_process = len(user_processes)
    divided_lists = [user_processes[i:i + 4] for i in range(0, len(user_processes), 4)]
    print(divided_lists)
    return divided_lists[3]


def user_add():
    user = psutil.users()
    users = str(user[0])
    return users


    #return user_processes.replace('psutil.Process', '\n')

if __name__ == "__main__":
     pass