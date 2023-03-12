import paddle
from paddlefx import symbolic_trace
import operator
from typing import Callable, Dict, List, NamedTuple, Optional, Set,Tuple,Any


def replace_pattern(traced, pattern, replacement):

    pass


class MyNet(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        self._fc1 = paddle.nn.Linear(in_features=10, out_features=10)
        self._fc2 = paddle.nn.Linear(in_features=10, out_features=10)
        self._fc3 = paddle.nn.Linear(in_features=10, out_features=10)

    def forward(self, x):
        x = self._fc1(x)
        x = self._fc2(x)
        x = self._fc3(x)
        y = paddle.add(x=x, y=x)
        y = paddle.add(x=x, y=y)
        y = paddle.add(x=x, y=y)
        return paddle.nn.functional.relu(x=y),x+x,x.add(x)
    
traced_layer = symbolic_trace(MyNet())

traced_layer.graph.print_tabular()

patterns = set([operator.add, paddle.add, "add"])

print(traced_layer.graph.nodes)
for node in traced_layer.graph.nodes:
    if node.op == "call_function":
        if node.target in patterns:
            # new_node = traced_layer.graph.call_function(paddle.bitwise_and, node.args, node.kwargs)
            node.target = paddle.subtract
            node.name = paddle.subtract.__name__
    if node.op == "out":
        if node.target in patterns:
            node.



# for node in traced_layer.graph.nodes:
#     print(node)

# for n in traced_layer.graph.nodes:
#     if any(n.target == pattern for pattern in patterns):
#         with traced_layer.graph.inserting_after(n):
#             new_node = traced_layer.graph.call_function(paddle.subtract, n.args, n.kwargs)
#             # https://github.com/pytorch/pytorch/blob/454c48b9873da7593b05b60596bc28d44e8b977c/torch/fx/node.py
#             n.replace_all_uses_with(new_node)
#         traced_layer.graph.erase_node(n)

        
traced_layer.graph.print_tabular()