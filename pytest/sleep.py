from cyber import *
from time import sleep

REF_INTERVAL = 60

idfile = 'ids.txt'


def load_id():
    idtxt = open(idfile).read()
    lines = idtxt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids


def cycle(ids):
    # Cycle through a set of username/password combinations,
    # while checking the live login status periodically.
    try:
        success = False

        for cred in ids:
            if init(cred[0], cred[1]):
                print('Logged in with %s' % cred[0])
                success = True

                while True:
                    sleep(REF_INTERVAL)
                    # print('Checking status of %s' % cred[0])

                    if not check_live(cred[0]):
                        success = False
                        break

        if not success:
            print('Damn! All combinations failed.')
        else:
            cycle()
    except:
        logout_request(cred[0])

if __name__ == '__main__':
    cycle(load_id())