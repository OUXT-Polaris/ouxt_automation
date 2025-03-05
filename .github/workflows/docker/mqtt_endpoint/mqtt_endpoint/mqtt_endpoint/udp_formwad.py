import socket

def udp_forwarder(listen_ip, listen_port, forward_ip, forward_port):
    """UDPパケットを転送する関数"""
    # 受信ソケットの作成
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_socket.bind((listen_ip, listen_port))

    # 転送先ソケットの作成
    forward_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"UDPパケット転送を開始します: {listen_ip}:{listen_port} -> {forward_ip}:{forward_port}")

    while True:
        # パケットを受信
        data, addr = listen_socket.recvfrom(1024)  # 1024はバッファサイズ

        # 受信したパケットを転送
        forward_socket.sendto(data, (forward_ip, forward_port))

        print(f"パケットを転送しました: {addr} -> {forward_ip}:{forward_port}")

if __name__ == "__main__":
    listen_ip = "0.0.0.0"  # 受信IPアドレス (すべてのインターフェース)
    listen_port = 5000  # 受信ポート番号
    forward_ip = "192.168.1.100"  # 転送先IPアドレス
    forward_port = 6000  # 転送先ポート番号

    udp_forwarder(listen_ip, listen_port, forward_ip, forward_port)
