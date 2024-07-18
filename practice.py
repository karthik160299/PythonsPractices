import click
from ollama import Qwen2

@click.command()
@click.option('-t', '--text', help='Input text or text file for summarization', required=True)
def summarize_text(text):
    qwen2_model = Qwen2()
    text_content = _read_text_content(text)
    summary = qwen2_model.summarize(text_content)
    click.echo(f'Summary: {summary}')

def _read_text_content(text_or_file):
    if text_or_file.endswith('.txt'):
        with open(text_or_file, 'r') as file:
            return file.read()
    else:
        return text_or_file

if __name__ == '__main__':
    summarize_text()