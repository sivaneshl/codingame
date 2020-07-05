import string
operation = input()
pseudo_random_number = int(input())
rotors = [input()for i in range(3)]
message = input()
alphabets = string.ascii_uppercase

if operation=='ENCODE':
    ceaser_shift = [(alphabets.index(message[i])+pseudo_random_number+i)%26 for i in range(len(message))]
    for i, rotor in enumerate(rotors):
        rotor_shift = list(rotor[j] for j in ceaser_shift)
        ceaser_shift = list(alphabets.index(x) for x in rotor_shift)
    print(''.join(rotor_shift))
else:
    rotor_shift = message
    for rotor in reversed(rotors):
        ceaser_shift = list(rotor.index(x) for x in rotor_shift)
        rotor_shift = list(alphabets[j] for j in ceaser_shift)
    print(''.join([alphabets[(alphabets.index(rotor_shift[i])-pseudo_random_number-i)%26] for i in range(len(rotor_shift))]))
