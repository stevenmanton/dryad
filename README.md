Dryad
=====

[![Build Status](https://travis-ci.org/stevenmanton/dryad.svg?branch=master)](https://travis-ci.org/stevenmanton/dryad)

This project combines variable ontologies with typical Python tabular data processing to create easier, less repetitive workflows. In essence, it consists of two main concepts:

1. Organizing data into object-oriented variable ontologies
1. Directly applying function methods from variables onto the data in a fluent API

Why?
----

For most tools for working with tabular data, a schema consists of a list of string column names and a data type. This simple organization does not take advantage of the richness of relationships that often exists between variable types. As a result, typical data processing workflows end up consisting of manual manipulations of data by the user. In many cases, however, we would like *data that knows how to manipulate itself*.
   
Example
=======

```python
df.columns = [NameField('FirstName'), NameField('LastName'), DOBField('DOB')]
df.clean().validate()
```

Automatic field detection
-------------------------

