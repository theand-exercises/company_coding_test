import string #fixed typo was using
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

print string.translate("COME TO ROME", rot13)
print string.translate("Yogiyo", rot13)
print string.translate("Lbtvlb", rot13)
