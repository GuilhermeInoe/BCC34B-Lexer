from automata.fa.Moore import Moore
from sys import argv

moore = Moore(#estados:
              ['qs', 'q0', 'q1', 'qf'],
              
              #alfabeto:
              ['a' , 'b' , 'c', 'd', 'e' , 'f' , 'g', 'h', 'i' , 'j' , 'k', 'l', 'm', 'n', 'o' , 'p', 'q', 'r' , 's' , 't', 'u', 'v' , 'w' , 'x', 'y', 'z',
               'A' , 'B' , 'C', 'D', 'E' , 'F' , 'G', 'H', 'I' , 'J' , 'K', 'L', 'M', 'N', 'O' , 'P', 'Q', 'R' , 'S' , 'T', 'U', 'V' , 'W' , 'X', 'Y', 'Z', ' '],
               
              #palavras:
              ['INT'],

              {
                  'qs' : {
                      'i' : 'q0',
                  },
                  'q0': {
                      'n': 'q1',
                  },
                  'q1': {
                      't': 'qf',
                  },
                  'qf': {
                      ' ': 'ID_input',
                  },
                  'ID_input': {
                    'a':'ID_input', 'A':'ID_input',
                    'b':'ID_input', 'B':'ID_input',
                    'c':'ID_input', 'C':'ID_input',
                    'd':'ID_input', 'D':'ID_input',
                    'e':'ID_input', 'E':'ID_input',
                    'f':'ID_input', 'F':'ID_input',
                    'g':'ID_input', 'G':'ID_input',
                    'h':'ID_input', 'H':'ID_input',
                    'i':'ID_input', 'I':'ID_input',
                    'j':'ID_input', 'J':'ID_input',
                    'k':'ID_input', 'K':'ID_input',
                    'l':'ID_input', 'L':'ID_input',
                    'm':'ID_input', 'M':'ID_input',
                    'n':'ID_input', 'N':'ID_input',
                    'o':'ID_input', 'O':'ID_input',
                    'p':'ID_input', 'P':'ID_input',
                    'q':'ID_input', 'Q':'ID_input',
                    'r':'ID_input', 'R':'ID_input',
                    's':'ID_input', 'S':'ID_input',
                    't':'ID_input', 'T':'ID_input',
                    'u':'ID_input', 'U':'ID_input',
                    'v':'ID_input', 'V':'ID_input',
                    'w':'ID_input', 'W':'ID_input',
                    'x':'ID_input', 'X':'ID_input',
                    'y':'ID_input', 'Y':'ID_input',
                    'z':'ID_input', 'Z':'ID_input',
                    '_':'ID_input',
                    
                    '(':'ID_output',
                  },
                  'ID_output':{
                      'v' : 'lparen_output',
                  },
                  'lparen_output': {
                      'o':'void_input0',
                  },
                  'void_input0':{
                      'i': 'void_input1',
                  },
                  'void_input1':{
                      'd': 'void_input2',
                  },
                  'void_input2':{
                      ')': 'void_output',
                  },
                  'void_output':{
                      '{': 'rparen_output',
                  },
                  'rparen_output':{
                      '\n':'lbraces_output',
                  }
              },

              #estado inicial:
              'qs',
              #saídas:
              {
                  'qs' : '',
                  'q0' : '',
                  'q1' : '',
                  'qf' : 'INT\n',
                  'ID_input' : '',
                  'ID_output' : 'ID\n',
                  'lparen_output' : 'LPAREN\n',
                  'rparen_output' : 'RPAREN\n',
                  'lbraces_output': 'LBRACES\n',
                  'void_input0'   : '',
                  'void_input1'   : '',
                  'void_input2'   : '',
                  'void_input3'   : '',
                  'void_output'   : 'VOID\n',
              }

              )

if __name__ == "__main__":
    if len(argv) < 2 :
        raise IOError("Use "+ argv[0] + " file.cm")
    else :
        aux = argv[1].split('.')
        if aux[-1] != 'cm':
            raise IOError("Not a .cm file!")
        data = open(argv[1])

        source_file = data.read()

        print("Definição da Máquina")
        print(moore)

        print("Entrada:")
        print(source_file)

        print("Lista de Tokens:")
        print(moore.get_output_from_string(source_file))

