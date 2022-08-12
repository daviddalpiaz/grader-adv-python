# %%

import pandas as pd 

df = pd.DataFrame({
    "id":[1, 2, 3], 
    "height": ["tall", "small", "normal"]},
    index=["JJB", "H", "X"]
)

descriptors = df.agg([lambda s: s.dtype])
descriptors.index = ["dtype"]
other = (descriptors.style
         .applymap(lambda v: "font-weight: bold;"))
styler = (df.style
            .set_table_styles([{"selector": ".foot_row0",
                                "props": "border-top: 1px solid black;"}]))
styler.concat(other)



# %%
