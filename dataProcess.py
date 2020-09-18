# _*_ coding:utf-8 _*_
# @FileName : dataProcess.PY
# @time     : 2020/9/8 10:19
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 20200901001
# @UpDate   : 202009011
# @Description: 文件读写处理

import re
import json
import xlwt
import xlrd
import pandas as pd
import os

from settings import Settings

class DataProcess:

    def file_input(self, filePath, fileName, fileData):
        '''
        数据存储
        :param filePath: 文件路径
        :param fileName: 文件名
        :param fileData: 文件内容
        :return:
        '''
        print('正在保存数据...')
        try:
            with open(filePath + str(fileName) + '.txt','a+', encoding='utf-8') as f:
                f.write(fileData)
            print('数据保存成功！')
            return 1
        except:
            print('数据写入失败！')
            return 0

    def file_read(self,filePath, fileName):
        '''
        数据读取
        :param filePath: 文件路径
        :param fileName: 文件名
        :return:
        '''
        print('正在读取数据...')
        try:
            with open(filePath + str(fileName) +'.txt', 'r', encoding='utf-8') as f:
                fileDate = f.readlines()
            print('数据读取成功！')
            return fileDate
        except:
            print('数据读取失败!')

    def get_mShop_items(self, filePath, fileName):
        '''
        解析原始数据，获取手机端Mitems信息
        :param filePath: 下载的原始shopItemsPath文件路径
        :param fileName: 手机端商店id（MshopId）
        :return: 处理后的Mitems商品信息
        '''
        fd = self.file_read(filePath,fileName)
        fd = [i.rstrip('\n') for i in fd if i != '\n']
        for fs in fd:
            mItemsInfo = json.loads(fs).get('items')
            for i in mItemsInfo:
                pMItemsInfo = {}
                pMItemsInfo['item_id'] = str(i.get('item_id'))
                pMItemsInfo['title'] = i.get('title')
                pMItemsInfo['url'] = i.get('url')
                pMItemsInfo['price'] = i.get('price')
                pMItemsInfo['sold'] = i.get('sold')
                pMItemsInfo['quantity'] = i.get('quantity')  # 库存
                pMItemsInfo['totalSoldQuantity'] = i.get('totalSoldQuantity')
                yield pMItemsInfo

    # def pMItemsInfoToExcel(self,inputFilePath,fileName,outputFilePath):
    #     # 已经迁移到run.py
    #     pMItemsInfo = []
    #     for pMItemInfo in self.get_mShop_items(inputFilePath,fileName):
    #         pMItemsInfo.append(pMItemInfo)
    #     print(pMItemsInfo)
    #     self.toExcel(pMItemsInfo,outputFilePath,fileName)

    def toExcel(self,fileData,outputFilePath, fileName):
        '''
        将数据保存在excel文件
        :param fileData: 数据
        :param outputFilePath: 数据路径
        :param fileName: 文件名
        :return:
        '''
        # fileData = fileData
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet(str(fileName) + 'items')
        ii = list(fileData[0].keys())
        for i in range(0,len(ii)):
            sheet1.write(0,i,ii[i])
        for j in range(0,len(fileData)):
            m = 0
            ls = list(fileData[j].values())
            for k in ls:
                sheet1.write(j+1,m,k)
                m += 1
        workbook.save(outputFilePath + str(fileName) + '.xls' )

    def get_pMItemsInfo_MitemsId(self, inputFilePath, fileName):
        '''
        从excel表同获取mItemsId
        :param inputFilePath: 文件路径output目录下的excel文件
        :param fileName: 文件名
        :return: 集合类型的 mItmesId
        '''
        fileDate = pd.read_excel(inputFilePath + str(fileName) + '.xls', encoding='utf-8')
        items = fileDate['item_id'].values.tolist()
        mItemsId = set()
        for item in items:
            mItemsId.add(item)
        return mItemsId

    def get_comm_file_name(self, inputFilePath):
        """
        1.根据文件路径再通过正则表达式提取文件中的数字，此数字就是商品列表id并且返回。
        2.清洗商品列表id，形成列表，返回int类型
        3.根据item解析文件第一页评论内容 得到item对于页数 类型为字典类型
        upDate:20200910
        :return:
        """
        # 根据文件路径再通过正则表达式提取文件中的数字，此数字就是商品列表id并且返回。
        dirs = os.listdir(inputFilePath)
        file_name_ls = []
        for file in dirs:
            file_items = re.findall('^Comm(.*?).txt',file)
            file_name_ls.append(file_items)

        # 清洗商品列表id，形成列表，返回int类型
        new_file_name_ls = []
        for i in file_name_ls:
            if i != []:
                new_file_name_ls.append(int(i[0]))
        # return new_file_name_ls

        # 根据item解析文件第一页评论内容 得到item对于页数
        item_page_ls = []
        for file_name_ls in new_file_name_ls:
            with open( inputFilePath + '\\Comm' + str(file_name_ls) + '.txt', 'r', encoding='utf-8') as f:
                fd = f.read()
                fd = re.findall('\\((.*)\\)', fd)
                for i in fd:
                    item_page_dict = {}
                    i = json.loads(i)
                    page = i.get('rateDetail').get('paginator').get('lastPage')
                    # print(page)
                    item_page_dict[file_name_ls] = page
                    # print(item_page_dict)
                    item_page_ls.append(item_page_dict)
        return item_page_ls

    def process_item_page(self, item_page_ls):
        """
        用于过滤评论页数为0的商品。（选择用）
        :param item_page_ls: 参数是get_comm_file_name()函数值。
        :return: 过滤就的item_page数据
        """
        item_page_ok_ls = []
        for i in item_page_ls:
            i_items = i.items()
            item_page_dict = {}
            for key, values in i_items:
                # 评论页为0的过滤掉。
                if values != 0:
                    # print(key,values)
                    item_page_dict[key] = values
                    item_page_ok_ls.append(item_page_dict)
        # print(item_page_ok_ls)
        return item_page_ok_ls

    def parse_item_comm(self,inputFilePath):
        """
        解析商品评论
        updata:20200911
        :param inputFilePath:
        :return:
        """
        # 获取文件名
        dirs = os.listdir(inputFilePath)
        file_name_ls = []
        # 正则表达式获取评论json
        for file in dirs:
            file_items = re.findall('^(.*?).txt', file)
            file_name_ls.append(file_items)
        # counts = 0
        for itemid in file_name_ls:
            # print(itemid)
            fd = self.file_read(inputFilePath,itemid[0])
            for i in fd:
                ss = re.findall('\\((.*)\\)', i)
                for s in ss:
                    # 解析评论
                    item = json.loads(s)
                    item_rateLists = item.get('rateDetail').get('rateList')
                    pages = item.get('rateDetail').get('paginator').get('lastPage')
                    for item_rateList in item_rateLists:
                        item_data = {}
                        item_data['itemID'] = itemid
                        item_data['pages'] = pages
                        item_data['id'] = item_rateList.get('id')
                        item_data['displayUserNick'] = item_rateList.get('displayUserNick')
                        item_data['rateContent'] = item_rateList.get('rateContent')
                        item_data['rateDate'] = item_rateList.get('rateDate')
                        # counts += 1
                        # print(item_data)
                        yield item_data
        # print('总条数：{}'.format(counts))



# 测试本类
# if __name__ == '__main__':
#     settings = Settings()
#     dataProcess = DataProcess()
#     dataProcess.parse_item_comm(settings.shopItemsAllPageCommPath)


#     fname=dataProcess.get_comm_file_name(settings.shopItemsOnePageCommPath)
#     print(fname)
#     inputFilePath = settings.shopItemsPath
#     fileName = settings.mShopId
#     outputFilePath = settings.output
#     # dataProcess.pMItemsInfoToExcel(inputFilePath, fileName , outputFilePath)
#     # 测试获取 itemsId
#     itemsId = dataProcess.read_pMItemsInfo(outputFilePath,fileName)
#     print(len(itemsId))
#     for i in itemsId:
#         print(i)


