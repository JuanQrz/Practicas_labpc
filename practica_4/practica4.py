#!/usr/bin/env python3

#-----Al descargar la imagen del logo me cambio el nombre--------

import base64
from typing import Callable

def encode_decode_bytes(byte_message: bytes, encode_fn: Callable[[bytes], bytes]) -> bytes:
    return encode_fn(byte_message)

def encode_file(path:str) -> bytes:
    with open(path, 'rb') as file_to_encode:
        return encode_decode_bytes(file_to_encode.read(), base64.b64encode)

def decode_file(path:str) -> bytes:
    file_to_encode = open(path, 'rb')
    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


def save_file(path: str,content: bytes) -> None:
    with open(path, 'wb') as file_to_save:
        file_to_save.write(content)



if __name__ == '__main__':
    import sys

    cmds = {'encode': base64.b64encode, 'decode': base64.b64decode}
    if len(sys.argv) > 1:
        main_cmd = sys.argv[1]
        encode_format = sys.argv[2] if len(sys.argv) > 2 else 'ascii'
        code_function = cmds.get(main_cmd, cmds.get('encode'))
        print(encode_decode_bytes(sys.stdin.read(), code_function))


#-------codificar msj.txt
save_file('TOP_Secret.txt', encode_file('msg.txt'))

#-------codificar imagen

save_file('Imagen_Codificada.txt', encode_file('MicrosoftTeams-image.png'))

#-------decodificar imagenes

save_file('Imagen1.jpg', decode_file('mystery_img.txt'))
save_file('Imagen2.jpg', decode_file('mystery_img2.txt'))
