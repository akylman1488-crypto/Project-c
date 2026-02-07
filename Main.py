import time
import json
import threading
from llm_engine import Brain
from memory_bridge import Memory
from tools import Tools
from config import cfg
import colorama

colorama.init(autoreset=True)

def get_network_sense():
    if cfg.REALTIME_DATA.exists():
        with open(cfg.REALTIME_DATA, 'r') as f:
            return f.read()
    return "{}"

def main():
    brain = Brain()
    mem = Memory()
    tools = Tools()
    
    print(colorama.Fore.GREEN + "AGI SYSTEM ONLINE")
    
    while True:
        user_in = input(colorama.Fore.CYAN + "You: ")
        if user_in.lower() in ['exit', 'quit']: break
        
        net_data = get_network_sense()
        past_mem = mem.recall()
        
        if "search" in user_in.lower():
            search_res = tools.search(user_in.replace("search", ""))
            context = f"Web: {search_res}\nNet: {net_data}\nMem: {past_mem}"
        else:
            context = f"Net: {net_data}\nMem: {past_mem}"
            
        response = brain.think(user_in, context)
        
        mem.add(f"User: {user_in} | AI: {response}")
        print(colorama.Fore.YELLOW + f"AGI: {response}")

if __name__ == "__main__":
    main()
