class Codec:

    next_id = 0
    table = {}
    root_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.table[self.next_id] = longUrl

        digits = self.digitConvert(self.next_id)

        enc = [chr(item) for item in digits]

        self.next_id += 1

        return self.root_url + ''.join(enc)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        enc = shortUrl.replace(self.root_url, "")

        ind = 0
        l = len(enc)
        for i in range(0, l):
            ind += ord(enc[i]) * 126**(l-i-1)
        return self.table[ind]

    def digitConvert(self, val):

        digits = []

        while val >= 126:
            orig_val = val
            digit = val//126
            digits.append(digit)
            val = orig_val - digit * 126
        digits.append(val)
        return digits



# Your Codec object will be instantiated and called as such:

codec = Codec()

url = "qwoejfpoqiew"
l = codec.encode(url)
print(l)
print(codec.decode(l))

url = "qwoejfpoasdfqiew"
l = codec.encode(url)
print(l)
print(codec.decode(l))

url = "qwoejfpwefoqiew"
l = codec.encode(url)
print(l)
print(codec.decode(l))

url = "qwoejwqrfpoqiew"
l = codec.encode(url)
print(l)
print(codec.decode(l))