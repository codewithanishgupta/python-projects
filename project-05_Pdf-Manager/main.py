import os
import tkinter as tk
from tkinter import filedialog, messagebox

from pypdf import PdfWriter


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("700x420")
        self.root.minsize(550, 320)

        self.selected_files = []

        title = tk.Label(root, text="Merge multiple PDF files", font=("Arial", 14, "bold"))
        title.pack(pady=(20, 10))

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.select_button = tk.Button(
            button_frame,
            text="Select PDFs",
            width=18,
            command=self.select_pdfs,
            font=("Arial", 10, "bold"),
        )
        self.select_button.grid(row=0, column=0, padx=10)

        self.merge_button = tk.Button(
            button_frame,
            text="Merge PDFs",
            width=18,
            command=self.merge_pdfs,
            font=("Arial", 10, "bold"),
        )
        self.merge_button.grid(row=0, column=1, padx=10)

        list_label = tk.Label(root, text="Selected PDF files:")
        list_label.pack(anchor="w", padx=25)

        frame = tk.Frame(root)
        frame.pack(padx=25, pady=(5, 20), fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        footer = tk.Label(
            root,
            text="Choose your PDFs, then click Merge PDFs to save a combined file.",
            font=("Arial", 9),
            fg="gray20",
        )
        footer.pack(pady=(0, 20))

    def select_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not files:
            return

        self.selected_files = list(files)
        self.listbox.delete(0, tk.END)

        for file_path in self.selected_files:
            self.listbox.insert(tk.END, os.path.basename(file_path))

    def merge_pdfs(self):
        if not self.selected_files:
            messagebox.showwarning("No files selected", "Please choose at least one PDF file first.")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save merged PDF",
            defaultextension=".pdf",
            initialfile="merged.pdf",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not output_path:
            return

        writer = PdfWriter()

        try:
            for pdf_file in self.selected_files:
                writer.append(pdf_file)

            writer.write(output_path)
            writer.close()
            messagebox.showinfo("Success", f"Merged PDF saved to:\n{output_path}")
            self.listbox.delete(0, tk.END)
            self.selected_files = []
        except Exception as exc:
            messagebox.showerror("Merge failed", f"An error occurred while merging PDFs:\n{exc}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
