import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
# import graphviz

st.title('超入門')

st.write('wigets')
'stert!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
    latest_iteration.text(f'Iteratuon {i+1}')
    time.sleep(1)
    bar.progress(i + 1)
    time.sleep(0.001)

'Done'

left_column, right_column = st.columns(2)
button = left_column.button('右に表示')
if button:
    right_column.write('aaa')

expander = st.expander('といあわせ')
expander.write('内容を書く')

text = st.text_input('おしえて')
'趣味は',text

text2 = st.slider('調子は',0 ,100, 50)
'condition',text2

option = st.selectbox(
    '好きな数字',
    list(range(1,11))
)

option2 = st.selectbox(
    '好きな数字は',
    list(range(1,11))
)

ans = option + option2
'すきな数字は',ans,'です'

if st.checkbox('show image'):
    img = Image.open('ダウンロード.png')
    st.image(img, caption='donut', use_column_width=True)
    st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

# st.write('DataFrame')



df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.65, 139.650],
    columns=['lat', 'lon']
    # np.random.rand(20, 3),
    # columns=['a','b','c']
    # '1列目':[1,2,3,4],
    # '2列目':[10,20,30,40]
)
st.map(df)

st.bar_chart(df)

st.area_chart(df)

st.line_chart(df)
# # st.dataframe(df.style.highlight_max(axis=0), width = 200, height=200)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### こう
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """