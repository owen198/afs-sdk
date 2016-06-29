# 构建一个Python模块
This is a HelloWorld project, as a template for describle how to build a python module package.

## 步骤

1. git clone https://github.com/wangdiwen/setup_py_helloworld
2. cd setup_py_helloworld
3. python setup.py sdist
4. 执行1-3后，在dist目录下会出现 xxx.tar.gz

## 使用
- 拿到xxx.tar.gz后，解压；
- python setup.py install

```
# python
import helloworld
>>> from helloworld import say
>>> say.hi()
Hello World.
```
