import os
import tkinter as tki
import tkinter.filedialog as fd
from tkinter.ttk import Treeview
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')



massstart = []
mas = []
db = pd.DataFrame()

def start(root):

    def opennextwindov():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        MainWind(root)

    root["bg"] = "SkyBlue1"
    lbl1 = tki.Label(
        root,
        text="Нажмите старт для работы с БД",
        font=(
            'Times',
            24,
            'bold'),
        bg='SkyBlue1')
    lbl1.grid(column=1, row=0, pady=100, padx=400)
    btn = tki.Button(
        root,
        text='Старт',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=opennextwindov)
    btn.grid(column=1, row=1)
    massstart = [lbl1, btn]


tabl1 = []
tabl2 = []
tabl3 = []
tabl4 = []


def MainWind(root):
    global db

    def ready():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        global db
        db = pd.read_csv("SavedBD.csv", sep=";")
        DataWindow(root)
    def newwin():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        tabl1.append("Data/tabl1.csv")
        tabl2.append("Data/tabl2.csv")
        tabl3.append("Data/tabl3.csv")
        tabl4.append("Data/tabl4.csv")
        global db
        db = pd.read_csv(tabl1[-1], sep=';') \
            .merge(pd.read_csv(tabl2[-1], sep=';'), on='Н_ПРО') \
            .merge(pd.read_csv(tabl3[-1], sep=';'), on='Н_ПРО') \
            .merge(pd.read_csv(tabl4[-1], sep=';'), on='Н_ЖАНР') \
            .drop(columns=['Н_ПРО', 'Н_ЖАНР']).sort_values(by='Н_АКТЁР', ascending=True)
        DataWindow(root)

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        start(root)

    def newwinifopened():
        if tabl1 == [] or tabl2 == [] or tabl3 == [] or tabl4 == []:
            print("Ещё не всё")
        else:
            for i in massstart:
                if i.winfo_viewable():
                    i.grid_remove()
                else:
                    i.grid()
            global db

            db = pd.read_csv(tabl1[-1], sep=';') \
                .merge(pd.read_csv(tabl2[-1], sep=';'), on='Н_ПРО') \
                .merge(pd.read_csv(tabl3[-1], sep=';'), on='Н_ПРО') \
                .merge(pd.read_csv(tabl4[-1], sep=';'), on='Н_ЖАНР') \
                .drop(columns=['Н_ПРО', 'Н_ЖАНР']).sort_values(by='Н_АКТЁР', ascending=True)
            DataWindow(root)

    def choose_file():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl1.append(filename)

    def choose_file2():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl2.append(filename)

    def choose_file3():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl3.append(filename)

    def choose_file4():
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=(("CSV файл", "*.csv"),))
        tabl4.append(filename)

    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)

    lbl1 = tki.Label(
        root,
        text="Используйте готовую или загрузите по отдельности БД",
        font=(
            'Times',
            24,
            'bold'),
        bg='SkyBlue1')
    lbl1.grid(column=1, row=0, padx=100)
    btnchoose1 = tki.Button(
        root,
        text='Выбрать личные данные',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file)

    btnchoose1.grid(column=0, row=1, pady=40, ipadx=18)
    btnchoose2 = tki.Button(
        root,
        text='Проекты',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file2)
    btnchoose2.grid(column=0, row=2, pady=40, ipadx=88)
    btnchoose3 = tki.Button(
        root,
        text='Номер проекта',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file3)
    btnchoose3.grid(column=0, row=3, pady=40, ipadx=62)
    btnchoose4 = tki.Button(
        root,
        text='Жанры',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=choose_file4)
    btnchoose4.grid(column=0, row=4, pady=40, ipadx=96)
    btnusingready = tki.Button(
        root,
        text='Использовать готовую БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=newwin)
    btnusingready.grid(column=1, row=2, pady=40)
    btnusingready1 = tki.Button(
        root,
        text='Создать свою БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=newwinifopened)
    btnusingready1.grid(column=1, row=3, pady=40, ipadx=40)
    btnusingready2 = tki.Button(
        root,
        text='Загрузить готовую',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=ready)
    btnusingready2.grid(column=1, row=4, pady=40, ipadx=40)

    massstart = [btn, btnchoose1, lbl1, btnchoose2, btnchoose3, btnchoose4, btnusingready, btnusingready1,
                 btnusingready2]


def DataWindow(root):
    global db
    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        MainWind(root)

    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)

    def to_window_report():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        Reports(root)

    to_reports = tki.Button(root,
                            text='К отчётам',
                            font=(
                                'Times',
                                14,
                                'bold'),
                            background='cyan1',
                            fg='black',
                            command=to_window_report)
    to_reports.grid(column=0, row=1, ipadx=81)

    def to_redact():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        RedactWindow(root)

    btn_redact = tki.Button(
        root,
        text='Редактировать базу данных',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=to_redact
    )



    btn_redact.grid(column=0, row=2, ipadx=4)
    tree = Treeview(root)
    db_col = list(db.columns)
    verscrlbar = tki.Scrollbar(root,
                               orient="vertical",
                               command=tree.yview)
    tree["columns"] = db_col
    tree['show'] = 'headings'
    for i in range(len(db_col)):
        tree.column(db_col[i], width=25, anchor='c')
        tree.heading(db_col[i], text=str(db_col[i]))
    for k in range(len(db)):
        tree.insert("", 'end', values=(list(db.iloc[k])))
    tree.grid(column=2, row=10, ipadx=200)
    verscrlbar.grid(column=3, row=10, ipady=86)
    tree.configure(yscrollcommand=verscrlbar.set)
    massstart = [btn, to_reports, verscrlbar, tree, btn_redact]


def Reports(root):
    global db

    def to_Graphs():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Graphs(root)

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        DataWindow(root)

    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)

    def stats_report():
        global db
        for i in mas:
            i.grid_remove()
        genre_min = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'min'}) \
            .rename(columns={'СТАЖ': 'Минимальный стаж'})
        genre_max = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'max'}) \
            .rename(columns={'СТАЖ': 'Максимальный стаж'})
        genre_std = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'std'}) \
            .rename(columns={'СТАЖ': 'Стандартное отклонение стажа'})
        genre_median = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'median'}) \
            .rename(columns={'СТАЖ': 'Медиана стажа'})
        genre_full = db.groupby('ЖАНР', as_index=False) \
            .agg({'СТАЖ': 'mean'}) \
            .rename(columns={'СТАЖ': 'Средний стаж'}) \
            .merge(genre_max, on='ЖАНР') \
            .merge(genre_min, on='ЖАНР') \
            .merge(genre_std, on='ЖАНР') \
            .merge(genre_median, on='ЖАНР')
        genre_full['Стандартное отклонение стажа'] = round(genre_full['Стандартное отклонение стажа'],2)
        genre_full['Медиана стажа'] = round(genre_full['Медиана стажа'], 2)
        genre_full['Средний стаж'] = round(genre_full['Средний стаж'], 2)
        tree3 = Treeview(root)
        db_col = list(genre_full.columns)
        tree3["columns"] = db_col
        tree3['show'] = 'headings'
        mas.append(tree3)
        for i in range(len(db_col)):
            tree3.column(db_col[i], width=25, anchor='c')
            tree3.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(genre_full)):
            tree3.insert("", 'end', values=(list(genre_full.iloc[k])))
        tree3.grid(column=5, row=10, ipadx=200)

    btn_stats = tki.Button(root,
                           text='Простая статистика БД',
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           command=stats_report)
    btn_stats.grid(column=1, row=4)

    def opensimple_report():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        simple_report(root)
    def create_pivot():
        global db
        for i in mas:
            i.grid_remove()
        pivot = db.groupby(['ФИО', 'ЖАНР'], as_index=False) \
            .agg({'ПРОЕКТ': 'count'}) \
            .pivot('ФИО', 'ЖАНР', 'ПРОЕКТ') \
            .fillna(0) \
            .reset_index()
        tree2 = Treeview(root)
        db_col = list(pivot.columns)
        verscrlbar2 = tki.Scrollbar(root,
                                    orient="vertical",
                                    command=tree2.yview)

        tree2["columns"] = db_col
        tree2['show'] = 'headings'
        for i in range(len(db_col)):
            tree2.column(db_col[i], width=25, anchor='c')
            tree2.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(pivot)):
            tree2.insert("", 'end', values=(list(pivot.iloc[k])))
        tree2.grid(column=5, row=10, ipadx=200)
        verscrlbar2.grid(column=3, row=10, ipady=86)
        tree2.configure(yscrollcommand=verscrlbar2.set)
        mas.append(tree2)
        mas.append(verscrlbar2)

    generate_pivot = tki.Button(root,
                                text="Сводная таблица",
                                font=(
                                    'Times',
                                    14,
                                    'bold'),
                                background='cyan1',
                                fg='black',
                                command=create_pivot)
    generate_pivot.grid(column=1, row=2, ipadx=27)

    to_simple = tki.Button(root,
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           text='Простой отчёт',
                           command=opensimple_report)
    to_simple.grid(column=1, row=1, ipadx=40)
    Graph_btn = tki.Button(root,
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='cyan1',
                           fg='black',
                           text='К графикам',
                           command=to_Graphs)
    Graph_btn.grid(column=1, row=3, ipadx=50)
    massstart = [btn, generate_pivot, to_simple, Graph_btn, btn_stats]


