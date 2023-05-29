import openai # Instalar libreria (pip install openai)
import config
import typer # https://typer.tiangolo.com/  # Para una mejor visualizacion de interfaz 
from  rich import print # github.com/textualize/rich
from rich.table import Table

def main():

    openai.api_key = config.APY_KEY

    print("[bold blue]Mi version de ChatGPT[/bold blue]")

    # CONTEXTO ASISTENTE
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)   
    messages = [{"role":"system", 
                "content":"Eres un asistente muy útil. En programacion"}]
    while True:
        
        contenido = _prompt()

        messages.append({"role":"user", "content":contenido})

        respondeAPI = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages) # Modelos para utilizar (https://platform.openai.com/docs/models)
        
        responde_contenido = respondeAPI.choices[0].message.content 
        messages.append({"role":"assistant", "content":responde_contenido})

        print(f"[bold green]> [/bold green] [green]{responde_contenido}[/green]")


def _prompt() -> str:
    prompt = typer.prompt("¿Que te gustaria saber? ")
    if prompt == "exit":
        exit = typer.confirm("¿Estas seguro?")
        if exit:
            raise typer.Abort()
    
        return _prompt()
    return prompt

if __name__ == "__main__":
    typer.run(main)