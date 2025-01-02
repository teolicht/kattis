secs = int(input())

mins = (secs // 60) % 60
hours = (secs // 60) // 60
secs = secs % 60

print("%d : %d : %d" % (hours, mins, secs))
