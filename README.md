# Other News Sources

Other News Sources is a simple script that takes a news site url as an input, retrieves the title and searches Google News for other news sites/sources carrying the same news. Reddit news summarizer bots can use this little script to add alternative news sources.
### Version
0.1

###Requirements
  - requests
  - lxml

### Installation

```sh
$ sudo pip install requests
$ sudo pip install lxml
```
if a simple sudo pip install lxml doesn't work

```sh
$ sudo CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/libxml2 CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install lxml

```

###Usage
see example.py

### Development & Ramifications
I wrote this on a night I couldn't sleep. Please do not hold me accountable for accuracy or reliability.

###Improvements
  - possibility of doing a meta keywords based search
  - possibility of filtering recent news articles from captured links

License
----

MIT
