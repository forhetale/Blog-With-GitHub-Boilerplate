# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "forhetale/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "半半's wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-6-20T16:51+08:00"
author = "半半"
email = "banban@forhetale.com"
author_homepage = "https://blog.forhetale.com"
description = "Growth always means change."
key_words = ['Maverick', 'Galileo', 'blog','半半']
language = 'zh-CN'
external_links = [
    {
        "name": "半半's blog",
        "url": "https://blog.forhetale.com",
        "brief": "记录 分享"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/forhetale",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
