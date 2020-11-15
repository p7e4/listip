#!/usr/bin/env python3

from ipaddress import ip_network, ip_address

def expand(raw):
    ips = []
    for r in raw.replace(" ", "").split(","):
        if "/" in r:
            for i in ip_network(r, strict=False).hosts():
                ips.append(str(i))
        elif "-" in r:
            start, end = [ip_address(i) for i in r.split("-")]
            if start >= end:
                start, end = end, start
            while start <= end:
                if start.version == 6 or not int(start) % 256 in [0, 255]:
                    ips.append(str(start))
                start += 1
        else:
            ips.append(str(ip_address(r)))
    return ips

def listip(raw, exclude=""):
    ips = expand(raw)
    if exclude:
        ips = list(set(ips) - set(expand(exclude)))

    ips.sort()
    return ips


if __name__ == '__main__':
    for i in listip("192.168.1.1, 192.168.0.1/30, 192.168.2.1-192.168.2.10", exclude="192.168.1.1, 192.168.2.1/24"):
        print(i)




