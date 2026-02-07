from duckduckgo_search import DDGS
from config import cfg

class Tools:
    def search(self, query):
        try:
            results = DDGS().text(query, max_results=3)
            return "\n".join([f"{r['title']}: {r['href']}" for r in results])
        except:
            return "Search unavailable"

    def write_file(self, name, content):
        path = cfg.WORKSPACE / name
        with open(path, 'w') as f:
            f.write(content)
        return f"Saved to {name}"
