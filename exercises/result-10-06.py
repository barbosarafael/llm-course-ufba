# Instruções: baixar como zip, e depois deszipar, o repositório: https://github.com/qiyuangong/leetcode

# 0) Libs

import os
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
import random

# 1) Definindo o caminho para o repositório

path_to_files = 'leetcode-master/'

# 2) Criação de funções:

# a) Lê todos os arquivos da pasta, inclusive sub-diretórios

def list_files_walk(start_path = '.'):
    
    l = []
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            
            files = os.path.join(root, file)
            l.append(files)
            
    return l

# b) Identifica a extensão do arquivo 

def identify_language(file: str):
    
    try:
    
        regex = r'\.[^.]+$'

        string = re.search(regex, file).group()
        
    except:
        
        string = ''
    
    return string

# c) Lê o conteúdo do arquivo:

def read_files(file: str):
    
    with open(file, 'r', encoding = 'utf-8') as src:
        content = src.read()
    
    return content

# d) Exclui as linhas com comentários 

def remove_comments(file: str, extension_file: str):
    
    lines = file.strip().split('\n')
    
    if extension_file == '.py':    
        
        uncommented_lines = [line for line in lines if not line.strip().startswith('#')]
    
    elif extension_file in ('.java', '.cpp'):    
        
        uncommented_lines = [line for line in lines if not line.strip().startswith('//')]
    
    else: 
        
        print('Não reconhecido')
        
    rows = '\n'.join(uncommented_lines)
    
    return rows

# e) Aplica o spliter/chunk por linguagens:

def text_splitter_by_language(
    doc: str,
    extension_file: str,
    chunk_size: int = 200,
    chunk_overlap: int = 20
    ):
    
    if extension_file == '.py':
        
        lang = Language.PYTHON
        
    elif extension_file == '.java':
        
        lang = Language.JAVA
        
    elif extension_file == '.cpp':
        
        lang = Language.CPP
        
    else: 
        
        lang = None    
        
    text_splitter = RecursiveCharacterTextSplitter.from_language(
            language = lang,
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = len
            )
    
    split_doc = text_splitter.split_text(doc)
    
    return split_doc

# 3) Aplicação da função:

# a) Lendo todos os arquvios e separando seus caminhos relativos

all_files = list_files_walk(start_path = path_to_files)

# b) Mantendo na lista somente os que nos interessam: .py, .cpp, .java

official_files = [x for x in all_files if identify_language(x) in ('.py', '.cpp', '.java')]
official_files = random.sample(official_files, 10) # Separando 10 arquivos aleatórios

# c) Loop para todos os arquivos:

for file in official_files:
    
    print(f'\n>>>>>>>>>> Nome do arquivo: {file}')
    
    # Lendo o conteúdo
    
    content = read_files(file = file)
    
    # Pegando a extensão
    
    extension = identify_language(file = file)
    
    # Excluindo linhas com comentários
    
    content_preprocess = remove_comments(file = content, extension_file = extension)
    
    # Aplicando o chunk
    
    chunk = text_splitter_by_language(doc = content_preprocess, extension_file = extension)
    
    count = 0
    for doc in chunk: 
        count += 1
        print(f'\n {count}º chunk: > ', doc)
        
        
# Resultado:

# (venv) rafael@pop-os:~/Documentos/github/llm-course-ufba-main$ python result-10-06.py 

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/221_Maximal_Square.py

#  1º chunk: >  class Solution(object):

#  2º chunk: >  def maximalSquare(self, matrix):
#         if matrix is None or len(matrix) == 0:
#             return 0
#         rows, cols, res, prev = len(matrix), len(matrix[0]), 0, 0

#  3º chunk: >  dp = [0] * (cols + 1)
#         for i in range(1, rows + 1):
#             for j in range(1, cols + 1):
#                 temp = dp[j]
#                 if matrix[i - 1][j - 1] == '1':

#  4º chunk: >  dp[j] = min(dp[j - 1], dp[j], prev) + 1
#                     res = max(res, dp[j])
#                 else:
#                     dp[j] = 0
#                 prev = temp

#  5º chunk: >  return res * res

# >>>>>>>>>> Nome do arquivo: leetcode-master/cpp/201_bitwise_and_of_numbers_range.cpp

#  1º chunk: >  /** time complexity : O(logN). N = min(m, n) **/

#  2º chunk: >  class Solution {
# public:
#     int rangeBitwiseAnd(int m, int n) {
#         int cnt = 0;
#         while(m < n) {
#             m = m >> 1;
#             n = n >> 1;
#             cnt++;
#         }

#  3º chunk: >  }
#         return n<<cnt;
#     }
# };

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/367_Valid_Perfect_Square.py

#  1º chunk: >  class Solution(object):

#  2º chunk: >  def isPerfectSquare(self, num):
#         low, high = 1, num
#         while low <= high:
#             mid = (low + high) / 2
#             mid_square = mid * mid
#             if mid_square == num:

