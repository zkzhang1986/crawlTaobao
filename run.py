# _*_ coding:utf-8 _*_
# @FileName : run.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 202009011
# @Description: 运行主函数

from crawlerTaobaoItem import CrawlerTaobaoItem
from dataProcess import DataProcess
from settings import Settings
from crawlerTaobaoComment import CrawlerTaobaoComment

# import crawlerTaobaoComment
import filePreRegular
import time

settings = Settings()
dataProcess = DataProcess()
crawlerTaobaoItem = CrawlerTaobaoItem()
crawlerTaobaoComment = CrawlerTaobaoComment()

def crawlerTaobaoItems(pages):
    # 通过手机端获取商品信息并下载保存原始数据
    # crawlerTaobaoItem = CrawlerTaobaoItem()
    for page in range(1,pages):
        print('第{}页'.format(page))
        crawlerTaobaoItem.get_mShop_items(page)
        print('休息一下...(约25秒)')
        time.sleep(25)

def pMItemsInfoToExcel():
    '''
    将dataProcess.get_mShop_items()与 dataProcess.toExcel串起来。
    主要功能：将get_mShop_items()处理后的Mitems商品信息保存在excel文件
    :param inputFilePath: 用于get_mShop_items()中数据来源
    :param fileName: 文件名
    :param outputFilePath: 保存excel路径
    :return:
    '''
    # dataProcess = DataProcess()
    # 以下是参数。【我已经被参数搞晕了，直接将传参写函数里，要修改直接修改函数中的参】
    # 解析原始数据的目录（即第一次爬取手机端获取商品信息下载保存原始数据）。
    inputFilePath = settings.shopItemsPath
    # 文件名
    fileName = settings.mShopId
    # 保存到excel的文件路径
    outputFilePath = settings.output

    pMItemsInfo = []
    # 解析原始数据，获取手机端Mitems信息。添加到 pMItemsInfo 列表中
    for pMItemInfo in dataProcess.get_mShop_items(inputFilePath, fileName):
        pMItemsInfo.append(pMItemInfo)
    # 将 pMItemsInfo 列表中数据保存在excel文件
    dataProcess.toExcel(pMItemsInfo, outputFilePath, fileName)

def crawlerTaobaoItemOnepageComm():
    '''
    获取商品的第一页评论
    :return:
    '''
    # 以下是参数。【我已经被参数搞晕了，直接将传参写函数里，要修改直接修改函数中的参】
    # 读取excel的路径
    inputFilePath = settings.output
    # 爬取商品第一页评论的原始数据保存路径
    getOnepageCommFilePath = settings.shopItemsOnePageCommPath
    # 文件名
    fileName = settings.mShopId
    # 爬取评论的页数。
    pages = 1
    # 用来控制保存数据路径。
    isOneage = 'Y'
    # 从excel中获取itemsid
    pMItems_id = dataProcess.get_pMItemsInfo_MitemsId(inputFilePath, fileName)
    # print(items_id)
    # 通过for循环 爬取每个商品的第一页评论
    for pMitem_id in pMItems_id:
        print('商品itemId:{}'.format(pMitem_id))
        crawlerTaobaoComment.get_items_comm(getOnepageCommFilePath, pMitem_id, pages, isOneage)
        print('休息一下...(约25秒)')
        time.sleep(25)

def crawlerTaobaoItemAllpageComm():
    """
    根据itemid爬取淘宝所有评论
    :return:
    """
    item_page_ls = dataProcess.get_comm_file_name(settings.shopItemsOnePageCommPath)
    getAllpageCommFilePath = settings.shopItemsAllPageCommPath
    isOneage = 'N'
    for i in item_page_ls :
        i_item = i.items()
        for key,values in i_item:
            print("商品item:{},总页数:{}".format(key,values))
            for values_i in range(1, int(values)+1):
                print("商品item_id:{},第{}页".format(key,values_i))
                crawlerTaobaoComment.get_items_comm(getAllpageCommFilePath, key, values_i, isOneage)
                # continue
                print('休息一下...(约25秒)')
                time.sleep(25)

def itemComToexcel():
    """
    把解析出来的评论内容，存储在excel文件中
    updata:20200911
    :return:
    """
    # 需要解析原始数据的路径
    inputFilePath = settings.shopItemsAllPageCommPath
    # excel文件名
    fileName = '中顺洁柔天猫旗舰店评论'
    # 保存到excel的文件路径
    outputFilePath = settings.output

    itemsCom = []
    for itemCom in dataProcess.parse_item_comm(inputFilePath):
        itemsCom.append(itemCom)
    # print(itemsCom)
    # 保存到excel中
    dataProcess.toExcel(itemsCom, outputFilePath, fileName)


if __name__ == '__main__':

    input_ = eval(input("1.获取手机端商品信息；"
                        "2.手机端商品信息保存到excel；"
                        "3.爬取商品一页的评论；"
                        "4.获取商品所有评论；"
                        "5.保存商品评论到excel文件；"
                        "请录入数字："))
    if input_ == 1:
        # peges 是根据ajax 数据得到。
        pages = 18
        # 通过手机端获取商品信息并下载保存原始数据
        crawlerTaobaoItems(pages)
    elif input_ == 2:
        # 将get_mShop_items()处理后的Mitems商品信息保存在excel文件
        pMItemsInfoToExcel()
    elif input_ == 3:
        # 获取商品的第一页评论
        crawlerTaobaoItemOnepageComm()
    elif input_ == 4:
        # 获取商品所有评论
        crawlerTaobaoItemAllpageComm()
    elif input_ == 5:
        itemComToexcel()
