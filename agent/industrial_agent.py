from __future__ import annotations
import os

def multiline_prompt():
    print('MULTILINE PROMPT MODE — type /end on a new line to submit, /cancel to cancel.')
    lines=[]
    while True:
        line=input('> ')
        if line.strip()=='/cancel': return None
        if line.strip()=='/end': return '\n'.join(lines).strip()
        lines.append(line)

def files_prompt():
    print('Enter local text files one per line; /end when done.')
    chunks=[]
    while True:
        p=input('file> ').strip()
        if p=='/end': break
        if not p: continue
        try: chunks.append(f'\n--- FILE: {p} ---\n'+open(p,encoding='utf-8').read())
        except Exception as exc: print(f'Could not read {p}: {exc}')
    note=input('Request for these files (optional): ').strip()
    return note+'\n'+''.join(chunks)

def main():
    print('Industrial AI Diagnostic Agent — PUBLIC DEMO')
    print('Mode: READ ONLY / synthetic telemetry')
    print('Commands: /paste /files /clear /exit')
    history=[]
    while True:
        q=input('\nYou: ').strip()
        if q=='/exit': break
        if q=='/clear': history.clear(); print('History cleared.'); continue
        if q=='/paste': q=multiline_prompt() or ''; print(f'Captured {len(q)} characters.')
        elif q=='/files': q=files_prompt()
        if not q: continue
        history.append(q)
        print('\nPublic demo shell captured the request.')
        print('Connect your preferred LLM/tool-calling runtime here; sample read-only tools are in mcp/read_only_tools.py.')

if __name__=='__main__': main()
