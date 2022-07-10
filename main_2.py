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
        self.register_bank = RAM(cell_count=16)
        # Special Registers
        self.counter = register()
        # RAM
        self.RAM = RAM(cell_count=8)
        # ROM
        self.ROM = ROM()
    def cycle(self):
        byte = format(self.ROM.read(self.counter.read()), 'b').zfill(8)
        ins = int(byte, 2)

        print('---Cycle---')
        print('Counter: {}'.format(self.counter.read()))
        print('Intruction Byte: {}'.format(byte))

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
            # read reg write reg
            self.register_bank.write(data_D, self.register_bank.read(data_B))
        elif ins == '0010':
            # read reg write RAM
            self.RAM.write(data_D, self.register_bank.read(data_B))
        elif ins == '0011':
            # read RAM write reg
            self.register_bank.write(data_A, self.RAM.read(data_byte_full))
        elif ins == '0100':
            # read RAM write RAM
            self.RAM.write()
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

        self.counter.write(self.counter.read() + 2)

a = CPU()
a.cycle()
a.cycle()