import ast

def extract_genres(genre_str):
    """Extract genre names from the JSON-like string."""
    try:
        genres = ast.literal_eval(genre_str)
        return [g['name'] for g in genres if 'name' in g]
    except (ValueError, SyntaxError):
        return []
