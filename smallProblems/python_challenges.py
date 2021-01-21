#Challenge 1
def challenge1():
    return 2**38

#Challenge 2
def challenge2(charachters):
    str1="abcdefghijklmnopqrstuvwxyz"
    str2="cdefghijklmnopqrstuvwxyzab"
    trans_table = str.maketrans(str1,str2)
    return charachters.translate(trans_table)
challenge2_input="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(challenge2(challenge2_input))
print(challenge2("map"))

#Challenge 3
