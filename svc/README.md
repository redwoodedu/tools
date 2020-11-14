# 简易视频剪切点截取

## 简介

此工具源于红杉学社内部项目，帮助视频组确定可剪辑内容。传统方法有以下缺点：
1. 精度最高只能到秒
2. 需要手动写下截取时间点
3. 需要暂停视频
4. 无统一格式
5. 回放编辑麻烦
6. 无法协同工作

## 使用方法

本工具目前只支持Youtube在线浏览，并非专业的视频编辑工具。

### 加载视频

加载视频有三种方法：
1. 直接复制Youtube视频链接（URL）并黏贴到页面顶部的文本框，回车即可。
2. 通过传递URL参数videoId来加载对应视频。
3. 上传通过此工具下载的文件。

### 按键操作

**请勿将Youtube窗口设为焦点，比如鼠标点击暂停，调节分辨率字幕等，按键将无法识别。取消Youtube视窗焦点，可以在页面空白处点击鼠标。**

**安装Vimium或类似插件也会造成按键失效，请禁用或者将以下按键添加到例外中**

* `i`: （in）添加视频片段起始点，重复按下会更新此起始点时间
* `o`: （out）添加视频片段结束点，重复按下会更新结束点时间
* `u`: （undo）删除时间戳中最新添加的片段
* `→`: 视频向前5秒
* `←`: 视频回退5秒
* `space`: (空格)暂停视频

### 文件下载

下载格式为文本文件，文件格式如下：
```
[format],[video id]
start_time,end_time
 ...
```

跟据格式(format)不同，时间的表示方法也有所区别：
* 如果格式为seconds，时间则直接以秒计数
* 如果格式为HHMMSSmmm，则时间为时分秒的形式，如`01:34:20.342`。

视频识别码（video id）会自动添加如何从本工具直接下载。如视频识别码不存在，可手动在页面顶部的文本框中添加。

### 加载文件

有三种加载文件方式：
* 通过本地文件上传，请注意文件格式需要符合如上所述的形式。
* 通过URL。除格式上需要注意外，还需要防止[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors)限制。目前所知Github的raw文件链接可以使用。（已知不可用：PasteBin raw链接）
* 通过链接参数url，但如果videoId的参数也提供了的话，会被url中的数据覆盖。

### 快速剪辑

**需下载[ffmpeg](https://ffmpeg.org/download.html)，并将其添加至系统路径，即在系统命令行/终端中输入ffmpeg可找到此命令**

使用以下命令，可以根据时间戳剪辑成视频：
```
python cutVideoByTimestamps.py 原视频 时间戳文件 [-o 输出文件]
```

默认输出文件为当前文件夹`out.mp4`。

## DEMO

* 时间戳文件: https://raw.githubusercontent.com/NoahDragon/simple-video-cutter/main/sample/timestamps.txt
* 加载视频通过链接参数: https://www.abnerchou.me/simple-video-cutter?videoId=fOmz2fPlyfo
* 加载时间戳文件通过链接参数: https://www.abnerchou.me/simple-video-cutter?url=https://raw.githubusercontent.com/NoahDragon/simple-video-cutter/main/sample/timestamps.txt

## TODO

* 快速剪辑可支持下载Youtube视频选项
* 支持本地视频时间戳制作



