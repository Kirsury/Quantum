import Quantum_Verification.benchmark_verify as verify


c1 = verify.process('./benchmark/peres_9.real')
c2 = verify.process('./benchmark/4gt13_92.real')
verify.matrix_equal(c1, c2)
