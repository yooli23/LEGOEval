from util.server_util import setup_server, delete_heroku_server
import signal
import time

THREAD_SHORT_SLEEP = 0.1

if __name__ == '__main__':
    addr = setup_server('yoolitest')
    print(addr)
    print("holy success")
    def signal_handler(signal,frame):
        print('Terminate tasks...')
        delete_heroku_server
        print('Done!')
        sys.exit(0)

    signal.signal(signal.SIGINT,signal_handler)
    while True:
        time.sleep(THREAD_SHORT_SLEEP)