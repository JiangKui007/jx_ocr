# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2018/1/29 10:11'

import xml.dom.minidom
"""创建根节点"""
def creatroot(doc,rootElement):
    root = doc.createElement(rootElement)
    #设置根节点属性
    root.setAttribute("billtype","gl")
    root.setAttribute("codeexchanged","y")
    root.setAttribute("docid","989898989898")
    root.setAttribute("proc","add")
    root.setAttribute("receiver","2000")
    root.setAttribute("roottag","voucher")
    root.setAttribute("sender","1999")
    return root

"""导入id列表"""
def voucherIdList():
    """非嵌套结构"""
    idlist = {"id":"1499A91000000000WFKR"}
    return idlist

"""导入头部内容"""
def headContent():
    headContent ={"company":"040104",
         "voucher_type":"记账凭证",
         "fiscal_year":"2017",
         "accounting_period":"04",
         "voucher_id":"14",
         "attachment_number":"1",
         "enter":"林可加",
         "prepareddate":"2017-04-07",
         "cashier":"",
         "signature":"N",
         "checker":"",
         "posting_date":"",
         "posting_person": "",
         "voucher_making_system": "现金管理",
         "memo1": "",
         "memo2": "",
         "reserve1": "",
         "reserve2": "N",
         "revokeflag": "",
         }
    return headContent

"""导入输入内容"""
def entryContent():
    entryList = [
        {
            "entry_id":'1',
            'account_code': '51030801',
            'abstract': '俞光线报销差旅费（其中火车票费用）',
            'settlement': '',
            'bankcode': '',
            'notetype': '',
            'document_id': '',
            'document_date': '',
            'currency': '人民币',
            'unit_price': '0.00000000',
            'exchange_rate1': '0.00000000',
            'exchange_rate2': '1.00000000',
            'debit_quantity': '0.00000000',
            'primary_debit_amount': '209.0000',
            'secondary_debit_amount': '0.00000000',
            'natural_debit_currency': '209.0000',
            'credit_quantity': '0.00000000',
            'primary_credit_amount': '0.00000000',
            'secondary_credit_amount': '0.00000000',
            'natural_credit_currency': '0.00000000',
            'bill_type': '',
            'bill_id': '',
            'bill_date': '',
            'auxiliary_accounting': [('工程项目辅助核算','100')],
            'detail': '',
        },
        {
            "entry_id": '2',
            'account_code': '10020101',
            'abstract': '俞光线报销差旅费（其中火车票费用）',
            'settlement': '',
            'bankcode': '',
            'notetype': '',
            'document_id': '',
            'document_date': '',
            'currency': '人民币',
            'unit_price': '0.00000000',
            'exchange_rate1': '0.00000000',
            'exchange_rate2': '1.00000000',
            'debit_quantity': '0.00000000',
            'primary_debit_amount': '0.00000000',
            'secondary_debit_amount': '0.00000000',
            'natural_debit_currency': '0.00000000',
            'credit_quantity': '0.00000000',
            'primary_credit_amount': '209.0000',
            'secondary_credit_amount': '0.00000000',
            'natural_credit_currency': '209.0000',
            'bill_type': '',
            'bill_id': '',
            'bill_date': '',
            'auxiliary_accounting': [('工程项目辅助核算','100'),('现金流量项目','1124'),('往来项目辅助核算','09'),],
            'detail': '',
        }
    ]
    return entryList

"""主程序，创建xml文件"""
def creatXml():
    #在内存中创建一个空文档
    doc = xml.dom.minidom.Document()
    #创建一个根节点Managers对象
    root = creatroot(doc,'ufinterface')
    #将根节点加入doc文档中
    doc.appendChild(root)
    #读取voucher列表
    voucherIdList1 = voucherIdList()
    #    for i in voucherIdList1:  #遍历id列表
    nodeId = doc.createElement('voucher')
    #以id为标签创建voucher
    nodeId.setAttribute("id",str(voucherIdList1["id"]))
    root.appendChild(nodeId)
    #将voucher_head、voucher_body两个子节点加入voucher
    nodeHead = doc.createElement("voucher_head")
    nodeBody = doc.createElement("voucher_body")
    nodeId.appendChild(nodeHead)
    #为head赋值
    headContent1 =headContent()
    for item in headContent1:
        if item is not "revokeflag" :
            nodeName = doc.createElement(item)
            nodeName.appendChild(doc.createTextNode(headContent1.get(item)))
            nodeHead.appendChild(nodeName)
        else:
            nodeName = doc.createElement(item)
            nodeHead.appendChild(nodeName)
    nodeId.appendChild(nodeBody)
    #将entry子节点加入voucher_body
    entryContent1 = entryContent()
    for entryData in entryContent1:
        nodeEntry = doc.createElement("entry")
        nodeBody.appendChild(nodeEntry)
        for item in entryData:
            # 将节点遍历
            # 名称不是auxiliary_accounting的
            if item is not "auxiliary_accounting":
                entryChildNode = doc.createElement(item)
                entryChildNode.appendChild(doc.createTextNode(entryData.get(item)))
                nodeEntry.appendChild(entryChildNode)
            else:
                #名称是auxiliary_accounting的
                entryChildNode = doc.createElement("auxiliary_accounting")
                nodeEntry.appendChild(entryChildNode)
                itemList = entryData.get("auxiliary_accounting")
                for temptuple in itemList:
                    k,v = temptuple
                    entryGrandsunNode = doc.createElement("item")
                    entryGrandsunNode.setAttribute("name", k)
                    entryGrandsunNode.appendChild(doc.createTextNode(v))
                    entryChildNode.appendChild(entryGrandsunNode)
    return doc

if __name__ =="__main__":
    fp = open("test2.xml",'w+')
    doc = creatXml()
    doc.writexml(fp,indent='',addindent='\t',newl='\n',encoding='UTF-8')