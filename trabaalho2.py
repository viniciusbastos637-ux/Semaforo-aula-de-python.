"""Cliente e servidor TCP local, compatível com Windows."""
import socket
import threading

def servidor(pronto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 0))
        s.listen(1)
        pronto.append(s.getsockname()[1])
        evento.set()
        conn, _ = s.accept()
        with conn:
            dados = conn.recv(1024)
            conn.sendall(b"ACK:" + dados)

if __name__ == "__main__":
    evento = threading.Event()
    porta = []
    thread = threading.Thread(target=servidor, args=(porta,), daemon=True)
    thread.start()
    evento.wait()
    with socket.create_connection(("127.0.0.1", porta[0]), timeout=5) as cliente:
        cliente.sendall(b"mensagem TCP")
        print(cliente.recv(1024).decode("utf-8"))
    thread.join()
