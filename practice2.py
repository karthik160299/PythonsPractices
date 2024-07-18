import click
from ollama import Qwen2

@click.command()
@click.option('-t', '--text', help='Input text or text file for summarization')
def summarize_text(text):
    qwen2_model = Qwen2()
    if text.endswith('.txt'):
        with open(text, 'r') as file:
            text_content = file.read()
        summary = qwen2_model.summarize(text_content)
    else:
        summary = qwen2_model.summarize(text)
    
    click.echo(f'Summary: {summary}')

if __name__ == '__main__':
    summarize_text()
