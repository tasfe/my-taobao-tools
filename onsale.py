#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.
# 出售商品

from util.base import *

class ListHandler(handler):
    def get(self):
        onsale=items.onsale()
        page=self.request.get('page').isdigit() and int(self.request.get('page')) or 1
        rows=self.request.get('rows').isdigit() and int(self.request.get('rows')) or 20
        datagrid=[onsale[value[0]] for value in items.onsale_sort()[(page-1)*rows:page*rows]]
        self.response.out.write(simplejson.dumps({'total':len(onsale),'rows':datagrid}))

class ReportHandler(handler):
    def get(self):
        report=memcache.get('onsale_report',base.user())
        if type(report) is not types.DictType:
            max=[0 for k in range(4)]
            min=[86400 for k in range(4)]
            data=[{} for k in range(4)]
            error=[]
            datagrid=[]
            footer=[]
            for value in items.onsale_sort()+items.instock_regular():
                if value[1]%300>0:
                    error.append(value[0])
                else:
                    tmp1=value[1]%86400//21600
                    tmp2=value[1]%86400
                    tmp3=int(time.strftime('%w',time.gmtime(value[1])))
                    if not data[tmp1].has_key(tmp2):
                        data[tmp1][tmp2]=[0 for k in range(7)]
                    data[tmp1][tmp2][tmp3]+=1
                    if max[tmp1]<tmp2:
                        max[tmp1]=tmp2
                    if min[tmp1]>tmp2:
                        min[tmp1]=tmp2
            for tmp1 in range(4):
                if min[tmp1]<max[tmp1]:
                    total=[0 for k in range(7)]
                    datagrid.append({'Time':[u'凌晨',u'上午',u'下午',u'傍晚'][tmp1],'Sun':'','Mon':'','Tus':'','Wen':'','Thur':'','Fri':'','Sat':''})
                    for tmp2 in range(min[tmp1],max[tmp1]+1,300):
                        period='%s:%s'%(str(tmp2//3600).zfill(2),str(tmp2%3600//60).zfill(2))
                        if data[tmp1].has_key(tmp2):
                            for tmp3 in range(7):
                                if data[tmp1][tmp2][tmp3]>0:
                                    total[tmp3]+=data[tmp1][tmp2][tmp3]
                                else:
                                    data[tmp1][tmp2][tmp3]='-'
                            datagrid.append({'Time':period,'Sun':data[tmp1][tmp2][0],'Mon':data[tmp1][tmp2][1],'Tus':data[tmp1][tmp2][2],'Wen':data[tmp1][tmp2][3],'Thur':data[tmp1][tmp2][4],'Fri':data[tmp1][tmp2][5],'Sat':data[tmp1][tmp2][6]})
                        else:
                            datagrid.append({'Time':period,'Sun':'-','Mon':'-','Tus':'-','Wen':'-','Thur':'-','Fri':'-','Sat':'-'})
                    footer.append({'Time':[u'凌晨合计',u'上午合计',u'下午合计',u'傍晚合计'][tmp1],'Sun':total[0],'Mon':total[1],'Tus':total[2],'Wen':total[3],'Thur':total[4],'Fri':total[5],'Sat':total[6]})
            report={'data':simplejson.dumps({'total':len(datagrid),'rows':datagrid,'footer':footer}),'error':simplejson.dumps({'total':len(error),'rows':error})}
            memcache.set('onsale_report',report,600,0,base.user())
        if self.request.get('action')=='error':
            self.response.out.write(report['error'])
        else:
            self.response.out.write(report['data'])

def main():
    application=webapp.WSGIApplication([
                                        (r'/onsale/list.*',ListHandler),
                                        (r'/onsale/report.*',ReportHandler),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()