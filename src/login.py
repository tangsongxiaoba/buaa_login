import CVBB_LOGIN
import sys, getopt, time
import pprint

def getArgs():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "i:p:")
    except getopt.GetoptError:
        print("Usage: login -i <id> -p <password>")
        sys.exit(-1)
    id = None
    pwd = None
    for name, value in opts:
        if name == "-i":
            id = value
        if name == "-p":
            pwd = value
    if id == None or pwd == None:
        print("Usage: login -i <id> -p <password>")
        sys.exit(-1)
    return id, pwd

def main():
    id, pwd = getArgs()
    login = CVBB_LOGIN.CVBB_LOGIN(id, pwd)
    info = login.run()
    success = True
    if info[0] == -1:
        success = False
        print("login failed.")
    elif info[0] == 0:
        flag = False
        for _ in range(10):
            time.sleep(1)
            info = login.run()
            if info[0] == 1:
                flag = True
                break
        if not flag :
            success = False
            print("After 10 retries, login failed.")
    if success:
        print("login successful!")
    pprint.pprint(info[1])

if __name__ == "__main__":
    main()