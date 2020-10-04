import numpy as np
import csv


# 读取电路文件，提取信息
def read_revlib(filename):
    """
    :param filename:benchmark文件路径
    :return:文件中的数据(列表)
    """
    data = []
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data


# 获取版本号
def get_version(file_data):
    """
    :param file_data:文件数据(列表)
    :return:版本号version(char)
    """
    version = ''
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:8] == '.version':  # 检测到版本
            ver_str = a[9:]
            version = ver_str.split()  # 存储
            break
        if a[0:4] == '.end':    # 说明没检测到version
            return 0
    return version


# 获取变量数量
def get_numvars(file_data):
    """
    :param file_data:文件数据(列表)
    :return:变量数量numvars(int)
    """
    num = 0
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:8] == '.numvars':  # 检测到变量数量
            num = int(a[9])  # 存储
            break
        if a[0:4] == '.end':    # 说明没检测到numvars
            return 0
    return num


# 获取变量列表
def get_variables(file_data):
    """
    :param file_data:文件数据(列表)
    :return:变量variables(列表)
    """
    index = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:10] == '.variables':  # 检测到变量声明
            var_str = a[11:]
            index = var_str.split()  # 存储
            break
        if a[0:4] == '.end':    # 说明没检测到variables
            return 0
    return index


# 获取输入端列表
def get_inputs(file_data):
    """
    :param file_data:文件数据(列表)
    :return:输入端inputs(列表)
    """
    in_put = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:7] == '.inputs':  # 检测到输入变量
            input_str = a[8:]
            in_put = input_str.split()  # 存储
            break
        if a[0:4] == '.end':    # 说明没检测到inputs
            return 0
    return in_put


# 获取输出端列表
def get_outputs(file_data):
    """
    :param file_data:文件数据(列表)
    :return:输出端outputs(列表)
    """
    out_put = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:8] == '.outputs':  # 检测到输出变量
            output_str = a[9:]
            out_put = output_str.split()  # 存储
            break
        if a[0:4] == '.end':    # 说明没检测到outputs
            return 0
    return out_put


# 获取常量输入列表
def get_constants(file_data):
    """
    :param file_data:文件数据(列表)
    :return:常量输入constants(列表)
    """
    a = []
    const = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:10] == '.constants':  # 检测到常量输入
            const_str = a[11:]
            const = list(const_str)  # 存储
            break
    if a[0:4] == '.end':    # 说明没检测到const
        return 0
    return const


# 获取垃圾输出列表
def get_garbage(file_data):
    """
    :param file_data:文件数据(列表)
    :return:垃圾输出garbage(列表)
    """
    garb = []
    a = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0:8] == '.garbage':  # 检测到垃圾输出
            garb_str = a[9:]
            garb = list(garb_str)  # 存储
            break
    if a[0:4] == '.end':    # 说明没检测到garbage
        return 0
    return garb


# 获取门列表
def get_gates(file_data):
    """
    :param file_data:文件数据(列表)
    :return:量子门gates(列表)
    """
    gates = []
    for m in file_data:  # 遍历文本的每一行
        a = " ".join(m)
        if a[0] != '.' and a[0] != '#':  # 排除注释及其他信息
            gate_str = a[:]
            _gate = gate_str.split()
            gates.append(_gate)  # 用列表存储每一行
        elif a[0:4] == '.end':  # 检测到end
            break  # 退出
    return gates


# 将变量列表与从0开始的数字进行匹配，存到字典中
def create_dict(variables):
    """
    :param variables:变量variables(列表)
    :return:匹配字典dict0
    """
    x = 0
    # 将变量列表与从0开始的数字进行匹配，存到字典中
    dict0 = {}
    for k in variables:
        dict0[k] = x
        x = x + 1
    return dict0


# not
def not_gate(tar, result):
    """
    :param tar:目标位所在线序号
    :param result:经过not门处理后的结果
    :return:None
    """
    if result[tar] == 1:
        result[tar] = 0
    if result[tar] == 0:
        result[tar] = 1


# swap
def swap_gate(tar1, tar2, result):
    """
    :param tar1:目标位1所在线序号
    :param tar2:目标位2所在线序号
    :param result:经过swap门处理后的结果
    :return:None
    """
    in_1 = result[tar1]
    in_2 = result[tar2]
    result[tar1] = in_2
    result[tar2] = in_1


# control-not
def c_not_gate(ctr, tar, result):
    """
    :param ctr:控制位所在线序号
    :param tar:目标位所在线序号
    :param result:经过cnot门处理后的结果
    :return:None
    """
    if result[ctr] == 1:
        if result[tar] == 0:
            result[tar] = 1
        elif result[tar] == 1:
            result[tar] = 0


