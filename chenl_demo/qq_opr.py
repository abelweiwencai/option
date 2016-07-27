# -*- coding: utf-8 -*-
import DBUtil

__author__ = 'cl'
#篮子股票操作，录入基础数据

from WindPy import *
#w.start();#命令超时时间为120秒
w.start(waitTime=60);#命令超时时间设置成60秒
print w.isconnected();#即判断WindPy是否已经登陆成功

############
#starttime='2016-03-01';
#endtime='2016-03-31';
#starttime='2016-05-09';
starttime='2016-06-21';
endtime='2016-06-21';
#几月合约控制
t_yf="6"
#stock_id='10000523';
#STOCK_market='10000523.SH';

sql = "select t.trade_code from PM_QQ_CONFIG t where t_yf="+t_yf+" and t.is_enable=1 order by trade_code"
map_res=DBUtil.executeQueryList(sql)
print(map_res)

# update_sql_base="update PM_QQ_CONFIG t set t.xq_price=#xq_price#,t.xq_fx=#xq_fx# where t.trade_code='#trade_code#' and t.t_yf="+t_yf
# for i in map_res:
#     stock_id = i[0]
#     STOCK_market = stock_id+'.SH'
#     data =w.wsd(STOCK_market,"exe_price,exe_mode",starttime, starttime)
#     #print data;
#     exe_price = data.Data[0][0];
#     exe_mode = data.Data[1][0];
#     print str(exe_price)+","+exe_mode
#     xq_fx="-1"
#     if exe_mode==u'认购' :
#         xq_fx="1"
#     update_sql=update_sql_base.replace("#trade_code#", stock_id).replace('#xq_price#', str(exe_price)).replace('#xq_fx#', xq_fx)
#     print update_sql
#     DBUtil.executeUpdate(update_sql)

#方便多种操作
# flag_data=True
# if flag_data :
#     w.stop();
#     exit(0)


###
sql_del_model = "delete from PM_QQ_DATE where TRADE_CODE='#stock_id#' and LAST_TRADE_DAY>=to_date('#start_date#','yyyy-mm-dd') and LAST_TRADE_DAY<=to_date('#end_date#','yyyy-mm-dd')"
for i in map_res:
    stock_id = i[0]
    sql_del = sql_del_model.replace("#stock_id#", stock_id).replace('#start_date#', starttime).replace("#end_date#", endtime)
    print sql_del
    DBUtil.executeUpdate(sql_del)

####
sql_insert_model = "insert into PM_QQ_DATE(SYS_INT_ID,LAST_TRADE_DAY,TRADE_CODE,SEC_NAME,US_IMPLIEDVOL,THEORYVALUE,DELTA,GAMMA,VEGA,THETA,PTMTRADEDAY,UNDERLYINGHISVOL_30D,PRE_CLOSE,OPEN,CLOSE,HIGH,LOW,VOLUME,SWING,CHG,VWAP) " \
                   "values(stock_object_seq.nextval,to_date('#update_date#','yyyy-mm-dd'),'#TRADE_CODE#','#SEC_NAME#',#US_IMPLIEDVOL#,#THEORYVALUE#,#DELTA#,#GAMMA#,#VEGA#,#THETA#,#PTMTRADEDAY#,#UNDERLYINGHISVOL_30D#,#PRE_CLOSE#,#OPEN#,#CLOSE#,#HIGH#,#LOW#,#VOLUME#,#SWING#,#CHG#,#VWAP#)"

for i in map_res:
    stock_id = i[0]
    STOCK_market = stock_id+'.SH'
    data =w.wsd(STOCK_market,"trade_code,sec_name,us_impliedvol,theoryvalue,delta,gamma,vega,theta,ptmtradeday,underlyinghisvol_30d,pre_close,open,close,high,low,volume,swing,chg,vwap",starttime, endtime)
    print data;
    for d in range(len(data.Times)):
        update_date = data.Times[d].strftime("%Y-%m-%d")
        TRADE_CODE = data.Data[0][d];
        SEC_NAME = data.Data[1][d];
        #US_IMPLIEDVOL,THEORYVALUE,DELTA,GAMMA,VEGA,THETA,PTMTRADEDAY,UNDERLYINGHISVOL_30D,PRE_CLOSE,OPEN,CLOSE,HIGH,LOW,VOLUME,SWING,CHG,VWAP
        US_IMPLIEDVOL = data.Data[2][d];
        THEORYVALUE = data.Data[3][d];
        DELTA = data.Data[4][d];
        GAMMA = data.Data[5][d];
        VEGA = data.Data[6][d];
        THETA = data.Data[7][d];
        PTMTRADEDAY = data.Data[8][d];
        UNDERLYINGHISVOL_30D = data.Data[9][d];
        PRE_CLOSE = data.Data[10][d];
        OPEN = data.Data[11][d];
        CLOSE = data.Data[12][d];
        HIGH = data.Data[13][d];
        LOW = data.Data[14][d];
        VOLUME = data.Data[15][d];
        SWING = data.Data[16][d];
        CHG = data.Data[17][d];
        VWAP = data.Data[18][d];

        if CHG == None :
            continue;

        sql_insert = sql_insert_model.replace("#TRADE_CODE#", TRADE_CODE).replace('#update_date#', update_date).replace("#SEC_NAME#", SEC_NAME).replace("#US_IMPLIEDVOL#", str(US_IMPLIEDVOL))\
            .replace("#THEORYVALUE#", str(THEORYVALUE)).replace("#DELTA#", str(DELTA)).replace("#GAMMA#", str(GAMMA)).replace("#VEGA#", str(THEORYVALUE)).replace("#THEORYVALUE#", str(VEGA))\
            .replace("#THETA#", str(THETA)).replace("#PTMTRADEDAY#", str(PTMTRADEDAY)).replace("#UNDERLYINGHISVOL_30D#", str(UNDERLYINGHISVOL_30D)).replace("#PRE_CLOSE#", str(PRE_CLOSE))\
            .replace("#OPEN#", str(OPEN)).replace("#CLOSE#", str(CLOSE)).replace("#HIGH#", str(HIGH)).replace("#LOW#", str(LOW)).replace("#VOLUME#", str(VOLUME)).replace("#SWING#", str(SWING))\
            .replace("#CHG#", str(CHG)).replace("#VWAP#", str(VWAP))

        print sql_insert
        DBUtil.executeUpdate(sql_insert)



#'.Data=[[-2.7224435591]]  需要除以100
#w_wsd_data = w.wss("000063.SZ", "pct_chg_per","startDate=20160401;endDate=20160411")
#print w_wsd_data;




#####################
w.stop();
print '测试_end';