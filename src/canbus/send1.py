import can
import time

def send_can_message(channel, can_id, data):
    bus = can.interface.Bus(channel=channel, bustype='socketcan')
    message = can.Message(arbitration_id=can_id, data=data, is_extended_id=False)
    bus.send(message)
    print(f"发送的消息: {message}")
    bus.shutdown()

if __name__ == '__main__':
    can_channel = 'can0'
    can_id = 0x123
    data = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88]

    send_can_message(can_channel, can_id, data)

