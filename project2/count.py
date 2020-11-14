with open('file.txt', 'r') as file:
    a = file.read().lower().strip().split()
    m = 0
    st = []
    for word in a:
        if a.count(word) > m:
            st.clear()
            m = a.count(word)
            st.append(word)
        elif a.count(word) == m and word not in st:
            st.append(word)
    if len(st) >1:
        print(min(st))
    else:
     print(*st, m)
