import html2text

handler = html2text.HTML2Text()
handler.ignore_links = True

def to_text(text):
    return handler.handle(text)
