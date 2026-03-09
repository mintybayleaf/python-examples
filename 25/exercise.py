def xmltag(tag, *args, **kwargs):
    attributes = " ".join(f'{k}="{v}"' for k, v in kwargs.items())
    value = " ".join(args)
    return f"<{tag} {attributes}>{value}</{tag}>"


print(xmltag("foo"))
print(xmltag("foo", "bar"))
print(xmltag("foo", "bar", a=1, b=2, c=3))
