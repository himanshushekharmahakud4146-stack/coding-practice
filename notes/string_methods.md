# String Manipulation Methods

Common Python string operations used in coding interviews.

## lower()
Converts all characters of a string to lowercase.

Example
"HELLO".lower() -> "hello"

## upper()
Converts all characters to uppercase.

Example
"hello".upper() -> "HELLO"

## isalnum()
Checks whether a character is alphanumeric (letter or number).

Example
"a".isalnum() -> True
"#".isalnum() -> False

## strip()
Removes spaces from beginning and end.

Example
" hello ".strip() -> "hello"

## replace()
Replaces part of a string.

Example
"hello".replace("h","y") -> "yello"

## split()
Splits a string into a list.

Example
"a b c".split()

## join()
Joins a list into a string.

Example
" ".join(["a","b","c"])

## String Slicing

Reverse a string:

string[::-1]

Example
"hello"[::-1] -> "olleh"