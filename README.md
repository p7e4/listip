# listip
Expand ip range/cidr, for scanners

## Usage
`pip3 install listip`

``` python
from listip import listip

if __name__ == '__main__':
    for i in listip("192.168.1.1, 192.168.0.1/30, 192.168.2.1-192.168.2.10", exclude="192.168.1.1, 192.168.2.1/24"):
        print(i)

```

**Output:**

```
192.168.0.1
192.168.0.2

```


