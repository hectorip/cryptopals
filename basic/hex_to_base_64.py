# Converting from Hexadecimal string to Base64

import base64

input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


input_hex = bytes.fromhex(input)
o = base64.encodebytes(input_hex)
print(o)