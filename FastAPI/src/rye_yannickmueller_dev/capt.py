from captcha.image import ImageCaptcha

async def generate(text):
    image = ImageCaptcha(fonts=['./static/captcha.ttf'])
    data = image.generate(text)
    image.write(text, f'./static/captchas/{text}.jpg')
