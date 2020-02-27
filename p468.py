class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP is None:
            return "Neither"
        if len(IP) < 3:
            return "Neither"

        v4 = IP.split(".")

        if len(v4) > 1:
            # check IPv4
            return self.checkV4(v4)
        else:
            # check IPv6
            v6 = IP.split(":")
            return self.checkV6(v6)

    def checkV4(self, ranges):
        if len(ranges) != 4:
            return "Neither"
        for r in ranges:
            if len(r) == 0:
                return "Neither"
            if r[0] == "0" and len(r) > 1:
                return "Neither"
            if not r[0].isdigit():
                return "Neither"
            try:
                val = int(r)
            except ValueError:
                return "Neither"
            if val > 255:
                return "Neither"
        return "IPv4"

    def checkV6(self, ranges):
        if len(ranges) != 8:
            return "Neither"
        if len(ranges[0]) == 0:
            return "Neither"
        if ranges[0][0] == '0' and len(ranges[0]) > 1:
            return "Neither"
        for r in ranges:
            if len(r) > 4:
                return "Neither"
            if len(r) == 0:
                return "Neither"
            if r[0] == '-':
                return "Neither"
            try:
                v = int(r, 16)
                if v < 0:
                    return "Neither"
            except ValueError:
                return "Neither"
        return "IPv6"


if __name__ == '__main__':
    s = Solution()

    ip = "2001:0db8:85a3:00000:0:8A2E:0370:7334"

    print(s.validIPAddress(ip))
