'''
Hackxercise 1 
Timing attacks: Unlocking Information Security I: From Cryptography to Buffer Overflows

In computer security, a side-channel attack is any attack based on extra information that
can be gathered because of the fundamental way a computer protocol or algorithm is implemented, 
rather than flaws in the design of the protocol or algorithm itself (e.g. flaws found in
a cryptanalysis of a cryptographic algorithm) or minor, but potentially devastating, mistakes
or oversights in the implementation
'''


from Root.pswd import real_password
import time
import sys  # ignore
sys.path.insert(0, '.')  # ignore


def check_password(password):  # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

# TODO


def crack_password():
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = 0
    y = 0
    z = 0
    v = 0
    number = d[x]+d[y]+d[z]+d[v]
    c = False
    while (c != True):
        start_time = time.time()
        c = check_password(number)
        elapsed_time = time.time()-start_time

        while (elapsed_time <= 0.2):
            x += 1
            number = d[x]+d[y]+d[z]+d[v]
            start_time = time.time()
            c = check_password(number)
            elapsed_time = time.time()-start_time

        while (elapsed_time <= 0.3):
            y += 1
            number = d[x]+d[y]+d[z]+d[v]
            start_time = time.time()
            c = check_password(number)
            elapsed_time = time.time()-start_time

        while (elapsed_time <= 0.4):
            z += 1
            number = d[x]+d[y]+d[z]+d[v]
            start_time = time.time()
            c = check_password(number)
            elapsed_time = time.time()-start_time

        while (elapsed_time <= 0.5 and c == False):
            v += 1
            number = d[x]+d[y]+d[z]+d[v]
            start_time = time.time()
            c = check_password(number)
            elapsed_time = time.time()-start_time

    return number


start_time = time.time()
print(crack_password())
elapsed_time = time.time()-start_time
print(elapsed_time)
