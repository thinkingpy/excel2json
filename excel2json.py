import xlrd
import os

# 将 excel 转换后输出成 json
def excel2json(excelpath,outpath,head_map=None):
    data = read_excel(excelpath, head_map)
    with open(outpath,encoding='utf8',mode="w") as f:
        f.write("\n".join([str(r) for r in data]))
        f.close()

# 将目录中的 excel 转换后合并输出成 json
def excel2json(excel_dirpath,outpath,head_map=None):
    excel_files =[x for x  in os.listdir(excel_dirpath) if x.endswith(".xls") ]
    data=[]
    for file in excel_files:
        excelpath=os.path.join(excel_dirpath,file)
        rst=read_excel(excelpath, head_map)
        data.extend(rst)
    with open(outpath,encoding='utf8',mode="w") as f:
        f.write("\n".join([str(r) for r in data]))
        f.close()

# 读取 excel 内容
def read_excel(excelpath,head_map=None):
    wordbook = xlrd.open_workbook(excelpath)
    table = wordbook.sheet_by_index(0)
    data=[]
    head= table.row_values(0)

    for rindex in range(1,table.nrows):
        row=table.row_values(rindex)
        rowObj={}
        for cindex in range(0,table.ncols):
            name=head[cindex]
            if head_map is not None:
                key = head_map[name]
                if(key!=''):
                    rowObj[key]=row[cindex]
            else:
                rowObj[name] = row[cindex]


        data.append(rowObj)

    return data

