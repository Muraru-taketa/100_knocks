#51. 特徴量抽出
'''
学習データ，検証データ，評価データから特徴量を抽出し，
それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ． 
なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
'''
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def a_apples():

    filenames = ['train.txt' ,'valid.txt' ,'test.txt']
    apple = []
    #TfidfVectorizer
    vec_tfidf = TfidfVectorizer()

    #データ読み込み
    for filename in filenames:
        file_path='./'+str(filename)
        df = pd.read_csv(file_path, header=None, sep='\t', names=['TITLE', 'CATEGORY'])
        apple.append(df.TITLE)
    dataframe = pd.concat(apple)
    vec_tfidf.fit(dataframe)

    #ベクトル化
    t_train = vec_tfidf.transform(apple[0])
    t_valid = vec_tfidf.transform(apple[1])
    t_test = vec_tfidf.transform(apple[2])

    #ベクトルをデータフレーム化
    X_train = pd.DataFrame(t_train.toarray(), columns=vec_tfidf.get_feature_names())
    X_valid = pd.DataFrame(t_valid.toarray(), columns=vec_tfidf.get_feature_names())
    X_test = pd.DataFrame(t_test.toarray(), columns=vec_tfidf.get_feature_names())
    
    #保存
    X_train.to_csv('./train.feature.txt', sep='\t', index=False)
    X_valid.to_csv('./valid.feature.txt', sep='\t', index=False)
    X_test.to_csv('./test.feature.txt', sep='\t', index=False)

    return filenames

if __name__ == "__main__":
    filenames = a_apples()

    #print(X_train.head())
