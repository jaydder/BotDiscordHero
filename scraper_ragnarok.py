from typing import Dict, List

import requests
from bs4 import BeautifulSoup


class RagnarokItemScraper:
    def __init__(self, id):
        self.url = f"https://site.heroragnarok.com/?module=item&action=view&id={id}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def fetch_page(self) -> str:
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()

            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a página: {e}")
            return None

    def extract_item_values(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")
        items = []

        table = soup.find("table", class_="shops-table")

        if table:
            rows = table.find_all("tr")[1:]

            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    try:
                        loja_name = cols[0].get_text(strip=True)
                        quantidade = cols[3].get_text(strip=True)
                        refino = cols[1].get_text(strip=True)
                        type_value = cols[5].get_text(strip=True)
                        qtd = cols[4].get_text(strip=True)

                        if loja_name:
                            items.append(
                                {
                                    "loja": loja_name,
                                    "quantidade_rops": quantidade,
                                    "refino": refino,
                                    "type_value": type_value,
                                    "qtd": qtd,
                                }
                            )
                    except (IndexError, AttributeError):
                        continue

        return items
