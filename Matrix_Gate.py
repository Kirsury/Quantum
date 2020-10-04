import numpy as np

qbit_0 = [[1], [0]]
qbit_1 = [[0], [1]]


Result = ['|1>', '|0>', '|1>']  # 创建一个列表存放初始输入


def not_gate(tar):
    gate_matrix = [[0, 1],
                   [1, 0]]
    m1 = [[1], [0]]
    m2 = [[0], [1]]
    in_1 = Result[tar]
    if in_1 == '|1>':
        out_1 = np.dot(gate_matrix, qbit_1)
    elif in_1 == '|0>':
        out_1 = np.dot(gate_matrix, qbit_0)
    if (out_1 == m1).all():
        Result[tar] = '|0>'
    if (out_1 == m2).all():
        Result[tar] = '|1>'


def swap_gate(tar1, tar2):
    in_1 = Result[tar1]
    in_2 = Result[tar2]
    Result[tar1] = in_2
    Result[tar2] = in_1


def c_not_gate(ctr, tar):			# ctr:控制位位置 tar:目标位位置
    gate_matrix = [[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 1, 0]]
    m1 = [[1], [0], [0], [0]]
    m2 = [[0], [1], [0], [0]]
    m3 = [[0], [0], [1], [0]]
    m4 = [[0], [0], [0], [1]]
    in_ctr = Result[ctr]
    in_tar = Result[tar]
    if in_ctr == '|0>' and in_tar == '|0>':
        tensor_pro = np.kron(qbit_0, qbit_0)
    if in_ctr == '|1>' and in_tar == '|1>':
        tensor_pro = np.kron(qbit_1, qbit_1)
    if in_ctr == '|0>' and in_tar == '|1>':
        tensor_pro = np.kron(qbit_0, qbit_1)
    if in_ctr == '|1>' and in_tar == '|0>':
        tensor_pro = np.kron(qbit_1, qbit_0)

    out = np.dot(gate_matrix, tensor_pro)

    if (out == m1).all():
        Result[ctr] = '|0>'
        Result[tar] = '|0>'
    elif (out == m2).all():
        Result[ctr] = '|0>'
        Result[tar] = '|1>'
    elif (out == m3).all():
        Result[ctr] = '|1>'
        Result[tar] = '|0>'
    elif (out == m4).all():
        Result[ctr] = '|1>'
        Result[tar] = '|1>'


