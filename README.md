# PythonDemo
## 简介
由三部分组成分别问爬虫服务器（crawler_server），
爬虫客户端(crawler_client)，网页服务器(server)

## 环境
Linux version 4.15.0-118-generic (buildd@lgw01 -amd64-039)

python3.8, django3.0, zookeeper, mysql

## 使用
使用docker部署，启动顺序为（zookeeper，mysql）-（crawler_server）- (crawler_client, server)

example可由dockerfile与docker-compose依次按上面顺序进行启动

Demo/ docker-compose up -d （启动zookeeper,mysql）

Demo/crawler/crawler_server docker build -t c_server .

Demo/crawler/crawler_server docker run -d --network demo_default c_server (启动爬虫服务器)

....依次启动使用同一网桥即可

crawler_client是交互界面，启动需执行 docker run -it 进行启动命令例如  

(get all)查询所有服务器        (get uid 1 2)获得uid1，2的数据   

(set mysql)修改指定数据库   (set thread 3)修改线程数  

(set thread 000000001 3)修改指定服务器的线程数

## 实现
zookeeper主要目的为实现分布式锁，数据库的不停机切换，爬虫客户端与爬虫服务器之间的解耦，可以加入爬虫服务器进行分布式爬取等

crawler_server部分功能做相应优化如采用池化技术，如线程池与数据库连接池防止重复创造，销毁带来的性能损耗，数据库连接池使用队列的形式保存资源，保证资源同一时刻只被单一占有

server使用django框架作为网页服务器

## 流程
crawler_client输入想获取的用户uid，并以随机分配的形式挑选结点进行保存，监听该结点的crawler_server唤醒先通过其id获取分布式锁，防止处理过程中客户端对该结点重新设置导致资源丢失, 
crawler_server获取用户uid后，生成该uid对应的task，随后将其加入到线程池进行消费，task再向连接池获取连接将数据保存在数据库。最后由server从数据库
中获取用户uid数据以网页的形式呈现
