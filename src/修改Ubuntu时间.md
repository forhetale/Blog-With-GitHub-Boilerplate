---
layout: post
title: Ubuntu修改时间
slug: ubuntu-time
date: 2020/07/10 00:36:00
status: publish
author: 半半
categories: 
  - 系统
tags: 
  - Ubuntu
excerpt: 修改Ubuntu时区以达到目的
---

# Ubuntu修改时间

Ubuntu时钟分为系统时钟（System Clock）和硬件（Real Time Clock，简称RTC）时钟。

```
查看系统时间：date -R
```

```
查看硬件时间: sudo hwclock --show
```

-----------------

## 修改Ubuntu系统时间

### 修改时间

```
tzselect  
```

依次选择4->9->1->1  *Asia->China->Beijing->yes*

### 复制文件到/etc目录下

```
sudo cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
```

### 查看修改结果

```
date -R
```

---------------

## 修改Ubuntu硬件时间

```
sudo date -s MM/DD/YY //修改日期
sudo date -s hh:mm:ss //修改时间
sudo hwclock --systohc //修改生效
```

-------------------

转载自：https://www.jianshu.com/p/a6a6dde68b91