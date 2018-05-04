# Ciphers
An implementation of Caesar and substitution ciphers using classes.
## Caesar cipher
Here is an example of the Caesar cipher running in the Python interpreter:
```
>>> import caesar_cipher as cc
>>> pt = cc.PlaintextMessage('Quick Red Fox', 5)
>>> pt.get_message_text_encrypted()
'Vznhp Wji Ktc'
>>> pt.change_shift(8)
>>> pt.get_message_text_encrypted()
'Ycqks Zml Nwf'
>>> ct = cc.CiphertextMessage('Ycqks Zml Nwf')
>>> ct.decrypt_message()
(18, 'Quick Red Fox')
```
