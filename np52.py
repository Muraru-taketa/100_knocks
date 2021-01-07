#np52.py
"""
51で構築した学習データを用いて、ロジスティック回帰モデルを学習せよ。
"""
import np51

filenames = np51.a_apples

from sklearn.linear_model import LogisticRegression
#モデルの学習
lg = LogisticRegression(random_state=123, max_iter=10000)
lg.fit(t_train, train['CATEGORY'])

