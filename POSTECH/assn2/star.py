import sys


stage = int(sys.stdin.readline())
request = [0] * stage

for iteration in range(stage):
    request[iteration] = int(sys.stdin.readline())
    
output =""

for input_n in request:
    
    star_cage =  ("*****", " * *", "  *")

    if input_n == 3 :
        for line in star_cage:
            output += line+'\n'
    
    else:

        while input_n/2 != len(star_cage):
            new_cage = ()
            
            for line in star_cage:
                new_cage += (" "*len(star_cage)+line,)
            
            for line in star_cage:
                new_cage += (line + (" "*(2*len(star_cage) - len(line))) +line, )

            star_cage = new_cage


        for line in star_cage:

            output += " "*len(star_cage)+line+'\n'

        for line in star_cage:
            output += line + (" "*(2*len(star_cage) - len(line))) +line + "\n"


print(output)
