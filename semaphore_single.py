import threading
import time
import emoji
import random
import math

class Manager():
    def __init__(self, ctl = 0, max = 4):
        self.ctl = ctl
        self.max = max

    def increment_ctl(self):
        self.ctl = (self.ctl + 1) % 4

        if self.ctl == 0:
            print("\n")

class Semaforo():
    def __init__(self, manager, names):
        self.manager = manager
        self.names = names
        self.should_run = True

    def run(self):
        while self.should_run:
            for name in self.names:
                rand = math.floor(random.random() * 3)
            
                if rand == 0:
                    chr = ':red_circle:'
                elif rand == 1:
                    chr = ':yellow_circle:'
                else:
                    chr = ':green_circle:'

                print(f"{name} : {emoji.emojize(chr)}")
                manager.increment_ctl()

                time.sleep(1)

    def stop(self):
        self.should_run = False

if __name__ == "__main__":
    manager = Manager()
    semaforo = Semaforo(manager, ["Norte", "Sul", "Leste", "Oeste"])

    semaforo.run()

    try:
        while True:
            time.sleep(4)  # Aguarda 1 segundo

    except KeyboardInterrupt:
        semaforo.stop()  # Para a execução do semáforo "Norte"
        print("Fim da simulação.")

