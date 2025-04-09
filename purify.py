import sys
import re

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

    # Split content into tokens (moves and results)
    tokens = content.replace('\n', ' ').split()
    moves = []
    result = None

    for token in tokens:
        # If we encounter a result (1-0, 0-1, 1/2-1/2), save it to append later
        if token in ['1-0', '0-1', '1/2-1/2']:
            result = token
        elif not token.endswith('.'):
            moves.append(token)

    # Combine the moves into a clean sequence with move numbers
    cleaned_moves = []
    move_number = 1
    i = 0
    while i < len(moves):
        if i + 1 < len(moves):
            cleaned_moves.append(f"{move_number}. {moves[i]} {moves[i+1]}")
            i += 2
        else:
            cleaned_moves.append(f"{move_number}. {moves[i]}")
            i += 1
        move_number += 1

    # Join all cleaned moves into the final output
    final_output = ' '.join(cleaned_moves)

    # Append the result (if any) only once at the end of the PGN
    if result:
        final_output += f' {result}'

    # Write the cleaned PGN to a file
    with open('output_cleaned.pgn', 'w', encoding='utf-8') as f:
        f.write(final_output)

    print("The cleaned PGN has been written to the file ‘output_cleaned.pgn’.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python purify.py <pgn_file>")
    else:
        clean_pgn(sys.argv[1])
