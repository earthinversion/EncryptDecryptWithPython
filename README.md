# Encrypt and Decrypt your software using Python
```
$ python endecrypt_with_python.py -h
usage: endecrypt_with_python.py [-h] [-encpref ENCRYPT_PREFIX]
                                [-decpref DECRYPT_PREFIX] [-en] [-de] -inp
                                INPUTS [INPUTS ...] -k KEY

Python utility program to encrypt/decrypt multiple files (by Utpal Kumar, UC
Berkeley, 2021/11)

optional arguments:
  -h, --help            show this help message and exit
  -encpref ENCRYPT_PREFIX, --encrypt_prefix ENCRYPT_PREFIX
                        prefix for the encrypted files
  -decpref DECRYPT_PREFIX, --decrypt_prefix DECRYPT_PREFIX
                        prefix for the decrypted files
  -en, --encrypt        encrypt the files
  -de, --decrypt        decrypt the files
  -inp INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        input files to encrypt or decrypt
  -k KEY, --key KEY     key to encrypt or decrypt the files

enter filename(s) and key to encrypt and decrypt
```

## Example
### Encrypt files
```
$ python endecrypt_with_python.py -inp "myscript.py" "helloworld.py" -k "password" -en 
```

### Decrypt files:
```
$ python endecrypt_with_python.py -inp "CC-myscript.py" "CC-helloworld.py" -k "password" -de 
```