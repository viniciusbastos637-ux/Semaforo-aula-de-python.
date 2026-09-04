"""Produtor-consumidor com Condition; executa em Windows, sem subprocessos."""
from collections import deque
from threading import Condition, Thread
import time

buffer = deque()
condicao = Condition()
CAPACIDADE = 2

def produtor():
    for item in range(5):
        with condicao:
            while len(buffer) == CAPACIDADE:
                condicao.wait()
            buffer.append(item)
            print("produziu", item)
            condicao.notify_all()
        time.sleep(0.1)

def consumidor():
    for _ in range(5):
        with condicao:
            while not buffer:
                condicao.wait()
            item = buffer.popleft()
            print("consumiu", item)
            condicao.notify_all()
        time.sleep(0.2)

if __name__ == "__main__":
    produtor_thread = Thread(target=produtor)
    consumidor_thread = Thread(target=consumidor)
    produtor_thread.start(); consumidor_thread.start()
    produtor_thread.join(); consumidor_thread.join()
