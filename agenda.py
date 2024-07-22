import os

def get_contacts_file_path():
    """
    Retorna o caminho absoluto para o arquivo de contatos.
    """
    return os.path.join(os.path.dirname(__file__), "contacts.txt")

def add_contact(name, address, phone_num):
    """
    Adiciona um contato ao arquivo.

    Args:
        name (str): Nome do contato.
        address (str): Endereço do contato.
        phone_num (str): Número de telefone do contato.
    """
    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone_num}\n"
    with open(get_contacts_file_path(), "a", encoding="utf-8") as file:
        file.write(contact + "\n")

def view_contacts():
    """
    Lê e retorna todos os contatos do arquivo.

    Returns:
        str: Lista de contatos ou mensagem indicando que a agenda está vazia.
    """
    if not os.path.exists(get_contacts_file_path()):
        return "Sua agenda de contatos está vazia."
    
    with open(get_contacts_file_path(), "r", encoding="utf-8") as file:
        return file.read()

def delete_contacts():
    """
    Exclui todos os contatos do arquivo.

    Returns:
        str: Mensagem de confirmação de exclusão ou indicação de agenda vazia.
    """
    if not os.path.exists(get_contacts_file_path()):
        return "Sua agenda de contatos está vazia."
    
    with open(get_contacts_file_path(), "w", encoding="utf-8") as file:
        file.write("")
    
    return "Seus contatos foram excluídos com sucesso."
