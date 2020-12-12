beacons = ["ibeacon", "ibeacon2", "ibeacon3"]
ds = ["25c", "50c", "75c", "1m", "125c", "150c"]

sums = {}
avgs = {}

for beacon in beacons:
    for d in ds:
        file_name = beacon + "_" + d + ".txt"
        with open(file_name) as fp:
            i=0
            for line in fp.readlines():
                line = line.strip()
                if(line=="Starting scan"):
                    sums[file_name] = 0
                else:
                    sums[file_name] += int(line)
                    i+=1
            avgs[file_name] = sums[file_name]/i

for a in avgs:
    print(a, ":", avgs[a])
