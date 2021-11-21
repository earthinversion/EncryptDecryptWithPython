import argparse

info_string = '''
Python utility program to encrypt/decrypt multiple files (by Utpal Kumar, UC Berkeley, 2021/11)
'''

PARSER = argparse.ArgumentParser(description=info_string, epilog="enter filename(s) and key to encrypt and decrypt")



def Encrypt(filename, key, pref):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for kk in key:
        kk = ord(kk)
        for index, value in enumerate (data):
            data[index] = value ^ kk

    file = open (pref + "-" + filename, "wb")
    file.write(data)
    file.close()

def Decrypt(filename, key, pref):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for kk in key:
        kk = ord(kk)
        for index, value in enumerate (data):
            data[index] = value ^ kk
    
    defilename = filename.split("-")[-1] #remove the encryption prefix
    file = open (pref + "-" +defilename, "wb")
    file.write(data)
    file.close()


# key = "qsis123" #between 1-255

# filenames = ['myscript.py', 'helloworld.py']
def enc_files(filenames, key, pref):
    for ff in filenames:
        Encrypt(ff, key, pref)

# print("--------")
def dec_files(filenames, key, pref):
    for ff in filenames:
        # ff = "CC-"+ff
        Decrypt(ff, key, pref)


if __name__ == '__main__':
    PARSER.add_argument("-encpref",'--encrypt_prefix', type=str, default="CC", help="prefix for the encrypted files")
    PARSER.add_argument("-decpref",'--decrypt_prefix', type=str, default="De", help="prefix for the decrypted files")
    PARSER.add_argument("-en", '--encrypt', help="encrypt the files", action='store_true')
    PARSER.add_argument("-de", '--decrypt', help="decrypt the files", action='store_true')
    PARSER.add_argument("-inp",'--inputs', nargs='+', type=str, help="input files to encrypt or decrypt", required=True)
    PARSER.add_argument("-k",'--key', type=str, help="key to encrypt or decrypt the files", required=True)

    args = PARSER.parse_args()

    if args.encrypt and args.decrypt:
        raise ValueError("Please select either encryption or decryption, not both")

    if args.encrypt:
        enc_files(filenames=args.inputs, key=args.key, pref=args.encrypt_prefix)

    if args.decrypt:
        dec_files(filenames=args.inputs, key=args.key, pref=args.decrypt_prefix)
