# 合一算法的实现
def is_variable(x):
    # 判断是否为变量
    return isinstance(x, str) and x.islower()

def unify(x, y, subst):
    # 合一算法主函数
    if subst is None:
        return None
    elif x == y:
        return subst
    elif is_variable(x):
        return unify_variable(x, y, subst)
    elif is_variable(y):
        return unify_variable(y, x, subst)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], subst))
    else:
        return None

def unify_variable(var, x, subst):
    # 合一变量
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    elif occurs_check(var, x, subst):
        return None
    else:
        subst[var] = x
        return subst

def occurs_check(var, x, subst):
    # 检查是否发生循环
    if var == x:
        return True
    elif is_variable(x) and x in subst:
        return occurs_check(var, subst[x], subst)
    elif isinstance(x, list):
        return any(occurs_check(var, t, subst) for t in x)
    elif isinstance(x, tuple):
        return occurs_check(var, x[1], subst)
    else:
        return False

# 测试合一算法
if __name__ == "__main__":
    # Test Sample: 
    '''变量名称需满足由小写字母构成，
    谓词名称需要至少含有一个大写字母
    函词用tuple表示'''
    
    term1 = ["Knows", "John", "x"]
    term2 = ["Knows", "John", "Jane"]
    
    # term1 = ["Knows", "John", "x"]
    # term2 = ["Knows", "y", "OJ"]
    
    # term1 = ["Knows", "John", "x"]
    # term2 = ["Knows", "x", "OJ"]
    
    # term1 = ["Knows", "John", "x"]
    # term2 = ["Knows", "y", ("Mother", "y")]
    
    # term1 = ["Knows", "John", "x"]
    # term2 = ["Knows", "y", ("Mother", ("Mother", "y"))]
    
    result = unify(term1, term2, {})
    
    if result is not None:
        print(f"合一成功，替换为: {result}")
    else:
        print("无法合一")