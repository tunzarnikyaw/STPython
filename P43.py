s = 'python PROgramming'
#    012345678901234567
t = '123၁၂၃'

print( len(s) )                         # 18
print( s.upper() )                      # PYTHON PROGRAMMING
print( s.lower() )                      # python programming
print( s.capitalize() )                 # Python programming
print( s.title() )                      # Python Programming

print( s.count('m') )                   # 2
print( s.count('m', 0, len(s)//2) )     # 0
print( s.count('m', len(s)//2, len(s)) )    # 2
print( s.count('m', len(s)//2 ) )           # 2

print( s.find('m') )                    # 13
print( s.find('m', 0, len(s)//2) )      # -1
print( s.find('j') )                    # -1
print( s.find('p') )                    # 0
print( s.find('n') )                    # 5
print( s.find('n', 6) )                 # 16

print( s.isalnum() )                    # False
print( s.isalpha() )                    # False (because the string has Space char)
print( s.isdigit() )                    # False
print( t.isdigit() )                    # True
print( s.isupper() )                    # False
print( s.islower() )                    # False
print( s.istitle() )                    # False
print( s.isspace() )                    # False
print( s.isnumeric() )                  # False
print( t.isnumeric() )                  # True
print( s.replace('n', '?') )            # pytho? PROgrammi?g
print( s.replace('n', '?', 1) )         # pytho? PROgramming
print( s.startswith('j')  )             # False
print( s.startswith('p')  )             # True
print( s.endswith('p')  )               # False
print( s.endswith('ing')  )             # True
