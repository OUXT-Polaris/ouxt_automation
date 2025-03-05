import socket
import argparse

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
    parser = argparse.ArgumentParser(description="UDPパケット転送ツール")
    parser.add_argument("forward_ip", help="転送先IPアドレス")
    parser.add_argument("forward_port", type=int, help="転送先ポート番号")
    parser.add_argument("--listen_port", type=int, default=5000, help="リッスンポート番号 (デフォルト: 5000)")
    parser.add_argument("--listen_ip", default="0.0.0.0", help="リッスンIPアドレス (デフォルト: 0.0.0.0)")

    args = parser.parse_args()

    udp_forwarder(args.listen_ip, args.listen_port, args.forward_ip, args.forward_port)
