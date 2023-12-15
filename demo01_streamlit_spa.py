# Streamlit是一个用于创建数据应用的开源Python库。以下是一些基本的Streamlit组件的使用示例：
import streamlit as st

# 文本和数据
st.title('Streamlit 教程')
st.header('这是一个header')
st.subheader('这是一个subheader')
st.text('这是一些文本。')
st.markdown('**这是一些markdown**')
st.latex(r'\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i')  # LaTeX
st.write('这是一些文本，可以包含变量', 10)

# 数据
st.dataframe({'a': [1, 2, 3], 'b': [4, 5, 6]})  # pandas dataframe
st.table({'a': [1, 2, 3], 'b': [4, 5, 6]})  # static table

# 图形
st.line_chart({'a': [1, 5, 3], 'b': [4, 2, 6]})  # line chart
st.area_chart({'a': [1, 5, 3], 'b': [4, 2, 6]})  # area chart
st.bar_chart({'a': [1, 5, 3], 'b': [4, 2, 6]})  # bar chart
st.pyplot()  # matplotlib plot
st.altair_chart()  # altair plot
st.vega_lite_chart()  # vega lite plot
st.pydeck_chart()  # pydeck plot

# 交互
st.button('Button')
st.checkbox('Checkbox')
st.radio('Radio', [1, 2, 3])
st.selectbox('Selectbox', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])
st.slider('Slider', min_value=0, max_value=10)
st.select_slider('Select Slider', options=[1, 2, 3])
st.text_input('Text Input')
st.number_input('Number Input')
st.text_area('Text Area')
st.date_input('Date Input')
st.time_input('Time Input')
st.file_uploader('File Uploader')
st.color_picker('Color Picker')

# 其他
st.echo()  # echo code
st.spinner()  # spinner
st.balloons()  # balloons
st.error('Error message')  # error message
st.warning('Warning message')  # warning message
st.info('Info message')  # info message
st.success('Success message')  # success message
st.exception(RuntimeError('This is an exception'))  # exception

# 注意：以上代码中的一些函数需要传入特定的参数，这里只是为了展示函数的用法，可能无法直接运行。

# run: streamlit run demo.py