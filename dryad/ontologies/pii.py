from __future__ import absolute_import

from ..ontology import *

class SSN(DigitField):
    pass

class NameField(StringField):
    pass

class AddressField(StringField):
    pass

class PhoneField(StringField):
    pass

class DOBField(DateField):
    pass

class EmailField(StringField):
    pass
