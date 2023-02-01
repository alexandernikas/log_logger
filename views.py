import streamlit as st
import stool_db as sdb
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
db = sdb.Database('store.db')



#ftb = sdb.Filter('store.db')
def update_stools():
    stoolList = []
    for row in db.fetch():
        stoolList.append(row)
    global stls
    stls = pd.DataFrame(stoolList, columns =['ID', 'Length', 'Girth','Volume','Bristol #','Date','Tags'])
update_stools()

def filter_stools(query):
    stoolsFiltered = []
    for row in db.filter_table(query):
        stoolsFiltered.append(row)
    global fstls
    fstls = pd.DataFrame(stoolsFiltered, columns =['ID', 'Length', 'Girth','Volume','Bristol #','Date','Tags'])

gb = GridOptionsBuilder.from_dataframe(stls)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()


def mainView():
        
    st.header("Stool Tracker")
    grid_response = AgGrid(
    stls,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='balham', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=False
    )
    #data = grid_response['data']
    selected = grid_response['selected_rows'] 
    sstls = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df
    try:
        pids = sstls['ID']
        pidList = list(pids)
    except KeyError:
        pidList = []
    print(pidList)
    if st.button("Drop Selected Rows"):
        for row in pidList:
            db.delete_row(row)
        st.success("Rows deleted")
        update_stools()
    if st.button("Drop Table"):
        db.clear_db()

        