#  3º chunk: >  return True
#             elif mid_square < num:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return False

# >>>>>>>>>> Nome do arquivo: leetcode-master/java/003_Longest_Substring_Without_Repeating_Characters.java

#  1º chunk: >  public class Solution {

#  2º chunk: >  public int lengthOfLongestSubstring(String s) {
#         int[] charMap = new int[256];
#         Arrays.fill(charMap, -1);
#         int i = 0, maxLen = 0;
#         for (int j = 0; j < s.length(); j++) {

#  3º chunk: >  if (charMap[s.charAt(j)] >= i) {
#                         i = charMap[s.charAt(j)] + 1;
#                 }
#                 charMap[s.charAt(j)] = j;
#                 maxLen = Math.max(j - i + 1, maxLen);
#         }
#         return maxLen;
#     }
# }

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/226_Invert_Binary_Tree.py

#  1º chunk: >  class Solution(object):

#  2º chunk: >  def invertTree(self, root):
#         if root is None:
#             return None
#         queue = [root]
#         while len(queue):
#             curr = queue.pop(0)

#  3º chunk: >  curr.left, curr.right = curr.right, curr.left
#             if curr.left is not None:
#                 queue.append(curr.left)
#             if curr.right is not None:

#  4º chunk: >  queue.append(curr.right)
#         return root

# >>>>>>>>>> Nome do arquivo: leetcode-master/java/867_Transpose_Matrix.java

#  1º chunk: >  class Solution {
#     public int[][] transpose(int[][] A) {
#         int R = A.length, C = A[0].length;
#         int[][] ans = new int[C][R];
#         for (int r = 0; r < R; ++r)

#  2º chunk: >  for (int c = 0; c < C; ++c) {
#                 ans[c][r] = A[r][c];
#             }
#         return ans;
#     }
# }

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/134_Gas_Station.py

#  1º chunk: >  class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         """
#         :type gas: List[int]
#         :type cost: List[int]
#         :rtype: int
#         """
#         ls = len(gas)

#  2º chunk: >  begin, end = 0, ls - 1
#         curr = gas[end] - cost[end]
#         while begin < end:
#             if curr >= 0:
#                 curr += gas[begin] - cost[begin]
#                 begin += 1

#  3º chunk: >  else:
#                 end -= 1
#                 curr += gas[end] - cost[end]
#         if curr >= 0:
#             return end
#         else:
#             return -1

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/223_Rectangle Area.py

#  1º chunk: >  class Solution(object):
#     def computeArea(self, A, B, C, D, E, F, G, H):
#         """
#         :type A: int
#         :type B: int
#         :type C: int
#         :type D: int
#         :type E: int

#  2º chunk: >  :type F: int
#         :type G: int
#         :type H: int
#         :rtype: int
#         """
#         result = (C - A) * (D - B) + (G - E) * (H - F)

#  3º chunk: >  if (C <= E or G <= A or H <= B or D <= F):
#             return result
#         dx = min(C, G) - max(A, E)
#         dy = min(D, H) - max(B, F)
#         return result - dx * dy

# >>>>>>>>>> Nome do arquivo: leetcode-master/java/728_Self_Dividing_Numbers.java

#  1º chunk: >  class Solution {
#     public List<Integer> selfDividingNumbers(int left, int right) {
#         LinkedList list = new LinkedList();
#         for(int i = left; i <= right; i++) {

#  2º chunk: >  if(isSelfDiving(i))
#             list.add(i);
#         }
#         return list;
#     }
    
#     public boolean isSelfDiving(int num) {
#             int digit = num % 10;

#  3º chunk: >  int temp = num;
#             boolean isTrue = true;
#             while(temp != 0) {
#                 if(digit == 0 || num % digit != 0) {
#                     isTrue = false;

#  4º chunk: >  break;
#                 } else {
#                     temp /= 10;
#                     digit = temp % 10;
#                 }
#             }
#             return isTrue;
#     }
# }

# >>>>>>>>>> Nome do arquivo: leetcode-master/python/415_Add_Strings.py

#  1º chunk: >  class Solution(object):

#  2º chunk: >  def addStrings(self, num1, num2):
#         res = []
#         pos1 = len(num1) - 1
#         pos2 = len(num2) - 1
#         carry = 0
#         while pos1 >= 0 or pos2 >= 0 or carry == 1:

#  3º chunk: >  digit1 = digit2 = 0
#             if pos1 >= 0:
#                 digit1 = ord(num1[pos1]) - ord('0')
#             if pos2 >= 0:
#                 digit2 = ord(num2[pos2]) - ord('0')

#  4º chunk: >  res.append(str((digit1 + digit2 + carry) % 10))
#             carry = (digit1 + digit2 + carry) / 10
#             pos1 -= 1
#             pos2 -= 1
#         return ''.join(res[::-1])        