#!/usr/bin/env python3

from utils import check_dependencies
from search import search

def main():
    check_dependencies()
    print("✅ Semua dependency tersedia")
    print("CLI Audio Player 🎧 already used")

    query = input("Search: ").strip()
    if not query:
        print("❌ Search tidak boleh kosong")
        return
    
    print("🔍 Mencari...")
    results = search(query)

    if not results:
        print("❌ Tidak ada hasil")
        return
    
    print("\nHasil:")
    for i, item in enumerate(results, start=1):
        print(f"{i}. {item['title']}")

if __name__ == "__main__":
    main()