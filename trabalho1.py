"""Pipe bidirecional entre processos, compatível com Windows."""
import multiprocessing as mp

def trabalhador(conn):
    try:
        mensagem = conn.recv()
        print(f"Filho recebeu: {mensagem}")
        conn.send(mensagem.upper())
    finally:
        conn.close()

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method("spawn", force=True)
    pai, filho = mp.Pipe()
    processo = mp.Process(target=trabalhador, args=(filho,))
    processo.start()
    filho.close()
    pai.send("dados via pipe")
    print("Pai recebeu:", pai.recv())
    pai.close()
    processo.join()