def simple_report(root):

    global db

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Reports(root)

    def clean():
        global db
        for i in mas:
            i.grid_remove()
        search_simple()

    def search_simple():
        global db
        tree3 = Treeview(root)
        verscrlbar2 = tki.Scrollbar(root,
                                    orient="vertical",
                                    command=tree3.yview)
        mas.append(tree3)
        mas.append(verscrlbar2)
        Needed_columns = ['Н_АКТЁР']
        if bolcb2.get() == True:
            Needed_columns.append(cb2.cget('text'))
        if bolcb3.get() == True:
            Needed_columns.append(cb3.cget('text'))
        if bolcb4.get() == True:
            Needed_columns.append(cb4.cget('text'))
        if bolcb5.get() == True:
            Needed_columns.append(cb5.cget('text'))
        if bolcb6.get() == True:
            Needed_columns.append(cb6.cget('text'))
        if bolcb7.get() == True:
            Needed_columns.append(cb7.cget('text'))

        db_simple = db[Needed_columns]

        db_col = list(db_simple.columns)
        tree3["columns"] = db_col
        tree3['show'] = 'headings'
        for i in range(len(db_col)):
            tree3.column(db_col[i], width=50, anchor='c', stretch=False)
            tree3.heading(db_col[i], text=str(db_col[i]))
        for k in range(len(db_simple)):
            tree3.insert("", 'end', values=(list(db_simple.iloc[k])))
        tree3.grid(column=2, row=10)
        verscrlbar2.grid(column=3, row=10, ipady=86)
        tree3.configure(yscrollcommand=verscrlbar2.set)

    bolcb2 = tki.BooleanVar()
    cb2 = tki.Checkbutton(text="ФИО", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb2)
    bolcb3 = tki.BooleanVar()
    cb3 = tki.Checkbutton(text="Д.Р.", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb3)
    bolcb4 = tki.BooleanVar()
    cb4 = tki.Checkbutton(text="ПОЛ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb4)
    bolcb5 = tki.BooleanVar()
    cb5 = tki.Checkbutton(text="СТАЖ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb5)
    bolcb6 = tki.BooleanVar()
    cb6 = tki.Checkbutton(text="ПРОЕКТ", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb6)
    bolcb7 = tki.BooleanVar()
    cb7 = tki.Checkbutton(text="ЖАНР", font=('Times', 14, 'bold'), background='SkyBlue1', variable=bolcb7)
    cb2.grid(column=0, row=2, sticky='W')
    cb3.grid(column=0, row=3, sticky='W')
    cb4.grid(column=0, row=4, sticky='W')
    cb5.grid(column=0, row=5, sticky='W')
    cb6.grid(column=0, row=6, sticky='W')
    cb7.grid(column=0, row=7, sticky='W')

    search = tki.Button(root,
                        text="Искать",
                        font=(
                            'Times',
                            14,
                            'bold'),
                        background='cyan1',
                        fg='black',
                        command=clean)
    search.grid(column=1, row=1)
    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)
    massstart = [btn, search, cb5, cb6, cb7, cb4, cb3, cb2]


def Graphs(root):
    global db

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        Reports(root)

    btn_back = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)

    def barplot():
        global db
        db_for_bar = db.groupby('ФИО', as_index=False) \
            .agg({'ПРОЕКТ': 'count'}) \
            .rename(columns={'ПРОЕКТ': 'Количество проектов'})
        sns.set(rc={'figure.figsize': (9, 5)})
        fig = plt.figure()
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('orange')
        ax.patch.set_alpha(1.0)
        sns.barplot(x=db_for_bar['ФИО'], y=db_for_bar['Количество проектов']) \
            .set(title='\nКоличество проектов актёра')
        plt.xticks(rotation=45)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
        if not os.path.exists('Graphs'):
            os.mkdir('Graphs')
        plt.savefig('Graphs/bar_plot.png')

    barplot_btn = tki.Button(root,
                             text='Построить Барплот',
                             font=(
                                 'Times',
                                 14,
                                 'bold'),
                             background='cyan1',
                             fg='black',
                             command=barplot)

    def histplot():
        global db
        fig = plt.figure()
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.histplot(x=db['ПРОЕКТ'], hue=db['ЖАНР']) \
            .set(title='\nКоличество актёров в проекте')
        plt.xticks(rotation=90)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
        if not os.path.exists('Graphs'):
            os.mkdir('Graphs')
        plt.savefig('Graphs/hist_plot.png')

    histplot_btn = tki.Button(root,
                              text='Построить Хистплот',
                              font=(
                                  'Times',
                                  14,
                                  'bold'),
                              background='cyan1',
                              fg='black',
                              command=histplot)

    def boxplot():
        global db
        fig = plt.figure()
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.boxplot(x=db['ЖАНР'], y=db['СТАЖ']) \
            .set(title='\nСтаж актёров по жанрам')
        plt.xticks(rotation=45)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
        if not os.path.exists('Graphs'):
            os.mkdir('Graphs')
        plt.savefig('Graphs/box_plot.png')

    boxlot_btn = tki.Button(root,
                            text='Построить Боксплот',
                            font=(
                                'Times',
                                14,
                                'bold'),
                            background='cyan1',
                            fg='black',
                            command=boxplot)

    def scatter():
        global db
        fig = plt.figure()
        fig.patch.set_facecolor('blue')
        fig.patch.set_alpha(0.6)
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('none')
        ax.patch.set_alpha(1.0)
        sns.scatterplot(x=db['Д.Р.'], y=db['СТАЖ'], hue=db['ПОЛ']) \
            .set(title='\nВзаимосвязь даты рождения и стажа актёров')
        plt.xticks(rotation=45)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=6, column=3)
        mas.append(canvas.get_tk_widget())
        if not os.path.exists('Graphs'):
            os.mkdir('Graphs')
        plt.savefig('Graphs/Scatter_plot.png')
    scatter_btn = tki.Button(root,
                             text='Построить Скаттер-плот',
                             font=(
                                 'Times',
                                 14,
                                 'bold'),
                             background='cyan1',
                             fg='black',
                             command=scatter)
    btn_back.grid(column=0, row=0, ipadx=100)
    barplot_btn.grid(column=0, row=1, ipadx=41)
    histplot_btn.grid(column=0, row=2, ipadx=36)
    boxlot_btn.grid(column=0, row=3, ipadx=36)
    scatter_btn.grid(column=0, row=4, ipadx=18)
    massstart = [btn_back, barplot_btn, histplot_btn, boxlot_btn, scatter_btn]


