import streamlit as st
st.title("Kalki is The SAviour of the World")
#title of the page -h6 format 
st.header("prabhas is the Bhairava and KArna in The saga KALKI 4898AD")
#Header will display in the h5 format
st.subheader("Prabhas is a bounty hunter and his bounty is  sum80 -->")
# sub header will display in tthe h4 format
st.write("Kalki is the last avatar of Lord Vishnu and he is the saviour of the world")
#write will display the text in h2 format


## displaying the data
##Text DAta

st.text("hello ,vanakkam ,adab ,namaste nenu mee nagarjunaa") #h1 format 
st.caption("ragada,king,manmadhudu")#grey color coded text
st.markdown("# prabhas") # single line markdown

#for multi line markdoen use triple quotes

st.markdown(""" # Prabhas \n## yaskin
                \n### Ashwathama
                \n#### karna
                \n##### Bhairava
                \n###### Kalki 
""",unsafe_allow_html=True)

st.markdown("""# <span style='color:blue'>Prabhas</span>""",unsafe_allow_html=True)

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

### st.metrics
st.metric("KALKI Revenue", "1000 CR")
st.metric("KALKI Revenue", "1000", "1800 cr")
st.metric("killbill Revenue", "1000", "800 cr",delta_color="inverse")

