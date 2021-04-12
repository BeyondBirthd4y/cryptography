def cripto(frase):
    tradutor=""
    for letra in frase:
        if letra in "Aa":
            tradutor=tradutor+"Я"
        elif letra in "Bb":
            tradutor=tradutor+"Ю"
        elif letra in "Cc":
            tradutor=tradutor+"Э"
        elif letra in "Dd":
            tradutor=tradutor+"Ѣ"
        elif letra in "Ee":
            tradutor=tradutor+"Ж"
        elif letra in "Ff":
            tradutor=tradutor+"Ф"
        elif letra in "Gg":
            tradutor=tradutor+"Щ"
        elif letra in "Hh":
            tradutor=tradutor+"Ш"
        elif letra in "Ii":
            tradutor=tradutor+"Ч"
        elif letra in "Jj":
            tradutor=tradutor+"Ц"
        elif letra in "Kk":
            tradutor=tradutor+"Х"
        elif letra in "Ll":
            tradutor=tradutor+"У"
        elif letra in "Mm":
            tradutor=tradutor+"Т"
        elif letra in "Nn":
            tradutor=tradutor+"С"
        elif letra in "Oo":
            tradutor=tradutor+"Р"
        elif letra in "Pp":
            tradutor=tradutor+"П"
        elif letra in "Qq":
            tradutor=tradutor+"О"
        elif letra in "Rr":
            tradutor=tradutor+"Н"
        elif letra in "Ss":
            tradutor=tradutor+"М"
        elif letra in "Tt":
            tradutor=tradutor+"А"
        elif letra in "Uu":
            tradutor=tradutor+"Б"
        elif letra in "Vv":
            tradutor=tradutor+"В"
        elif letra in "Ww":
            tradutor=tradutor+"Г"
        elif letra in "Xx":
            tradutor=tradutor+"Д"
        elif letra in "Yy":
            tradutor=tradutor+"Е"
        elif letra in "Zz":
            tradutor=tradutor+"И"
        else:
            tradutor=tradutor + letra
    return tradutor

print(cripto(input("Digite a Mensagem:")))
