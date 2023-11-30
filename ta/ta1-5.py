# A=10 B=11 C=12 D=13 E=14 F=15 G=16 H=17 I=34 J=18 K=19 L=20
# M=21 N=22 O=35 P=23 Q=24 R=25 S=26 T=27 U=28 V=29 W=32 X=30
# Y=31 Z=33

data_dict = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}


identity = input()

checksum = 0

eng_num = str(data_dict[identity[0]])

# A1234567
# eng_num = 10
# 1 + 0 * 9
checksum += int(eng_num[0]) + int(eng_num[1]) * 9

# 1 ~ 8
for i in range(1, 9):
    checksum += int(identity[i]) * (9 - i)
checksum += int(identity[9])

if checksum % 10 == 0:
    print("合法")
else:
    print("不合法")
