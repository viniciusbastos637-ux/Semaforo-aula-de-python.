"""Prevenção de deadlock por ordem global e timeout, compatível com Windows."""
from threading import Lock, Thread
import time

LOCK_A = Lock()
LOCK_B = Lock()

def tarefa(nome, primeiro, segundo):
    with primeiro:
        time.sleep(0.05)
        if segundo.acquire(timeout=0.2):
            try:
                print(nome, "obteve os dois locks")
            finally:
                segundo.release()
        else:
            print(nome, "detectou possível espera circular; abortou")

if __name__ == "__main__":
    # As duas threads adquirem primeiro LOCK_A: a ordem global evita ciclo.
    t1 = Thread(target=tarefa, args=("T1", LOCK_A, LOCK_B))
    t2 = Thread(target=tarefa, args=("T2", LOCK_A, LOCK_B))
    t1.start(); t2.start(); t1.join(); t2.join()
