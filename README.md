# LPTHW (Learn Python The Hard Way)

学习环境：Windows 10 & Anaconda with Python 3.7

文本编辑器 & 终端： Notepad++ & Cmder（需要将 Anaconda 文件夹地址放入 PATH 中）

参考资料：
- *Learn Python The Hard Way (LPTHW)*
- *Learn Python 3 The Hard Way (LP3THW)*
- *Learn More Python 3 The Hard Way (LMP3THW)*

## 我的 Python 学习之路

没有什么半途而废，只是暂时歇息而已~

那些成功坚持下来的人，平均“放弃”过 5 次~

- 2017
	- 7.28 - 8.3：学习 LPTHW ex1-21
	- 8.4：整理 LPTHW ex1-21  [学习笔记（with python 2）](https://github.com/lctfwyt/LPTHW/blob/master/studynotes.md)
	- 8.7：开始学习 [开智学堂 Python 基础班四期](https://detail.youzan.com/show/goods?alias=2xlc5axxl5m8h)，对新手不友好，2w 就掉队了 _(:з」∠)_
	- 学习 LPTHW ex22 之后的一些章节，日期和进度无记录
- 2018
	- 7.22 - 11.5 学习 [ANU COMP1100](https://cs.anu.edu.au/courses/comp1100/) ([alt](https://programsandcourses.anu.edu.au/2018/course/COMP1100))，学的是 Haskell 不是 Python，让我在编程方面真正入门了
	- 11.16 - 22：学习 [Coursera Interactive Python 1](https://www.coursera.org/learn/interactive-python-1) week 0-1
	- 11.28 - 12.1、12.10：将 ex1-21 更新到 LP3THW 版本（with python 3）
- 2019
	- 1.23 - 2.8：学习 [Coursera Interactive Python 1](https://www.coursera.org/learn/interactive-python-1) week 2-4
	- 2.8 - 12：学习 [Coursera Interactive Python 2](https://www.coursera.org/learn/interactive-python-2) week 5a
	- 2.8 - 9、3.2、3.13 - 17、4.5 - 9：学习 [Udacity 数据科学入门](https://cn.udacity.com/course/intro-to-data-science--ud359) Lesson 1-9.10
	- 2.26 - 6.14：学习 [ANU COMP2420](https://cs.anu.edu.au/courses/comp2420/) ([alt](https://programsandcourses.anu.edu.au/2019/course/COMP2420))
	- 12.1 - 6、12.9 - 10：复习 LP3THW ex01-21 并整理笔记（如下）
	- 12.11 - 12：学习 LP3THW ex23-31

## 学习笔记目录

- LP3THW
	- [**Exercise 0** The Setup](#Exercise-0-The-Setup)
	- [**Exercise 1** A Good First Program](#Exercise-1-A-Good-First-Program)
	- [**Exercise 2** Comments and Pound Characters](#Exercise-2-Comments-and-Pound-Characters)
	- [**Exercise 3** Numbers and Math](#Exercise-3-Numbers-and-Math)
	- [**Exercise 4** Variables and Names](#Exercise-4-Variables-and-Names)
	- [**Exercise 5** More Variables and Printing](#Exercise-5-More-Variables-and-Printing)
	- [**Exercise 6** Strings and Text](#Exercise-6-Strings-and-Text)
	- [**Exercise 7** More Printing](#Exercise-7-More-Printing)
	- [**Exercise 8** Printing, Printing](#Exercise-8-Printing-Printing)
	- [**Exercise 9** Printing, Printing, Printing](#Exercise-9-Printing-Printing-Printing)
	- [**Exercise 10** What Was That?](#Exercise-10-What-Was-That)
	- [**Exercise 11** Asking Questions](#Exercise-11-Asking-Questions)
	- [**Exercise 12** Prompting People](#Exercise-12-Prompting-People)
	- [**Exercise 13** Parameters, Unpacking, Variables](#Exercise-13-Parameters-Unpacking-Variables)
	- [**Exercise 14** Prompting and Passing](#Exercise-14-Prompting-and-Passing)
	- [**Exercise 15** Reading Files](#Exercise-15-Reading-Files)
	- [**Exercise 16** Reading and Writing Files](#Exercise-16-Reading-and-Writing-Files)
	- [**Exercise 17** More Files](#Exercise-17-More-Files)
	- [**Exercise 18** Names, Variables, Code, Functions](#Exercise-18-Names-Variables-Code-Functions)
	- [**Exercise 19** Functions and Variables](#Exercise-19-Functions-and-Variables)
	- [**Exercise 20** Functions and Files](#Exercise-20-Functions-and-Files)
	- [**Exercise 21** Functions Can Return Something](#Exercise-21-Functions-Can-Return-Something)
	- [**Exercise 22** What Do You Learn So Far?](#Exercise-22-What-Do-You-Learn-So-Far)

## Exercise 0 The Setup

- 一些终端指令
	- 进入 python `python`，退出 python `quit()` `exit()` `Ctrl+Z`
	- 新建文件夹`mkdir xxx`，进入文件夹`cd xxx`
	- 列出当前文件夹中的所有文件和文件夹`ls`/`dir`
	- 更多指令见课本附录
- 切换窗口
	- 切换到上一个窗口`Alt+Tab`
	- 按住`Alt`，按 n 次`Tab`，松开`Alt`切换到上 n 个窗口
	- 按住`Alt`，按一次`Tab`，左右键选择目标窗口，松开`Alt`
- 总之，不许用 IDE，233
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 1 A Good First Program

- 打印`print(...)`
- 字符串`"..."` `'...'`
- 在终端中运行 py 文件`python xxx.py`
- 什么都不打印也会占用一行`print()`/`print("")`

## Exercise 2 Comments and Pound Characters

- 注释`# ...`，可作解释说明，或暂时不运行一行代码
- 字符串中的井号不会被当作注释`"#"`

## Exercise 3 Numbers and Math

- 加减乘除和余数`+` `-` `*` `/` `%`，遵循数学中的运算符号顺序
- 整型相除得浮点型，如是整数，后加`.0`
- 不等号`<` `>` `<=` `>=`，运行不等式得布尔型`True`/`False`
- 打印多个东西`print(..., ..., ...)`，会有空格隔开它们

## Exercise 4 Variables and Names

- 给变量赋值`x = ...`
- 下划线`_`可用在变量名中作空格

## Exercise 5 More Variables and Printing

- 格式化字符串`f"...{var_name}..."`将变量嵌入字符串
- 四舍五入
	- `round(1.7333)`取整得 `2`
	- `round(1.7333, 2)`留小数点后 2 位得 `1.73`
- 只有加`print()`的表达式才会在代码运行后显示
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 6 Strings and Text

- 将变量/表达式嵌入字符串的另一种方式`"...{}...".format(...)`
- 无缝拼接字符串`"..." + "..."`

## Exercise 7 More Printing

- 无缝拼接同一字符串 n 次`"..." * n`
- `print(..., end = ' ')`与下一行要打印的东西以空格连接，不转行

## Exercise 8 Printing, Printing

- 将多个变量/表达式嵌入字符串`"{}{}{}".format(..., ..., ...)`

## Exercise 9 Printing, Printing, Printing

- 转义字符`\n`：换行符
- 多行字符串`"""..."""` `'''...'''`

## Exercise 10 What Was That?

- 转义字符
	- `\t`：横向制表符（`Tab`键）
	- `\\`：普通`\`字符
	- `\'` `\"`：普通`'` `"`字符
- 在字符串中输入引号的方法
	1. 在双/单引号字符串中输入单/双引号
	2. 使用转义字符
	3. 使用多行字符串
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 11 Asking Questions

- 获取用户输入的内容（字符串）`x = input()`
- 转换`x`的数据类型为整型`int(x)`

## Exercise 12 Prompting People

- `x = input("...? ")`等价于`print("...?", end = ' '); x = input()`
- 阅读 python 文档`python -m pydoc xxx`
	- 假如文档太长：`Enter`键下滚，`q`键退出

## Exercise 13 Parameters, Unpacking, Variables

- 导入`sys`模块中的`argv`函数`from sys import argv`
- `argv`返回一个列表，储存运行 py 文件时跟在`python`后面的参数字符串们
	- `argv`中储存的第一个参数是所运行的 py 文件名
- 解包`argv`，即将其中储存的字符串赋值给变量`x, y, z = argv`
	- 解包时变量数和`argv`中的参数数必须一致，否则报错
- 也可以直接用列表索引`argv[0]` `argv[1]` `argv[2]`

## Exercise 14 Prompting and Passing

- 将提示词赋值给变量`prompt = ' >`，之后一律`input(prompt)`
	- 如需更换所有问题的提示词，在赋值处更改一次即可

## Exercise 15 Reading Files

- 打开文件并返回文件本身`open(filename)`
	- `filename`是字符串，比如`"ex15_sample.txt"`
	- 文件可被多次打开，不报错
	- 文件可被赋值`file = open(filename)`
- 读取并返回文件内容（字符串）`file.read()`
	- 可被打印`print(file.read())`
	- 第二次使用`file.read()`就只返回空字符串
	- 因为上一次阅读后，“光标”停在了文件末尾
	- 文件被关闭再打开，“光标”会回到开头
- 关闭文件`file.close()`
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 16 Reading and Writing Files

- 文件内容（字符串）`file.read()`可被赋值
- 仅读取并返回一行（字符串）`file.readline()`
	- 见`'\n'`停，包括`'\n'`
	- “光标”停在下一行开头，再次调用返回下一行
- 清空文件内容`file.truncate()`，**要小心！**
	- `'w'` `'w+'`模式下不需要使用
	- 只有“光标”在文件开头才能用，返回`0`，否则返回`99`
- 将`'stuff'`写入文件`file.write('stuff')`
- “光标”返回至开头`file.seek(0)`
- `input()`可以让用户做决定，`Enter`继续运行，`Ctrl+C`中断运行
- `open(filename)`默认以只读模式`'r'`打开文件
	- 如文件不存在，报错
	- 如文件存在，“光标”在文件开头
	- 只可读取内容，不可写入或清空内容
- 以只写模式打开文件`open(filename, 'w')`
	- 如文件不存在，创建文件
	- 如文件存在，清空文件内容，**要小心！**
	- 只可写入内容，不可读取内容
- 以追加模式打开文件`open(filename, 'a')`
	- 如文件不存在，创建文件
	- 如文件存在，“光标”在文件末尾
	- 只可写入内容，不可读取内容
- 读写模式，可读亦可写`'r+'` `'w+'` `'a+'`
	- `'r+'`在`'r'`基础上增加写入功能，从开头写入，写多少覆盖多少
	- `'w+'`/`'a+'`在`'w'`/`'a'`基础上增加读取功能

## Exercise 17 More Files

- `data = open(filename).read()`等价于`file = open(filename); data = file.name()`
	- 这样就无需`file.close()`了，python 会帮你关闭文档
	- 多行代码可通过代入/嵌套的方式或加`;`的方式变为一行，但会变得很难读
- 返回字符串的长度（字节数）`len()`
- `from os.path import exists`检查文件是否存在`exist(filename)`，返回布尔值
- 在终端创建并将内容写入文件`echo ...> xxx.text`
	- 课本上是`echo "..." > xxx.txt`，但我这里会将引号和大于号前的空格也写入
- 在终端读取文件内容`cat xxx.txt`返回`...`
- 在我的终端无法用`man cat`查看帮助文档，`help cat`也会显示对此命令不支持，辣鸡 Windows ...
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 18 Names, Variables, Code, Functions

- 定义函数：
```
def function_name(arg1, arg2, ...):
	...
	...
```
- 要点：
	- 以`def`开头
	- 函数名以字母开头，只能由字母、数字、下划线构成，和变量名一样
	- 函数名和`(`之间没空格
	- 参数名不可重复
	- 参数可被打包为`(*xxx)`，解包`arg1, arg2, ... = xxx`，类似于`argv`，不过通常不是必需的
	- 参数个数可为 0
	- 参数写完写`):`
	- `:`之后缩进 4 格的代码行表示它们都是这个函数定义的一部分
	- 不再缩进的代码行即为函数定义的结束（不包括这一行）
- 调用函数：函数名，`(`，被`,`隔开的参数值，`)`
- 之前见到的`exists` `open`等都是函数

## Exercise 19 Functions and Variables

- 传入函数的参数值可以是：
	- 值
	- 变量
	- 值的数学运算表达式
	- 值和变量的数学运算表达式
- 只要是能被赋值给变量的，都能作为参数被传入函数
- 避免（全局）变量和函数中的参数（局部变量）同名
- 函数中可以调用函数
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[[返回顶部]](#LPTHW-Learn-Python-The-Hard-Way)

## Exercise 20 Functions and Files

- `x += y`等价于`x = x + y`

## Exercise 21 Functions Can Return Something

- 函数定义中`return`后面跟着的是函数返回值，相当于给函数赋值
- 转换`x`的数据类型为浮点型`float(x)`

## Exercise 22 What Do You Learn So Far?

- 复习课，笔记略
- 复习的时候，每 15 分钟休息一下，这样会学得更快、挫败感更少
