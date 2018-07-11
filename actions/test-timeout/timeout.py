import time

def main(args):
    print("Sleep start")
    count = 1
    while (count < 60):
        time.sleep(10)
        count = count + 1
        print "Slept %d seconds" % (count*10)
