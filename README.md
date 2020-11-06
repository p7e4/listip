# listip
Expand ip range/cidr, for scanners

## Usage
`pip3 install listip`

``` python
from listip import listip

if __name__ == '__main__':
    for i in listip("192.168.1.1, 192.168.0.1/30, 192.168.2.1-192.168.2.10"):
        print(i)

```

**Output:**

```
192.168.1.1
192.168.0.1
192.168.0.2
192.168.2.1
192.168.2.2
192.168.2.3
192.168.2.4
192.168.2.5
192.168.2.6
192.168.2.7
192.168.2.8
192.168.2.9
192.168.2.10

```


