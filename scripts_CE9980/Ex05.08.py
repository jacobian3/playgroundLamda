personal_info = "595-33-9193:68:Columbus, OH"

social, num, cit_sta = personal_info.split(':')

# triple-quoted multiline string
print("""SS#: {}
Age: {}
Residence: {}""".format(social, num, cit_sta)
)


