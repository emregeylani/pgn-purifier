import sys

def remove_braced_blocks(text, open_char, close_char):
    result = []
    depth = 0
    for c in text:
        if c == open_char:
            depth += 1
        elif c == close_char:
            if depth > 0:
                depth -= 1
            continue
        elif depth == 0:
            result.append(c)
    return ''.join(result)

def clean_pgn(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove everything inside {}, (), and []
    content = remove_braced_blocks(content, '{', '}')
    content = remove_braced_blocks(content, '(', ')')
    content = remove_braced_blocks(content, '[', ']')

    # Remove annotations like !, ?, !!, ??, ?!, !?
    content = content.replace('!', '').replace('?', '')

    tokens = content.replace('\n', ' ').split()
    moves = []

    for token in tokens:
        if token.endswith('.'):
            continue
        elif token in ['1-0', '0-1', '1/2-1/2', '*']:
            moves.append(token)
        else:
            moves.append(token)

    result = []
    move_number = 1
    i = 0
    while i < len(moves):
        if i + 1 < len(moves):
            result.append(f"{move_number}. {moves[i]} {moves[i+1]}")
            i += 2
        else:
            result.append(f"{move_number}. {moves[i]}")
            i += 1
        move_number += 1

    final_output = ' '.join(result)

    with open('output_cleaned.pgn', 'w', encoding='utf-8') as f:
        f.write(final_output)

    print(“The cleaned PGN has been written to the file ‘output_cleaned.pgn’.”)
  
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(“Usage: python purify.py <pgn_file>”)
    else:
        clean_pgn(sys.argv[1])