def cc_not_gate(ctr1, ctr2, tar):
    gate_matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 0, 1, 0]]
    in_ctr_1 = Result[ctr1]
    in_ctr_2 = Result[ctr2]
    in_tar = Result[tar]
    m1 = [[1], [0], [0], [0], [0], [0], [0], [0]]
    m2 = [[0], [1], [0], [0], [0], [0], [0], [0]]
    m3 = [[0], [0], [1], [0], [0], [0], [0], [0]]
    m4 = [[0], [0], [0], [1], [0], [0], [0], [0]]
    m5 = [[0], [0], [0], [0], [1], [0], [0], [0]]
    m6 = [[0], [0], [0], [0], [0], [1], [0], [0]]
    m7 = [[0], [0], [0], [0], [0], [0], [0], [1]]
    m8 = [[0], [0], [0], [0], [0], [0], [1], [0]]
    if in_ctr_1 == '|0>' and in_ctr_2 == '|0>' and in_tar == '|0>':
        tensor_pro_0 = np.kron(qbit_0, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr_1 == '|0>' and in_ctr_2 == '|0>' and in_tar == '|1>':
        tensor_pro_0 = np.kron(qbit_0, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr_1 == '|0>' and in_ctr_2 == '|1>' and in_tar == '|0>':
        tensor_pro_0 = np.kron(qbit_0, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr_1 == '|0>' and in_ctr_2 == '|1>' and in_tar == '|1>':
        tensor_pro_0 = np.kron(qbit_0, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr_1 == '|1>' and in_ctr_2 == '|0>' and in_tar == '|0>':
        tensor_pro_0 = np.kron(qbit_1, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr_1 == '|1>' and in_ctr_2 == '|0>' and in_tar == '|1>':
        tensor_pro_0 = np.kron(qbit_1, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr_1 == '|1>' and in_ctr_2 == '|1>' and in_tar == '|0>':
        tensor_pro_0 = np.kron(qbit_1, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr_1 == '|1>' and in_ctr_2 == '|1>' and in_tar == '|1>':
        tensor_pro_0 = np.kron(qbit_1, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)

    out = np.dot(gate_matrix, tensor_pro)

    if (out == m1).all():
        Result[ctr1] = '|0>'
        Result[ctr2] = '|0>'
        Result[tar] = '|0>'
    if (out == m2).all():
        Result[ctr1] = '|0>'
        Result[ctr2] = '|0>'
        Result[tar] = '|1>'
    if (out == m3).all():
        Result[ctr1] = '|0>'
        Result[ctr2] = '|1>'
        Result[tar] = '|0>'
    if (out == m4).all():
        Result[ctr1] = '|0>'
        Result[ctr2] = '|1>'
        Result[tar] = '|1>'
    if (out == m5).all():
        Result[ctr1] = '|1>'
        Result[ctr2] = '|0>'
        Result[tar] = '|0>'
    if (out == m6).all():
        Result[ctr1] = '|1>'
        Result[ctr2] = '|0>'
        Result[tar] = '|1>'
    if (out == m8).all():
        Result[ctr1] = '|1>'
        Result[ctr2] = '|1>'
        Result[tar] = '|0>'
    if (out == m7).all():
        Result[ctr1] = '|1>'
        Result[ctr2] = '|1>'
        Result[tar] = '|1>'


def c_swap(ctr, tar1, tar2):
    gate_matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 0, 1, 0]]
    b1 = [[1], [0], [0], [0], [0], [0], [0], [0]]
    b2 = [[0], [1], [0], [0], [0], [0], [0], [0]]
    b3 = [[0], [0], [0], [0], [0], [0], [0], [0]]
    b4 = [[0], [0], [1], [0], [0], [0], [0], [0]]
    b5 = [[0], [0], [0], [1], [0], [0], [0], [0]]
    b6 = [[0], [0], [0], [0], [1], [0], [0], [0]]
    b7 = [[0], [0], [0], [0], [0], [1], [0], [1]]
    b8 = [[0], [0], [0], [0], [0], [0], [1], [0]]
    in_ctr = Result[ctr]
    in_1 = Result[tar1]
    in_2 = Result[tar2]
    if in_ctr == '|0>' and in_1 == '|0>' and in_2 == '|0>':
        tensor_pro_0 = np.kron(qbit_0, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr == '|0>' and in_1 == '|0>' and in_2 == '|1>':
        tensor_pro_0 = np.kron(qbit_0, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr == '|0>' and in_1 == '|1>' and in_2 == '|0>':
        tensor_pro_0 = np.kron(qbit_0, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr == '|0>' and in_1 == '|1>' and in_2 == '|1>':
        tensor_pro_0 = np.kron(qbit_0, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr == '|1>' and in_1 == '|0>' and in_2 == '|0>':
        tensor_pro_0 = np.kron(qbit_1, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr == '|1>' and in_1 == '|0>' and in_2 == '|1>':
        tensor_pro_0 = np.kron(qbit_1, qbit_0)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)
    if in_ctr == '|1>' and in_1 == '|1>' and in_2 == '|0>':
        tensor_pro_0 = np.kron(qbit_1, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_0)
    if in_ctr == '|1>' and in_1 == '|1>' and in_2 == '|1>':
        tensor_pro_0 = np.kron(qbit_1, qbit_1)
        tensor_pro = np.kron(tensor_pro_0, qbit_1)

    out = np.dot(gate_matrix, tensor_pro)

    if (out == b1).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_1
        Result[tar2] = in_2
    if (out == b2).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_1
        Result[tar2] = in_2
    if (out == b3).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_1
        Result[tar2] = in_2
    if (out == b4).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_1
        Result[tar2] = in_2
    if (out == b5).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_2
        Result[tar2] = in_1
    if (out == b6).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_2
        Result[tar2] = in_1
    if (out == b7).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_2
        Result[tar2] = in_1
    if (out == b8).all():
        Result[ctr] = in_ctr
        Result[tar1] = in_2
        Result[tar2] = in_1

if __name__ == '__main__':
    c_not_gate(1, 0)
    c_not_gate(0, 1)
    c_not_gate(1, 0)
    c_not_gate(1, 2)
    print(Result)

