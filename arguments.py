# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1: Greet Template

import string


def greet(name, greeting_template='Hello, <name>!'):
    greet = greeting_template.replace("<name>",name)
    return(greet)

print(greet('Bob'))


#Part 2: Force

def force(mass: float, body='earth'):
    gravity_factors = dict([
        ('earth', 9.8),
        ('sun', 274),
        ('jupiter', 24.9),
        ('neptune', 11.5),
        ('saturn', 11.4),
        ('uranus', 8.9),
        ('venus', 8.9),
        ('mars', 3.7),
        ('mercury', 3.7),
        ('moon', 1.6),
        ('pluto', 0.6)
    ])
    if type(mass) == float:
        return(mass * gravity_factors[body])
    
print(force(0.1))
print(force(1.0, body='saturn'))


#Part 3: Gravity

#for this one wincpy returns "We expected student_module.pull(1, 2, 3) is not None" but it's either None or arguments are not float
# def pull(m1: float, m2: float, d: float):
#     G = 6.674 * 10**11
#     if type(m1) == float and type(m2) == float and type(d) == float:
#         return(G * ((m1 * m2) / d**2))

def pull(m1: float, m2: float, d: float):
    G = 6.674 * 10**-11
    return(G * ((m1 * m2) / d**2))
    
print(round(pull(800.0,1500.0,3.0),10))

