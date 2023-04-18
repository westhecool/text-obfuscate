import sys
new = "ⱯɃÇƉƐƑƓĦİĴƘĿMNOƤɊŘŞŦŲVɰXɎƵɐɓƈɖɛƒɠɦɨʝƙɭɱŋơƥʠɾʂƭųʋɯxƴʒ"
old = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def textobfuscate(s):
    r = ''
    for x in s:
        try:
            r += new[old.index(x)]
        except ValueError:
            r += x
    return r
print(textobfuscate(sys.argv[1]))
