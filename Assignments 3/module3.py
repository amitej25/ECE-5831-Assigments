import logic_gate as lg
logic_gate = lg.LogicGates()

logic_gate.do_and(0,1)
logic_gate.print_output('AND')

logic_gate.do_or(0,1)
logic_gate.print_output('OR')

logic_gate.do_nor(0,1)
logic_gate.print_output('NOR')

logic_gate.do_nand(0,1)
logic_gate.print_output('NAND')