import sys
key="T0pS3cre7key"
enc_text="Bot kmws mikferuigmzf rmfrxrwqe abs perudsf! Nvm kda ut ab8bv_w4ue0_ab8v_DDU"
alphaL = "abcdefghijklnmopqrstuvqxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
num    = "0123456789"
keychars = num+alphaL+alphaU
key="T0pS3cre7key"
dec_char=""
dec_text=""
for i in range(len(enc_text)):
    rotate_amount = keychars.index(key[i % len(key)])
    if enc_text[i] in alphaL:
        dec_char=(ord(enc_text[i])-ord('a')-rotate_amount)%26+ord('a')
    elif enc_text[i] in alphaU:
        dec_char = (ord(enc_text[i])-ord('A')-rotate_amount)%26+ord('A')
    elif enc_text[i] in num:
        dec_char =(ord(enc_text[i])-ord('0')-rotate_amount)%10+ord('0')
    else:
        dec_char = ord(enc_text[i])
    dec_text=dec_text+chr(dec_char)
print(dec_text)
