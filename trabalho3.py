"""Fila de mensagens entre processos, compatível com Windows."""
import multiprocessing as mp

def produtor(fila):
    for item in ["A", "B", "C"]:
        fila.put(item)
    fila.put(None)

def consumidor(fila):
    while True:
        item = fila.get()
        if item is None:
            break
        print("Consumidor processou", item)

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method("spawn", force=True)
    fila = mp.Queue()
    p1 = mp.Process(target=produtor, args=(fila,))
    p2 = mp.Process(target=consumidor, args=(fila,))
    p1.start(); p2.start()
    p1.join(); p2.join()
    fila.close(); fila.join_thread()
