
## Ubuntu下安装EMQX
[下载 EMQX](https://www.emqx.io/zh/downloads?os=Ubuntu)


>1.配置 EMQX Apt 源
>curl -s https://assets.emqx.com/scripts/install-emqx-deb.sh | sudo bash
>2.安装 EMQX
>sudo apt-get install emqx
>3.启动 EMQX
>sudo systemctl start emqx

启动：emqx start
停止：emqx stop

在云服务器控制台开启端口18083和1883
![[Pasted image 20221124150749.png]]


安装MQTT客户端
[MQTT X: Cross-platform MQTT 5.0 Desktop Client](https://mqttx.app/)

连接到云服务器

![[Pasted image 20221124151027.png]]

公网IP:18083打开EMQX网页配置

![[Pasted image 20221124151459.png]]


点击连接，默认Websockets的端口号是8083，记得在云服务器控制台上开启相应端口号
![[Pasted image 20221124151651.png]]

订阅主题：主题名字取决于在MQTT发布的名称


发布端点击发送
![[Pasted image 20221124151901.png]]

接收端立即显示接收数据：
![[Pasted image 20221124151951.png]]

反过来同理，双方均可以是发布端Public也可以是订阅者subscribe，只要主题名字统一便可进行通信。


sudo pip install  pythonpackages

sudo apt upgrade
sudo apt-get ##








