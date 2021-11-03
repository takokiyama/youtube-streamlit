import streamlit as st
import time

st.title("streamlit 超入門")

# st.write("DataFrame")

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )
# st.map(df)


st.write("プログレスバーの表示")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)
"Done!!!"

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字表示")
if button:
    right_column.write("右カラムだよ")

expander = st.beta_expander("うんちを漏らしてしまった")
expander.write("拭いてください")

text = st.sidebar.text_input("あなたの趣味を教えてください ")
condition = st.sidebar.slider("あなたの便意は？", 0, 100, 80)

"あなたの趣味は、", text, "です"
"ウンディション:" , condition

st.write("Display Image")
if st.checkbox("show Image"):
    img = Image.open("IMG_2311 (1).jpg")
    st.image(img, caption="Yuta Imai", use_column_width=True)

