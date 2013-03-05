
# Copyright (C) 2013 Christopher Pramerdorfer

# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.

# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:

# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import sublime, sublime_plugin
import subprocess, tempfile, webbrowser, re, os

class MarkeyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.convert()

    # fix relative links
    def fixLinks(self, match) :
        fpath = match.group(1)
        if fpath.startswith(('http://', 'https://', 'file://', '/')) :
            return 'src="' + fpath + '"'
        else :
            return 'src="' + self.fileDir + "/" + fpath + '"'

    # replace inline math with placeholders
    def stripInlineMath(self, match) :
        self.inlineMathStr.append(match.group(1))
        return '$$' + str(len(self.inlineMathStr) - 1) + '$$'

    # replace display math with placeholders
    def stripDisplayMath(self, match) :
        self.displayMathStr.append(match.group(1))
        return '^^^' + str(len(self.displayMathStr) - 1) + '^^^'

    # replace inline math placeholders with actual content
    def replaceInlineMath(self, match) :
        return '$$' + self.inlineMathStr[int(match.group(1))] + '$$'

    # replace display math placeholders with actual content
    def replaceDisplayMath(self, match) :
        return '\\[' + self.displayMathStr[int(match.group(1))] + '\\]'

    def convert(self):
        # load settings
        settings = sublime.load_settings('Markey.sublime-settings')

        # get directory of current file
        self.fileDir = os.path.dirname(self.view.file_name())

        # get content
        region = sublime.Region(0, self.view.size())
        content = self.view.substr(region)

        # strip math if needed
        if settings.get('parse_math') :
            self.inlineMathStr = []
            reInlineMath = re.compile(r'\$\$(.+?)\$\$')
            content = reInlineMath.sub(self.stripInlineMath, content)

            self.displayMathStr = []
            reDisplayMath = re.compile(r'\\\[(.+?)\\\]', re.MULTILINE | re.DOTALL)
            content = reDisplayMath.sub(self.stripDisplayMath, content)

        # search for code
        haveCode = re.search(r'^```[a-zA-Z]+', content, re.MULTILINE) is not None

        # send to marked and get result
        sp = subprocess.Popen('marked', stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=-1)
        markdown = sp.communicate(content)[0]

        # fix relative links
        reSrc = re.compile(r'src="(.+?)"')
        markdown = reSrc.sub(self.fixLinks, markdown)

        # replace math if needed
        if settings.get('parse_math') :
            reInlineMath = re.compile(r'\$\$(\d+)\$\$')
            markdown = reInlineMath.sub(self.replaceInlineMath, markdown)

            reDisplayMath = re.compile(r'\^\^\^(\d+)\^\^\^')
            markdown = reDisplayMath.sub(self.replaceDisplayMath, markdown)

        # create file contents
        html =  '<!DOCTYPE HTML>\n<html>\n<head>\n'
        html += '<link rel="stylesheet" href="' + settings.get('markdown_css_path') + '">\n'

        if haveCode :
            html += '<link rel="stylesheet" href="' + settings.get('highlight_js_css_path') + '">\n'
            html += '<script src="' + settings.get('jquery_path') + '"></script>\n'

            html += '<script src="' + settings.get('highlight_js_path') + '"></script>\n'
            html += '<script>\n$(document).ready(function() {\n'
            html += '$("pre > code[class]").each(function(i, e) { hljs.highlightBlock(e)} );\n});\n</script>\n'

        if settings.get('parse_math') and (len(self.inlineMathStr) > 0 or len(self.displayMathStr) > 0) :
            html += '<script src="' + settings.get('mathjax_path') + '"></script>\n'
            html += '<script type="text/x-mathjax-config">\nMathJax.Hub.Config({\ntex2jax: {\n'
            html += 'inlineMath: [["$$","$$"]],\n'
            html += 'displayMath: [["\\\\[","\\\\]"]]\n'
            html += '}});\n</script>\n'

        html += '</head>\n\n<body>\n'
        html += markdown
        html += '</body>\n</html>\n'

        # write to temp file
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(html.encode('utf-8'))
        f.close()
        
        # open file in browser (linux: might need to set BROWSER envvar)
        webbrowser.open(f.name)
