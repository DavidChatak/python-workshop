from flask import Flask, render_template, request,url_for
uygulama = Flask(__name__)

def converter(data):
    res=""
    if data < 1000:
        return f"{data} millisecond/s"
    else:
        res=""
        data=data//1000
        for i in ['second/s','minute/s','hour/s']:
            res=(f"{data%60} {i} ")*(data%60!=0)+res
            data=data//60
    return res
developer_name='David CHATAK'

@uygulama.route('/',methods=['GET'])
def anasayfa():
    return render_template('index.html',not_valid=False,developer_name=developer_name )

@uygulama.route('/',methods=['POST'])
def sonuc_hesapla():
    data=request.form['number']
    tip=f"{type(data)} is decimal?{data.isdecimal()}"
    
    
    if not data.isdecimal():
        return render_template('index.html',not_valid=True,developer_name=developer_name )
    else:
        data2=int(data)
        return render_template('result.html',tip=tip,not_valid=False,developer_name=developer_name,milliseconds=data,result=converter(data2))

if __name__ == '__main__':
    uygulama.run(host='0.0.0.0', debug=True,port=80)
