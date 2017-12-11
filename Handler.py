import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher():
    DIRECTORY_TO_WATCH = "C:/Users/pandu/Desktop/txt"


    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH,
                               recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        print event.event_type
        # if event.is_directory:
            # return None

        if event.event_type == 'created':
            print "Received created event - %s." % event.src_path

        elif event.event_type == 'modified':
            print "Received modified event - %s." % event.src_path

        elif event.event_type == 'moved':
           print "Received rename event - %s." % event.src_path

        elif event.event_type == 'deleted':
            print "Received deleted event - %s." % event.src_path


    @staticmethod
    def on_moved(event):
        print event.event_type
        print "received rename event -%s" % event.src_path

# f = open('newfile',"wb")
# f.seek(1073741824-1)
# f.write("\0")
# f.close()

    #
    # for i in range(0, 100):
    #     print i
    # path = "/home/harikumar/Desktop/test1"
    # if not os.path.exists(path):
    #     os.makedirs(path)
    #
    # k = os.path.join(path, str(i))
    # if not os.path.exists(k):
    #     os.makedirs(k)
    # #f = open(os.path.join(k, str(i)+".txt"), "a")


if __name__ == '__main__':
    w = Watcher()
    w.run()
