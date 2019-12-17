# 2XCompose
Automated commandline tools for creating, cleaning and maintaining XCompose files.

An XCompose file consists of lines that may be `include` statements or lines formatted as
```
    <𝐴> [<𝐵> ⋯ ] : "𝐶" U𝑋 [#𝑁]
```
where 𝐴, 𝐵,… are keys forming the key combination for the character, 𝐶 is the Unicode character, 𝑋 is the hexadecimal Unicode point and 𝑁 is 𝐶's Unicode name.
For example,
```
    <Multi_key> <braceleft> <parenleft>: "⊂" U2282 # SUBSET OF
    <Multi_key> <braceleft> <equal> <parenleft>: "⊆" U2286 # SUBSET OF OR EQUAL TO
    <Multi_key> <exclam> <braceleft> <parenleft>: "⊄" U2284 # NOT A SUBSET OF
```
Text after a pound-sign, #, are comments. So while not strictly required, the Unicode names are nice to have for human readers, and can be used to find errors.

## Utilities

* `cleanXCompose` proofreads an XCompose file correlating characters 𝐶 with the provided hex Unicode points 𝑋. It preserves user comments, includes and empty lines. User provided names are ignored and are replaced in output by the name provided in the selected database (Python's built in or `--web`).
* `char2XCompose` takes a single Unicode character as a positional argument, and optionally a key string `<𝐴> [<𝐵> ⋯]` specified with `--keys`. It produces a formatted line for an XCompose file, complete with hex codepoint and name comment. Uses Python's built in Unicode database, or web interfece if provided `--web`.
* `hex2XCompose` takes a string, a hex Unicode codepoint such as `U21D4` and optionally a key string `<𝐴> [<𝐵> ⋯]` specified with `--keys`. It produces a formatted line for an XCompose file, complete with hex codepoint and name comment. Uses Python's built in Unicode database, or web interfece if provided `--web`.
* `name2XCompose` takes a single string and uses Python's build in name-lookup, producing a formatted XCompose line complete with hex codepoint and name comment. The string (the positional argument) is automatically made uppercase. No `--web` option because Tobin's interface doesn't offer name-lookup.

*NB:* if `--keys` doesn't begin with `<Multi_key>`, it will be automatically prepended. If no `--keys` are specified, `<Multi_key>` alone will be the default.

Thanks to [Richard Tobin](http://www.cogsci.ed.ac.uk/~richard/) for maintaining the web app used for the web back-end: http://www.ltg.ed.ac.uk/~richard/utf-8.html
