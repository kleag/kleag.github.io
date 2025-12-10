import os
import argparse
from pathlib import Path
from pybtex.database import parse_file

def sanitize_filename(text):
    """Sanitizes a string to be safe for use as a filename."""
    # Replace spaces with underscores and remove characters that are unsafe/unwanted in filenames
    text = text.replace(' ', '_')
    text = "".join(c for c in text if c.isalnum() or c in ('_', '-'))
    # Limit length to prevent issues
    return text[:100]

def determine_type(entry):
    """Determines a simpler publication type from the BibTeX entry type."""
    type_map = {
        'article': 'journal',
        'inproceedings': 'conference',
        'proceedings': 'conference',
        'phdthesis': 'thesis',
        'mastersthesis': 'thesis',
        'book': 'book',
        'incollection': 'book_chapter',
        'techreport': 'report',
    }
    return type_map.get(entry.type.lower(), 'misc')

def get_venue_and_short(entry, entry_type):
    """Extracts venue and a short venue name based on the entry type."""
    
    venue = ""
    venue_short = ""

    if entry_type in ['conference', 'report', 'misc']:
        # For conferences/reports, try 'booktitle' first, then 'journal'
        venue = str(entry.fields.get('booktitle', entry.fields.get('journal', '')))
    elif entry_type == 'journal':
        # For articles, use 'journal'
        venue = str(entry.fields.get('journal', ''))
    elif entry_type == 'book':
        # For books, use 'publisher' or 'title'
        venue = str(entry.fields.get('publisher', entry.fields.get('title', '')))

    # Attempt to derive a short name. This is heuristic.
    if venue:
        # Simple heuristic: use initials of the major words
        words = [w for w in venue.split() if w.lower() not in ['on', 'of', 'in', 'and', 'the']]
        if len(words) > 1 and all(w.isupper() for w in words):
            venue_short = venue # Assume it's already an acronym
        elif len(words) > 0:
            # Create an acronym from the first letters of capitalized words
            venue_short = "".join(w[0] for w in words if w[0].isupper()).upper()
            if not venue_short:
                 # Fallback for all lowercase titles
                 venue_short = "".join(w[0] for w in words[:4]).upper()
        
        # If the heuristic fails or is too short, use the first few words
        if len(venue_short) < 2 or len(venue_short) > 10:
            venue_short = " ".join(words[:2])


    # Simple cleanup of venue name
    venue = venue.strip().replace('\n', ' ')
    venue_short = venue_short.strip()

    return venue, venue_short

def format_authors(entry):
    """Formats the list of authors for the markdown file."""
    authors = []
    for person in entry.persons.get('author', []):
        # Join first/middle names and last names
        name = " ".join(person.first() + person.middle() + person.last())
        authors.append(f'  - {name.strip()}')
    return '\n'.join(authors)

def format_date(entry):
    """Formats the date as YYYY-MM-DD, using only year if month/day is missing."""
    year = entry.fields.get('year')
    month = entry.fields.get('month', '01')
    day = entry.fields.get('day', '01')

    # pybtex month values can be names or numbers; this handles names by converting to '01'
    try:
        if not str(month).isdigit():
            # A very simple way to handle month names, assuming January if not a number
            month_num = '01'
        else:
            month_num = str(month).zfill(2)
    except:
        month_num = '01' # Safety fallback

    # A simple date format, which might not be fully accurate but provides a placeholder
    return f"{year}-{month_num}-01" if year else 'YYYY-MM-DD'


def generate_markdown_content(entry, bibtex_key):
    """Generates the full markdown content for a publication."""
    title = str(entry.fields.get('title', f'Untitled Publication ({bibtex_key})')).replace('{', '').replace('}', '')
    year = entry.fields.get('year', 'UnknownYear')
    abstract = str(entry.fields.get('abstract', 'Explores the main themes of the publication.')).strip()
    doi = entry.fields.get('doi')
    url = entry.fields.get('url')
    
    # Determine type, venue, and authors
    pub_type = determine_type(entry)
    venue, venue_short = get_venue_and_short(entry, pub_type)
    authors_yaml = format_authors(entry)
    date_formatted = format_date(entry)

    # Construct the links block
    links = []
    if url:
        links.append(f'  paper: {url}')
    elif doi:
        links.append(f'  doi: https://doi.org/{doi}')

    links_yaml = '\n'.join(links)

    # The Markdown content structure
    markdown_template = f"""---
title: "{title}"
authors:
{authors_yaml}
date: {date_formatted}
venue: "{venue}"
venue_short: "{venue_short}"
type: {pub_type}
links:
{links_yaml}
---

{abstract}
"""
    return markdown_template

def process_bibtex_file(bibtex_path, output_dir):
    """Parses the BibTeX file and creates the directory and markdown structure."""
    
    # Check if the BibTeX file exists
    bibtex_file = Path(bibtex_path)
    if not bibtex_file.is_file():
        print(f"Error: BibTeX file not found at {bibtex_path}")
        return

    # Create the output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Parsing BibTeX file: {bibtex_file.name}")
    
    try:
        # Parse the BibTeX file
        # pybtex can often infer the encoding, but we'll try UTF-8 first
        bib_data = parse_file(str(bibtex_file), bib_format='bibtex')
    except Exception as e:
        print(f"Error parsing BibTeX file: {e}")
        return

    publications_processed = 0
    
    # Iterate over all entries in the BibTeX file
    for key, entry in bib_data.entries.items():
        try:
            # 1. Get the year and create the year directory
            year = entry.fields.get('year')
            if not year:
                print(f"Warning: Entry '{key}' missing year. Skipping.")
                continue

            year_dir = output_path / year
            year_dir.mkdir(exist_ok=True)

            # 2. Generate the markdown content
            markdown_content = generate_markdown_content(entry, key)

            # 3. Create a unique, sanitized filename
            # Use a sanitized version of the title and the BibTeX key
            title_safe = sanitize_filename(entry.fields.get('title', key))
            filename = f"{title_safe}.md"
            file_path = year_dir / filename
            
            # 4. Write the content to the markdown file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            publications_processed += 1
            # print(f"  -> Generated {file_path}")

        except Exception as e:
            print(f"An error occurred while processing entry '{key}': {e}")
            
    print(f"\n✅ Successfully processed {publications_processed} publication(s).")
    print(f"Output directory structure created at: {output_path.resolve()}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Convert a BibTeX file into a year-based directory structure with Markdown files."
    )
    parser.add_argument(
        "bibtex_file",
        type=str,
        help="Path to the input BibTeX (.bib) file."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="_publications",
        help="Name of the output directory. (Default: publications_output)"
    )
    
    args = parser.parse_args()
    process_bibtex_file(args.bibtex_file, args.output)

