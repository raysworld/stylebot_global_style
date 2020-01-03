# font family
font_family_cn_seri = ['Simsun', 'NSimsun', '宋体', '新宋体']
font_family_cn_sans = ['Simhei', '黑体', 'Microsoft Yahei', '微软雅黑']
font_family_en_seri = ['Arial', 'Arial Black', 'Tahoma', 'Trebuchet MS', 'Verdana', 'Segoe UI']
font_family_en_sans = ['Times New Roman', 'Times', 'Times CY']
font_family_mn_seri = ['Georgia', 'Courier New', 'Palatino Linotype']
font_family_mn_sans = ['Consolas', 'Helvetica', 'Helvetica Neue', 'Lucida Console', 'Monaco']

# unicode range
unicode_range_cn  = 'U+2E80-FFFF'
unicode_range_en  = 'U+0-2E7F'
unicode_range_all = 'U+0-FFFF'

'''
    Call gen_font_style function to generate a font replacement style
'''
def gen_font_style(font_family, font_style, unicode_range, font_replace):
    font_face = '''font-family: "{old_font}"; \
{font_style}unicode-range: {unicode_range}; \
src: local("{new_font}");'''.format(
                       old_font=font_family, 
                       font_style=font_style, 
                       unicode_range=unicode_range, 
                       new_font=font_replace)
    font_face = '@font-face { %s }\n' % font_face

    return font_face

# the result will be saved to style.txt
file = open('style.txt','w')
for f in font_family_cn_seri:
    file.write(gen_font_style(f, '', unicode_range_all, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_all, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_all, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_all, 'Source Han Serif'))

for f in font_family_cn_sans:
    file.write(gen_font_style(f, '', unicode_range_all, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_all, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_all, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_all, 'Source Han Sans CN Normal'))

for f in font_family_cn_seri:
    file.write(gen_font_style(f, '', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_cn, 'Source Han Serif'))

for f in font_family_en_sans:
    file.write(gen_font_style(f, '', unicode_range_cn, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_cn, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_cn, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_cn, 'Source Han Sans CN Normal'))
    file.write(gen_font_style(f, '', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_en, f))

for f in font_family_mn_seri:
    file.write(gen_font_style(f, '', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_cn, 'Source Han Serif'))
    file.write(gen_font_style(f, '', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_en, f))

for f in font_family_mn_sans:
    file.write(gen_font_style(f, '', unicode_range_cn, 'Sarasa Mono SC'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_cn, 'Sarasa Mono SC'))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_cn, 'Sarasa Mono SC'))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_cn, 'Sarasa Mono SC'))
    file.write(gen_font_style(f, '', unicode_range_en, 'Sarasa Mono SC'))
    file.write(gen_font_style(f, 'font-weight: bold; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-style: italic; ', unicode_range_en, f))
    file.write(gen_font_style(f, 'font-weight: bold; font-style: italic; ', unicode_range_en, f))

file.close()