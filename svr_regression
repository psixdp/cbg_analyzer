# -*- coding: utf-8 -*-

from sklearn.svm import SVR
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
import csv
import config_heros

def load_data(path):
    csv_file=csv.reader(open(path,'r'))
    rows=[row for row in csv_file]
    # y=[0 for i in range(len(rows)-2)]
    # x=[[0 for i in range(len(rows[0])-1)] for i in range(len(rows)-2)]
    y=np.zeros(len(rows)-2)
    x=np.zeros((len(rows)-2,len(rows[0])-1))


    for i in range(2,len(rows)):
        y[i-2]=rows[i][0]
        x[i-2]=np.array(rows[i][1:])
    return {'label':y,'feature':x}
def get_star5_flag():
    hero_info=config_heros.get_config()['hero']
    flag=[]
    for i in range(len(hero_info)):
        if hero_info[i]['quality']==5:
            flag.append(i)
    return np.array(flag)

def template_svr(data):
    # rng = np.random
    # svr = joblib.load('svr.pkl')        # 读取模型

    # x = rng.uniform(1, 100, (100, 1))
    # y = 5 * x + np.sin(x) * 5000 + 2 + np.square(x) + rng.rand(100, 1) * 5000

    n_sample=len(data['label'])


    x=data['feature'][0:n_sample*9/10]
    y=data['label'][0:n_sample*9/10]
    # 自动选择合适的参数
    svr = GridSearchCV(SVR(), param_grid={"kernel": ("linear", 'rbf'), "C": np.logspace(-3, 3, 7),
                                          "gamma": np.logspace(-3, 3, 7)})
    # svr=SVR(kernel='rbf',C=1e3,gamma=1e-3)
    svr.fit(x, y)
    # joblib.dump(svr, 'svr.pkl')        # 保存模型

    xneed=data['feature'][n_sample*9/10+1:]
    yneed=data['label'][n_sample*9/10+1:]
    y_pre = svr.predict(xneed)  # 对结果进行可视化：
    # plt.scatter(x, y, c='k', label='data', zorder=1)
    # # plt.hold(True)
    # plt.plot(xneed, y_pre, c='r', label='SVR_fit')
    # plt.xlabel('data')
    # plt.ylabel('target')
    # plt.title('SVR versus Kernel Ridge')
    # plt.legend()
    # plt.show()
    # print(svr.best_params_)
    for i in range(len(y_pre)):
        print 'predicted:',y_pre[i]/100,'labeled:',yneed[i]/100
if __name__=="__main__"  :
    path='result/data_platform_1_909_samples_2019-03-24-02_40_48.csv'
    data=load_data(path)
    # template_svr(data)
    print data[1,get_star5_flag()]