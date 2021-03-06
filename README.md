# Bull #

基于pyqt4的gui选股神器, 使用scrum方法开发. scrum管理工具为version one.

## 特性 ##

- 根据股票基础数据的范围搜索符合条件的股票
- 保存选取条件
- 缓存与更新本地股票数据
- 多个网站数据来源(目前支持同花顺和雪球)

## 环境 ##
主要为win32环境适配, 其他平台跑不起来也不要来找我 - -

### 依赖 ###

- [Python2.7](https://www.python.org/download/releases/2.7/)
- [PyQt4.11.3](http://www.riverbankcomputing.com/software/pyqt/download)
- [py2exe0.6.9](http://www.py2exe.org/)
- [PyCurl](http://www.py2exe.org/)
- [SIP](https://pypi.python.org/pypi/SIP)

py2exe后在win xp, win7, win8下运行正常.

## 目录结构 ##

```
- master/                      主分支
    +- bull/                   源文件
        +- setup.py            py2exe的setup
        +- main.py             主程序入口
        +- build.bat           py2exe批处理, 生成运行文件
        +- images/             图片
        +- view/               view层代码, 即GUI
        +- controller/         controller层代码
        +- service/            service层代码
        +- dao/                dao层代码
        +- model/              model层代码
        +- util/               一些通用工具
        +- setting.json        配置文件
        +- default.qss         样式表
        +- bull.py             主程序入口
        +- fav.json            用户收藏
        +- xxx_title.json      不用来源的网站的指标的id与中文对应
    +- docs/                   文档
        +- task/               任务描述
        +- backlog/            backlog
```

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          87            579            385           3748
JSON                             6              2              0            175
DOS Batch                        1              0              0              2
-------------------------------------------------------------------------------
SUM:                            94            581            385           3925
-------------------------------------------------------------------------------
```

## 效果图
**主界面:**
![效果图](./effect_picture1.png)
**筛选结果:**
![效果图](./effect_picture2.png)