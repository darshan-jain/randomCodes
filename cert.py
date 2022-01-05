from PIL import Image, ImageDraw, ImageFont
def gen_cert():
    global sample_clg_name,sample_name
    with open('sample_name.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
        font = ImageFont.truetype('./font/Poppins-Medium.otf',60)
        sample_name = []
        sample_clg_name = []
        for i in content:
            s = i.split(',')
            sample_name.append(s[0])
            sample_clg_name.append(s[1])
            sample_image = Image.open('sample_certi.png')
            draw = ImageDraw.Draw(sample_image)
            draw.text(xy=(400,350),text='{}'.format(s[0]),fill=(0,0,0),font=font)
            sample_image.save('./certificates/{}.png'.format(s[0]))
gen_cert()