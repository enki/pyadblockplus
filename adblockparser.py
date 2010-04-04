import re
elemhideRegExp = '^([^\/\*\|\@"]*?)#(?:([\w\-]+|\*)((?:\([\w\-]+(?:[$^*]?=[^\(\)"]*)?\))*)|#([^{}]+))$'
regexpRegExp = '^(@@)?\/.*\/(?:\$~?[\w\-]+(?:=[^,\s]+)?(?:,~?[\w\-]+(?:=[^,\s]+)?)*)?$'
optionsRegExp = '\$(~?[\w\-]+(?:=[^,\s]+)?(?:,~?[\w\-]+(?:=[^,\s]+)?)*)$'

class Filter(object):
    knownfilters = {}
    
    @classmethod
    def fromText(klass, text):
        if not re.match('\S', text):
            return
        
        known = klass.knownfilters.get(text)
        if known:
            return known
        
        ret = None
        if re.match(elemhideRegExp, text):
            ret = 'elem hide'
        elif text[0] == '!':
            ret = None
        else:
            ret = RegExpFilter.fromText(text)
        
        klass.knownfilters[text] = ret
        return ret

class RegExpFilter(object):
    def __init__(self, origText, text, *args, **kwargs):
        self.whitelist = kwargs['whitelist']
    
    @classmethod
    def fromText(klass, text):
        origText = text
        whitelist = False
        if text.find('@@') == 0:
            whitelist = True
            # print 'white'
            text = text[2:]
        
        contentType = None
        matchCase = None
        domains = None
        thirdParty = None
        collapse = None
        options = None
        
        result = re.match(optionsRegExp, text)
        if result:
            print 'options not implemented'
        
        return klass(origText, text, contentType, matchCase, domains, thirdParty, collapse, whitelist=whitelist)
        
import sys
for text in open(sys.argv[1]).readlines():
    print Filter.fromText(text)