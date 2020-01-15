# Copyright

Generate copyright.

# Features

* format: `© {year} {name}`
* example: `© 2020 ytyaru`

# Requirement

* Python 2.7
* Python 3

# Installation

```sh
pip2 install --user -i https://test.pypi.org/simple/ Copyright
pip3 install --user -i https://test.pypi.org/simple/ Copyright
```

# Usage

```python
from Copyright import Copyright 
```
```python
Copyright.Generator()
Copyright.Generator('Your name')
```

# Note

* The year is local time. Not UTC time.
* Only TestPyPI was registered. Could not register with PyPI. #1, #2

# Author

　ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

