import Tkinter
import time
import threading
import random
import Queue


class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        sendButt = Tkinter.Button(master, text='Done', command=send)
        recvButt = Tkinter.Button(master, text='Done', command=recv)
        # console.pack()


    def processIncoming(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply print it
                print msg
            except Queue.Empty:
                pass


class ThreadedClient:
    def __init__(self, master):
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        if not self.running:

            import sys
            sys.exit(1)
        self.master.after(100, self.periodicCall)

    def workerThread1(self):

        while self.running:
            time.sleep(rand.random() * 0.3)
            msg = rand.random()
            self.queue.put(msg)

    # def endApplication(self):
    #     self.running = 0


rand = random.Random()
root = Tkinter.Tk()

client = ThreadedClient(root)
root.mainloop()
