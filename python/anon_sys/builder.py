# Written in Python for prototyping purposes only, Rust impl preferred.

from typing import TYPE_CHECKING
import os
import json

if TYPE_CHECKING:
    from io import TextIOWrapper
    from typing import List, Optional, Callable, Tuple

from pathlib import Path

FILE_EXT = '.asys'



DEFAULT_CONFIG = {
    
}

def rw_asys(s: os.PathLike):
    with open(s, 'r') as f:
        data = json.load(f)

def walk_asys(s: os.PathLike):
    for branch, buds, fruits in os.walk(s):
        for fruit in fruits:
            fruit: str
            if not fruit.endswith(FILE_EXT):
                continue
            fruit = fruit[:len(FILE_EXT)]
            

if __name__ == '__main__':
    walk_asys('..')



# def process(s: str, reserved_kw_unary: List[str] = [''], reserved_kw_binary: List[str] = ['']):
#     reserved_kw_unary = reserved_kw_unary.copy()
#     reserved_kw_binary = reserved_kw_binary.copy()
#     # Reasonability measure
#     s = s.strip()
#     # Adding the not changed the meaning interestingly.
#     if any(map(lambda x: not s.startswith(x), reserved_kw_unary)):
#         pass
    

# def buffered_replace(f: TextIOWrapper, start_sep: str = '{[{', end_sep: str = '}]}' , buffer_size = 2048, escape_chars: str = '[]', e_char: str = '\\', processor = process,  **kwargs):
#     """
#     Buffered implementation of a file replace.
    
#     PARAMETERS
#     ----------
#     f -
#         An open file descriptor.
#     replace_sep -
#         The start and end of a value that must be replaced with a value from kwargs.
#     """
#     l_sep = functools.reduce(lambda h, acc: acc.replace(h, e_char), escape_chars, start_sep)
#     r_sep = functools.reduce(lambda h, acc: acc.replace(h, e_char), escape_chars, end_sep)
#     print(l_sep, r_sep)
#     pattern = re.compile(f'{l_sep}(\w+){r_sep}')
#     data = f.read(buffer_size)
#     while data:
#         for match in pattern.finditer(data):
#             start_idx, end_idx = match.span()
#             snippet = data[start_idx+len(start_sep):end_idx-len(end_sep)]
#             result = process(snippet)
#         data = f.read(buffer_size)

# def build(name: str, cwd: str = os.getcwd()):
#     for dir_ in os.listdir(cwd):
#         print(f'building {dir_}')
#         if os.path.isdir(dir_):
#             build(dir_)
#         elif os.path.isfile(dir_):
#             with open(dir_, 'r+') as f:
#                 buffered_replace(f)


