import numpy as np

class LogicGates:

    def __init__(self):
        self.w1 = None
        self.w2 = None
        self.th = None
        self.out = None
        self.x1 = self.x2 = None


    def print_output(self, gate):
        if gate == 'AND':
            print(f'{self.x1} AND {self.x2} is {self.out}')
        elif gate == 'OR':    
            print(f'{self.x1} OR {self.x2} is {self.out}')
        elif gate == 'NAND':
            print(f'{self.x1} NAND {self.x2} is {self.out}')     
        elif gate == 'NOR':
            print(f'{self.x1} NOR {self.x2} is {self.out}')       






    def do_and(self,x1,x2):
        self.w1 = 0.5
        self.w2= 0.5
        self.th= 1 

        self.x1 = x1
        self.x2 = x2



        x = np.array([x1,x2])
        w = np.array([self.w1,self.w2])

        if np.sum(x*w) >= self.th:
         
         self.out =1
         return 1
        else:
         self.out = 0
         return 0    

    def do_or(self,x1,x2):

        self.w1 = 0.5
        self.w2 = 0.5
        self.th =0


        x= np.array([x1,x2])
        w= np.array([self.w1,self.w2])

        if np.sum(x*w) >=self.th:
            self.out =1
            return 1
        else:
            self.out = 0
            return 0
        
    def do_nor(self,x1,x2):
        self.w1= 1
        self.w2=1
        self.th=-1

        x= np.array([x1,x2])
        w= np.array([self.w1,self.w2])

        
        if np.sum(x*w) + self.th<=0:
            self.out =1
            return 1
        else:
            self.out =0
            return 0

        
    def do_nand(self,x1, x2):
        self.w1 = -1 
        self.w2 = -1
        self.th = 2
        
        x= np.array([x1,x2])
        w= np.array([self.w1,self.w2])
        
        if np.sum(x*w) + self.th < 0:
            self.out =0
            return 0
        else:
            self.out =1
            return 1    

if __name__ == '__main__':
    logic_gate = LogicGates()

    logic_gate.do_and(1, 0)
    logic_gate.print_output('AND')

    logic_gate.do_or(1, 0)
    logic_gate.print_output('OR')

    logic_gate.do_nand(1,0)
    logic_gate.print_output('NAND')
     
    logic_gate.do_nor(1,0)
    logic_gate.print_output('NOR')