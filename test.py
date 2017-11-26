from excel2json import  excel2json


head_map={'执行日期':"",
          '航空公司':"Airline",
          '主附航班':"",
          '航班号':"Flight",
          '属性':"",
          '任务':"",
          '进出':"Direction",
          '出发站':"",
          '起飞时间':"DepTime",
          '到达时间':"ArrTime",
          '到达站':"",
          '内部异常状态':"",
          '内部异常原因':"",
          '外部异常状态':"",
          '外部异常原因':"",
          '机号':"",
          '机型':"Model",
          '机位':"StopPosition",
          '航线':"",
          '备降站':"",
          '值机柜台':"",
          '登机口':"",
          '滑槽':"",
          '行李转盘':"",
          '航站楼':"",
          '混合航班国际段航站楼':"",
          'VIP':"",
          'CDM预降':"",
          'CDM计降':"",
          'CDM计撤':"",
          'CDM计起':""
}
excelFilePath=""
excelFileBundleDir=r"D:\_MyProjects\AirPark\Document\需求\201711\5.1_7.31"
exportJsonFileName=r"D:\out\excel2json.json"

# dd=read_excel(r"D:\_MyProjects\AirPark\Document\需求\201711\5.1_7.31\5.17-5.20.xls",head_map)
# print("\n".join([str(nd) for nd in dd]))

excel2json(excelFileBundleDir,exportJsonFileName,head_map)
# print("\n".join([str(nd) for nd in dd]))
