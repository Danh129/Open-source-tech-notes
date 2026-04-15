def dem_chan_le(a):
    chan = 0
    le = 0
    for x in a:
        if x % 2 == 0:
            chan += 1
        else:
            le += 1
    return chan, le


a = list(map(int, input("Nhập các số: ").split()))
chan, le = dem_chan_le(a)

print("Số chẵn:", chan)
print("Số lẻ:", le)
