from util.server_util import setup_server, delete_heroku_server
import signal
import time
import sys

THREAD_SHORT_SLEEP = 0.1

if __name__ == '__main__':
    addr = setup_server('yoolitest') # different tasks can have different task names here
    print(addr)
    print("holy success")
    # heroku addons:create heroku-postgresql:hobby-dev
    def signal_handler(signal,frame):
        print('Terminate tasks...')
        #delete_heroku_server
        print('Done!')
        sys.exit(0)

    signal.signal(signal.SIGINT,signal_handler)
    while True:
        time.sleep(THREAD_SHORT_SLEEP)