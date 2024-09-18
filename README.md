# FOL-Unification
一阶谓词逻辑中合一算法的python实现
注意：算法的输入由term1和term2两个项以及替换集subst构成，term中的变量名称需满足由小写字母构成，谓词名称需要至少含有一个大写字母，函词用tuple表示
Demo 1:
term1 = Knows(John, x) = ["Knows", "John", "x"]
term2 = Knows(John, Jane) = ["Knows", "John", "Jane"]

Demo 2:
term1 = Knows(John, x) = ["Knows", "John", "x"]
term2 = Knows(y, Mother(y)) = ["Knows", "y", ("Mother", "y")]
