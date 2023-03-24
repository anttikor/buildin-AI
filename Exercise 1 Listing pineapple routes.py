import itertools
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    fixed_element= portnames[0]
    rest_elements= portnames[1:]

    if len(rest_elements) == 0:
        print("liian lyhyt")
    else:
        p = itertools.permutations(rest_elements)
        for j in list(p):
            print(fixed_element+' '+' ' .join (j))


permutations([0], list(range(1, len(portnames))))


def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
 
permutations([0], list(range(1, len(portnames))))