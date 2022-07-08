# %%
# импорт библиотек

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# %%
###################################### дизайн страницы ######################################

# %%
# оформление страницы с дашбордом
st.title("Отчет UrgY")

# %%
###################################### рассчеты ######################################

# %%
# # для отладки
# df = pd.read_csv('/Users/arturfattahov/Downloads/Telegram Desktop/offers_statuses (3).txt', sep='|')


# для запуска
count_task = "offers_statuses (3).txt"
df = pd.read_csv(count_task, sep='|')

# %%
# обработка датафрейма
df = df.dropna()

df.columns = ['offer_id', 'offer_created_at','platform','count_responds', 'count_prematch']

df['offer_created_at'] = pd.to_datetime(df['offer_created_at'])
df.offer_created_at = df.offer_created_at.values.astype('M8[D]')

df['count_responds'] = df['count_responds'].astype(int)
df['count_prematch'] = df['count_prematch'].astype(int)

df['platform'] = df['platform'].str.strip()

# %%
# разделение даты
df_june = df[df['offer_created_at'] > '2022-05-31']
df_may = df[df['offer_created_at'] < '2022-05-31']

# %%
# общее количество задач
all_task_june = df_june['offer_id'].nunique()
all_task_may = df_may['offer_id'].nunique()

# разниа в количестве задач
difference_task = all_task_june - all_task_may


# %%
# количество созданных задач в мобльном приложении
task_mobile_may = df_may.query('platform == "android"').count()[0] + df_may.query('platform == "ios"').count()[0]
task_mobile_june = df_june.query('platform == "android"').count()[0] + df_june.query('platform == "ios"').count()[0]

# %%
# общее количество созданных задач по платформам

count_task_platform_june = (
    df_june
    .pivot_table(index=["platform"], values='offer_id', aggfunc='count'))

count_task_platform_june = count_task_platform_june.reset_index()
count_task_platform_june.columns = ['platform', 'count_task']

count_task_platform_june = count_task_platform_june.query('platform != "''"')

# %%


# %%


# %%


# %%


# %%


# %%
###################################### отображение элементов ######################################

# %%
# создание круговой диаграммы [Распределение задач по платформе]
# создание круговой диаграммы [Распределение задач по платформе]
st.subheader("Количество созданных задач")

fig = px.pie(
    count_task_platform_june,
    values='count_task',
    names='platform',
    title='Распределение задач по платформе',
    labels={
                "platform": "Платформа",  "count_task": "Количество задач"
            })

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Количество созданных задач, июнь", value=all_task_june, delta=difference_task)
with col2:
    st.plotly_chart(fig)

# %%



