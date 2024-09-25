m_list = []
for i in range(9):
    m_list.append(int(input()))
print(max(m_list))
print(m_list.index(max(m_list))+1)