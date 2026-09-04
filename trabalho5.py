"""Notificação de evento sem SIGUSR1, compatível com Windows e Unix.

No Windows, SIGUSR1 não existe. Este exemplo usa Event entre processos,
uma alternativa portátil para sinalizar encerramento ou mudança de estado.
"""
import multiprocessing as mp
import time

def trabalhador(evento):
    print("Trabalhador aguardando uma notificação...")
    evento.wait()
    print("Notificação recebida; encerrando com segurança.")

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method("spawn", force=True)
    evento = mp.Event()
    processo = mp.Process(target=trabalhador, args=(evento,))
    processo.start()
    time.sleep(1)
    print("Processo principal enviando a notificação")
    evento.set()
    processo.join()
