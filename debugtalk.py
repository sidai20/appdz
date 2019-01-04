import pymysql
def connectMysql(sql,fetch="one"):
    conn = pymysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        if "one" == fetch:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        raise e

# 获取桌位
def getTableid():
    sql = "SELECT MAX(id) FROM xt_dc_seller_table WHERE sellerid = 154 and `status` = 0 and `enable` = 1 "
    result = connectMysql(sql)
    print(result)
    return result[0]
#查询新建订单
def getCreatID():
    sql = "SELECT MAX(id) FROM xt_dc_order WHERE sellerid = 154"
    result = connectMysql(sql)
    return str(result[0])
#备注
def getremark():
    sql = "SELECT id FROM xt_dc_remark WHERE sellerid = 154"
    result = connectMysql(sql,"all")
    return result[0][0]

#订单时间
def getcdate(orderid):
    sql = "SELECT cdate FROM xt_dc_order WHERE id = {}".format(orderid)
    result = connectMysql(sql)
    return result[0]
#获取菜品id
def getcookbookid():
    sql = "SELECT MAX(id) FROM xt_dc_seller_cookbook WHERE sellerid = 154"
    result = connectMysql(sql)
    return result[0]
#获取菜品价格
def getcookPrice():
    cookid = getcookbookid()
    sql = "SELECT price FROM xt_dc_seller_cookbook WHERE id = {}".format(cookid)
    result = connectMysql(sql)
    return result[0]

#获取餐位费
def getmeal_fee(orderid,meal_fee):
    sql = "SELECT meal_fee FROM xt_dc_order WHERE id = {}".format(orderid)
    result = connectMysql(sql)
    total = int(result[0]/int(meal_fee))
    return total
#获取订单金额
def getPrice(orderid):
    sql = "SELECT price FROM xt_dc_order WHERE id = {}".format(orderid)
    result = connectMysql(sql)
    return result[0]
#获取支付方式
def getPayment():
    sql = "SELECT id FROM xt_dc_seller_payment WHERE sellerid = 154"
    result = connectMysql(sql)
    return result[0]
#订单的桌位
def getorderTableid(orderid):
    sql = "SELECT tableid FROM xt_dc_order WHERE id = {}".format(orderid)
    result = connectMysql(sql)
    return result[0]

#支付完成后订单状态
def getStatus(orderid):
    sql = "SELECT status FROM xt_dc_order WHERE id = {}".format(orderid)
    result = connectMysql(sql)
    return result[0]
