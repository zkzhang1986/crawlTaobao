# _*_ coding:utf-8 _*_
# @FileName : Settings.PY
# @time     : 2020/9/7 15:01
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 20200908
# @Description: 参数设置

class Settings():

    def __init__(self):
        # 原始数据文件目录 Input
        # 店铺商品列表路径
        self.shopItemsPath = '..//ZSJRTaobao//Input//shopItems//'
        # 店铺商品列表爬取商品一页评论
        self.shopItemsOnePageCommPath = '..//ZSJRTaobao//Input//shopItemsOnePageComm//'
        # 商品列表所有评论(实际就是99页)
        self.shopItemsAllPageCommPath = '..//ZSJRTaobao//Input//shopItemsAllPageComm//'
        # 数据处理中文件目录
        self.process = '..//SJRTaobao//Process//'
        # 数据处理后输出
        self.output = '..//ZSJRTaobao//Output//'

        # 手机网页版天猫店id
        self.mShopId = 115842711
        # 天猫店销售id
        self.sEllerId = 2328901391

        # 手机网页版天猫店cookie
        self.mCookie = 'lid=gd_zzk888; enc=i5KLOflYb%2FS8Tqze1AKMG3vTxCttYOjRJ4cV30fE0QhO659eblJhak7eN0xyKv%2BAoURQfAA3qixzu2TpOs2apA%3D%3D; cna=WDK6F65Sl0wCAXeORULl6bLH; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E100dsredHMSnSRn6V9C%2FodBIS2Ea%2B%2BLN7nARb1mXp%2BBziL%2F6RH070K%2FIbHQDcddsMLvr6zdyhxsmc7YNIOcKvT6Ow%3D%3D; t=a05ba69ee87b559716af551ede32de86; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dCufXAC0ILsI47qqY%3D&id2=UNkwchw0GUym&nk2=BJJmy%2BsSQO%2F%2F; tracknick=gd_zzk888; uc4=id4=0%40Ug46vTm8Zo825HIKTevk2z43jXY%3D&nk4=0%40Bpa5i7mKAW0tp0o5QZpRIARhNhs%3D; lgc=gd_zzk888; _tb_token_=e1aef18e65e3e; cookie2=1dd13c2ff6e0c5870fc6c4d2a024c48a; xlly_s=1; _m_h5_tk=7c691a4b4b0fb410d4f726694235560e_1598601784937; _m_h5_tk_enc=e39a6dd9130c8c9225b9bdbb3134d7df; l=eBMrhFbuOOwEc9MiBOfZnurza77TQIRfguPzaNbMiOCP9if957lNWZP97X8pCnGVnsH6R3WlE43MBvTKeyUIQxv9-egE3aGqndLh.; tfstk=cj4GBgx2jlo6j_n3VNg_Nj9-EI5daIAEB-y_8yD9YdobaI4K_s2kY37MYMD3IrKf.; isg=BPj4FuWR0xPYYz_aiuSXsRQEyaaKYVzrVMUTdzJpRDPmTZg32nEsew5rAQXYHRTD'
        # PC端天猫店cookie
        self.pcCookie ='lid=gd_zzk888; enc=i5KLOflYb%2FS8Tqze1AKMG3vTxCttYOjRJ4cV30fE0QhO659eblJhak7eN0xyKv%2BAoURQfAA3qixzu2TpOs2apA%3D%3D; cna=WDK6F65Sl0wCAXeORULl6bLH; hng=CN%7Czh-CN%7CCNY%7C156; t=a05ba69ee87b559716af551ede32de86; tracknick=gd_zzk888; _tb_token_=f7e14e98ba780; cookie2=2459d29a14481a080b11c1638d4e2678; dnk=gd_zzk888; lgc=gd_zzk888; xlly_s=1; _m_h5_tk=2ab54805d1dcc8f05afbc25df956cb8b_1597987114097; _m_h5_tk_enc=acc2c9809ad34c0fa805d271fb011520; _l_g_=Ug%3D%3D; unb=397232047; cookie1=BxAdLiKCnaKhZWVTyqjLKL05zRnNeUlNFGBAqQrihds%3D; login=true; cookie17=UNkwchw0GUym; _nk_=gd_zzk888; sg=879; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTV6yD45OwnDA%3D%3D&cookie21=WqG3DMC9EdFmJgkfrG6mWw%3D%3D&pas=0&existShop=true&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D; uc3=id2=UNkwchw0GUym&nk2=BJJmy%2BsSQO%2F%2F&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCufTDAbAg5L21pmI%3D; uc4=nk4=0%40Bpa5i7mKAW0tp0o5QZWDnr4BMn8%3D&id4=0%40Ug46vTm8Zo825HIKTeQ7mIOcjwc%3D; sgcookie=EVzVWY1PxbVyzwUHVxLcW; csg=d9bffd05; x5sec=7b22726174656d616e616765723b32223a223930346332626664653766376236343233343231643864623233623238643538434a754d2f666b46454d696873377252724f664d53526f4c4d7a6b334d6a4d794d4451334f7a453d227d; tfstk=cticBQbNoqzjOcUoRnZjduMa6F0GZ5BzMflj404L2orS0qmPip7P87jWr7cmXN1..; l=eBMrhFbuOOwEchFhBOfwourza77OSIRAguPzaNbMiOCPOJfk56yRWZu35B8DC3GVh6SpR3WlE43gBeYBqIq0x6aNa6Fy_Ckmn; isg=BKSkGV7_pyh8EtNeBgiDzWBgdaKWPcinYGF_877FMG8zaUQz5k2YN9rPKcHxsQD_'

        # u
        self.userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'











