import threading
import time
from uuid import getnode as get_mac
import requests
import time
import json

DEFAULT_URL='http://127.0.0.1:8000/license/?format=json&machine_id='

class LicensingManager(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=240):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.mac = get_mac()

        self.url = DEFAULT_URL + str(self.mac)

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Verify license')

            response = requests.get(self.url)
            json_data = json.loads(response.text)
            if len(json_data) > 0:
                if int(json_data[0]["machine_id"]) == self.mac:
                    time.sleep(self.interval)
                    continue
                else:
                    raise RuntimeError('bye')
            else:
                raise RuntimeError('bye')

