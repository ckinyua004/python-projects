from graphviz import Digraph

# Create a state diagram for the ATM case
dot = Digraph('ATM_StateDiagram', format='png')
dot.attr(rankdir='LR', size='8,5')

# Define nodes
dot.node('Start', shape='circle', label='', style='filled', fillcolor='black')
dot.node('Startup', 'Startup Test')
dot.node('OutOfService', 'Out of Service')
dot.node('Idle', 'Idle')
dot.node('Serving', 'Serving Customer', shape='rectangle')
dot.node('Auth', 'Customer Authentication', shape='box')
dot.node('Select', 'Selecting Transaction', shape='box')
dot.node('Txn', 'Transaction', shape='box')
dot.node('End', shape='doublecircle', label='')

# Transitions
dot.edge('Start', 'Startup')
dot.edge('Startup', 'OutOfService', label='Test Fail')
dot.edge('Startup', 'Idle', label='Test Pass')
dot.edge('Idle', 'Serving', label='insertCard / readCard')
dot.edge('Serving', 'Idle', label='cancel OR after ejectCard')

# Composite state internal transitions
dot.edge('Serving', 'Auth', style='dashed')
dot.edge('Auth', 'Select')
dot.edge('Select', 'Txn')
dot.edge('Txn', 'Serving', label='[exit] ejectCard')

# Render and save the diagram
dot.render('atm_state_diagram', cleanup=False)
