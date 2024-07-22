import tkinter as tk
from tkinter import messagebox
from agenda import add_contact, view_contacts, delete_contacts

def add_contact_gui():
    """
    Coleta dados dos campos de entrada e adiciona um contato.
    Se os campos estiverem vazios, exibe um aviso.
    """
    name = name_entry.get()
    address = address_entry.get()
    phone_num = phone_entry.get()
    
    if name and address and phone_num:
        add_contact(name, address, phone_num)
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
        # Limpa os campos de entrada após adicionar o contato
        name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

def view_contacts_gui():
    """
    Atualiza o widget de texto com a lista de contatos.
    """
    contacts = view_contacts()
    contacts_text.delete("1.0", tk.END)  # Limpa o conteúdo atual
    contacts_text.insert(tk.END, contacts)  # Insere a lista de contatos

def delete_contacts_gui():
    """
    Solicita confirmação antes de excluir todos os contatos.
    Se confirmado, exclui e limpa o widget de texto.
    """
    response = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir todos os contatos?")
    if response:
        message = delete_contacts()
        messagebox.showinfo("Informação", message)
        contacts_text.delete("1.0", tk.END)  # Limpa o conteúdo após exclusão

# Configuração da janela principal
root = tk.Tk()
root.title("Agenda de Contatos")

# Criação dos widgets para adicionar contatos
tk.Label(root, text="Nome:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Endereço:").grid(row=1, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1)

tk.Label(root, text="Telefone:").grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

tk.Button(root, text="Adicionar Contato", command=add_contact_gui).grid(row=3, columnspan=2)

# Criação do widget para visualizar contatos
tk.Button(root, text="Listar Contatos", command=view_contacts_gui).grid(row=4, columnspan=2)
contacts_text = tk.Text(root, width=50, height=10)
contacts_text.grid(row=5, columnspan=2)

# Criação do widget para remover contatos
tk.Button(root, text="Remover Contatos", command=delete_contacts_gui).grid(row=6, columnspan=2)

# Inicia o loop da interface gráfica
root.mainloop()
