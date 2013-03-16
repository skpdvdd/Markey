
Markey
======

**[Markey](https://github.com/skpdvdd/Markey)** is a [markdown](http://daringfireball.net/projects/markdown/) parser package for [Sublime Text 2](http://www.sublimetext.com/).

Installation
------------

Markey relies on [node](http://nodejs.org) and [marked](https://github.com/chjj/marked). Installation under Arch Linux:

    sudo pacman -S nodejs
    sudo npm install -g marked

To install Markey, clone the repository inside Sublime Text's `Packages` folder, e.g.:

    cd ~/.config/sublime-text-2/Packages/
    git clone git://github.com/skpdvdd/Markey.git

Configuration
-------------

The file `Markey.sublime-settings` contains a default configuration that should work out of the box. To change the configuration edit `Markey.sublime-settings` or better create a file called `Markey.sublime-settings` inside the `Packages/User` folder, like so:

    {
        "markdown_css_path" : "path/to/your/css/file",
    }

Usage
-----

Markey understands everything [marked](https://github.com/chjj/marked) does. Math is also supported (using [MathJax](http://www.mathjax.org/)). Syntax:

    inline math: $$y=kx+d$$
    display math: \[ e=mc^2 \]

Code highlighting is supported via [highlight.js](http://softwaremaniacs.org/soft/highlight/en/). Example:

    ```python
    print('hello')
    ```

Call Markey to convert the currently open buffer to markdown. You might want to add a key binding, e.g.:

    { "keys": ["alt+m"], "command": "markey" }

The parsed file will be opened in a new default browser window. The Python version Sublime Text 2 uses currently does not support all browsers, at least not on Linux. To account for this you can specify the browser name to call manually in the configuration file (e.g. `chromium`). If the `auto_convert` setting is `true` Markey will be called automatically if a file with the ending `.md`, `.markdown` or `.mdown` is saved. If you do not want this behaviour, set the setting to `false`.

Calling Markey will open a new browser even if the file is already open. Install the [LiveReload](https://github.com/dz0ny/LiveReload-sublimetext2) plugin if you don't want this behaviour.

Syntax highlighting
-------------------

Markey comes with a syntax definition comprising most of markdown as well as the math and code syntax described above. To enable syntax highlighting hit `ctrl+shift+p`, write `markey` and select `Set Syntax: Markey - Markdown`. You also need compatible styles to your style file (`.tmTheme`). A colorful example is shown below.

    <dict>
        <key>name</key>
        <string>markey inline math</string>
        <key>scope</key>
        <string>markey.math</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#4dd900</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markey display math</string>
        <key>scope</key>
        <string>markey.displaymath</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#4dd900</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markey code block</string>
        <key>scope</key>
        <string>markey.codeblock</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#00a2ff</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown code block</string>
        <key>scope</key>
        <string>markdown.codeblock</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#00a2ff</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown code</string>
        <key>scope</key>
        <string>markdown.code</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#00a2ff</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown emphasize</string>
        <key>scope</key>
        <string>markdown.em</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#ff3434</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown lists</string>
        <key>scope</key>
        <string>markdown.list</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#ff00ea</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown citations</string>
        <key>scope</key>
        <string>markdown.citation</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#b9bbd4</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown sections</string>
        <key>scope</key>
        <string>markdown.section</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#fff55a</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>markdown links</string>
        <key>scope</key>
        <string>markdown.link</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#ff00ea</string>
        </dict>
    </dict>

License
-------

Markey is released under the [zlib license](http://www.zlib.net/zlib_license.html).