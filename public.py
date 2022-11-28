# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import time
import sys
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_subscribe(client,userdata,mid,granted_qos):
    print("消息发送成功")


client = mqtt.Client(protocol=3)
client.username_pw_set("admin", "password")
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.connect(host="8.134.153.175", port=1883, keepalive=60)  # 订阅频道
time.sleep(1)
i = 0


# 循环发布消息
while True:
    try:
        # 发布MQTT信息
        sensor_data = "test" + str(i)
        client.publish(topic="public", payload=sensor_data, qos=0)
        time.sleep(1)
        i += 1
    except KeyboardInterrupt:
        print("EXIT")
        client.disconnect()
        sys.exit(0)
