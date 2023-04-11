# https://www.codewars.com/kata/563fbac924106b8bf7000046
# As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link to do all the dirty work in my place.
# What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.
# All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.
# Seems easy enough?
# Well, probably not so much, but we have one last extra rule: if one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.
# Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.


def generate_bc(url, separator):
    ignored_words = ["the", "of", "in", "from", "by", "with", "and", "or",
                     "for", "to", "at", "a"]
    prefixes = ("http://", "https://", "http:/")
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, "", 1)
            break

    SPLITTIE = url.split("/")
    try:
        SPLITTIE.remove('')
    except Exception:
        pass

    if SPLITTIE[-1].startswith("index."):
        SPLITTIE.pop(-1)
    SPLITTIE.pop(0)
    if len(SPLITTIE) == 0:
        result = '<span class="active">HOME</span>'
        return result
    HOMMIE = '<a href="/">HOME</a>'
    blacklist = ['?', '#']
    blacklist2 = ['html', 'htm', 'php', 'asp']
    MAGICSTARTSHERE = []

    for i in range(len(SPLITTIE)):
        BANANA = SPLITTIE[i]
        for j in range(len(BANANA)):
            if BANANA[j] in blacklist:
                BANANA = BANANA[:j]
                break
        if i > 0 and BANANA.startswith('-'):
            BANANA = BANANA.lstrip('-')
        if '.' in BANANA:
            ESPRESSO = BANANA.split('.')
            if ESPRESSO[-1] in blacklist2:
                BANANA = '.'.join(ESPRESSO[:-1])

        MAGICSTARTSHERE.append(BANANA)
    SPLITTIE = MAGICSTARTSHERE
    PROTOSPANNIE = str(SPLITTIE[-1].upper())
    if len(PROTOSPANNIE) > 30:
        PROTO2 = "".join(
            [word[0].upper() for word in PROTOSPANNIE.split("-") if
             word.lower() not in ignored_words])
        PROTO3 = ''.join(PROTO2)
        PROTOSPANNIE = PROTO3
    else:
        PROTOSPANNIE = PROTOSPANNIE.replace('-', ' ').upper()
    SPANNIE = '<span class="active">' + PROTOSPANNIE + '</span>'

    SPLITTIE.pop(-1)
    if len(SPLITTIE) == 0:
        result = HOMMIE + separator + SPANNIE
        return result

    def a_wrapper(part, position):
        replaced_part = part.replace('-', ' ')
        if len(part) > 30:
            part2 = "".join([word[0].upper() for word in part.split("-") if
                             word not in ignored_words])
            part3 = ''.join(part2)
        else:
            part3 = replaced_part.upper()
        if position == 0:
            return '<a href="/' + part + '/">' + part3 + '</a>'
        else:
            return '<a href="/' + "/".join(
                SPLITTIE[:position]) + '/' + part + '/">' + part3 + '</a>'

    MAGICSTARTSHERE = []
    for i in range(len(SPLITTIE)):
        part = SPLITTIE[i]
        MAGICSTARTSHERE.append(a_wrapper(part, i))
    if len(MAGICSTARTSHERE) == 1:
        MAGICSTARTSHERE = MAGICSTARTSHERE[0]
    else:
        MAGICSTARTSHERE = separator.join(MAGICSTARTSHERE)
    result = HOMMIE + separator + MAGICSTARTSHERE + separator + SPANNIE
    return result
