# Ciphers
An implementation of Caesar and substitution ciphers using classes.
## Caesar cipher
Here is an example of the Caesar cipher running using the Python interpreter:
```
>>> from caesar_cipher import *
>>> pt = PlaintextMessage('Quick Red Fox', 5)
>>> pt.get_message_text_encrypted()
'Vznhp Wji Ktc'
>>> pt.change_shift(8)
>>> pt.get_message_text_encrypted()
'Ycqks Zml Nwf'
>>> ct = CiphertextMessage('Ycqks Zml Nwf')
>>> ct.decrypt_message()
(18, 'Quick Red Fox')
```
## Substitution cipher
Here is an example of the substitution cipher running using the Python interpreter:
```
>>> from sub_cipher import *
>>> sm = SubMessage('The Lazy Yellow Lion.')
>>> sm.apply_transpose(sm.build_transpose_dict('eaoui'))
'Tha Lezy Yalluw Loun.'
>>> esm = EncryptedSubMessage('Tha Lezy Yalluw Loun.')
>>> esm.decrypt_message()
'The Lazy Yellow Lion.'
```
