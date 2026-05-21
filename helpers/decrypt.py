import base64


def decrypt_data(enc_url):
    try:
        data = base64.b64decode(enc_url)
        return data.decode()
    except:
        return enc_url
