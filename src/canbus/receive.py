import can
import os

def receive_can_messages(channel):
    print("Bus initialized")

#    os.system('sudo ip link set can0 type can bitrate 100000')
 #   os.system('sudo ifconfig can0 up')

    bus = can.interface.Bus(channel=channel, bustype='socketcan')

    while True:
        message = bus.recv()  # 接收一条CAN消息

        # 处理接收到的消息
        can_id = message.arbitration_id
        data = message.data

        x = int.from_bytes(data[0:2], byteorder='little', signed=True)
        y = int.from_bytes(data[2:4], byteorder='little', signed=True)
        z = int.from_bytes(data[4:6], byteorder='little', signed=True)

        print(f"Received CAN message: ID={can_id:#x}, Data={data}, X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    can_channel = "can0"
    receive_can_messages(can_channel)



