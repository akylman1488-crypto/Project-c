import ctypes
import json
import os
import numpy as np
from config import cfg

class Memory:
    def __init__(self):
        lib_name = "./memory_core.so"
        self.lib = ctypes.CDLL(lib_name)
        self.lib.find_best_match.restype = ctypes.c_int
        self.data = []
        self.vectors = []
        self.load()

    def add(self, text):
        vec = np.random.rand(128).tolist() 
        self.data.append(text)
        self.vectors.append(vec)
        self.save()

    def recall(self, query_vec=None):
        if not self.data: return "Memory Empty"
        if not query_vec: query_vec = np.random.rand(128).tolist()
        
        c_query = (ctypes.c_double * 128)(*query_vec)
        flat = np.array(self.vectors).flatten()
        c_db = (ctypes.c_double * len(flat))(*flat)
        
        idx = self.lib.find_best_match(c_query, c_db, len(self.data), 128)
        return self.data[idx] if idx != -1 else "Unknown"

    def save(self):
        with open(cfg.MEMORY_FILE, 'w') as f:
            json.dump({'data': self.data, 'vectors': self.vectors}, f)

    def load(self):
        if cfg.MEMORY_FILE.exists():
            with open(cfg.MEMORY_FILE, 'r') as f:
                d = json.load(f)
                self.data = d['data']
                self.vectors = d['vectors']
