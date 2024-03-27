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

class Semaforo(threading.Thread):
    def __init__(self, manager, name):
        super().__init__()
        self.manager = manager
        self.name = name
        self.should_run = True

    def run(self):
        while self.should_run:
            rand = math.floor(random.random() * 3)
            
            if rand == 0:
                chr = ':red_circle:'
            elif rand == 1:
                chr = ':yellow_circle:'
            else:
                chr = ':green_circle:'

            print(f"{self.name} : {emoji.emojize(chr)}")
            manager.increment_ctl()

            time.sleep(1)

    def stop(self):
        self.should_run = False

if __name__ == "__main__":
    manager = Manager()
    semaforo_norte = Semaforo(manager, "Norte")  # Cria um semáforo chamado "Norte" com tempos de duração definidos
    semaforo_sul = Semaforo(manager, "Sul")  # Cria um semáforo chamado "Sul" com tempos de duração definidos
    semaforo_leste = Semaforo(manager, "Leste")  # Cria um semáforo chamado "Leste" com tempos de duração definidos
    semaforo_oeste = Semaforo(manager, "Oeste")  # Cria um semáforo chamado "Oeste" com tempos de duração definidos

    semaforo_norte.start()  # Inicia a execução do semáforo "Norte" em uma thread separada
    time.sleep(0.1)

    semaforo_sul.start()  # Inicia a execução do semáforo "Sul" em uma thread separada
    time.sleep(0.1)

    semaforo_leste.start()  # Inicia a execução do semáforo "Leste" em uma thread separada
    time.sleep(0.1)

    semaforo_oeste.start()  # Inicia a execução do semáforo "Oeste" em uma thread separada
    time.sleep(0.1)
    
    try:
        while True:
            time.sleep(1)  # Aguarda 1 segundo

    except KeyboardInterrupt:
        semaforo_norte.stop()  # Para a execução do semáforo "Norte"
        semaforo_sul.stop()  # Para a execução do semáforo "Sul"
        semaforo_leste.stop()  # Para a execução do semáforo "Leste"
        semaforo_oeste.stop()  # Para a execução do semáforo "Oeste"
        print("Fim da simulação.")

