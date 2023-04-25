bin_num = '1001111'
lng = len(bin_num)
t = [6,5,4,3,2,1,0]
out = 0
for l, n in enumerate(bin_num):
    out += int(n)*2**t[l]
print(f"TABUb{bin_num} = d{out} ")
out = 0
for i in range(0, lng):
    out += int(bin_num[-i-1])*(2**i)

print(f"b{bin_num} = d{out}")
print(0b1001111)

hex_num = 0x1DB
oct_num = 0o2063

print(f"0x{hex_num},o{oct_num} ")