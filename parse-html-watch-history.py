import sys
import csv
from colorama import Fore, Style
from bs4 import BeautifulSoup
from tqdm import tqdm


def extract_links_and_titles(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    divs = soup.find_all('div', {'class': 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1'})
    
    links_and_titles = []

    with tqdm(total=len(divs), desc="Extracting", ncols=100) as pbar:
        for cell in divs:
            link_tag = cell.find('a', href=True)
            if link_tag:
                youtube_link = link_tag['href']
                title = ' '.join(link_tag.stripped_strings)
                links_and_titles.append([youtube_link, title])
            pbar.update(1)

    return links_and_titles


def read_file(file_path):
    encodings = ['utf-8', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return (file.read(), encoding)
        except UnicodeDecodeError:
            print(f"{Fore.YELLOW}Failed to read file with encoding {encoding}. Trying next encoding...{Style.RESET_ALL}")
    raise UnicodeDecodeError(f"Failed to read file with encodings: {', '.join(encodings)}")


def parse_html(input_file, output_file, resume=False):
    contents, encoding = read_file(input_file)

    print(f"{Fore.GREEN}Reading HTML complete.{Style.RESET_ALL}")
    
    # extracting the data
    data = extract_links_and_titles(contents)

    print(f"{Fore.GREEN}Writing to file.{Style.RESET_ALL}")
    
    # writing to csv file
    with open(output_file, 'w', newline='', encoding=encoding) as file:
        writer = csv.writer(file)
        writer.writerow(["Youtube Link", "Title"])

        for pair in data:
            writer.writerow([pair[0], pair[1]])
    print(f"{Fore.GREEN}Writing complete.{Style.RESET_ALL}")


def main(input_file, output_file):
    parse_html(input_file, output_file, resume=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])