def RedactWindow(root):
    global db

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        for i in mas:
            i.grid_remove()
        db.to_csv("Output/SavedBD.csv", sep=";",index=False)
        DataWindow(root)

    def to_add():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        AddWindow(root,tree_edit)

    btn_add = tki.Button(
        root,
        text='Добавить в базу данных',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=to_add
    )
    btn_add.grid(column=0, row=5, ipadx=21)
    btn_back = tki.Button(
        root,
        text='Назад и сохранить БД',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    tree_edit = Treeview(root)
    db_col = list(db.columns)
    verscrlbar = tki.Scrollbar(root,
                               orient="vertical",
                               command=tree_edit.yview)
    tree_edit["columns"] = db_col
    tree_edit['show'] = 'headings'
    for i in range(len(db_col)):
        tree_edit.column(db_col[i], width=25, anchor='c')
        tree_edit.heading(db_col[i], text=str(db_col[i]))
    for k in range(len(db)):
        tree_edit.insert("", 'end', values=(list(db.iloc[k])))
    tree_edit.grid(column=2, row=10, ipadx=200)
    verscrlbar.grid(column=3, row=10, ipady=86)
    tree_edit.configure(yscrollcommand=verscrlbar.set)
    btn_back.grid(column=0, row=0, ipadx=100)

    def delete():
        global db
        selected = tree_edit.selection()
        for i in selected:
            tree_edit.delete(i)
        values = []
        new_db = pd.DataFrame(columns=['Н_АКТЁР', 'ФИО', 'Д.Р.', 'ПОЛ', 'СТАЖ', 'ПРОЕКТ', 'ЖАНР'])
        for line in tree_edit.get_children():
            for value in tree_edit.item(line)['values']:
                values.append(value)
        for i in range(0, len(values), 7):
            new_row = {'Н_АКТЁР': values[i], 'ФИО': values[i + 1], 'Д.Р.': values[i + 2],
                       'ПОЛ': values[i + 3], 'СТАЖ': values[i + 4], 'ПРОЕКТ': values[i + 5], 'ЖАНР': values[i + 6]}
            new_db = new_db.append(new_row, ignore_index=True)
        db = new_db
    btn_delete = tki.Button(
        root,
        text='Удалить выбранное',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=delete)
    btn_delete.grid(column=1, row=0)
    massstart = [btn_back, btn_delete, btn_add, tree_edit, verscrlbar]


def AddWindow(root,tree):
    global db

    def pred():
        for i in massstart:
            if i.winfo_viewable():
                i.grid_remove()
            else:
                i.grid()
        RedactWindow(root)

    def add(tree):
        global db
        values = []
        values.append(text_number_entry.get())
        values.append(message_entry.get())
        values.append(message_entry_date.get())
        values.append(message_entry_sex.get())
        values.append(message_entry_years.get())
        values.append(message_entry_project.get())
        values.append(message_entry_type.get())
        tree.insert("", 'end', values=values)
        full_data = []
        new_db = pd.DataFrame(columns=['Н_АКТЁР', 'ФИО', 'Д.Р.', 'ПОЛ', 'СТАЖ', 'ПРОЕКТ', 'ЖАНР'])
        for line in tree.get_children():
            for value in tree.item(line)['values']:
                full_data.append(value)
        for i in range(0, len(full_data), 7):
            new_row = {'Н_АКТЁР': full_data[i], 'ФИО': full_data[i + 1], 'Д.Р.': full_data[i + 2],
                       'ПОЛ': full_data[i + 3], 'СТАЖ': full_data[i + 4], 'ПРОЕКТ': full_data[i + 5], 'ЖАНР': full_data[i + 6]}
            new_db = new_db.append(new_row, ignore_index=True)
        db = new_db

    btn = tki.Button(
        root,
        text='Назад',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=pred)
    btn.grid(column=0, row=0, ipadx=100)
    btn_add = tki.Button(
        root,
        text='Добавить',
        font=(
            'Times',
            14,
            'bold'),
        background='cyan1',
        fg='black',
        command=lambda:add(tree))
    btn_add.grid(column=0, row=1, ipadx=84)
    text_number = tki.Label(root,
                            text="Введите номер актёра",
                            font=(
                                'Times',
                                14,
                                'bold'),
                            background='SkyBlue1',
                            fg='black'
                            )
    text_number_entry = tki.Entry(root,
                                  textvariable=tki.StringVar(),
                                  font=(
                                      'Times',
                                      14,
                                      'bold'),
                                  background='cyan1',
                                  fg='black')
    text_number.grid(column=1, row=0)
    text_number_entry.grid(column=1, row=1)
    text_fio = tki.Label(root,
                         text="Введите ФИО",
                         font=(
                             'Times',
                             14,
                             'bold'),
                         background='SkyBlue1',
                         fg='black'
                         )
    text_fio.grid(column=1, row=2)
    message_entry = tki.Entry(root,
                              textvariable=tki.StringVar(),
                              font=(
                                  'Times',
                                  14,
                                  'bold'),
                              background='cyan1',
                              fg='black')
    message_entry.grid(column=1, row=3)
    text_date = tki.Label(root,
                          text="Введите дату рождения актёра",
                          font=(
                              'Times',
                              14,
                              'bold'),
                          background='SkyBlue1',
                          fg='black'
                          )
    text_date.grid(column=1, row=4)
    message_entry_date = tki.Entry(root,
                                   textvariable=tki.StringVar(),
                                   font=(
                                       'Times',
                                       14,
                                       'bold'),
                                   background='cyan1',
                                   fg='black')
    message_entry_date.grid(column=1, row=5)
    text_sex = tki.Label(root,
                         text="Введите пол",
                         font=(
                             'Times',
                             14,
                             'bold'),
                         background='SkyBlue1',
                         fg='black'
                         )
    text_sex.grid(column=1, row=6)
    message_entry_sex = tki.Entry(root,
                                  textvariable=tki.StringVar(),
                                  font=(
                                      'Times',
                                      14,
                                      'bold'),
                                  background='cyan1',
                                  fg='black')
    message_entry_sex.grid(column=1, row=7)
    text_years = tki.Label(root,
                           text="Введите стаж актёра",
                           font=(
                               'Times',
                               14,
                               'bold'),
                           background='SkyBlue1',
                           fg='black'
                           )
    text_years.grid(column=1, row=8)
    message_entry_years = tki.Entry(root,
                                    textvariable=tki.StringVar(),
                                    font=(
                                        'Times',
                                        14,
                                        'bold'),
                                    background='cyan1',
                                    fg='black')
    message_entry_years.grid(column=1, row=9)
    text_project = tki.Label(root,
                             text="Проект",
                             font=(
                                 'Times',
                                 14,
                                 'bold'),
                             background='SkyBlue1',
                             fg='black'
                             )
    text_project.grid(column=1, row=10)
    message_entry_project = tki.Entry(root,
                                      textvariable=tki.StringVar(),
                                      font=(
                                          'Times',
                                          14,
                                          'bold'),
                                      background='cyan1',
                                      fg='black')
    message_entry_project.grid(column=1, row=11)
    text_type = tki.Label(root,
                          text="Введите жанр",
                          font=(
                              'Times',
                              14,
                              'bold'),
                          background='SkyBlue1',
                          fg='black'
                          )
    text_type.grid(column=1, row=12)
    message_entry_type = tki.Entry(root,
                                   textvariable=tki.StringVar(),
                                   font=(
                                       'Times',
                                       14,
                                       'bold'),
                                   background='cyan1',
                                   fg='black')
    message_entry_type.grid(column=1, row=13)
    btn.grid(column=0, row=0, ipadx=100)
    global massstart
    massstart = [btn, message_entry, text_fio, message_entry_date, text_date, message_entry_sex, text_sex,
                 message_entry_years, text_years, message_entry_project, text_project, message_entry_type, text_type,
                 btn_add,text_number,text_number_entry]
