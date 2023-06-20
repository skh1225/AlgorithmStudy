import math

def solution(numbers):
    answer = []
    for number in numbers:
        binary = get_binary(number)
        if decision(binary):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def get_binary(number):
    binary = ''
    while number > 0:
        if number % 2 == 0:
            binary='0'+binary
        else:
            binary='1'+binary
        number=number//2
    length = len(binary)
    binary = '0'*int(math.pow(2,math.ceil(math.log(length+1,2)))-length-1)+binary
    return binary

def decision(binary):
    if len(binary) > 1:     
        mid = len(binary)//2
        if binary[mid] == '1' and decision(binary[mid+1:]) and decision(binary[:mid]):
            return True     
        else:
            for bin in binary:
                if bin != '0':
                    return False
            return True
    return True
    