# double—control-toffoli
def cc_not_gate(ctr1, ctr2, tar, result):
    """
    :param ctr1:控制位1所在线序号
    :param ctr2:控制位2所在线序号
    :param tar:目标位所在线序号
    :param result:经过ccnot门处理后的结果
    :return:None
    """
    if result[ctr1] == 1 and result[ctr2] == 1:
        if result[tar] == 0:
            result[tar] = 1
        elif result[tar] == 1:
            result[tar] = 0


# three—control-toffoli
def ccc_not_gate(ctr1, ctr2, ctr3, tar, result):
    """
    :param ctr1:控制位1所在线序号
    :param ctr2:控制位2所在线序号
    :param ctr3:控制位3所在线序号
    :param tar:目标位所在线序号
    :param result:经过cccnot门处理后的结果
    :return:None
    """
    if result[ctr1] == 1 and result[ctr2] == 1 and result[ctr3] == 1:
        if result[tar] == 0:
            result[tar] = 1
        elif result[tar] == 1:
            result[tar] = 0


# control-swap
def c_swap(ctr, tar1, tar2, result):
    """
    :param ctr:控制位所在线序号
    :param tar1:目标位1所在线序号
    :param tar2:目标位2所在线序号
    :param result:经过cswap门处理后的结果
    :return:None
    """
    if result[ctr] == 1:
        in_1 = result[tar1]
        in_2 = result[tar2]
        result[tar1] = in_2
        result[tar2] = in_1


# 电路运行
def run(circuit, result, dict0):
    """
    :param circuit: 电路列表
    :param result: 更新数组，用于每个门的输入和输出
    :param dict0: 匹配字典
    :return:None
    """
    for i in circuit:
        _Gate = i[0][1]
        if _Gate == '1':
            not_gate(dict0[i[1]], result)
        elif _Gate == '2':
            c_not_gate(dict0[i[1]], dict0[i[2]], result)
        elif _Gate == '3':
            cc_not_gate(dict0[i[1]], dict0[i[2]], dict0[i[3]], result)


# 创建真值表输入端（矩阵表示）
def in_matrix(number):
    """
    :param number:变量数量numvars
    :return:真值表输入端(二维数组)
    """
    in_table = np.empty([0, number], dtype=int)
    if number == 3:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    in_table = np.append(in_table, [[i, j, k]], axis=0)
    if number == 4:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        in_table = np.append(in_table, [[i, j, k, l]], axis=0)
    if number == 5:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        for m in range(2):
                            in_table = np.append(in_table, [[i, j, k, l, m]], axis=0)
    return in_table


# 导入benchmark电路文件，返回该电路真值表输出端
def process(file):
    """
    :param file:benchmark文件路径
    :return:真值表输出端(二维数组)或0(空电路)
    """
    data = read_revlib(file)
    num = get_numvars(data)
    const = get_constants(data)
    gate = get_gates(data)
    garb = get_garbage(data)
    index = get_variables(data)
    dict0 = create_dict(index)
    truth_in = list(in_matrix(num))  # 通过输入变量个数得到真值表的输入端
    # 接下来处理constant输入
    for _in in range(num):      # 对每一位进行判断
        if const != 0:
            if const[_in] == '0':   # 若该位常量输入为0
                truth_in = list(filter(lambda y: y[_in] == 0, truth_in))   # 剔除与常量输入不相符的那一行
            elif const[_in] == '1':     # 若该位常量为1
                truth_in = list(filter(lambda y: y[_in] == 1, truth_in))
            else:
                continue
        else:
            break
    truth_in = np.array(truth_in)
    print("-------输入-------")
    print(truth_in)
    truth_out = []
    # 电路运算
    if len(gate) != 0:
        for i in range(len(truth_in)):
            result = truth_in[i]
            run(gate, result, dict0)
            truth_out.append(result)
    else:
        print("无量子电路")
        return 0
    # 处理垃圾输出
    for _out in range(num):
        if garb != 0:
            if garb[_out] == '1':
                for i in range(len(truth_out)):
                    truth_out[i][_out] = -1
        else:
            break
    truth_out = np.array(truth_out)
    print("-------输出-------")
    print(truth_out)
    return truth_out


# 验证真值表输出端是否相等
def matrix_equal(a, b):
    """
    :param a:真值表输出端1(二维数组)
    :param b:真值表输出端2(二维数组)
    :return:None
    """
    if np.array_equal(a, b):
        print("电路等价")
    else:
        print("电路不等价")
