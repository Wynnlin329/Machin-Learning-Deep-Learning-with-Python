from keras.layers import SimpleRNN,Dropout,Dense
import numpy as np
from keras.utils import np_utils
np.random.seed(10)
from keras.datasets import mnist
from keras.models import Sequential

#建立訓練資料和測試資料，包括訓練特徵集、訓練標籤和測試特徵集、測試標籤	
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()  

#將 Features 特徵值換為 60000*28*28 的 3 維矩陣
train_feature_vector =train_feature.reshape(len(train_feature),28,28).astype('float32')
test_feature_vector = test_feature.reshape(len(test_feature),28,28).astype('float32')

#Features 特徵值標準化
train_feature_normalize = train_feature_vector/255
test_feature_normalize = test_feature_vector/255

#label 轉換為 One-Hot Encoding 編碼
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

# 建立簡單的線性執行的模型
model = Sequential()
# 加入 SimpleRNN 層
model.add(SimpleRNN(
    # input_shape=(TIME_STEPS, INPUT_SIZE)
    # TIME_STEPS 讀取次數，INPUT_SIZE 每次讀取多少個像素
    input_shape=(28, 28), 
    units=256, # 隱藏層：256 個神經元
    unroll=True, #計算時展開結構
)) 

# Dropout層防止過度擬合，拋棄比例:0.1
model.add(Dropout(0.1))

# 輸出層
model.add(Dense(units=10, kernel_initializer='normal', activation='softmax'))

# 這些訓練會累積，準確會愈來愈高
try:
    model.load_weights("Mnist_Rnn_model.weight")
    print("載入模型參數成功，繼續訓練模型!")
except :    
    print("載入模型失敗，開始訓練一個新模型!")
   
#定義訓練方式:選擇損失函數、優化方法及成效衡量方式
model.compile(loss='categorical_crossentropy', 
              optimizer='adam', metrics=['accuracy'])

#以(train_feature_normalize,train_label_onehot)資料訓練，
#訓練資料保留 20% 作驗證,訓練10次、每批次讀取200筆資料，顯示簡易訓練過程
train_history =model.fit(x=train_feature_normalize,
                         y=train_label_onehot,validation_split=0.2, 
                         epochs=10, batch_size=200,verbose=2)    

#評估準確率
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print('\n準確率=',scores[1])
    
#將模型儲存至 HDF5檔案中
model.save('Mnist_Rnn_model.h5')
print("Mnist_Rnn_model.h5 模型儲存完畢!")
model.save_weights("Mnist_Rnn_model.weight")
print("模型參數儲存完畢!")

del model  
    