import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# score = [80, 55, 78, 99, 100, 34, 67, 77, 89, 100]
# bins = [0, 60, 80, 100]
# 
# result = pd.cut(score, bins)
# 
# labels = ['不及格', '中等', '优异']
# result = pd.cut(score, bins, labels=labels)
# =============================================================================

df = pd.read_excel("D:/d/csdn/1.xlsx")
df.fillna(0, inplace=True)

newDf = df[['target', 'score1']].copy() # 不能直接截取成新的df，构建新的df要copy
newDf.fillna(0, inplace=True)
newDf['id'] = df.index.values
# =============================================================================
# print(df.columns.values)
# =============================================================================
newDf.sort_values(by=['score1'], inplace=True)
# =============================================================================
# print(newDf.target)
# =============================================================================
labels = ['a', 'b', 'c', 'd', 'e']
newDf['result'] =pd.qcut(newDf.id, q=5, duplicates='drop')
counts = newDf['result'].value_counts()
# print(newDf['result'].value_counts())
# print(newDf['target'].value_counts())
print(type(counts))
print(counts)

groups = newDf.groupby('result')
# =============================================================================
# print(groups.groups)
# =============================================================================
# groups_a = groups.get_group('a')
# print(groups_a)
# cs = []
for name, group in groups:
    print(name)
#     # print(group)
#     # print(type(group))
#     # print(group.index.values)
#     # print(group.columns.values)
    item = group.target.value_counts(1)
    print(item)
#     print(group.shape)
#     print(item[0])
#     cs.append(group.shape[0] * item[0])
# print(cs)

# df = pd.DataFrame(cs, columns=['plot'])
# print(df)
# df.plot(kind='hist')
df = newDf.groupby(['result'])['target'].sum().reset_index()
print(df['target'])
df['target'].plot(kind='hist')
df['target'].plot(kind='line')
# df['target'].T.plot(kind='bar')


plt.show()