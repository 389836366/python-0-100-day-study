#BMI=体重/身高²
#BMI计算器
#18.5<=BMI<24是正常范围，BMI<18.5说明体重过轻，BMI>=24说明体重过重，大于27说明肥胖
height = float(input('请输入身高(cm): '))
weight = float(input('请输入体重(kg): '))
BMI = weight / (height/100) ** 2
print(f'{BMI = :.1f}')
if BMI < 18.5:
    print('你的体重过轻!')
elif 18.5<= BMI < 24:
    print('你的身材很标准！')
elif 24 <= BMI < 27:
    print('你的体重过重！')
else:
    print('你已达到肥胖！')

