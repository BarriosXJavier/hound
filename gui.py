import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from functools import partial
from . import main


def search(output_text, search_query_var):
    search_query = search_query_var.get()
    if search_query:
        main.search_google(search_query, output_text)


def create_gui():
    root = tk.Tk()
    root.title("Google Search")

    search_query_var = tk.StringVar()
    output_text = ScrolledText(root, wrap=tk.WORD, width=50, height=20)
    output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    tk.Label(root, text="Search Query: ").grid(
        row=0, column=0, padx=10, pady=5)
    entry_query = tk.Entry(root, textvariable=search_query_var)
    entry_query.grid(row=0, column=1, padx=10, pady=5)

    search_partial = partial(search, output_text, search_query_var)
    btn_search = tk.Button(root, text="Search", command=search_partial)
    btn_search.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
