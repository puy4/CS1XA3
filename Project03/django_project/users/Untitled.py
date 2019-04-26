def pluralize(w):
    if w[-1:]=='s'or 'h':
        w+='es'
    elif w[-1:]=='y':
        w = w[:-1]
        w +='ies'
    else:
        w +='s'
    return w
    # Your code here
