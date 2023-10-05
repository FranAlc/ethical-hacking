#encode
import base64

shDecodificado = b'Texto que sera codificado'

encode = base64.b64encode(shDecodificado)

print(encode)
# >> VGV4dG8gcXVlIHNlcmEgY29kaWZpY2Fkbw==


#decode

shCodificado = b'VGV4dG8gcXVlIHNlcmEgZGVjb2RpZmljYWRv' 

decode = base64.b64decode(shCodificado)

print(decode)
# >> VGV4dG8gcXVlIHNlcmEgZGVjb2RpZmljYWRv