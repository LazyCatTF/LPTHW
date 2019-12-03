# LPTHW (Learn Python The Hard Way) 学习笔记

学习环境：Windows 10 & Anaconda with Python 3.7

文本编辑器 & 终端： Notepad++ & Cmder（需要将 Anaconda 文件夹地址放入 Path 中）

参考资料：
- *Learn Python The Hard Way (LPTHW)*
- *Learn Python 3 The Hard Way (LP3THW)*
- *Learn More Python 3 The Hard Way (LMP3THW)*

## 我的 Python 学习之路

没有什么半途而废，只是暂时歇息而已~

- 2017
	- 7.28 - 8.3：学习 LPTHW ex1-21
	- 8.4：整理 LPTHW ex1-21 学习笔记 [studynotes.md](https://github.com/lctfwyt/LPTHW/blob/master/studynotes.md)
- 2018
	- 11.16 - 22：学习 [Interactive Python 1](https://www.coursera.org/learn/interactive-python-1) week 0-1
	- 11.28 - 12.1、12.10：将 ex1-21 更新到 LP3THW 版本
- 2019
	- 1.23 - 2.8：学习 [Interactive Python 1](https://www.coursera.org/learn/interactive-python-1) week 2-4
	- 2.8 - 12：学习 [Interactive Python 2](https://www.coursera.org/learn/interactive-python-2) week 5a
	- 2.8 - 9、3.2、3.13 - 17、4.5 - 9：学习 [数据科学入门](https://cn.udacity.com/course/intro-to-data-science--ud359) Lesson 1-9.10
	- 2.26 - 6.14：学习 [ANU COMP2420](https://cs.anu.edu.au/courses/comp2420/) ([alt](https://programsandcourses.anu.edu.au/2019/course/COMP2420))
	- 12.1 - 3：复习 LP3THW ex01-10

## 目录

- LP3THW
	- [**Exercise 0** The Setup](#Exercise-0-The-Setup)
	- [**Exercise 1** A Good First Program](#Exercise-1-A-Good-First-Program)
	- [**Exercise 2** Comments and Pound Characters](#Exercise-2-Comments-and-Pound-Characters)
	- [**Exercise 3** Numbers and Math](#Exercise-3-Numbers-and-Math)
	- [**Exercise 4** Variables and Names](#Exercise-4-Variables-and-Names)
	- [**Exercise 5** More Variables and Printing](#Exercise-5-More-Variables-and-Printing)
	- [**Exercise 6** Strings and Text](#Exercise-6-Strings-and-Text)
	- [**Exercise 7** More Printing](#Exercise-7-More-Printing)
	- [**Exercise 8** Printing, Printing](#Exercise-8-Printing,-Printing)
	- [**Exercise 9** Printing, Printing, Printing](#Exercise-9-Printing,-Printing,-Printing)
	- [**Exercise 10** What Was That?](#Exercise-10-What-Was-That?)

## Exercise 0 The Setup

- 一些终端指令
	- 进入 Python `python`，退出 Python `quit()` `exit()` `Ctrl+Z`
	- 新建文件夹`mkdir xxx`，进入文件夹`cd xxx`
	- 列出当前文件夹中的所有文件和文件夹`ls`/`dir`
	- 更多指令见课本附录
- 切换窗口
	- 切换到上一个窗口`Alt+Tab`
	- 按住`Alt`，按 n 次`Tab`，松开`Alt`切换到上 n 个窗口
	- 按住`Alt`，按一次`Tab`，左右键选择目标窗口，松开`Alt`
- 总之，不许用 IDE，233

## Exercise 1 A Good First Program

- 打印`print(...)`
- 字符串`"..."` `'...'`
- 在终端中运行写好的代码`python xxx.py`
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

- 给变量赋值`var_name = ...`
- 下划线`_`可用在变量名中作空格

## Exercise 5 More Variables and Printing

- 格式化字符串`f"...{var_name}..."`将变量嵌入字符串
- 四舍五入
	- `round(1.7333)`取整得 `2`
	- `round(1.7333, 2)`留小数点后 2 位得 `1.73`
- 只有加`print()`的表达式才会在代码运行后显示

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