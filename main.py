from dis import Instruction
from json import load

class register:
    def __init__(self, width=8):
        self.width = width
        self.data = 0    
    def read(self):
        return(self.data)
    def write(self, data):
        if (data < 0) or (data >= 2 ** self.width):
            raise ValueError()
        else:
            self.data = data

class RAM:
    def __init__(self, cell_count=16, width=8):
        self.data = [register(width=width) for i in range(cell_count)]
    def read(self, index):
        return(self.data[index].read())
    def write(self, index, data):
        self.data[index].write(data)

class ROM:
    def __init__(self, path='program.json'):
        f = open(path)
        self.data = load(f)['data']
    def read(self, index):
        return(int(self.data[index], 2))

class CPU:
    def __init__(self):
        # Flags
        self.overflow_flag = register(width=1)
        # Registers
        self.reg_0 = register()
        self.reg_1 = register()
        self.reg_2 = register()
        self.reg_3 = register()
        self.ALU_reg_A = register()
        self.ALU_reg_B = register()
        self.ALU_reg_out = register()
        # Special Registers
        self.counter = register()
        # RAM
        self.RAM_A = RAM(cell_count=8)
        # ROM
        self.ROM_A = ROM()
    def cycle(self):
        raw_data = self.ROM_A.read(self.counter.read())
        binary = format(raw_data, 'b').zfill(8)
        ins = binary[0:4]
        data = int(binary[4:8], 2)

        print('---Cycle---')
        print('Counter: {}'.format(self.counter.read()))
        print('Binary Instruction: {}'.format(binary))

        # read reg write reg
        # read reg write RAM

        # read RAM write reg
        # read RAM write RAM

        # Read ROM write reg
        # Read ROM write RAM

        if ins == '0000':
            # do nothing
            print('Interpreted Instruction: Do nothing')
            pass
        elif ins == '0001':
            # Write y to register x
            if data == 0:
                print('Interpreted Intruction: Write {} to register #0'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_0.write(self.ROM_A.read(self.counter.read() + 1))
            elif data == 1:
                print('Interpreted Intruction: Write {} to register #1'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_1.write(self.ROM_A.read(self.counter.read() + 1))
            elif data == 2:
                print('Interpreted Intruction: Write {} to register #2'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_2.write(self.ROM_A.read(self.counter.read() + 1))
            elif data == 3:
                print('Interpreted Intruction: Write {} to register #3'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_3.write(self.ROM_A.read(self.counter.read() + 1))
            elif data == 4:
                print('Interpreted Intruction: Write {} to ALU register A'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_3.write(self.ROM_A.read(self.counter.read() + 1))
            elif data == 5:
                print('Interpreted Intruction: Write {} to ALU register B'.format(self.ROM_A.read(self.counter.read() + 1)))
                self.reg_3.write(self.ROM_A.read(self.counter.read() + 1))
        elif ins == '0010':
            # Jump to line x
            pass
        elif ins == '0011':
            # jump to line a if con_reg == y
            pass
        elif ins == '0100':
            # ALU add
            pass
        elif ins == '0101':
            # ALU sub
            pass
        elif ins == '0110':
            # ALU Multiply
            pass
        elif ins == '0111':
            # ALU divide
            pass
        elif ins == '1000':
            pass
        elif ins == '1001':
            pass
        elif ins == '1010':
            pass
        elif ins == '1011':
            pass
        elif ins == '1100':
            pass
        elif ins == '1101':
            pass
        elif ins == '1110':
            pass
        elif ins == '1111':
            pass

        self.counter.write(self.counter.read() + 1)

a = CPU()
a.cycle()
a.cycle()