"""Memória compartilhada protegida por Lock, compatível com Windows."""
import multiprocessing as mp

def incrementar(valor, lock, vezes):
    for _ in range(vezes):
        with lock:
            valor.value += 1

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method("spawn", force=True)
    valor = mp.Value("i", 0)
    lock = mp.Lock()
    processos = [mp.Process(target=incrementar, args=(valor, lock, 10000)) for _ in range(4)]
    for p in processos: p.start()
    for p in processos: p.join()
    print("Valor final esperado=40000; obtido=", valor.value)
