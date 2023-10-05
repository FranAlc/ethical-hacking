import base64
print("Se codificara su password.")

pwd = b'EstaSeraMiClave123+-' #digitar clave
#pwd_byte = pwd.encode('utf-8') // o encambio se utiliza b'' que es lo mismo pero simplificado

encode_pwd = base64.b64encode(pwd)

print(encode_pwd)

"""
print("Se codificara su password.")

pwd = input(b'Digite la clave -> ')

encode_pwd = base64.b64encode(pwd.encode('utf-8'))

print(encode_pwd)

"""