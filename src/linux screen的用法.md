---
layout: post
title: linux screen的用法
slug: screen
date: 2020-07-10 01:12:00
status: publish
author: 半半
categories: 
  - 工具
tags: 
  - screen
excerpt: 使用screen管理会话
---

Screen是一个可以在多个进程之间多路复用一个物理终端的全屏窗口管理器。Screen中有会话的概念，用户可以在一个会话中创建多个screen窗口，在每一个screen窗口中就像操作一个真实的telnet/SSH连接窗口那样。
 通俗的讲，screen命令用于新建一个或多个“命令行窗口”，在新建的这“窗口”中，可以执行命令；每个“窗口”都是独立并行的。

------------------

## 安装screen

### ***Centos***

` yum install screen `

### ***Debian***

`apt-get install screen`

安装中途需要输入y并按回车执行

-------------

## 使用screen

1、创建会话

`screen -S [name]`

2、离开会话

`ctrl+a+d`

依次按

3、恢复创建的会话

`screen -r [name]`

若只有一个会话

`screen -r`

4、查看已经创建的会话

`screen -ls`

5、恢复时出现There is no screen to be resumed matching ****

`screen -d ****`

再使用恢复命令恢复

6、退出screen

在会话中输入

`exit`

7、杀死已经detached的screen会话

`screen -X -S **** quit`

8、其他命令

```
Ctrl + a，d       #暂离当前会话
Ctrl + a，c       #在当前screen会话中创建一个子会话
Ctrl + a，w       #子会话列表
Ctrl + a，p       #上一个子会话
Ctrl + a，n       #下一个子会话
Ctrl + a，0-9     #在第0窗口至第9子会话间切换
```